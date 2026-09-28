"""每秒运动量曲线：高斯去噪后的逐帧差分，输出每秒 avg / median / max。

为什么不能直接用 `blackframe` 的 `pblack`：H3 出片颗粒极重，实测**静止镜头**（雨天窗特写）
`pblack` 也在 79~99 之间波动，与「手完全冻结」的那一秒（85~99）**无法区分** —— pblack 只能看
整体镜头节奏，看不出被摄体（手/脸/物件）有没有在动。

本脚本先做高斯模糊把颗粒抹平，再取相邻帧差分的**中位数**：中位数对"整段基本静止、个别帧跳变"
（切镜）稳健，因此能直接回答「这一段到底有没有在动」。配合 `--crop` 把 ROI 收到手上/脸上，
就得到该部位的独立运动量。

用法:
  python motion-profile.py <视频> [--crop w:h:x:y] [--scale W] [--fps N] [--json]
输出:
  每秒一行：avg / 中位 / max（单位 = 8bit 灰度级），并给出全程中位数参考。
  --json 时改输出 JSON，便于脚本化对比。
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys

import cv2
import numpy as np

FALLBACK_FFMPEG = r"D:\Program Files\ffmpeg\bin\ffmpeg.exe"


def tool(name: str) -> str:
    p = shutil.which(name)
    if p:
        return p
    if name == "ffmpeg" and shutil.os.path.exists(FALLBACK_FFMPEG):
        return FALLBACK_FFMPEG
    sys.exit(f"找不到 {name}，请加进 PATH")


def frames(path: str, crop: str | None, width: int) -> np.ndarray:
    """解码成灰度小图序列 (N, H, W) uint8。"""
    probe = subprocess.run(
        [tool("ffprobe"), "-v", "error", "-select_streams", "v:0",
         "-show_entries", "stream=width,height", "-of", "csv=p=0", path],
        capture_output=True, text=True, check=True).stdout.strip()
    sw, sh = (int(x) for x in probe.split(",")[:2])
    if crop:
        cw, ch, cx, cy = (int(v) for v in crop.split(":"))
    else:
        cx, cy, cw, ch = 0, 0, sw, sh
    if cx + cw > sw or cy + ch > sh:
        sys.exit(f"crop {crop} 超出画面 {sw}x{sh}")

    vf = ([f"crop={crop}"] if crop else []) + [f"scale={width}:-2", "format=gray"]
    raw = subprocess.run([tool("ffmpeg"), "-v", "error", "-i", path,
                          "-vf", ",".join(vf), "-f", "rawvideo", "-"],
                         capture_output=True, check=True).stdout
    ow = width
    oh = max(2, round(ch * ow / cw / 2) * 2)
    n = len(raw) // (ow * oh)
    if n < 2:
        sys.exit("解码帧数不足")
    return np.frombuffer(raw[: n * ow * oh], dtype=np.uint8).reshape(n, oh, ow)


def main() -> int:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    path = args[0]
    crop = args[args.index("--crop") + 1] if "--crop" in args else None
    width = int(args[args.index("--scale") + 1]) if "--scale" in args else 208
    fps = float(args[args.index("--fps") + 1]) if "--fps" in args else 24.0
    as_json = "--json" in args

    seq = frames(path, crop, width)
    blur = np.stack([cv2.GaussianBlur(f, (7, 7), 2.0) for f in seq]).astype(np.int16)
    d = np.abs(np.diff(blur, axis=0)).mean(axis=(1, 2))

    per_sec: dict[int, list[float]] = {}
    for i, v in enumerate(d):
        per_sec.setdefault(int(i / fps), []).append(float(v))
    rows = [{"sec": s,
             "avg": round(sum(v) / len(v), 3),
             "median": round(float(np.median(v)), 3),
             "max": round(max(v), 3),
             "frames": len(v)}
            for s, v in sorted(per_sec.items())]

    if as_json:
        print(json.dumps({"video": path, "crop": crop, "scale": width, "fps": fps,
                          "decoded_frames": int(len(seq)), "per_second": rows},
                         ensure_ascii=False, indent=1))
        return 0

    print(f"{path}")
    print(f"  解码 {len(seq)} 帧 @ {seq.shape[2]}x{seq.shape[1]}"
          + (f"  裁剪={crop}" if crop else "  (全画幅)"))
    print(f"  {'秒':>4} {'avg':>8} {'中位':>8} {'max':>8}   bar(中位)")
    for r in rows:
        print(f"  {r['sec']:>4} {r['avg']:>8.3f} {r['median']:>8.3f} {r['max']:>8.3f}"
              f"   {'#' * min(60, int(r['median'] * 6))}")
    allm = float(np.median(d))
    print(f"  全程差分中位数 = {allm:.3f}；单帧 max > 30 基本就是一次切镜")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
