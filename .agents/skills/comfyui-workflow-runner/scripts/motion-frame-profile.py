"""逐帧帧间差剖面：判断一个时间窗里「谁在动、相机停没停」，并为跨 take 比较提供可除的静态控制区。

它解决的是 `motion-profile.py` 的盲点：那个脚本按秒汇总，切镜那一帧会把整秒抬起来；而且跨 take
直接比绝对值会被"本轮雨更大 / 切点更早"骗到（实测取 5.60–6.95s 当静止窗时，新片全幅中位 0.188→0.438，
连本应静止的窗区都涨了，于是得出相反结论 —— 其实是新片 6.40–6.61s 已经在切镜）。

用法:
  python motion-frame-profile.py <视频> [--t0 5.4] [--t1 7.0] [--fps 24] [--blur 4]
        [--roi 手:330,310,490,410] [--roi 臂:150,240,320,340] [--control 740,0,830,130]

判读:
  1) 全幅均值单帧飙到几十以上 = 切镜；取**两片都还没切、全幅差已落到地板**的区间再比。
  2) `--control` 必须两片持平，否则说明相机动了/光照变了，该窗口作废。
  3) 结论用 ``ROI ÷ control``，不要用裸值。
"""
from __future__ import annotations

import pathlib
import subprocess
import sys

import numpy as np
from PIL import Image

TMP = pathlib.Path(r"D:\Comfy\temp-frames")


def parse_box(spec: str) -> tuple[str, tuple[int, int, int, int]]:
    name, box = spec.split(":", 1)
    x0, y0, x1, y1 = (int(v) for v in box.split(","))
    return name, (x0, y0, x1, y1)


def box_blur(a: np.ndarray, k: int) -> np.ndarray:
    h, w = a.shape
    h2, w2 = h - h % k, w - w % k
    b = a[:h2, :w2].reshape(h2 // k, k, w2 // k, k).mean(axis=(1, 3))
    return np.repeat(np.repeat(b, k, axis=0), k, axis=1)


def run(video: str, t0: float, t1: float, fps: int, k: int, rois, control):
    tag = pathlib.Path(video).stem
    out = TMP / f"prof-{tag}"
    out.mkdir(parents=True, exist_ok=True)
    for f in out.glob("*.png"):
        f.unlink()
    subprocess.run(["ffmpeg", "-y", "-v", "error", "-ss", str(t0), "-to", str(t1), "-i", video,
                    "-vf", f"fps={fps}", str(out / "f-%03d.png")], check=True)
    files = sorted(out.glob("f-*.png"))
    arrs = [box_blur(np.asarray(Image.open(f).convert("L"), dtype=np.float32), k) for f in files]
    d = np.stack([np.abs(arrs[i + 1] - arrs[i]) for i in range(len(arrs) - 1)])

    cname, (cx0, cy0, cx1, cy1) = control
    names = [n for n, _ in rois] + [cname]
    print(f"\n=== {tag}  {len(arrs)} 帧 (t0={t0}, fps={fps}) ===")
    print(f"  {'t':>5} {'全幅中位':>9} {'全幅均值':>9} " + " ".join(f"{n:>8}" for n in names))
    rows = []
    for i in range(len(d)):
        t = t0 + (i + 1) / fps
        g_med, g_mean = float(np.median(d[i])), float(d[i].mean())
        vals = [float(d[i, y0:y1, x0:x1].mean()) for _, (x0, y0, x1, y1) in rois]
        ctrl = float(d[i, cy0:cy1, cx0:cx1].mean())
        rows.append((g_mean, vals, ctrl))
        print(f"  {t:5.2f} {g_med:9.3f} {g_mean:9.3f} "
              + " ".join(f"{v:8.3f}" for v in vals)
              + f" {ctrl:8.3f}   " + " ".join(f"{v / max(1e-6, ctrl):5.2f}x" for v in vals))

    floor = min(r[0] for r in rows)
    ctrl_med = float(np.median([r[2] for r in rows]))
    print(f"  --> 全幅均值地板={floor:.3f}  静态控制区({cname})中位={ctrl_med:.3f}")
    for name, _ in rois:
        idx = [n for n, _ in rois].index(name)
        med = float(np.median([r[1][idx] for r in rows]))
        print(f"      {name:<10} 中位={med:7.3f}  /{cname}={med / max(1e-6, ctrl_med):5.2f}x  "
              f"/全域地板={med / max(1e-6, floor):5.2f}x")


if __name__ == "__main__":
    a = sys.argv
    opts = {"--t0", "--t1", "--fps", "--blur", "--roi", "--control"}
    vids, i = [], 1
    while i < len(a):
        if a[i] in opts:
            i += 2
            continue
        if a[i].startswith("--"):
            i += 1
            continue
        vids.append(a[i])
        i += 1
    t0 = float(a[a.index("--t0") + 1]) if "--t0" in a else 5.4
    t1 = float(a[a.index("--t1") + 1]) if "--t1" in a else 7.0
    fps = int(a[a.index("--fps") + 1]) if "--fps" in a else 24
    k = int(a[a.index("--blur") + 1]) if "--blur" in a else 4
    rois = [parse_box(a[i + 1]) for i, x in enumerate(a) if x == "--roi"]
    control = parse_box(a[a.index("--control") + 1]) if "--control" in a else ("控制区", (0, 0, 1, 1))
    if not rois:
        sys.exit("至少给一个 --roi 名字:x0,y0,x1,y1")
    for v in vids:
        run(v, t0, t1, fps, k, rois, control)
