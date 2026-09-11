"""检查 safetensors 文件完整性: 解析 header 并核对每个 tensor 的 data_offsets 是否越界。

等价于 ComfyUI load_safetensors 的预检查 ("Tensor ... extends past the end of the file"),
但不加载权重、不吃内存, 可批量扫描。
"""

import json
import pathlib
import struct
import sys

ROOT = pathlib.Path(r"D:\Comfy\models")


def check(path: pathlib.Path):
    size = path.stat().st_size
    with path.open("rb") as f:
        raw = f.read(8)
        if len(raw) < 8:
            return False, f"文件头不足 8 字节 (仅 {len(raw)})", size
        n = struct.unpack("<Q", raw)[0]
        if n <= 0 or n > size:
            return False, f"header 长度异常 ({n})", size
        header_bytes = f.read(n)
    try:
        header = json.loads(header_bytes)
    except Exception as e:  # noqa: BLE001
        return False, f"header JSON 解析失败: {e}", size
    data_start = 8 + n
    max_end = 0
    bad = []
    for name, meta in header.items():
        if name == "__metadata__":
            continue
        off = meta.get("data_offsets")
        if not off:
            continue
        end = off[1]
        max_end = max(max_end, end)
        if data_start + end > size:
            bad.append((name, end))
    if bad:
        return False, f"{len(bad)} 个 tensor 越界, 首个: {bad[0][0]} (end={bad[0][1]})", size
    if data_start + max_end != size:
        return False, f"尾部不符: header+data={data_start + max_end} vs 实际 {size} (缺 {size - data_start - max_end} 字节)", size
    return True, f"{len([k for k in header if k != '__metadata__'])} 个 tensor", size


def main() -> int:
    patterns = sys.argv[1:] or [
        "loras/minimax_h3_*.safetensors",
        "vae/minimax_h3_*.safetensors",
        "model_patches/minimax_h3_*.safetensors",
        "latent_upscale_models/minimax_h3_*.safetensors",
        "diffusion_models/minimax_h3_*.safetensors",
    ]
    files = []
    for p in patterns:
        files.extend(sorted(ROOT.glob(p)))
    print(f"扫描 {len(files)} 个文件\n")
    bad_count = 0
    for f in files:
        ok, info, size = check(f)
        mark = "OK " if ok else "BAD"
        if not ok:
            bad_count += 1
        print(f"  [{mark}] {f.parent.name}/{f.name}  {size / 1048576:.1f} MB  {info}")
    print(f"\n损坏 {bad_count} 个 / 共 {len(files)} 个")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
