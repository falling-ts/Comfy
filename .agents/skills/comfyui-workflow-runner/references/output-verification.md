# 产出校验配方

运行成功 ≠ 产出正确。每次都要探测文件并**真的看一眼**。

## 1. 探测（区分 temp 预览与已保存产出）

```bash
ffmpeg -hide_banner -i <file> 2>&1 | grep -E 'Duration|Stream #'
```

关注：时长、分辨率、帧率、**是否存在音频流**（FallingTS 的预览节点与部分工作流不带音轨；
用户可能明确表示不需要音频，此时不要当成缺陷）。

定位最近任务的产出：

```bash
python scripts/list-recent-outputs.py   # /history?max_items=N 的输出文件映射
```

**注意**：`PreviewVideo` / `PreviewImageSave` 默认只写 `ComfyUI/temp/`（点「保存」才写 output），
所以 media 目录里找不到不代表没生成。

## 2. 抽帧拼板

```bash
# 1 秒 1 帧，12 秒 → 4x3
ffmpeg -y -i in.mp4 -vf "fps=1,scale=480:-1,tile=4x3" -frames:v 1 grid.png
# 均匀 N 帧（如 8 帧：fps=8/时长）
ffmpeg -y -i in.mp4 -vf "fps=2/3,scale=640:-1,tile=4x2" -frames:v 1 grid8.png
```

然后**读图**判断内容、构图演进、物件是否漂移或凭空增减。

## 3. 运动一致性（定量）

```bash
ffmpeg -hide_banner -i in.mp4 \
  -vf "fps=2,scale=160:90,tblend=all_mode=difference,blackframe=amount=0:threshold=10" \
  -f null - 2>&1 | grep pblack
```

`pblack` = 差异后接近纯黑的像素百分比，**越大表示运动越小**。

判读：匀速镜头应近似**恒定**；出现 80+ 的尖峰即停顿/吸附，出现 <30 的谷值即猛冲/跳变。
把整条曲线打印成柱状，一眼能看出节奏是否均匀。

## 4. 镜头运动类型判别

从抽帧图上判断是**原地旋转**还是**平移**：

- 原地旋转（pan / turn in place）：中心物体保持在画面中央附近，四周背景依次滑入滑出
- 平移（tracking）：被摄主体从画面中央**移向一侧**，像布景横向掠过

提示词里误用「环绕 / orbit」会导致模型做出平移 —— 该词在影视术语中指"机位绕主体转圈"，
而"以场景中央为轴旋转"应写 **固定机位 + 原地水平转动**。

## 5. 音频（仅在需要时）

```bash
ffmpeg -hide_banner -i in.mp4 -af astats=metadata=1:reset=1 -f null - 2>&1 | grep -E 'Peak|RMS'
```

- 峰值贴 0 dBFS 且长时间持平 → 削波/爆音
- H3 原生音轨为 32 kHz 立体声；采样率异常说明链路被改动过

## 6. 缓存陷阱

执行缓存会让**逐字节相同**的工作流秒回结果。做 A/B 时务必改 seed 或提示词，
否则会把"5 秒的缓存命中"当成真实渲染耗时（真实 H3 480p 4 步约 140-190 秒）。
