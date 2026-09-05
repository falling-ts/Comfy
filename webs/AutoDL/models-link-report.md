# AutoDL 云模型软链报告

数据源 `webs/AutoDL/models.md`(4646 行), 实际建链 **2988** 条。源 = 实例路径(文件本身), 目标 = `models/<本地目录>/<模型名称>`, 相对软链。

- 未识别(无本地槽位/无信号)跳过: 939 行
- 同名同源(重复上传)去重: 416 行
- 同名多源冲突按更新时间保留最新: 115 组, 落选 265 个(源文件仍在原路径可访问)
- 目标已存在(本机已有模型)跳过: 27
- 源文件缺失: 1

## 目标已存在(未覆盖, 本机保留原文件)

| 目标 | 云库来源 | 现有类型 |
|---|---|---|
| models/background_removal/birefnet.safetensors | `/.autodl/47/4c/0d/474c0d343806856b6d69fb4f57196684` | 链接 |
| models/checkpoints/stable_audio_3_medium.safetensors | `/.autodl/c6/f0/ed/c6f0ed356b05870466cdd0954562ef04` | 链接 |
| models/controlnet/Qwen-Image-InstantX-ControlNet-Inpainting.safetensors | `/.autodl/17/da/05/17da05512904d59ace58134e972a1692` | 链接 |
| models/diffusion_models/flux-2-klein-9b-fp8.safetensors | `/.autodl/7c/5f/15/7c5f15e30b24f3f24ac97adda21c1e8c` | 链接 |
| models/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors | `/.autodl/Comfy-Org/MiniMax-H3/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors` | 链接 |
| models/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors | `/.autodl/Comfy-Org/MiniMax-H3/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors` | 链接 |
| models/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors | `/.autodl/Comfy-Org/Qwen-Image_ComfyUI/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors` | 链接 |
| models/diffusion_models/qwen_image_edit_2511_bf16.safetensors | `/.autodl/a0/65/ec/a065ec8e87041a2c1b071fa2c98dbd49` | 链接 |
| models/diffusion_models/qwen_image_edit_2511_fp8mixed.safetensors | `/.autodl/31/8d/36/318d36574a2cd26aa3efa25cc86c8527` | 链接 |
| models/diffusion_models/qwen_image_fp8_e4m3fn.safetensors | `/.autodl/ce/64/be/ce64be77ee1d54260186b8d4da714765` | 链接 |
| models/facerestore_models/GFPGANv1.3.pth | `/.autodl/43/fc/9d/43fc9d9e6879c5982329d7efa587cd91` | 链接 |
| models/facerestore_models/GFPGANv1.4.pth | `/.autodl/94/d7/35/94d735072630ab734561130a47bc44f8` | 链接 |
| models/facerestore_models/GPEN-BFR-512.onnx | `/.autodl/d7/e3/fd/d7e3fd57554b1269176b3705fa9ae0cc` | 链接 |
| models/facerestore_models/codeformer-v0.1.0.pth | `/.autodl/30/f8/a1/30f8a1c9ae8600a5245b3d6bbe7ea475` | 链接 |
| models/loras/Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors | `/.autodl/a3/8b/6f/a38b6f56d2c3d2bf663d1b8343055691` | 链接 |
| models/loras/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors | `/.autodl/lightx2v/Qwen-Image-Edit-2511-Lightning/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors` | 链接 |
| models/loras/Qwen-Image-Lightning-4steps-V1.0.safetensors | `/.autodl/8f/ec/bb/8fecbbb1b60f30136a5e173c4c8c25cd` | 链接 |
| models/loras/minimax_h3_fl2v_turbo_4step_v1.0_768p_comfyui_bf16.safetensors | `/.autodl/e4/ff/e5/e4ffe5e088c48a42974f5cba44f3d95a` | 链接 |
| models/loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors | `/.autodl/34/96/d1/3496d1ffa7bedbbb2513f541b94dfc27` | 链接 |
| models/loras/minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors | `/.autodl/07/a6/21/07a621b3fa21b234876f867f230dc9fd` | 链接 |
| models/loras/qwen-image-edit-2511-multiple-angles-lora.safetensors | `/.autodl/19/30/f2/1930f2e0757b0491e58694c1e4fec4f3` | 链接 |
| models/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors | `/.autodl/Comfy-Org/MiniMax-H3/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | 链接 |
| models/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors | `/.autodl/b8/98/22/b89822a44279e6d83c06a5061d7b1ca6` | 链接 |
| models/vae/full_encoder_small_decoder.safetensors | `/.autodl/9e/a0/18/9ea01865431b258e6b8fdb3f2fc62f2b` | 链接 |
| models/vae/minimax_h3_audio_vae_fp32.safetensors | `/.autodl/Comfy-Org/MiniMax-H3/vae/minimax_h3_audio_vae_fp32.safetensors` | 链接 |
| models/vae/minimax_h3_video_vae_fp16.safetensors | `/.autodl/Comfy-Org/MiniMax-H3/vae/minimax_h3_video_vae_fp16.safetensors` | 链接 |
| models/vae/qwen_image_vae.safetensors | `/.autodl/circlestone-labs/Anima/split_files/vae/qwen_image_vae.safetensors` | 链接 |

## 同名多源冲突(保留最新, 落选来源)

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
| `/.autodl/7d/ca/df/7dcadf7a096598f98db2ce0df055fde0` | 2025-10-02 01:18 | 0 MB |
| `/.autodl/7d/ca/df/7dcadf7a096598f98db2ce0df055fde0` | 2025-10-02 01:00 | 0 MB |
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

### `models/LLM/merges.txt` ← 保留 `/.autodl/e7/88/82/e78882c2e224a75fa8180ec610bae243` (更新于 2025-10-16 13:23)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/72/da/cf/72dacf1de43bc354dc3c521e44ed0b24` | 2025-10-02 00:52 | 1 MB |
| `/.autodl/72/da/cf/72dacf1de43bc354dc3c521e44ed0b24` | 2025-09-25 23:00 | 1 MB |
| `/.autodl/72/da/cf/72dacf1de43bc354dc3c521e44ed0b24` | 2025-09-25 15:51 | 1 MB |

### `models/LLM/model-00001-of-00002.safetensors` ← 保留 `/.autodl/Qwen/wen3-VL-4B-Instruct/model-00001-of-00002.safetensors` (更新于 2026-09-02 00:52)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
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
| `/.autodl/Qwen/Qwen3-VL-8B-Instruct/model-00001-of-00004.safetensors` | 2025-10-16 11:17 | 4675 MB |
| `/.autodl/9a/8a/c0/9a8ac027b735bcae41d82f1d9fd1855b` | 2025-10-02 01:07 | 4731 MB |
| `/.autodl/e7/e8/39/e7e8399329373acfb7c6e81615f38676` | 2025-09-28 15:16 | 4659 MB |

### `models/LLM/model-00001-of-00005.safetensors` ← 保留 `/.autodl/86/44/c8/8644c8b51bc77b2e0c050ce5e7be30f7` (更新于 2026-01-21 22:23)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Qwen/Qwen3-8B/model-00001-of-00005.safetensors` | 2025-09-25 15:51 | 3811 MB |

### `models/LLM/model-00002-of-00002.safetensors` ← 保留 `/.autodl/Qwen/wen3-VL-4B-Instruct/model-00002-of-00002.safetensors` (更新于 2026-09-02 00:53)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
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
| `/.autodl/Qwen/Qwen3-VL-8B-Instruct/model-00002-of-00004.safetensors` | 2025-10-16 11:23 | 4688 MB |
| `/.autodl/3b/5b/d9/3b5bd9efada20946e6e33f7d6a4b2de9` | 2025-10-02 01:00 | 4732 MB |

### `models/LLM/model-00002-of-00005.safetensors` ← 保留 `/.autodl/12/20/b9/1220b9cc11ac55254d4165e285c7e2d9` (更新于 2026-01-21 22:18)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Qwen/Qwen3-8B/model-00002-of-00005.safetensors` | 2025-09-25 15:51 | 3808 MB |

### `models/LLM/model-00003-of-00004.safetensors` ← 保留 `/.autodl/d6/22/87/d62287ce7c41d7e4683f96ce13344136` (更新于 2026-05-31 03:29)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/13/e4/1b/13e41b8dd5963cc65b021a4c6fd7c269` | 2026-01-22 05:48 | 4336 MB |
| `/.autodl/15/5b/86/155b86ba11c2d37adc2312d1a29074f8` | 2025-12-31 09:32 | 4664 MB |
| `/.autodl/01/e9/e4/01e9e44667a46ca5527c40964f417600` | 2025-12-09 14:42 | 5057 MB |
| `/.autodl/6d/1f/47/6d1f473b5bdad9c1b41753a340145f0f` | 2025-11-25 11:34 | 4732 MB |
| `/.autodl/44/1f/27/441f27b7f22858b16ba7605154f1ba8d` | 2025-10-16 12:12 | 4768 MB |
| `/.autodl/Qwen/Qwen3-VL-8B-Instruct/model-00003-of-00004.safetensors` | 2025-10-16 11:30 | 4768 MB |
| `/.autodl/fa/10/0d/fa100d2b178e0afe7715de3529e10a20` | 2025-10-02 01:12 | 3890 MB |

### `models/LLM/model-00003-of-00005.safetensors` ← 保留 `/.autodl/4e/c4/05/4ec40524f0a3e91ec66dc5729d46d118` (更新于 2026-01-21 22:13)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Qwen/Qwen3-8B/model-00003-of-00005.safetensors` | 2025-09-25 15:51 | 3776 MB |

### `models/LLM/model-00004-of-00004.safetensors` ← 保留 `/.autodl/0a/af/cc/0aafcc743c0a30e72c977b918c9f9e5c` (更新于 2026-05-31 03:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/72/70/3f/72703ff71e99e2d43fa64a3274d938f0` | 2026-01-22 05:43 | 2152 MB |
| `/.autodl/17/04/6f/17046f72a720e51dab6cc812c781f3f2` | 2025-12-31 09:34 | 1200 MB |
| `/.autodl/3d/6c/33/3d6c3312ba81d7663e97ccba7b48d30a` | 2025-12-09 14:47 | 4442 MB |
| `/.autodl/fa/b6/0e/fab60e39907ce2f3d4e7ffa01b1685e9` | 2025-11-25 11:38 | 2961 MB |
| `/.autodl/13/15/15/131515c326389881bab75f96780aab7a` | 2025-10-16 11:53 | 2590 MB |
| `/.autodl/Qwen/Qwen3-VL-8B-Instruct/model-00004-of-00004.safetensors` | 2025-10-16 11:33 | 2590 MB |
| `/.autodl/f0/a1/23/f0a12337efe782016472f3d17f16588a` | 2025-10-02 01:44 | 1940 MB |

### `models/LLM/model-00004-of-00005.safetensors` ← 保留 `/.autodl/7b/57/97/7b5797821c1bbb60aa3dd9a65c88eedc` (更新于 2026-01-21 22:27)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Qwen/Qwen3-8B/model-00004-of-00005.safetensors` | 2025-09-25 15:51 | 3040 MB |

### `models/LLM/model-00005-of-00005.safetensors` ← 保留 `/.autodl/ab/4f/b1/ab4fb1ef087d7df0bc0df603e017d3cd` (更新于 2026-01-21 22:28)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Qwen/Qwen3-8B/model-00005-of-00005.safetensors` | 2025-09-25 15:51 | 1187 MB |

### `models/LLM/model.safetensors` ← 保留 `/.autodl/5f/6f/4b/5f6f4b3a3d0ec8a4a3f7f2cc1f0cd251` (更新于 2026-08-26 19:56)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/5f/2e/3d/5f2e3dafe599c6629af12160e31aa00a` | 2026-08-23 11:18 | 2592 MB |
| `/.autodl/IndexTeam/IndexTTS-2/qwen0.6bemo4-merge/model.safetensors` | 2026-04-22 10:04 | 1136 MB |
| `/.autodl/17/19/9c/17199ca96b5834ac77cb6c6b55d20388` | 2026-01-22 02:39 | 2641 MB |
| `/.autodl/5d/8d/8f/5d8d8f7c41f79160117160d1f13afe15` | 2026-01-22 02:30 | 5792 MB |
| `/.autodl/ca/0b/6c/ca0b6cc31c3b5c9d0236da365c1f7a6b` | 2026-01-22 02:22 | 2530 MB |
| `/.autodl/a6/a7/a7/a6a7a7ada992f203f802c812bb8ade78` | 2026-01-21 22:08 | 6580 MB |
| `/.autodl/6c/49/b5/6c49b59d80ad0591ae9cbb9c26a0d8fc` | 2025-12-31 09:17 | 3888 MB |
| `/.autodl/f4/c8/87/f4c887e55e159f96453e18a1d6ca984f` | 2025-11-13 03:33 | 3349 MB |
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
| `/.autodl/64/23/13/6423133b9cc1a2077b57822c30c211aa` | 2025-09-25 23:00 | 10 MB |
| `/.autodl/c9/4b/9a/c94b9adb41dddaa3fe95dd06cf5897a1` | 2025-09-25 19:59 | 6 MB |
| `/.autodl/64/23/13/6423133b9cc1a2077b57822c30c211aa` | 2025-09-25 15:51 | 10 MB |

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

### `models/TTS/bigvgan_generator.pt` ← 保留 `/.autodl/ac/8a/42/ac8a425c522c18f24154d23b23e5ab0e` (更新于 2026-08-25 17:58)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/11/b7/da/11b7daeeffa464064fb9e2b3638cc05d` | 2026-04-13 10:16 | 466 MB |

### `models/TTS/bigvgan_generator_3msteps.pt` ← 保留 `/.autodl/7c/3e/00/7c3e00bd06c9fc4bfa6aaee9e1fbb712` (更新于 2026-04-22 09:54)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/61/df/70/61df709276dbd3c5282da3984815fb09` | 2026-04-13 10:16 | 466 MB |

### `models/TTS/codec.pth` ← 保留 `/.autodl/d4/90/69/d49069422c5ff2b95b4762d220f932f1` (更新于 2026-08-22 01:44)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/drbaph/s2-pro-fp8/codec.pth` | 2026-04-12 01:23 | 1784 MB |
| `/.autodl/drbaph/s2-pro-fp8/codec.pth` | 2026-03-18 16:47 | 1784 MB |
| `/.autodl/drbaph/s2-pro-fp8/codec.pth` | 2026-03-18 16:09 | 1784 MB |
| `/.autodl/drbaph/s2-pro-fp8/codec.pth` | 2026-03-18 12:06 | 1784 MB |
| `/.autodl/drbaph/s2-pro-fp8/codec.pth` | 2026-03-16 11:24 | 1784 MB |

### `models/TTS/config.json` ← 保留 `/.autodl/1f/6d/d9/1f6dd9c4a4bc46f84fe4f763df02b0e1` (更新于 2025-10-16 20:59)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/9a/7b/45/9a7b457d1922d1da2b781e2c8f1479ea` | 2025-10-02 10:15 | 0 MB |

### `models/TTS/configuration.json` ← 保留 `/.autodl/82/dc/f8/82dcf8c6ca41273fbf35d167922a2434` (更新于 2025-11-01 00:15)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/7d/ca/df/7dcadf7a096598f98db2ce0df055fde0` | 2025-10-16 20:59 | 0 MB |
| `/.autodl/91/12/4d/91124d776bec0b391288489244121f61` | 2025-10-02 10:15 | 0 MB |

### `models/TTS/gpt.pth` ← 保留 `/.autodl/94/75/8c/94758ca56e99aed6000e19e376ab3033` (更新于 2026-08-22 01:42)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/IndexTeam/IndexTTS-2/gpt.pth` | 2026-04-22 09:58 | 3323 MB |
| `/.autodl/IndexTeam/IndexTTS-2/gpt.pth` | 2026-01-14 15:38 | 3323 MB |
| `/.autodl/IndexTeam/IndexTTS-2/gpt.pth` | 2026-01-05 19:09 | 3323 MB |

### `models/TTS/model.safetensors` ← 保留 `/.autodl/a4/c5/2e/a4c52ed581e0d8d3e9f26b18ec7fc29e` (更新于 2026-08-31 21:14)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/b5/ef/05/b5ef05a51449482a8268625ca5db2916` | 2026-08-31 21:06 | 8089 MB |
| `/.autodl/35/a6/59/35a659a565907fd173d15a63be42cae8` | 2026-08-25 18:21 | 168 MB |
| `/.autodl/53/f5/6e/53f56e9aa933eee52b9b8908343b46b8` | 2026-08-25 18:21 | 162 MB |
| `/.autodl/b5/04/d7/b504d7c039fe0f15d29c565887e88d03` | 2026-08-25 18:19 | 1260 MB |
| `/.autodl/77/82/c0/7782c0fcbd779b5527801ac6ea7f8632` | 2026-08-25 18:14 | 1348 MB |
| `/.autodl/b1/32/a6/b132a6d1387c0ef4e3e74cbce523bb60` | 2026-08-25 18:10 | 2847 MB |
| `/.autodl/5b/0a/e2/5b0ae2ff886124c262673a86dac9a169` | 2026-08-25 17:58 | 2214 MB |
| `/.autodl/35/a6/59/35a659a565907fd173d15a63be42cae8` | 2026-08-25 17:58 | 168 MB |
| `/.autodl/IndexTeam/IndexTTS-2/qwen0.6bemo4-merge/model.safetensors` | 2026-08-22 01:46 | 1136 MB |
| `/.autodl/5b/0a/e2/5b0ae2ff886124c262673a86dac9a169` | 2026-08-22 01:45 | 2214 MB |
| `/.autodl/IndexTeam/IndexTTS-2/qwen0.6bemo4-merge/model.safetensors` | 2026-08-13 10:34 | 1136 MB |
| `/.autodl/5b/0a/e2/5b0ae2ff886124c262673a86dac9a169` | 2026-08-13 10:33 | 2214 MB |
| `/.autodl/5b/0a/e2/5b0ae2ff886124c262673a86dac9a169` | 2026-04-22 10:09 | 2214 MB |
| `/.autodl/35/a6/59/35a659a565907fd173d15a63be42cae8` | 2026-04-22 10:07 | 168 MB |
| `/.autodl/drbaph/s2-pro-fp8/model.safetensors` | 2026-03-18 16:47 | 5877 MB |
| `/.autodl/baicai1145/s2-pro-w4a16/model.safetensors` | 2026-03-18 16:09 | 4041 MB |
| `/.autodl/5b/0a/e2/5b0ae2ff886124c262673a86dac9a169` | 2026-01-14 15:41 | 2214 MB |
| `/.autodl/35/a6/59/35a659a565907fd173d15a63be42cae8` | 2026-01-14 15:39 | 168 MB |
| `/.autodl/IndexTeam/IndexTTS-2/qwen0.6bemo4-merge/model.safetensors` | 2026-01-14 15:39 | 1136 MB |
| `/.autodl/35/a6/59/35a659a565907fd173d15a63be42cae8` | 2026-01-05 19:28 | 168 MB |
| `/.autodl/IndexTeam/IndexTTS-2/qwen0.6bemo4-merge/model.safetensors` | 2026-01-05 19:18 | 1136 MB |
| `/.autodl/3d/52/3b/3d523b643a0f329f47f3b18291ca1ac6` | 2025-12-30 20:39 | 360 MB |

### `models/TTS/pytorch_model.bin` ← 保留 `/.autodl/f3/0e/b1/f30eb1497d8644cb1fe44f4c0ca53223` (更新于 2025-12-30 20:40)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/aa/96/e0/aa96e0632f2ba76f3aebb9f5eb595e0b` | 2025-10-02 10:17 | 1244 MB |

### `models/TTS/s2-pro-fp8/model.safetensors` ← 保留 `/.autodl/drbaph/s2-pro-fp8/model.safetensors` (更新于 2026-03-18 17:01)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/baicai1145/s2-pro-w4a16/model.safetensors` | 2026-03-18 17:01 | 4041 MB |

### `models/TTS/s2mel.pth` ← 保留 `/.autodl/ca/92/3b/ca923bd52acdd113338bc4f76ded91c0` (更新于 2026-08-22 01:48)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/IndexTeam/IndexTTS-2/s2mel.pth` | 2026-04-22 10:02 | 1146 MB |
| `/.autodl/IndexTeam/IndexTTS-2/s2mel.pth` | 2026-01-14 15:38 | 1146 MB |
| `/.autodl/IndexTeam/IndexTTS-2/s2mel.pth` | 2026-01-05 19:09 | 1146 MB |

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

### `models/TTS/tokenizer.json` ← 保留 `/.autodl/drbaph/s2-pro-fp8/tokenizer.json` (更新于 2026-03-18 16:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/16/7a/a6/167aa6ce363be90f5531128fe3d653e2` | 2025-10-02 10:17 | 3 MB |

### `models/checkpoints/Hunyuan3D-2.1/model.fp16.ckpt` ← 保留 `/.autodl/Tencent-Hunyuan/Hunyuan3D-2.1/hunyuan3d-dit-v2-1/model.fp16.ckpt` (更新于 2025-11-10 19:54)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Tencent-Hunyuan/Hunyuan3D-2.1/hunyuan3d-vae-v2-1/model.fp16.ckpt` | 2025-11-10 19:54 | 625 MB |

### `models/checkpoints/taesdxl_decoder.pth` ← 保留 `/.autodl/3f/21/dd/3f21ddf6ccf51c4182236dac7f9f98c0` (更新于 2025-10-02 16:47)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/cc/63/0e/cc630e4dacf767bcd18c320f9dc375fe` | 2025-09-29 22:08 | 4 MB |

### `models/clip_vision/model.safetensors` ← 保留 `/.autodl/Tencent-Hunyuan/Hunyuan3D-2.1/hunyuan3d-paintpbr-v2-1/image_encoder/model.safetensors` (更新于 2025-11-11 09:45)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Wan-AI/Wan2.1-I2V-14B-720P-Diffusers/image_encoder/model.safetensors` | 2025-10-30 19:32 | 1205 MB |

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
| `/.autodl/ef/2f/9d/ef2f9d0a1e0cb053e580e6e9bdc87d90` | 2025-10-10 16:13 | 2386 MB |
| `/.autodl/60/b6/18/60b6180531ec631317a8101da326e7f2` | 2025-10-10 03:19 | 4772 MB |

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
| `/.autodl/1c/ea/46/1cea46444d8a44258bc41e6907e71ceb` | 2025-11-16 22:55 | 557 MB |
| `/.autodl/67/6a/6d/676a6d9ee21a28e661358e830b46bb20` | 2025-10-30 19:41 | 661 MB |
| `/.autodl/5f/06/2e/5f062ef1d5300e110818e47bef68c410` | 2025-10-13 16:10 | 9840 MB |
| `/.autodl/f5/88/6c/f5886ca2f7df9c7a7a1278245603aa1d` | 2025-10-04 00:15 | 9794 MB |

### `models/diffusion_models/flux1-dev-fp8.safetensors` ← 保留 `/.autodl/23/73/8c/23738c26b548113ea2d392abd91d3fd0` (更新于 2025-10-28 12:03)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/39/7c/06/397c06d6752a47005c6c7ea594551be1` | 2025-10-12 02:25 | 11350 MB |

### `models/diffusion_models/ltx-2-19b-distilled.safetensors` ← 保留 `/.autodl/a2/d6/65/a2d665f86b438bdd7b463b33ed859507` (更新于 2026-01-15 18:55)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Lightricks/LTX-2/ltx-2-19b-distilled.safetensors` | 2026-01-08 02:29 | 41326 MB |

### `models/loras/WanAnimate_relight_lora_fp16.safetensors` ← 保留 `/.autodl/03/30/74/0330745fc9fe8bd0ecba6a444b4f561d` (更新于 2025-12-06 20:11)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/e3/3c/40/e33c404972404ae19980347a388d27e3` | 2025-10-19 11:56 | 1370 MB |

### `models/loras/pytorch_lora_weights.safetensors` ← 保留 `/.autodl/34/59/93/34599376ce90d3304795406cfdc39ca9` (更新于 2025-10-10 01:36)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/b4/37/1e/b4371e17a6121898a2c75551c1a6149b` | 2025-10-10 00:54 | 200 MB |
| `/.autodl/fb/6f/a0/fb6fa0bf09bcfbe3d002ce0bfdfa7770` | 2025-10-10 00:52 | 128 MB |
| `/.autodl/20/3e/16/203e1659efe067716f3376bb02ab9a2e` | 2025-10-02 17:13 | 228 MB |

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

### `models/text_encoders/model-00001-of-00004.safetensors` ← 保留 `/.autodl/black-forest-labs/FLUX.2-klein-base-9B/text_encoder/model-00001-of-00004.safetensors` (更新于 2026-04-17 16:28)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00001-of-00004.safetensors` | 2025-12-20 00:32 | 4738 MB |
| `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00001-of-00004.safetensors` | 2025-09-29 20:25 | 4738 MB |

### `models/text_encoders/model-00002-of-00004.safetensors` ← 保留 `/.autodl/black-forest-labs/FLUX.2-klein-base-9B/text_encoder/model-00002-of-00004.safetensors` (更新于 2026-04-17 16:20)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00002-of-00004.safetensors` | 2025-12-20 00:32 | 4760 MB |

### `models/text_encoders/model-00003-of-00004.safetensors` ← 保留 `/.autodl/black-forest-labs/FLUX.2-klein-base-9B/text_encoder/model-00003-of-00004.safetensors` (更新于 2026-04-17 16:20)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00003-of-00004.safetensors` | 2025-12-20 00:33 | 4704 MB |

### `models/text_encoders/model-00004-of-00004.safetensors` ← 保留 `/.autodl/black-forest-labs/FLUX.2-klein-base-9B/text_encoder/model-00004-of-00004.safetensors` (更新于 2026-04-17 16:20)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00004-of-00004.safetensors` | 2025-12-20 00:33 | 1613 MB |
| `/.autodl/Qwen/Qwen-Image-Edit-2511/text_encoder/model-00004-of-00004.safetensors` | 2025-09-29 20:12 | 1613 MB |

### `models/text_encoders/model.safetensors` ← 保留 `/.autodl/33/2f/5a/332f5a1d05041bf39f9e770f15cfe741` (更新于 2026-08-27 00:19)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/5b/0a/e2/5b0ae2ff886124c262673a86dac9a169` | 2026-01-05 19:41 | 2214 MB |
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

### `models/vae/LTX-2/diffusion_pytorch_model.safetensors` ← 保留 `/.autodl/Lightricks/LTX-2/vae/diffusion_pytorch_model.safetensors` (更新于 2026-01-15 11:27)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/Lightricks/LTX-2/audio_vae/diffusion_pytorch_model.safetensors` | 2026-01-15 11:26 | 101 MB |

### `models/vae/LTX2_video_vae_bf16.safetensors` ← 保留 `/.autodl/07/36/dc/0736dcf7daa618f5c99fb1b2b8c5e1ce` (更新于 2026-02-03 00:16)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/f8/d4/db/f8d4dbc9190731031b4d0b0ca0057edc` | 2026-01-11 02:59 | 2378 MB |

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
| `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae/diffusion_pytorch_model.safetensors` | 2025-10-14 02:15 | 319 MB |

### `models/vae/stable-diffusion-xl-base-1.0/diffusion_pytorch_model.fp16.safetensors` ← 保留 `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae_1_0/diffusion_pytorch_model.fp16.safetensors` (更新于 2025-11-10 17:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae/diffusion_pytorch_model.fp16.safetensors` | 2025-11-10 17:31 | 159 MB |

### `models/vae/stable-diffusion-xl-base-1.0/diffusion_pytorch_model.safetensors` ← 保留 `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae_1_0/diffusion_pytorch_model.safetensors` (更新于 2025-11-10 17:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae/diffusion_pytorch_model.safetensors` | 2025-11-10 17:31 | 319 MB |

### `models/vae/stable-diffusion-xl-base-1.0/openvino_model.bin` ← 保留 `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae_decoder/openvino_model.bin` (更新于 2025-11-10 17:31)

| 落选来源 | 更新时间 | 大小 |
|---|---|---|
| `/.autodl/stabilityai/stable-diffusion-xl-base-1.0/vae_encoder/openvino_model.bin` | 2025-11-10 17:31 | 130 MB |

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


## 源文件缺失

- `/.autodl/mistralai/Ministral-3-8B-Reasoning-2512/tekken.json` (模型名称 `tekken.json`)
