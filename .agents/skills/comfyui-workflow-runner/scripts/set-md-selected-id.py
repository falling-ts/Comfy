"""把工作流 mdtable 的 selected.id 改为指定值(供 workflow-to-prompt 的 --refresh-md 定位行)。

用法: python scripts/set-md-selected-id.py "3030-*.json" "场景参考板-书房"
"""

import glob
import json
import pathlib
import sys

pat = sys.argv[1]
new_id = sys.argv[2]
p = pathlib.Path(glob.glob(str(pathlib.Path(r"D:\Comfy\workflows") / pat))[0])
d = json.loads(p.read_text(encoding="utf-8"))

for n in d["nodes"]:
    if n["type"] != "FallingTSMarkDownTable":
        continue
    wv = (n.get("widgets_values") or [{}])[0]
    sel = wv.setdefault("selected", {})
    print(f"[{n['id']}] selected.id: {sel.get('id')!r} -> {new_id!r}")
    sel["id"] = new_id
    # values 里也同步 ID 字段(其余字段由 refresh 时按 md 覆盖)
    vals = sel.setdefault("values", {})
    if "ID" in vals:
        vals["ID"] = new_id

p.write_text(json.dumps(d, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
print(f"已写入 {p.name}")
