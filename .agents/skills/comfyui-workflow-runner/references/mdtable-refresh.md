# FallingTS MarkDown 数据表：状态结构与刷新机制

## 状态结构

节点控件值 `data`（前端序列化进工作流 `widgets_values[0]`）：

```json
{
  "md_path": "stories/七纹刻印/3020-参考场景.md",
  "fields": [{"name": "ID", "type": "STRING"}, {"name": "<Picture 1>", "type": "IMAGE"}, ...],
  "selected": {
    "id": "参考场景-书房360",
    "values": {"ID": "...", "<Picture 1>": "@{场景旋镜-书房四图}", "场景提示词": "六段式提示词全文", ...}
  }
}
```

- `md_path`：md 文件路径，支持项目根相对路径（如 `stories/.../x.md`）与绝对路径
- `fields`：表头字段定义（名 + 类型），决定输出端口
- `selected.id`：选中的行 ID
- `selected.values`：该行的**字段快照**（提示词全文就在这里）

## HTTP 接口

| 方法 | 路径 | 用途 |
|---|---|---|
| GET | `/fallingts_mdtable/read?path=<相对或绝对路径>` | **读取并解析 md**，返回 `{ok, path, fields, rows, total}` |
| GET | `/fallingts_mdtable/browse?path=<目录>` | 浏览 md 文件树 |
| GET | `/fallingts_mdtable/preview?path=<媒体路径>` | 提供图片/视频/音频的本地预览（支持 `@{ID}` 引用） |
| GET | `/fallingts_mdtable/resolve?path=<值>&kind=<类型>` | 把 `@{ID}` 引用解析为实际文件路径 |
| POST | `/fallingts_mdtable/select_file` | 弹出系统文件选择器（仅 GUI 环境有意义） |

## 刷新机制（关键）

```
前端「刷新」按钮
  → GET /fallingts_mdtable/read?path=<md_path>
  → 用返回的 fields/rows 覆盖节点的 widgets_values
  → 存入工作流 JSON

后端 execute(data, id)
  → normalize_state(data)     ← 只用 data
  → build_outputs(state)
  → 从不读取 md 文件本身
```

**推论**：改了 md 之后，工作流 JSON 里的提示词仍是旧值，除非有东西把 `/read` 的结果写回 `data`。
无头运行时，**自己调 `/read` 并构造 `data`** 与点刷新完全等价。

## 无头刷新做法

```python
r = GET(f"/fallingts_mdtable/read?path={quote(state['md_path'])}")
row = next(x for x in r["rows"] if x["id"] == state["selected"]["id"])
new_state = dict(state, fields=r["fields"],
                 selected={"id": row["id"], "values": row["values"]})
prompt["<mdtable_node_id>"]["inputs"]["data"] = new_state
```

## 验证刷新确实生效

对比刷新前后的提示词长度（`workflow-to-prompt.py` 会打印）：

```
mdtable: 提示词 2489 -> 2657 字符 (已按 md 刷新)
```

长度不变 = 没刷新 = 你正在静默重跑上一版提示词。这是最容易犯的隐性错误。

## 相关实现细节

- `IS_CHANGED(cls, data, **kwargs)`：缓存签名取 `data` 的 JSON + 媒体字段源文件 mtime；
  因此**只改 md 文件而不改 `data` 不会触发重跑** —— 又一次说明必须把新值写进 `data`。
- IMAGE/VIDEO/AUDIO/MASK 字段在 `execute` 里经 `resolve_media_path` 解析 `@{ID}` 引用并加载为张量；
  解析失败输出 `None`（可选输入惯例），所以引用写错不会立刻报错，只会让下游收到无值。
