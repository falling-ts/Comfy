# AGENTS.md — ComfyUI 本地工作区

ComfyUI 及自定义节点的本地开发工作区。系统为 Windows,shell 为 PowerShell,路径均为绝对路径。

> 本文件于 2026-08-05 由 `.codex\AGENTS.md` 提取至项目根(Codex 与 Claude Code 均自动读取),仅保留 **项目私有/特殊信息**;通用 ComfyUI 框架、模型目录、后缀术语等知识不在此展开,需要时读在线文档或 `backups\backup-20260805-路径清理\` 归档。`.codex\` 与 `.claude\` 已删除,原内容见该归档备份。本文件内路径均为相对项目根目录的写法,便于跨机器使用。

## 目录结构

| 路径 | 说明 |
|------|------|
| `ComfyUI` | ComfyUI 主程序,`master` 分支,v0.30.0(独立 git 仓库;官方默认分支即 `master`;本地曾用 `dev` 分支,现已删除) |
| `ComfyUI-GGUF` | GGUF 量化模型加载/推理节点(独立 git 仓库,`main`) |
| `ComfyUI-KJNodes` | KJNodes 工具节点包(独立 git 仓库,`main`) |
| `ComfyUI-FallingTS` | comfy-desktop-plugins:Seedance 2.0 视频生成节点,走 Volcengine API(独立 git 仓库,`main`,2026-08-04 开源发布准备完成) |
| `ComfyUI_UltimateSDUpscale` | 分块重绘插件 Ultimate SD Upscale(git clone 含子模块 `repositories/ultimate_sd_upscale`) |
| `ComfyUI-Docs` | ComfyUI 官方文档仓库本地克隆(Comfy-Org/docs,`main` 分支,SSH) |
| `MiniMax-H3` | MiniMax H3 官方模型仓库(子模块,`main`),自带官方 Skills,见「子项目约定 → MiniMax-H3」 |
| `workflows` | **用户工作流实际存储处**(17 个 json:图片 8 / 视频 4 / 音频 5),前端保存即在此,可经 `GET /userdata?dir=workflows` 读取 |
| `models` | 模型目录(实际存放处,`ComfyUI\models` 为软链接) |
| `media` | 输入/输出文件(input、output 均软链接到此) |
| `Templates` | ComfyUI 官方模板库本地缓存(494 个,按类分目录) |
| `RunningHub` | RunningHub 调研(非 git):`RunningHub-API读取指南.md` + `API.md` + `workflows\`(429 个) |
| `Bilibili` | B 站调研(非 git):`B站教程调研.md` + `工作流大全\`(153 个配套工作流) |
| `backups` | **工作流/重要文件的修改前备份目录**(2026-08-04 起,替代原 `.claude\` 存放位置) |
| `start-comfyui.cmd / .ps1` | 一键启动脚本(等价 `python main.py --enable-manager`) |

## 软链接映射(重要,全项目为相对路径 SymbolicLink)

所有链接均为相对路径符号链接,**项目根目录整体移动后不失效**:

| ComfyUI 内路径 | 类型 | 相对目标 | 实际指向 |
|------|------|------|------|
| `custom_nodes\ComfyUI_UltimateSDUpscale` | SymbolicLink | `..\..\ComfyUI_UltimateSDUpscale` | `ComfyUI_UltimateSDUpscale` |
| `custom_nodes\ComfyUI-GGUF` | SymbolicLink | `..\..\ComfyUI-GGUF` | `ComfyUI-GGUF` |
| `custom_nodes\ComfyUI-KJNodes` | SymbolicLink | `..\..\ComfyUI-KJNodes` | `ComfyUI-KJNodes` |
| `custom_nodes\ComfyUI-FallingTS` | SymbolicLink | `..\..\ComfyUI-FallingTS` | `ComfyUI-FallingTS`(原 `ComfyUI-Plugins`,更早 `comfy_desktop_plugins`) |
| `ComfyUI\input` | SymbolicLink | `..\media` | `media` |
| `ComfyUI\output` | SymbolicLink | `..\media` | `media` |
| `ComfyUI\models` | SymbolicLink | `..\models` | `models`(模型实际存放处) |
| `ComfyUI\user\default\workflows` | SymbolicLink | `..\..\..\workflows` | `workflows`(用户工作流实际存储处) |

- `custom_nodes` 已被 ComfyUI `.gitignore` 忽略,改动不污染 git
- `ComfyUI\temp\`(真实目录,非链接):运行中生成的临时文件/预览图(如 `ComfyUI_temp_*.png`),可随时清理
- ⚠️ **`ComfyUI\input\`(用户上传)与 `output\`(生成结果)是真实数据:严禁删除、移动或批量清理**;只有 `temp\` 可清理

## 版本与运行

- conda 环境 `ComfyUI`(位于 `miniconda3\envs\ComfyUI`,Python 3.13.14)
- 依赖版本:torch 2.13.0+cu130、comfyui-frontend-package 1.47.11、comfyui-manager 4.2.2、comfyui-workflow-templates 0.11.27
- 启动:

```powershell
conda activate ComfyUI
cd ComfyUI
python main.py --enable-manager
```

- 或 `conda run -n ComfyUI python main.py --enable-manager`(在 `ComfyUI` 下);双击 `start-comfyui.cmd` / 运行 `start-comfyui.ps1` 等价
- 前端默认地址 `http://127.0.0.1:8188`
- 注意:环境名是 `ComfyUI`(不是 "ConfyUI");不要用系统级 Python 运行主程序
- 改自定义节点代码后**重启 ComfyUI 生效**,无需复制文件(经软链接即时加载)

## 模型与蓝图(2026-08-05 现状)

模型实际存放在 `models\` 下(ComfyUI\models 为软链接)。当前已就绪:

| 目录 | 已就绪 |
|------|--------|
| diffusion_models | `qwen_image_2512_fp8_e4m3fn`、`qwen_image_edit_2511_bf16`、`flux-2-klein-9b-fp8`、`minimax_h3_fl2va_pruned_int8_convrot`、`minimax_h3_ref2va_pruned_int8_convrot` |
| text_encoders | `qwen_2.5_vl_7b_fp8_scaled`(Qwen-Edit)、`qwen_3_8b_fp8mixed`(Klein)、`qwen3.5_2b_bf16`(音频)、`t5gemma_b_b_ul2`(音频) |
| vae | `qwen_image_vae`、`full_encoder_small_decoder`(Klein/FLUX.2) |
| loras | `Qwen-Image-2512-Lightning-4steps-V1.0-fp32` |
| checkpoints | `stable_audio_3_medium.safetensors`(音频) |
| upscale_models | `4x-UltraSharp.pth`、`4xNomos8kDAT`、`RealESRGAN_x4plus.pth` |
| background_removal | `birefnet.safetensors` |

**MiniMax H3 视频类仍缺 3 个**(已下 fl2va/ref2va,共约 21.5GB 待补,见 `视频-01~04`):
- `vae/minimax_h3_video_vae_fp16.safetensors`(~5.2GB)
- `vae/minimax_h3_audio_vae_fp32.safetensors`(~0.6GB)
- `text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors`(~15.7GB)

已删除(2026-08-03):FLUX.2 文生图全套 5 文件 69.28G、qwen_image 文生图全家、qwen_edit 2509、LTX-2.3/Wan 2.2 视频、TripoSplat 3D;路线转向 Qwen-Image(国漫/中文更优)。`blueprints\` 内置 89 个蓝图;除 Qwen 2511 外其余蓝图均缺模型。

## 官方文档与分类文档

- 本地克隆 `ComfyUI-Docs`(SSH,`main`,保持纯净);在线源码为 GitHub `Comfy-Org/docs`(内容规则详见该仓库,不在此展开)
- 分类文档已归档到 `backups\backup-20260805-路径清理\`(01-08 全量;05 含 Codex 协作约定与 Claude 协作约定两版)
- 专题资料:`Bilibili\B站教程调研.md`(含 MiniMax H3 专题);`RunningHub-API读取指南.md` + `API.md` + `workflows-list.md`

## 子项目约定

### ComfyUI-GGUF
- GGUF 量化模型加载/推理;注册 `UnetLoaderGGUF`、`CLIPLoaderGGUF`、`DualCLIPLoaderGGUF`、`TripleCLIPLoaderGGUF`、`QuadrupleCLIPLoaderGGUF`、`UnetLoaderGGUFAdvanced`
- 关键文件:`nodes.py`(注册)、`loader.py`、`ops.py`、`dequant.py`

### ComfyUI-KJNodes
- 大型工具节点包;节点分散在 `nodes\` 下(`nodes.py` 核心 + `curve_nodes.py`、`batchcrop_nodes.py`、`image_nodes.py`、`mask_nodes.py`、`lora_nodes.py`、`ltxv_nodes.py`、`audioscheduler_nodes.py` 等),`__init__.py` 聚合导出
- 新节点按类别放入对应文件并同步 `__init__.py` 导出

### ComfyUI-FallingTS(comfy-desktop-plugins)
- 使用 ComfyUI V3 扩展 API(`comfy_api.latest` 的 `IO`/`ComfyExtension`),只兼容 `dev` 分支(v0.29+),不要降级 ComfyUI
- 当前注册 2 个节点:`Seedance2FirstLastFrame`(首尾帧生视频)、`Seedance2Reference`(多模态参考生视频);入口 `plugin.py`(`comfy_entrypoint()` / `inject()`)
- ⚠️ **`.env` 含真实 API Key,禁止读取、打印或提交**(`.env` 已在 .gitignore)
- 注意:`README.md` 已过时(仍声称 4 个节点,实际 2 个),改动节点时同步文档

### MiniMax-H3(官方模型仓库 + 官方 Skills)
- MiniMax H3 官方仓库(子模块,`main` 分支),包含完整模型结构(diffusers 组件)与官方 Skills;本地推理仍走 ComfyUI 内置 H3 节点与各加速插件
- **官方 Skills 位置:`MiniMax-H3\skills\`**,共 9 个:
  - `h3-prompt-writing`(核心,英文):H3 提示词写作规范,覆盖全部 5 种生成模式 T2VA / I2VA / FL2VA / L2VA / Ref2VA,结构化为 `integrated_multimodal_description` + `overall_soundscape` + `non_diegetic_music`;附 `references\base-en.txt`(基础模式)与 `references\ref-en.txt`(Ref2VA 全参考模式)
  - 8 个风格生成器(均含 `SKILL.md` + 中文 `SKILL.cn.md`):`3d-animation-short-generator`、`brand-promo-video-generator`、`co-op-game-intro-generator`、`handdrawn-live-video-generator`、`minimalist-product-ad-generator`、`mv-subtitle-skill-confirmed`、`paper-collage-explainer-generator`、`papercraft-stop-motion-explainer`
- **用法**:写 H3 提示词时先读 `MiniMax-H3\skills\h3-prompt-writing\SKILL.md` 及其 references;风格类任务在基础规范之上叠加对应生成器 skill(读其 `SKILL.md`/`SKILL.cn.md`)
- 官方安装 CLI(备用):`npx skills add https://github.com/MiniMax-AI/MiniMax-H3 --skill h3-prompt-writing`
- 更新:`git -C MiniMax-H3 pull`(子模块)

## 开发规范

- 修改 ComfyUI 主程序时遵守 `ComfyUI\AGENTS.md` 上游规范:改动小且直接、尽量少改文件、不引入新依赖、核心代码不发网络请求、保持节点/API 兼容
- 各子项目是独立 git 仓库,必须与线上保持纯粹一致:**不要在这些目录内新增/修改/删除文件**;项目根目录本身不是 git 仓库,不要在根目录执行 git 操作
- 节点注册(V1 `NODE_CLASS_MAPPINGS` / V3 `comfy_entrypoint()`)等通用约定与代码书写规范见全局 `~/.claude\CLAUDE.md`

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
- `media` 目前为空(2026-08-05):workflows 里引用的输入图片/音频文件均尚不存在,运行前需放入

## 常见任务

- 修改工作流或重要文件前,先备份到 `backups\`,命名 `backup-<文件名>-<YYYYMMDD>-<说明>.json`;**备份一律放 `backups`,不要再放 `.claude\`**
- 新增/修改自定义节点:直接改对应子项目,经软链接即时生效,无需复制到 custom_nodes
- 验证节点加载:启动后查日志中 custom node 加载输出,或访问 `/object_info` 检查节点是否注册
- 挑选/运行工作流:先核对「模型与蓝图」确认组件就位,再开 `blueprints\`、`Templates\`(494 个)、`Bilibili\工作流大全\`、`RunningHub\workflows\` 的 json
- 清理临时输出残留:删 `temp\` 里 `ComfyUI_temp_*.png` 后,前端「资产 → 已生成」可能仍显示内容 —— 那是任务历史(`GET /history`)中的输出记录,文件已删但引用还在。清理:`POST /history` + `{"clear": true}` 全清(等价 `server.py` 的 `wipe_history()`),或 `{"delete": ["<prompt_id>", ...]}` 定向删除;验证 `GET /history` 归零,前端 F5 刷新。注:资产系统默认禁用(`--enable-assets` 才启用),任务历史是「已生成」面板唯一来源;清空前确认 history 输出均为 `temp` 类型(无 output/input 真实数据)
