"""把工作流 JSON 转成 ComfyUI API prompt, 并可选择按最新 md 刷新 mdtable 控件状态。

目的: 不依赖前端, 改完 md 后直接提交工作流(拿到的就是最新提示词)。
机制: mdtable 的 execute 只吃控件状态 data, 而该状态由前端调 /fallingts_mdtable/read 同步;
      本脚本直接调同一接口取最新行, 因此无需"点击刷新"。

处理规则:
  - MarkdownNote / Note / Reroute 不进入 API prompt (Reroute 的下游引用解析为真实源);
  - widget 名按 /object_info 的 required+optional 顺序映射, 已被转为输入的 widget 跳过;
  - mode=4(bypass) 的节点按"透传"处理: 其下游引用解析到它的同名输入源。

用法:
  .venv\\Scripts\\python.exe scripts\\workflow-to-prompt.py "0032-*.json" [--refresh-md] [--submit] [--dump out.json]
"""

import glob
import json
import pathlib
import sys
import time
import urllib.parse
import urllib.request

API = "http://127.0.0.1:8188"
SKIP_TYPES = {"MarkdownNote", "Note", "Reroute"}
# COMFY_DYNAMICCOMBO_V3 = io.DynamicCombo(如 SaveVideo 的 format/format.codec): 值来自
# widgets_values, 不是连线输入; 漏掉它会让 format 不进 prompt, 执行时报
# `SaveVideo.execute() missing 1 required positional argument: 'format'`(采样已白跑)。
# LOAD_3D = 节点内的 3D 视口控件(Load3D.image / PreviewGaussianSplat.viewport_state /
# SaveGaussianSplat.viewport_state): 它同样住在 widgets_values 里, 后端只要一个状态字典;
# 不当控件处理会报 `Required input is missing: viewport_state`。
WIDGET_TYPES = ("INT", "FLOAT", "STRING", "BOOLEAN", "COMBO", "COMFY_DYNAMICCOMBO_V3", "LOAD_3D")
# 3D 视口控件在无头运行时没有前端状态, 给空字典即可(节点内部按 {} 取默认相机)。
VIEWPORT_TYPES = ("LOAD_3D",)
# 前端在 seed/noise_seed(以及 PrimitiveInt 的 value)后插入的控件, 后端定义里没有;
# 它占 widgets_values 的一个位置, 补进名字表以便对齐, 但不注入 prompt。
FRONTEND_CTRL = "\0control_after_generate"


def api_get(path: str, timeout: int = 180):
    with urllib.request.urlopen(API + path, timeout=timeout) as r:
        return json.load(r)


def api_post(path: str, payload: dict, timeout: int = 120):
    req = urllib.request.Request(
        API + path, data=json.dumps(payload).encode(), headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def widget_default(name: str, spec: dict) -> object:
    """控件缺 widgets_values 时的兜底值。

    前端的图形控件(如 ImageCompare 的 compare_view)不进 widgets_values, 但后端把它
    声明成 required, 直接提交会报 "Required input is missing: compare_view"。
    优先用声明里的 default; 没有就按类型给一个能通过校验的空值。
    """
    for sec in ("required", "optional"):
        d = (spec["input"].get(sec) or {}).get(name)
        if d is None:
            continue
        t = d[0] if isinstance(d, list) else d
        opt = d[1] if isinstance(d, list) and len(d) > 1 and isinstance(d[1], dict) else {}
        if "default" in opt:
            return opt["default"]
        if isinstance(t, list):
            return t[0] if t else ""
        return {"INT": 0, "FLOAT": 0.0, "STRING": "", "BOOLEAN": False}.get(t, {})
    return {}


def dynamic_children(spec: dict, combo_name: str, key) -> list:
    """动态下拉(COMFY_DYNAMICCOMBO_V3)选中项的子控件名。

    `CreateCameraInfo.mode='orbit'` 会多出 yaw/pitch/distance 三个控件; 它们不在
    /object_info 的 input 里, 只挂在 options[<key>].inputs 下 —— 按位置对齐时漏掉它们,
    其后的 target_x/target_y/... 会整体前移 (实测 fov 拿到 0、zoom 拿到 3.0)。
    """
    d = (spec["input"].get("required") or {}).get(combo_name) or (spec["input"].get("optional") or {}).get(combo_name)
    if not isinstance(d, list) or len(d) < 2 or not isinstance(d[1], dict):
        return []
    out = []
    for opt in d[1].get("options") or []:
        if opt.get("key") != key:
            continue
        for sec in ("required", "optional"):
            for ck in (opt.get("inputs", {}).get(sec) or {}):
                out.append(f"{combo_name}.{ck}")
    return out


def widget_names(spec: dict, class_type: str = "", values: list | None = None) -> list:
    """节点全部控件(非连线类型)输入名, 按前端序列化顺序。

    注意: 前端序列化的 widgets_values 与**全部** widget 一一对应 —— 即使某个 widget
    已被转成输入(有连线)它也仍占一个位置, 因此必须用完整列表 zip 后再过滤,
    否则会整体错位(如 PreviewImageSave 的 format 会拿到 filename_suffix 的值)。

    前端还会额外插入一个**后端不存在的** control_after_generate 控件, 且位置在
    seed 类控件**之后**而非数组末尾 —— 漏掉它会让其后的所有控件整体前移一格
    (实测 KSampler: sampler_name 拿到 steps 的值, denoise 拿到 scheduler 的值)。
    这里按前端规则补上同名占位, 由调用方跳过, 不注入 prompt。
    """
    names = []
    for sec in ("required", "optional"):
        for name, d in (spec["input"].get(sec) or {}).items():
            t = d[0] if isinstance(d, list) else d
            opt = d[1] if isinstance(d, list) and len(d) > 1 and isinstance(d[1], dict) else {}
            # 控件判定: 常见标量类型, 或选项表(COMBO), 或后端标了 socketless
            # (如 ImageCropV2 的 BOUNDING_BOX / ImageCompare 的 IMAGECOMPARE ——
            #  它们是节点内控件而非可连线插槽, 只看类型名会漏掉, 报
            #  "Required input is missing: crop_region")。
            is_widget = isinstance(t, list) or t in WIDGET_TYPES or opt.get("socketless")
            if is_widget:
                names.append(name)
                # 动态下拉的子控件跟着选中项出现, 必须按位置补进对齐表(见 dynamic_children)。
                if t == "COMFY_DYNAMICCOMBO_V3" and values is not None:
                    key = values[len(names) - 1] if len(names) - 1 < len(values) else None
                    names.extend(dynamic_children(spec, name, key))
                # 前端只在种子类控件与 PrimitiveInt 的 value 后追加该控件。
                if name in ("seed", "noise_seed") or (class_type == "PrimitiveInt" and name == "value"):
                    names.append(FRONTEND_CTRL)
    return names


def refresh_state(state: dict) -> dict:
    """按 md 文件刷新 mdtable 控件状态(等价于前端点「刷新」)。"""
    path = state.get("md_path")
    if not path:
        return state
    r = api_get("/fallingts_mdtable/read?path=" + urllib.parse.quote(str(path)))
    if not r.get("ok"):
        raise RuntimeError(f"读取 md 失败: {r.get('error')}")
    sid = (state.get("selected") or {}).get("id")
    row = next((x for x in r["rows"] if x.get("id") == sid), None)
    if row is None:
        raise RuntimeError(f"md 中找不到行: {sid}")
    new = dict(state)
    new["fields"] = r["fields"]
    new["selected"] = {"id": row["id"], "values": row["values"]}
    return new


def build(wf_path: str, refresh_md: bool):
    wf = json.loads(pathlib.Path(wf_path).read_text(encoding="utf-8"))
    nodes = {n["id"]: n for n in wf["nodes"]}
    links = {l[0]: l for l in wf.get("links", [])}
    oi = api_get("/object_info")

    def resolve(nid, slot):
        """Reroute / bypass 节点解析为真实数据源。"""
        n = nodes.get(nid)
        if n is None:
            return (nid, slot)
        if n["type"] == "Reroute":
            inp = (n.get("inputs") or [{}])[0]
            l = links.get(inp.get("link"))
            if l:
                return resolve(l[1], l[2])
        elif n.get("mode") == 4:
            # 旁路节点不进 prompt, 其输出须透传到同名(否则同类型)的已连输入;
            # 否则下游仍指向那个被跳过的 id, ComfyUI 校验时报 KeyError。
            outs = n.get("outputs") or []
            out = outs[slot] if slot < len(outs) else {}
            wired = [i for i in (n.get("inputs") or []) if i.get("link") is not None]
            src = next((i for i in wired if i.get("name") == out.get("name")), None)
            if src is None:
                src = next((i for i in wired if i.get("type") == out.get("type")), None)
            l = links.get(src["link"]) if src else None
            if l:
                return resolve(l[1], l[2])
        return (nid, slot)

    prompt = {}
    notes = []
    for n in wf["nodes"]:
        t = n["type"]
        nid = n["id"]
        if t in SKIP_TYPES:
            continue
        if n.get("mode") in (2, 4):
            notes.append(f"节点 {nid} {t} mode={n['mode']} (已跳过)")
            continue
        spec = oi.get(t)
        if not spec:
            notes.append(f"节点 {nid} 类型 {t} 未知, 已跳过")
            continue

        inputs = {}
        for inp in n.get("inputs") or []:
            lid = inp.get("link")
            if lid is None:
                continue
            l = links.get(lid)
            if not l:
                continue
            src_id, src_slot = resolve(l[1], l[2])
            inputs[inp["name"]] = [str(src_id), src_slot]

        if t == "FallingTSMarkDownTable":
            state = (n.get("widgets_values") or [{}])[0]

            def longest_field(st: dict) -> int:
                """取最长字段的长度作为提示词规模指标。

                字段名各表不同(场景提示词/视频提示词/...), 不能写死, 否则统计恒为 0。
                """
                vals = (st.get("selected") or {}).get("values") or {}
                return max((len(str(v)) for v in vals.values()), default=0)

            before = longest_field(state)
            if refresh_md:
                state = refresh_state(state)
            after = longest_field(state)
            notes.append(f"mdtable: 最长字段 {before} -> {after} 字符" + (" (已按 md 刷新)" if refresh_md else ""))
            inputs["data"] = state
        else:
            wv = n.get("widgets_values") or []
            all_names = widget_names(spec, t, wv)
            # widgets_values_named 以控件**名字**为键, 比位置可靠: 前端会把动态子控件
            # (如 BlockSparseAttention 的 selection.tau)一并写进 widgets_values, 而它根本
            # 不在 /object_info 里 —— 一旦按位置 zip, 它之后的控件全体前移一格
            # (实测 start_percent 拿到 1.3、min_tokens 拿到 "", 提交被 max/枚举校验拦下)。
            named = n.get("widgets_values_named")
            named = named if isinstance(named, dict) else {}
            linked_names = {i["name"] for i in (n.get("inputs") or []) if i.get("link") is not None}
            types_by_name = {}
            for sec in ("required", "optional"):
                for wn, wd in (spec["input"].get(sec) or {}).items():
                    types_by_name[wn] = wd[0] if isinstance(wd, list) else wd
            used = filled = by_pos = 0
            for idx, name in enumerate(all_names):
                if name == FRONTEND_CTRL:
                    continue
                # 动态下拉(COMFY_DYNAMICCOMBO_V3)的子控件被连线时, 父控件本身仍要注入选中项:
                # V3 执行期靠 `_expand_schema_for_dynamic` 把 "mode" + "mode.yaw" 收成
                # {"mode": {...}}; 漏掉父项会让子项原样进 kwarg, 报
                # `CreateCameraInfo.execute() got an unexpected keyword argument 'mode.yaw'`。
                is_dyn_parent = types_by_name.get(name) == "COMFY_DYNAMICCOMBO_V3"
                if any(lk == name or (not is_dyn_parent and lk.startswith(name + ".")) for lk in linked_names):
                    continue
                if name in named:
                    inputs[name] = named[name]
                elif idx < len(wv):
                    inputs[name] = wv[idx]
                    by_pos += 1
                else:
                    # 前端图形控件(如 compare_view)不进 widgets_values, 用兜底值补上。
                    inputs[name] = widget_default(name, spec)
                    filled += 1
                used += 1
            # 3D 视口控件(LOAD_3D): 前端状态是字典, 无头运行只有空串 —— 归一到 {} ,
            # 节点内部会据此取默认相机 (传给它的下游 RenderSplat.camera_info 因此为空)。
            for name in list(inputs):
                if types_by_name.get(name) not in VIEWPORT_TYPES:
                    continue
                val = inputs[name]
                if isinstance(val, str) and val.strip().startswith("{"):
                    try:
                        val = json.loads(val)
                    except ValueError:
                        val = {}
                inputs[name] = val if isinstance(val, dict) else {}
            # 动态子控件(BlockSparseAttention 的 selection.tau、SaveVideo 的 format.codec):
            # 后端按 "<父>.<子>" 作为**独立输入**收值, 但 /object_info 里根本不列它 ——
            # 只按对齐表注入会报 `Required input is missing: tau`(input_name=selection.tau)。
            # 名字表里有的、父名在对齐表内的一律补上; 父名不在表内的(纯前端控件)不碰。
            dyn = 0
            for name, val in named.items():
                if name in inputs or "." not in name or name in linked_names:
                    continue
                parent = name.split(".", 1)[0]
                if parent in all_names and parent not in linked_names:
                    inputs[name] = val
                    dyn += 1
            if len(wv) != len(all_names) or filled or dyn:
                fix = f"; 按名字取 {used - by_pos - filled} 个, 按位置取 {by_pos} 个" if named else ""
                fix += f", 动态子控件 {dyn} 个" if dyn else ""
                notes.append(f"节点 {nid} {t}: widgets_values {len(wv)} 个 vs 对齐表 {len(all_names)} 个 "
                             f"(差值含前端附加控件; 注入 {used} 个控件值, 其中 {filled} 个用默认值补齐{fix})")

        prompt[str(nid)] = {"class_type": t, "inputs": inputs}
    return prompt, notes


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    pat = args[0] if args else "*.json"
    refresh_md = "--refresh-md" in sys.argv
    submit = "--submit" in sys.argv
    dump = None
    if "--dump" in sys.argv:
        dump = sys.argv[sys.argv.index("--dump") + 1]

    files = sorted(glob.glob(str(pathlib.Path(r"D:\AI\Comfy\workflows") / pat)))
    if not files:
        print("未匹配到工作流")
        return 1
    wf = files[0]
    print(f"工作流: {pathlib.Path(wf).name}")

    prompt, notes = build(wf, refresh_md)
    print(f"转换完成: {len(prompt)} 个节点进入 API prompt")
    for x in notes:
        print("  .", x)

    if dump:
        pathlib.Path(dump).write_text(json.dumps(prompt, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"已导出 -> {dump}")

    if not submit:
        print("\n(dry-run; 加 --submit 真正提交)")
        return 0

    print("\n提交中...")
    t0 = time.time()
    try:
        resp = api_post("/prompt", {"prompt": prompt, "client_id": "dsh-auto"})
    except urllib.error.HTTPError as e:
        body = e.read().decode()
        print("提交失败:", body[:2000])
        # 校验错误按节点翻成人话: 否则只看到一整串 JSON, 定位不到是哪个控件错位。
        try:
            info = json.loads(body)
            types = {str(x["id"]): x.get("type") for x in
                     json.loads(pathlib.Path(wf).read_text(encoding="utf-8"))["nodes"]}
        except Exception:
            return 1
        for nid, err in (info.get("node_errors") or {}).items():
            print(f"  节点 {nid} ({types.get(str(nid), '?')}):")
            for item in err.get("errors", []):
                got = (item.get("extra_info") or {}).get("received_value")
                print(f"    - {item.get('details') or item.get('input_name')}: {item.get('message')}"
                      f"  (收到 {got!r})")
        return 1
    pid = resp.get("prompt_id")
    print(f"prompt_id = {pid}")

    while True:
        if time.time() - t0 > 1800:
            print("超时")
            return 1
        time.sleep(5)
        try:
            h = api_get(f"/history/{pid}", timeout=60)
        except Exception:
            continue
        if pid in h:
            st = h[pid].get("status", {})
            ok = st.get("status_str") == "success"
            print(f"结果: {'成功' if ok else '失败'}  用时 {time.time() - t0:.1f}s")
            if not ok:
                for name, data in st.get("messages", []):
                    if "error" in name:
                        print("  ", json.dumps(data, ensure_ascii=False)[:800])
            for nid, o in (h[pid].get("outputs") or {}).items():
                for kind in ("images", "videos", "gifs", "audio"):
                    for item in o.get(kind) or []:
                        if isinstance(item, dict) and item.get("filename"):
                            print(f"  输出: {item.get('subfolder','')}/{item['filename']}")
            return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
