# Your machine

**This file is yours, not the kit's.** It holds the facts about THIS install: where ComfyUI lives, what GPUs
are in the box, how to start the server when it is down. The installer creates it once and then never touches
it again, so a `git pull` plus a reinstall cannot wipe what the bootstrap learned. Nothing here ships back to
the repo.

> 本文件值采集自运行中的 ComfyUI API(`/system_stats`、`/object_info`,2026-08-11),与本地 CLAUDE.md 交叉核对。若服务重启后数值变化,以实时查询为准。

- **ComfyUI**: source install(conda 环境),core path **`D:\Comfy\ComfyUI`**,API at **`http://127.0.0.1:8188`**(运行中,ComfyUI 0.31.0 / 前端 1.48.7)。Check: `GET /system_stats` -> 200。
- **GPUs**: 1x `cuda:0` NVIDIA GeForce RTX 4060,VRAM **8.0 GB**(运行中 free 约 6.9 GB)。
- **Models installed**(2026-08-11 实测 `/object_info`):
  - UNETLoader: `qwen_image_edit_2511_bf16`、`qwen_image_edit_2511_fp8mixed`、`qwen_image_2512_fp8_e4m3fn`、`flux-2-klein-9b-fp8`、`minimax_h3_fl2va_pruned_int8_convrot`、`minimax_h3_ref2va_pruned_int8_convrot`
  - CheckpointLoaderSimple: `stable_audio_3_medium.safetensors`
  - CLIPLoader: `qwen_2.5_vl_7b_fp8_scaled`(Qwen-Image-Edit 用)、`qwen3vl_32b_minimax_h3_nvfp4_awq`(H3 视频)、`qwen_3_8b_fp8mixed`(Klein)、`qwen3.5_2b_bf16`、`t5gemma_b_b_ul2`
  - VAELoader: `qwen_image_vae`、`full_encoder_small_decoder`、`minimax_h3_audio_vae_fp32`、`minimax_h3_video_vae_fp16`
  - LoraLoaderModelOnly: `Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16`、`Qwen-Image-2512-Lightning-4steps-V1.0-fp32`、`[Qwen-Edit]3DChineseStyle_25`、`Kook_Qwen_2512_真实幻想`、`minimax_h3_turbo_4step`、`qwen-image-edit-2511-multiple-angles-lora`
- **Shared models dir / extra_model_paths**: 无 extra_model_paths.yaml;模型实际存放 **`D:\Comfy\models`**(`ComfyUI\models` 是其相对软链接),input/output 同样软链到 `D:\Comfy\media`。
- **GUI workflows folder**(bridge 回前端): `D:\Comfy\ComfyUI\user\default\workflows\`(该路径是软链接,实际存储 `D:\Comfy\workflows`)。可写。
- **Template library**: **`D:\Comfy\templates`**(官方模板缓存按类分目录 + 根目录 17 个个人归档工作流)+ `D:\Comfy\ComfyUI\blueprints`(89 个官方蓝图)。⚠️ 本机**没有** kit 默认的 `~/comfyui-agent-kit-data/workflow_templates` 与 `_quick_index.json`;`TASKS.md` 若按该路径找模板索引会落空,直接用上面本地目录。
- **Launch command**(服务未运行、:8188 关闭时): `cd /d D:\Comfy\ComfyUI && C:\Users\zghyu\Miniconda3\envs\ComfyUI\python.exe main.py --enable-manager --disable-pinned-memory --fast-disk`(conda 环境名 `ComfyUI`,Python 3.13.14)。若 :8188 已被前端占用,勿重复启动。
- **Known local quirks**(本机与 docs 不符之处,省时的关键):
  - **知识独立安装,无 MCP 驱动层**:未安装 `comfyui-mcp`(npm),SKILL.md 里 `health_check / get_node_info / list_installed_nodes` 等 MCP 工具**不存在**。与 API 通信一律用本目录 `comfy_client.py`(stdlib)直连 :8188,或直接 HTTP。
  - **8GB 小显存**:图像/视频优先 fp8/int8 量化 + Lightning 4 步 LoRA + SageAttention;主文生图链路默认 `--fast-disk --disable-pinned-memory`。
  - **sibling skills 未装**:SKILL.md 提及的 `minimax-h3` / `krea` / `seedance` 不在本机;H3 提示词由本机已有 `h3-prompt-writing` skill 承担,遇到 krea/seedance 模型直接说明未安装。
  - **Qwen-Image-Edit 条件节点**:`TextEncodeQwenImageEditPlus`(三参考图 image1/2/3,提示词内用 `图N` / `Picture N` 编号引用,VAE 参考 latent 写入 `reference_latents`);单图用 `TextEncodeQwenImageEdit`。自研 `GJJ_TextEncodeQwenImageEditPlus` 用 `imageN:` 标签。规范详见 `docs\Qwen-Image-Edit-三参考图提示词规范与可用Skills-2026-08-11.md`。
  - **自定义插件聚合**:`D:\Comfy\custom_nodes`(目录级软链接加载,FallingTS / GJJ_Nodes / KJNodes / LayerStyle / Impact-Pack / Easy-Use / SeedVR2 / SUPIR / UltimateSDUpscale / MiniMaxH3 套件),改节点代码需重启 ComfyUI 生效。
