---
name: comfyui-workflow-runner
description: |
  通过 HTTP API 无头运行本地 ComfyUI 工作流，无需触碰浏览器：把保存的工作流 JSON 转成 API prompt 格式、
  按 md 文件刷新 FallingTS 数据表状态（等价于点击该节点的刷新按钮）、提交 /prompt、轮询 /history 至完成，
  并对产出做探测与抽帧校验。适用于需要自主执行或重跑工作流、md 数据表里改过的提示词必须真正生效、
  或需要对成片做客观检查（时长、帧率、有无音轨、运动与连贯性）的场合。不适用于撰写提示词文本或开发自定义节点。
---

# ComfyUI 工作流无头运行器

用脚本驱动本地 ComfyUI（`http://127.0.0.1:8188`）：**改源数据 → 刷新数据表节点 → 提交 → 检查产出**。
不需要浏览器、不需要人点 Run、也不需要手工同步前端状态。

## 何时使用

- 工作流需要被执行并检查产出，而用户不会替你点 Run。
- `stories/**/*.md` 数据表里的提示词刚改过 —— 工作流 JSON 里仍是**旧文本**，除非有东西去刷新它。
- 需要真实渲染来做 A/B 对比或回归检查。

## 核心原理（为什么什么都不用点）

`FallingTSMarkDownTable.execute(data, id)` 只消费前端序列化进工作流的**控件状态** `data`
（`{md_path, fields, selected}`），**它自己从不读 md 文件**。前端的"刷新"按钮只是调用
`GET /fallingts_mdtable/read?path=...`，把返回的行写回该状态。因此调同一个接口、自己构造 `data`
与之等价 —— 而且完全不需要浏览器。

## 操作步骤

1. **转换并刷新**
   `python scripts/workflow-to-prompt.py "<glob>" --refresh-md --dump prompt.json`
   确认节点数，以及 mdtable 的提示词长度已变成新值（长度没变说明没刷新，等于在静默重跑上一版提示词）。
2. **干跑检查** —— 在消耗 GPU 之前抽查几个关键节点（加载器、采样器、SigmaShift、数据表）。
3. **提交** —— 加 `--submit`。脚本会 POST `/prompt`、轮询 `/history/<id>`，并打印产出的文件名。
4. **校验产出** —— 不要只看"成功"，要探测并**看**它：
   - `ffmpeg -i file.mp4` → 时长、分辨率、帧率、**以及是否存在音轨**
   - 抽帧拼板：`ffmpeg -y -i f.mp4 -vf "fps=1/N,scale=640:-1,tile=4x2" -frames:v 1 grid.png`
   - 读 `grid.png`，据此判断内容、连贯性与一致性
   - 运动一致性：`-vf "fps=2,scale=160:90,tblend=all_mode=difference,blackframe=amount=0:threshold=10"`，
     比较 `pblack` 值；**恒定**代表匀速，剧烈起伏代表卡顿或停滞

## 陷阱（每一条都花过一轮真实调试）

- **`widgets_values` 包含"已被转成输入"的 widget**。被连线的 widget 仍占数组里的位置，所以必须先按
  **完整** widget 列表 zip、**再**跳过被连线的；先过滤会整体错位 —— `PreviewImageSave.format` 会静默
  拿到 `filename_suffix` 的值。**这类错误不报错**，因为错的值仍是合法值。
- **`Reroute` 在 API 图里不存在**。必须把下游引用解析到真实源节点，否则那些输入会丢失连接。
- **`MarkdownNote` / `Note` 是纯前端节点** —— 跳过。
- **`mode: 4`（bypass）与 `mode: 2`（mute）** 需要显式处理；脚本目前跳过并报告。
- **执行缓存**：字节完全相同的工作流会秒回缓存。做 A/B 时改 seed 或提示词，否则你会"测"到一次
  5 秒的假渲染。
- **新增自定义节点需要重启 ComfyUI** 才会出现在 `/object_info`。
- 被杀掉的运行不会留下产出；应查 `/history` 的 `execution_error` 消息，而不是断定脚本失败。

## 文件

- `scripts/workflow-to-prompt.py` —— 工作流 JSON → API prompt、md 刷新、提交与轮询。
- `scripts/list-recent-outputs.py` —— 把最近的任务映射到其产出文件（temp 预览 vs 已保存）。
- `references/workflow-to-prompt.md` —— 转换规则与完整陷阱清单。
- `references/mdtable-refresh.md` —— FallingTS mdtable 的状态结构、接口与刷新机制。
- `references/output-verification.md` —— 探测、抽帧拼板、运动与音频分析配方。
