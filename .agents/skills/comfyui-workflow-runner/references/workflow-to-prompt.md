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

从 `/object_info/<type>` 取 `input.required` + `input.optional`，按定义顺序收集**非连线类型**
（`INT`/`FLOAT`/`STRING`/`BOOLEAN` 以及 combo = 列表类型）的输入名，得到 **完整控件名列表**。

然后：

```python
for name, val in zip(全部控件名, widgets_values):
    if name in 已连线控件名:      # 被转成了输入
        continue
    inputs[name] = val
```

**必须用完整列表 zip，再过滤**。原因：前端序列化 `widgets_values` 时，被转成输入的控件**仍然占位**。

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

## 验证方法

转换后不要直接提交，先 `--dump` 出 JSON 并抽查：

- 加载器：模型名是否正确
- 采样器：`scheduler`/`steps`/`denoise`
- 数据表节点：`data.selected.values` 里的提示词长度是否为新值
- 有连线的输入：源节点 id 是否指向预期节点（尤其经 Reroute 的）

**判断依据**：非法输入会被 ComfyUI 拒绝并报错，但**错位的合法值不会** —— 后者只能靠抽查发现。
