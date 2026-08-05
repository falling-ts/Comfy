# Comfy — AI 驱动的 ComfyUI 全模态工作区

> 本仓库是一套开箱即用的 **ComfyUI 全模态工作区**:包含 ComfyUI 主程序、Seedance 2.0 视频生成、GGUF / KJNodes / 超分等自定义节点、图片/视频/音频工作流方案,以及模型目录规划。
>
> **核心思路:所有安装、配置、运行、出图、训练工作流,都交给 AI(OpenCode)来做。** 你只需要:装 Git → 克隆本仓库 → 装 OpenCode → 让它干活。

---

## 目录

- [这是什么](#这是什么)
- [开始之前](#开始之前)
- [第 1 步:安装 Git](#第-1-步安装-git)
- [第 2 步:克隆本项目](#第-2-步克隆本项目)
- [第 3 步:安装 OpenCode(桌面版)](#第-3-步安装-opencode桌面版)
- [第 4 步:以管理员身份运行 OpenCode,建立软连接](#第-4-步以管理员身份运行-opencode按软连接方案建立软连接)
- [第 5 步:让 OpenCode 装它自己的 CLI(可选)](#第-5-步让-opencode-装它自己的-cli可选)
- [第 6 步:让 OpenCode 安装其它 AI 工具(可选)](#第-6-步让-opencode-安装其它-ai-工具可选)
- [第 7 步:让 OpenCode 配置 Python 环境](#第-7-步让-opencode-配置-python-环境)
- [第 8 步:让 OpenCode 安装 ComfyUI 依赖并启动](#第-8-步让-opencode-安装-comfyui-依赖并启动)
- [第 9 步:之后一切都交给 AI](#第-9-步之后一切都交给-ai)
- [常见问题](#常见问题)
- [附录](#附录)

---

## 这是什么

- **ComfyUI 主程序**(`ComfyUI\`,dev 分支,v0.30.0)—— 本地节点式 AI 图像/视频/音频生成引擎
- **自定义节点**(经 `ComfyUI\custom_nodes\` 软链接加载):
  - `ComfyUI-FallingTS` —— Seedance 2.0 视频生成(首尾帧 / 多模态参考,走火山引擎 API)
  - `ComfyUI-GGUF` —— GGUF 量化模型加载
  - `ComfyUI-KJNodes` —— 大型工具节点包
  - `ComfyUI_UltimateSDUpscale` —— 分块重绘放大
- **工作流方案**:图片 8 + 音频 6 + 视频 6(见[附录 B](#附录-b工作流方案总览))
- **模型目录**(`models\`,软链接到项目根)—— 见[附录 C](#附录-c模型下载清单)
- **文档**:官方文档本地克隆 `ComfyUI-Docs\`;工作区说明 `AGENTS.md`

---

## 开始之前

- **系统**:Windows 10/11(推荐;本文以 Windows 为准)
- **硬件**:内存 16G 以上;**有 NVIDIA 显卡**(N 卡)体验最佳;无 N 卡也能跑,但慢
- **网络**:能访问外网即可;部分地区需代理;国内下载模型可用 `hf-mirror.com` 镜像(见附录 E)
- **你不需要提前装任何东西**——Python、CUDA、Miniconda、各种 CLI 都由 AI 帮你装

---

## 第 1 步:安装 Git

Git 用于克隆本仓库、后续管理子项目。

1. 浏览器打开 **https://git-scm.com/download/win**,下载安装包(64-bit),一路「下一步」默认安装即可
2. 验证:按 `Win` 键,搜索并打开「Git Bash」,输入:

```bash
git --version
```

能打印出版本号即成功。

---

## 第 2 步:克隆本项目

在 Git Bash 里执行:

```bash
git clone https://github.com/falling-ts/Comfy
cd Comfy
```

完成后,你会得到一个包含 `ComfyUI\`、各 `ComfyUI-*\` 插件、`workflows\`、`models\` 的完整工作区。**后续所有操作都在这个 `Comfy` 目录里进行。**

> 提示:克隆后 `models\` 是空的(模型体积大,不随仓库分发),需要按[附录 C](#附录-c模型下载清单)下载;`media\` 是空的,是输入/输出文件的家。

---

## 第 3 步:安装 OpenCode(桌面版)

OpenCode 是你和这套工作区之间的 AI 主力,负责装软件、配环境、跑工作流。

1. 浏览器打开 **https://opencode.ai/zh/download** ,下载「**桌面端**」
2. 安装并启动 OpenCode
3. 在左侧「**添加项目**」,选择刚才克隆的 `Comfy` 目录
4. 之后在这个项目里和 AI 对话即可

---

## 第 4 步:以管理员身份运行 OpenCode,按软连接方案建立软连接

> ⚠️ **很重要**:本工作区依赖「相对路径符号链接」,把 `ComfyUI\` 里的相关目录指向项目根(`models\`、`media\`、`workflows\`、各插件目录)。**创建符号链接需要管理员权限,所以必须以管理员身份运行 OpenCode。**

1. 在开始菜单找到 OpenCode,右键 →「**以管理员身份运行**」
2. 打开本项目(添加 `Comfy` 目录),把下面这段话发给它:

> 请按以下「软连接方案」检查并修复本项目的软链接(全部用**相对路径**符号链接):
>
> 1. 先确认 `ComfyUI\` 下这些路径里哪些是**真实目录**(不是链接):`custom_nodes\ComfyUI_UltimateSDUpscale`、`custom_nodes\ComfyUI-GGUF`、`custom_nodes\ComfyUI-KJNodes`、`custom_nodes\ComfyUI-FallingTS`、`input`、`output`、`models`,以及 `user\default\workflows`;
> 2. 把这些**真实目录删除**(若已是链接则跳过),再逐个建立相对路径符号链接,目标指向项目根目录:
>    - `ComfyUI\custom_nodes\ComfyUI_UltimateSDUpscale` → `..\..\ComfyUI_UltimateSDUpscale`
>    - `ComfyUI\custom_nodes\ComfyUI-GGUF` → `..\..\ComfyUI-GGUF`
>    - `ComfyUI\custom_nodes\ComfyUI-KJNodes` → `..\..\ComfyUI-KJNodes`
>    - `ComfyUI\custom_nodes\ComfyUI-FallingTS` → `..\..\ComfyUI-FallingTS`
>    - `ComfyUI\input` → `..\media`
>    - `ComfyUI\output` → `..\media`
>    - `ComfyUI\models` → `..\models`
>    - `ComfyUI\user\default\workflows` → `..\..\..\workflows`
> 3. 全部完成后,用 `dir` 或资源管理器确认这些路径显示为「符号链接」,并验证 `ComfyUI\models\diffusion_models` 等子目录可正常进入。
>
> 注意:只能删除上面列出的真实目录;`ComfyUI\temp\` 等真实目录保留;所有链接一律用相对路径,保证整个项目文件夹移动后不失效。

3. 软链接就绪后,继续[第 5 步](#第-5-步让-opencode-装它自己的-cli可选)。

---

## 第 5 步:让 OpenCode 装它自己的 CLI(可选)

如果你更习惯在命令行里用 OpenCode,直接对它说:

> 帮我安装 opencode cli 版本,具体下载安装,你从网络搜索。

它会在你的终端里装好 `opencode` 命令,以后 `cd Comfy && opencode` 即可使用。

---

## 第 6 步:让 OpenCode 安装其它 AI 工具(可选)

继续以 OpenCode 为基地,让它帮你把常用的 AI CLI 都装上(这样你可以随时切换):

> 帮我安装以下 AI 工具:codex、claude code、cc-switch。具体下载安装,你从网络搜索。

- **codex** —— OpenAI 的 AI 编码 CLI
- **claude code** —— Anthropic 的 AI 编码 CLI
- **cc-switch** —— AI CLI 配置切换工具(在多个服务商之间一键切换)

---

## 第 7 步:让 OpenCode 配置 Python 环境

把这段话发给 OpenCode(让它先装 Miniconda,再建 ComfyUI 专用环境):

> 帮我安装 miniconda,并初始化一个名为 ComfyUI 的 conda 环境(python 3.13)。具体下载安装,你从网络搜索。
>
> 注意:环境名必须是 `ComfyUI`(不是 ConfyUI),后面所有依赖都装进这个环境,不要用系统 Python。

完成后验证(它会在终端里执行):

```powershell
conda activate ComfyUI
python --version
```

---

## 第 8 步:让 OpenCode 安装 ComfyUI 依赖并启动

把这段话发给 OpenCode(它会依次完成:装 CUDA 版 PyTorch → 装主程序依赖 → 装各插件依赖 → 启动):

> 进入 `ComfyUI` 目录,按顺序:
>
> 1. **先装 CUDA 版 PyTorch**:执行
>    `pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu130`
>    (先检测我的 NVIDIA 显卡和驱动支持哪个 CUDA 版本,选择匹配的 `cuXXX`;若没有 N 卡则装 CPU 版)
> 2. 再装剩余依赖:`pip install -r requirements.txt`
> 3. 然后进入其它 `ComfyUI-*` 相关目录(`ComfyUI-GGUF`、`ComfyUI-KJNodes`、`ComfyUI-FallingTS`、`ComfyUI_UltimateSDUpscale`、`ComfyUI-Docs`),逐个检查各自需要的依赖(如各自的 `requirements.txt` 或 README),都帮我安装好。
> 4. 最后回到 `ComfyUI` 目录启动:`python main.py --enable-manager`
>
> 启动成功后告诉我前端地址。

启动后,浏览器打开 **http://127.0.0.1:8188** 即是 ComfyUI 前端界面。

---

## 第 9 步:之后一切都交给 AI

环境就绪后,所有工作都可以让 AI 帮你做:

- 下载模型(按[附录 C](#附录-c模型下载清单),直接说"下载 xx 模型到 models\yyy\")
- 运行 / 修改 / 新建工作流(在 `workflows\` 里)
- 安装新自定义节点、排错、调参、出图、训练
- 视频/音频/图片生成(Seedance、MiniMax、Stable Audio、Qwen 系列等)

一句话总结:**你负责"想要什么",AI 负责"怎么做"。**

---

## 常见问题

- **代理 / 下载慢**:默认直连;失败时用本机代理(如 Clash 的 `127.0.0.1:7890`);HuggingFace 模型国内可用 `hf-mirror.com` 镜像,把链接前缀 `huggingface.co` 换成 `hf-mirror.com` 即可(见附录 E)
- **Windows 软链接**:`custom_nodes\` 下的插件和 `models\` 等使用相对路径符号链接。创建链接需要管理员权限,推荐**以管理员身份运行 OpenCode**再让它修复(见[第 4 步](#第-4-步以管理员身份运行-opencode按软连接方案建立软连接));或手动开启「开发者模式」(设置 → 隐私和安全性 → 开发者选项 → 开启开发者模式)
- **显存不足**:Klein 9B 蒸馏版较吃显存(24G 卡跑 1024 tile 偏紧,爆显存降到 768);MiniMax H3 需大显存,低显存建议用量化版或云端(详见附录 C 备注)
- **模型放好后记得重启 ComfyUI**,加载节点才会识别新模型

---

# 附录

## 附录 A · 项目结构

```
Comfy/
├── ComfyUI/                  # ComfyUI 主程序(dev 分支)
│   ├── main.py               # 启动入口(python main.py --enable-manager)
│   ├── custom_nodes/         # 自定义节点(软链接 → ../各插件目录)
│   ├── input/  output/       # 输入/输出(软链接 → ../media)
│   └── models/               # 模型(软链接 → ../models)
├── ComfyUI-GGUF/             # GGUF 量化模型节点
├── ComfyUI-KJNodes/          # KJNodes 工具节点包
├── ComfyUI-FallingTS/        # Seedance 2.0 视频生成节点(火山引擎 API)
├── ComfyUI_UltimateSDUpscale/ # 分块重绘放大
├── ComfyUI-Docs/             # 官方文档本地克隆(只读参考)
├── workflows/                # 用户工作流(图片/视频/音频)
├── models/                   # 模型实际存放处(按子目录分类)
├── media/                    # 输入图片/音频 + 生成结果
├── Templates/  Bilibili/  RunningHub/   # 官方模板 + 调研资料
└── AGENTS.md                 # 工作区说明(供 AI 读取)
```

## 附录 B · 工作流方案总览

### 图片类(8 个,模型已全部就绪)

| # | 工作流 | 核心模型 |
|---|--------|---------|
| 1 | 文生图 T2I(928×1664 竖版) | Qwen-Image-2512 |
| 2 | 参考图生图 I2I(风格/角色参考) | FLUX.2 Klein 9B |
| 3 | 图片指令修改(换装/换背景/改元素) | Qwen-Image-Edit 2511 |
| 4 | 图片四周扩大 Outpaint | Qwen-Edit 2511 + Klein 9B + LaMa 预填充(可选) |
| 5 | 图片中心放大/局部重绘 Inpaint | Klein 9B + 掩码(手动/SAM3) |
| 6 | 物体移除 | Klein 9B + 掩码扩张 |
| 7 | 图片放大/超清(3~4 倍,8 整除) | 4x-UltraSharp |
| 8 | 三视图/多角度生成 | Qwen-Edit 2511 + 多角度 LoRA |

### 音频类(6 个)

| # | 工作流 | 核心模型 | 状态 |
|---|--------|---------|------|
| 1 | 音乐/歌曲生成 | ACE-Step 1.5(内置 nodes_ace;低显存可选 split 版) | 需下载 |
| 2 | 背景音乐/纯器乐 | Stable Audio 3 | **已就绪** |
| 3 | 环境音/音效 | Stable Audio 3(SFX/One-shot 类别) | **已就绪** |
| 4 | 情绪语音生成(8 种情绪) | Qwen3-TTS(情感标签);备用 IndexTTS-2 | 需下载 |
| 5 | 人物说话·参考音色克隆 | Qwen3-TTS 声音克隆(3s 参考音频+情绪标签/指令) | 需下载 |
| 6 | 多角色对话/混音 | Qwen3-TTS RoleBank+AdvancedDialogue | 需装插件 |

### 视频类(6 个,MiniMax H3)

文生视频 T2V / 图生视频 I2V / 首帧参考 / 首尾帧 / 多图参考 / 图像+音频参考 —— 全部需下载模型(见附录 C)。

## 附录 C · 模型下载清单

> 方案原则:全开源、本地推理、零 API 费用。模型统一放 `models\` 对应子目录。下载大文件建议走镜像(附录 E),或让 AI 帮你下载。

### 图片类

| 模型 | 放置目录 | 状态 | 下载地址 |
|------|---------|------|---------|
| `qwen_image_2512_fp8_e4m3fn.safetensors` | `models\diffusion_models\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors> |
| `qwen_image_edit_2511_bf16.safetensors` | `models\diffusion_models\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors> |
| `flux-2-klein-9b-fp8.safetensors` | `models\diffusion_models\` | ✅ 已就绪 | <https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-fp8/resolve/main/flux-2-klein-9b-fp8.safetensors> ⚠️门控 |
| `qwen_3_8b_fp8mixed.safetensors`(Klein 文本编码器) | `models\text_encoders\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/flux2-klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors> |
| `full_encoder_small_decoder.safetensors`(Klein/FLUX.2 解码器) | `models\vae\` | ✅ 已就绪 | <https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/resolve/main/full_encoder_small_decoder.safetensors> |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors`(Qwen-Edit 文本编码器) | `models\text_encoders\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors> |
| `qwen_image_vae.safetensors` | `models\vae\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors> |
| `4x-UltraSharp.pth`(放大,已验证可下) | `models\upscale_models\` | ✅ 已就绪 | <https://huggingface.co/lokCX/4x-Ultrasharp/resolve/main/4x-UltraSharp.pth> |
| `sam3.1_multiplex_fp16.safetensors`(自动掩码,可选) | `models\checkpoints\` | ⬇️ 可选 | <https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors> |
| LaMa/MAT 预填充(可选,装 Acly ComfyUI-Inpaint-Nodes 后) | 插件自动下载 | ⬇️ 可选 | 随 [ComfyUI-Inpaint-Nodes](https://github.com/Acly/ComfyUI-Inpaint-Nodes) 安装 |

### 音频类

| 模型 | 放置目录 | 状态 | 下载地址 |
|------|---------|------|---------|
| `stable_audio_3_medium.safetensors` | `models\checkpoints\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/stable-audio-3/resolve/main/checkpoints/stable_audio_3_medium.safetensors> |
| `t5gemma_b_b_ul2.safetensors`(StableAudio 文本编码器) | `models\text_encoders\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/stable-audio-3/resolve/main/text_encoders/t5gemma_b_b_ul2.safetensors> |
| `ace_step_1.5_turbo_aio.safetensors`(音乐/歌曲) | `models\checkpoints\` | ⬇️ 需下载 | <https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/checkpoints/ace_step_1.5_turbo_aio.safetensors> |
| ACE-Step 1.5 split 版(低显存替代 AIO) | `diffusion_models`+`text_encoders`+`vae` | ⬇️ 可选 | `acestep_v1.5_turbo.safetensors` + `qwen_0.6b_ace15`(歌词质量选 `qwen_4b_ace15`)+ `ace_1.5_vae.safetensors`,均见 <https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files> |
| Qwen3-TTS-12Hz-1.7B-Base(万能:克隆+对话,工作流 ④⑤⑥ 默认,~4.5 GB) | 插件自动下载至 `models/TTS/Qwen/` | ⬇️ 需下载 | <https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base> |
| Qwen3-TTS-12Hz-1.7B-CustomVoice(9 预设音色,~4.5 GB) | 同上 | ⬇️ 可选 | <https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice> |
| Qwen3-TTS-12Hz-1.7B-VoiceDesign(自然语言造声,~4.5 GB) | 同上 | ⬇️ 可选 | <https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign> |
| Qwen3-TTS-12Hz-0.6B-Base(低显存克隆,约 4GB VRAM,~2.5 GB) | 同上 | ⬇️ 可选 | <https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base> |
| Qwen3-TTS-12Hz-0.6B-CustomVoice(低显存预设音色,~2.5 GB) | 同上 | ⬇️ 可选 | <https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice> |
| SenseVoiceSmall(ASR 自动转写参考文本,工作流 ⑤ 必需,~0.9 GB) | 插件自动下载 | ⬇️ 需下载 | <https://huggingface.co/FunAudioLLM/SenseVoiceSmall> |

> **Qwen3-TTS 下载说明**:均为**目录型模型**,必须整目录下载(`config.json`/`tokenizer` 词表/`speech_tokenizer/` 等,仅下 safetensors 无法加载)。推荐直接开 `Qwen3TTSLoader` 的 `auto_download`(默认开),插件自动从 ModelScope 整目录快照下载并自动建目录;**手动下载**时按以下结构放入(`models/` 是软链接,实际落点 `D:\Comfy\models\`):
>
> ```
> models/TTS/Qwen/Qwen3-TTS-12Hz-1.7B-Base/          ← 5 个 Qwen3-TTS 模型都放 TTS/Qwen/ 下
> models/TTS/Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice/
> models/TTS/Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign/
> models/TTS/Qwen/Qwen3-TTS-12Hz-0.6B-Base/
> models/TTS/Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice/
> models/TTS/SenseVoiceSmall/                        ← SenseVoice 直接放 TTS/ 下,无 Qwen 子目录
> ```
| IndexTTS-2 全套(情绪语音备用,含 gpt/s2mel/bigvgan 等,~5 GB) | TTS-Audio-Suite 目录 | ⬇️ 可选 | <https://huggingface.co/IndexTeam/IndexTTS-2>(镜像 [AEmotionStudio/index-tts-2-models](https://huggingface.co/AEmotionStudio/index-tts-2-models)) |
| F5-TTS(参考音色克隆备用,最快零样本) | TTS-Audio-Suite 目录 | ⬇️ 可选 | <https://huggingface.co/SWivid/F5-TTS> |
| CosyVoice3(跨语言克隆,可选) | TTS-Audio-Suite 目录 | ⬇️ 可选 | 随 [TTS-Audio-Suite](https://github.com/diodiogod/TTS-Audio-Suite) 文档 |
| `qwen3.5_2b_bf16.safetensors`(音频编码) | `models\text_encoders\` | ✅ 已就绪 | <https://huggingface.co/Comfy-Org/Qwen3.5/resolve/main/text_encoders/qwen3.5_2b_bf16.safetensors> |

### 视频类(MiniMax H3,Comfy-Org/MiniMax-H3 仓库)

| 模型 | 放置目录 | 状态 | 下载地址 |
|------|---------|------|---------|
| `minimax_h3_fl2va_pruned_int8_convrot.safetensors`(FL2VA,T2V/I2V 用) | `models\diffusion_models\` | ⬇️ 需下载 | <https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors> |
| `minimax_h3_ref2va_pruned_int8_convrot.safetensors`(Ref2VA,**R2V 参考生视频用,独立文件**) | `models\diffusion_models\` | ⬇️ 需下载 | <https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors> |
| `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors`(文本编码器) | `models\text_encoders\` | ⬇️ 需下载 | <https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors> |
| `minimax_h3_video_vae_fp16.safetensors`(视频 VAE) | `models\vae\` | ⬇️ 需下载 | <https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_fp16.safetensors> |
| `minimax_h3_audio_vae_fp32.safetensors`(音频 VAE) | `models\vae\` | ⬇️ 需下载 | <https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors> |

> **fl2va 与 ref2va 是同一基座的任务变体**:`视频-01 文生视频` 用 fl2va,`视频-02/03/04`(首帧/首尾帧/参考图音视频)用 ref2va,两者都要下。仓库另有 bf16/int8_convrot/pruned_fp8_scaled 档可选。

### MiniMax H3 加速方案(社区现状)

| 方案 | 提速 | 做法 | 代价 |
|------|------|------|------|
| Sage Attention | +20~30% | KJNodes `Patch Sage Attention KJ` 节点(已有 KJNodes) | 无害 dtype 警告 |
| EasyCache | 显著 | 参数 0.30/0.20/0.90 | 失帧/模糊,长视频连贯性下降 |
| GGUF 量化 | 显存↓ | `qwen3vl-32B-MiniMax-H3-Q4_K.gguf`(Q2 效果差) | 社区有分歧,需 A/B |
| INT4 文本编码器 | 显存↓ | 替代 nvfp4_awq | 更小可用 |
| 显存优化 | 防 OOM | `🎈VRAM/RAM-Cleanup` 节点;启动 `--fast-disk`、`--vram-headroom` | 编码器频繁重载 |
| Lightning 蒸馏 LoRA | 未来 | 尚未发布,等社区蒸馏 | — |

**低显存**:8G/12G/16G 均可跑(动态卸载,clip 编码器放 CPU);本地最高 768p,2K 需官方 API。

## 附录 D · 需安装的插件

| 插件 | 用途 | 地址 |
|------|------|------|
| ComfyUI-Qwen3-TTS | 开源 TTS 主方案(克隆/音色设计/情绪标签/无限多角色对话,Apache-2.0) | <https://github.com/wanaigc/ComfyUI-Qwen3-TTS> |
| TTS-Audio-Suite(可选备用) | IndexTTS-2/F5-TTS/CosyVoice3(情绪/克隆/SRT) | <https://github.com/diodiogod/TTS-Audio-Suite> |
| ComfyUI-Inpaint-Nodes(可选) | LaMa/MAT 预填充、ColorMatch 接缝修复 | <https://github.com/Acly/ComfyUI-Inpaint-Nodes> |
| ComfyUI-Angelo(可选) | Klein 点击式编辑(2026 趋势) | <https://github.com/shootthesound/ComfyUI-Angelo> |

## 附录 E · 网络与镜像

- **默认直连外网**;直连失败(超时/403/TLS 被掐)时,改用本机代理,如 Clash Verge 混合端口 `127.0.0.1:7890`(HTTP 与 SOCKS5 均可)
- **HuggingFace 国内镜像**:把下载链接前缀 `huggingface.co` 换成 `hf-mirror.com` 即可,例:
  `https://hf-mirror.com/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_fp16.safetensors`
- 部分站点(如 OpenAI 系域名)直连会被 Cloudflare 拦截,需走允许对应域名的代理节点

## 附录 F · 注意事项

- **门控仓库**:`black-forest-labs/FLUX.2-klein-9b-fp8` 需登录 HF 并接受 BFL 协议
- **显存**:Klein 9B 蒸馏版占用较高(24G 卡跑 1024 tile 偏紧,爆显存时降到 768);MiniMax H3 需大显存,低显存建议量化或云端
- **下载顺序建议**:先补音频小件(ACE-Step、Qwen3-TTS)→ 视频大件(MiniMax H3 全套 5 文件,fl2va 与 ref2va 都要下)
- **模型放好后重启 ComfyUI**;`stable_audio_3_medium` + `t5gemma` 就绪后,背景音乐工作流可立即运行
