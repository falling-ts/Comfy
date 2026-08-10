# ComfyUI 扩图与裁切放大三方插件 Star 榜

> 数据来源:GitHub API 实时查询,统计于 2026-08-10
> star 数为仓库当前 `stargazers_count`;提交时间为 GitHub `pushed_at`(最近一次 push/提交时间)
> 范围:图片**扩图(outpainting)** 与 **裁切放大(crop/upscale/局部重绘)** 相关第三方插件

---

## 一、完整榜单(按 star 从多到少)

| # | 插件 | GitHub 仓库 | ⭐ Star | 最近提交/推送 | 类别 | 说明 / 相关节点 | 本机已装 |
|---|------|------------|--------|--------------|------|----------------|---------|
| 1 | ComfyUI-Impact-Pack | ltdrdata/ComfyUI-Impact-Pack | **3251** | 2026-04-19 | 扩图/裁剪放大 | `FaceDetailer`/`DetailerForEach`/`ImpactImageCrop`,检测框选→裁剪→latent放大→重绘→贴回 | 否 |
| 2 | ComfyUI_LayerStyle | chflame163/ComfyUI_LayerStyle | **3118** | 2026-08-01 | 扩图/裁剪放大 | `LayerUtility: CropByMask`、`LayerMask: MaskBoxDetect`,画 mask 框选区域 | 否 |
| 3 | ComfyUI-KJNodes | kijai/ComfyUI-KJNodes | **3031** | 2026-08-07 | 裁剪放大 | `ImageResizeKJ`/`ImageResizeKJv2` 等工具节点 | ✅ 已装 |
| 4 | ComfyUI-SeedVR2_VideoUpscaler | numz/ComfyUI-SeedVR2_VideoUpscaler | **2723** | 2025-12-24 | 裁切放大/精修 | SeedVR2 图像/视频高清修复放大,`SeedVR2LoadDiTModel`/`SeedVR2VideoUpscaler` | 否 |
| 5 | ComfyUI-Easy-Use | yolain/ComfyUI-Easy-Use | **2651** | 2026-07-28 | 扩图/裁剪放大 | `easy imageCrop`(前端拖框截图)、`easy imageSplitGrid`(九宫格拆块放大) | 否 |
| 6 | ComfyUI-SUPIR | kijai/ComfyUI-SUPIR | **2303** | 2026-04-29 | 裁切放大/精修 | SUPIR 高清放大修复,`SUPIR_Upscale` | 否 |
| 7 | was-node-suite-comfyui(WAS Node Suite) | WASasquatch/was-node-suite-comfyui | **1814** | 2025-06-02 | 裁剪放大 | 210+ 节点,含 `Image Crop`/`Image Resize`/`Blend` 等 | 否 |
| 8 | ComfyUI-Florence2 | kijai/ComfyUI-Florence2 | **1730** | 2026-05-06 | 辅助(区域理解) | 图像区域理解/反推,辅助局部重绘选区域 | 否 |
| 9 | ComfyUI_UltimateSDUpscale | ssitu/ComfyUI_UltimateSDUpscale | **1535** | 2026-06-22 | 裁切放大 | 大图分块 tile 图生图放大补细节,`UltimateSDUpscale` | ✅ 已装 |
| 10 | LanPaint | scraed/LanPaint | **1318** | 2026-08-10 | 扩图/局部重绘 | 高质量免训练局部重绘 inpaint,适配各类 SD 模型 | 否 |
| 11 | ComfyUI_Comfyroll_CustomNodes | Suzie1/ComfyUI_Comfyroll_CustomNodes | **1291** | 2024-07-24 | 裁剪放大 | CR 工具节点,含裁剪/缩放/拼合 | 否 |
| 12 | comfyui-inpaint-nodes | Acly/comfyui-inpaint-nodes | **1227** | 2026-05-31 | 扩图/局部重绘 | `InpaintCrop(CutForInpaint)`+`InpaintStitch(BlendInpaint)` 零偏移裁剪重绘贴回、Fooocus/LaMa/MAT inpaint | 否 |
| 13 | ComfyUI-segment-anything-2 | kijai/ComfyUI-segment-anything-2 | **1210** | 2025-09-28 | 辅助(区域分割) | SAM2 分割目标,精确框选要放大的区域 | 否 |
| 14 | ComfyUI_essentials | cubiq/ComfyUI_essentials | **1155** | 2025-04-14 | 裁剪放大 | 轻量节点集,含 crop/resize/upscale 常用工具 | 否 |
| 15 | ComfyUI-Inpaint-CropAndStitch | lquesada/ComfyUI-Inpaint-CropAndStitch | **1137** | 2026-08-09 | 扩图/裁剪放大 | ⭐ 采样前裁剪、采样后贴回(crop→sample→stitch),区域放大重绘专用 | 否 |
| 16 | ComfyUI-Kontext-Inpainting | ZenAI-Vietnam/ComfyUI-Kontext-Inpainting | **401** | 2025-07-01 | 扩图 | Flux Kontext Inpainting 实现 | 否 |
| 17 | one-node-flux-2-klein | yanokusnir-ai/one-node-flux-2-klein | **379** | 2026-08-06 | 扩图/裁剪放大 | Flux 2 Klein 单节点封装:生成/编辑/放大 | 否 |
| 18 | Comfyui-LayerForge | Azornes/Comfyui-LayerForge | **337** | 2026-07-24 | 辅助(画布编辑) | 类 Photoshop 分层画布编辑器,方便框选编辑区域 | 否 |
| 19 | ComfyUi_NNLatentUpscale | Ttl/ComfyUi_NNLatentUpscale | **269** | 2024-12-01 | 裁切放大 | latent 空间神经网络放大 | 否 |
| 20 | LCM_Inpaint_Outpaint_Comfy | taabata/LCM_Inpaint_Outpaint_Comfy | **259** | 2024-11-18 | 扩图 | LCM 加速的 inpaint/outpaint 节点 | 否 |
| 21 | ComfyUI-Upscaler-Tensorrt | yuvraj108c/ComfyUI-Upscaler-Tensorrt | **248** | 2026-06-07 | 裁切放大 | TensorRT 加速 2-4x 放大 | 否 |

---

## 二、按用途归类

### 扩图 / 局部重绘(选区域 → 补画面)
- **Impact-Pack**(3251★):FaceDetailer / DetailerForEach 自动框选放大重绘
- **LayerStyle**(3118★):CropByMask / MaskBoxDetect 画遮罩选区域
- **Easy-Use**(2651★):easy imageCrop 前端拖框
- **LanPaint**(1318★):免训练高质量局部重绘
- **comfyui-inpaint-nodes**(1227★):InpaintCrop + InpaintStitch 零偏移重绘
- **ComfyUI-Inpaint-CropAndStitch**(1137★):裁剪→采样→贴回
- **ComfyUI-Kontext-Inpainting**(401★)、**LCM_Inpaint_Outpaint_Comfy**(259★)

### 裁切放大 / 高清放大(放大 + 补细节)
- **SeedVR2 VideoUpscaler**(2723★):SeedVR2 修复放大
- **SUPIR**(2303★):SUPIR 高清放大
- **WAS Node Suite**(1814★):裁切/缩放/拼合工具集
- **UltimateSDUpscale**(1535★):分块放大补细节(本机已装)
- **Comfyroll**(1291★)、**essentials**(1155★)、**NNLatentUpscale**(269★)、**Upscaler-Tensorrt**(248★)
- **KJNodes**(3031★):ImageResizeKJ 等(本机已装)

### 辅助(区域选择 / 理解)
- **Florence2**(1730★):区域理解反推
- **SAM2**(1210★):目标分割框选
- **LayerForge**(337★):分层画布编辑

---

## 三、本机落地对照(8GB)

| 场景 | 推荐插件 | Star | 备注 |
|------|---------|------|------|
| 局部区域放大补细节(首选,免安装思路) | 内置 `ImageCrop`/`CropByBBoxes` + 本机 Qwen-Edit-2511 | — | 详见《局部区域截图放大补细节工作流调研》 |
| 现成分块放大 | UltimateSDUpscale | 1535 | ✅ 已装即用 |
| 一站式自动框选放大重绘 | Impact-Pack | 3251 | 需安装,配 UltralyticsDetector |
| 画遮罩选区域,零偏移重绘 | comfyui-inpaint-nodes / Inpaint-CropAndStitch | 1227 / 1137 | 需安装 |
| 放大后精修 | SeedVR2(2723★)/ SUPIR(2303★) | — | 8GB 建议 3B 量化版 |

---

## 附:数据说明

- 部分仓库存在转移/改名:如 `ComfyUI-Manager` 已由 ltdrdata 转至 Comfy-Org;表中均为查询时 GitHub 返回的当前 `full_name`
- 「最近提交/推送」为 `pushed_at` 字段(最近一次推送/提交至默认分支的时间),UTC
- 未计入 ComfyUI-Manager、前端类(Custom-Scripts)等非扩图/放大功能插件
