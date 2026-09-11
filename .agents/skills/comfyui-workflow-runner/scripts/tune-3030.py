"""调参并提交 3030-OrbitSheets场景(避开 GUI 覆写: 直接改磁盘 + 经 API 提交)。

用法:
  .venv\\Scripts\\python.exe scripts\\tune-3030.py --wide off --detail off --shots 4 [--label ""] [--run]

参数留空表示不改动该项。--run 时调用 workflow-to-prompt.py 提交并等待。
"""

import glob
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(r"D:\Comfy")
WF = ROOT / "workflows"


def arg(name, default=None):
    return sys.argv[sys.argv.index(name) + 1] if name in sys.argv else default


def main() -> int:
    p = pathlib.Path(glob.glob(str(WF / "3030-*.json"))[0])
    d = json.loads(p.read_text(encoding="utf-8"))
    changed = []

    for n in d["nodes"]:
        wv = n.get("widgets_values")
        wvn = n.get("widgets_values_named")
        if not isinstance(wv, list):
            continue

        if n["type"] == "OrbitSheetsLocationPrompt":
            order = list(wvn.keys()) if wvn else ["location_description", "visual_style", "space",
                                                  "coverage", "rotation", "take_seconds",
                                                  "wide_establishing_shot", "detail_shot",
                                                  "shot_seconds", "time_of_day", "ambient_sound"]
            for flag, key in (("--wide", "wide_establishing_shot"), ("--detail", "detail_shot")):
                v = arg(flag)
                if v is None or key not in order:
                    continue
                new = v.lower() in ("on", "true", "1", "yes")
                wv[order.index(key)] = new
                if wvn:
                    wvn[key] = new
                changed.append(f"{key}={new}")
            # 文本类参数: coverage / rotation / space
            for flag, key in (("--coverage", "coverage"), ("--rotation", "rotation"), ("--space", "space")):
                v = arg(flag)
                if v is None or key not in order:
                    continue
                wv[order.index(key)] = v
                if wvn:
                    wvn[key] = v
                changed.append(f"{key}={v}")

        elif n["type"] == "OrbitSheetsFrameSelect":
            # 关键: widgets_values 的槽位顺序 = widgets_values_named 的键顺序,
            # 而不是 object_info 的输入顺序(后者含 images/clip 等非控件输入, 会整体错位)。
            order = list(wvn.keys()) if wvn else []
            for a, key in (("--shots", "shots"), ("--count", "count"), ("--candidates", "candidates")):
                v = arg(a)
                if v is None:
                    continue
                if key not in order:
                    print(f"  [warn] {key} 不在 named 键里, 跳过")
                    continue
                wv[order.index(key)] = int(v)
                wvn[key] = int(v)
                changed.append(f"{key}={v}")

        elif n["type"] == "OrbitSheetsContactSheet":
            # PowerShell 会吞掉空字符串参数, 故提供 --label-empty 显式清空
            order = list(wvn.keys()) if wvn else ["columns", "cell_width", "padding",
                                                  "label_frames", "label_prefix"]
            v = "" if "--label-empty" in sys.argv else arg("--label")
            key = "label_prefix"
            if v is not None and key in order:
                wv[order.index(key)] = v
                if wvn:
                    wvn[key] = v
                changed.append(f"{key}={v!r}")

    if not changed:
        print("未指定任何参数(示例: --wide off --detail off --shots 4 --count 4 --label \"\")")
        return 1

    text = json.dumps(d, ensure_ascii=False, separators=(",", ":"))
    # 无 BOM 写入(ComfyUI 不能解析带 BOM 的 JSON)
    p.write_text(text, encoding="utf-8")
    print(f"已更新 {p.name}: {', '.join(changed)}")

    # 复核
    d2 = json.loads(p.read_text(encoding="utf-8"))
    for n in d2["nodes"]:
        if n["type"].startswith("OrbitSheets"):
            print(f"  [{n['id']}] {n['type']}: {json.dumps(n.get('widgets_values'), ensure_ascii=False)}")

    if "--run" in sys.argv:
        print("\n提交中...")
        subprocess.run(
            [str(ROOT / ".venv" / "Scripts" / "python.exe"),
             str(ROOT / "scripts" / "workflow-to-prompt.py"), "3030-*.json", "--refresh-md", "--submit"],
            cwd=str(ROOT), check=False,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
