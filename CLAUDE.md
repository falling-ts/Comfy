# ComfyUI 本地工作区

ComfyUI 及自定义节点的本地开发工作区。系统为 Windows,shell 为 PowerShell,路径均相对项目根目录。

## 目录结构

| 路径 | 说明 |
|------|------|
| `ComfyUI` | ComfyUI 主程序(git submodule,`master` 分支) |
| `ComfyUI-GGUF` | GGUF 量化模型加载/推理节点(git submodule,`main`) |
| `ComfyUI-KJNodes` | KJNodes 工具节点包(git submodule,`main`) |
| `ComfyUI-FallingTS` | 这是我的插件,通用工具节点集:Continue/Selector/Table/Switch/PreviewVideo 5 节点 + 前端增强 |
| `ComfyUI_UltimateSDUpscale` | 分块重绘插件 Ultimate SD Upscale(git submodule,`main`,含 `repositories/ultimate_sd_upscale`) |
| `ComfyUI-Docs` | ComfyUI 官方文档仓库本地克隆(Comfy-Org/docs,`main` 分支) |
| `MiniMax-H3` | MiniMax H3 官方模型仓库(git submodule,`main`),自带官方 Skills(`MiniMax-H3\skills\`,共 9 个) |
| `ComfyUI-MiniMaxH3-Cache` 等 7 个 H3 配套插件 | EasyCache/HyperStep/Spectrum/SolAttn/ReservedVRAM(加速)+ Qwen3-TTS(语音)+ GJJ_Nodes(角色库),均 git submodule(`main`),经 `custom_nodes` **相对路径**软链接加载,详见「软链接映射 §B」 |
| `minimax-h3-guide` | H3 参考加载套件(git submodule,`main`),`custom_nodes\H3ReferenceSuite` 指向其 `custom_nodes\H3ReferenceSuite` |
| `SHUO-Canvas` | AI 多模态创作画布(原 AI-CanvasPro):文字/图片/视频/音频节点化串联,支持 RunningHub 与 ComfyUI 本地/云端工作流(git submodule,`main`,v0.7.2,非开源 NC 许可) |
| `workflows` | **用户工作流实际存储处**(21 个 json:17 个活动工作流[图片 8 / 视频 4 / 音频 5] + 4 个 `backup-*` 备份),前端保存即在此,可经 `GET /userdata?dir=workflows` 读取 |
| `models` | 模型目录(实际存放处,`ComfyUI\models` 为软链接) |
| `media` | 输入/输出文件(input、output 均软链接到此) |
| `Templates` | ComfyUI 官方模板库本地缓存(494 个,按类分目录) |
| `RunningHub` | RunningHub 调研(非 git):`RunningHub-API读取指南.md` + `API.md` + `workflows\`(429 个) |
| `Bilibili` | B 站调研(非 git):`B站教程调研.md` + `工作流大全\`(153 个配套工作流) |
| `AutoDL` | 云端 GPU 调研(非 git):`AutoDL-GPU选型-2026-08-06.md` + `api.md`(云模型库接口)+ `models.md`(4015 条模型清单) |
| `Stories` | Obsidian 故事写作工作区(`.obsidian\`):`template\` + `七纹刻印\` 两本 |
| `docs` | 本地参考文档(7 个 md):启动参数参考、KSampler 采样器指南、SageAttention 参数配置、Qwen 国漫 LoRA 清单、模型调研报告等 |
| `logs` | ComfyUI 运行日志(`comfyui*.log`/`comfyui-console*.log`,已 gitignore) |
| `backups` | **工作流/重要文件的修改前备份目录**(2026-08-04 起,替代原 `.claude\` 存放位置) |
| `README.md` / `LICENSE` | 项目说明与许可 |
| `.gitmodules` | 16 个子模块登记(git submodule) |
| `start-comfyui.cmd / .ps1` | 一键启动脚本(等价 `python main.py --enable-manager --disable-pinned-memory --fast-disk`) |

## 软链接映射(重要,共 16 个,全部为相对路径 SymbolicLink,2026-08-07 实测)

全部为 Windows **相对路径**符号链接,**项目根目录整体移动后不失效**。

### A. 基础链接(4 个)

| ComfyUI 内路径 | 类型 | 相对目标 | 实际指向 |
|------|------|------|------|
| `ComfyUI\input` | SymbolicLink | `..\media` | `media` |
| `ComfyUI\output` | SymbolicLink | `..\media` | `media` |
| `ComfyUI\models` | SymbolicLink | `..\models` | `models`(模型实际存放处) |
| `ComfyUI\user\default\workflows` | SymbolicLink | `..\..\..\workflows` | `workflows`(用户工作流实际存储处) |

### B. custom_nodes 插件链接(12 个,均指向项目根)

| ComfyUI 内路径 | 类型 | 相对目标 | 实际指向 |
|------|------|------|------|
| `custom_nodes\ComfyUI_UltimateSDUpscale` | SymbolicLink | `..\..\ComfyUI_UltimateSDUpscale` | `ComfyUI_UltimateSDUpscale` |
| `custom_nodes\ComfyUI-GGUF` | SymbolicLink | `..\..\ComfyUI-GGUF` | `ComfyUI-GGUF` |
| `custom_nodes\ComfyUI-KJNodes` | SymbolicLink | `..\..\ComfyUI-KJNodes` | `ComfyUI-KJNodes` |
| `custom_nodes\ComfyUI-FallingTS` | SymbolicLink | `..\..\ComfyUI-FallingTS` | `ComfyUI-FallingTS`(原 `ComfyUI-Plugins`,更早 `comfy_desktop_plugins`) |
| `custom_nodes\ComfyUI-MiniMaxH3-Cache` | SymbolicLink | `..\..\ComfyUI-MiniMaxH3-Cache` | `ComfyUI-MiniMaxH3-Cache` |
| `custom_nodes\ComfyUI-NB-H3-HyperStep` | SymbolicLink | `..\..\ComfyUI-NB-H3-HyperStep` | `ComfyUI-NB-H3-HyperStep` |
| `custom_nodes\ComfyUI-Qwen3-TTS` | SymbolicLink | `..\..\ComfyUI-Qwen3-TTS` | `ComfyUI-Qwen3-TTS` |
| `custom_nodes\ComfyUI-ReservedVRAM` | SymbolicLink | `..\..\ComfyUI-ReservedVRAM` | `ComfyUI-ReservedVRAM` |
| `custom_nodes\ComfyUI-SolAttn_triton` | SymbolicLink | `..\..\ComfyUI-SolAttn_triton` | `ComfyUI-SolAttn_triton` |
| `custom_nodes\ComfyUI-Spectrum-MiniMax-H3` | SymbolicLink | `..\..\ComfyUI-Spectrum-MiniMax-H3` | `ComfyUI-Spectrum-MiniMax-H3` |
| `custom_nodes\ComfyUI_GJJ_Nodes` | SymbolicLink | `..\..\ComfyUI_GJJ_Nodes` | `ComfyUI_GJJ_Nodes` |
| `custom_nodes\H3ReferenceSuite` | SymbolicLink | `..\..\minimax-h3-guide\custom_nodes\H3ReferenceSuite` | `minimax-h3-guide\custom_nodes\H3ReferenceSuite` |

- `custom_nodes` 已被 ComfyUI `.gitignore` 忽略,改动不污染 git
- `ComfyUI\temp\`(真实目录,非链接):运行中生成的临时文件/预览图(如 `ComfyUI_temp_*.png`),可随时清理
- ⚠️ **`ComfyUI\input\`(用户上传)与 `output\`(生成结果)是真实数据:严禁删除、移动或批量清理**;只有 `temp\` 可清理

## 版本与运行

- conda 根:`C:\Users\zghyu\Miniconda3`(conda 不在 Git Bash 的 PATH;用 `conda activate` 或直接调 env 内 `python.exe`)
- **两个名称极易混淆的 conda 环境,均为 Python 3.13.14 / torch 2.13.0+cu130(CUDA 13.0,RTX 4060 8GB VRAM)**:
  - `ComfyUI`(2026-07-31 建,197 包)= **运行环境**,`start-comfyui.cmd` 与本文档均用它,路径 `miniconda3\envs\ComfyUI\python.exe`
  - `Comfy`(2026-08-07 建,199 包)= 同款基础上多 `onnxruntime-gpu 1.28.0`、`opencv-python 5.0.0.93`(其余仅依赖小版本差异),疑似备用/实验环境,勿混用
- 共享关键版本:comfyui-frontend-package **1.48.6**、comfyui-manager **4.2.2**、comfyui-workflow-templates **0.11.31**、sageattention **2.2.0**(cu130)、comfy-kitchen **0.2.26**、comfy-aimdo 0.4.13、transformers 4.57.3、diffusers 0.39.0、numpy 2.4.6、safetensors 0.8.0
- 启动:

```powershell
conda activate ComfyUI
cd ComfyUI
python main.py --enable-manager
```

- 或 `conda run -n ComfyUI python main.py --enable-manager`(在 `ComfyUI` 下);双击 `start-comfyui.cmd` / 运行 `start-comfyui.ps1` 等价(脚本已带 `--disable-pinned-memory --fast-disk`,适配 8GB VRAM/16GB RAM)
- 前端默认地址 `http://127.0.0.1:8188`
- 注意:环境名是 `ComfyUI`(不是 "ConfyUI",也不要与 `Comfy` 混用);不要用系统级 Python(`C:\Program Files\Python313`,3.13.13)运行主程序
- 改自定义节点代码后**重启 ComfyUI 生效**,无需复制文件(经软链接即时加载)

## 模型与蓝图(2026-08-07 现状)

模型实际存放在 `models\` 下(`ComfyUI\models` 为软链接),当前合计约 178.7 GB。已就绪:

| 目录 | 已就绪 |
|------|--------|
| diffusion_models | `qwen_image_2512_fp8_e4m3fn`、`qwen_image_edit_2511_bf16`、`flux-2-klein-9b-fp8`、`minimax_h3_fl2va_pruned_int8_convrot`、`minimax_h3_ref2va_pruned_int8_convrot` |
| text_encoders | `qwen_2.5_vl_7b_fp8_scaled`(Qwen-Edit)、`qwen_3_8b_fp8mixed`(Klein)、`qwen3.5_2b_bf16`(音频)、`t5gemma_b_b_ul2`(音频)、`qwen3vl_32b_minimax_h3_nvfp4_awq`(H3 视频) |
| vae | `qwen_image_vae`、`full_encoder_small_decoder`(Klein/FLUX.2)、`minimax_h3_video_vae_fp16`、`minimax_h3_audio_vae_fp32` |
| loras | `Qwen-Image-2512-Lightning-4steps-V1.0-fp32`、`Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16`、`minimax_h3_turbo_4step`、`[Qwen-Edit]3DChineseStyle_25`、`Kook_Qwen_2512_真实幻想` |
| checkpoints | `stable_audio_3_medium.safetensors`(音频) |
| upscale_models | `4xNomos8kDAT`(原 `4x-UltraSharp.pth`、`RealESRGAN_x4plus.pth` 已移除) |
| background_removal | `birefnet.safetensors` |
| TTS | `TTS\Qwen\` 下 Qwen3-TTS-12Hz 五变体(0.6B-Base / 0.6B-CustomVoice / 1.7B-Base / 1.7B-CustomVoice / 1.7B-VoiceDesign,各含主模型 + speech_tokenizer);`TTS\SenseVoiceSmall`(ASR,`model.pt`) |

MiniMax H3 视频类此前缺的 3 个文件已全部补齐(2026-08-07):`vae\minimax_h3_video_vae_fp16`(~4.9GB)、`vae\minimax_h3_audio_vae_fp32`(~0.6GB)、`text_encoders\qwen3vl_32b_minimax_h3_nvfp4_awq`(~14.6GB)。

空目录(尚未放置模型):`ASR\`、`GJJ\`(character_library/costume_library/scene_library/wav 四个子目录)、`audio_encoders\`、`diffusers\` 等其余标准目录。

已删除(2026-08-03):FLUX.2 文生图全套 5 文件 69.28G、qwen_image 文生图全家、qwen_edit 2509、LTX-2.3/Wan 2.2 视频、TripoSplat 3D;路线转向 Qwen-Image(国漫/中文更优)。`ComfyUI\blueprints\` 内置 89 个蓝图(注意:位于 ComfyUI 目录内,不在项目根);除 Qwen 2511 外其余蓝图均缺模型。

## 官方文档与分类文档

- 本地克隆 `ComfyUI-Docs`(SSH,`main`,保持纯净);在线源码为 GitHub `Comfy-Org/docs`(内容规则详见该仓库,不在此展开)
- 分类文档已归档到 `backups\backup-20260805-路径清理\`(01-08 全量;05 含 Codex 协作约定与 Claude 协作约定两版)
- 专题资料:`Bilibili\B站教程调研.md`(含 MiniMax H3 专题);`RunningHub-API读取指南.md` + `API.md` + `workflows-list.md`

## 开发规范

- 项目根目录 `D:\Comfy` **本身是一个 git 仓库**(`main`),经 `.gitmodules` 登记 16 个子模块;根仓库跟踪的是各子模块的**指针提交**(`git ls-files -s` 中模式 `160000`)。不要误以为"根目录不是 git 仓库、不能在根目录执行 git 操作"
- 各子项目(ComfyUI 及全部插件、ComfyUI-Docs、MiniMax-H3、SHUO-Canvas 等)是根仓库的 git **子模块**:各自独立仓库、自身维护与上游一致。改动子模块代码在**子模块目录内**正常 commit/push,再回到根仓库 `git add <子模块路径>` 提交一次"指针更新";不要留着子模块脏工作树不提交,也不要往根仓库混入无关文件
- 修改 ComfyUI 主程序时遵守 `ComfyUI\AGENTS.md` 上游规范:改动小且直接、尽量少改文件、不引入新依赖、核心代码不发网络请求(见其 "No Internet Requests")、保持节点/API/工作流兼容、删除死代码、代码须看起来像手写
- 节点注册(V1 `NODE_CLASS_MAPPINGS` / V3 `comfy_entrypoint()`)与 ComfyUI API 使用约定见各插件仓库及 `ComfyUI\AGENTS.md`;代码书写规范(卫语句优先、switch 代替 if-else、缩进)与网络/代理策略见全局 `~/.claude\CLAUDE.md`

## 工作流节点固定规范(强制)

**所有创作或修改的工作流 JSON,全部节点必须"固定"(pinned),防止拖动/缩放破坏布局。**

- 固定写法:每个节点的 `flags` 必须包含 `"pinned": true`:
  ```json
  {
    "id": 8,
    "type": "EmptySD3LatentImage",
    "pos": [-520, 480],
    "size": [300, 560],
    "order": 16,
    "mode": 0,
    "flags": {"pinned": true},
    "inputs": [],
    "outputs": [],
    "widgets_values": []
  }
  ```
- 字段语义(源自前端源码 `GraphView`/`settingStore`/`api` schema):`flags.pinned = true` 后节点不可拖动、不可调整大小(等价右侧面板 SetPinned 开关 `node.pin(true)`);`mode` 为 0=always / 2=never / 4=bypass;`order` 为执行顺序;`pos` 为画布坐标、`size` 为宽高。
- 每次创建/修改工作流后必须验证:遍历所有节点,`flags.pinned === true`,且节点 `pos/size` 两两不重叠。
- 未固定的工作流视为未完成,提交前必须补上。注意:折叠子图(subgraph)内部节点同样要 pinned。

## 网络与代理

- 默认直连外网;直连失败(超时/403/TLS 被掐)时改用本机代理 `127.0.0.1:7890`(Clash Verge 混合端口,HTTP 与 SOCKS5 均可):
  - HTTP 代理:`http://127.0.0.1:7890`(curl `-x http://127.0.0.1:7890`、`HTTPS_PROXY`/`HTTP_PROXY` 环境变量)
  - SOCKS5:`socks5h://127.0.0.1:7890`(curl `-x socks5h://127.0.0.1:7890`)
- 注意:部分站点(如 OpenAI 系域名)直连会被 Cloudflare 拦截,普通代理节点也可能被按 SNI 掐断,需走允许对应域名的专用节点;huggingface 下载失败时优先重试直连,再带代理(国内可用 `hf-mirror.com` 镜像)

## 工作树现状(已知事项)

- `ComfyUI` 工作树含已删除的占位文件(`models/*/put_*_here` 等),属安装后正常现象,不要恢复或提交
- `ComfyUI-FallingTS` 已完成开源发布准备(README/.gitignore 完善、web 扩展入库、`.claude/` 已忽略),工作树干净
- `custom_nodes\websocket_image_save.py` 与 `example_node.py.example` 是本地文件,不属于任何仓库
- `media`(input/output 软链接目标)已有内容(2026-08-07 实测):`audio_00001.mp3`、`qwen3tts\`、`3d\` 等;部分旧工作流引用的输入文件可能仍缺失,运行前核对

## 常见任务

- 修改工作流或重要文件前,先备份到 `backups\`,命名 `backup-<文件名>-<YYYYMMDD>-<说明>.json`;**备份一律放 `backups`,不要再放 `.claude\`**
- 新增/修改自定义节点:直接改对应子项目,经软链接即时生效,无需复制到 custom_nodes
- 验证节点加载:启动后查日志中 custom node 加载输出,或访问 `/object_info` 检查节点是否注册
- 挑选/运行工作流:先核对「模型与蓝图」确认组件就位,再开 `blueprints\`、`Templates\`(494 个)、`Bilibili\工作流大全\`、`RunningHub\workflows\` 的 json
- 清理临时输出残留:删 `temp\` 里 `ComfyUI_temp_*.png` 后,前端「资产 → 已生成」可能仍显示内容 —— 那是任务历史(`GET /history`)中的输出记录,文件已删但引用还在。清理:`POST /history` + `{"clear": true}` 全清(等价 `server.py` 的 `wipe_history()`),或 `{"delete": ["<prompt_id>", ...]}` 定向删除;验证 `GET /history` 归零,前端 F5 刷新。注:资产系统默认禁用(`--enable-assets` 才启用),任务历史是「已生成」面板唯一来源;清空前确认 history 输出均为 `temp` 类型(无 output/input 真实数据)

## Git 提交规范

我的插件中, 严格按照 `git add .` `commit` 最后推送
项目根目录中, 严格按照 `git add .` `commit` 最后推送
子项目除了我的插件是我自己写的, 其它所有子项目不允许提交和修改代码, 或者推送
