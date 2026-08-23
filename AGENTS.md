# ComfyUI 本地工作区

ComfyUI 及自定义节点的本地开发工作区。下文路径均相对项目根目录,不绑定特定操作系统或 shell;文中命令示例按当前本机环境给出,部署到其它平台时按实际环境替换路径分隔符/可执行文件位置即可。

## 目录结构(展开至第二级)

| 路径 | 说明 |
|------|------|
| `ComfyUI` | ComfyUI 主程序(git submodule,`master` 分支):源码/入口在本目录;`models`/`input`/`output`/`user\default\workflows`/`custom_nodes` 均为相对软链接(见「软链接映射」);`blueprints\` 内置 90 个蓝图;其余结构遵循上游官方布局,不再逐一展开 |
| **`custom_nodes`** | **插件聚合目录**:43 个插件子模块 + `H3ReferenceSuite` 链接集中于此,`ComfyUI\custom_nodes` 为目录级相对软链接指向它(§B)。按功能归类: |
| └ 自有插件 | `ComfyUI-FallingTS`:通用工具节点集(Continue/Selector/Table/Switch/PreviewVideo 5 节点 + 前端增强,已开源) |
| └ H3 生态(6 插件 + 链接) | `ComfyUI-Spectrum-MiniMax-H3`(加速)、`ComfyUI-SolAttn_triton`(注意力加速)、`ComfyUI-ReservedVRAM`(显存预留)、`ComfyUI-Qwen3-TTS`(H3 语音)、`h3-latent-upscaler`(latent 放大)、`ComfyUI-OrbitSheets`(场景/角色参考板:锚点图 + H3 多视角运镜 + 视觉选帧拼网格图,2026-08-17 装)、`H3ReferenceSuite`(软链接,见 `h3`) |
| └ 放大/修复/局部重绘 | `ComfyUI-SeedVR2_VideoUpscaler`(视频高清修复)、`ComfyUI-SUPIR`(超分放大)、`ComfyUI_UltimateSDUpscale`(分块重绘)、`ComfyUI-Impact-Pack`(Detailer 局部精修)、`ComfyUI_LayerStyle`(图层/遮罩)、`ComfyUI-Inpaint-CropAndStitch`(裁剪贴回) |
| └ 视频 | `ComfyUI-VideoHelperSuite`、`ComfyUI-WanVideoWrapper`、`ComfyUI-Frame-Interpolation`(补帧)、`ComfyUI-qwenmultiangle`(Qwen 多镜头) |
| └ 图像/编辑/生成 | `ComfyUI-Easy-Use`、`ComfyUI_IPAdapter_plus`、`ComfyUI-ReActor`(换脸)、`ComfyUI-RMBG`、`ComfyUI-segment-anything-2`、`comfyui_controlnet_aux`、`ComfyUI-IC-Light`、`ComfyUI-DepthAnythingV2`、`Comfyui-QwenEditUtils`、`comfyui-mixlab-nodes`、`ComfyUI-Florence2`、`ComfyUI-post-processing-nodes`(后期处理) |
| └ 工具/其它 | `ComfyUI-GGUF`(GGUF 量化加载)、`ComfyUI-KJNodes`(KJ 工具包)、`rgthree-comfy`、`ComfyUI-Custom-Scripts`、`ComfyUI-Detail-Daemon`、`ComfyUI-Crystools`、`ComfyUI-MultiGPU`、`ComfyUI-LogicUtils`、`ComfyUI-Inspire-Pack`、`cg-use-everywhere`、`audio-separation-nodes-comfyui`、`ComfyUI_essentials`、`ComfyUI_LinkFX`(连线动画)、`ComfyUI-AnimatedLinks`(连线动画) |
| `docs` | 本地参考文档:20 个分类 md + 5 个子目录(4 个 git submodule + `Qwen-Image-Edit-Skills` 本地目录) | 
| └ `ComfyUI-Docs` | ComfyUI 官方文档仓库本地克隆(Comfy-Org/docs,子模块) |
| └ `Obsidian-Dev-Docs` | Obsidian 官方开发者文档(插件开发参考,子模块) |
| └ `Obsidian-API` | Obsidian API 类型定义(`obsidian.d.ts`/`publish.d.ts`,子模块) |
| └ `codex` | Codex CLI 源码/文档子模块(上游 OpenCode 体系,子模块) |
| └ `Qwen-Image-Edit-Skills` | Qwen-Image-Edit 官方 Skills 参考(本地目录,非子模块) |
| └ 分类 md | 启动参数参考、KSampler 采样器指南、SageAttention 参数配置、Qwen 国漫 LoRA 清单、节点输入类型总表、插件注册表、模型调研报告、H3 提示词格式调研、FallingTS 分段执行机制等 |
| `h3` | **MiniMax H3 生态聚合目录**(2026-08-10 建):`MiniMax-H3`(官方模型仓库,自带 9 个官方 Skills)+ `minimax-h3-guide`(参考加载套件,其 `H3ReferenceSuite` 由根 `custom_nodes` 子链接指向) |
| **`workflows`** | **用户工作流实际存储处**(前端保存即在此,可经 `GET /userdata?dir=workflows` 读取),共 24 个,按编号-用途分组: |
| └ `1xxx` 万物 | `1000-万物建模`(主线主流程)/ `1001-灰度遮罩` / `1010-万物变化` |
| └ `2xxx` 场景镜头 | `2000-场景首帧` / `2010-场景拉镜` / `2020-场景推镜` / `2030-场景旋镜` |
| └ `3xxx` 场景生成 | `3000-文生场景`(H3 T2VA,仅画面)/ `3010-图生场景`(I2V)/ `3020-参考场景`(R2V 多图多视频参考)/ `3030-OrbitSheets场景`(Location Sheet 参考板:锚点图+H3 多视角选帧拼板)/ `3040-Skythread场景`(R2V 三参考法:角色/道具/空场景) |
| └ `4xxx` 视频生成 | `4000-文生视频` / `4010-图生视频` / `4020-首尾视频` / `4030-参考视频` |
| └ `5xxx` 拆解 | `5000-视频拆帧` / `5010-视频拆音` |
| └ `6xxx` 音频生成 | `6000-背景音乐` / `6010-环境音效` / `6020-效果音效` / `6030-文生人声` / `6040-参考人声` |
| └ `7xxx` 截取 | `7000-截取声音` |
| `models` | 模型实际存放处(`ComfyUI\models` 软链接指向);38 个标准槽位子目录,每个目录带 `.gitignore`(内容 `*`+`!.gitignore`)忽略模型文件、仅占位入库。已就绪模型见「模型与蓝图」 |
| └ 核心生成 | `diffusion_models` / `text_encoders` / `vae` / `loras` / `checkpoints` / `upscale_models` / `background_removal`(已就绪) |
| └ 语音 | `TTS`(Qwen3-TTS 五变体 + SenseVoice)/ `ASR` / `speaker_models` / `audio_encoders` |
| └ 标准空槽位 | 其余 25 个标准槽位目录(如 `controlnet` / `clip` / `clip_vision` / `unet` / `embeddings` / `detection` / `SEEDVR2` / `ultralytics` 等,多数尚未放置模型) |
| `media` | 输入/输出文件(`ComfyUI\input`、`output` 软链接到此):`3d\` / `qwen3tts\` / `clipspace\` 及历史生成图;⚠️ 真实数据,严禁删除/批量清理 |
| `templates` | ComfyUI 官方模板库本地缓存:10 个分类子目录(`图像`/`视频`/`音频`/`3D模型`/`LLM`/`工具`/`快速开始`/`自定义节点`/`节点基础`/`使用案例`)+ `workflow-templates-list.md` 索引(2026-08-09 曾归档的个人工作流已迁回 `workflows\`) |
| `webs` | 三方网站调研聚合目录(已入库跟踪):三个调研源 |
| └ `RunningHub` | RunningHub 调研:`RunningHub-API读取指南.md` + `API.md` + `workflows-list.md` + `workflows\`(1360 个收集工作流,按 图像/视频/音频/数字人/室内外设计/风格化/插件 等子目录分类) |
| └ `Bilibili` | B 站教程调研:`B站教程调研.md` + `工作流大全\`(474 个配套工作流) |
| └ `AutoDL` | 云端 GPU 调研:`AutoDL-GPU选型-2026-08-06.md` + `api.md`(云模型库接口)+ `models.md`(4015 条模型清单) |
| `stories` | Obsidian 故事写作工作区(自带 `.obsidian\` 配置):`template\`(新建故事模板)+ 用户自定义故事库目录(库名随写作项目而定,以盘上实际为准) |
| `scripts` | 临时/可复用工具脚本(被 `scripts\.gitignore` 忽略,仅存本地不入库):工作流连线校验/修复/对比(`check-workflow-*`/`fix-*`/`diff-*`/`dump-*`)、布局校验、模型使用分析、模板/模型清单更新、H3/SeedVR2 调试等 |
| `logs` | ComfyUI 运行日志(`comfyui*.log`/`comfyui-console*.log`,已 gitignore) |
| `backups` | **工作流/重要文件的修改前备份**(2026-08-04 起):`backup-<文件名>-<YYYYMMDD>-<说明>.*` 命名;含 `backup-20260805-路径清理\`(官方/分类文档归档)、`sageattention\`(本地 wheel)、环境迁移快照(pip-freeze/conda export)等 |
| `.claude` | SymbolicLink → `.agents`(Claude Code 兼容垫片,技能聚合目录,见「软链接映射 §C」) |
| `README.md` / `LICENSE` | 项目说明与许可 |
| `.gitmodules` | 子模块登记(git submodule) |
| `comfy-server.sh` | **统一**后台服务式启动脚本(跨平台: Linux + Windows Git Bash;杀 8188 旧进程 → 静默后台启动 → 等待端口就绪,日志默认写系统临时目录/`/tmp` 的 `comfy-server-8188.log`;Windows 等价 `python main.py --enable-manager --disable-pinned-memory --fast-disk`,Linux 用 conda 环境 comfy + `--reserve-vram 22`;覆盖 `PORT`/`WAIT`/`PY_BIN`/`LOG`/`RESERVE_VRAM`) |

## 软链接映射(重要,共 7 个,全部为相对路径 SymbolicLink;2026-08-07 建,08-10 插件收敛为目录级链接,08-13 加 Claude Code 兼容链接)

全部为 **相对路径**符号链接,**项目根目录整体移动后不失效**(不依赖具体文件系统/平台)。

### A. 基础链接(4 个)

| ComfyUI 内路径 | 类型 | 相对目标 | 实际指向 |
|------|------|------|------|
| `ComfyUI\input` | SymbolicLink | `..\media` | `media` |
| `ComfyUI\output` | SymbolicLink | `..\media` | `media` |
| `ComfyUI\models` | SymbolicLink | `..\models` | `models`(模型实际存放处) |
| `ComfyUI\user\default\workflows` | SymbolicLink | `..\..\..\workflows` | `workflows`(用户工作流实际存储处) |

### B. custom_nodes 目录级链接 + H3ReferenceSuite 子链接(2 个)

| ComfyUI 内路径 | 类型 | 相对目标 | 实际指向 |
|------|------|------|------|
| `ComfyUI\custom_nodes` | SymbolicLink(目录级) | `..\custom_nodes` | 根 `custom_nodes`(插件聚合目录,43 插件 + H3ReferenceSuite 链接) |
| `custom_nodes\H3ReferenceSuite` | SymbolicLink(子链接) | `..\h3\minimax-h3-guide\custom_nodes\H3ReferenceSuite` | `h3\minimax-h3-guide\custom_nodes\H3ReferenceSuite` |

- 根 `custom_nodes` 由**根仓库**跟踪:43 个插件以 gitlink 形式登记(全仓共 50 个子模块:`ComfyUI` 1 + 插件 43 + `docs\` 4 + `h3\` 2),`H3ReferenceSuite` 为符号链接;本地文件 `example_node.py.example`、`websocket_image_save.py` 被根 `.gitignore` 排除(保留磁盘副本供加载)。`ComfyUI\custom_nodes` 是目录级符号链接,其目标内容不受 ComfyUI 子模块 git 影响
- `ComfyUI\temp\`(真实目录,非链接):运行中生成的临时文件/预览图(如 `ComfyUI_temp_*.png`),可随时清理
- ⚠️ **`ComfyUI\input\`(用户上传)与 `output\`(生成结果)是真实数据:严禁删除、移动或批量清理**;只有 `temp\` 可清理

### C. 根目录 Claude Code 兼容链接(1 个)

| 根内路径 | 类型 | 相对目标 | 实际指向 |
|------|------|------|------|
| `.claude` | SymbolicLink(目录级) | `.agents` | 根 `.agents`(技能聚合目录,Claude Code 兼容垫片,2026-08-13 建) |

## 版本与运行

- **Python 虚拟环境:项目内 `.venv`**(2026-08-16 由 conda 环境迁移而来,官方 `python -m venv` 基于系统 Python 3.13.13 创建;原 conda 专用环境已删除)。启动一律用 `.venv\Scripts\python.exe`(类 Unix 为 `.venv\bin/python`),不要用系统级 Python 或任何 conda 环境运行主程序
- **运行环境 `.venv`:Python 3.13.13 / torch 2.13.0+cu130(CUDA 13.0,RTX 4060 8GB VRAM)**,启动脚本与本文档均用它(`.venv\Scripts\python.exe`,类 Unix 为 `.venv\bin/python`);依赖安装顺序:torch(cu130 index)→ `ComfyUI\requirements.txt` → 插件 requirements → 加速依赖,迁移后与旧 conda 环境包版本对齐(见 `backups\pip-freeze-ComfyUI-20260816-020146.txt` 与 `pip-freeze-venv-final.txt` 对比)
- 共享关键版本:comfyui-frontend-package **1.48.7**、comfyui-manager **4.2.2**、comfyui-workflow-templates **0.11.34**、sageattention **2.2.0**(cu130,本地 wheel `backups\sageattention\`)、triton-windows **3.7.1.post27**、comfy-kitchen **0.2.28**、comfy-aimdo 0.4.13、transformers 4.57.3、diffusers 0.39.0、numpy 2.4.6、onnxruntime-gpu 1.28.0、safetensors 0.8.0
- 前端打包目录 = `<venv>/Lib/site-packages/comfyui_frontend_package/static/`:主入口 `index.html`,打包产物 `assets\`;插件 `web\js` 经 `GET /extensions` 运行时加载、**不参与前端打包**(重建 `assets\` 不影响扩展;`scripts\` 保留 `app.js`/`api.js` 等扩展 import 入口)
- 测试插件「从零安装」:清理浏览器缓存的 `assets\` 打包文件后,对 `http://127.0.0.1:8188` 强刷(`Ctrl+Shift+R`)再验证;**磁盘 `assets\` 勿删**(删了页面白屏)
- 启动:

先激活虚拟环境(`.venv\Scripts\activate` 或 `.venv/bin/activate`),再:

```text
cd ComfyUI
python main.py --enable-manager
```

- 或直接 `.venv\Scripts\python.exe main.py --enable-manager`(在 `ComfyUI` 下;类 Unix 用 `.venv/bin/python`);或运行 `bash comfy-server.sh`(统一跨平台后台服务式,Windows Git Bash / Linux 均可:停旧服务 → 后台启动 → 等端口;Windows 已带 `--disable-pinned-memory --fast-disk`,Linux 用 conda 环境 comfy + `--reserve-vram 22`,可覆盖 `PORT`/`WAIT`/`PY_BIN`/`LOG`/`RESERVE_VRAM`)
- 前端默认地址 `http://127.0.0.1:8188`
- 注意:主程序必须用 `.venv` 的 Python 运行(`.venv\Scripts\python.exe`,类 Unix 为 `.venv/bin/python`),不要用系统级 Python 或任何 conda 环境运行
- 改自定义节点代码后**重启 ComfyUI 生效**,无需复制文件(经软链接即时加载)

### ComfyUI 官方日志(排查插件/请求问题优先看这里)

- **官方日志文件**:`ComfyUI\user\comfyui.log`;多实例同时跑时按端口命名 `comfyui_<port>.log`(如 `comfyui_8188.log`);轮转保留 `comfyui.prev.log` / `comfyui.prev2.log`。启动时日志会打印一行 `** Log path: <路径>` 指明当前文件。
- **CLI 配置**:`--verbose LEVEL FILE` 可自定义控制台级别与文件输出(可重复),如 `--verbose INFO ComfyUI\user\comfyui_8188.log`;`--log-stdout` 把普通输出切到 stdout。
- **日志类别/格式**:行首 `[YYYY-MM-DD HH:MM:SS.mmm]` 时间戳,含级别(DEBUG/DETAIL/INFO/WARNING/ERROR/CRITICAL)。内容包括:启动信息(版本/设备/VRAM)、插件加载(`Import times for custom nodes`)、模型加载、报错 traceback、ComfyUI-Manager 网络操作,以及**自定义节点通过 `logging` 输出**的信息(插件里用 `print` 不一定进文件,建议用 `logging` 才稳定落盘)。
- **前端终端**:浏览器 ComfyUI 界面底部终端(经 WebSocket 推送的环形缓冲)也能实时看到同样的日志,排查前端扩展报错可直接看它。
- **注意**:`logs\comfyui*.log` 是用户自建重定向(如启动脚本),**不是官方位置**,可能缺部分输出;查不到关键日志时先看 `user\comfyui_<port>.log`。

## 模型与蓝图(2026-08-19 现状)

模型实际存放在 `models\` 下(`ComfyUI\models` 为软链接),当前合计约 189.1 GB。已就绪:

| 目录 | 已就绪 |
|------|--------|
| diffusion_models | `qwen_image_2512_fp8_e4m3fn`、`qwen_image_fp8_e4m3fn`、`qwen_image_edit_2511_fp8mixed`、`flux-2-klein-9b-fp8`、`minimax_h3_fl2va_pruned_int8_convrot`、`minimax_h3_ref2va_pruned_int8_convrot` |
| text_encoders | `qwen_2.5_vl_7b_fp8_scaled`(Qwen-Edit)、`qwen_3_8b_fp8mixed`(Klein)、`qwen3.5_2b_bf16`(音频)、`t5gemma_b_b_ul2`(音频)、`qwen3vl_32b_minimax_h3_nvfp4_awq`(H3 视频) |
| vae | `qwen_image_vae`、`full_encoder_small_decoder`(Klein/FLUX.2)、`minimax_h3_video_vae_fp16`、`minimax_h3_audio_vae_fp32` |
| loras | `Qwen-Image-2512-Lightning-4steps-V1.0-fp32`、`Qwen-Image-Lightning-4steps-V1.0`、`Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16`、`qwen-image-edit-2511-multiple-angles-lora`(多视角,配 `ComfyUI-qwenmultiangle` 插件)、`[Qwen-Edit]3DChineseStyle_25`、`Kook_Qwen_2512_真实幻想`、H3 加速三件:`minimax_h3_fl2v_turbo_4step_v1.0_768p_comfyui_bf16`(4 步 768p)/ `minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16` / `minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16` |
| checkpoints | `stable_audio_3_medium.safetensors`(音频) |
| upscale_models | `4xNomos8kDAT`(原 `4x-UltraSharp.pth`、`RealESRGAN_x4plus.pth` 已移除) |
| background_removal | `birefnet.safetensors` |
| controlnet | `Qwen-Image-InstantX-ControlNet-Inpainting`(InstantX Inpainting,扩图/局部重绘用) |
| facerestore_models | `GFPGANv1.4`、`GFPGANv1.3`、`codeformer-v0.1.0`、`GPEN-BFR-512`(人脸修复,Impact-Pack/ReActor 自动下载) |
| TTS | `TTS\Qwen\` 下 Qwen3-TTS-12Hz 五变体(0.6B-Base / 0.6B-CustomVoice / 1.7B-Base / 1.7B-CustomVoice / 1.7B-VoiceDesign,各含主模型 + speech_tokenizer);`TTS\SenseVoiceSmall`(ASR,`model.pt`) |

路线:Qwen-Image(国漫/中文更优)+ MiniMax H3(视频)+ FLUX.2-Klein(图像);曾清理 FLUX.2 全套、旧版 qwen_image、LTX-2.3/Wan 2.2、TripoSplat 等,后续按需重新引入(以表格为准)。`ComfyUI\blueprints\` 内置 90 个蓝图(位于 ComfyUI 目录内;除 Qwen 2511 外均缺模型)。

## 官方文档与分类文档

- `docs\ComfyUI-Docs` 为官方文档本地克隆(在线源码 GitHub `Comfy-Org/docs`);历史归档在 `backups\backup-20260805-路径清理\`;专题资料见 `webs\Bilibili\B站教程调研.md`(含 H3 专题)与 `webs\RunningHub\`(API 读取指南 / API.md / workflows-list.md)

## 开发规范

- **临时脚本(一次性调研/修改/校验用的 `.py`/`.ps1` 等)一律写入 `scripts\` 目录**,严禁散落在项目根目录或其它目录;用完即删或留存在 `scripts\` 内,不得在根目录遗留 `_*.py` 之类临时文件
- **项目根目录本身是一个 git 仓库**(`main`),子模块经 `.gitmodules` 登记、以**指针提交**(gitlink,模式 `160000`)跟踪;子模块改动在**子模块目录内** commit/push 后,再回根仓库 `git add <子模块路径>` 提交指针更新;不要留着子模块脏工作树,也不要往根仓库混入无关文件
- 修改 ComfyUI 主程序时遵守 `ComfyUI\AGENTS.md` 上游规范:改动小且直接、尽量少改文件、不引入新依赖、核心代码不发网络请求(见其 "No Internet Requests")、保持节点/API/工作流兼容、删除死代码、代码须看起来像手写
- 节点注册(V1 `NODE_CLASS_MAPPINGS` / V3 `comfy_entrypoint()`)与 ComfyUI API 使用约定见各插件仓库及 `ComfyUI\AGENTS.md`;代码书写规范(卫语句优先、switch 代替 if-else、缩进)与网络/代理策略见全局 `~/.claude\CLAUDE.md`

## 网络与代理

- 默认直连外网;直连失败(超时/403/TLS 被掐)时改用本机代理 `127.0.0.1:7890`(Clash Verge 混合端口,HTTP 与 SOCKS5 均可):
  - HTTP 代理:`http://127.0.0.1:7890`(curl `-x http://127.0.0.1:7890`、`HTTPS_PROXY`/`HTTP_PROXY` 环境变量)
  - SOCKS5:`socks5h://127.0.0.1:7890`(curl `-x socks5h://127.0.0.1:7890`)
- 注意:OpenAI 系域名等会被 Cloudflare/SNI 拦截,需走专用节点;huggingface 下载失败时优先直连、再带代理(国内可用 `hf-mirror.com` 镜像)

## 工作树现状(已知事项)

- `ComfyUI` 工作树含已删除的占位文件(`models/*/put_*_here` 等),属安装后正常现象,不要恢复或提交
- `custom_nodes\websocket_image_save.py` 与 `example_node.py.example` 是本地文件,不属于任何仓库
- `media`(input/output 软链接目标)已有内容(`audio_00001.mp3`、`qwen3tts\`、`3d\` 等);部分旧工作流引用的输入文件可能仍缺失,运行前核对

## 常见任务

- 修改工作流或重要文件前,先备份到 `backups\`,命名 `backup-<文件名>-<YYYYMMDD>-<说明>.json`;**备份一律放 `backups`,不要再放 `.claude\`**
- 新增/修改自定义节点:直接改对应子项目,经软链接即时生效,无需复制到 custom_nodes
- 验证节点加载:启动后查日志中 custom node 加载输出,或访问 `/object_info` 检查节点是否注册
- 挑选/运行工作流:先核对「模型与蓝图」确认组件就位,再开 `blueprints\`、`templates\`(官方子目录)、`webs\Bilibili\工作流大全\`、`webs\RunningHub\workflows\` 的 json
- 清理临时输出残留:删 `temp\` 里 `ComfyUI_temp_*.png` 后,「资产 → 已生成」仍显示属正常(任务历史 `GET /history` 的引用)。清理:`POST /history` + `{"clear": true}` 全清,或 `{"delete": ["<prompt_id>",...]}` 定向删;验证归零后前端 F5。⚠️ 清空前确认 history 输出均为 `temp` 类型,勿误清 output/input 真实数据

## 工作流布局规范(修改与创作必须遵守)

**布局目的**: 让工作流一眼可读、连线可追踪、节点群可辨识。以下四条为硬性要求, 修改或新建工作流时逐一自检。

1. **节点不重叠与边距**
   - 节点之间**严禁重叠**;
   - 相邻节点(横向或纵向相邻)之间边距**大于 10px** 即可, 无上限;
   - **`FallingTSMarkDownTable`(MD 数据表)节点在画布中单独占一列**: 其所在列的整条垂直方向(正下方无限延伸, 无像素限制)严禁放置任何节点——MD 节点会根据数据内容自动向下扩展高度, 同列下方有节点会被覆盖; 其他节点只能放在 MD 节点右侧的其他列(列间边距大于 10px), 与 MD 节点同列的任何位置均不得放置节点。

2. **连线走线(尽量直线)**
   - 整体按「向右向下推进」布局(见第 4 条)时, 连线天然从左上往右下正方向走, **理论上不会出现连线回折**, 无需单独校验回折;
   - 输出端口与对应输入端口**尽最大努力保持直线**: 同一功能链上的节点尽量同排/同列对齐, 让输出到下一输入基本水平(左→右);
   - 尽量避免长距离交叉串线; 有多个下游时优先保证主干直线。

3. **节点群按「正方向大区域」摆放**
   - 不同功能(加载器/采样/解码/后处理/条件)的节点群, 各自聚成**独立大区域**, 不要混排交错;
   - 整体流向保持**正向一致**: 模型/输入从左上或左侧进入, 处理链水平向右推进, 输出/保存落在右侧或右下;
   - 每个功能群内部节点紧凑对齐, 群与群之间留出明显空白带以区分。

4. **布局确定方式: 从起点开始逐个向右下推进, 定好即锁定**
   - 布局从**第一个节点**开始: 先定好它的起始位置, 再基于已定节点逐个计算后续节点的大小和位置, 一个一个确定;
   - 整体按**向右、向下**方向排列推进(新节点一般落在已定节点的右侧或右下);
   - 每确定一个节点的大小和位置后就**锁定, 不得再回头修改**; 后续节点只能适应已锁定节点, 不能反过来挪动已定节点;
   - 从开始往右下逐个确定, 直到**最后一个节点**确定完, 整套布局即视为完美定稿, 此时才允许统一修改写入文件。


## Git 提交规范

我的插件中, 严格按照 `git add .` `commit` 最后推送
项目根目录中, 严格按照 `git add .` `commit` 最后推送
子项目除了我的插件是我自己写的, 其它所有子项目不允许提交和修改代码, 或者推送
