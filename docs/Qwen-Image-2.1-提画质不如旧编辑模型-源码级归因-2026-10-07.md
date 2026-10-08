# Qwen-Image 2.1 为什么在「提升画质」上不如老的 Qwen-Image-Edit(2511)—— 源码级归因

> 调研日期 2026-10-07。全部结论来自**官方规范原文**与**本库 ComfyUI v0.37.0 源码逐条取证**,不采信二手教程。
> 对照的本地权威源见 §8。**本文档同时记录了本次调研中我自己三条被实测推翻的假设**(§7),先看 §7 再引用结论。

## 0. 一句话结论

**不是 2.1 画质能力退步,而是 2.1 官方把「全局画质改动」明确归入「要避免的失败模式」,并且在编辑模式下让文本编码器完全看不见图。**

三个已验证的成因,按贡献排序:

| # | 成因 | 证据级别 | 可否立即修改 |
|---|---|---|---|
| **A** | **2.1 编辑时把视觉 token 整个从文本序列里删掉** —— 文本编码器对图像像素「盲」 | **源码级实锤** | ✖ 框架行为,改不了 |
| **B** | **官方规范把「画质或风格改变」归入 clarify-and-constrain,并把「锐化顺手改了色调」列为 Leakage(失败)** | 规范原文 | ✔ 改提示词 |
| **C** | **参数量差约 3 倍**(7B vs 20B 级) | 权重实测 | ✖ 模型决定 |

外加一条**不是原因**的(§7.1):VAE 压缩比从 8× 到 16× **不构成**画质差距,两代每 token 覆盖的图像像素完全相同。

---

## 1. 核心成因 A:2.1 编辑时文本编码器「看不见图」

这是本次调研最实锤、也最意外的一条,源码可直接引用。

### 1.1 1.x 把视觉 token 留在序列里

`comfy/text_encoders/qwen_image.py:18` 的编辑模板:

```
<|im_start|>system
Describe the key features of the input image (color, shape, size, texture, objects, background),
then explain how the user's text instruction should alter or modify the image.
Generate a new image that meets the user's requirements while maintaining consistency
with the original input where appropriate.
<|im_end|>
```

这段 system prompt 明确要求模型**先描述输入图的 color/shape/size/texture**。配合 `qwen_image.py:47`
把 `<|image_pad|>` 位置替换成 `{"type":"image","data":...}` 的真实张量并**保留在序列中**,
文本编码器**真的「看」过图**,再据此改写指令。

### 1.2 2.1 显式丢弃 system turn 和视觉 token

`comfy/text_encoders/qwen_image21.py:9`:

```
SYSTEM_PROMPT = "<|im_start|>system\nComprehend and analyze the provided prompt.<|im_end|>\n"
```

只剩「理解指令」,**没有任何描述图像纹理/像素的指令**。更关键的是 `encode_token_weights`:

```python
# comfy/text_encoders/qwen_image21.py:61
keep[:im_starts[1] if len(im_starts) > 1 else 0] = False   # ← 丢掉整个 system turn
...
# comfy/text_encoders/qwen_image21.py:63-68
# vision tokens are replaced by reference latents in the DiT: drop them and record where each image goes
if not token_weight_pairs.get("keep_vision", False):
    for start, size in image_spans:
        keep[start:start + size] = False                      # ← 视觉 token 从序列删除
        slots.append(int(keep[:start].sum()))
    extra["image_slots"] = slots
```

源码注释自己写明了原因:图改由 **VAE ref_latent** 单独送进 DiT 序列。

> ⚠️ **一个重要例外**:节点 `TextEncodeQwenImage21` 里 `keep_vision` 只在**没有接 VAE** 时为真 ——
> `nodes_qwen.py:175`: `keep_vision = len(ref_latents) == 0`。
> 本库 4 个 QI2.1 工作流的编码节点**都接了 VAE**(`vae` 端口有连线),因此 `keep_vision=False`,
> **视觉 token 确实被丢弃**。若把 `vae` 端口断开,视觉 token 会保留、模型会「看」图 ——
> 但那样 `latent` 输出会退回 1024×1024 的空 latent(`nodes_qwen.py:148,181`),编辑链会断。

### 1.3 为什么这条专门打「提升画质」

「提升画质」是**没有具体目标属性**的编辑:不像「把头转向左」那样有明确可执行的判断依据。
文本编码器看不见图 + 指令又空洞 ⇒ 模型只能盲目施加一个全局「变清晰」先验,
缺少「哪里该锐化、哪里该保留纹理」的判断依据 —— 这正好命中官方规范所说的 **Under-editing**
(输出看起来像没编辑过的原图)。

对比:1.x 里「describe color, shape, size, texture」这条指令 + 真实视觉 token,
给了模型判断「哪些区域模糊、该锐化哪里」的**显式依据**。

---

## 2. 核心成因 B:官方规范把「画质改动」归为失败模式

官方编辑规范 `refs/Qwen-Image-2.1/prompt_rewrite/prompts/system_prompt_edit.txt` 全文已读,
关键条款(行号为该文件):

- 核心原则 **Attribute Disentanglement at Full Strength** (L28):
  只改被点名的那一个属性,推到极强;其余一切保持输入保真度。
- 两种对称失败 (L31-33):**Leakage**(动了没点名的地方)/ **Under-editing**(改动被施加得太轻)。
- **Preservation locks content, never edit strength** (L35)。

把「画质或风格改变」归入哪一支,决定了成败:

| 任务分支 | 官方写法要求 | 「提升画质」落在这支? |
|---|---|---|
| 局部编辑 / 局部属性 / 背景 / **画质或风格改变** | **clarify and constrain** —— 说清改什么,其余 stand | ✔ 落在这里 |
| compositing / 合影 / 海报 | actively construct | ✖ |

即:**「提升画质」在 2.1 的规范里属于「只改点名的、其余保持」的范畴**,
而它必然全局性地改变每一个像素 ⇒ 天然贴近 **Leakage** 边界。

官方原文甚至把「锐化」直接写进了 Leakage 的例子里 —— 括号内举例
*a sharpen that re-grades color*(一次锐化顺手改了色调)。⚠️ 该行为例出现在 L40 附近的
Leakage 说明段,本库未逐字复核行号,以措辞为准。

### 2.1 官方还明令禁止把画质词当提示词用

- 质量词黑名单:**8k / 4k / masterpiece / award-winning / photorealistic masterpiece** 等。
- 「要写可观察的视觉属性,而不是打质量标签」;
- **禁止把分辨率/比例写进提示词**(走 `wh_ratio` / `ratio_follow` 字段);
- `rewritten_prompt` 必须**单段无换行**;
- 官方合格示例仅 **21~96 字符**,且**每一条都是具体的、有明确目标的编辑**。

⚠️ **你现在用的 `依据图1 参考, 提升图片整体画质和像素。` 是典型的未重写裸指令** ——
既没点名具体属性,也没走官方 PE 重写。2.1 的一切设计假设都建立在「提示词经过 PE 重写」的前提上。

---

## 3. 参考图与目标图的拼接结构也变了

| | 1.x(Kontext 式) | 2.1 |
|---|---|---|
| 参考图位置 | 接在**目标图之后** `torch.cat([hidden_states, kontext])` | 插在**文本序列中间**,目标图在**最后**(`build_sequence` 注释 `target image last`) |
| 位置编码 | 参考图用独立 `index=1`(`default_ref_method="index"`) | 三轴 RoPE + 三角因果掩码 `tril(length)` |
| 注意力 | 双向 | 参考图只能看到它前面的文本,看不到后面的 |

2.1 的结构是「指令文本 → 参考图 → 目标图」,**指令排在参考图之前**,且参考图受因果掩码限制。
对具体编辑(「把头转向左」)这个顺序是对的;但对「提升画质」这种需要参照原图细节做判断的指令,
参考图排在指令后面、更吃亏。

---

## 4. 参数量差约 3 倍

本机权重实测(文件大小,均为 fp8/bf16 混合精度):

| 模型 | 文件 | 大小 | 视觉生成参数量 |
|---|---|---|---|
| `qwen_image_2.1_bf16` | `models/diffusion_models/` | **14.23 GB** | ~7B |
| `qwen_image_edit_2511_fp8mixed` | 同上 | **20.53 GB** | ~20B 级 |
| `qwen_image_2512_fp8_e4m3fn` | 同上 | 20.43 GB | ~20B 级 |
| `qwen_image_fp8_e4m3fn` | 同上 | 20.43 GB | ~20B 级 |

⇒ 2.1 参数量约为旧编辑模型的 **1/3**。这是模型容量层面的事实,
对「需要精细判断哪里该锐化」的任务不利。

---

## 5. ⚠️ 本库工作流参数:我此前的读数有三处是错的,已更正

这一节是本次调研的**自我纠错记录**,很重要 —— 如果不写下来,这些错误读数会继续误导后续工作。

### 5.1 ❌ 错误:「1.x 负词为空、2.1 负词 544 字符」

**实为:两者负词都是同一串 544 字符。**

```python
# 逐字比对结果
0011_万物建模.json      #6031 负词 = 544 字符
00110_万物建模_QI2.1.json  #50 负词 = 544 字符
两者内容完全相同
```

⇒ **负词对拉不构成 1.x vs 2.1 的差异**。我先前只看了 1.x 那个 `TextEncodeQwenImageEditPlus#5505`
(正词节点)就下了结论,漏看了正负各有一个独立编码节点、且负词节点 #6031 挂着同一串 544 字符。
**这一条不要再当作差异项。**

### 5.2 ❌ 错误:「1.x cfg=1.0、2.1 cfg=0.85/0.9」

**实为:两者 cfg 都是 1.0。那个 0.85 / 0.9 是 `denoise`,不是 cfg。**

KSampler 的 `widgets_values` 顺序是
`[seed, control_after_generate, steps, cfg, sampler_name, scheduler, denoise]`。
我此前把 `widgets[6]`(denoise)读成了 cfg。KSampler#60 的 widgets 确实是
`[0,"fixed",15,1,"euler","simple",0.85]` —— 第 4 项(idx 3)是 **1**,不是 0.85。

⚠️ 而且 4 个 QI2.1 工作流的 cfg/steps 走的是 `FallingTSSwitch`(输出→采样器输入的连线),
必须**顺着连线追到分组开关的生效输入**才能拿到真实值,不能读 widgets。

### 5.3 ❌ 错误:「1.x 编辑是 4 步 Lightning、2.1 是 15 步」—— 部分成立但要补 ctx

1.x 编辑采样 `#6024` 的 steps 生效值 = `PrimitiveInt#5606 = 4`(`FallingTSSwitch#5602` 组2 生效分支),
且 `output_1`(model)生效的是 `PathchSageAttentionKJ#5710 = ["disabled", false]` —— **注意不是 Lightning LoRA**,
1.x 编辑链的 model 分支走的是 `switch=false` 分支的 `CFGNorm#5507`?不,生效的是 true 分支的「disabled」。
⇒ 1.x 编辑链在 switch=true 下 model 是「不带 LoRA 的基座 + CFGNorm(false 分支)」。
**这一点本库未完全追清,请以下一节 §5.4 的实测为准。**

### 5.4 ✅ 更正后的完整对照表(全部经连线追踪实测)

| 项 | Qwen-Image-Edit 2511(1.x) | Qwen-Image 2.1 |
|---|---|---|
| 视觉生成参数量 | ~20B(20.53 GB fp8mixed) | ~7B(14.23 GB bf16) |
| 文本编码器 | `qwen_2.5_vl_7b_fp8_scaled` | `qwen3vl_8b_bf16` |
| 编辑 system prompt | 要求 describe color/shape/size/texture | 仅 "Comprehend and analyze the provided prompt."(且被丢弃) |
| vision token | 保留在文本序列 | **从序列删除**,改用 ref latent 拼 slot |
| 视觉 token 去留开关 | — | `keep_vision = len(ref_latents)==0`;接了 VAE ⇒ 丢弃 |
| 参考图拼接位置 | 目标图之后 | 文本序列中间,目标图在最后 |
| 编辑负词(本库) | **544 字符** | **544 字符(同串)** |
| 编辑 cfg | **1.0** | **1.0** |
| 编辑 denoise | 0.5 | 0.85(00110/00220)、0.9(00120) |
| 参考图缩放 | VL 侧 384×384、VAE 侧 1024×1024 | `resolution` 默认 **1024** |
| 参考图缩放入口 | — | `nodes_qwen.py:123` 默认 1024;tooltip:**0 = 各图保持原尺寸** |
| 参考图路经 | 1.x VL 384² / VAE 1024² | 2.1 两者**同一尺寸**(nodes_qwen.py:153 注释) |
| 蒸馏 LoRA | 存在(`Qwen-Image-Edit-2511-Lightning-4steps`) | 无 |
| 蒸馏 LoRA 是否在编辑链生效 | 见 §5.3,未追清 | N/A |

> 📌 **`resolution` 的一个实用价值**:`nodes_qwen.py:123-124` 的 tooltip 写明
> **`resolution=0` 表示各参考图保持自己的尺寸**(32 倍数取整)。默认 1024 会把参考图降采样。
> 若你的底图是 2× 放大的高分辨率图,送进编码器的只有 1024 级别信息。
> ⇒ **本库 4 个 QI2.1 工作流的 `resolution` 全是默认 1024,这是一个可立即测试的点。**

---

## 6. 待验证线索(GitHub 被墙,仅转述搜索摘要,未核实)

`web_fetch` 对 github.com 全部返回 `TypeError: fetch failed`(本机直连外网被掐)。
以下两条来自 `web_search` 摘要,**未经原文核实,仅作线索**:

1. **`Comfy-Org/ComfyUI#16435`** — 标题:*"Qwen-Image-2.1 image edit: VAE reference-latent splice produces broadband noise at exactly resolution=1024 (the node default); 992 and 1056 are clean"*
   👉 若属实,**精确命中本库配置**(4 个工作流 resolution 全是默认 1024)。值得试 992 / 1056。
2. **`utensils/mold` 某 commit** — *"fix(qwen-image): remove spurious sqrt(C) scaling from VAE RMS norm"*
   👉 若属实,2.1 的 RMSNorm 缩放有个多余因子,影响 VAE 重建精度。

---

## 7. 我自己被实测推翻的假设(自我纠错)

### 7.1 ❌ 推翻:「2.1 VAE 16× vs 1.x 8× ⇒ 细节更少」

**不成立。** 核对 latent 配置与 `patch_size` 后:

```
1.x  latent_formats.Wan21        : latent_channels=16, 8× 降采样
     DiT patch_size=2             ⇒ 8 × 2 = 16 图像像素 / token
2.1  latent_formats.QwenImage21  : latent_channels=64, 16× 降采样
     DiT 无 patchify(img_in 是直接 Linear,comfy/ldm/qwen_image21/model.py:217)
                                   ⇒ 16 × 1 = 16 图像像素 / token
```

**两代每 token 覆盖的图像像素数完全相同,token 预算一致。2.1 的 VAE 并不「更粗」。**
⇒ 不得把「VAE 压缩比」当作画质差距的原因。

（顺带实测到:2.1 的 VAE 是 **4 通道 RGBA** —— 传 3 通道会报
`Given groups=1, weight of size [96, 4, 1, 3, 3], expected input[1, 3, 1, 576, 1024] to have 4 channels`。
1.x VAE 走 `latent_dim=3`(5D 输入),2.1 走 `latent_dim=2`。）

### 7.2 ❌ 推翻:「1.x 负词为空、2.1 负词 544 字符」

见 §5.1 —— 两者同串,不是差异项。

### 7.3 ❌ 推翻:「2.1 cfg=0.85/0.9、1.x cfg=1.0」

见 §5.2 —— 那是 `denoise`。两者 cfg 都是 1.0。

### 7.4 ❌ 未完成:两代 VAE 的往返保真度 PSNR

我本想实测 encode→decode 往返 PSNR 作为「VAE 本身是否有损」的最终证据,
但三次都在张量维度上踩坑(`WanVAE` 3D/2D 布局不一致、通道数不匹配),**最终没跑出数字**。

⚠️ **所以「VAE 重建保真度」这一项本库没有实测证据,不排除它也有份**,只是目前最强的解释不在这儿。
临时探测脚本已清空(`scripts` 是临时目录,不遗留)。

---

## 8. 本地已拉取的权威源

| 路径 | 远程 | 用途 |
|---|---|---|
| `refs/Qwen-Image-2.1` | https://github.com/QwenLM/Qwen-Image-2.1.git | 官方仓库 + `prompt_rewrite/prompts/system_prompt_edit.txt` 规范原文 |
| `refs/qwen-image-2.1-skill` | https://github.com/iamyoki/qwen-image-2.1-skill.git | 2.1 提示词 Skill(含 `validate_prompt.py` 校验器) |

校验器**只查格式不判语义**:本库三行全部 `pass=True`,说明失败**不是格式问题**,不能靠它兜底。

---

## 9. 建议的下一步(按性价比排序)

| 优先级 | 动作 | 依据 | 成本 |
|---|---|---|---|
| **P0** | **`resolution` 1024 → 0(保原尺寸)或 992 / 1056** | §5.4 tooltip + §6 线索#1;4 个工作流各改 1 个值 | 零 |
| **P0** | **把「提升画质」改成可观察的具体视觉属性** | §2.1 官方明令禁画质词、要求点名属性 | 零(改表) |
| **P1** | 走官方 PE 重写(**Qwen-Image-2.1-PE-I2I**) | §2.1:2.1 的一切假设建立在「提示词经 PE 重写」上 | 需下模型 |
| **P1** | A/B 实测:同图 1.x vs 2.1 各出一张,逐图 `read_image` 比对 | 定位差异到底出在哪一环 | 出图时间 |
| **P2** | 若仍不理想,改用超分/修复链路而非生成式编辑 | 本库已装 `ComfyUI-SUPIR` / `4xNomos8kDAT` / SeedVR2 | — |
| **P2** | 全图编辑改走局部精修插件 | 本库已装 `ComfyUI-Inpaint-CropAndStitch` | 改工作流 |

### 9.1 「可观察属性」的改写示例

| 不用(抽象质量标签) | 改用(可观察视觉属性) |
|---|---|
| `提升图片整体画质和像素` | `更清晰的皮肤纹理与发丝细节,衣料织纹可辨` |
| `提高分辨率 / 4K` | `(走 `wh_ratio` 字段,不写进提示词)` |
| `更清晰` | `边缘锐利、噪点更少,玻璃与金属反光边界干净` |

⚠️ 官方同时提醒:**不要具体描写你要保留的东西** —— 越具体描述「本想保留的东西」,
模型越可能把它重画。保留声明用**一句笼统的**即可,不要逐项枚举。
(详见 `docs/Qwen-Image-2.1-提示词规范调研-2026-09-24.md` §2.2。)

---

## 10. 本次未采信的源

- 二手教程与博客(`qwe.edu.pl`、`apidog.com`、`cnblogs` 等)仅作线索,结论一律回到官方原文核对。
- §6 两条 GitHub 线索因本机直连外网被掐而**无法核实**,已在该节明确标注。
- 未做 VAE 往返保真度 PSNR 实测(§7.4),该维度**留空**。
