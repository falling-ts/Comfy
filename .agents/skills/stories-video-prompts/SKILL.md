---
name: stories-video-prompts
description: Video resource types for the story library — text-to-video, first-frame video, first-last-frame video, keyframe video (with its hard constraints and picture numbering), and reference video (Ref2VA). Covers each type's write trigger and prompt-extraction rules (T2VA, I2VA, FL2VA, keyframe anchoring, full-reference six-section rewrite). Use when writing or editing a video resource table whose subject is a character, creature, or object rather than a scene.
---

# 故事库视频资源规范（主体/人物视频）

> 尺寸与语言规范见技能 `stories-resource-tables`。场景类视频（360° 场景环绕）见技能 `stories-scene-video`。镜头运动术语见技能 `stories-shot-language`。参考多视图的编号与视角顺序规则见技能 `stories-scene-video` 的「场景参考图与 H3 运镜实测经验」第六条。

### 文生视频

即通过描述和秒数以及提示词生成视频，包含ID，视频提示词(TEXT)，宽度(INT)，高度(INT)，视频秒数(INT)

#### 写入时机

**需要我明确说明写入哪些内容时，才可以写入**；分析正文内容时，**不允许自动写入**。

#### 文生视频 提示词提取规范

视频提示词按 **T2VA** 规范书写，直接以三个核心字段开头，无图像对齐指令：

1. **integrated_multimodal_description**：沿时间线描述视觉、动作、镜头、说话者、对白、演唱与剧情内声音
2. **overall_soundscape**：概括整个视频中的环境音、物理动作声和非语言人声
3. **non_diegetic_music**：描述角色听不到、仅观众能听到的背景音乐

`[Shot 1]` 描述开场镜头，不带时间戳；后续镜头以 `[Shot 2] At MM:SS.mmm` 递增标注切换时间并说明切换方式（cut / cross-dissolve / fade）。说话者用 (S1)、(S2) 稳定编号并置于 `<d>` 之外，对白写作 `<d>[Chinese] 内容</d>` —— **方括号内一律填英文语言名**（Chinese / English / Japanese …），严禁写 `[中文]`（语言规则见「H3 提示词语言规范」）。

### 首帧视频

即通过首帧和秒数以及提示词生成视频，包含ID，<Picture 1>(IMAGE)，视频提示词(TEXT)，宽度(INT)，高度(INT)，视频秒数(INT)

#### 写入时机

**需要我明确说明写入哪些内容时，才可以写入**；分析正文内容时，**不允许自动写入**。

#### 首帧视频 提示词提取规范

视频提示词按 **I2VA** 规范书写，首帧为视频在 0.00 秒的实际第一帧：

1. 第一行对齐指令：`对于目标视频，在目标视频的 0.00 秒处，<Picture 1>（来自 [Shot 1]）被完整引用。`
2. 空一行后写三个核心字段：integrated_multimodal_description、overall_soundscape、non_diegetic_music

integrated_multimodal_description 采用「首帧锚点 → 动作发起 → 连续展开 → 结果或反应」结构：先在图像中确立风格、主体、构图与场景锚点，再描述后续动作，保持角色身份、服装、颜色、关键物体与空间关系一致。

**图片标签使用**：首帧图用 `<Picture 1>` 引用（对齐指令中即为 `<Picture 1>`）。此模式**不使用 `<Subject N>`**，画面一致性通过 integrated_multimodal_description 中「保留 <Picture 1> 的角色 X、服装 Y」之类的文字描述维持。

### 首尾视频

即通过首尾帧和秒数以及提示词生成视频，包含ID，<Picture 1>(IMAGE)，<Picture 2>(IMAGE)，视频提示词(TEXT)，宽度(INT)，高度(INT)，视频秒数(INT)

#### 写入时机

**需要我明确说明写入哪些内容时，才可以写入**；分析正文内容时，**不允许自动写入**。

#### 首尾视频 提示词提取规范

视频提示词按 **FL2VA** 规范书写，首帧为开场、尾帧为结局：

1. 第一行对齐指令：`参考图片与目标视频的对齐方式 — Picture 1（来自 Shot 1）对齐目标视频的 0.00 秒位置；Picture 2（来自 Shot N）对齐目标视频的 S.SS 秒位置。`
2. 空一行后写三个核心字段：integrated_multimodal_description、overall_soundscape、non_diegetic_music

integrated_multimodal_description 采用「首帧状态 → 可观察的中间变化 → 差异逐渐收窄 → 末帧状态」结构，聚焦主体如何运动、姿势如何变化、物体如何被操控、构图如何演变、场景或光照如何过渡。一般倾向单个镜头，由首帧连续插值到尾帧。

**图片标签使用**：首帧图用 `Picture 1`、尾帧图用 `Picture 2` 引用（对齐指令中即为 Picture 1 / Picture 2）。此模式**不使用 `<Subject N>`**，画面一致性通过 integrated_multimodal_description 中「由 Picture 1 确立的姿势/构图…落定到 Picture 2 确立的姿势/构图」之类的文字描述维持。

需要 **2 个以上中间关键帧**时改用「关键帧视频」（见下文）：首帧填其第 1 槽、尾帧填其第 9 槽、中间关键帧按序填第 2 ~ 8 槽，**只有中间帧需要在右侧的「关键帧n所在秒数」列填该图锚定的秒数**（首帧恒在片头、尾帧恒在片尾，位置固定，两者都不需要秒数），`锚点数` 列填实际锚点个数。

### 关键帧视频

即通过首帧、尾帧与任意数量中间关键帧和秒数以及提示词生成视频，包含ID，锚点数(INT)，<Picture 1> 首帧(IMAGE)，<Picture 2>(IMAGE)，关键帧2所在秒数(FLOAT)，<Picture 3>(IMAGE)，关键帧3所在秒数(FLOAT)，<Picture 4>(IMAGE)，关键帧4所在秒数(FLOAT)，<Picture 5>(IMAGE)，关键帧5所在秒数(FLOAT)，<Picture 6>(IMAGE)，关键帧6所在秒数(FLOAT)，<Picture 7>(IMAGE)，关键帧7所在秒数(FLOAT)，<Picture 8>(IMAGE)，关键帧8所在秒数(FLOAT)，<Picture 9> 尾帧(IMAGE)，视频提示词(TEXT)，宽度(INT)，高度(INT)，视频秒数(INT)

共 **22 列**。首帧列列名写作 `<Picture 1> 首帧`、尾帧列写作 `<Picture 9> 尾帧`（角色词写在类型后缀 `(IMAGE)` 之前——表头解析取**最后一对括号**为类型，角色词写到括号后面会导致类型识别失败）。

九张图为**固定语义槽位**：`<Picture 1> 首帧` 恒钉视频第 0 帧，`<Picture 9> 尾帧` 恒钉视频末帧，`<Picture 2>` ~ `<Picture 8>` 为 7 个中间帧槽位。**首帧、尾帧的位置是固定的，因此它们没有秒数列**：首帧在画布上由 `#40` 的 `frame_idx` 控件硬钉 `0`；尾帧由表达式 `max(0, a − 1)`（a = 吸附后总帧数 `length`）钉到第 `length − 1` 帧。**只有中间帧需要秒数**：第 2 ~ 8 槽每槽右侧跟一个「关键帧n所在秒数」列，工作流内每个中间帧配一个 `ComfyMathExpression`，把该秒数换算成帧索引 `frame_idx = max(0, min(round(关键帧n所在秒数 × 24), length − 1))`（24 为 H3 固定帧率），秒数留空按 0 处理。**槽位的先后与秒数大小无需单调**——中间帧按秒数各自独立定位，谁前谁后由秒数决定，不由槽位序决定。

**为什么是 9 个槽位**：官方核心没有「关键帧汇总节点」，逐帧锚定靠**链式串联 `MiniMaxH3AddGuide`**（每个节点吃 1 张图 + 1 个 `frame_idx`，数量本身无上限）。真正的上限在**文本编码器可见性**上——`MiniMaxH3ReferenceToVideo.ref_images` 是 `Autogrow.TemplatePrefix(prefix="ref_image_", min=0, max=9)`，槽位名硬生成 `ref_image_0` ~ `ref_image_8`，**第 10 个槽位名不存在**。故 **9 个图片槽位正好用满官方上限**，每个填入的槽位都能同时「被锚定」且「被提示词引用」。

**`锚点数` 列只作填写计数**：定位已改由「首帧/尾帧固定 + 中间帧逐列秒数」驱动，该列**不参与任何帧索引计算**，仅供提示词书写与自查参考；它应等于实际填图的槽位数（3 个锚点 = 首帧 + 1 个中间帧 + 尾帧）。因此**「槽位留空」就是唯一的「不锚定」开关**——空槽在数据表里输出 `None`，由 `FallingTSH3AddGuide` 原样透传，等价于该槽无锚点；**两个中间帧秒数相同（或换算后落在同一帧）时后到的那槽会被撤掉并告警**（同一时刻钉上两个互相矛盾的画面正是物件漂移的成因，该槽图片仍作为参考图参与条件）。

#### 写入时机

**需要我明确说明写入哪些内容时，才可以写入**；分析正文内容时，**不允许自动写入**。

#### 关键帧视频 提示词提取规范

视频提示词按 H3 **关键帧锚定**规范书写（由引导节点在任意像素帧锚定画面）。**依锚点构成择一模式**：

- 只锚首帧 → 按 **I2VA** 写（同首帧视频）
- 只锚首尾帧 → 按 **FL2VA** 写（同首尾视频）
- **锚点 ≥ 3（含中间关键帧）或有多个镜头 → 按 Ref2VA 全参考模式写**（六部分结构同参考视频），与官方 `video_minimax_h3_multiframe_reference` 模板一致

写法：

1. **FL2VA 模式**首行写对齐指令：`参考图片与目标视频的对齐方式 — <Picture 1>（来自 [Shot 1]）对齐目标视频的 0.00 秒位置；<Picture N> 对齐目标视频的 S.SS 秒位置。`，空一行后写三个核心字段
2. **Ref2VA 模式**在 detailed_description 的每个镜头首句点名锚点：`[Shot N] At S.SS 锚定在 <Picture N> 所确立的…`

对齐指令**逐条点名每一个已填槽位**，时间格式 `S.SS`（两位小数）：**首帧固定写 `0.00`**；**中间帧直接取该列「关键帧n所在秒数」的值**（提示词里的时点与工作流的锚定帧由同一个数字驱动，无需按帧号反推）；**尾帧固定写末帧时刻 `(length − 1) / 24`**（15 秒档 = `15.04`，由 `视频秒数` 吸附后的 `length` 决定，表里不填秒数）；**未填槽位不写入对齐指令**。integrated_multimodal_description / detailed_description 在对应时点插入 `<Picture N>` 引用：首次出现写「标签 + 完整画面特征描述」落地，后续镜头继续使用同一标签。

**`<Picture N>` 编号规则（最易错的一条）**：`<Picture N>` 的 N 是**该图在非空参考图里的连续排位**，**不是表里的槽位号**——官方 ref2va 对非空参考图逐张累加编号（`comfy/text_encoders/minimax.py` 中 `counters["image"] += 1` 后写出 `<Picture %d>`），空槽在 `comfy_extras/nodes_minimax_h3.py` 里被 `if img is None: continue` 跳过。故：首帧 = `<Picture 1>`；第 i 个中间帧 = `<Picture i+1>`（**中间帧必须从第 2 槽起连续填写**，这样槽位号与排位号才恰好相同）；**尾帧 = `<Picture 锚点数>`**——尾帧虽然固定在第 9 槽，提示词里写的是它的排位号（3 个锚点时为 `<Picture 3>`，**不是** `<Picture 9>`；写 `<Picture 9>` 会指向一张不存在的参考图）。

#### 关键帧视频 硬性约束（违反即失败或画面崩坏）

1. **首帧填第 1 槽、尾帧填第 9 槽（两端槽位固定，都应填写），中间帧从第 2 槽起连续填写、中间严禁留空**。留空的槽位输出 `None`（不锚点、不生成引导块，也不影响其余槽位的定位），但**中间留空会使提示词里的 `<Picture N>` 排位号与实际参考错位**（同「场景参考图与 H3 运镜实测经验」第六条）
2. **相邻锚点间隔 ≥ 1.5 秒**（官方 multiframe 演示锚点为 0.00 / 1.5 / 3.0 / 5.0 秒，1.5 秒为工程红线）；推荐间隔 **2.5 秒**（多镜头节奏），故 `视频秒数 ≈ (锚点数 − 1) × 1.5 ~ (锚点数 − 1) × 2.5`
3. **9 个槽位用满要求视频 ≥ 12 秒**（8 段间隔 × 1.5 秒），按推荐密度则应配 **13.5 ~ 15 秒**；单段合法上限为 **15.08 秒（362 帧）**，故 9 锚点的实用区间是 **12 ~ 15 秒**（15 秒 = 362 帧，间隔 1.875 秒）
4. **锚点必须落在已生成时长内**：中间帧的帧索引算式以吸附后 `length − 1` 为上限钳制（填负数则夹到 0），不会越界；首帧恒钉第 0 帧、尾帧恒钉第 `length − 1` 帧，天然不越界；秒数为空的槽位在引导节点里直接透传、不校验帧索引
5. **引导图对文本编码器不可见**：官方 `MiniMaxH3AddGuide` 只固定帧构图，提示词无法以 `<Picture N>` 引用它（官方 multiframe 模板里 `<Picture 2/3/4>` 就是这样悬空引用——那 3 张只接了引导、只有首帧进了 `ref_images`）。要让提示词引用某张关键帧，该图**必须同时进入 `ref_images` 通道**；0043 工作流因此把每个槽位**同时**接入 `MiniMaxH3ReferenceToVideo.ref_image_0` ~ `ref_image_8` 与对应引导节点
6. **空槽必须走 None 安全的引导节点**：官方 `MiniMaxH3AddGuide` 在 image 与 audio 同为 `None` 时直接抛 `ValueError`（不像 `MiniMaxH3ReferenceToVideo` 有 `if img is None: continue` 兜底），而数据表空槽按「可选输入惯例」输出 `None`、引擎又把它原样传给下游——所以 0043 的 9 路引导一律用自研 **`FallingTSH3AddGuide`**（空则原样透传 `positive`，等价于该槽无锚点），**官方引导节点不能直接串联成链**
7. **锚点图必须来自同一场景的一致性画面**：互相矛盾的关键帧是互相冲突的条件，会使模型在矛盾间摇摆（家具漂移、凭空增减物件），参见「场景参考图与 H3 运镜实测经验」第一条

**帧数换算**：总帧数 `length` 由 `视频秒数` 按 17k+5 网格向上吸附，单段合法 **124 ~ 362 帧**（5.17 ~ 15.08 秒），15 秒 = 362 帧。帧索引落点：**首帧 = 第 0 帧**（固定）；**第 n 个中间帧 = `max(0, min(round(关键帧n所在秒数 × 24), length − 1))`**；**尾帧 = 第 `length − 1` 帧**（固定）。以 `视频秒数 = 15` 为例：`length = 362`（实际时长 15.083 秒），尾帧落在第 361 帧 = `15.04` 秒——**提示词里的尾帧时点要写 `15.04`，写 `15` 会指向第 360 帧**（末帧时刻恒为 `(length − 1) / 24`，改 `视频秒数` 时必须同步改提示词里的尾帧时点）。
### 参考视频

即通过最高9张图片，3个视频，3个音频参考生视频，包含ID，<Picture 1>(IMAGE)，<Picture 2>(IMAGE)，<Picture 3>(IMAGE)，<Picture 4>(IMAGE)，<Picture 5>(IMAGE)，<Picture 6>(IMAGE)，<Picture 7>(IMAGE)，<Picture 8>(IMAGE)，<Picture 9>(IMAGE)，<Video 1>(VIDEO)，<Video 2>(VIDEO)，<Video 3>(VIDEO)，<Audio 1>(AUDIO)，<Audio 2>(AUDIO)，<Audio 3>(AUDIO)，视频提示词(TEXT)，宽度(INT)，高度(INT)，视频秒数(INT)

#### 写入时机

根据视频**静态或动态镜头语言分类**，对正文描述的内容进行**视频化提示词描述**；参考主要用上面**自动写入**的 万物 和 场景 生成 ID 进行参考。

#### 参考视频 提示词提取规范

视频提示词按 **Ref2VA 全参考模式** 规范书写，六部分结构与写法同 **参考场景**（见上文）：subject_definitions / summary / retention_analysis / detailed_description / overall_soundscape / non_diegetic_music；参考标签使用、Subject 三层绑定机制、图片编号规则亦全部相同。

仅两处差异：

1. **`<Subject N>` 用途**：参考视频用于可复用内容（**人物、器物、场景、服装、动作、风格**）；参考场景为（场景、地形、环境、建筑、道具、风格）
2. **detailed_description 内容**：参考视频按播放顺序逐镜头描述画面、动作、镜头、声音与对话；参考场景为场景画面、运镜、空间布局与声音

详细规则遵循 H3 全参考模式改写格式指南。
