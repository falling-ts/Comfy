"""验证假设: 参考板四格(每 90 度一个正交视角)是否导致镜头在参考视角处"吸附"、在中间角度"猛冲"。

做法: 把已有视频的每 0.5 秒运动量(pblack, 越大=越慢)与"该时刻镜头角度距最近参考视角的偏差"对齐,
按偏差分组统计。若 0 度组显著更慢, 说明模型在参考视角上停住 —— 即"离散参考视角与连续旋转不切合"。
"""

import subprocess

FFMPEG = r"D:\Program Files\ffmpeg\bin\ffmpeg.exe"
VIDEO = r"D:\Comfy\ComfyUI\temp\ComfyUI_temp_cfwwk_00001_.mp4"  # 12 秒去泄漏版
SECONDS = 12.25
FPS_SAMPLE = 2  # 每 0.5 秒一个采样


def pblack_series(path: str) -> list:
    out = subprocess.run(
        [FFMPEG, "-hide_banner", "-i", path,
         "-vf", f"fps={FPS_SAMPLE},scale=160:90,tblend=all_mode=difference,blackframe=amount=0:threshold=10",
         "-f", "null", "-"],
        capture_output=True, text=True, encoding="utf-8", errors="ignore",
    ).stderr
    vals = []
    for line in out.splitlines():
        if "pblack:" in line:
            try:
                vals.append(int(line.split("pblack:")[1].split()[0]))
            except (IndexError, ValueError):
                pass
    return vals


def main() -> int:
    vals = pblack_series(VIDEO)
    n = len(vals)
    print(f"采样点 {n} 个 (每 {1 / FPS_SAMPLE:.1f}s)\n")

    # 360 度均分到整段时长
    per_sample_deg = 360.0 / n
    groups = {0: [], 15: [], 30: [], 45: []}
    rows = []
    for i, pb in enumerate(vals):
        deg = (i + 0.5) * per_sample_deg % 360
        # 距最近 90 度整数倍的偏差
        dev = min(deg % 90, 90 - (deg % 90))
        bucket = min(groups.keys(), key=lambda k: abs(k - dev))
        groups[bucket].append(pb)
        rows.append((i * 0.5 + 0.5, deg, dev, pb))

    print("t(s)   角度    距最近锚点   pblack")
    for t, deg, dev, pb in rows:
        bar = "#" * max(1, int((110 - pb) / 3))
        print(f"{t:5.1f}  {deg:6.1f}  {dev:6.1f}      {pb:3d}  {bar}")

    print("\n=== 按「距最近参考视角的偏差」分组 ===")
    print("偏差(度)  样本数   pblack 均值   说明")
    for k in sorted(groups):
        g = groups[k]
        if not g:
            continue
        avg = sum(g) / len(g)
        note = "← 参考视角上(吸附?)" if k == 0 else ("← 正中间(最无约束)" if k == 45 else "")
        print(f"  {k:3d}      {len(g):3d}      {avg:6.1f}     {note}")

    anchor = groups[0]
    middle = groups[45]
    if anchor and middle:
        a, m = sum(anchor) / len(anchor), sum(middle) / len(middle)
        print(f"\n锚点处均值 {a:.1f} vs 中段均值 {m:.1f}  ->  锚点慢 {a / m:.2f} 倍")
        print("(pblack 越大=运动越小; 若锚点显著更大, 即证明模型在参考视角上停住)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
