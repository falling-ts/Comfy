# Qwen-Image-Edit 多镜头插件 与 多视角 LoRA 模型 TOP10(2026-08-09)

调研日期:2026-08-09(数据实时)。数据来源:GitHub Search API(按 star) + HuggingFace API(按下载量,走代理核验)。

主题:Qwen-Image-Edit(Qwen-Image-Edit-2511 / 2509)的**多镜头/相机角度控制**插件,以及**多视角(Multiple-Angles)LoRA**模型。核心实现 = `ComfyUI-qwenmultiangle` 节点 + `Multiple-Angles-LoRA`,提供 96 种相机机位(距离 × 方位角 × 俯仰角)交互式控制。

---

## A. GitHub 插件 / 项目 TOP10(多镜头 / 多角度控制)

| 排名 | 仓库 | ⭐ | 说明 | 访问地址 |
|------|------|----|------|------|
| 1 | **jtydhr88/ComfyUI-qwenmultiangle** | 1305 | **ComfyUI 多角度控制主力插件**:Three.js 3D 交互式相机角度控制节点,拖拽控制 96 种机位,自动生成多角度提示词,兼容 Qwen-Image-Edit 2511/2509 + Multiple-Angles-LoRA | https://github.com/jtydhr88/ComfyUI-qwenmultiangle |
| 2 | **ShuaixinHuang/image-multiple-angles-3d-camera** | 265 | 3D 相机控制原始实现(Gradio 应用 / HF Space):拖拽手柄切换 96 种摄像机角度,Multiple-Angles-LoRA 的原配套 UI | https://github.com/ShuaixinHuang/image-multiple-angles-3d-camera |
| 3 | PRITHIVSAKTHIUR/Qwen-Image-Edit-2511-LoRAs-Fast-Lazy-Load | 118 | 2511 LoRA 懒加载(Fast/Lazy Load)演示,多 LoRA 组合加载 | https://github.com/PRITHIVSAKTHIUR/Qwen-Image-Edit-2511-LoRAs-Fast-Lazy-Load |
| 4 | amrrs/qwenmultiangle | 100 | 基于 **fal.ai API** 的多角度生成 UI,免本地显卡 | https://github.com/amrrs/qwenmultiangle |
| 5 | camilocbarrera/-Qwen-Image-Edit-2511-Multiple-Angles-Playground | 23 | 2511 多角度 3D 相机控制 Playground | https://github.com/camilocbarrera/-Qwen-Image-Edit-2511-Multiple-Angles-Playground |
| 6 | PRITHIVSAKTHIUR/Qwen-Image-Edit-2511-LoRAs-Fast-Multi-Image-Rerun | 11 | 2511 多图快速重跑演示(懒加载) | https://github.com/PRITHIVSAKTHIUR/Qwen-Image-Edit-2511-LoRAs-Fast-Multi-Image-Rerun |
| 7 | varshith15/Qwen-Image-2509-MultipleAngles | 11 | 2509 版多角度生成参考 | https://github.com/varshith15/Qwen-Image-2509-MultipleAngles |
| 8 | hashms0a/ComfyUI-Qwen-Multi-Angle-Camera-Nodes | 9 | 面向 2511-Multiple-Angles-LoRA 的 ComfyUI 相机角度控制节点 | https://github.com/hashms0a/ComfyUI-Qwen-Multi-Angle-Camera-Nodes |
| 9 | PRITHIVSAKTHIUR/Qwen-Image-Edit-3D-Lighting-Control | 9 | 3D **光照控制**演示(与多角度互补) | https://github.com/PRITHIVSAKTHIUR/Qwen-Image-Edit-3D-Lighting-Control |
| 10 | tomosud/qwen-image-multiple-angles-3d-camera_lowspec | 7 | 3D 相机控制的 Windows 低配(12GB 显存)版 | https://github.com/tomosud/qwen-image-multiple-angles-3d-camera_lowspec |

---

## B. HuggingFace 多视角 LoRA 模型 TOP10(按下载量)

| 排名 | 模型 | 下载 | 赞 | 对应版本 | 下载地址 |
|------|------|------|----|------|------|
| 1 | **dx8152/Qwen-Edit-2509-Multiple-angles** | 224,135 | 964 | 2509(下载量最高) | https://huggingface.co/dx8152/Qwen-Edit-2509-Multiple-angles |
| 2 | **fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA** | 57,660 | 1,498 | 2511(点赞最高,官方配套) | https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA |
| 3 | dx8152/Qwen-Edit-2509-Multi-Angle-Lighting | 5,298 | 168 | 2509(多角度+灯光) | https://huggingface.co/dx8152/Qwen-Edit-2509-Multi-Angle-Lighting |
| 4 | wan-world/Qwen-Image-Edit-2511-Multiple-Angles-LoRA | 1,523 | 1 | 2511(社区复刻) | https://huggingface.co/wan-world/Qwen-Image-Edit-2511-Multiple-Angles-LoRA |
| 5 | zachyuan/Qwen-Image-Edit-2511-Multiple-Angles-LoRA | 860 | 7 | 2511 | https://huggingface.co/zachyuan/Qwen-Image-Edit-2511-Multiple-Angles-LoRA |
| 6 | stronman/Qwen-Image-Edit-2511-Multiple-Angles-LoRA | 457 | 1 | 2511 | https://huggingface.co/stronman/Qwen-Image-Edit-2511-Multiple-Angles-LoRA |
| 7 | 0k-t0/Qwen-Image-Edit-2511-Multiple-Angles-LoRA | 300 | 0 | 2511 | https://huggingface.co/0k-t0/Qwen-Image-Edit-2511-Multiple-Angles-LoRA |
| 8 | AdversaLLC/Qwen-Image-Edit-2511-Multiple-Angles-LoRA | 176 | 1 | 2511 | https://huggingface.co/AdversaLLC/Qwen-Image-Edit-2511-Multiple-Angles-LoRA |
| 9 | ScottzillaSystems/qwen-image-edit-plus-nsfw-lora | 55,038 | 85 | 2511(NSFW,非多角度) | https://huggingface.co/ScottzillaSystems/qwen-image-edit-plus-nsfw-lora |
| 10 | strangerzonehf/Qwen-Image-Edit-LoRA-Collection | 1,781 | 31 | 多 LoRA 合集(含多角度等) | https://huggingface.co/strangerzonehf/Qwen-Image-Edit-LoRA-Collection |

> 说明:第 9/10 为非多角度类别(NSFW / 合集),一并列出作参考;多角度专项以第 1-8 为准。

---

## C. 关键模型直接下载地址(直链)

### 最推荐:Qwen-Image-Edit-2511 + Multiple-Angles-LoRA(本地 ComfyUI)
- **模型文件**(~LoRA,放 `models/loras/`):
  https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA/resolve/main/qwen-image-edit-2511-multiple-angles-lora.safetensors
- **配套 ComfyUI 工作流**:`comfyui-workflow-multiple-angles.json`(同上仓库 `resolve/main/comfyui-workflow-multiple-angles.json`)
- **模型页**:https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA

### 下载量最高:Qwen-Edit-2509 多角度
- 模型文件:仓库内文件名 `镜头转换.safetensors`
  https://huggingface.co/dx8152/Qwen-Edit-2509-Multiple-angles/resolve/main/%E9%95%9C%E5%A4%B4%E8%BD%AC%E6%8D%A2.safetensors
- 配套工作流:`Qwen-Edit-2509-多角度切换.json`
- 模型页:https://huggingface.co/dx8152/Qwen-Edit-2509-Multiple-angles

### 多角度 + 灯光:Qwen-Edit-2509 Multi-Angle-Lighting
- 文件:`多角度灯光-251121.safetensors`(最新)/ `多角度灯光-251116.safetensors`(旧)
- 模型页:https://huggingface.co/dx8152/Qwen-Edit-2509-Multi-Angle-Lighting

---

## D. 使用与部署

**ComfyUI 本地(推荐)**:
1. 装插件:`git clone https://github.com/jtydhr88/ComfyUI-qwenmultiangle` 到 `ComfyUI/custom_nodes/`,重启;
2. 下载 2511 LoRA(`qwen-image-edit-2511-multiple-angles-lora.safetensors`)→ `models/loras/`;
3. 加载 `comfyui-workflow-multiple-angles.json`,节点上拖拽手柄即可生成 96 种相机角度(距离/方位/俯仰)。

**在线(免显卡)**:amrrs/qwenmultiangle(fal.ai API)或 HF Space(ShuaixinHuang/image-multiple-angles-3d-camera)。

**版本提示**:
- 2511 用 `fal/...2511-Multiple-Angles-LoRA`,2509 用 `dx8152/...2509-Multiple-angles`;LoRA 需与基座版本匹配,混用易出问题;
- 2509 多角度灯光(`Multi-Angle-Lighting`)与 2511 多角度可叠加,但灯光控制节点为另一插件(见 GitHub 第 9 条)。
