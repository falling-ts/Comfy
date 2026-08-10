# 视频提示词写作指南(T2VA / I2VA / FL2VA / L2VA)

## 1. 任务总览

- **T2VA**:从文本构建完整的视听时间线。
- **I2VA**:T2VA 主体 + 首帧指令 + 从首帧向前展开的视觉路径。
- **FL2VA**:T2VA 主体 + 首帧和末帧指令 + 从首帧到末帧的连续路径。
- **L2VA**:T2VA 主体 + 末帧指令 + 从合理的先前状态汇聚到末帧的路径。

## 2. 最终提示词结构

### 2.1 第一部分为指令

**T2VA** 没有图像对齐指令,直接以三个核心字段开头。

**I2VA** 始终使用:

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.
```

**FL2VA** 始终使用:

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot N) aligns with the S.SS-second mark of the target video.
```

**L2VA** 始终使用:

```text
How the reference pictures align with the target video — <Picture 1> (from [Shot N]) aligns with the S.SS-second mark of the target video.
```

其中,`N` 是实际最终镜头的编号,`S.SS` 是有效视频时长,精确格式化为两位小数。指令必须是最终提示词的第一行,其后空一行,再写核心字段。

### 2.2 第二部分包含三个核心字段

```text
integrated_multimodal_description: [Shot 1] ...

overall_soundscape: ...

non_diegetic_music: ...
```

- **integrated_multimodal_description**:沿时间线描述视觉、动作、镜头、说话者、对白、演唱以及剧情内声音(diegetic audio)。
- **overall_soundscape**:概括整个视频中的环境音、物理动作声和非语言人声。
- **non_diegetic_music**:描述角色听不到、只有观众能听到的背景音乐。

## 3. 如何将关键帧纳入多模态描述

### 3.1 I2VA:从图像出发并向前展开

`<Picture 1>` 是视频在 0.00 秒处的实际第一帧,属于 `[Shot 1]`。描述应先在图像中确立风格、主体、构图和场景锚点,然后描述下一个动作。角色身份、服装、颜色、关键物体和空间关系应保持一致。

推荐结构:**首帧锚点 → 动作发起 → 连续展开 → 结果或反应**。

### 3.2 FL2VA:描述首帧与末帧之间的路径

Picture 1 是开场,Picture 2 是结局。聚焦于主体如何运动、姿势如何变化、物体如何被操控、构图如何演变,以及场景或光照如何过渡。

FL2VA 一般倾向于单个镜头,以便模型能从首帧到末帧连续插值。仅在明确指定时才使用多个镜头。末帧必须由视频末尾的最终 `[Shot N]` 到达。

推荐结构:**首帧状态 → 可观察的中间变化 → 差异逐渐收窄 → 末帧状态**。

### 3.3 L2VA:推断开场并在结尾落在图像上

`<Picture 1>` 是视频的最后一帧,属于最后一个 `[Shot N]`,并不天然属于 Shot 1。根据用户意图和末帧推断一个合理的先前状态,然后描述角色、物体、摄像机和场景如何逐渐逼近参考图。

推荐结构:**合理的先前状态 → 明确的动作与转换路径 → 最终镜头中逐渐收敛 → 末帧落地**。

## 4. 如何撰写三个共享核心部分

### 4.1 沿时间线展开多模态描述

`integrated_multimodal_description` 是改写后提示词的主体。每个细节都应对应可见或可闻的内容:视觉风格、初始构图、主体外观与位置、场景与关键道具、动作与反应、镜头切换、口头语言,以及同步的剧情内声音。

在 `[Shot 1]` 开头,陈述整体风格和初始构图。常见风格包括 `Cinematic`、`live-action`、`2D-animated`、`3D CG`、`claymation`、`watercolor` 和 `vintage film`。对于关键帧任务,从参考图中推导风格;对于 T2VA,从用户文本中选择。

```text
[Shot 1] Live-action, cinematic, a medium-wide shot frames...
```

### 4.2 镜头与切换

不要给第一个镜头添加时间戳。后续镜头使用递增的镜头编号,且每个镜头以严格递增、落在视频时长范围内的切换时间开头:

```text
[Shot 2] At 00:03.500, the camera cuts to...
```

对于普通切换,使用 `the camera cuts to`、`the shot cuts to`、`the shot transitions to`、`the shot changes to` 或 `the shot switches to`。当用户明确要求时,也可以使用叠化(cross-dissolve)、淡入淡出(fade)或划变(wipe)。切换应引入关于主体、空间、状态、视点或时间的新信息。如果只需改变距离或轻微角度,优先使用摄像机运动。

### 4.3 摄像机运动:运动类型 + 幅度 + 速度

一个完整的摄像机运动表达包含三个维度:**运动类型**定义摄像机如何运动,**幅度**定义构图变化范围,**速度**定义该变化的节奏。只在有意义时添加幅度和速度;中等幅度和常规速度通常省略。

| 维度 | 可用表达 | 描述 |
|-|-|-|
| 运动类型 | `Zoom In / Zoom Out` | 机身不动,焦距发生变化 |
| 运动类型 | `Push In / Pull Out` | 摄像机向前 / 向后移动 |
| 运动类型 | `Pan Left / Pan Right` | 机身不动,镜头水平摆动 |
| 运动类型 | `Truck Left / Truck Right` | 摄像机水平平移 |
| 运动类型 | `Tilt Up / Tilt Down` | 机身不动,镜头垂直摆动 |
| 运动类型 | `Pedestal Up / Pedestal Down` | 整台摄像机向上 / 向下移动 |
| 运动类型 | `Arc Shot` | 摄像机绕主体弧线运动 |
| 运动类型 | `Tracking Shot` | 摄像机跟随运动主体 |
| 运动类型 | `Static Shot` | 摄像机位置与镜头保持静止 |
| 运动类型 | `Shake Slightly / Shake Strongly` | 轻微 / 强烈摄像机抖动 |
| 运动类型 | `POV` | 主体的视点 |
| 运动类型 | `Roll Clockwise / Roll Counterclockwise` | 摄像机绕镜头光轴顺时针 / 逆时针旋转 |
| 幅度 | `with small amplitude` | 小范围变化 |
| 幅度 | `with large amplitude` | 大范围变化 |
| 速度 | `at slow speed` | 缓慢运动 |
| 速度 | `at fast speed` | 快速运动 |

摄像机运动应写成镜头内自然的英文动作,而不是堆叠在句尾的独立标签:

```text
The camera pushes in with small amplitude at slow speed toward the folded letter in her hands.
The camera pans right with large amplitude at fast speed, revealing the open doorway.
The camera holds a static shot as the runner exits the frame.
```

### 4.4 说话者、对白与演唱

开口说话、演唱或发出画外人声的主体使用稳定的 ID,如 `(S1)` 和 `(S2)`。当多个已编号的说话者一起说话或演唱时,使用复合 ID,如 `(S1,S2)`。说话者在各镜头间保持相同 ID;从未发声的角色不分配说话者 ID。

当说话者首次出现时,提供足够的视听上下文信息以建立稳定身份,例如角色类型、年龄、性别、是否在画面内、音高、音色、语速或口音。将说话者的身份描述短语、ID、动作和表达方式放在 `<d>` 之外。在 `<d>` 内,只包含语言标签和用户实际提供的口头内容。逐字保留原始单词和标点;不得翻译或改写。

```text
The young woman with a quiet, breathy voice (S1) says: <d>[English] I get off at the next station.</d>
The two children (S1,S2) shout together, <d>[English] Wait for us!</d>
```

对于旁白,使用确切短语 `says in an off-screen voiceover`。在每个旁白 `<d>` 块之后,立即说明对应画中角色的嘴唇保持闭合:

```text
The man (S1) says in an off-screen voiceover: <d>[English] I still remember that road.</d> while his lips remain completely closed.
```

当同一句对白或歌词跨越切换时,在两部分相接处使用 `<scenetrans>`,并明确说明音频跨越切换继续。当说话被视频结尾截断时,使用 `<cutoff>`。连贯性可用 `continues seamlessly across the cut`、`continues uninterrupted into the next shot`、`carries over from the previous shot` 或 `remains audible across the transition` 表达。

### 4.5 画面内文字

任何实际可见于画面的横幅、标牌、标签、字幕或霓虹文字,都放在英文双引号内。逐字保留原始文字和标点,不进行翻译。

```text
A red neon sign reading "营业中" glows above the doorway.
```

### 4.6 overall_soundscape

用 1–4 句英文,以一个连续段落概括整个视频中的环境音、物理动作声和非语言人声,如风声、雨声、交通声、脚步声、布料摩擦声、撞击声、呼吸声、笑声或喘气声。对白、演唱和剧情内音乐已属于多模态描述,不应在此重复。仅当用户明确要求整段视频完全静音时,才使用 `N/A`。

```text
overall_soundscape: Steady rain taps against the café windows while low room ambience continues underneath. The entrance bell rings once, followed by wet footsteps and the soft scrape of a chair.
```

### 4.7 non_diegetic_music

用 1–3 句英文描述角色听不到、只有观众能听到的背景音乐。聚焦于乐器、速度、节奏和动态变化;不要使用抽象情绪词,也不要解释配乐的情感功能。角色能听到的演唱、乐器、收音机、电视或手机音乐属于剧情内事件,应出现在多模态描述中。没有非剧情音乐时使用 `N/A`。

```text
non_diegetic_music: Sparse piano notes at a slow tempo, joined by sustained low strings that gradually increase in volume before fading out.
```

## 5. 案例

### 案例 1:T2VA

没有参考图像,直接从文本构建完整时间线。可以添加与用户意图保持一致的场景、角色、动作和声音细节。

```text
integrated_multimodal_description: [Shot 1] Live-action, cinematic, a medium-wide shot frames a baker opening the shutters of a small street bakery before sunrise. The camera pushes in with small amplitude at slow speed as the middle-aged baker with a calm, slightly raspy voice (S1) places a fresh loaf on the wooden counter and says: <d>[English] First batch of the morning.</d> [Shot 2] At 00:05.000, the camera cuts to a close-up of steam rising from the sliced bread while the baker's final words carry over from the previous shot.

overall_soundscape: Wooden shutters scrape open over a quiet street as trays clink softly inside the bakery. The doorbell rings once, followed by light footsteps and the crisp sound of bread being sliced.

non_diegetic_music: A soft acoustic-guitar pattern at a moderate tempo, joined by sparse upright-bass notes and a gentle fade at the end.
```

### 案例 2:I2VA

先写首帧指令,然后把 Picture 1 中的主体、构图和场景作为 Shot 1 的起点,再描述场景如何继续展开。

```text
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, the young woman shown in <Picture 1> remains beside the rain-covered train window, preserving her appearance, clothing, seat position, and the carriage layout. The camera trucks right with small amplitude at slow speed as she lifts her gaze from the folded letter toward the passing city lights. Her reflection moves across the glass while the quiet, breathy young woman (S1) says: <d>[English] I get off at the next station.</d> She folds the letter along its existing crease.

overall_soundscape: The train wheels produce a steady metallic rhythm beneath a low ventilation hum. Rain ticks against the window while paper rustles softly in her hands.

non_diegetic_music: Sustained cello notes at a slow tempo with widely spaced piano tones, gradually decreasing in volume.
```

### 案例 3:FL2VA

两张图分别锚定开场和结局。主体不应重复两份静态图像描述,而应提供连接二者的运动路径。以下示例是一个八秒的单镜头。

```text
How the reference pictures align with the target video — Picture 1 (from Shot 1) aligns with the 0.00-second mark of the target video; Picture 2 (from Shot 1) aligns with the 8.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, a rain-soaked cyclist begins in the position and framing established by Picture 1, holding a closed black umbrella beside a silver bicycle. The camera pulls out with small amplitude at slow speed as she releases the bicycle handle, raises the umbrella above her shoulder, and presses the runner upward until the canopy opens. Water rolls from the expanding fabric while she steps beneath it, rotates the handle into the final angle, and settles into the pose, spacing, and composition established by Picture 2 at the end of the shot.

overall_soundscape: Rain falls steadily on the pavement, followed by the metallic click of the umbrella runner and the soft snap of the canopy opening. Water drips from the bicycle frame as distant traffic passes.

non_diegetic_music: N/A
```

### 案例 4:L2VA

图像仅锚定最后时刻。先建立一个兼容的先前状态,然后让动作、物体状态和构图在最终镜头中逐渐落在 Picture 1 上。以下示例是一个六秒的单镜头。

```text
How the reference pictures align with the target video — <Picture 1> (from [Shot 1]) aligns with the 6.00-second mark of the target video.

integrated_multimodal_description: [Shot 1] Live-action, cinematic, a close shot begins with an intact drinking glass near the edge of a dark wooden table, while the same hand and sleeve visible in <Picture 1> approach from the right. The camera pushes in with small amplitude at slow speed as the fingertips strike the rim. The glass tips, falls, and hits the floor with a sharp impact; cracks spread through it as fragments slide outward. Toward the end, the moving pieces lose momentum and settle into the exact broken arrangement, hand position, camera angle, lighting, and final composition established by <Picture 1>.

overall_soundscape: Fingertips tap the glass before it scrapes across the tabletop, falls, and breaks with a sharp crash. Small fragments scatter and gradually stop sliding across the floor.

non_diegetic_music: A low electronic pulse at a slow tempo, ending immediately after the glass breaks.
```
