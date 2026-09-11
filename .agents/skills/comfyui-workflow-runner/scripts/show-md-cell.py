"""打印指定 md 资源表第 2 行(首条数据)的指定列, 便于逐句检查提示词。

用法: python scripts/show-md-cell.py "3010-首帧场景.md" 3
"""

import pathlib
import sys

md = pathlib.Path(r"D:\Comfy\stories\七纹刻印") / sys.argv[1]
col = int(sys.argv[2]) if len(sys.argv) > 2 else 3
lines = md.read_text(encoding="utf-8").splitlines()
if len(lines) < 3:
    print("无数据行")
    raise SystemExit(1)
cells = lines[2].split("|")
print(f"列数: {len(cells) - 2}\n")
val = cells[col].strip()
print(val.replace("<br>", "\n"))
