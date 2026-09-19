# Obsidian-Comfy

为故事库的 md 数据表提供阅读体验增强，并打通 ComfyUI `output` 目录的资源引用。

面向 [stories](../../) 仓库（vault = `D:\Comfy\stories`）开发，桌面版专用。

## 功能

### 1. 表格增强（第一列是 `ID` 的表格）

- **单行渲染**：所有列与内容强制单行，绝不换行
- **省略号截断**：列为 `TEXT` 类型（表头形如 `主-正词(TEXT)`）时，超长内容在渲染层用 `...` 截断，**md 源码完全不变**
- **横向滚动**：表格超宽时容器横向滚动，滚动条细样式
- **搜索过滤**：表格上方搜索框，按 ID 或任意字段实时过滤
- **完整分页**：每页数量选择（20/50/100/200/全部）、首页、上一页、页码、下一页、尾页、跳转输入框
- **ID 排序**：点击 `ID` 列表头或工具栏 `ID ↑/↓` 按钮切换增序 / 降序（按 ID 开头的数字排序，5 位插入编号也能正确排序）

### 2. `@` 资源引用弹窗

在编辑器里输入 `@` 时自动弹出 `output` 目录浏览器：

- 只列出**普通文件**与**「数字-」编号目录**（如 `0040-文生视频`），跳过 `3d`、`clipspace` 等非编号目录与隐藏项
- 文件带**缩略图**：图片显示缩略图、视频显示首帧、音频显示音符图标
- 显示文件类型标签与大小
- 可进入编号目录选择其中的文件，也可返回根目录
- 过滤框按文件名筛选，双击条目直接确定
- 点「确定」自动插入引用：子目录文件插入 `@{目录名/文件名}`，根目录文件插入 `@{文件名}`（**均为去掉扩展名的写法**，符合故事库 ID 引用规范）

## 安装

插件源码在本目录；Obsidian 从 `.obsidian/plugins/` 读取插件，因此需要在此建立链接：

```powershell
# 在 vault 根目录 (stories) 下执行
cmd /c mklink /J ".obsidian\plugins\obsidian-comfy" "Obsidian-Comfy"
```

并在 `.obsidian\community-plugins.json` 中启用：

```json
[
  "obsidian-comfy"
]
```

首次打开 vault 时 Obsidian 会询问「是否信任这个仓库的作者」，需选择**信任仓库作者并启用插件**（否则处于安全模式，插件不加载）。

修改 `main.js` / `styles.css` 后，用命令面板执行「重新加载 Obsidian」即可生效。

## 使用前提

- **阅读模式**：表格增强走 `registerMarkdownPostProcessor`，**只在阅读模式（Ctrl+E 切换）生效**，实时预览模式下表格仍是原生渲染。
- **桌面版**：插件通过 Node `fs` 读取 vault 外的 ComfyUI output 目录，故 `isDesktopOnly: true`。

## 设置

设置 → 第三方插件 → Comfy 数据表：

| 项 | 说明 | 默认 |
|---|---|---|
| output 目录 | ComfyUI 的 output 绝对路径 | `D:\Comfy\media\七纹刻印` |
| 启用表格增强 | 总开关 | 开 |
| 启用 @ 弹窗 | 总开关 | 开 |
| 每页数量可选项 | 逗号分隔 | `20,50,100,200` |
| 默认每页数量 | 0 表示全部 | `20` |
| TEXT 列最大宽度 | 超出即截断 | `420` |
| 其它列最大宽度 | 非 TEXT 列上限 | `720` |
| 缩略图取图方式 | `app`（`app://local` 协议）/ `base64`（内联，兼容性最好但占内存） | `app` |
| 弹窗缩略图宽度 | 像素 | `72` |

## 实现要点

- **省略号截断为什么不用 `td` 的 `max-width`**：在 `table-layout: auto` 下 `td` 的 `max-width` 不生效，因此单元格内容会被包进 `.oc-clip` 容器，由该容器承担 `max-width` + `overflow: hidden` + `text-overflow: ellipsis`。
- **排序为什么要重排 DOM**：`apply()` 先按当前查询过滤、再按 ID 数字键排序，然后**按排序结果**依次 `appendChild` 回 `tbody`；若按原始顺序重排会覆盖排序结果。
- **ID 列点击用事件委托**：挂在滚动容器上并判断 `closest('th.oc-th-id')`，避免 Obsidian 重渲染表格后节点句柄失效。
- **`@` 触发**：借用 `EditorSuggest.onTrigger` 做按键检测（比 CodeMirror 扩展简单且准确），命中后直接打开自定义 `Modal` 并返回 `null`，因此不会显示候选列表。

## 文件

| 文件 | 说明 |
|---|---|
| `manifest.json` | 插件清单 |
| `main.js` | 插件全部逻辑（纯 JS，无构建步骤、无第三方依赖） |
| `styles.css` | 表格与弹窗样式 |

插件不引入任何 npm 依赖，也不需要打包——`main.js` 直接由 Obsidian 以 CommonJS 加载。
