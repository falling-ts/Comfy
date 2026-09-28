# 工作流 JSON → API prompt 转换规则

## 两种格式的差异

| | 工作流 JSON（前端保存） | API prompt（`POST /prompt`） |
|---|---|---|
| 顶层 | `{"nodes": [...], "links": [...]}` | `{"<node_id>": {"class_type", "inputs"}}` |
| 节点标识 | 数字 `id` | 字符串键 |
| 连线表达 | `links` 数组 + 节点 `inputs[].link` | 输入值直接写 `["<源节点id>", <源槽位>]` |
| 控件值 | `widgets_values` 数组 | 按控件**名**写入 `inputs` |

## 转换步骤

1. 建 `nodes = {id: node}` 与 `links = {link_id: [id, src_node, src_slot, dst_node, dst_slot, type]}`。
2. **跳过** `MarkdownNote` / `Note`（纯前端）。
3. **解析 `Reroute`**：它没有 `class_type`，下游对它的引用必须递归回溯到它的输入源；
   否则那些输入会没有连线（`filename_prefix` 之类会丢失）。
4. 对每个节点：
   - 连线输入：`inputs[inp.name] = [str(src_id), src_slot]`（经 Reroute 解析后）
   - 控件值：见下一节
5. `mode == 2/4` 的节点：跳过并报告（bypass 节点在 API 图里不存在，其直通语义需要另行展开）。

## 控件值映射（最容易出错的一步）

**首选按名字取**。前端保存的工作流里通常带 `widgets_values_named`（以控件名为键的镜像），
用它映射就不受位置错位影响：

```python
for idx, name in enumerate(控件名列表):
    if name in 已连线控件名:
        continue
    if name in widgets_values_named:      # 首选
        inputs[name] = widgets_values_named[name]
    elif idx < len(widgets_values):       # 兜底
        inputs[name] = widgets_values[idx]
```

**没有名字表时才按位置 zip，且必须用完整列表 zip、再过滤**。原因：前端序列化 `widgets_values` 时，
被转成输入的控件**仍然占位**。

反例（错误做法）：先过滤出"未连线控件名"再 zip → 整体前移，例如

```
PreviewImageSave 定义: filename_prefix, filename_suffix, format, bit_depth, input_color_space
widgets_values      : ['preview', '前面', 'png', '8-bit', 'sRGB', None]
filename_prefix 有连线（应跳过）
先过滤再 zip  → filename_suffix='preview', format='前面', bit_depth='png', ...   ← 全错且不报错
完整列表 zip  → filename_prefix='preview'(跳过), filename_suffix='前面', format='png', ...  ← 正确
```

## 前端附加控件

`widgets_values` 可能比节点定义**更长**，多出的是前端附加控件（如 seed 旁的 `control_after_generate`、
预览节点的 UI 状态）。按定义长度 zip 会自然忽略尾部多余项；**但**若某个前端控件插在中间，映射仍会错位 ——
此时应对照 `/object_info` 的定义顺序逐项核对。

## 动态子控件（`<父>.<子>`）

`COMFY_DYNAMICCOMBO_V3` 会按父控件的取值**动态展开子控件**。子控件在 `/object_info` 里**完全不出现**，
但在 API 载荷里是**独立输入**，键名是 `<父>.<子>`：

| 节点 | 父控件取值 | 子控件（API 键） |
|---|---|---|
| `BlockSparseAttention` | `selection = "sol-attn"` | `selection.tau` |
| `SaveVideo` | `format = "mp4"` | `format.codec` |

两个方向都会翻车（实测各踩一次）：

1. **按位置 zip** → 子控件在 `widgets_values` 里多占一格，其后所有控件前移一位：
   `start_percent` 拿到 `1.3`、`min_tokens` 拿到 `""`、`extra_tokens` 拿到 `12288`、
   `sink_conditioning` 拿到 `256`。提交被 `/prompt` 的 max/枚举校验拦下。
2. **只注入对齐表里的名字** → 子控件被整条丢掉，提交报
   `Required input is missing: tau`（`input_name: selection.tau`）。

正确做法：名字表里**父名已在控件表内**、且带 `.` 的额外键，一律原样注入；
父名不在表内的（纯前端状态）不碰。

## 验证方法

转换后不要直接提交，先 `--dump` 出 JSON 并抽查：

- 加载器：模型名是否正确
- 采样器：`scheduler`/`steps`/`denoise`
- 数据表节点：`data.selected.values` 里的提示词长度是否为新值
- 有连线的输入：源节点 id 是否指向预期节点（尤其经 Reroute 的）

**判断依据**：越界或枚举外的错位会被 `POST /prompt` 校验拦下（`node_errors` 里直接指明节点、
输入名与实际收到的值）；**落在合法区间内的错位不会报错** —— 后者只能靠抽查发现。
所以「提交成功」不等于「参数对」，抽查这一步不能省。
