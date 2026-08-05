# ComfyUI 全模态工作流方案

> 图片 8 + 音频 6 + 视频 6，共 20 个工作流。模型统一放 `models\` 对应子目录（`ComfyUI\models` 为软链接）。
> 下载规则：直连失败时走代理 `127.0.0.1:7890`；国内可用 `hf-mirror.com` 镜像。
> 方案原则：全开源、本地推理、零 API 费用（ACE-Step 1.5 / Stable Audio 3 / Qwen3-TTS）。

## 一、工作流总览

### 图片类（8 个，模型已全部就绪）

| # | 工作流 | 核心模型 |
|---|--------|---------|
| 1 | 文生图 T2I（928×1664 竖版） | Qwen-Image-2512 |
| 2 | 参考图生图 I2I（风格/角色参考） | FLUX.2 Klein 9B |
| 3 | 图片指令修改（换装/换背景/改元素） | Qwen-Image-Edit 2511 |
| 4 | 图片四周扩大 Outpaint | Qwen-Edit 2511 + Klein 9B + LaMa 预填充（可选） |
| 5 | 图片中心放大/局部重绘 Inpaint | Klein 9B + 掩码（手动/SAM3） |
| 6 | 物体移除 | Klein 9B + 掩码扩张 |
| 7 | 图片放大/超清（3~4 倍，8 整除） | 4x-UltraSharp |
| 8 | 三视图/多角度生成 | Qwen-Edit 2511 + 多角度 LoRA |

### 音频类（6 个）

| # | 工作流 | 核心模型 | 状态 |
|---|--------|---------|------|
| 1 | 音乐/歌曲生成 | ACE-Step 1.5（内置 nodes_ace、turbo_aio；低显存可选 split 版） | 需下载 |
| 2 | 背景音乐/纯器乐 | Stable Audio 3 | **已就绪** |
| 3 | 环境音/音效 | Stable Audio 3（SFX/One-shot 类别） | **已就绪** |
| 4 | 情绪语音生成（8 种情绪） | Qwen3-TTS（情感标签）；备用 IndexTTS-2 | 需下载 |
| 5 | 人物说话·参考音色克隆 | Qwen3-TTS 声音克隆（3s 参考音频）；备用 F5-TTS | 需下载 |
| 6 | 多角色对话/混音 | Qwen3-TTS RoleBank+AdvancedDialogue | 需装插件 |

### 视频类（6 个，MiniMax H3）

文生视频 T2V / 图生视频 I2V / 首帧参考 / 首尾帧 / 多图参考 / 图像+音频参考 —— 全部需下载。

## 二、模型下载清单

### 图片类

| 模型 | 放置目录 | 状态 | 下载地址 |
|------|---------|------|---------|
| `qwen_image_2512_fp8_e4m3fn.safetensors` | `models\diffusion_models\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors> |
| `qwen_image_edit_2511_bf16.safetensors` | `models\diffusion_models\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors> |
| `flux-2-klein-9b-fp8.safetensors` | `models\diffusion_models\` | ✅ 已就绪 | <https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-fp8/resolve/main/flux-2-klein-9b-fp8.safetensors> ⚠️门控 |
| `qwen_3_8b_fp8mixed.safetensors`（Klein 文本编码器） | `models\text_encoders\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/flux2-klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors> |
| `full_encoder_small_decoder.safetensors`（Klein/FLUX.2 解码器） | `models\vae\` | ✅ 已就绪 | <https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/resolve/main/full_encoder_small_decoder.safetensors> |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors`（Qwen-Edit 文本编码器） | `models\text_encoders\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors> |
| `qwen_image_vae.safetensors` | `models\vae\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors> |
| `4x-UltraSharp.pth`（放大，已验证可下） | `models\upscale_models\` | ✅ 已就绪 | <https://huggingface.co/lokCX/4x-Ultrasharp/resolve/main/4x-UltraSharp.pth> |
| `sam3.1_multiplex_fp16.safetensors`（自动掩码，可选） | `models\checkpoints\` | ⬇️ 可选 | <https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors> |
| LaMa/MAT 预填充（可选，装 Acly ComfyUI-Inpaint-Nodes 后） | 插件自动下载 | ⬇️ 可选 | 随 [ComfyUI-Inpaint-Nodes](https://github.com/Acly/ComfyUI-Inpaint-Nodes) 安装 |

### 音频类

| 模型 | 放置目录 | 状态 | 下载地址 |
|------|---------|------|---------|
| `stable_audio_3_medium.safetensors` | `models\checkpoints\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/stable-audio-3/resolve/main/checkpoints/stable_audio_3_medium.safetensors> |
| `t5gemma_b_b_ul2.safetensors`（StableAudio 文本编码器） | `models\text_encoders\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/stable-audio-3/resolve/main/text_encoders/t5gemma_b_b_ul2.safetensors> |
| `ace_step_1.5_turbo_aio.safetensors`（音乐/歌曲） | `models\checkpoints\` | ⬇️ 需下载 | <https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/checkpoints/ace_step_1.5_turbo_aio.safetensors> |
| ACE-Step 1.5 split 版（低显存替代 AIO） | `diffusion_models`+`text_encoders`+`vae` | ⬇️ 可选 | `acestep_v1.5_turbo.safetensors` + `qwen_0.6b_ace15`（歌词质量选 `qwen_4b_ace15`）+ `ace_1.5_vae.safetensors`，均见 <https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files> |
| Qwen3-TTS-12Hz-1.7B-Base（万能：克隆+对话） | 插件自动下载至 `models/TTS/Qwen/` | ⬇️ 需下载 | <https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base>（默认走 ModelScope 国内源） |
| Qwen3-TTS-12Hz-1.7B-CustomVoice（预设音色，可选） | 同上 | ⬇️ 可选 | <https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice> |
| IndexTTS-2 全套（情绪语音备用，含 gpt/s2mel/bigvgan 等） | TTS-Audio-Suite 目录 | ⬇️ 可选 | <https://huggingface.co/IndexTeam/IndexTTS-2>（镜像 [AEmotionStudio/index-tts-2-models](https://huggingface.co/AEmotionStudio/index-tts-2-models)） |
| F5-TTS（参考音色克隆备用，最快零样本） | TTS-Audio-Suite 目录 | ⬇️ 可选 | <https://huggingface.co/SWivid/F5-TTS> |
| CosyVoice3（跨语言克隆，可选） | TTS-Audio-Suite 目录 | ⬇️ 可选 | 随 [TTS-Audio-Suite](https://github.com/diodiogod/TTS-Audio-Suite) 文档 |
| `qwen3.5_2b_bf16.safetensors`（音频编码） | `models\text_encoders\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/Qwen3.5/resolve/main/text_encoders/qwen3.5_2b_bf16.safetensors> |

### 视频类（MiniMax H3，Comfy-Org/MiniMax-H3 仓库）

| 模型 | 放置目录 | 状态 | 下载地址 |
|------|---------|------|---------|
| `minimax_h3_fl2va_pruned_int8_convrot.safetensors`（FL2VA 扩散模型，T2V/I2V 用） | `models\diffusion_models\` | ⬇️ 需下载 | <https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors> |
| `minimax_h3_ref2va_pruned_int8_convrot.safetensors`（Ref2VA 扩散模型，**R2V 参考生视频用，独立文件**） | `models\diffusion_models\` | ⬇️ 需下载 | <https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors> |
| `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors`（文本编码器） | `models\text_encoders\` | ⬇️ 需下载 | <https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors> |
| `minimax_h3_video_vae_fp16.safetensors`（视频 VAE） | `models\vae\` | ⬇️ 需下载 | <https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_fp16.safetensors> |
| `minimax_h3_audio_vae_fp32.safetensors`（音频 VAE） | `models\vae\` | ⬇️ 需下载 | <https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors> |

> **fl2va 与 ref2va 是同一基座的任务变体**：`视频-01 文生视频` 用 fl2va，`视频-02/03/04`（首帧/首尾帧/参考图音视频）用 ref2va，两者都要下。仓库另有 bf16/int8_convrot/pruned_fp8_scaled 档可选。

## MiniMax H3 加速方案（2026-08 社区现状）

| 方案 | 提速 | 做法 | 代价 |
|------|------|------|------|
| Sage Attention | +20~30% | KJNodes `Patch Sage Attention KJ` 节点（已有 KJNodes） | 无害 dtype 警告 |
| EasyCache | 显著 | 参数 0.30/0.20/0.90 | 失帧/模糊，长视频连贯性下降 |
| GGUF 量化 | 显存↓ | `qwen3vl-32B-MiniMax-H3-Q4_K.gguf`（Q2 效果差） | 社区有分歧，需 A/B |
| INT4 文本编码器 | 显存↓ | 替代 nvfp4_awq | 更小可用 |
| 显存优化 | 防 OOM | `🎈VRAM/RAM-Cleanup` 节点；启动 `--fast-disk`、`--vram-headroom` | 编码器频繁重载 |
| Lightning 蒸馏 LoRA | 未来 | 尚未发布，等社区蒸馏 | — |

**低显存**：8G/12G/16G 均可跑（动态卸载，clip 编码器放 CPU）；本地最高 768p，2K 需官方 API。

## 三、需安装的插件

| 插件 | 用途 | 地址 |
|------|------|------|
| ComfyUI-Qwen3-TTS | 开源 TTS 主方案（克隆/音色设计/情绪标签/无限多角色对话，Apache-2.0） | <https://github.com/wanaigc/ComfyUI-Qwen3-TTS> |
| TTS-Audio-Suite（可选备用） | IndexTTS-2/F5-TTS/CosyVoice3（情绪/克隆/SRT） | <https://github.com/diodiogod/TTS-Audio-Suite> |
| ComfyUI-Inpaint-Nodes（可选） | LaMa/MAT 预填充、ColorMatch 接缝修复 | <https://github.com/Acly/ComfyUI-Inpaint-Nodes> |
| ComfyUI-Angelo（可选） | Klein 点击式编辑（2026 趋势） | <https://github.com/shootthesound/ComfyUI-Angelo> |

## 四、镜像地址（国内直连可用时优先）

将上方地址 `huggingface.co` 前缀替换为 `hf-mirror.com` 即可，例：
`https://hf-mirror.com/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_fp16.safetensors`

## 五、注意事项

- **门控仓库**：`black-forest-labs/FLUX.2-klein-9b-fp8` 需登录 HF 并接受 BFL 协议
- **显存**：Klein 9B 蒸馏版占用较高（24G 卡跑 1024 tile 偏紧，爆显存时降到 768）；MiniMax H3 需大显存，低显存建议量化或云端
- **下载顺序建议**：先补音频小件（ACE-Step、Qwen3-TTS）→ 视频大件（MiniMax H3 全套 5 文件，fl2va 与 ref2va 都要下）
- 模型放好后重启 ComfyUI；`stable_audio_3_medium` + `t5gemma` 已就绪，背景音乐工作流可立即运行