# ComfyUI 本地工作区

ComfyUI 及自定义节点的本地开发工作区。系统为 Windows,shell 为 PowerShell,路径均相对项目根目录。

## 目录结构

| 路径 | 说明 |
|------|------|
| `ComfyUI` | ComfyUI 主程序(git submodule,`master` 分支) |
| `custom_nodes` | **插件聚合目录**(2026-08-10 起):15 个插件子模块 + `H3ReferenceSuite` 链接全部集中于此;`ComfyUI\custom_nodes` 经**目录级**相对软链接指向它,详见「软链接映射 §B」 |
| `custom_nodes\ComfyUI-GGUF` | GGUF 量化模型加载/推理节点(git submodule,`main`) |
| `custom_nodes\ComfyUI-KJNodes` | KJNodes 工具节点包(git submodule,`main`) |
| `custom_nodes\ComfyUI-FallingTS` | 这是我的插件,通用工具节点集:Continue/Selector/Table/Switch/PreviewVideo 5 节点 + 前端增强 |
| `custom_nodes\ComfyUI_UltimateSDUpscale` | 分块重绘插件 Ultimate SD Upscale(git submodule,`main`,含 `repositories/ultimate_sd_upscale`) |
| `custom_nodes\ComfyUI-Impact-Pack` | 局部放大/检测精修插件(git submodule,`main`,2026-08-10 加入):`DetailerForEach`/`FaceDetailer`/`ImpactImageCrop`,区域框选→裁剪→放大→重绘→贴回 |
| `custom_nodes\ComfyUI_LayerStyle` | 图层风格化节点集(git submodule,`main`,2026-08-10 加入):`LayerUtility: CropByMask`/`LayerMask: MaskBoxDetect` 画遮罩选区域 |
| `custom_nodes\ComfyUI-Easy-Use` | 易用节点集(git submodule,`main`,2026-08-10 加入):`easy imageCrop` 前端拖框截图、`easy imageSplitGrid` 九宫格拆块放大 |
| `custom_nodes\ComfyUI-SeedVR2_VideoUpscaler` | SeedVR2 高清修复/放大插件(git submodule,`main`,2026-08-10 加入,支持图像与视频) |
| `custom_nodes\ComfyUI-SUPIR` | SUPIR 超分放大插件(git submodule,`main`,2026-08-10 加入,kijai 维护) |
| `docs\ComfyUI-Docs` | ComfyUI 官方文档仓库本地克隆(Comfy-Org/docs,`main` 分支),2026-08-10 移入 `docs\` |
| `docs\Obsidian-Dev-Docs` | Obsidian 官方**开发者文档**仓库(obsidianmd/obsidian-developer-docs,`main`,2026-08-10 加入),开发 Obsidian 插件参考 |
| `docs\Obsidian-API` | Obsidian **API 类型定义**仓库(obsidianmd/obsidian-api,`master`,2026-08-10 加入),开发插件用 `obsidian.d.ts`/`publish.d.ts` |
| `h3` | **MiniMax H3 生态聚合目录**(2026-08-10 建):`MiniMax-H3` + `minimax-h3-guide` 两个子模块 |
| `h3\MiniMax-H3` | MiniMax H3 官方模型仓库(git submodule,`main`),自带官方 Skills(`h3\MiniMax-H3\skills\`,共 9 个) |
| `custom_nodes\ComfyUI-MiniMaxH3-Cache` 等 6 个 H3 配套插件 | EasyCache/Spectrum/SolAttn/ReservedVRAM(加速)+ Qwen3-TTS(语音)+ GJJ_Nodes(角色库),均 git submodule(`main`),集中于 `custom_nodes\`,经目录级软链接加载,详见「软链接映射 §B」 |
| `h3\minimax-h3-guide` | H3 参考加载套件(git submodule,`main`);其 `custom_nodes\H3ReferenceSuite` 由根 `custom_nodes\H3ReferenceSuite` 子链接指向 |
| `workflows` | **用户工作流实际存储处**(当前仅 **`万物建模.json`** 1 个主工作流;原图片 8/视频 4/音频 5 共 17 个工作流已于 2026-08-09 移入 `templates\` 根目录归档),前端保存即在此,可经 `GET /userdata?dir=workflows` 读取 |
| `models` | 模型目录(实际存放处,`ComfyUI\models` 为软链接) |
| `media` | 输入/输出文件(input、output 均软链接到此) |
| `templates` | ComfyUI 官方模板库本地缓存(按类分目录)+ **个人工作流归档**(根目录 17 个 json:图片 8 / 视频 4 / 音频 5,2026-08-09 移入) |
| `webs` | **三方网站调研聚合目录**(非 git,2026-08-10 移入):`RunningHub\` + `Bilibili\` + `AutoDL\` |
| `webs\RunningHub` | RunningHub 调研(非 git):`RunningHub-API读取指南.md` + `API.md` + `workflows\`(429 个) |
| `webs\Bilibili` | B 站调研(非 git):`B站教程调研.md` + `工作流大全\`(153 个配套工作流) |
| `webs\AutoDL` | 云端 GPU 调研(非 git):`AutoDL-GPU选型-2026-08-06.md` + `api.md`(云模型库接口)+ `models.md`(4015 条模型清单) |
| `stories` | Obsidian 故事写作工作区(`.obsidian\`):`template\` + `七纹刻印\` 两本 |
| `docs` | 本地参考文档(7 个 md)+ **文档子模块**(`docs\ComfyUI-Docs` + `docs\Obsidian-Dev-Docs` + `docs\Obsidian-API`):启动参数参考、KSampler 采样器指南、SageAttention 参数配置、Qwen 国漫 LoRA 清单、模型调研报告等 |
| `logs` | ComfyUI 运行日志(`comfyui*.log`/`comfyui-console*.log`,已 gitignore) |
| `backups` | **工作流/重要文件的修改前备份目录**(2026-08-04 起,替代原 `.claude\` 存放位置) |
| `README.md` / `LICENSE` | 项目说明与许可 |
| `.gitmodules` | 21 个子模块登记(git submodule) |
| `start-comfyui.cmd / .ps1` | 一键启动脚本(等价 `python main.py --enable-manager --disable-pinned-memory --fast-disk`) |

## 软链接映射(重要,共 6 个,全部为相对路径 SymbolicLink;2026-08-07 建,08-10 插件收敛为目录级链接)

全部为 Windows **相对路径**符号链接,**项目根目录整体移动后不失效**。

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
| `ComfyUI\custom_nodes` | SymbolicLink(目录级) | `..\custom_nodes` | 根 `custom_nodes`(插件聚合目录,15 插件 + H3ReferenceSuite 链接) |
| `custom_nodes\H3ReferenceSuite` | SymbolicLink(子链接) | `..\h3\minimax-h3-guide\custom_nodes\H3ReferenceSuite` | `h3\minimax-h3-guide\custom_nodes\H3ReferenceSuite` |

- 根 `custom_nodes` 由**根仓库**跟踪:15 个插件以 gitlink 形式登记,`H3ReferenceSuite` 为符号链接;本地文件 `example_node.py.example`、`websocket_image_save.py` 被根 `.gitignore` 排除(保留磁盘副本供加载)。`ComfyUI\custom_nodes` 是目录级符号链接,其目标内容不受 ComfyUI 子模块 git 影响
- `ComfyUI\temp\`(真实目录,非链接):运行中生成的临时文件/预览图(如 `ComfyUI_temp_*.png`),可随时清理
- ⚠️ **`ComfyUI\input\`(用户上传)与 `output\`(生成结果)是真实数据:严禁删除、移动或批量清理**;只有 `temp\` 可清理

## 版本与运行

- conda 根:`C:\Users\zghyu\Miniconda3`(conda 不在 Git Bash 的 PATH;用 `conda activate` 或直接调 env 内 `python.exe`)
- **两个名称极易混淆的 conda 环境,均为 Python 3.13.14 / torch 2.13.0+cu130(CUDA 13.0,RTX 4060 8GB VRAM)**:
  - `ComfyUI`(2026-07-31 建,197 包)= **运行环境**,`start-comfyui.cmd` 与本文档均用它,路径 `miniconda3\envs\ComfyUI\python.exe`
  - `Comfy`(2026-08-07 建,199 包)= 同款基础上多 `onnxruntime-gpu 1.28.0`、`opencv-python 5.0.0.93`(其余仅依赖小版本差异),疑似备用/实验环境,勿混用
- 共享关键版本:comfyui-frontend-package **1.48.6**、comfyui-manager **4.2.2**、comfyui-workflow-templates **0.11.31**、sageattention **2.2.0**(cu130)、comfy-kitchen **0.2.26**、comfy-aimdo 0.4.13、transformers 4.57.3、diffusers 0.39.0、numpy 2.4.6、safetensors 0.8.0
- 前端打包目录(web_root,`server.py:251` 经 `FrontendManager.init_frontend()` 定位)= `<虚拟环境>/Lib/site-packages/comfyui_frontend_package/static/`(即 `C:\Users\zghyu\Miniconda3\envs\ComfyUI\Lib\site-packages\comfyui_frontend_package\static\`):主入口 `index.html`,打包产物在 `assets\`(421 个 `<分块名>-<hash>.js`,含 `core-*.js`/`api-*.js`/`index-*.js`),`scripts\` 保留 `app.js`/`api.js`/`domWidget.js` 等扩展 import 入口;插件 `web\js` 经 `GET /extensions`(`server.py:356`)运行时加载,**不参与前端打包**,重建 `assets\` 不影响扩展
- 测试插件「从零安装」是否正常时:需清理**浏览器缓存**的前端打包文件(即 `assets\` 下载到浏览器侧的 `-hash.js`/`-hash.css`),对 `http://127.0.0.1:8188` 强刷(`Ctrl+Shift+R`)或清除该站点数据,以验证扩展在无陈旧缓存的干净状态下能正常加载;**磁盘 `assets\` 目录勿删**(是前端真实构建产物,删了页面白屏/无法加载)
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

### ComfyUI 官方日志(排查插件/请求问题优先看这里)

- **官方日志文件**:`ComfyUI\user\comfyui.log`;多实例同时跑时按端口命名 `comfyui_<port>.log`(如 `comfyui_8188.log`);轮转保留 `comfyui.prev.log` / `comfyui.prev2.log`。启动时日志会打印一行 `** Log path: <路径>` 指明当前文件。
- **CLI 配置**:`--verbose LEVEL FILE` 可自定义控制台级别与文件输出(可重复),如 `--verbose INFO D:\Comfy\ComfyUI\user\comfyui_8188.log`;`--log-stdout` 把普通输出切到 stdout。
- **日志类别/格式**:行首 `[YYYY-MM-DD HH:MM:SS.mmm]` 时间戳,含级别(DEBUG/DETAIL/INFO/WARNING/ERROR/CRITICAL)。内容包括:启动信息(版本/设备/VRAM)、插件加载(`Import times for custom nodes`)、模型加载、报错 traceback、ComfyUI-Manager 网络操作,以及**自定义节点通过 `logging` 输出**的信息(插件里用 `print` 不一定进文件,建议用 `logging` 才稳定落盘)。
- **前端终端**:浏览器 ComfyUI 界面底部终端(经 WebSocket 推送的环形缓冲)也能实时看到同样的日志,排查前端扩展报错可直接看它。
- **注意**:`logs\comfyui*.log` 是用户自建重定向(如启动脚本),**不是官方位置**,可能缺部分输出;查不到关键日志时先看 `user\comfyui_<port>.log`。

## 模型与蓝图(2026-08-07 现状)

模型实际存放在 `models\` 下(`ComfyUI\models` 为软链接),当前合计约 178.7 GB。已就绪:

| 目录 | 已就绪 |
|------|--------|
| diffusion_models | `qwen_image_2512_fp8_e4m3fn`、`qwen_image_edit_2511_fp8mixed`、`flux-2-klein-9b-fp8`、`minimax_h3_fl2va_pruned_int8_convrot`、`minimax_h3_ref2va_pruned_int8_convrot` |
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

- 本地克隆 `docs\ComfyUI-Docs`(SSH,`main`,保持纯净);在线源码为 GitHub `Comfy-Org/docs`(内容规则详见该仓库,不在此展开)
- 分类文档已归档到 `backups\backup-20260805-路径清理\`(01-08 全量;05 含 Codex 协作约定与 Claude 协作约定两版)
- 专题资料:`webs\Bilibili\B站教程调研.md`(含 MiniMax H3 专题);`webs\RunningHub\RunningHub-API读取指南.md` + `API.md` + `workflows-list.md`

## 开发规范

- 项目根目录 `D:\Comfy` **本身是一个 git 仓库**(`main`),经 `.gitmodules` 登记 21 个子模块;根仓库跟踪的是各子模块的**指针提交**(`git ls-files -s` 中模式 `160000`)。不要误以为"根目录不是 git 仓库、不能在根目录执行 git 操作"
- 各子项目(ComfyUI 及全部插件、ComfyUI-Docs、MiniMax-H3 等)是根仓库的 git **子模块**:各自独立仓库、自身维护与上游一致。改动子模块代码在**子模块目录内**正常 commit/push,再回到根仓库 `git add <子模块路径>` 提交一次"指针更新";不要留着子模块脏工作树不提交,也不要往根仓库混入无关文件
- 修改 ComfyUI 主程序时遵守 `ComfyUI\AGENTS.md` 上游规范:改动小且直接、尽量少改文件、不引入新依赖、核心代码不发网络请求(见其 "No Internet Requests")、保持节点/API/工作流兼容、删除死代码、代码须看起来像手写
- 节点注册(V1 `NODE_CLASS_MAPPINGS` / V3 `comfy_entrypoint()`)与 ComfyUI API 使用约定见各插件仓库及 `ComfyUI\AGENTS.md`;代码书写规范(卫语句优先、switch 代替 if-else、缩进)与网络/代理策略见全局 `~/.claude\CLAUDE.md`

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
- 挑选/运行工作流:先核对「模型与蓝图」确认组件就位,再开 `blueprints\`、`templates\`(官方子目录 + 根目录个人归档 17 个)、`webs\Bilibili\工作流大全\`、`webs\RunningHub\workflows\` 的 json
- 清理临时输出残留:删 `temp\` 里 `ComfyUI_temp_*.png` 后,前端「资产 → 已生成」可能仍显示内容 —— 那是任务历史(`GET /history`)中的输出记录,文件已删但引用还在。清理:`POST /history` + `{"clear": true}` 全清(等价 `server.py` 的 `wipe_history()`),或 `{"delete": ["<prompt_id>", ...]}` 定向删除;验证 `GET /history` 归零,前端 F5 刷新。注:资产系统默认禁用(`--enable-assets` 才启用),任务历史是「已生成」面板唯一来源;清空前确认 history 输出均为 `temp` 类型(无 output/input 真实数据)

## 工作流布局规范(修改与创作必须遵守)

**布局目的**: 让工作流一眼可读、连线可追踪、节点群可辨识。以下三条为硬性要求, 修改或新建工作流时逐一自检。

1. **节点间距与不重叠**
   - 节点之间**严禁重叠**;
   - 相邻节点(横向或纵向相邻)之间边距 **20~50px(至少 20px, 最多 50px)**;
   - 对角线相隔较远的不算相邻, 不受 50px 上限限制(但也不得重叠、不得低于 20px)。

2. **连线走线(尽量直线)**
   - 连线**不允许大于 90 度的回折**(不出现走回头路/明显绕线的直角回弯);
   - 输出端口与对应输入端口**尽最大努力保持直线**: 同一功能链上的节点尽量同排/同列对齐, 让输出到下一输入基本水平(左→右)或垂直(上→下);
   - 避免长距离交叉串线; 有多个下游时优先保证主干直线。

3. **节点群按「正方向大区域」摆放**
   - 不同功能(加载器/采样/解码/后处理/条件)的节点群, 各自聚成**独立大区域**, 不要混排交错;
   - 整体流向保持**正向一致**: 模型/输入从左上或左侧进入, 处理链水平向右推进, 输出/保存落在右侧或右下;
   - 每个功能群内部节点紧凑对齐, 群与群之间留出明显空白带以区分。

**自检方法**: 重排后对全部节点做两两包围盒校验 —— 任一轴分离小于 20px 即判为过近/重叠, 超过 50px 视为间距过大, 均需调整。


## Git 提交规范

我的插件中, 严格按照 `git add .` `commit` 最后推送
项目根目录中, 严格按照 `git add .` `commit` 最后推送
子项目除了我的插件是我自己写的, 其它所有子项目不允许提交和修改代码, 或者推送
