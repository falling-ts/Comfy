# Qwen-Image-Edit 输入/输出分辨率要求报告(2026-08-06)

调研日期:2026-08-06。来源:官方模型卡与 API 文档(HF / 阿里云百炼 / RunPod / Replicate)、ComfyUI 本地源码(v0.30.0 `comfy_extras/nodes_qwen.py`)、diffusers / vLLM-Omni / InvokeAI 实现、Civitai 工作流、全网与社区实测。

---

## 一、结论速览

| 项目 | 要求/推荐 |
|---|---|
| 输入图总像素(官方 API) | 512×512 ~ 2048×2048 之间 |
| 输入图最佳 | 约 **1MP(1024×1024 量级)**,宽高 384~2048px,单图 ≤10MB |
| 输入图数量 | 1~3 张(ComfyUI 原生 3 个输入;vLLM-Omni 放宽到 4 张) |
| 输出分辨率(ComfyUI 原生) | **= 输入分辨率**(编辑模型没有独立空 latent,直接编输入图) |
| 输出分辨率(官方 API) | 默认接近 1024×1024;可指定 512~2048 总像素;2511 官方推荐 6 种尺寸 |
| 参考图(理解用) | 自动缩到 1MP(单图 1024×1024 面积;多图模式 VLM 图 384×384、ref_latent 1MP) |
| 社区高分辨率上限 | 16MP(补丁节点 Eric_Qwen_Edit_Experiments,支持 17MP,生成可达 60MP) |

---

## 二、官方 API 要求(阿里云 Model Studio / 百炼 qwen-image-edit)

- **可指定**:图像总像素需在 **512×512 ~ 2048×2048** 之间;
- **默认**:总像素数接近 **1024×1024**,宽高比与输入图相近(多图输入时为最后一张);
- **建议**:宽和高均在 384~2048 像素之间;图像大小不超过 10MB;
- **输出张数**:`qwen-image-edit` 仅支持 1 张;`qwen-image-2.0` 系列 / `qwen-image-edit-max` / `qwen-image-edit-plus` 系列可选 1~6 张。

## 三、官方推荐输出尺寸(Qwen-Image-Edit-2511)

RunPod 官方端点文档列出的输出尺寸档位(也是社区 ComfyUI 工作流常用档位):

```
1024×1024、1024×1280、1280×1024、1280×1280、1280×1536、1536×1080
```

即官方训练/推荐的 6 种输出规格,总像素约 1~2MP。

## 四、ComfyUI 原生行为(本地源码确认,v0.30.0)

### 4.1 单图编辑 `TextEncodeQwenImageEdit`

```python
total = int(1024 * 1024)
scale_by = math.sqrt(total / (samples.shape[3] * samples.shape[2]))
width = round(samples.shape[3] * scale_by)
height = round(samples.shape[2] * scale_by)
s = comfy.utils.common_upscale(samples, width, height, "area", "disabled")
```

- 输入参考图**自动缩放到总像素 1024×1024(保持宽高比,area 插值)**;
- 有 VAE 时 `ref_latent = vae.encode(1MP 图)` —— 参考潜空间固定为 1MP 面积。

### 4.2 多图编辑 `TextEncodeQwenImageEditPlus`(本工作流在用)

- 给 VLM 理解的图像:`total = 384×384`(缩到 ~0.15MP);
- 参考潜空间:`total = 1024×1024`,再按 8px 对齐(`width = round(.../8)*8`)。

### 4.3 生成尺寸

- ComfyUI 编辑链路:**VAEEncode(输入图)→ KSampler → VAEDecode**,没有独立空 latent,所以**输出分辨率 = 输入图分辨率**;
- 官方工作流模板(`image_qwen_image_edit_2511.json`)无空 latent 节点,证实这一点;
- 参考潜空间(1MP)与生成潜空间(输入尺寸)不一致时,靠 `reference_latents` conditioning 机制处理,模型按训练习惯把参考图当 1MP 语义输入。

## 五、diffusers / vLLM / 社区实现口径

- **diffusers `QwenImageEditPipeline`**:参考图自动 resize(InvokeAI PR #9155 确认缩到约 1024² 面积,匹配 `VAE_IMAGE_SIZE`,使参考 token 保持在训练分布内);
- **vLLM-Omni**:参考图按 `calculated_height/width` 预处理(PR #1265);输入图数量上限 4 张(PR #2840);
- **Eric_Qwen_Edit_Experiments**(GitHub):指出「原版 ComfyUI Qwen-Edit 实现**不保留输入分辨率**」;该补丁节点保持输入分辨率(32px 对齐),默认上限 **16MP**(可到 17MP),生成最高 **60MP** —— 想要超 1MP 输出的唯一现成方案;
- **Civitai Rebels Qwen Edit 2511 GGUF 工作流**:输入图超过 1024×1024 时,先用 `ImageScaleToTotalPixels` 缩到 **1 兆像素**,否则模型会把大输入图当成独立图层放在生成图中央;
- **Civitai 官方示例工作流(Qwen-Edit 2511 Plus)**:作者声明设计目标就是 **1024×1024 输入输出**,更大尺寸未测试。

## 六、本工作区实际用法(图片-01-文生图 修线环节)

| 环节 | 节点 | 设置 | 效果 |
|---|---|---|---|
| 分块重绘输出(6K) | — | 6K 超大图 | 不能直接进 Edit |
| 缩小 | ImageScaleBy | lanczos × 0.25 | 6K → 约 1.5K(总像素约 2.4MP) |
| 编码 | VAEEncode | 1.5K 图 | 生成潜空间 = 1.5K |
| 编辑 | TextEncodeQwenImageEditPlus | 提示词 | 参考图自动缩 1MP 供理解 |
| 输出 | VAEDecode | — | 1.5K 编辑图,再走后续放大 |

> 你的用法(先缩到 ~2.4MP 再编辑)在社区推荐范围内(1~4MP 可接受),比 1MP 更清晰、比 6K 更稳。若追求最稳可缩到 1MP(`ImageScaleToTotalPixels 1048576`)。

## 七、实操建议

1. **输入图**:总像素控制在 1~4MP(边长约 1K~2K);超过 4MP 先缩,否则易出"大图当图层放中央"或结构漂移;
2. **输出**:默认跟随输入;要超 1MP 输出,装 `Eric_Qwen_Edit_Experiments`(16MP)或分块重绘;
3. **API 模式**:直接按官方 6 种尺寸(1024×1024 / 1024×1280 / 1280×1024 / 1280×1280 / 1280×1536 / 1536×1080)传参;
4. **参考图数量**:单图最稳,多图(角色/物件融合)最多 3 张,第 4 张仅 vLLM 后端支持;
5. **对齐**:ComfyUI 内尺寸保持 8 的倍数(latent /8 对齐),外部补丁节点按 32px 对齐。

---

> 主要来源:阿里云百炼 qwen-image-edit API 文档、RunPod Qwen-Image-Edit-2511 文档、ComfyUI v0.30.0 `comfy_extras/nodes_qwen.py`(已逐行核对)、QwenLM/Qwen-Image 官方仓库、EricRollei/Eric_Qwen_Edit_Experiments、vllm-project/vllm-omni PR #1265/#2840、InvokeAI PR #9155、Civitai Rebels 与官方示例工作流。
