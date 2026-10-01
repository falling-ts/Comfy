# AutoDL 云模型软链报告

数据源 `webs/AutoDL/models.md`(5063 行)。源 = 「实例路径」列(云库文件本身), 目标 = `models/<本地目录>/<模型名称>`(本地目录含 `/` 时先建仓库子目录), 相对软链; 目标已存在(真实文件或旧链接)一律跳过、绝不覆盖。

本次建链 **388** 条。

| 分类 | 行数 |
|---:|---|
| 本次建链 | 388 |
| 目标已存在(本机已有, 未覆盖) | 2707 |
| 未识别跳过 | 872 |
| 同名同源(重复上传)去重 | 779 |
| 同名多源冲突(留最新) | 306 |
| 文件名不安全跳过 | 10 |
| 源文件缺失 | 1 |

## 本次新建软链(388 条)

### `ASR` (15)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/ASR/base.en.pt` | `/.autodl/7e/34/6b/7e346b00288f71609da408e835c709eb` | 2026-03-18 18:01 |
| `models/ASR/base.pt` | `/.autodl/5d/a5/32/5da532a9c096eff1c7c00e989fe58da3` | 2026-03-18 18:01 |
| `models/ASR/config.json` | `/.autodl/9a/97/b0/9a97b08e545dce3e9d49c5351945c708` | 2026-09-21 09:29 |
| `models/ASR/large-v1.pt` | `/.autodl/9b/5f/07/9b5f07bc2d2e1498ea287a5c3eb19820` | 2026-03-18 18:31 |
| `models/ASR/large-v2.pt` | `/.autodl/66/87/64/668764447eeda98eeba5ef7bfcb4cc3d` | 2026-03-18 18:31 |
| `models/ASR/large-v3.pt` | `/.autodl/01/7b/aa/017baacdaada84d0d5cb030140875b65` | 2026-03-18 18:01 |
| `models/ASR/medium.en.pt` | `/.autodl/93/b2/a3/93b2a3c05cdfc49cfff286d580458667` | 2026-03-18 18:31 |
| `models/ASR/model-00001-of-00002.safetensors` | `/.autodl/37/86/7f/37867feeaeb3243041197f60b0ef3ed7` | 2026-09-24 23:31 |
| `models/ASR/model-00002-of-00002.safetensors` | `/.autodl/ff/88/a5/ff88a5cf43203fd87d505b749f8456b3` | 2026-09-24 23:39 |
| `models/ASR/model.safetensors` | `/.autodl/c2/7e/fa/c27efa5e05a73b7c73dc146ef0fd2082` | 2026-09-14 21:48 |
| `models/ASR/preprocessor_config.json` | `/.autodl/5b/9e/b2/5b9eb2d81599b4e21d51c81ea23bb1f6` | 2026-09-21 09:30 |
| `models/ASR/pytorch_model.bin` | `/.autodl/91/3d/a0/913da0bb0494f505cc3a59dde5e86fb9` | 2026-09-21 09:31 |
| `models/ASR/tiny.en.pt` | `/.autodl/c0/7b/25/c07b25a762e6ce14b8374d7a4420c3cf` | 2026-03-18 18:01 |
| `models/ASR/tiny.pt` | `/.autodl/a4/eb/10/a4eb109400a70c83ef9e367439118e81` | 2026-03-18 18:01 |
| `models/ASR/unet.pth` | `/.autodl/TMElyralab/MuseTalk/musetalkV15/unet.pth` | 2026-09-21 10:58 |

### `ASR/whisper-large-v3` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/ASR/whisper-large-v3/whisper_large_v3_fp16.safetensors` | `/.autodl/openai/whisper-large-v3/model.safetensors` | 2025-11-26 14:32 |

### `LLM` (7)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/LLM/Gemma-4-E4B-Uncensored-HauhauCS-Aggressive-Q4_K_P.gguf` | `/.autodl/b7/82/1d/b7821da8c11673bdf3635f815bc245e9` | 2026-09-16 11:04 |
| `models/LLM/Qwen3-VL-30B-A3B-Thinking-Q4_K_M.gguf` | `/.autodl/dd/8f/11/dd8f110a94d0bd2802ee2707c2797981` | 2026-09-16 19:32 |
| `models/LLM/Qwen3.5-4B-Uncensored-HauhauCS-Aggressive-Q4_K_M.gguf` | `/.autodl/92/ca/b1/92cab1ccd9d4a60e3dcbfe188534dcf5` | 2026-09-24 18:27 |
| `models/LLM/Qwen3.8-27B-Uncensored-Q4_K_M.gguf` | `/.autodl/72/ef/4e/72ef4e0b724139395b5d8b3004bdb341` | 2026-09-16 19:01 |
| `models/LLM/Qwen3.8-27B-Uncensored-Q8_0.gguf` | `/.autodl/60/da/c3/60dac3022ba15f185e0abdacd433b5ee` | 2026-09-16 19:01 |
| `models/LLM/mmproj-Qwen3.5-4B-Uncensored-HauhauCS-Aggressive-BF16.gguf` | `/.autodl/60/55/c4/6055c43fd0d62fb3e316f2d1184343c9` | 2026-09-24 17:53 |
| `models/LLM/qwen3.8_27b_w4a8.safetensors` | `/.autodl/48/de/01/48de012e74df01c937134e3f6b98c079` | 2026-09-28 08:11 |

### `LLM/xinlingjun` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/LLM/xinlingjun/aa1851b9-b539-5a87-84f3-96b629969f14.safetensors` | `/.autodl/12/20/ec/1220eca4c92ed96918dc26a4b0ade184` | 2025-09-23 19:44 |

### `TTS` (3)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/TTS/DiT_seed_v2_uvit_whisper_base_f0_44k_bigvgan_pruned_ft_ema_v2.pth` | `/.autodl/63/3e/c7/633ec705943831758ee384d26b3fe9fc` | 2026-09-14 21:49 |
| `models/TTS/auk_flash.safetensors` | `/.autodl/10/40/76/104076b3a8e5b2dd0efad5470574e9f6` | 2026-09-22 13:42 |
| `models/TTS/qwen3-tts-design-1.7b.safetensors` | `/.autodl/34/12/a1/3412a1109ee5b88cf3e3ce315ab29663` | 2026-09-24 23:34 |

### `TTS/Breeze-TTS-2-comfyui` (5)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/TTS/Breeze-TTS-2-comfyui/Breeze-TTS-2-bf16.safetensors` | `/.autodl/7b/c4/62/7bc4628a2398483081aef21b4fb24ba6` | 2026-09-08 01:10 |
| `models/TTS/Breeze-TTS-2-comfyui/LICENSE.txt` | `/.autodl/c7/2b/c4/c72bc4b511cbcf71c23347942e077c0e` | 2026-09-07 20:15 |
| `models/TTS/Breeze-TTS-2-comfyui/NOTICE.txt` | `/.autodl/9b/68/6d/9b686dc0fb53fb7079af59ff455fb79d` | 2026-09-07 20:15 |
| `models/TTS/Breeze-TTS-2-comfyui/model.safetensors` | `/.autodl/cc/f5/bd/ccf5bd95ff388925556b42371ff72502` | 2026-09-07 20:16 |
| `models/TTS/Breeze-TTS-2-comfyui/qwen3-tts-speech-tokenizer.safetensors` | `/.autodl/cc/f5/bd/ccf5bd95ff388925556b42371ff72502` | 2026-09-24 23:39 |

### `background_removal` (4)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/background_removal/birefnet.py` | `/.autodl/fa/5b/4f/fa5b4f0ac243012e2cf04fcad94088e6` | 2026-08-26 22:00 |
| `models/background_removal/d6d3df01-1a1f-5ffd-bc39-feb9f9f5aaaf.safetensors` | `/.autodl/bd/ac/41/bdac4113ecca6558871b7b96948601f4` | 2025-09-23 19:44 |
| `models/background_removal/matanyone2.pth` | `/.autodl/b1/d3/cf/b1d3cfbb7596ecf3b88391198427ca95` | 2026-09-18 12:20 |
| `models/background_removal/rmbg2model.safetensors` | `/.autodl/bd/ac/41/bdac4113ecca6558871b7b96948601f4` | 2025-11-30 22:56 |

### `background_removal/ComfyUI-BiRefNet` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/background_removal/ComfyUI-BiRefNet/BiRefNet-matting.safetensors` | `/.autodl/b9/b2/62/b9b262d97adc59cc5bd689ebd4e0f831` | 2026-09-17 22:23 |
| `models/background_removal/ComfyUI-BiRefNet/Matting.safetensors` | `/.autodl/b9/b2/62/b9b262d97adc59cc5bd689ebd4e0f831` | 2026-04-28 15:11 |

### `checkpoints` (7)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/checkpoints/anything_v3.yaml` | `/.autodl/3f/70/94/3f7094ffef5088fdb561cc159159b809` | 2026-09-09 10:34 |
| `models/checkpoints/diffusion_pytorch_model.safetensors` | `/.autodl/ef/2f/9d/ef2f9d0a1e0cb053e580e6e9bdc87d90` | 2025-10-10 16:13 |
| `models/checkpoints/ema_model.safetensors` | `/.autodl/97/4d/2e/974d2e8435bdb9fe3b51884bde4e1139` | 2026-09-18 12:19 |
| `models/checkpoints/makinaMix_v22.safetensors` | `/.autodl/bc/ea/e5/bceae5dd2aae0a53af29e09756bcee62` | 2026-09-14 12:31 |
| `models/checkpoints/miaomiaoHarem_29BBETA11.safetensors` | `/.autodl/74/30/87/743087023e74dd5186ba931773fbbad1` | 2026-09-30 00:13 |
| `models/checkpoints/v1-inference_clip_skip_2.yaml` | `/.autodl/3f/70/94/3f7094ffef5088fdb561cc159159b809` | 2026-09-09 10:44 |
| `models/checkpoints/比鲁斯极简中古室内_V0.2.safetensors` | `/.autodl/bf/6a/35/bf6a3563bd5c77396240aaa85b7cdd5f` | 2026-07-25 08:45 |

### `checkpoints/ComfyUI-ACE-Step` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/checkpoints/ComfyUI-ACE-Step/ace_step_1.5_turbo_aio.safetensors` | `/.autodl/b0/de/5e/b0de5ee7c1837ed36c302e2924dff11f` | 2026-09-17 16:26 |

### `checkpoints/ComfyUI-IC-Light` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/checkpoints/ComfyUI-IC-Light/Realistic_Vision_V5.1_fp16-no-ema.safetensors` | `/.autodl/f7/f7/ac/f7f7ac1fd458f17968e02392ab7ef9c1` | 2026-09-17 15:27 |

### `checkpoints/models` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/checkpoints/models/161d596a-f092-5a14-9a74-e50d05a61857.safetensors` | `/.autodl/45/73/0c/45730c869795aa67ed8109cff7fafd78` | 2025-09-23 19:43 |

### `classifiers` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/classifiers/wan2.2_dancer_14b_global_fp8_scaled.safetensors` | `/.autodl/b7/7c/cc/b77ccc8cb200bd15317b1438ba8d5cfd` | 2026-09-10 02:36 |
| `models/classifiers/wan2.2_dancer_14b_local_fp8_scaled.safetensors` | `/.autodl/e4/c7/ee/e4c7eeb11bc7da0b9a7350671cb9089a` | 2026-09-10 02:40 |

### `clip` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/clip/model.fp16.safetensors` | `/.autodl/81/b8/7e/81b87e641699a4cd5985f47e99e71eeb` | 2025-11-10 17:28 |
| `models/clip/model.safetensors` | `/.autodl/f4/c8/87/f4c887e55e159f96453e18a1d6ca984f` | 2025-11-13 03:33 |

### `clip/clip-vit-large-patch14` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/clip/clip-vit-large-patch14/525bcc12-1c24-5ffd-8aca-e5d0ef1c1b81.safetensors` | `/.autodl/openai/clip-vit-large-patch14/model.safetensors` | 2025-09-23 19:43 |
| `models/clip/clip-vit-large-patch14/clip-vit-large-patch14.safetensors` | `/.autodl/openai/clip-vit-large-patch14/model.safetensors` | 2025-10-10 02:48 |

### `clip_vision` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/clip_vision/latest.ckpt` | `/.autodl/b7/8c/bf/b78cbfb95852ea7299ed1bf9c15fe384` | 2026-01-05 23:18 |
| `models/clip_vision/tf_model.h5` | `/.autodl/3a/e5/a6/3ae5a679cbccb4bf76a783acdccf4252` | 2026-01-05 23:19 |

### `clip_vision/models` (3)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/clip_vision/models/14234924-855d-55cc-8ff1-ec34ad59d5c4.safetensors` | `/.autodl/ed/38/a0/ed38a0b229471ee0c1826a6ddb658083` | 2025-09-23 19:43 |
| `models/clip_vision/models/CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors` | `/.autodl/ed/38/a0/ed38a0b229471ee0c1826a6ddb658083` | 2025-10-10 02:55 |
| `models/clip_vision/models/CLIP-ViT-H-14.safetensors` | `/.autodl/ed/38/a0/ed38a0b229471ee0c1826a6ddb658083` | 2026-02-20 14:48 |

### `controlnet` (8)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/controlnet/control_v11f1e_sd15_tile.pth` | `/.autodl/84/b5/bd/84b5bd6710faad3e9f5989df8705276c` | 2026-09-14 12:17 |
| `models/controlnet/control_v11f1p_sd15_depth.pth` | `/.autodl/9f/89/1e/9f891e7a6464993aa9b34571ad56dc97` | 2026-09-14 12:21 |
| `models/controlnet/controlnet-union-sdxl-1.0.safetensors` | `/.autodl/17/98/4c/17984cb5a1233ce873e0939f7ad030cf` | 2025-09-30 14:11 |
| `models/controlnet/diffusers_xl_canny_full.safetensors` | `/.autodl/ac/a2/40/aca2403a1b6d7cb163870a937bafeb3d` | 2026-09-14 13:18 |
| `models/controlnet/minimax_h3_fun_controlnet_union_2.0_pruned_bf16.safetensors` | `/.autodl/7f/be/74/7fbe74e276c4d9e91a09d3f3b3ec7008` | 2026-09-23 23:12 |
| `models/controlnet/minimax_h3_fun_controlnet_union_2.0_pruned_int8_convrot.safetensors` | `/.autodl/1d/5a/10/1d5a108256d815ea4f5f2dbd1578c5ed` | 2026-09-23 23:05 |
| `models/controlnet/photomaker-v1.bin` | `/.autodl/f1/6f/70/f16f70b3a7d79e938a195c610627f4ed` | 2025-10-10 15:43 |
| `models/controlnet/qwen_image_layered_control_bf16.safetensors` | `/.autodl/ff/63/33/ff633360e3d73c8bead14399d61f2115` | 2026-09-12 17:33 |

### `controlnet/xinlingjun` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/controlnet/xinlingjun/296ed393-1192-504d-b8cb-3a1c0909f609.safetensors` | `/.autodl/99/94/ef/9994ef96bb3b2eb6fb4cb45e553f60aa` | 2025-09-23 19:43 |

### `detection` (6)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/detection/args.json` | `/.autodl/0a/cb/9e/0acb9e9dd8dcc63a040aaa793dc44666` | 2026-09-14 11:33 |
| `models/detection/deeplabv3p-resnet50-human.onnx` | `/.autodl/b6/7e/54/b67e5419f86fb147ed9e01a5b45f814c` | 2026-09-18 08:15 |
| `models/detection/dinov2_vitl14.safetensors` | `/.autodl/01/74/59/017459f62f369b07f5b3da66ac715f47` | 2026-09-18 12:20 |
| `models/detection/sam_3d_body_dinov3_bf16.safetensors` | `/.autodl/26/38/07/263807c8ec22254e4dce6f7cb9f9c526` | 2026-08-25 12:45 |
| `models/detection/sam_3d_body_dinov3_int8_convrot.safetensors` | `/.autodl/7d/e0/36/7de0360270decba2a45705d60ff7cf53` | 2026-08-25 12:47 |
| `models/detection/yolo11x-pose.pt` | `/.autodl/67/fd/a4/67fda45f349142193129dabaf530cda9` | 2026-04-07 14:19 |

### `diffusion_models` (74)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/diffusion_models/10Eros_Max_h3_TURBO-hybrid_beta5_int8.safetensors` | `/.autodl/71/67/de/7167de8a44fb4ec0a9802f062ae4af05` | 2026-09-10 21:47 |
| `models/diffusion_models/10Eros_Max_h3_TURBO-hybrid_beta5_w4a8_14gb_optimized.safetensors` | `/.autodl/ae/b0/f3/aeb0f3189472f388fc5a70f47c7b96dd` | 2026-09-11 00:06 |
| `models/diffusion_models/10Eros_Max_h3_hybrid_beta5_w4a8_14gb_optimized.safetensors` | `/.autodl/ce/ec/d6/ceecd601ced18e5a0c284f2ff580bfd9` | 2026-09-11 01:26 |
| `models/diffusion_models/Anima-2.9B-preview-v1.safetensors` | `/.autodl/d9/46/d5/d946d5873c875c172532e3b493658bf9` | 2026-09-23 22:20 |
| `models/diffusion_models/DasiwaMinimaxH3_dasiwaHybridTurboV2_int8.safetensors` | `/.autodl/ab/6a/bd/ab6abd151ac34bb2154a3a5217c1a32c` | 2026-09-12 16:30 |
| `models/diffusion_models/DasiwaMinimaxH3_dasiwaHybridV2_int8.safetensors` | `/.autodl/2a/3e/8c/2a3e8cc7800537e52f903359ed7ed534` | 2026-09-12 01:54 |
| `models/diffusion_models/DasiwaMinimaxH3_dasiwaREF2VAHybridV1_0.safetensors` | `/.autodl/25/02/5c/25025ca02c025d460189c70a08c6b3e6` | 2026-09-09 13:34 |
| `models/diffusion_models/FLUX.1-Kontext-dev-fp8_v1.safetensors` | `/.autodl/97/fc/c2/97fcc25721fc704ddf7502b6bfd81569` | 2026-09-15 01:19 |
| `models/diffusion_models/FireRed-Image-Edit-1.1-transformer.safetensors` | `/.autodl/6c/f8/55/6cf855417ae5d123651585f4c760cfc6` | 2026-09-23 00:03 |
| `models/diffusion_models/FrameRush-Minimax-V2_c2-st1500-F32.safetensors` | `/.autodl/a6/18/6f/a6186fef9778138e768e539f7c769057` | 2026-09-12 16:41 |
| `models/diffusion_models/GunFu.safetensors` | `/.autodl/99/5f/0c/995f0cd3ff18bc727d44f3286696eacd` | 2026-09-30 16:01 |
| `models/diffusion_models/HDR360.safetensors` | `/.autodl/a7/19/4a/a7194a2a52cdd33b541bedeb019907ca` | 2026-07-24 21:50 |
| `models/diffusion_models/Image-Turbo-INT8.safetensors` | `/.autodl/6e/f5/27/6ef5271016a28f1bb08b60d76f7b9832` | 2026-09-08 14:49 |
| `models/diffusion_models/Klein-yizhixing-lora.safetensors` | `/.autodl/ee/d9/39/eed9390e24862ace28749dc7308f23f5` | 2026-03-09 00:04 |
| `models/diffusion_models/Krea2-Moody-Mix-premium_int8_convrot.safetensors` | `/.autodl/09/11/3c/09113c363d77831ea1b172bb9aea0766` | 2026-09-17 23:26 |
| `models/diffusion_models/Krea2_Anything2RealCharacters-V2.5_int8.safetensors` | `/.autodl/23/c8/e0/23c8e09004f5370c5ba695a3ac514c85` | 2026-09-10 09:39 |
| `models/diffusion_models/LTX-2.3-Transition-LORA.safetensors` | `/.autodl/af/12/28/af12285d229974499cd6120f22823cb8` | 2026-04-13 22:07 |
| `models/diffusion_models/Minimax H3真实电影质感V0.1.safetensors` | `/.autodl/5a/11/e8/5a11e8ed0ddb04d11b0cac231dc1c8f3` | 2026-09-09 10:47 |
| `models/diffusion_models/Minimax-h3_Singularity_ref2va_Pruned_v1.3_int8.safetensors` | `/.autodl/36/9a/d1/369ad107b1f6a6492bbd56b050f959ce` | 2026-09-14 13:23 |
| `models/diffusion_models/Minimax-h3_Singularity_ref2va_v1.3_Pruned_w4a8.safetensors` | `/.autodl/a0/48/a1/a048a15b8ac5677b2516a40d99d7be80` | 2026-09-21 08:44 |
| `models/diffusion_models/Minimax-h3_Singularity_ref2va_v1.3_int8.safetensors` | `/.autodl/95/c5/8e/95c58e55d163c3204243276ac6e56e4e` | 2026-09-14 13:30 |
| `models/diffusion_models/PS创城fp8.safetensors` | `/.autodl/a0/42/86/a04286ae9609fe9fd7fc6429e2ffc56f` | 2026-09-15 00:10 |
| `models/diffusion_models/Put_it_here_V4.2.safetensors` | `/.autodl/d2/51/d0/d251d0b445f8af72016cbaee28ba7b20` | 2026-07-25 14:50 |
| `models/diffusion_models/QuadView_krea2_v1.safetensors` | `/.autodl/ed/22/c7/ed22c7a00199d8953e1268f269e53ae1` | 2026-09-09 11:46 |
| `models/diffusion_models/REDQW21-UNLOCKED-v1-BF16-ComfyMCP-builtwithqwen.safetensors` | `/.autodl/38/e7/5b/38e75b1cd0cb99fc42af1baabe64aa57` | 2026-09-26 00:25 |
| `models/diffusion_models/RedCraft-HighNoise-MASO-MangaDrama-Krea2Turbo-RedMix-v4.safetensors` | `/.autodl/7c/cf/c3/7ccfc3946809dbb251506134d711e7aa` | 2026-09-18 18:38 |
| `models/diffusion_models/RedCraft-LowNoise-MASO-MangaDrama-Krea2Turbo-RedMix-v4.safetensors.safetensors` | `/.autodl/7f/6a/9e/7f6a9e5470bb2911b9f4f4c1ee8de959` | 2026-09-12 16:30 |
| `models/diffusion_models/T_S_anima_baseV10.safetensors` | `/.autodl/dd/d2/e2/ddd2e28cd13b6a823dcbffa749a555c6` | 2026-09-19 21:18 |
| `models/diffusion_models/Wan2.2-I2V-SlopBounce-Low-i2v-(弹跳lora不变脸).safetensors` | `/.autodl/95/42/79/9542790d550e8acceec6a49e99440c06` | 2026-04-10 15:51 |
| `models/diffusion_models/anima-turbo-v1.1.safetensors` | `/.autodl/db/b3/02/dbb30271999bd460b77f86e449ee6a01` | 2026-09-30 08:00 |
| `models/diffusion_models/custom_node_hyperflow_8step_v1.0_comfyui.safetensors` | `/.autodl/d8/41/56/d84156c67617bba02a931b4672975cbf` | 2026-09-19 19:51 |
| `models/diffusion_models/custom_node_hyperflow_8step_v1.0_comfyui_pruned.safetensors` | `/.autodl/50/59/ab/5059abd623ac7169b37a883ac1f056d9` | 2026-09-19 19:51 |
| `models/diffusion_models/fastvideo_fasth3_8step_v2_pruned_bf16.safetensors` | `/.autodl/b8/5f/5a/b85f5a556082e8488efb5cc205c13814` | 2026-09-16 21:42 |
| `models/diffusion_models/fastvideo_fasth3_8step_v2_pruned_int8_convrot.safetensors` | `/.autodl/97/de/0a/97de0ad1b814569d95d71252e0c60b0f` | 2026-09-16 15:36 |
| `models/diffusion_models/joyai_image_edit_bf16.safetensors` | `/.autodl/32/68/ad/3268ad9b3f05049c365c38a0d63f515c` | 2026-09-11 04:41 |
| `models/diffusion_models/joyai_image_edit_int8_convrot.safetensors` | `/.autodl/d8/61/64/d86164e549e57be3caaa2bd7633dc569` | 2026-09-11 04:38 |
| `models/diffusion_models/krea2Anime_v14_int4.safetensors` | `/.autodl/6b/8e/6f/6b8e6f18f34aaa1dba4f5a5ce7361420` | 2026-09-28 11:01 |
| `models/diffusion_models/krea2Anime_v14_int8.safetensors` | `/.autodl/cb/49/52/cb4952b9a8f196351292367a62463dc4` | 2026-09-29 05:52 |
| `models/diffusion_models/ming_image_0.1_design_bf16.safetensors` | `/.autodl/69/b7/5b/69b75b35e549318470911135eeacebd2` | 2026-09-28 09:18 |
| `models/diffusion_models/ming_image_0.1_design_int8_convrot.safetensors` | `/.autodl/c2/26/31/c2263131ea4729886886473e19cc107f` | 2026-09-28 09:04 |
| `models/diffusion_models/ming_image_0.1_design_layer_bf16.safetensors` | `/.autodl/46/02/47/46024716801d2374ec54d5c9b1a25a4d` | 2026-09-28 09:10 |
| `models/diffusion_models/ming_image_0.1_design_layer_int8_convrot.safetensors` | `/.autodl/6a/09/54/6a095445c870c4a362e68c7fbcca1767` | 2026-09-28 09:16 |
| `models/diffusion_models/ming_image_0.1_ling_mini_2.0_bf16.safetensors` | `/.autodl/10/d2/55/10d25554b480c0bb534979a7673c28d0` | 2026-09-28 15:34 |
| `models/diffusion_models/ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors` | `/.autodl/ea/81/20/ea8120e0d89b5e91547fec7caecb2197` | 2026-09-28 13:47 |
| `models/diffusion_models/ming_image_0.1_ling_mini_2.0_layer_bf16.safetensors` | `/.autodl/09/b0/10/09b01018a667a29471b45f8d0aecc334` | 2026-09-28 22:53 |
| `models/diffusion_models/ming_image_0.1_ling_mini_2.0_layer_int8_convrot.safetensors` | `/.autodl/f3/b4/21/f3b4212a553ee9dc3999e8eaeede8c27` | 2026-09-28 13:33 |
| `models/diffusion_models/ming_image_0.1_ling_mini_2.0_w4a8.safetensors` | `/.autodl/48/30/17/483017ea61c273289b0704ce358fdec8` | 2026-09-28 13:36 |
| `models/diffusion_models/minimaxH3枪斗术GunFu.safetensors` | `/.autodl/99/5f/0c/995f0cd3ff18bc727d44f3286696eacd` | 2026-09-16 21:01 |
| `models/diffusion_models/minimax_h3_delta_fl2va_ref2va_r1024_fp8_scaled.safetensors` | `/.autodl/c0/98/b8/c098b8de141f381463dc3f4ea3142ac9` | 2026-09-08 14:19 |
| `models/diffusion_models/minimax_h3_fl2v_turbo_4step_v1.1_768p_fp8.safetensors` | `/.autodl/af/bd/66/afbd66f4930eb18a201fa10231b8ccba` | 2026-09-11 01:26 |
| `models/diffusion_models/minimax_h3_fl2va_4step_quantfunc_int4_r128.safetensors` | `/.autodl/27/ec/8b/27ec8b0ee2be6a0891ddef94ad5e90f2` | 2026-09-29 08:42 |
| `models/diffusion_models/minimax_h3_hyperflow_8step_v1.0_comfyui_bf16.safetensors` | `/.autodl/45/43/ea/4543eafeb2b1ced00928c178601a5503` | 2026-09-19 17:41 |
| `models/diffusion_models/minimax_h3_hyperflow_8step_v1.0_comfyui_pruned_bf16.safetensors` | `/.autodl/a4/63/d4/a463d4ac4ce222e6bd8655e9bf367e43` | 2026-09-19 17:41 |
| `models/diffusion_models/minimax_h3_ref2va_8steps_quantfunc_int4_r128.safetensors` | `/.autodl/a1/dd/ef/a1ddef91931f632b52015ec0b6acafc8` | 2026-09-29 08:45 |
| `models/diffusion_models/minimax_h3_ref2va_viggle_pruned_int8_convrot.safetensors` | `/.autodl/5d/11/69/5d1169b64963fa31487815ca5bcd2441` | 2026-09-14 21:18 |
| `models/diffusion_models/model-00001-of-00004.safetensors` | `/.autodl/80/b1/47/80b147de9a1afde4c4d4a8bf0f7cf965` | 2026-01-14 10:40 |
| `models/diffusion_models/model-00002-of-00004.safetensors` | `/.autodl/f9/a4/0e/f9a40e3293281327b2820a0e595aee98` | 2026-01-14 10:31 |
| `models/diffusion_models/model-00003-of-00004.safetensors` | `/.autodl/4e/8a/90/4e8a900ffe317320149b5370cd3b7db8` | 2026-01-14 10:22 |
| `models/diffusion_models/model-00004-of-00004.safetensors` | `/.autodl/03/fd/42/03fd429e1e6b38a0d1b07322a93ce01a` | 2026-01-14 10:35 |
| `models/diffusion_models/model.safetensors` | `/.autodl/84/78/22/847822125fcb72c484dc8fca777a680f` | 2026-09-07 13:07 |
| `models/diffusion_models/moodyAmateurMixKrea2_3JAVStyle_int8.safetensors` | `/.autodl/68/12/6a/68126a5c45aabab170955acd4c6e02c0` | 2026-09-17 23:23 |
| `models/diffusion_models/moodyAmateurMixKrea2_4RawStudioShot_int8.safetensors` | `/.autodl/9c/5e/e8/9c5ee8ee1aaef38c1a810e8ba0d4eae7` | 2026-09-17 23:23 |
| `models/diffusion_models/nanfeng-h3-b25-49.safetensors` | `/.autodl/5b/4a/2b/5b4a2b4244c8331597c7eeef4b57a725` | 2026-09-17 22:25 |
| `models/diffusion_models/qwen-image-edit-2511-multiple-angles-lora.safetensors` | `/.autodl/19/30/f2/1930f2e0757b0491e58694c1e4fec4f3` | 2026-03-10 15:38 |
| `models/diffusion_models/qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors` | `/.autodl/2e/e4/cf/2ee4cf11996deea1b17772686edd7a2c` | 2026-09-21 22:31 |
| `models/diffusion_models/qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors` | `/.autodl/3d/3f/3a/3d3f3a0b0ba34f661417445411d510eb` | 2026-09-21 22:35 |
| `models/diffusion_models/qwen3vl_8b_joyimage_edit_bf16.safetensors` | `/.autodl/1a/53/8d/1a538d619d1fed3598ac4099b1367ec8` | 2026-09-11 14:27 |
| `models/diffusion_models/qwen3vl_8b_joyimage_edit_int8_convrot.safetensors` | `/.autodl/84/53/dc/8453dccf21dda5eeab04116057a376be` | 2026-09-11 14:25 |
| `models/diffusion_models/qwen_image_2.1_bf16.safetensors` | `/.autodl/25/bd/b2/25bdb21b951a9cc4e78aefe96916c6f3` | 2026-09-25 00:22 |
| `models/diffusion_models/qwen_image_2.1_int8_convrot.safetensors` | `/.autodl/7c/40/26/7c4026516e59abf14c6d2eea96f5b64d` | 2026-09-25 00:31 |
| `models/diffusion_models/qwen_image_edit_2509_int8_convrot.safetensors` | `/.autodl/94/1d/83/941d83b7f46e82e45757f7be86f2e73b` | 2026-09-14 03:24 |
| `models/diffusion_models/wan2.1_14B_SCAIL_2_nvfp4_mxpf8_mix.safetensors` | `/.autodl/ba/60/ab/ba60ab85b9455e179e502f7a5b2b61f5` | 2026-09-11 20:35 |
| `models/diffusion_models/yue2_3b_bf16.safetensors` | `/.autodl/ac/d6/61/acd661ae90fcf20f8955a84088c01cce` | 2026-09-14 03:06 |
| `models/diffusion_models/yue2_3b_int8_convrot.safetensors` | `/.autodl/86/45/f0/8645f0d943c3e481ef3d66657c6d27df` | 2026-09-14 03:10 |

### `diffusion_models/Flux` (3)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/diffusion_models/Flux/787e95f4-08cf-547a-9648-97b44434b75c.safetensors` | `/.autodl/bstungnguyen/Flux/flux1-dev.safetensors` | 2025-09-23 19:44 |
| `models/diffusion_models/Flux/flux1-dev.sft` | `/.autodl/bstungnguyen/Flux/flux1-dev.safetensors` | 2025-10-11 15:22 |
| `models/diffusion_models/Flux/flux1-dev_unet.safetensors` | `/.autodl/bstungnguyen/Flux/flux1-dev.safetensors` | 2025-11-04 05:31 |

### `diffusion_models/Krea-2-Raw` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/diffusion_models/Krea-2-Raw/krea2_raw_bf16.safetensors` | `/.autodl/krea/Krea-2-Raw/raw.safetensors` | 2026-06-24 22:44 |

### `diffusion_models/Krea-2-Turbo` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/diffusion_models/Krea-2-Turbo/krea2_turbo_bf16.safetensors` | `/.autodl/krea/Krea-2-Turbo/turbo.safetensors` | 2026-06-24 22:41 |

### `diffusion_models/LTX-2.5` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/diffusion_models/LTX-2.5/ltx-2.5-22b-dev-transformer-comfy-int8-convrot.s afetensors` | `/.autodl/Lightricks/LTX-2.5/diffusion_models/ltx-2.5-22b-dev-transformer-comfy-int8-convrot.safetensors` | 2026-08-12 17:23 |
| `models/diffusion_models/LTX-2.5/ltx-2.5-22b-distilled-transformer-comfy-in t8-convrot.safetensors` | `/.autodl/Lightricks/LTX-2.5/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors` | 2026-08-12 17:23 |

### `diffusion_models/MiniMax-H3-experimental` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/diffusion_models/MiniMax-H3-experimental/minimax_h3_video_vae_int8_convrot-v2.safetensors` | `/.autodl/15/22/fc/1522fc49e094bb75c704ee519582252d` | 2026-09-19 00:26 |

### `diffusion_models/Qwen-Image-2.1` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/diffusion_models/Qwen-Image-2.1/diffusion_pytorch_model-00001-of-00002.safetensors` | `/.autodl/Qwen/Qwen-Image-2.1/transformer/diffusion_pytorch_model-00001-of-00002.safetensors` | 2026-09-29 10:50 |
| `models/diffusion_models/Qwen-Image-2.1/diffusion_pytorch_model-00002-of-00002.safetensors` | `/.autodl/Qwen/Qwen-Image-2.1/transformer/diffusion_pytorch_model-00002-of-00002.safetensors` | 2026-09-29 10:50 |

### `diffusion_models/models` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/diffusion_models/models/z-image-turbo_fp8_scaled_e4m3fn_KJ.safetensors` | `/.autodl/89/2b/40/892b40f243d1d255f25b6d1bf6fa0146` | 2025-12-12 14:34 |
| `models/diffusion_models/models/z_image_turbo_bf16.safetensors` | `/.autodl/d7/f6/0a/d7f60a81306d9b8edeae4577d3779561` | 2025-12-01 03:38 |

### `diffusion_models/stable-diffusion-xl-base-1.0` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/diffusion_models/stable-diffusion-xl-base-1.0/945a5f58-cd78-5ffd-b5d3-f90ac6322b71.safetensors` | `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/sd_xl_base_1.0.safetensors` | 2025-09-23 19:44 |

### `diffusion_models/xinlingjun` (4)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/diffusion_models/xinlingjun/5a3d2d02-299c-5ef4-a235-15597676aa16.safetensors` | `/.autodl/67/6a/6d/676a6d9ee21a28e661358e830b46bb20` | 2025-09-23 19:44 |
| `models/diffusion_models/xinlingjun/diffusion_pytorch_model.safetensors` | `/.autodl/67/6a/6d/676a6d9ee21a28e661358e830b46bb20` | 2025-10-30 19:41 |
| `models/diffusion_models/xinlingjun/flux.1-turbo-alpha.safetensors` | `/.autodl/67/6a/6d/676a6d9ee21a28e661358e830b46bb20` | 2025-10-04 12:49 |
| `models/diffusion_models/xinlingjun/flux1-turbo.safetensors` | `/.autodl/67/6a/6d/676a6d9ee21a28e661358e830b46bb20` | 2025-10-30 19:43 |

### `embeddings` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/embeddings/fixed_embed_fwd_anyframe.safetensors` | `/.autodl/62/a1/e5/62a1e5a3ea244a5487e881218e2ce12c` | 2026-09-14 17:16 |

### `geometry_estimation` (9)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/geometry_estimation/marigold_v2_albedo.safetensors` | `/.autodl/f5/0e/ca/f50eca2e67603c44198045cb029e5072` | 2026-09-14 02:47 |
| `models/geometry_estimation/marigold_v2_albedo_conditioning.safetensors` | `/.autodl/4e/65/b7/4e65b733edcb71c18b43db7fe104b23d` | 2026-09-14 02:47 |
| `models/geometry_estimation/marigold_v2_depth_conditioning.safetensors` | `/.autodl/52/87/df/5287dfc83c56a3552994ef2010c20666` | 2026-09-14 02:47 |
| `models/geometry_estimation/marigold_v2_depth_log_stage2.safetensors` | `/.autodl/61/e8/31/61e831f7886a2caabf451bc72559a52b` | 2026-09-14 02:49 |
| `models/geometry_estimation/marigold_v2_normals.safetensors` | `/.autodl/db/6a/81/db6a819738ca5dc971b8141c4cb92b9b` | 2026-09-14 02:50 |
| `models/geometry_estimation/marigold_v2_normals_conditioning.safetensors` | `/.autodl/f2/72/a8/f272a8fbc56b3c2e16d0459deda55659` | 2026-09-14 02:50 |
| `models/geometry_estimation/moge-3-vitg_fp16.safetensors` | `/.autodl/92/33/5c/92335ca9a86e7844f19a2631508da7d4` | 2026-09-18 05:42 |
| `models/geometry_estimation/moge-3-vitl_fp16.safetensors` | `/.autodl/22/17/96/221796916b25b9409a75ca207998674f` | 2026-09-18 05:47 |
| `models/geometry_estimation/video_depth_anything_vits.pth` | `/.autodl/fb/05/c3/fb05c39903512191bcb05e7fa26edfbb` | 2026-09-18 14:03 |

### `latent_upscale_models` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/latent_upscale_models/h3_upscaler_lms_v0.1_fp32.safetensors` | `/.autodl/ac/75/19/ac7519f39f426a41e8dbf3b9a5e792ad` | 2026-09-28 16:05 |
| `models/latent_upscale_models/h3_upscaler_sharpness_2000steps_v0.1_fp32.safetensors` | `/.autodl/ac/75/19/ac7519f39f426a41e8dbf3b9a5e792ad` | 2026-09-28 16:05 |

### `latent_upscale_models/LTX-2.5` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/latent_upscale_models/LTX-2.5/ltx-2.3-temporal-upscaler-x2-1.0.safetensors` | `/.autodl/Lightricks/LTX-2.5/latent_upscale_models/ltx-2.5-latent-temporal-upscaler-x2-bf16-1.0.safetensors` | 2026-05-26 16:40 |

### `loras` (142)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/loras/1.5-林鹤-妆容，美颜，磨皮，滤镜，四合一_v1.safetensors` | `/.autodl/d3/8d/ff/d38dff1f0fbbfc997bf7250f7e193dd7` | 2026-09-14 12:00 |
| `models/loras/3DChineseStyle_25.safetensors` | `/.autodl/f1/32/d4/f132d4d904da0a481cb9482db4d8b0f9` | 2026-09-12 22:00 |
| `models/loras/3Dguoman.safetensors` | `/.autodl/0a/9a/36/0a9a3628e3b1b9f78220c36c9c96e16e` | 2026-09-13 19:47 |
| `models/loras/90huaijiu_qwen.safetensors` | `/.autodl/66/19/f1/6619f12ef2c5b856c62ae49825c6516d` | 2026-09-10 22:04 |
| `models/loras/Afterlight_v1.safetensors` | `/.autodl/3b/80/5a/3b805a53ff3365f3b48dbd3904ee8e2a` | 2026-09-09 11:32 |
| `models/loras/BUNNY_H3_ActionLogic_Bridge_V1_T8_Compat.safetensors` | `/.autodl/79/c2/98/79c2981daf8b8c64ddfd0290cb7196fc` | 2026-09-28 13:04 |
| `models/loras/CinematicMH3-V01.safetensors` | `/.autodl/3c/e6/0e/3ce60ecc6afc7eaa6007e5b918952655` | 2026-09-20 15:20 |
| `models/loras/Cyrene-v2-noob-Tanger.safetensors` | `/.autodl/3d/f4/95/3df495889e439f226f696cd96aa9f0f7` | 2026-09-07 22:53 |
| `models/loras/Detailer-KREA2.safetensors` | `/.autodl/4a/60/94/4a6094d18583a5db37d67223476affa4` | 2026-09-09 11:32 |
| `models/loras/FULX极致真实.safetensors` | `/.autodl/34/a5/20/34a520fc4844b6d6e02ba155ec82592a` | 2026-09-14 12:03 |
| `models/loras/H3-PK-Parasyte-Turbo.safetensors` | `/.autodl/06/a5/2f/06a52f466dfb0c4a45552b2713f326b7` | 2026-09-30 13:42 |
| `models/loras/H3_speed_slider_1.1.safetensors` | `/.autodl/83/e2/3d/83e23d3816f6ac855a110dcf33b5102e` | 2026-09-27 18:23 |
| `models/loras/JY波光粼粼.safetensors` | `/.autodl/9a/cf/9e/9acf9e67b33095979df67b745ec8c21e` | 2026-09-14 12:00 |
| `models/loras/K2-MJ美学增强Afterlight_v1.safetensors` | `/.autodl/3b/80/5a/3b805a53ff3365f3b48dbd3904ee8e2a` | 2026-09-20 12:00 |
| `models/loras/K2_cgStyle_V1_nnegret.safetensors` | `/.autodl/0f/85/6e/0f856e19d03d5129c7cf223baa50e0a3` | 2026-09-09 11:37 |
| `models/loras/Krea2-25D动漫Semi_Real_Anime_V2_NSW.safetensors` | `/.autodl/24/4e/ac/244eaca9636247a6e69169160cf8bfca` | 2026-09-09 11:36 |
| `models/loras/Krea2-Nikki_Style_Anime_NSW.safetensors` | `/.autodl/ca/31/8b/ca318bbfcc275729a641abc78c7c094d` | 2026-09-09 11:51 |
| `models/loras/Krea2-asia_cosplay_krea_2.safetensors` | `/.autodl/15/6a/50/156a50a5a98ebc4cc582bf11d6db1558` | 2026-09-09 11:41 |
| `models/loras/Krea2-asianMix_v1-bf16.safetensors` | `/.autodl/66/95/8d/66958d3d5dc41d33324e74548090ebc2` | 2026-09-09 11:47 |
| `models/loras/Krea2-gpt anime render.safetensors` | `/.autodl/c7/bb/38/c7bb38f6db813706832ad2d965f1bd84` | 2026-09-09 11:48 |
| `models/loras/Krea2-亚洲hina_krea2Turbo_lora_tqd_v4.0.safetensors` | `/.autodl/86/84/52/8684521b60d86ff275e128c162adc05e` | 2026-09-20 11:47 |
| `models/loras/Krea2-动漫umina_krea2_v1.safetensors` | `/.autodl/1d/2c/58/1d2c588b62e48ca16cdf2dca3a43d8ea` | 2026-09-09 11:48 |
| `models/loras/Krea2-动漫yukan-style.safetensors` | `/.autodl/7a/55/48/7a5548410d24d84e84dfb974552f9858` | 2026-09-09 11:50 |
| `models/loras/Krea2-动漫角色融合Anime Character Fusion.safetensors` | `/.autodl/12/96/b8/1296b852b240ebab8e1fe4d874e3717d` | 2026-09-09 11:49 |
| `models/loras/Krea2-漫画风格ogipote-ep63.safetensors` | `/.autodl/d0/b4/91/d0b491a8a79d104b5b8902c537086516` | 2026-09-09 13:46 |
| `models/loras/Krea2-绘画美学风格painterly render style.safetensors` | `/.autodl/80/dc/29/80dc293aede1d1d7bcdceab9d6bc3468` | 2026-09-09 11:51 |
| `models/loras/Krea2_Anything2RealCharacters-V3.safetensors` | `/.autodl/41/50/6f/41506fe833f9d269aaf0cb8057c8eac0` | 2026-09-09 17:08 |
| `models/loras/Krea2_Character_Design_4-View_V1.safetensors` | `/.autodl/02/86/e8/0286e830f318cb0049fb24a001aa892e` | 2026-09-15 09:41 |
| `models/loras/Krea_2_zidiusArt_Melancholy_v2.safetensors` | `/.autodl/26/cf/bb/26cfbb445e0bb23364d4a011eafb94f2` | 2026-09-08 22:36 |
| `models/loras/MMH3-MPOV.safetensors` | `/.autodl/3a/ec/63/3aec6394976c8ff6cf33888f9ee77050` | 2026-09-28 16:20 |
| `models/loras/MiniMaxH3_SemanticBridge_v1.safetensors` | `/.autodl/ed/c6/df/edc6dfe5a53f121b61ce57feab1af5dd` | 2026-09-27 14:49 |
| `models/loras/MiniMaxH3_SemanticBridge_v1_T8_Compat.safetensors` | `/.autodl/16/59/4c/16594cbe241057da5246172a9971d69f` | 2026-09-28 13:04 |
| `models/loras/Minimax-H3真实电影质感V0.1-解决张量报错.safetensors` | `/.autodl/da/39/c5/da39c5d5597b92a2069e928c24a179e6` | 2026-09-14 23:17 |
| `models/loras/Minimax-h3_Third_person_view.safetensors` | `/.autodl/6a/fb/9f/6afb9f31ed62e867563b544f0118d004` | 2026-09-19 02:57 |
| `models/loras/Motion_Repair_V2.safetensors` | `/.autodl/b3/b8/30/b3b830291f5df8182827ac7b318c3002` | 2026-09-29 01:11 |
| `models/loras/MysticXXX_MMH3-V4-ref2va.safetensors` | `/.autodl/1d/58/94/1d5894edd78cfa99b96a944e34c46b53` | 2026-09-20 01:25 |
| `models/loras/Pornmaster_QI2.1_Breasts_Slider_V1.safetensors` | `/.autodl/51/f9/79/51f979eb73decf921aae39470b3d5668` | 2026-09-27 23:11 |
| `models/loras/Qwen-现代短剧动漫_V1.safetensors` | `/.autodl/9e/19/15/9e1915471fbec18358ef0a49057112c0` | 2026-09-11 20:35 |
| `models/loras/Qwen2.1_Anime2Real_Beta.safetensors` | `/.autodl/ee/de/0a/eede0af133a4025e3502dc86996a716b` | 2026-09-25 21:50 |
| `models/loras/Qwen2.1_Anything2RealCharacters.safetensors` | `/.autodl/28/5a/9e/285a9ecc41b3d64024e5f484a964e8e4` | 2026-09-29 18:22 |
| `models/loras/QwenImage_AnimeTweaker_v1.2-aio.safetensors` | `/.autodl/6b/17/1c/6b171cbf4ec98a6ab75e0605a8952e12` | 2026-09-29 06:00 |
| `models/loras/Scail-2_relighting-lora.safetensors` | `/.autodl/80/9b/34/809b34349e067e34c89bdba3f8136842` | 2026-09-18 18:41 |
| `models/loras/T_S_Anima_Detail_Tweaker.safetensors` | `/.autodl/a0/53/f1/a053f1513286cbe4ac204ca0f3abb269` | 2026-09-19 21:15 |
| `models/loras/TripleView_klein9b_v1.safetensors` | `/.autodl/49/63/3f/49633f767aa2aeaa01725e8583ae1933` | 2026-09-09 11:33 |
| `models/loras/Wuli-Qwen-Image-2512-Turbo-LoRA-2steps-V1.0-bf16.safetensors` | `/.autodl/5c/e0/f7/5ce0f79de7574431bc85e26ecb891b10` | 2026-09-06 06:42 |
| `models/loras/adapter_config.json` | `/.autodl/6d/c9/9c/6dc99cf0106eb663f95970dd7636cee4` | 2026-09-07 16:08 |
| `models/loras/anima-lllite-any-test-like-1-step1000.safetensors` | `/.autodl/78/79/46/7879461e3c5fb228e68350f583ed9834` | 2026-09-11 04:06 |
| `models/loras/anima-lllite-any-test-like-1-step2000.safetensors` | `/.autodl/c5/fa/47/c5fa4734bb5f5cd0057d3915ddadebc9` | 2026-09-11 04:06 |
| `models/loras/anima-lllite-any-test-like-v2-beta-epoch-03.safetensors` | `/.autodl/8b/b3/76/8bb376eb9de44be404dc75c708823207` | 2026-09-11 04:06 |
| `models/loras/anima-lllite-any-test-like-v2.safetensors` | `/.autodl/e3/b1/4f/e3b14f0e32840279b200ee7ebd338669` | 2026-09-11 04:06 |
| `models/loras/anima-lllite-depth-1.safetensors` | `/.autodl/5b/ed/62/5bed629164d5a5ba14873c9c71b79e37` | 2026-09-11 04:06 |
| `models/loras/anima-lllite-inpainting-v1.safetensors` | `/.autodl/c0/bc/00/c0bc00917cecf92525e6242a6deefd8c` | 2026-09-11 04:07 |
| `models/loras/anima-lllite-inpainting-v2.safetensors` | `/.autodl/f4/4f/74/f44f74adf9b452f802c094fc9bf5c84c` | 2026-09-11 04:07 |
| `models/loras/anima-lllite-lineart-1.safetensors` | `/.autodl/81/18/c3/8118c301395cfb451ffa6248dd351e5a` | 2026-09-11 04:07 |
| `models/loras/anima-lllite-pose-1.safetensors` | `/.autodl/b2/be/d3/b2bed36f10190bb9f95f754707471b56` | 2026-09-11 04:07 |
| `models/loras/anima-lllite-scribble-1.safetensors` | `/.autodl/cf/6c/f4/cf6cf40a7ec44c57f1675e4c23c6d805` | 2026-09-11 04:07 |
| `models/loras/anima-turbo-lora-v0.1.safetensors` | `/.autodl/30/e4/0d/30e40d2e2e9424ac280680aca3cff8f2` | 2026-09-11 04:06 |
| `models/loras/anima-turbo-lora-v0.2.safetensors` | `/.autodl/55/3a/57/553a573f26636c4c11c15e55cc57066c` | 2026-09-11 04:06 |
| `models/loras/bunnyH3ConditioningBridge_v10.safetensors` | `/.autodl/60/7b/a5/607ba510a318bf3eec9540587d9a11c7` | 2026-09-19 12:18 |
| `models/loras/chuantongshuimo_qwen.safetensors` | `/.autodl/a6/03/90/a60390d93e45077b737b1f8078307e77` | 2026-09-11 13:53 |
| `models/loras/davham_cinema-h3-Euler-simple-0.8.safetensors` | `/.autodl/13/2c/c2/132cc20507b7d07e5c6525c169b497cf` | 2026-09-19 00:04 |
| `models/loras/f2k_9B_lcs_consist_20260415.safetensors` | `/.autodl/73/e2/54/73e2546e983d4acff3f3b07ebae7cd5b` | 2026-09-09 11:37 |
| `models/loras/fafafast.safetensors` | `/.autodl/83/e2/3d/83e23d3816f6ac855a110dcf33b5102e` | 2026-09-23 16:05 |
| `models/loras/flux-multi-angles-v2-72poses-comfy.safetensors` | `/.autodl/d8/d5/1e/d8d51e48d7056cfe792a4e51a61b2fa5` | 2026-09-10 02:23 |
| `models/loras/flux2放大.safetensors` | `/.autodl/11/0c/51/110c512c0fabce853d93960f1558cfbd` | 2026-09-14 12:02 |
| `models/loras/guangbolinlin.safetensors` | `/.autodl/a0/40/0a/a0400a58165648eddaf4c59b4c88e642` | 2026-09-14 12:11 |
| `models/loras/h3-realism-people-t2v-i2v-r2v-触发词r34l1sm.safetensors` | `/.autodl/e4/1d/d8/e41dd88134dfce38e0b1cdc5d73c8312` | 2026-08-15 18:14 |
| `models/loras/h3_character_swap_pro4500_1000.safetensors` | `/.autodl/71/76/db/7176dbdf1e6a51fa8eff330f1a9ffd68` | 2026-09-27 23:06 |
| `models/loras/hina_Krea2Turbo_animeEnhance_v1.0.safetensors` | `/.autodl/fb/e6/42/fbe6423534ebbf803f2e3ba4da6c043f` | 2026-09-26 10:57 |
| `models/loras/ig_tiktok_aesthetic_h3_lora_v1_500.safetensors` | `/.autodl/ee/b9/8e/eeb98e7a7e48ecdb711263f59a5b794c` | 2026-09-14 23:18 |
| `models/loras/jin_000002250.safetensors` | `/.autodl/64/6b/e7/646be7b41af56e2a6fb0c66fa84ca1e9` | 2026-09-14 12:09 |
| `models/loras/klein_9B_Turbo_r128.safetensors` | `/.autodl/78/9e/59/789e595d819fed7af77ef46225385590` | 2026-05-28 11:42 |
| `models/loras/krea2-MJ.safetensors` | `/.autodl/e0/4b/8e/e04b8e85cedce72c6e13ecfa4af690d6` | 2026-09-09 11:48 |
| `models/loras/krea2_raw_to_turbo_r256_comfy.safetensors` | `/.autodl/7b/d9/13/7bd9132163db96fa54cb1b4e8135d9f5` | 2026-09-20 11:27 |
| `models/loras/krea2_ta86_inkriot_V2.safetensors` | `/.autodl/e7/c3/be/e7c3bebe963fa8b66545135fc7ace873` | 2026-09-08 22:36 |
| `models/loras/krea2_turbo_4step_rank_64_lora_comfyui.safetensors` | `/.autodl/86/15/ff/8615ff2a3e10325d6141a0bc3111f904` | 2026-09-07 23:47 |
| `models/loras/krea2_turbo_4step_rank_64_lora_latest_comfyui.safetensors` | `/.autodl/94/5f/86/945f86d97ace1f86bd2a114d6d7acc11` | 2026-09-09 11:52 |
| `models/loras/krea2小志_xm_k20_texture.safetensors` | `/.autodl/c1/29/81/c12981e7e928fe0e16d4b9a23c45da26` | 2026-09-20 12:00 |
| `models/loras/krea_nylonsocks_v1.safetensors` | `/.autodl/f5/42/a7/f542a733be7bb2812b2681b20f8b9180` | 2026-09-26 00:36 |
| `models/loras/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors` | `/.autodl/b8/9c/8f/b89c8f23cbd548e8d9d7ef1416b87cc5` | 2025-11-13 03:52 |
| `models/loras/lightx2v_hybrid-4to8step-Turbo_r48.safetensors` | `/.autodl/df/a4/e1/dfa4e110c65bdd6de2b02516d1f89295` | 2026-09-14 23:19 |
| `models/loras/ltx-2.3-22b-ic-lora-colorization-0.9.safetensors` | `/.autodl/05/37/32/05373275b33ec47f0ab919432166110a` | 2026-09-22 15:27 |
| `models/loras/ltx-2.3-22b-ic-lora-day-to-night-0.9.safetensors` | `/.autodl/0b/2b/14/0b2b14ecc26bca445574c68203ebf491` | 2026-09-22 15:13 |
| `models/loras/ltx-2.3-22b-ic-lora-decompression-0.9.safetensors` | `/.autodl/8a/47/20/8a472095919a75335a10d502dabba8ef` | 2026-09-22 15:31 |
| `models/loras/ltx-2.3-22b-ic-lora-dubit-0.9.safetensors` | `/.autodl/ec/c6/29/ecc629668da1222455718ac1e24508fb` | 2026-09-18 14:12 |
| `models/loras/ltx-2.3-22b-ic-lora-pixel-spatial-upscaler-x2-0.9.safetensors` | `/.autodl/5b/58/bd/5b58bd51a36b98b42cc8e565ebc4a623` | 2026-09-22 15:23 |
| `models/loras/ltx-2.3-22b-ic-lora-water-simulation-0.9.safetensors` | `/.autodl/a7/52/d6/a752d6d3e09f99d0673e523ee2b6c6d6` | 2026-09-22 15:36 |
| `models/loras/ltx-2.5-22b-ic-lora-ingredients-0.9.safetensors` | `/.autodl/ce/4d/c2/ce4dc25502a173ea4f7ab5de1de103d5` | 2026-09-12 03:58 |
| `models/loras/minimax_h3_4step_lora_flashgen_v1.0_768p_fl2va_pruned_avg_rank_13_bf16.safetensors` | `/.autodl/75/e8/30/75e8304d27ea5f49799a348ef2dff224` | 2026-09-23 23:01 |
| `models/loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_resized_avg_rank_21_bf16.safetensors` | `/.autodl/3d/01/22/3d0122a5feeb02da7c9f4b7dbfff2319` | 2026-09-29 23:22 |
| `models/loras/minimax_h3_fl2va_bf16_turbo_multistep_fro099_r48_pruned.safetensors` | `/.autodl/cc/35/91/cc35916833c33e9ee4b3e380d2c73b1d` | 2026-09-14 21:19 |
| `models/loras/minimax_h3_head_swap_v1.0_r32.safetensors` | `/.autodl/77/c4/7b/77c47b2ebb8b76d303adccfe7edae1f8` | 2026-09-28 16:07 |
| `models/loras/minimax_h3_hyperflow_8step_v1.0.safetensors` | `/.autodl/4e/b8/71/4eb8714ddaa4a4bf52f90d43fc484322` | 2026-09-19 14:12 |
| `models/loras/minimax_h3_hyperflow_EMA600_pruned_r128_fro0995_turbo_lora.safetensors` | `/.autodl/6c/77/6a/6c776aacc2ca0c6a6bb90b8fb480e50e` | 2026-09-27 23:27 |
| `models/loras/minimax_h3_live_wallpaper_v1.0_ref2va_r32.safetensors` | `/.autodl/e5/79/df/e579df4227ee55613259e4641b049e43` | 2026-09-28 17:13 |
| `models/loras/minimax_h3_live_wallpaper_v1.0_ref2va_r64_r.safetensors` | `/.autodl/91/86/d2/9186d21d60f2ab2fed477065275d6250` | 2026-09-28 22:31 |
| `models/loras/minimax_h3_lms_v1.0_r64.safetensors` | `/.autodl/da/f9/17/daf917ad335db6072b5c72d8bc7a08de` | 2026-09-16 16:17 |
| `models/loras/minimax_h3_lms_v1.0_r64_r2.safetensors` | `/.autodl/fc/66/7c/fc667c8111d04a6ecc62fea1ca3632e0` | 2026-09-28 17:13 |
| `models/loras/minimax_h3_ref2v_turbo_4step_v0.1_comfyui_resized_avg_rank_21_bf16.safetensors` | `/.autodl/d1/d0/12/d1d012e0f7e7fbdd322db85e4dcd4ea4` | 2026-09-29 23:24 |
| `models/loras/minimax_h3_ref2va_training_adapter_v3.safetensors` | `/.autodl/83/f7/da/83f7da938c7280074f8542d4912372bc` | 2026-09-29 14:10 |
| `models/loras/minimax_h3_style_transfer_v1.0_r64.safetensors` | `/.autodl/c4/21/09/c42109458afdb324de0d459f937d3aa2` | 2026-09-16 16:18 |
| `models/loras/minimax_h3_style_transfer_v1.0_r64_r.safetensors` | `/.autodl/9d/3b/7e/9d3b7e1a242c267f283bac5affec0da0` | 2026-09-28 22:31 |
| `models/loras/minimax_h3_taomate_3step_lora_avg_rank_19_bf16.safetensors` | `/.autodl/61/a5/7f/61a57f6952f9bd0223c76a1b5c9689e0` | 2026-09-14 03:36 |
| `models/loras/minimax_h3_turbo_4step_ckpt500_V1.safetensors` | `/.autodl/dc/95/76/dc95768422807cb349212cf400a7bc2d` | 2026-09-15 07:23 |
| `models/loras/minimax_h3_turbo_4step_ckpt600_V4.safetensors` | `/.autodl/8d/04/5f/8d045fb20533e99f5f0c309f6f26e1db` | 2026-09-15 07:23 |
| `models/loras/minimax_h3_turbo_4step_ckpt600_ema_V4.safetensors` | `/.autodl/42/e7/02/42e7022f101491b781f7f12add0445e1` | 2026-09-15 07:23 |
| `models/loras/minimax_h3_turbo_4step_ckpt850_V1.safetensors` | `/.autodl/f3/40/09/f34009283819d454aa44c400ec249423` | 2026-09-15 07:23 |
| `models/loras/minimax_h3_vfx_edit_v1.0_r128.safetensors` | `/.autodl/da/b2/4e/dab24e3482ad0de7e006172e332894e7` | 2026-09-28 22:31 |
| `models/loras/minimax_h3_vfx_edit_v1.0_r128_ffp_r.safetensors` | `/.autodl/5b/49/14/5b4914983b87505632367c6b4f35de5a` | 2026-09-28 22:31 |
| `models/loras/minimax_h3_video_vae_fp8mix.safetensors` | `/.autodl/f7/05/b4/f705b4eba975832ae2d3ae12e5fb705d` | 2026-09-09 13:10 |
| `models/loras/qwen_image_detail_slider.safetensors` | `/.autodl/f2/bc/6e/f2bc6e53f7fcdcbd59102b44fd01fd02` | 2026-09-29 20:40 |
| `models/loras/shandeng.safetensors` | `/.autodl/28/00/8a/28008ad163b3e9fb311a5d3313ebe436` | 2026-09-14 12:02 |
| `models/loras/shangmei_qwen.safetensors` | `/.autodl/ba/d9/6d/bad96d5818c5f53a942dc87c11080614` | 2026-09-11 14:09 |
| `models/loras/shaoshi_qwen.safetensors` | `/.autodl/b5/14/6b/b5146b617ce0b62ec0447e332ee88baa` | 2026-09-12 10:11 |
| `models/loras/shuimo_qwen.safetensors` | `/.autodl/5f/b8/12/5fb81252a4bab83f9c6eae4bbc1058bb` | 2026-09-11 13:40 |
| `models/loras/tintin_style_qwen_v2.safetensors` | `/.autodl/fd/4f/02/fd4f0251a1c38ec0ca01ec9aca04d516` | 2026-09-12 10:21 |
| `models/loras/viggle_animate_dmd_lora.safetensors` | `/.autodl/cb/df/8b/cbdf8b54fbb4f7fc6726849e8c25d439` | 2026-09-14 20:26 |
| `models/loras/viggle_animate_dmd_lora_r64.safetensors` | `/.autodl/d2/1f/7c/d21f7cd11c80ea1c04ddf52dad9aaa15` | 2026-09-14 20:21 |
| `models/loras/wan2.1_SCAIL_2_relight_lora_bf16.safetensors` | `/.autodl/6a/65/fc/6a65fc2561a5c34735adcc6a85c8979b` | 2026-09-11 17:39 |
| `models/loras/wuqi.safetensors` | `/.autodl/f4/6e/b8/f46eb88a297970c305dfdc499fb688f7` | 2026-09-14 12:10 |
| `models/loras/wuxia_qwen.safetensors` | `/.autodl/a9/d0/0b/a9d00bde73a84ce53cfb0b344f074d4e` | 2026-09-11 22:31 |
| `models/loras/xinshuimo_qwen.safetensors` | `/.autodl/cd/26/01/cd2601b4eb3dfaf8cf616590453f5e0d` | 2026-09-11 23:13 |
| `models/loras/xuejing.safetensors` | `/.autodl/4a/83/cc/4a83ccc3d26beee68d77c0952c679750` | 2026-09-14 12:11 |
| `models/loras/一键竹林前景.safetensors` | `/.autodl/d7/5f/29/d75f2951c018ab46541613382188622e` | 2026-09-14 12:06 |
| `models/loras/万能修图.safetensors` | `/.autodl/4a/0e/3c/4a0e3ccf34a8942f7e3f4988910e9a44` | 2026-09-14 12:08 |
| `models/loras/优化光影.safetensors` | `/.autodl/96/eb/11/96eb11a730a3cbd035c58757a42588a9` | 2026-09-14 12:05 |
| `models/loras/修复草地.safetensors` | `/.autodl/67/ab/59/67ab59d44a67f7ffaa61070adabc7300` | 2026-09-14 12:03 |
| `models/loras/修复裤腿O型腿_v2.safetensors` | `/.autodl/4d/e6/58/4de658bf167a1140d01629fadb6da48d` | 2026-09-14 11:57 |
| `models/loras/华丽短剧古风人物插画_v1.safetensors` | `/.autodl/d4/f4/95/d4f495d16413b0259f0aaca8760bad72` | 2026-04-08 16:04 |
| `models/loras/古风cg.safetensors.safetensors` | `/.autodl/f1/cb/d2/f1cbd2616f8fd95638b20f583bd58ae8` | 2026-09-11 22:22 |
| `models/loras/古风修图_1.0.safetensors` | `/.autodl/5e/27/01/5e2701b20957e6b10ce1095721b8dfb0` | 2026-09-14 12:08 |
| `models/loras/古风小说漫剧.safetensors` | `/.autodl/ee/02/60/ee0260fb8fed818df9a4fa7c2b0426b6` | 2026-04-09 00:04 |
| `models/loras/外景晴空.safetensors` | `/.autodl/ca/78/98/ca7898b0a85ce4af11edd13098dc46d7` | 2026-09-14 12:01 |
| `models/loras/室内打光.safetensors` | `/.autodl/54/fa/c8/54fac8943d56d31ff61f7da2e2c287a4` | 2026-09-15 11:16 |
| `models/loras/床单.safetensors` | `/.autodl/13/c9/9c/13c99cbd4947deed10eceb5006991967` | 2026-09-14 12:04 |
| `models/loras/模糊变清晰 2.2万步.safetensors` | `/.autodl/47/05/0d/47050da7112c17ab222b9b0f380d06e3` | 2026-09-14 12:12 |
| `models/loras/电影感H3-loraV1.0正式版.safetensors` | `/.autodl/f1/e0/18/f1e018a8b6a7328b7b8c5ed657c47ba0` | 2026-09-15 11:31 |
| `models/loras/电影感H3-loraV1.0正式版_剪枝与非剪枝通用.safetensors` | `/.autodl/19/15/ab/1915ab5953146169e5e331079ae51b15` | 2026-09-15 10:40 |
| `models/loras/秋天优化.safetensors` | `/.autodl/ec/c7/a7/ecc7a788fe266db0a19917f2509817db` | 2026-09-14 12:07 |
| `models/loras/超真实日常.safetensors` | `/.autodl/43/8d/58/438d58f55ff9ba7e8636b1d4d169af8e` | 2026-09-14 12:04 |
| `models/loras/轮廓光.safetensors` | `/.autodl/ea/48/92/ea489244101c981e04410dc60eef814f` | 2026-09-14 12:06 |
| `models/loras/逆光.safetensors` | `/.autodl/f1/53/50/f153509a63fd920248b70ec2e128ffcb` | 2026-09-14 12:13 |

### `loras/Ditto_models` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/loras/Ditto_models/ditto_global_style.safetensors` | `/.autodl/QingyanBai/Ditto_models/models/ditto_global_style.safetensors` | 2026-02-01 11:39 |

### `loras/evansuen` (8)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/loras/evansuen/v1-inference.yaml` | `/.autodl/ad/0b/80/ad0b808368aaed09f20ef2084164c4e5` | 2026-09-09 10:38 |
| `models/loras/evansuen/v1-inference_clip_skip_2_fp16.yaml` | `/.autodl/f3/82/61/f38261026f3620d6c55af131a89f8c26` | 2026-09-09 11:01 |
| `models/loras/evansuen/v1-inference_fp16.yaml` | `/.autodl/73/f0/c2/73f0c2527150d7ea8d3161d1280bfc7f` | 2026-09-09 11:01 |
| `models/loras/evansuen/v1-inpainting-inference.yaml` | `/.autodl/37/dd/9e/37dd9e21f47478e447db1f1408ee1a4c` | 2026-09-09 11:01 |
| `models/loras/evansuen/v2-inference-v.yaml` | `/.autodl/b7/17/9b/b7179b2145fc8365c9a9ccd3aebb77ee` | 2026-09-09 11:01 |
| `models/loras/evansuen/v2-inference-v_fp32.yaml` | `/.autodl/b6/c4/f6/b6c4f6b8b5c25ad2c1d9337f06c88570` | 2026-09-09 11:01 |
| `models/loras/evansuen/v2-inference.yaml` | `/.autodl/13/13/86/13138658aede9aab6e146116ee854e6e` | 2026-09-09 11:01 |
| `models/loras/evansuen/v2-inference_fp32.yaml` | `/.autodl/e5/08/e0/e508e0dfacacef6a6a9f0b29b43b8549` | 2026-09-09 11:01 |

### `loras/stage-dmd-step-250` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/loras/stage-dmd-step-250/adapter_model.safetensors.manifest.json` | `/.autodl/10/fe/e4/10fee4c5ecf48b14b7c93ad6818a1d37` | 2026-09-07 16:09 |

### `loras/xinlingjun` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/loras/xinlingjun/3f362708-fba9-5106-9354-91f35dc6f559.safetensors` | `/.autodl/ac/30/a5/ac30a5b254f40c8974ebe89115194842` | 2025-09-23 19:43 |

### `optical_flow` (4)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/optical_flow/10159dca-7d77-58f3-bf16-6af15b765577.safetensors` | `/.autodl/ed/2c/2c/ed2c2cad2be4acd394c61760c7cfba7d` | 2025-09-23 19:43 |
| `models/optical_flow/flowformer_sintel_fp32.safetensors` | `/.autodl/90/d4/b2/90d4b2a2cae56488d399a00e8bbc7cff` | 2026-05-13 14:20 |
| `models/optical_flow/gimmvfi_f_arb_lpips_fp32.safetensors` | `/.autodl/58/61/34/5861343be0bb05d10483ccf0eecfda87` | 2026-05-13 14:20 |
| `models/optical_flow/gimmvfi_r_arb_lpips_fp32.safetensors` | `/.autodl/ed/2c/2c/ed2c2cad2be4acd394c61760c7cfba7d` | 2026-05-13 14:20 |

### `style_models` (5)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/style_models/MGE_V6.1_IL_Final_R1.safetensors` | `/.autodl/73/09/60/730960f21e3d32c242f809c70d70db48` | 2025-12-30 15:01 |
| `models/style_models/NOOB_vp1_detailer_by_volnovik_v1.safetensors` | `/.autodl/7c/fa/de/7cfadeff1a8f9abd78f42dd1f274b675` | 2025-12-30 15:01 |
| `models/style_models/gongqijun_qwen.safetensors` | `/.autodl/0b/8e/5e/0b8e5ec77992287995c6fef09afbb534` | 2026-09-10 21:41 |
| `models/style_models/ma1ma1helmes_b-000014.safetensors` | `/.autodl/0d/f1/95/0df1958d26ab784659641a7ce818d378` | 2025-12-30 15:01 |
| `models/style_models/ppw_v8_Illuv2stable_128.safetensors` | `/.autodl/6f/96/bf/6f96bf5ad1d3dcebe0de1e75c9947372` | 2025-12-30 15:01 |

### `text_encoders` (5)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/text_encoders/Image-Turbo-text_encoder-Q4_K_M.gguf` | `/.autodl/b8/7b/8d/b87b8da97ebfc118c446fb03943c0c8b` | 2026-09-08 14:59 |
| `models/text_encoders/Qwen2.5-VL-7B-Instruct-Q4_K_M.gguf` | `/.autodl/14/f0/0f/14f00fec6edfb38d93048b730ae387fc` | 2026-09-14 13:33 |
| `models/text_encoders/model_quantized.onnx` | `/.autodl/f4/21/d6/f421d64ec022f0c5ab496ec0fd240e02` | 2026-09-23 01:58 |
| `models/text_encoders/qwen3vl_8b_int8_convrot.safetensors` | `/.autodl/6f/32/f9/6f32f9794879cea9e29830e9262c019c` | 2026-09-25 00:53 |
| `models/text_encoders/qwen3vl_8b_w4a8.safetensors` | `/.autodl/f0/89/8a/f0898a128048643ae0f182c4622d58b3` | 2026-09-21 00:20 |

### `text_encoders/FLUX.1-Kontext-dev` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/text_encoders/FLUX.1-Kontext-dev/6fb2bf27-9244-50e5-a5fc-8753ef8525e5.safetensors` | `/.autodl/black-forest-labs/FLUX.1-Kontext-dev/text_encoder_2/model-00002-of-00002.safetensors` | 2025-09-23 19:44 |
| `models/text_encoders/FLUX.1-Kontext-dev/a3d8745c-bb27-5fc3-bc42-cdcb873e8de3.safetensors` | `/.autodl/black-forest-labs/FLUX.1-Kontext-dev/text_encoder_2/model-00001-of-00002.safetensors` | 2025-09-23 19:44 |

### `text_encoders/FLUX.1-dev` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/text_encoders/FLUX.1-dev/8c4183b2-f6f7-5c42-b9ba-92231b34b754.safetensors` | `/.autodl/black-forest-labs/FLUX.1-dev/text_encoder/model.safetensors` | 2025-09-23 19:44 |

### `text_encoders/Qwen-Image-2.1` (4)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/text_encoders/Qwen-Image-2.1/model-00001-of-00004.safetensors` | `/.autodl/Qwen/Qwen-Image-2.1/text_encoder/model-00001-of-00004.safetensors` | 2026-09-29 10:50 |
| `models/text_encoders/Qwen-Image-2.1/model-00002-of-00004.safetensors` | `/.autodl/Qwen/Qwen-Image-2.1/text_encoder/model-00002-of-00004.safetensors` | 2026-09-29 10:50 |
| `models/text_encoders/Qwen-Image-2.1/model-00003-of-00004.safetensors` | `/.autodl/Qwen/Qwen-Image-2.1/text_encoder/model-00003-of-00004.safetensors` | 2026-09-29 10:50 |
| `models/text_encoders/Qwen-Image-2.1/model-00004-of-00004.safetensors` | `/.autodl/Qwen/Qwen-Image-2.1/text_encoder/model-00004-of-00004.safetensors` | 2026-09-29 10:50 |

### `text_encoders/Qwen-Image-Edit-2511` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/text_encoders/Qwen-Image-Edit-2511/de62a29a-c044-5353-b457-6ca240ac6aa4.safetensors` | `/.autodl/54/2c/85/542c855aeb4ed9bd24fc478b2e04214a` | 2025-09-23 19:44 |
| `models/text_encoders/Qwen-Image-Edit-2511/frpc_linux_amd64_v0.3` | `/.autodl/d9/62/df/d962df6d33741b8c7b2bbd350ab2c455` | 2025-09-29 20:28 |

### `text_encoders/models` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/text_encoders/models/789a53dc-4383-5e67-9a09-da80e43e8cd0.safetensors` | `/.autodl/b8/98/22/b89822a44279e6d83c06a5061d7b1ca6` | 2025-09-23 19:44 |
| `models/text_encoders/models/qwen_2.5.safetensors` | `/.autodl/b8/98/22/b89822a44279e6d83c06a5061d7b1ca6` | 2025-11-21 21:17 |

### `text_encoders/stable-diffusion-xl-base-1.0` (2)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/text_encoders/stable-diffusion-xl-base-1.0/a6da6474-7a7c-50d1-bbb8-3b2b88c3dfae.safetensors` | `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/text_encoder_2/model.fp16.safetensors` | 2025-09-23 19:44 |
| `models/text_encoders/stable-diffusion-xl-base-1.0/clip_g.safetensors` | `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/text_encoder_2/model.fp16.safetensors` | 2025-10-09 12:55 |

### `unet` (5)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/unet/Flux-fill-Q8_0.gguf` | `/.autodl/2e/6f/e9/2e6fe9c4b9dbafcc320baae3798f2b6a` | 2026-09-15 00:35 |
| `models/unet/flux1-dev-fp8.safetensors` | `/.autodl/39/7c/06/397c06d6752a47005c6c7ea594551be1` | 2025-10-12 02:25 |
| `models/unet/qwen-rapid-nsfw-v5.3-Q4_K_M.gguf` | `/.autodl/b9/01/fc/b901fc888b8b46b2f83d9af6ebc5d161` | 2026-09-15 00:56 |
| `models/unet/推荐FULX.safetensors` | `/.autodl/19/dc/8f/19dc8fc8fc8fc7c379d59291662fea68` | 2026-09-15 00:10 |
| `models/unet/麦橘超然majicFlus_v1.safetensors` | `/.autodl/ff/26/38/ff2638259798f38c86e864b6da8f853b` | 2026-09-14 14:05 |

### `upscale_models` (3)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/upscale_models/4xNomos8kHAT-L_otf.pth` | `/.autodl/27/63/24/276324aada8e8289bfda7baa88205f4e` | 2026-09-14 12:02 |
| `models/upscale_models/4xNomos8kSCHAT-L.safetensors` | `/.autodl/3d/d9/e8/3dd9e8a172970936fe6c76746a87f37d` | 2026-09-14 12:01 |
| `models/upscale_models/T_S_2x-AnimeSharpV4_RCAN.safetensors` | `/.autodl/e1/cf/75/e1cf757ab6e0f043bc4fa21c98251792` | 2026-09-20 13:23 |

### `upscale_models/models` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/upscale_models/models/ESRGAN_4x.pth` | `/.autodl/6c/ae/a9/6caea96e18438caf70505f64e93e10b3` | 2025-10-02 23:35 |

### `vae` (14)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/vae/Z-VAE.safetensors` | `/.autodl/Tongyi-MAI/Z-Image/vae/diffusion_pytorch_model.safetensors` | 2026-01-20 20:54 |
| `models/vae/hyperVAEKrea2Minimax_v20MinimaxX2Upscale.safetensors` | `/.autodl/c9/56/8b/c9568bb0df37704aede65fc973edafd6` | 2026-09-28 23:17 |
| `models/vae/marigold_v2_albedo_vae.safetensors` | `/.autodl/70/7f/d6/707fd68876534e7ff2637904c25862b4` | 2026-09-14 02:47 |
| `models/vae/marigold_v2_depth_log_stage2_vae.safetensors` | `/.autodl/b7/2f/fb/b72ffb4841dacb8008339ac7e616fbf7` | 2026-09-14 02:49 |
| `models/vae/marigold_v2_normals_vae.safetensors` | `/.autodl/3f/a6/a2/3fa6a256e64e386ad16a9ae62283ca23` | 2026-09-14 02:51 |
| `models/vae/ming_image_vae_bf16.safetensors` | `/.autodl/2d/62/d2/2d62d26123d87a16f76ace0218ea919d` | 2026-09-28 09:16 |
| `models/vae/minimax_h3_vae_decoder.onnx` | `/.autodl/3e/17/b3/3e17b3bbee0f8155313cdfc179a24d4e` | 2026-09-18 13:30 |
| `models/vae/minimax_h3_vae_decoder.onnx.data` | `/.autodl/66/9f/61/669f61a7a35edcbb509640639d8a06e9` | 2026-09-18 14:30 |
| `models/vae/minimax_h3_vae_encoder.onnx` | `/.autodl/4f/37/6c/4f376cbf98dae5fcc48156a91d4b0b83` | 2026-09-18 13:30 |
| `models/vae/qwen_image_2.1_vae_bf16.safetensors` | `/.autodl/e9/91/c8/e991c8302f76ed7491244e0a5f0b64db` | 2026-09-25 00:34 |
| `models/vae/trellis_2_shape_vae_bf16.safetensors` | `/.autodl/fb/89/44/fb8944dc6842811ecbb85d28dc5a0909` | 2026-09-29 17:32 |
| `models/vae/trellis_2_texture_vae_bf16.safetensors` | `/.autodl/57/ce/db/57cedbb67d444daf7f6caea1fe29299d` | 2026-09-29 17:33 |
| `models/vae/triposplat_vae_decoder_fp16.safetensors` | `/.autodl/e2/4f/32/e24f321a32158c7af0e65a19d910450d` | 2026-06-04 12:10 |
| `models/vae/vae.safetensors` | `/.autodl/14/70/fb/1470fbaef3a41da8b3c4bf7411684022` | 2026-09-20 22:05 |

### `vae/Comfy-Org-z_image` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/vae/Comfy-Org-z_image/ae.sft` | `/.autodl/5c/8c/20/5c8c2087d13d0951b36be6dfbd3cd157` | 2025-10-11 15:22 |

### `vae/MiniMax-MiniMax-H3` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/vae/MiniMax-MiniMax-H3/config.json` | `/.autodl/ee/df/62/eedf62d539b2e47bfd830ffef4e46033` | 2026-09-14 11:33 |

### `vae/Qwen-Image-2.1` (1)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/vae/Qwen-Image-2.1/diffusion_pytorch_model.safetensors` | `/.autodl/Qwen/Qwen-Image-2.1/vae/diffusion_pytorch_model.safetensors` | 2026-09-29 10:50 |

### `yolo` (4)

| 目标 | 云库来源 | 更新时间 |
|---|---|---|
| `models/yolo/dw-ll_ucoco_384_bs5.torchscript.pt` | `/.autodl/65/58/4e/65584efa00abe85641cfb4af964c7c7f` | 2026-04-11 21:58 |
| `models/yolo/real_person_detection_v0_l_yv11.pt` | `/.autodl/c0/a6/5c/c0a65cdbd424302a1afe8417b7c1aa4f` | 2026-04-13 21:05 |
| `models/yolo/vitpose_h_wholebody_data.bin` | `/.autodl/62/a7/67/62a767bd296a80bae326ad61a4bc6031` | 2025-10-26 00:40 |
| `models/yolo/vitpose_h_wholebody_model.onnx` | `/.autodl/a6/a1/5c/a6a15c6fb2a76437e3111cccf4b5f0ea` | 2025-10-26 00:40 |

## 同名多源冲突(134 组, 保留更新时间最新者)

落选来源文件仍在原路径, 未删除。

### `models/ASR/Step-Audio-TTS-3B/model.pt` ← 保留 `/.autodl/f6/8e/43/f68e43213feb29605a145ded1cdcc1f4` (更新于 2026-07-19 10:10)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/stepfun-ai/Step-Audio-Tokenizer/dengcunqin/speech_paraformer-large_asr_nat-zh-cantonese-en-16k-vocab8501-online/model.pt` | 2026-03-18 17:01 | 840 MB |

### `models/LLM/LICENSE` ← 保留 `/.autodl/0b/19/e6/0b19e609b901d29b7a3b908e80e81314` (更新于 2025-09-25 23:00)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/15/c5/1c/15c51c21254625e68f0788f309e2859a` | 2025-09-25 19:59 | 0 MB |

### `models/LLM/Qwen3.5-9B.Q8_0.gguf` ← 保留 `/.autodl/92/e2/3f/92e23f0b9119e4f1a239016ecba840d7` (更新于 2026-04-03 15:29)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/3b/de/a9/3bdea9a000faae0363c61f26c07a5611` | 2026-03-18 12:09 | 9086 MB |

### `models/LLM/README.md` ← 保留 `/.autodl/1d/6a/6e/1d6a6e0c9f1baa162829485d98099691` (更新于 2025-10-16 13:23)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/da/3b/c5/da3bc57cc4995f72ca3ee71e7c3b93d9` | 2025-10-16 12:54 | 0 MB |
| `/.autodl/4b/5e/7a/4b5e7ab404d4c65f66cc7c255cbc5072` | 2025-10-16 11:49 | 0 MB |
| `/.autodl/47/aa/ff/47aaff7a4886324191e5df059d0d6a56` | 2025-10-16 11:11 | 0 MB |
| `/.autodl/97/4e/bb/974ebbc41393db9dcbb69755a55a9f95` | 2025-10-02 01:18 | 0 MB |
| `/.autodl/97/4e/bb/974ebbc41393db9dcbb69755a55a9f95` | 2025-10-02 00:52 | 0 MB |
| `/.autodl/e1/11/a1/e111a172b4db87caed221ba009891629` | 2025-09-25 23:00 | 0 MB |
| `/.autodl/d7/76/95/d77695abd8a111fb9e793eb6ba461249` | 2025-09-25 19:59 | 0 MB |
| `/.autodl/d9/87/4c/d9874cb951385743f6cc64b82777861b` | 2025-09-25 15:51 | 0 MB |

### `models/LLM/SenseNova-U1-8B-MoT/model-00001-of-00008.safetensors` ← 保留 `/.autodl/8a/f4/84/8af48428b97f8df932e2291aa442e9d4` (更新于 2026-09-11 22:23)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/sensenova/SenseNova-U1-8B-MoT/model-00001-of-00008.safetensors` | 2026-05-13 23:11 | 4708 MB |

### `models/LLM/SenseNova-U1-8B-MoT/model-00002-of-00008.safetensors` ← 保留 `/.autodl/4e/69/f2/4e69f24102120696d4547e46ebf73e04` (更新于 2026-09-11 00:21)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/sensenova/SenseNova-U1-8B-MoT/model-00002-of-00008.safetensors` | 2026-05-13 23:11 | 4768 MB |

### `models/LLM/SenseNova-U1-8B-MoT/model-00003-of-00008.safetensors` ← 保留 `/.autodl/34/37/0a/34370ae61516b1453c98ea7f8e536dc1` (更新于 2026-09-11 22:57)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/sensenova/SenseNova-U1-8B-MoT/model-00003-of-00008.safetensors` | 2026-05-13 23:11 | 4704 MB |

### `models/LLM/SenseNova-U1-8B-MoT/model-00004-of-00008.safetensors` ← 保留 `/.autodl/c8/f0/25/c8f025a2ee46eb9112d84e074e698f0e` (更新于 2026-09-11 23:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/sensenova/SenseNova-U1-8B-MoT/model-00004-of-00008.safetensors` | 2026-05-13 23:11 | 4768 MB |

### `models/LLM/SenseNova-U1-8B-MoT/model-00005-of-00008.safetensors` ← 保留 `/.autodl/db/41/6f/db416f443bb211dff705bd483b8dd7cd` (更新于 2026-09-12 00:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/sensenova/SenseNova-U1-8B-MoT/model-00005-of-00008.safetensors` | 2026-05-13 23:11 | 4704 MB |

### `models/LLM/SenseNova-U1-8B-MoT/model-00006-of-00008.safetensors` ← 保留 `/.autodl/4f/bd/cc/4fbdccf2363a18d2c6e81cef54847744` (更新于 2026-09-12 01:04)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/sensenova/SenseNova-U1-8B-MoT/model-00006-of-00008.safetensors` | 2026-05-13 23:11 | 4704 MB |

### `models/LLM/SenseNova-U1-8B-MoT/model-00007-of-00008.safetensors` ← 保留 `/.autodl/b0/9e/8a/b09e8ada3965967a114d5c2e8fd2165d` (更新于 2026-09-12 01:37)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/sensenova/SenseNova-U1-8B-MoT/model-00007-of-00008.safetensors` | 2026-05-13 23:11 | 3776 MB |

### `models/LLM/SenseNova-U1-8B-MoT/model-00008-of-00008.safetensors` ← 保留 `/.autodl/84/17/41/841741d9155345c9b516757d4d9a7ff6` (更新于 2026-09-12 13:57)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/sensenova/SenseNova-U1-8B-MoT/model-00008-of-00008.safetensors` | 2026-05-13 23:10 | 1344 MB |

### `models/LLM/chat_template.json` ← 保留 `/.autodl/7f/37/0a/7f370ac84627406c5dd0b6400c2289f8` (更新于 2025-10-16 13:23)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/2b/0b/ba/2b0bba5aeb1f5581a0bc951a80d984b2` | 2025-10-16 12:54 | 0 MB |
| `/.autodl/2b/0b/ba/2b0bba5aeb1f5581a0bc951a80d984b2` | 2025-10-16 11:49 | 0 MB |
| `/.autodl/34/0d/66/340d6696136954b83e8b5434a598ccb1` | 2025-10-16 11:11 | 0 MB |

### `models/LLM/config.json` ← 保留 `/.autodl/50/f4/d0/50f4d07fb0c8de34bc9fd593c95e9716` (更新于 2025-10-16 13:23)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/17/06/8d/17068d7109e7df78ae17a952f63138c0` | 2025-10-16 11:49 | 0 MB |
| `/.autodl/17/06/8d/17068d7109e7df78ae17a952f63138c0` | 2025-10-16 11:11 | 0 MB |
| `/.autodl/16/82/70/16827006a42b9eed7c795d1fab29a0b8` | 2025-10-02 01:18 | 0 MB |
| `/.autodl/5f/94/9a/5f949a27aae73a76a94c2ebc6b75d975` | 2025-10-02 00:52 | 0 MB |
| `/.autodl/f5/73/a1/f573a1fca59a1d5f44c4db8de6a13c00` | 2025-09-25 23:00 | 0 MB |
| `/.autodl/d6/d0/70/d6d070f441ea76c7a1e71febaaf7c350` | 2025-09-25 19:59 | 0 MB |
| `/.autodl/85/a4/91/85a491bc89baa282426717ff96c55d80` | 2025-09-25 15:51 | 0 MB |

### `models/LLM/configuration.json` ← 保留 `/.autodl/5e/17/04/5e170425c97cda8f798c74041979a569` (更新于 2025-10-16 13:23)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/04/0f/58/040f5895a7c8ae7cf58c622e3fcc1ba5` | 2025-09-25 19:59 | 0 MB |

### `models/LLM/gemma-3-12b-it-abliterated-sikaworld-high-fidelity-edition.safetensors` ← 保留 `/.autodl/42/ec/33/42ec337e04506dbff92040601f4cf05f` (更新于 2026-07-20 19:25)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/9c/87/17/9c87172f77f43c0e7f3d953b01830552` | 2026-07-20 19:21 | 11800 MB |

### `models/LLM/generation_config.json` ← 保留 `/.autodl/ff/83/34/ff83341cb36174edd24f64ac03315274` (更新于 2025-10-16 13:23)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/4f/c7/db/4fc7dbf40a728941247235a70e6634a7` | 2025-10-16 12:54 | 0 MB |
| `/.autodl/4f/c7/db/4fc7dbf40a728941247235a70e6634a7` | 2025-10-16 11:49 | 0 MB |
| `/.autodl/59/62/6a/59626ac557e1ccbe6c440248e3d835c3` | 2025-09-25 23:00 | 0 MB |
| `/.autodl/59/62/6a/59626ac557e1ccbe6c440248e3d835c3` | 2025-09-25 15:51 | 0 MB |

### `models/LLM/mmproj-BF16.gguf` ← 保留 `/.autodl/41/16/fd/4116fde520e6d0c881abc2d9b0c2dc8d` (更新于 2026-07-17 00:34)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/unsloth/Qwen3.5-9B-GGUF/mmproj-BF16.gguf` | 2026-03-11 17:08 | 879 MB |

### `models/LLM/model-00001-of-00002.safetensors` ← 保留 `/.autodl/Qwen/wen3-VL-4B-Instruct/model-00001-of-00002.safetensors` (更新于 2026-09-02 00:52)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/ca/3b/7d/ca3b7d774a3fda2fcd970b4b3c0e9bd0` | 2026-07-16 17:20 | 5114 MB |
| `/.autodl/1a/c9/7c/1ac97cef18a9d47656174c0d5ba975c0` | 2026-05-31 03:27 | 4745 MB |
| `/.autodl/ca/3b/7d/ca3b7d774a3fda2fcd970b4b3c0e9bd0` | 2026-04-12 00:45 | 5114 MB |
| `/.autodl/07/cf/45/07cf450aec714a4d66a5b81f78790b40` | 2026-01-22 03:27 | 4736 MB |
| `/.autodl/cb/7a/85/cb7a85c04a2019a9a7fa0f851d34c3a1` | 2025-10-16 13:06 | 4737 MB |
| `/.autodl/55/dc/e0/55dce061919857b8099647ba714e0282` | 2025-09-27 00:26 | 4646 MB |
| `/.autodl/6d/84/32/6d84326269e40a1773fd563fa40058cf` | 2025-09-26 23:58 | 4666 MB |

### `models/LLM/model-00001-of-00004.safetensors` ← 保留 `/.autodl/7d/a8/33/7da8339d777f46bd57006633579fe0f6` (更新于 2026-01-22 05:54)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/84/2d/2a/842d2a9c35ebd8f20401430583aa2e46` | 2025-12-31 09:23 | 4745 MB |
| `/.autodl/63/68/43/636843662c41eda5b7e986a951739009` | 2025-12-09 14:32 | 5074 MB |
| `/.autodl/7e/e1/29/7ee129129dc28151aaff5425fd42db3b` | 2025-11-25 11:20 | 4720 MB |
| `/.autodl/24/5a/d8/245ad8de5b7d42df2885cfba9a50f2fc` | 2025-10-16 11:59 | 4675 MB |
| `/.autodl/9a/8a/c0/9a8ac027b735bcae41d82f1d9fd1855b` | 2025-10-02 01:07 | 4731 MB |
| `/.autodl/e7/e8/39/e7e8399329373acfb7c6e81615f38676` | 2025-09-28 15:16 | 4659 MB |

### `models/LLM/model-00001-of-00005.safetensors` ← 保留 `/.autodl/5b/ae/27/5bae27b359586e89642964ca0749683d` (更新于 2026-04-05 16:49)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/86/44/c8/8644c8b51bc77b2e0c050ce5e7be30f7` | 2026-01-21 22:23 | 3719 MB |
| `/.autodl/86/44/c8/8644c8b51bc77b2e0c050ce5e7be30f7` | 2025-12-08 14:07 | 3719 MB |
| `/.autodl/86/44/c8/8644c8b51bc77b2e0c050ce5e7be30f7` | 2025-12-08 12:56 | 3719 MB |
| `/.autodl/86/44/c8/8644c8b51bc77b2e0c050ce5e7be30f7` | 2025-12-08 12:53 | 3719 MB |

### `models/LLM/model-00002-of-00002.safetensors` ← 保留 `/.autodl/Qwen/wen3-VL-4B-Instruct/model-00002-of-00002.safetensors` (更新于 2026-09-02 00:53)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/dd/08/7a/dd087ac2e71e4feba87591b200aaacf3` | 2026-07-16 17:20 | 4984 MB |
| `/.autodl/11/9d/c3/119dc3e5b0c9e2a7d44d2769169e1755` | 2026-05-31 03:32 | 112 MB |
| `/.autodl/dd/08/7a/dd087ac2e71e4feba87591b200aaacf3` | 2026-04-12 00:58 | 4984 MB |
| `/.autodl/ff/74/ac/ff74ac819fed24804512d772f97520d7` | 2026-01-22 03:21 | 3006 MB |
| `/.autodl/4c/51/b5/4c51b5d19e35c878aeb8a515801fb0c3` | 2025-10-16 13:00 | 3727 MB |
| `/.autodl/0f/ac/ca/0facca85007b67038a258ac5df5b3196` | 2025-09-27 00:26 | 256 MB |
| `/.autodl/4e/71/98/4e719818521aa45be659872d524fd69d` | 2025-09-26 23:58 | 1002 MB |

### `models/LLM/model-00002-of-00004.safetensors` ← 保留 `/.autodl/3c/7b/f8/3c7bf8b11683ffc8766b56004dede4e2` (更新于 2026-05-31 03:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/d7/00/89/d70089efeb334be2711f13defe0ca155` | 2026-01-22 06:01 | 5056 MB |
| `/.autodl/80/a5/e0/80a5e08e2459bd2d0f9f22ba2ced2250` | 2025-12-31 09:28 | 4705 MB |
| `/.autodl/87/40/44/874044ff1a24951c89c4dbbb3a40f6f4` | 2025-12-09 14:37 | 5057 MB |
| `/.autodl/89/f0/3a/89f03aaa2ad17e11ffbd8b1a9d35ac52` | 2025-11-25 11:26 | 4732 MB |
| `/.autodl/b9/5a/07/b95a071031f1a2fc1d37968b70eaad8e` | 2025-10-16 12:06 | 4688 MB |
| `/.autodl/3b/5b/d9/3b5bd9efada20946e6e33f7d6a4b2de9` | 2025-10-02 01:00 | 4732 MB |

### `models/LLM/model-00002-of-00005.safetensors` ← 保留 `/.autodl/ee/92/04/ee92040190004b9ab380e3dac7c18c45` (更新于 2026-04-05 16:49)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/12/20/b9/1220b9cc11ac55254d4165e285c7e2d9` | 2026-01-21 22:18 | 3685 MB |
| `/.autodl/12/20/b9/1220b9cc11ac55254d4165e285c7e2d9` | 2025-12-08 14:07 | 3685 MB |
| `/.autodl/12/20/b9/1220b9cc11ac55254d4165e285c7e2d9` | 2025-12-08 12:56 | 3685 MB |
| `/.autodl/12/20/b9/1220b9cc11ac55254d4165e285c7e2d9` | 2025-12-08 12:54 | 3685 MB |

### `models/LLM/model-00003-of-00004.safetensors` ← 保留 `/.autodl/d6/22/87/d62287ce7c41d7e4683f96ce13344136` (更新于 2026-05-31 03:29)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/13/e4/1b/13e41b8dd5963cc65b021a4c6fd7c269` | 2026-01-22 05:48 | 4336 MB |
| `/.autodl/15/5b/86/155b86ba11c2d37adc2312d1a29074f8` | 2025-12-31 09:32 | 4664 MB |
| `/.autodl/01/e9/e4/01e9e44667a46ca5527c40964f417600` | 2025-12-09 14:42 | 5057 MB |
| `/.autodl/6d/1f/47/6d1f473b5bdad9c1b41753a340145f0f` | 2025-11-25 11:34 | 4732 MB |
| `/.autodl/44/1f/27/441f27b7f22858b16ba7605154f1ba8d` | 2025-10-16 12:12 | 4768 MB |
| `/.autodl/fa/10/0d/fa100d2b178e0afe7715de3529e10a20` | 2025-10-02 01:12 | 3890 MB |

### `models/LLM/model-00003-of-00005.safetensors` ← 保留 `/.autodl/be/84/10/be8410cd1dc33f42a51d74f5d51d2975` (更新于 2026-04-05 16:49)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/4e/c4/05/4ec40524f0a3e91ec66dc5729d46d118` | 2026-01-21 22:13 | 3685 MB |
| `/.autodl/4e/c4/05/4ec40524f0a3e91ec66dc5729d46d118` | 2025-12-08 14:07 | 3685 MB |
| `/.autodl/4e/c4/05/4ec40524f0a3e91ec66dc5729d46d118` | 2025-12-08 12:56 | 3685 MB |
| `/.autodl/4e/c4/05/4ec40524f0a3e91ec66dc5729d46d118` | 2025-12-08 12:53 | 3685 MB |
| `/.autodl/4e/c4/05/4ec40524f0a3e91ec66dc5729d46d118` | 2025-12-08 12:53 | 3685 MB |

### `models/LLM/model-00004-of-00004.safetensors` ← 保留 `/.autodl/0a/af/cc/0aafcc743c0a30e72c977b918c9f9e5c` (更新于 2026-05-31 03:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/72/70/3f/72703ff71e99e2d43fa64a3274d938f0` | 2026-01-22 05:43 | 2152 MB |
| `/.autodl/17/04/6f/17046f72a720e51dab6cc812c781f3f2` | 2025-12-31 09:34 | 1200 MB |
| `/.autodl/3d/6c/33/3d6c3312ba81d7663e97ccba7b48d30a` | 2025-12-09 14:47 | 4442 MB |
| `/.autodl/fa/b6/0e/fab60e39907ce2f3d4e7ffa01b1685e9` | 2025-11-25 11:38 | 2961 MB |
| `/.autodl/13/15/15/131515c326389881bab75f96780aab7a` | 2025-10-16 11:53 | 2590 MB |
| `/.autodl/f0/a1/23/f0a12337efe782016472f3d17f16588a` | 2025-10-02 01:44 | 1940 MB |

### `models/LLM/model-00004-of-00005.safetensors` ← 保留 `/.autodl/0f/84/f6/0f84f6d8481bea50eeb8de41c6db0079` (更新于 2026-04-05 16:49)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/7b/57/97/7b5797821c1bbb60aa3dd9a65c88eedc` | 2026-01-21 22:27 | 3685 MB |
| `/.autodl/7b/57/97/7b5797821c1bbb60aa3dd9a65c88eedc` | 2025-12-08 14:07 | 3685 MB |
| `/.autodl/7b/57/97/7b5797821c1bbb60aa3dd9a65c88eedc` | 2025-12-08 12:56 | 3685 MB |
| `/.autodl/7b/57/97/7b5797821c1bbb60aa3dd9a65c88eedc` | 2025-12-08 12:54 | 3685 MB |

### `models/LLM/model.safetensors` ← 保留 `/.autodl/80/16/5b/80165ba356a71ec483539dcf40ea1f1a` (更新于 2026-09-25 00:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/5f/6f/4b/5f6f4b3a3d0ec8a4a3f7f2cc1f0cd251` | 2026-08-26 19:56 | 1136 MB |
| `/.autodl/5f/2e/3d/5f2e3dafe599c6629af12160e31aa00a` | 2026-08-23 11:18 | 2592 MB |
| `/.autodl/17/19/9c/17199ca96b5834ac77cb6c6b55d20388` | 2026-01-22 02:39 | 2641 MB |
| `/.autodl/5d/8d/8f/5d8d8f7c41f79160117160d1f13afe15` | 2026-01-22 02:30 | 5792 MB |
| `/.autodl/ca/0b/6c/ca0b6cc31c3b5c9d0236da365c1f7a6b` | 2026-01-22 02:22 | 2530 MB |
| `/.autodl/a6/a7/a7/a6a7a7ada992f203f802c812bb8ade78` | 2026-01-21 22:08 | 6580 MB |
| `/.autodl/6c/49/b5/6c49b59d80ad0591ae9cbb9c26a0d8fc` | 2025-12-31 09:17 | 3888 MB |
| `/.autodl/MiaoshouAI/Florence-2-base-PromptGen-v2.0/model.safetensors` | 2025-10-30 19:35 | 1033 MB |
| `/.autodl/20/0e/e7/200ee7bc5d4a2cdad2ae376eff7f7ad4` | 2025-10-02 01:23 | 3725 MB |
| `/.autodl/d7/ae/51/d7ae514c5872600d8daa3049298c1453` | 2025-09-27 01:10 | 2530 MB |

### `models/LLM/model.safetensors.index.json` ← 保留 `/.autodl/ef/e0/c4/efe0c45f6a8e11f0dfa43494659bdc2a` (更新于 2025-10-16 13:23)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/15/bb/27/15bb2771b7a9610b4f1298319f58e535` | 2025-10-16 11:49 | 0 MB |
| `/.autodl/15/bb/27/15bb2771b7a9610b4f1298319f58e535` | 2025-10-16 11:33 | 0 MB |
| `/.autodl/2a/25/9a/2a259a3dbc3316e00c63791695babe01` | 2025-10-02 01:12 | 0 MB |
| `/.autodl/52/67/06/5267062723802fa8b1d8d506ea19986f` | 2025-09-25 23:00 | 0 MB |
| `/.autodl/5f/d9/60/5fd96070c6fab3ecf5735c7fb261e80f` | 2025-09-25 19:59 | 0 MB |
| `/.autodl/1f/82/6f/1f826f0016a2d9becb00e52c90cb678a` | 2025-09-25 15:51 | 0 MB |

### `models/LLM/tokenizer.json` ← 保留 `/.autodl/f1/31/94/f13194680891e5fd5817a56a341bf015` (更新于 2025-10-16 13:23)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/6c/90/31/6c9031018592e0cfccb5fc876a71b06e` | 2025-10-02 01:13 | 10 MB |
| `/.autodl/c9/4b/9a/c94b9adb41dddaa3fe95dd06cf5897a1` | 2025-09-25 19:59 | 6 MB |

### `models/LLM/tokenizer_config.json` ← 保留 `/.autodl/50/c5/d3/50c5d37d9d3904e0e243e709bdbb6c37` (更新于 2025-10-16 13:23)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/4f/98/c5/4f98c568c63d7ed8063946108a2d1aed` | 2025-10-16 12:54 | 0 MB |
| `/.autodl/4f/98/c5/4f98c568c63d7ed8063946108a2d1aed` | 2025-10-16 11:49 | 0 MB |
| `/.autodl/a2/79/6b/a2796b8d83c587e37b6c4db54d5c9b3f` | 2025-10-02 01:00 | 0 MB |
| `/.autodl/b0/6e/10/b06e103ac555ec4b51266078b518c0f0` | 2025-09-25 23:00 | 0 MB |
| `/.autodl/af/ae/08/afae08adec17b90629f06af7fb90d600` | 2025-09-25 19:59 | 0 MB |
| `/.autodl/b0/6e/10/b06e103ac555ec4b51266078b518c0f0` | 2025-09-25 15:51 | 0 MB |

### `models/TTS/IndexTTS-2.5-Comfy/config.json` ← 保留 `/.autodl/d3/5b/4f/d35b4f90004c074eab01d704de5591a0` (更新于 2026-08-28 12:44)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/d1/6d/00/d16d00d42f069a6f5c8ca572328ff680` | 2026-08-28 12:43 | 0 MB |
| `/.autodl/68/d7/23/68d723d3d3abf67072effe23dadb8bf1` | 2026-08-28 12:43 | 0 MB |

### `models/TTS/IndexTTS-2.5-Comfy/model.safetensors` ← 保留 `/.autodl/5b/0a/e2/5b0ae2ff886124c262673a86dac9a169` (更新于 2026-08-28 12:44)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/IndexTeam/IndexTTS-2/qwen0.6bemo4-merge/model.safetensors` | 2026-08-28 12:42 | 1136 MB |
| `/.autodl/IndexTeam/IndexTTS-2/qwen0.6bemo4-merge/model.safetensors` | 2026-08-22 01:46 | 1136 MB |
| `/.autodl/IndexTeam/IndexTTS-2/qwen0.6bemo4-merge/model.safetensors` | 2026-08-13 10:34 | 1136 MB |
| `/.autodl/IndexTeam/IndexTTS-2/qwen0.6bemo4-merge/model.safetensors` | 2026-04-22 10:04 | 1136 MB |
| `/.autodl/IndexTeam/IndexTTS-2/qwen0.6bemo4-merge/model.safetensors` | 2026-01-14 15:39 | 1136 MB |
| `/.autodl/IndexTeam/IndexTTS-2/qwen0.6bemo4-merge/model.safetensors` | 2026-01-05 19:18 | 1136 MB |
| `/.autodl/IndexTeam/IndexTTS-2/qwen0.6bemo4-merge/model.safetensors` | 2025-11-20 19:55 | 1136 MB |

### `models/TTS/Qwen3-TTS-12Hz-1.7B-CustomVoice.zip` ← 保留 `/.autodl/09/ad/1d/09ad1d5fa2a089d943d56415c6d483a9` (更新于 2026-04-22 22:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/6a/e6/4e/6ae64eba4cda5523ece87a69c9e86656` | 2026-02-06 14:14 | 1 MB |

### `models/TTS/README.md` ← 保留 `/.autodl/a0/dc/a8/a0dca84124b1f8cd601e9fa8b0a05816` (更新于 2025-10-16 20:59)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/11/9a/27/119a27a286fc77cf7ecc14e341661780` | 2025-10-02 10:15 | 0 MB |

### `models/TTS/Step-Audio-TTS-3B/flow.pt` ← 保留 `/.autodl/stepfun-ai/Step-Audio-TTS-3B/CosyVoice-300M-25Hz/flow.pt` (更新于 2026-03-18 17:01)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/stepfun-ai/Step-Audio-TTS-3B/CosyVoice-300M-25Hz-Music/flow.pt` | 2026-03-18 17:00 | 402 MB |

### `models/TTS/bigvgan_discriminator_optimizer.pt` ← 保留 `/.autodl/d9/5f/4b/d95f4bb032d92e4f7a59378f3371bb7b` (更新于 2026-04-22 09:44)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/61/67/fb/6167fbc65a55867989d0885ccade87af` | 2026-04-13 10:16 | 1455 MB |

### `models/TTS/bigvgan_discriminator_optimizer_3msteps.pt` ← 保留 `/.autodl/dd/11/44/dd114469406b903458ace6af2e6bc93d` (更新于 2026-04-22 09:50)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/8c/9f/34/8c9f34e49cc8fd8294b7139a2c511800` | 2026-04-13 10:16 | 1455 MB |

### `models/TTS/bigvgan_generator_3msteps.pt` ← 保留 `/.autodl/7c/3e/00/7c3e00bd06c9fc4bfa6aaee9e1fbb712` (更新于 2026-04-22 09:54)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/61/df/70/61df709276dbd3c5282da3984815fb09` | 2026-04-13 10:16 | 466 MB |

### `models/TTS/config.json` ← 保留 `/.autodl/1f/6d/d9/1f6dd9c4a4bc46f84fe4f763df02b0e1` (更新于 2025-10-16 20:59)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/9a/7b/45/9a7b457d1922d1da2b781e2c8f1479ea` | 2025-10-02 10:15 | 0 MB |

### `models/TTS/configuration.json` ← 保留 `/.autodl/82/dc/f8/82dcf8c6ca41273fbf35d167922a2434` (更新于 2025-11-01 00:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/7d/ca/df/7dcadf7a096598f98db2ce0df055fde0` | 2025-10-16 20:59 | 0 MB |
| `/.autodl/91/12/4d/91124d776bec0b391288489244121f61` | 2025-10-02 10:15 | 0 MB |
| `/.autodl/7d/ca/df/7dcadf7a096598f98db2ce0df055fde0` | 2025-10-02 01:18 | 0 MB |
| `/.autodl/7d/ca/df/7dcadf7a096598f98db2ce0df055fde0` | 2025-10-02 01:00 | 0 MB |

### `models/TTS/model.safetensors` ← 保留 `/.autodl/a4/c5/2e/a4c52ed581e0d8d3e9f26b18ec7fc29e` (更新于 2026-08-31 21:14)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/b5/ef/05/b5ef05a51449482a8268625ca5db2916` | 2026-08-31 21:06 | 8089 MB |
| `/.autodl/35/a6/59/35a659a565907fd173d15a63be42cae8` | 2026-08-25 18:21 | 168 MB |
| `/.autodl/53/f5/6e/53f56e9aa933eee52b9b8908343b46b8` | 2026-08-25 18:21 | 162 MB |
| `/.autodl/b5/04/d7/b504d7c039fe0f15d29c565887e88d03` | 2026-08-25 18:19 | 1260 MB |
| `/.autodl/77/82/c0/7782c0fcbd779b5527801ac6ea7f8632` | 2026-08-25 18:14 | 1348 MB |
| `/.autodl/b1/32/a6/b132a6d1387c0ef4e3e74cbce523bb60` | 2026-08-25 18:10 | 2847 MB |
| `/.autodl/35/a6/59/35a659a565907fd173d15a63be42cae8` | 2026-08-25 17:58 | 168 MB |
| `/.autodl/35/a6/59/35a659a565907fd173d15a63be42cae8` | 2026-04-22 10:07 | 168 MB |
| `/.autodl/84/2c/b0/842cb086e7318420bcd412fbf9b9f569` | 2026-03-16 11:26 | 1789 MB |
| `/.autodl/34/12/a1/3412a1109ee5b88cf3e3ce315ab29663` | 2026-02-06 13:23 | 3655 MB |
| `/.autodl/34/12/a1/3412a1109ee5b88cf3e3ce315ab29663` | 2026-01-23 10:24 | 3655 MB |
| `/.autodl/34/12/a1/3412a1109ee5b88cf3e3ce315ab29663` | 2026-01-23 10:08 | 3655 MB |
| `/.autodl/35/a6/59/35a659a565907fd173d15a63be42cae8` | 2026-01-14 15:39 | 168 MB |
| `/.autodl/35/a6/59/35a659a565907fd173d15a63be42cae8` | 2026-01-05 19:28 | 168 MB |
| `/.autodl/3d/52/3b/3d523b643a0f329f47f3b18291ca1ac6` | 2025-12-30 20:39 | 360 MB |

### `models/TTS/pytorch_model.bin` ← 保留 `/.autodl/24/e6/1a/24e61ab29cb578bb0e99ecb07049b0cd` (更新于 2026-07-29 22:32)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/f3/0e/b1/f30eb1497d8644cb1fe44f4c0ca53223` | 2025-12-30 20:40 | 360 MB |
| `/.autodl/aa/96/e0/aa96e0632f2ba76f3aebb9f5eb595e0b` | 2025-10-02 10:17 | 1244 MB |

### `models/TTS/s2-pro-fp8/model.safetensors` ← 保留 `/.autodl/drbaph/s2-pro-fp8/model.safetensors` (更新于 2026-03-18 17:01)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/baicai1145/s2-pro-w4a16/model.safetensors` | 2026-03-18 17:01 | 4041 MB |
| `/.autodl/baicai1145/s2-pro-w4a16/model.safetensors` | 2026-03-18 16:09 | 4041 MB |

### `models/TTS/shiro-voice-pretrained/D40k.pth` ← 保留 `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v2/D40k.pth` (更新于 2026-01-24 22:14)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v1/D40k.pth` | 2026-01-24 22:13 | 104 MB |

### `models/TTS/shiro-voice-pretrained/D48k.pth` ← 保留 `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v2/D48k.pth` (更新于 2026-01-24 22:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v1/D48k.pth` | 2026-01-24 22:14 | 104 MB |

### `models/TTS/shiro-voice-pretrained/D_0.pth` ← 保留 `/.autodl/39c5bb/shiro-voice-pretrained/sovits/tiny/vec768l12_vol_emb/D_0.pth` (更新于 2026-01-24 22:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/39c5bb/shiro-voice-pretrained/sovits/hubertsoft/D_0.pth` | 2026-01-24 22:15 | 178 MB |
| `/.autodl/39c5bb/shiro-voice-pretrained/sovits/768l12/vol_emb/D_0.pth` | 2026-01-24 22:15 | 178 MB |
| `/.autodl/39c5bb/shiro-voice-pretrained/sovits/768l12/D_0.pth` | 2026-01-24 22:15 | 178 MB |
| `/.autodl/39c5bb/shiro-voice-pretrained/sovits/D_0.pth` | 2026-01-24 22:15 | 178 MB |

### `models/TTS/shiro-voice-pretrained/G40k.pth` ← 保留 `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v2/G40k.pth` (更新于 2026-01-24 22:14)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v1/G40k.pth` | 2026-01-24 22:14 | 69 MB |

### `models/TTS/shiro-voice-pretrained/G48k.pth` ← 保留 `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v2/G48k.pth` (更新于 2026-01-24 22:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v1/G48k.pth` | 2026-01-24 22:14 | 69 MB |

### `models/TTS/shiro-voice-pretrained/G_0.pth` ← 保留 `/.autodl/39c5bb/shiro-voice-pretrained/sovits/768l12/vol_emb/G_0.pth` (更新于 2026-01-24 22:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/39c5bb/shiro-voice-pretrained/sovits/tiny/vec768l12_vol_emb/G_0.pth` | 2026-01-24 22:15 | 122 MB |
| `/.autodl/39c5bb/shiro-voice-pretrained/sovits/hubertsoft/G_0.pth` | 2026-01-24 22:15 | 145 MB |
| `/.autodl/39c5bb/shiro-voice-pretrained/sovits/768l12/G_0.pth` | 2026-01-24 22:15 | 199 MB |
| `/.autodl/39c5bb/shiro-voice-pretrained/sovits/G_0.pth` | 2026-01-24 22:15 | 172 MB |

### `models/TTS/shiro-voice-pretrained/f0D40k.pth` ← 保留 `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v2/f0D40k.pth` (更新于 2026-01-24 22:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v1/f0D40k.pth` | 2026-01-24 22:14 | 104 MB |

### `models/TTS/shiro-voice-pretrained/f0D48k.pth` ← 保留 `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v2/f0D48k.pth` (更新于 2026-01-24 22:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v1/f0D48k.pth` | 2026-01-24 22:14 | 104 MB |

### `models/TTS/shiro-voice-pretrained/f0G40k.pth` ← 保留 `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v2/f0G40k.pth` (更新于 2026-01-24 22:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v1/f0G40k.pth` | 2026-01-24 22:14 | 69 MB |

### `models/TTS/shiro-voice-pretrained/f0G48k.pth` ← 保留 `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v2/f0G48k.pth` (更新于 2026-01-24 22:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/39c5bb/shiro-voice-pretrained/rvc/v1/f0G48k.pth` | 2026-01-24 22:14 | 69 MB |

### `models/TTS/shiro-voice-pretrained/model_0.pt` ← 保留 `/.autodl/39c5bb/shiro-voice-pretrained/sovits/diffusion/768l12/max100/model_0.pt` (更新于 2026-01-24 22:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/39c5bb/shiro-voice-pretrained/sovits/diffusion/hubertsoft/model_0.pt` | 2026-01-24 22:15 | 210 MB |
| `/.autodl/39c5bb/shiro-voice-pretrained/sovits/diffusion/768l12/model_0.pt` | 2026-01-24 22:15 | 210 MB |

### `models/background_removal/birefnet.py` ← 保留 `/.autodl/fa/5b/4f/fa5b4f0ac243012e2cf04fcad94088e6` (更新于 2026-08-26 22:00)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/37/1b/23/371b231c7778989cf8a35ea2912ff74c` | 2026-08-26 22:00 | 0 MB |

### `models/checkpoints/Hunyuan3D-2.1/model.fp16.ckpt` ← 保留 `/.autodl/Tencent-Hunyuan/Hunyuan3D-2.1/hunyuan3d-dit-v2-1/model.fp16.ckpt` (更新于 2025-11-10 19:54)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Tencent-Hunyuan/Hunyuan3D-2.1/hunyuan3d-vae-v2-1/model.fp16.ckpt` | 2025-11-10 19:54 | 625 MB |

### `models/checkpoints/dreamshaperXL_lightningDPMSDE.safetensors` ← 保留 `/.autodl/50/e5/75/50e575d38a5437f6af02d6cbe58dc5e0` (更新于 2026-09-15 11:30)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/f6/d9/46/f6d946d1aa53f7001e28e30c09fb5a1b` | 2025-11-11 02:34 | 6617 MB |

### `models/checkpoints/taesdxl_decoder.pth` ← 保留 `/.autodl/3f/21/dd/3f21ddf6ccf51c4182236dac7f9f98c0` (更新于 2025-10-02 16:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/cc/63/0e/cc630e4dacf767bcd18c320f9dc375fe` | 2025-09-29 22:08 | 4 MB |

### `models/clip_vision/latest.ckpt` ← 保留 `/.autodl/b7/8c/bf/b78cbfb95852ea7299ed1bf9c15fe384` (更新于 2026-01-05 23:18)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/f3/4f/d7/f34fd7c1d96c3da9dc2e80be3b1a7aff` | 2026-01-05 23:16 | 3978 MB |

### `models/controlnet/diffusion_pytorch_model.safetensors` ← 保留 `/.autodl/4e/52/58/4e52586c5a29671f5313b3fa58222496` (更新于 2026-02-20 14:59)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/5f/ec/c3/5fecc39f151b5b0112d5a74f12abcaa0` | 2026-02-20 14:58 | 3303 MB |
| `/.autodl/7c/6a/1e/7c6a1ecb2204a00318cb0a11e0a81e55` | 2025-10-11 13:54 | 1135 MB |
| `/.autodl/2d/65/86/2d6586332e56857bf97e0521e637ffd5` | 2025-10-11 13:51 | 1135 MB |
| `/.autodl/13/ba/b9/13bab9d0c0cf5ad8224668641177d77f` | 2025-10-11 13:32 | 1135 MB |
| `/.autodl/79/c6/a3/79c6a39f85f3a4f667ab1a51b2b76a27` | 2025-10-11 13:25 | 2386 MB |
| `/.autodl/17/a7/52/17a752fa559d4844325275b7237a6b36` | 2025-10-11 13:22 | 2386 MB |
| `/.autodl/34/41/32/344132111035a05e0c6f681e9555d0b4` | 2025-10-11 13:15 | 2386 MB |
| `/.autodl/94/4f/73/944f73fb51b1f603986da6e99562bb9b` | 2025-10-11 12:36 | 2386 MB |
| `/.autodl/13/9a/27/139a27bcb6354fc0358d10fb928cd85b` | 2025-10-11 12:27 | 2386 MB |
| `/.autodl/17/98/4c/17984cb5a1233ce873e0939f7ad030cf` | 2025-10-11 12:09 | 2395 MB |
| `/.autodl/1a/09/17/1a09171f5e4910100f0c6e2794a68818` | 2025-10-11 12:06 | 3417 MB |
| `/.autodl/3a/a4/aa/3aa4aa920dda0ab39823ea2e3e436406` | 2025-10-11 12:01 | 3417 MB |
| `/.autodl/38/79/b2/3879b2910f09313bb2d1521ef674bc0d` | 2025-10-11 11:55 | 3417 MB |
| `/.autodl/20/1d/38/201d387c1ce9a57c201080d4da7b9673` | 2025-10-11 05:00 | 6298 MB |
| `/.autodl/1d/ee/72/1dee724caa74b6bf54a30afe4b5b3864` | 2025-10-11 04:39 | 6298 MB |
| `/.autodl/60/b6/18/60b6180531ec631317a8101da326e7f2` | 2025-10-10 03:19 | 4772 MB |

### `models/diffusion_models/MiniMax-H3-experimental/minimax_h3_video_vae_int8_convrot.safetensors` ← 保留 `/.autodl/15/22/fc/1522fc49e094bb75c704ee519582252d` (更新于 2026-09-16 22:52)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Kijai/MiniMax-H3-experimental/minimax_h3_video_vae_int8_convrot.safetensors` | 2026-08-10 00:08 | 3024 MB |
| `/.autodl/Kijai/MiniMax-H3-experimental/minimax_h3_video_vae_int8_convrot.safetensors` | 2026-08-06 21:33 | 3024 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/diffusion_pytorch_model-00003-of-00014.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/transformer_ref/diffusion_pytorch_model-00003-of-00014.safetensors` (更新于 2026-08-05 08:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/transformer/diffusion_pytorch_model-00003-of-00014.safetensors` | 2026-08-05 08:43 | 4704 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/diffusion_pytorch_model-00004-of-00014.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/transformer_ref/diffusion_pytorch_model-00004-of-00014.safetensors` (更新于 2026-08-05 08:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/transformer/diffusion_pytorch_model-00004-of-00014.safetensors` | 2026-08-05 08:43 | 4355 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/diffusion_pytorch_model-00005-of-00014.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/transformer_ref/diffusion_pytorch_model-00005-of-00014.safetensors` (更新于 2026-08-05 08:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/transformer/diffusion_pytorch_model-00005-of-00014.safetensors` | 2026-08-05 08:43 | 4484 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/diffusion_pytorch_model-00007-of-00014.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/transformer_ref/diffusion_pytorch_model-00007-of-00014.safetensors` (更新于 2026-08-05 08:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/transformer/diffusion_pytorch_model-00007-of-00014.safetensors` | 2026-08-05 08:44 | 4355 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/diffusion_pytorch_model-00008-of-00014.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/transformer_ref/diffusion_pytorch_model-00008-of-00014.safetensors` (更新于 2026-08-05 08:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/transformer/diffusion_pytorch_model-00008-of-00014.safetensors` | 2026-08-05 08:44 | 4484 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/diffusion_pytorch_model-00009-of-00014.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/transformer_ref/diffusion_pytorch_model-00009-of-00014.safetensors` (更新于 2026-08-05 08:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/transformer/diffusion_pytorch_model-00009-of-00014.safetensors` | 2026-08-05 08:44 | 4704 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/diffusion_pytorch_model-00010-of-00014.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/transformer_ref/diffusion_pytorch_model-00010-of-00014.safetensors` (更新于 2026-08-05 08:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/transformer/diffusion_pytorch_model-00010-of-00014.safetensors` | 2026-08-05 08:44 | 4355 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/diffusion_pytorch_model-00013-of-00014.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/transformer_ref/diffusion_pytorch_model-00013-of-00014.safetensors` (更新于 2026-08-05 08:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/transformer/diffusion_pytorch_model-00013-of-00014.safetensors` | 2026-08-05 08:45 | 4355 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/diffusion_pytorch_model-00014-of-00014.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/transformer_ref/diffusion_pytorch_model-00014-of-00014.safetensors` (更新于 2026-08-05 08:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/transformer/diffusion_pytorch_model-00014-of-00014.safetensors` | 2026-08-05 08:45 | 4429 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00001-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00001-of-00013.safetensors` (更新于 2026-08-05 08:46)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00001-of-00013.safetensors` | 2026-08-05 08:45 | 4985 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00002-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00002-of-00013.safetensors` (更新于 2026-08-05 08:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00002-of-00013.safetensors` | 2026-08-05 08:45 | 4925 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00003-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00003-of-00013.safetensors` (更新于 2026-08-05 08:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00003-of-00013.safetensors` | 2026-08-05 08:45 | 4925 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00004-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00004-of-00013.safetensors` (更新于 2026-08-05 08:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00004-of-00013.safetensors` | 2026-08-05 08:45 | 4925 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00005-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00005-of-00013.safetensors` (更新于 2026-08-05 08:46)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00005-of-00013.safetensors` | 2026-08-05 08:45 | 4925 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00006-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00006-of-00013.safetensors` (更新于 2026-08-05 08:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00006-of-00013.safetensors` | 2026-08-05 08:45 | 4925 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00007-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00007-of-00013.safetensors` (更新于 2026-08-05 08:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00007-of-00013.safetensors` | 2026-08-05 08:45 | 4925 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00008-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00008-of-00013.safetensors` (更新于 2026-08-05 08:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00008-of-00013.safetensors` | 2026-08-05 08:45 | 4925 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00009-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00009-of-00013.safetensors` (更新于 2026-08-05 08:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00009-of-00013.safetensors` | 2026-08-05 08:45 | 4925 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00010-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00010-of-00013.safetensors` (更新于 2026-08-05 08:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00010-of-00013.safetensors` | 2026-08-05 08:45 | 4925 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00011-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00011-of-00013.safetensors` (更新于 2026-08-05 08:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00011-of-00013.safetensors` | 2026-08-05 08:45 | 4925 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00012-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00012-of-00013.safetensors` (更新于 2026-08-05 08:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00012-of-00013.safetensors` | 2026-08-05 08:46 | 4925 MB |

### `models/diffusion_models/MiniMax-MiniMax-H3/model-00013-of-00013.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/transformer/model-00013-of-00013.safetensors` (更新于 2026-08-05 08:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/Ref2VA/transformer/model-00013-of-00013.safetensors` | 2026-08-05 08:46 | 4045 MB |

### `models/diffusion_models/Qwen-Edit-2509-Multiple-angles.safetensors` ← 保留 `/.autodl/48/09/64/4809640c73283e56ecb3c4be79feb0b9` (更新于 2026-01-08 04:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/a6/39/63/a6396375578d15ba356db5c80a894242` | 2025-12-16 00:14 | 225 MB |

### `models/diffusion_models/Wan2.2-I2V-A14B-Diffusers-bf16/diffusion_pytorch_model-00001-of-00003.safetensors` ← 保留 `/.autodl/ai-toolkit/Wan2.2-I2V-A14B-Diffusers-bf16/transformer/diffusion_pytorch_model-00001-of-00003.safetensors` (更新于 2025-10-30 19:27)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/ai-toolkit/Wan2.2-I2V-A14B-Diffusers-bf16/transformer_2/diffusion_pytorch_model-00001-of-00003.safetensors` | 2025-10-30 19:27 | 9507 MB |

### `models/diffusion_models/Wan2.2-I2V-A14B-Diffusers-bf16/diffusion_pytorch_model-00002-of-00003.safetensors` ← 保留 `/.autodl/ai-toolkit/Wan2.2-I2V-A14B-Diffusers-bf16/transformer/diffusion_pytorch_model-00002-of-00003.safetensors` (更新于 2025-10-30 19:27)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/ai-toolkit/Wan2.2-I2V-A14B-Diffusers-bf16/transformer_2/diffusion_pytorch_model-00002-of-00003.safetensors` | 2025-10-30 19:27 | 9433 MB |

### `models/diffusion_models/Wan2.2-I2V-A14B-Diffusers-bf16/diffusion_pytorch_model-00003-of-00003.safetensors` ← 保留 `/.autodl/ai-toolkit/Wan2.2-I2V-A14B-Diffusers-bf16/transformer/diffusion_pytorch_model-00003-of-00003.safetensors` (更新于 2025-10-30 19:27)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/ai-toolkit/Wan2.2-I2V-A14B-Diffusers-bf16/transformer_2/diffusion_pytorch_model-00003-of-00003.safetensors` | 2025-10-30 19:27 | 8313 MB |

### `models/diffusion_models/Wan2.2-T2V-A14B-Diffusers-bf16/diffusion_pytorch_model-00001-of-00003.safetensors` ← 保留 `/.autodl/ai-toolkit/Wan2.2-T2V-A14B-Diffusers-bf16/transformer/diffusion_pytorch_model-00001-of-00003.safetensors` (更新于 2025-10-30 19:27)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/ai-toolkit/Wan2.2-T2V-A14B-Diffusers-bf16/transformer_2/diffusion_pytorch_model-00001-of-00003.safetensors` | 2025-10-30 19:27 | 9506 MB |

### `models/diffusion_models/Wan2.2-T2V-A14B-Diffusers-bf16/diffusion_pytorch_model-00002-of-00003.safetensors` ← 保留 `/.autodl/ai-toolkit/Wan2.2-T2V-A14B-Diffusers-bf16/transformer/diffusion_pytorch_model-00002-of-00003.safetensors` (更新于 2025-10-30 19:27)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/ai-toolkit/Wan2.2-T2V-A14B-Diffusers-bf16/transformer_2/diffusion_pytorch_model-00002-of-00003.safetensors` | 2025-10-30 19:27 | 9433 MB |

### `models/diffusion_models/Wan2.2-T2V-A14B-Diffusers-bf16/diffusion_pytorch_model-00003-of-00003.safetensors` ← 保留 `/.autodl/ai-toolkit/Wan2.2-T2V-A14B-Diffusers-bf16/transformer/diffusion_pytorch_model-00003-of-00003.safetensors` (更新于 2025-10-30 19:27)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/ai-toolkit/Wan2.2-T2V-A14B-Diffusers-bf16/transformer_2/diffusion_pytorch_model-00003-of-00003.safetensors` | 2025-10-30 19:27 | 8313 MB |

### `models/diffusion_models/boogu_image_edit_nvfp4.safetensors` ← 保留 `/.autodl/5a/88/76/5a8876e7173ea63f2a4b02b29f35faeb` (更新于 2026-07-13 21:27)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/f2/1f/d9/f21fd917e9b494ef78e01424cc77ebcf` | 2026-06-21 00:32 | 5564 MB |

### `models/diffusion_models/diffusion_pytorch_model.fp16.safetensors` ← 保留 `/.autodl/85/33/00/8533004a837038606d080cd7005b2352` (更新于 2025-11-16 22:54)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/13/ff/c1/13ffc1fa663a3e7ae2cb6795ad1cc132` | 2025-10-13 16:24 | 4920 MB |
| `/.autodl/9c/68/8d/9c688d78a75c1d3a0b33afffdd7e72f2` | 2025-10-03 23:38 | 4897 MB |

### `models/diffusion_models/diffusion_pytorch_model.safetensors` ← 保留 `/.autodl/da/8e/6e/da8e6e48ffe735a1cbb8ee7641e37473` (更新于 2026-04-21 23:00)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/70/19/1c/70191c082b06f50d1d7cbd481d97c885` | 2026-04-21 23:00 | 3322 MB |
| `/.autodl/43/93/72/4393721fc31ecd65257fee25436943ac` | 2026-04-17 15:52 | 7392 MB |
| `/.autodl/56/b1/6f/56b16f67087801edf88f1f4af94e038f` | 2026-01-14 10:03 | 774 MB |
| `/.autodl/NewBieAi-lab/NewBie-image-Exp0.1/transformer/diffusion_pytorch_model.safetensors` | 2025-12-10 19:44 | 6650 MB |
| `/.autodl/1c/ea/46/1cea46444d8a44258bc41e6907e71ceb` | 2025-11-16 22:55 | 557 MB |
| `/.autodl/5f/06/2e/5f062ef1d5300e110818e47bef68c410` | 2025-10-13 16:10 | 9840 MB |
| `/.autodl/f5/88/6c/f5886ca2f7df9c7a7a1278245603aa1d` | 2025-10-04 00:15 | 9794 MB |

### `models/diffusion_models/diffusion_pytorch_model_streaming_dmd.safetensors` ← 保留 `/.autodl/c1/8e/f6/c18ef6013fc1d62b5b50b80260772dae` (更新于 2026-09-17 15:30)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/22/20/00/222000a51c9a09fc97bef82a37153929` | 2025-12-16 01:04 | 5413 MB |

### `models/diffusion_models/model-00001-of-00004.safetensors` ← 保留 `/.autodl/80/b1/47/80b147de9a1afde4c4d4a8bf0f7cf965` (更新于 2026-01-14 10:40)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/49/51/fc/4951fcf003fba21e603c5e9806523d1c` | 2025-11-16 22:46 | 4699 MB |

### `models/diffusion_models/model-00002-of-00004.safetensors` ← 保留 `/.autodl/f9/a4/0e/f9a40e3293281327b2820a0e595aee98` (更新于 2026-01-14 10:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/2f/8e/f5/2f8ef50c84453d348a51dc1d35977573` | 2025-11-16 22:39 | 4704 MB |

### `models/diffusion_models/model-00003-of-00004.safetensors` ← 保留 `/.autodl/4e/8a/90/4e8a900ffe317320149b5370cd3b7db8` (更新于 2026-01-14 10:22)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/81/bd/b1/81bdb183aa32107366803dfe819538bf` | 2025-11-16 22:52 | 4768 MB |

### `models/diffusion_models/model-00004-of-00004.safetensors` ← 保留 `/.autodl/03/fd/42/03fd429e1e6b38a0d1b07322a93ce01a` (更新于 2026-01-14 10:35)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/5c/83/ae/5c83aeba5651a77787c9f699e64e56bc` | 2025-11-16 22:53 | 1243 MB |

### `models/loras/WanAnimate_relight_lora_fp16.safetensors` ← 保留 `/.autodl/03/30/74/0330745fc9fe8bd0ecba6a444b4f561d` (更新于 2025-12-06 20:11)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/e3/3c/40/e33c404972404ae19980347a388d27e3` | 2025-10-19 11:56 | 1370 MB |

### `models/loras/adapter_model.safetensors` ← 保留 `/.autodl/2e/af/b5/2eafb5b8114762ef61a6648982368ca3` (更新于 2026-09-07 15:33)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/6c/41/eb/6c41eb07399d6f588d26ebd625f43f28` | 2026-09-07 14:59 | 812 MB |
| `/.autodl/dc/47/bd/dc47bd930e1b5a4c2450a6ef2241fcf6` | 2026-09-07 14:24 | 318 MB |
| `/.autodl/8f/47/6f/8f476f44df7fa4333f1fa325c841f48a` | 2026-07-24 16:20 | 160 MB |

### `models/loras/ltx-2.3-22b-ic-lora-motion-track-control-ref0.5.safetensors` ← 保留 `/.autodl/b5/57/01/b5570110c8dc278c688021f9ae884f78` (更新于 2026-09-22 13:49)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/cb/0c/19/cb0c19a7c30529ff1d81cb13ad1f2fd0` | 2026-04-12 00:32 | 312 MB |
| `/.autodl/cb/0c/19/cb0c19a7c30529ff1d81cb13ad1f2fd0` | 2026-03-07 17:17 | 312 MB |

### `models/loras/models/ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors` ← 保留 `/.autodl/00/9e/0b/009e0bdca6f3896ae8c0c1c8bf7dab20` (更新于 2026-09-18 13:54)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/5a/81/3d/5a813df10e62f3fa453a2c17a56b2e2b` | 2026-04-13 21:05 | 624 MB |
| `/.autodl/5a/81/3d/5a813df10e62f3fa453a2c17a56b2e2b` | 2026-04-13 21:02 | 624 MB |
| `/.autodl/5a/81/3d/5a813df10e62f3fa453a2c17a56b2e2b` | 2026-03-07 17:18 | 624 MB |

### `models/loras/pytorch_lora_weights.safetensors` ← 保留 `/.autodl/34/59/93/34599376ce90d3304795406cfdc39ca9` (更新于 2025-10-10 01:36)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/b4/37/1e/b4371e17a6121898a2c75551c1a6149b` | 2025-10-10 00:54 | 200 MB |
| `/.autodl/fb/6f/a0/fb6fa0bf09bcfbe3d002ce0bfdfa7770` | 2025-10-10 00:52 | 128 MB |
| `/.autodl/20/3e/16/203e1659efe067716f3376bb02ab9a2e` | 2025-10-02 17:13 | 228 MB |

### `models/text_encoders/LongCat-Video/model-00005-of-00005.safetensors` ← 保留 `/.autodl/da/71/93/da7193e339ab64808f7e8700c68f4cc8` (更新于 2026-04-05 16:49)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/meituan-longcat/LongCat-Video/text_encoder/model-00005-of-00005.safetensors` | 2025-10-30 19:34 | 2752 MB |
| `/.autodl/meituan-longcat/LongCat-Video/text_encoder/model-00005-of-00005.safetensors` | 2025-10-30 19:32 | 2752 MB |
| `/.autodl/meituan-longcat/LongCat-Video/text_encoder/model-00005-of-00005.safetensors` | 2025-10-30 19:31 | 2752 MB |
| `/.autodl/meituan-longcat/LongCat-Video/text_encoder/model-00005-of-00005.safetensors` | 2025-10-30 19:28 | 2752 MB |

### `models/text_encoders/Qwen-Image-Edit-2511/model-00001-of-00004.safetensors` ← 保留 `/.autodl/54/2c/85/542c855aeb4ed9bd24fc478b2e04214a` (更新于 2026-05-31 03:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00001-of-00004.safetensors` | 2025-12-31 19:55 | 4738 MB |
| `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00001-of-00004.safetensors` | 2025-12-31 19:03 | 4738 MB |
| `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00001-of-00004.safetensors` | 2025-12-20 00:32 | 4738 MB |
| `/.autodl/tencent/HunyuanOCR/model-00001-of-00004.safetensors` | 2025-11-28 15:07 | 419 MB |
| `/.autodl/ZhipuAI/Glyph/model-00001-of-00004.safetensors` | 2025-11-07 14:55 | 5057 MB |
| `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00001-of-00004.safetensors` | 2025-10-30 19:37 | 4738 MB |
| `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00001-of-00004.safetensors` | 2025-10-30 19:37 | 4738 MB |
| `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00001-of-00004.safetensors` | 2025-09-29 20:25 | 4738 MB |

### `models/text_encoders/Qwen-Image-Edit-2511/model-00002-of-00004.safetensors` ← 保留 `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00002-of-00004.safetensors` (更新于 2025-12-31 19:55)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/tencent/HunyuanOCR/model-00002-of-00004.safetensors` | 2025-11-28 15:07 | 432 MB |
| `/.autodl/ZhipuAI/Glyph/model-00002-of-00004.safetensors` | 2025-11-07 14:55 | 5057 MB |

### `models/text_encoders/Qwen-Image-Edit-2511/model-00003-of-00004.safetensors` ← 保留 `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00003-of-00004.safetensors` (更新于 2025-12-31 19:55)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/tencent/HunyuanOCR/model-00003-of-00004.safetensors` | 2025-11-28 15:07 | 440 MB |
| `/.autodl/ZhipuAI/Glyph/model-00003-of-00004.safetensors` | 2025-11-07 14:55 | 5057 MB |

### `models/text_encoders/Qwen-Image-Edit-2511/model-00004-of-00004.safetensors` ← 保留 `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00004-of-00004.safetensors` (更新于 2025-12-31 19:55)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/tencent/HunyuanOCR/model-00004-of-00004.safetensors` | 2025-11-28 15:07 | 608 MB |
| `/.autodl/ZhipuAI/Glyph/model-00004-of-00004.safetensors` | 2025-11-07 14:54 | 4459 MB |

### `models/text_encoders/clip_g_hidream.safetensors` ← 保留 `/.autodl/2d/44/51/2d4451ce295a65394afa5a22aa164068` (更新于 2025-10-21 05:54)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/2a/05/4a/2a054ad15e7df7e1aa5f67a087e93a93` | 2025-10-21 05:43 | 0 MB |

### `models/text_encoders/clip_l_hidream.safetensors` ← 保留 `/.autodl/43/9c/5f/439c5f36e63ee61dcb2a577e9db5b89d` (更新于 2025-10-21 05:50)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/53/6f/8e/536f8ed54e11e3d9156698beb31b378a` | 2025-10-21 05:43 | 0 MB |

### `models/text_encoders/llama_3.1_8b_instruct_fp8_scaled.safetensors` ← 保留 `/.autodl/41/f8/f6/41f8f65351b5e66d3300f326ca6176c7` (更新于 2025-10-21 11:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/85/2e/82/852e82043de5dc53d1b887d3fee9ff95` | 2025-10-21 05:43 | 0 MB |

### `models/text_encoders/model.safetensors` ← 保留 `/.autodl/33/2f/5a/332f5a1d05041bf39f9e770f15cfe741` (更新于 2026-08-27 00:19)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/1f/4d/fd/1f4dfdc034dac8caf7016d058c147ded` | 2025-10-07 17:45 | 850 MB |
| `/.autodl/c8/75/a4/c875a4fb835aa184f8623508e9be7320` | 2025-10-03 13:55 | 1325 MB |

### `models/text_encoders/pytorch_model.bin` ← 保留 `/.autodl/Tencent-Hunyuan/Hunyuan3D-2.1/hunyuan3d-paintpbr-v2-1/text_encoder/pytorch_model.bin` (更新于 2025-11-11 09:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/google/t5-v1_1-xxl/pytorch_model.bin` | 2025-10-30 19:36 | 42478 MB |

### `models/text_encoders/stable-diffusion-xl-base-1.0/flax_model.msgpack` ← 保留 `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/text_encoder_2/flax_model.msgpack` (更新于 2025-11-10 17:29)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/text_encoder/flax_model.msgpack` | 2025-11-10 17:28 | 469 MB |

### `models/text_encoders/stable-diffusion-xl-base-1.0/model.safetensors` ← 保留 `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/text_encoder_2/model.safetensors` (更新于 2025-11-10 17:29)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/text_encoder/model.safetensors` | 2025-11-10 17:28 | 469 MB |

### `models/text_encoders/stable-diffusion-xl-base-1.0/openvino_model.bin` ← 保留 `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/text_encoder_2/openvino_model.bin` (更新于 2025-11-10 17:29)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/text_encoder/openvino_model.bin` | 2025-11-10 17:28 | 469 MB |

### `models/text_encoders/tokenizer.json` ← 保留 `/.autodl/7e/72/32/7e7232d3a0d2509306dd5ebd566a6609` (更新于 2026-08-26 22:01)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/ea/c1/43/eac14313ee1816d9e8ef962f7615fd93` | 2026-08-26 22:01 | 0 MB |

### `models/text_encoders/umt5_xxl_encoder/model-00001-of-00003.safetensors` ← 保留 `/.autodl/3e/6a/0b/3e6a0b03fe6bfc4e42461ea5ba211ad9` (更新于 2026-09-17 00:56)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/ai-toolkit/umt5_xxl_encoder/text_encoder/model-00001-of-00003.safetensors` | 2026-02-27 19:44 | 4707 MB |

### `models/text_encoders/umt5_xxl_encoder/model-00002-of-00003.safetensors` ← 保留 `/.autodl/59/1b/48/591b483eedb54d8840e95f58a36ed121` (更新于 2026-09-17 01:24)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/ai-toolkit/umt5_xxl_encoder/text_encoder/model-00002-of-00003.safetensors` | 2026-02-27 19:44 | 4752 MB |

### `models/text_encoders/umt5_xxl_encoder/model-00003-of-00003.safetensors` ← 保留 `/.autodl/72/a7/2a/72a72a7c979cdd0457832a6aa1845d3a` (更新于 2026-09-17 01:36)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/ai-toolkit/umt5_xxl_encoder/text_encoder/model-00003-of-00003.safetensors` | 2026-02-27 19:44 | 1376 MB |

### `models/vae/LTX-2/diffusion_pytorch_model.safetensors` ← 保留 `/.autodl/Lightricks/LTX-2/vae/diffusion_pytorch_model.safetensors` (更新于 2026-01-15 11:27)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Lightricks/LTX-2/audio_vae/diffusion_pytorch_model.safetensors` | 2026-01-15 11:26 | 101 MB |

### `models/vae/LTX2_video_vae_bf16.safetensors` ← 保留 `/.autodl/07/36/dc/0736dcf7daa618f5c99fb1b2b8c5e1ce` (更新于 2026-02-03 00:16)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/f8/d4/db/f8d4dbc9190731031b4d0b0ca0057edc` | 2026-01-11 02:59 | 2378 MB |

### `models/vae/MiniMax-MiniMax-H3/diffusion_pytorch_model.safetensors` ← 保留 `/.autodl/72/22/d9/7222d934878fcad0f6c14c02e0287f14` (更新于 2026-09-18 12:18)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/audio_vae/diffusion_pytorch_model.safetensors` | 2026-08-05 08:43 | 577 MB |

### `models/vae/MiniMax-MiniMax-H3/model.safetensors` ← 保留 `/.autodl/MiniMax/MiniMax-H3/FL2VA/video_vae/source/model.safetensors` (更新于 2026-08-05 08:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/MiniMax/MiniMax-H3/FL2VA/audio_vae/model.safetensors` | 2026-08-05 08:46 | 577 MB |
| `/.autodl/MiniMax/MiniMax-H3/FL2VA/audio_vae/model.safetensors` | 2026-08-05 08:46 | 577 MB |

### `models/vae/Wan2_1_VAE_bf16.safetensors` ← 保留 `/.autodl/58/e7/a4/58e7a4bf163459cd5ca0258be991e6b8` (更新于 2026-07-29 19:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/6f/69/56/6f6956f1a44321b1c322783a04b52dce` | 2025-10-20 23:47 | 242 MB |

### `models/vae/diffusion_pytorch_model.safetensors` ← 保留 `/.autodl/Tongyi-MAI/Z-Image/vae/diffusion_pytorch_model.safetensors` (更新于 2026-04-21 23:00)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/black-forest-labs/FLUX.2-klein-base-9B/vae/diffusion_pytorch_model.safetensors` | 2026-04-17 16:35 | 160 MB |
| `/.autodl/black-forest-labs/FLUX.2-klein-base-9B/vae/diffusion_pytorch_model.safetensors` | 2026-04-17 15:29 | 160 MB |
| `/.autodl/black-forest-labs/FLUX.2-klein-base-9B/vae/diffusion_pytorch_model.safetensors` | 2026-01-20 11:20 | 160 MB |
| `/.autodl/black-forest-labs/FLUX.2-klein-base-9B/vae/diffusion_pytorch_model.safetensors` | 2026-01-20 10:44 | 160 MB |

### `models/vae/stable-diffusion-xl-base-1.0/diffusion_pytorch_model.fp16.safetensors` ← 保留 `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae_1_0/diffusion_pytorch_model.fp16.safetensors` (更新于 2025-11-10 17:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae/diffusion_pytorch_model.fp16.safetensors` | 2025-11-10 17:31 | 159 MB |
| `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae/diffusion_pytorch_model.fp16.safetensors` | 2025-10-14 02:14 | 159 MB |

### `models/vae/stable-diffusion-xl-base-1.0/diffusion_pytorch_model.safetensors` ← 保留 `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae_1_0/diffusion_pytorch_model.safetensors` (更新于 2025-11-10 17:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae/diffusion_pytorch_model.safetensors` | 2025-11-10 17:31 | 319 MB |
| `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae/diffusion_pytorch_model.safetensors` | 2025-10-14 02:15 | 319 MB |

### `models/vae/stable-diffusion-xl-base-1.0/openvino_model.bin` ← 保留 `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae_decoder/openvino_model.bin` (更新于 2025-11-10 17:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae_encoder/openvino_model.bin` | 2025-11-10 17:31 | 130 MB |

### `models/vae/taeh3.safetensors` ← 保留 `/.autodl/5c/4d/2e/5c4d2e7b4f3ef8c6b440a92c6bdf3015` (更新于 2026-09-20 21:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/c9/ed/b9/c9edb90bdaad36a2aab16c29f325c140` | 2026-08-19 14:51 | 9 MB |
| `/.autodl/c9/ed/b9/c9edb90bdaad36a2aab16c29f325c140` | 2026-08-06 14:16 | 9 MB |

### `models/yolo/person_yolov8m-seg.pt` ← 保留 `/.autodl/85/8c/83/858c83996bd34f441c3cf3a73d11ab25` (更新于 2026-08-17 02:06)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/d4/fb/12/d4fb120f165659b2d37ae7153a7ca9c2` | 2026-02-28 14:03 | 52 MB |

### `models/yolo/yolo-world.pt` ← 保留 `/.autodl/23/1e/d1/231ed1a1a837314cc70e2bd6b3965043` (更新于 2026-05-01 21:56)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/ea/f4/0d/eaf40df12c14ca9020922983f6136dc1` | 2026-02-28 14:02 | 139 MB |
| `/.autodl/47/09/10/470910ac7d4cd64929926ed26a07a0ff` | 2026-02-28 14:02 | 24 MB |
| `/.autodl/05/82/c0/0582c062ecc4bfe2ffb47472e77a3a7d` | 2026-02-28 14:02 | 54 MB |
| `/.autodl/c4/d9/1c/c4d91cfe460fd38c2d5f4e2719fd004e` | 2026-02-28 14:02 | 89 MB |
| `/.autodl/0b/82/fe/0b82fe17fc4ea31cc33f6cb24ad89ca2` | 2026-02-28 14:02 | 25 MB |
| `/.autodl/92/83/76/9283768affe1238375edb31f88fcadb0` | 2026-02-28 14:02 | 55 MB |

## 源文件缺失(1)

- `/.autodl/mistralai/Ministral-3-8B-Reasoning-2512/tekken.json` (模型名称 `tekken.json`, 槽位 `LLM`)

## 文件名不安全跳过(10)

- `.mv` (槽位 `LLM`, 源 `/.autodl/5b/95/b3/5b95b3d07c1d67965dd2a30c0122bf12`)
- `.msc` (槽位 `LLM`, 源 `/.autodl/32/31/67/323167924d05cb5bdcbc5bec363e4f06`)
- `.mv` (槽位 `LLM`, 源 `/.autodl/ef/db/15/efdb154c9cd2a28bf768d2a2fe37ea6d`)
- `.msc` (槽位 `LLM`, 源 `/.autodl/b5/2e/7e/b52e7e89f7a7e66783029c2492772b77`)
- `.mv` (槽位 `LLM`, 源 `/.autodl/0b/a3/0a/0ba30a0a1b23015785d7d301027d49b3`)
- `.msc` (槽位 `LLM`, 源 `/.autodl/d7/61/ad/d761ad3bbf55c79bfadaed83a1cf5abc`)
- `.mv` (槽位 `LLM`, 源 `/.autodl/0b/a3/0a/0ba30a0a1b23015785d7d301027d49b3`)
- `.msc` (槽位 `LLM`, 源 `/.autodl/ed/33/2d/ed332d8e9c4a4fafd4c707c8306789b0`)
- `.mv` (槽位 `LLM`, 源 `/.autodl/2e/5a/2f/2e5a2fc012d4629652366b2f83f4d68c`)
- `.msc` (槽位 `LLM`, 源 `/.autodl/b0/9e/f0/b09ef09d91752b7823800174b71070af`)
