# 全参考模式(Full-Reference Mode)改写输出格式指南

本指南解释全参考模式下改写输出(rewrite outputs)的组织方式与撰写方式。

六个改写部分全部用英文撰写。仅 `<d>` 内的对话与歌词,以及画面中实际可见的文字,保留原始语言。

**描述详细度:** 尽可能让 `detailed_description` 详细且明确。对每个镜头,清晰交代当前构图、主体外观与位置、环境与灯光、动作与状态变化、镜头运动、当前声音,以及被参考内容实际出现或生效的位置。避免把描述简化为剧情概要或参考关系清单。

> 镜头、镜头运动、说话者、对话与普通声音的基础格式,与视频提示词撰写指南(T2VA / I2VA / FL2VA / L2VA)共用。本指南专注于全参考模式特有的参考标签、分析部分与格式差异。

## 1. 整体结构

一份完整的改写输出由以下六部分按顺序组成:

| 部分 | 用途 |
| --- | --- |
| `subject_definitions` | 定义被参考内容及其参考标签 |
| `summary` | 概括任务类型、目标视频与主要参考关系 |
| `retention_analysis` | 描述被参考内容如何被保留、转移或复用 |
| `detailed_description` | 按播放顺序描述画面、动作、镜头、声音与对话 |
| `overall_soundscape` | 概括环境氛围声与物理音效 |
| `non_diegetic_music` | 描述仅观众可闻的背景音乐 |

## 2. 参考标签与定义(`subject_definitions`)

全参考改写使用四类标签来标识被参考内容的来源与作用:

| 标签 | 含义 |
| --- | --- |
| `<Subject N>` | 从参考素材中抽象出的、可在目标视频中复用或修改的可见内容 |
| `<Picture N>` | 用作具体目标帧或镜头规划锚点的参考图片 |
| `<Video N>` | 提供剪辑来源、续写起点或整片时间结构的参考视频 |
| `<Audio N>` | 被复制或引用的音频信号 |

> 一个参考标签一旦被赋予某段内容,它在 `subject_definitions`、`summary`、`retention_analysis`、`detailed_description` 以及两个音频部分中始终表示同一含义。

`subject_definitions` 定义每段需要后续单独追踪的被参考内容,例如一个人、一个环境、某源视频的结构或一条音轨。为每一项单独列出一行,说明其标签所指内容、参考作用以及需要遵循的主要特征;当需要明确出处时,注明对应的源素材。如果 `<Picture N>` 或 `<Video N>` 只是标识另一被参考项的来源,且后续不会单独被分析或使用,则在该项的定义内引用它即可,无需另起一行。`retention_analysis` 记录每个被参考项出现在哪里,以及它是被完整保留、部分保留、转移还是复用。

### 2.1 `<Subject N>`

`<Subject N>` 用于可复用的可见内容,包括:

- 人物、动物或物体
- 场景、背景或环境
- 服装、道具、界面或视觉效果
- 风格、动作、表情或姿态

它代表一段将在目标视频中实际使用的内容单元,而非源文件本身。一个主体可能由多个参考素材定义,一个参考素材也可能提供多个主体。

```text
<Subject 1> is the young woman in <Picture 1>, with long dark hair, a blue cardigan, and a thin silver necklace.
```

当同一主体来自多个素材时,合并来源并说明每个素材分别提供了什么:

```text
<Subject 1> is the woman whose appearance comes from <Picture 1> and whose walking motion comes from <Video 1>.
```

### 2.2 `<Picture N>`

当参考图片本身充当某个镜头的首帧、关键帧、尾帧、剪辑关键帧或构图锚点时,使用独立的 `<Picture N>`:

```text
<Picture 2> is the first frame of [Shot 1], showing a woman seated beside a café window.
```

如果一张图片仅用于定义角色、场景、服装或风格,不要建立独立的图片条目;而是将图片来源引用到对应 `<Subject N>` 的定义中。

当图片作为分镜或镜头规划的参考时,说明它对应哪些镜头以及提供了哪些规划信息:

```text
<Picture 3> is a storyboard reference for [Shot 1] and [Shot 2], defining their viewpoint, subject placement, and shot order.
```

### 2.3 `<Video N>`

`<Video N>` 专用于整片级别的关系,例如:

- 剪辑一段原始视频
- 从原始视频的结尾继续
- 参考原始视频的镜头运动、剪辑、节奏或时间结构

```text
<Video 1> is the source video for the target video edit.
```

如果参考视频中的某个人物、物体、场景、动作或特效作为可见内容被复用,它仍然归属于 `<Subject N>`。`<Video N>` 标识素材或结构来源,并不取代主体标签。

### 2.4 `<Audio N>`

`<Audio N>` 表示独立的音频素材,或来自参考视频的一条已启用同步音轨。常见用途包括:

- 复制音频信号的全部或部分
- 参考背景音乐风格
- 参考说话者的音色与表达方式
- 使用原音频中的对话、歌词或音效
- 参考节拍、节奏或音频连续性

当某个 `<Audio N>` 明确对应一位目标说话者时,在定义中复用该说话者的全局 ID:若说话者对应已定义的主体,写作 `<Subject N> (Sx)`;否则使用稳定的声音描述后接 `(Sx)`。该 ID 来自目标视频的全局说话者顺序,在音频定义中不独立分配或重新编号。说话者编号规则参见第 5.4 节:

```text
<Audio 1> is the voice-timbre reference for <Subject 1> (S1).
```

当一个音频素材承担多种作用时,用一句自然的话描述这些作用,而不是另建小节。

### 2.5 同一参考视频的画面与音轨

`<Video N>` 与 `<Audio N>` 各自独立编号。每个编号只表示该标签在其自身类别内的顺序,并不编码两个类别之间的配对关系。因此,同一参考视频可能同时对应 `<Video 1>` 和 `<Audio 2>`;不同的编号并不妨碍它们来自同一源素材。

一个普通参考视频不会仅因为文件含声音就产生 `<Audio N>`。

`<Audio N>` 的定义主要陈述音频的作用,不必指明它来自哪个 `<Video N>`。仅当需要消除来源歧义时才说明共同来源,例如:

```text
<Video 1> is the source video for the target video edit.
<Audio 2> is the synchronized audio track of <Video 1> and is reused in the target video.
```

## 3. `summary`

本部分用一段简短的英文段落概括目标视频及其参考关系。它以方括号包裹的任务类型前缀开头:

```text
[reference generation] ...
[video editing + reference generation + audio reuse] ...
```

根据每个参考素材在目标视频中实际承担的作用选择任务类型:

| 任务类型 | 使用时机 |
| --- | --- |
| `keyframe completion` | 图片充当目标视频的首帧、关键帧、尾帧、剪辑关键帧或另一具体帧锚点 |
| `reference generation` | 图片、视频或音频素材为角色、场景、风格、动作、镜头运动、分镜等提供生成指导,但不充当具体帧,也不是被剪辑或续写的源视频 |
| `video editing` | 直接修改现有源视频;剪辑图片或在静止关键帧之间生成不属于此类型 |
| `video continuation` | 新内容从现有源视频延续、扩展、恢复或过渡 |
| `audio reuse` | 同一音频信号被全部或部分复用 |
| `audio reference` | 不直接复制音频信号,仅参考其音乐风格、音色、对话或歌词内容、音效质感、节拍或连续性 |

当一项任务满足多种关系时,用 ` + ` 组合任务类型,且不重复某一类型。例如,从源视频续写的同时用一张图片作为尾帧,写作 `[video continuation + keyframe completion]`。剪辑源视频并保留其原始音频,可写作 `[video editing + audio reuse]`。

仅仅存在视频或音频,并不自动产生对应的任务类型。如果参考视频只提供镜头运动、剪辑或节奏,通常归入 `reference generation`。只有在该视频被直接剪辑或续写时,才使用 `video editing` 或 `video continuation`。

剪辑源视频时,如果其原始音频仍可闻,也应使用 `audio reuse`。续写源视频而不直接复制音频信号时,如果新音频仅延续原音轨的可闻特征,则使用 `audio reference`。

`summary` 使用先前定义的 `<Subject N>`、`<Picture N>`、`<Video N>` 和 `<Audio N>` 标签来描述主要主体、镜头流程与参考素材的作用。不要在本部分引入新的参考标签。

对于视频剪辑任务,在任务类型前缀之后以如下方式开始概括:

```text
The target video is an edited version of <Video 1>.
```

## 4. `retention_analysis`

本部分描述每段被参考内容在目标视频中如何被保留、转移、复制或引用。每个参考标签占一行,并保持 `subject_definitions` 中已确立的含义。

### 4.1 可见内容

`<Subject N>`、`<Picture N>` 和 `<Video N>` 使用以下关系标记。这些标记是输出格式中的固定英文值:

| 关系标记 | 含义 |
| --- | --- |
| `fully_preserved` | 被参考内容的既定作用被完整保留 |
| `partially_preserved` | 被参考内容仍被使用,但部分既定特征被改变或仅部分保留 |
| `attribute_transfer` | 被参考的特征被转移到另一个可识别的目标主体上 |
| `weak_reference` | 仅保留风格、类别、构图或氛围层面的宽泛相似性 |

主体条目:

```text
<Subject 1> (appears in [Shot 1], [Shot 3]): fully_preserved - ...
```

图片条目:

```text
<Picture 2> ([Shot 1] first frame): fully_preserved - ...
```

视频结构条目:

```text
<Video 1> (cut and pacing structure): weak_reference - ...
```

### 4.2 音频

`<Audio N>` 使用以下关系标记:

| 关系标记 | 含义 |
| --- | --- |
| `fully_copy` | 完整源音频作为目标视频的完整最终音轨 |
| `partially_copy` | 只复制部分时间线或选定的音频层,或在复制后增删、替换其他声音 |
| `reference` | 不直接复制信号,只参考音色、节奏、音乐风格、对话内容或声音质感 |
| `weak_reference` | 仅保留类别或氛围层面的宽泛相似性 |

```text
<Audio 1>: fully_copy - <Audio 1> is reused 1:1 as the target video's complete final audio track.
```

```text
<Audio 2>: reference - the target speaker follows <Audio 2>'s voice timbre and measured delivery without copying the original signal.
```

每个关系标记只能在 `subject_definitions` 中已为该标签定义好的参考作用范围内选择。不要把目标视频中新增的动作、背景或情节事件视为参考保真度的损失。

## 5. `detailed_description`

这是全参考改写的主体部分。它按目标视频播放顺序逐镜头描述画面、动作、声音与对话,并在适用处插入参考标签。

### 5.1 基础格式

基础格式遵循视频提示词撰写指南(T2VA / I2VA / FL2VA / L2VA):

- 正文用英文撰写。对话、歌词与画面可见文字保留原始语言。
- `[Shot 1]` 标记开场镜头,不带时间戳。后续镜头使用 `[Shot N] At MM:SS.mmm, ...` 标记剪辑时间点。
- 在当前镜头内用自然英文书写镜头运动,在需要表达时包含运动类型、幅度与速度。
- 为发声来源赋予稳定的 `(S1)`、`(S2)` 及后续 ID。对话与歌词写作 `<d>[Language] ...</d>`。
- 对话跨越剪辑、语音因视频结束而被截断、声音跨镜头连续,分别使用 `<scenetrans>`、`<cutoff>` 及相应的连续性描述。

关于镜头词汇、群体对话、画外音、跨剪辑对话与画面可见文字的完整规则与示例,参见视频提示词撰写指南(T2VA / I2VA / FL2VA / L2VA)。

### 5.2 全参考模式的差异

| 维度 | T2VA | 全参考模式 |
| --- | --- | --- |
| 主字段 | `integrated_multimodal_description` | `detailed_description` |
| 风格开头 | 写在 `[Shot 1]` 之后 | 在 `[Shot 1]` 之前用一到两句英文确立 |
| 参考信息 | 不使用全参考标签 | 在首次出现及作用适用的位置插入 `<Subject N>`、`<Picture N>`、`<Video N>` 和 `<Audio N>` |
| 音频关系 | 描述目标视频自身的声音 | 在对应镜头或音频阶段引用 `<Audio N>`,并说明信号是复制还是引用 |

开头示例:

```text
The target video is in a cinematic, literary music-video style with soft lighting and a slightly desaturated color palette.
[Shot 1] The scene opens in a crowded urban street...
[Shot 2] At 00:09.000, the shot cuts to an extreme close-up...
```

对于生成任务,`detailed_description` 通常为 350-500 英文词。对话密集的内容优先容纳完整的说话时间线,而不是机械地凑字数。视频剪辑类描述随源视频复杂程度伸缩,不必遵循生成任务的字数区间。单个镜头并不自动意味着更短的描述;应根据信息负载把细节分配到多个镜头中。

### 5.3 在镜头中使用参考标签

当某个重要 `<Subject N>` 首次清晰出现时,在其实际可见范围内描述其被参考的特征、画面中的位置与当前动作。后续镜头继续使用同一标签,无需重新定义该标签所代表的内容。

对具体帧锚点使用自然措辞:

```text
the shot begins from <Picture 1>
the shot's keyframe corresponds to <Picture 2>
the shot ends on <Picture 3>
```

当剪辑或续写原始视频时,在其源状态、结构或续写关系适用的位置自然引用 `<Video N>`。在音频关系生效的镜头或语义阶段引用 `<Audio N>`。

### 5.4 说话者、音频来源与对话

基础说话者 ID 与 `<d>` 格式遵循 T2VA。当被参考的主体实际开口说话时,同时保留画面参考标签与说话者 ID:

```text
<Subject 2> (S1) turns toward the woman and says, <d>[English] Last summer, I went to my grandfather's house. He talked about you.</d>
```

`<Subject N>` 标识被参考的主体,`(Sx)` 标识实际的说话者。主体开口说话时写作 `<Subject N> (Sx)`。同一主体在画外说话时保持同一形式,并标记为 `off-screen`。当说话者不对应任何已定义主体时,使用稳定的声音描述后接 `(Sx)`。

当口头内容只是直接复用的 BGM 或完整配乐中的一段唱词,没有真人、角色、旁白或其他独立发声来源在物理上产生它时,用 `<Audio N>` 作为可闻来源,不要虚构额外的 `(Sx)`。如果确有真人、角色、旁白或其他独立发声来源发出该声音,则为该来源分配并复用 `(Sx)`:

```text
When <Audio 1> reaches the phrase <d>[English] I'm lonely lonely lonely lonely lonely I'm lonely</d>, <Subject 1> performs the corresponding hand gesture without becoming a separate speaker source.
```

当参考音频中的对话、旁白或歌词被直接复用,或输入提示词明确要求重新演绎它们时,在 `<d>` 内保留准确的源词句与原始语言。对听不清的片段写作 `[unclear]`,不要猜测或改写。标点规范为表达句子所需的基本书面标记,如 `,`、`.`、`?` 和 `!`;删除重复的波浪号、emoji、项目符号以及重复或装饰性标点。完整的陈述句、疑问句与感叹句在 `</d>` 前分别以 `.`、`?` 或 `!` 结尾。

当只参考音色、节奏、情绪或表达方式时,不要把参考音频中的原对话带进目标视频。

`(Sx)` 根据目标视频中实际发声事件的顺序一次性分配。在 `detailed_description` 的每个实际发声事件处复用对应 ID;`subject_definitions` 中与目标说话者绑定的 `<Audio N>` 定义同样复用该 `(Sx)`,但绝不独立分配新 ID。不要在 `retention_analysis` 中写 `(Sx)`。仅存在于直接复用的 BGM 或完整配乐中的口头唱词使用 `<Audio N>`;由真人、角色、旁白或其他独立发声来源物理产生的声音使用 `(Sx)`。

## 6. `overall_soundscape` 与 `non_diegetic_music`

这两类声音的定义遵循视频提示词撰写指南(T2VA / I2VA / FL2VA / L2VA)。

`overall_soundscape` 概括整片范围内的环境氛围声与物理音效。对话、歌唱以及与特定镜头同步的声音事件仍留在 `detailed_description`:

```text
overall_soundscape: Quiet indoor room tone and a low ventilation hum continue throughout the video.
```

`non_diegetic_music` 描述角色听不到、仅观众可闻的背景音乐。当存在音乐时,说明其配器、速度与力度发展:

```text
non_diegetic_music: A restrained solo-piano score at a slow tempo, with sustained low cello underneath and no swell.
```

当使用参考音频时,只在与其可闻层匹配的部分说明其复制或引用关系:环境氛围声与音效归入 `overall_soundscape`,仅观众可闻的配乐归入 `non_diegetic_music`。如果同一段音频同时提供两类内容,则在各相应部分分别描述其关系:

```text
overall_soundscape: The copied ambience layer from <Audio 1> continues throughout the target video.
non_diegetic_music: <Audio 2> is directly reused as the complete audience-only score.
```

完整的对话与歌词只在 `detailed_description` 的 `<d>` 内书写,不要在这两个部分重复。

## 7. 完整示例

<details>
<summary>显示完整示例</summary>

```text
subject_definitions:
<Subject 1> is the coffee-shop environment in <Picture 1>, featuring an exposed brick wall, an orange tufted sofa with patterned pillows, a neon sign, and a wooden coffee table.
<Subject 2> is the fluffy white Samoyed in <Picture 2>, <Picture 3>, and <Picture 4>, with thick white fur, pointed ears, a dark nose, and a curved tail.
<Subject 3> is the young blonde woman in <Video 1>, with long blonde hair and a light-pink button-down shirt with rolled-up sleeves.
<Subject 4> is the young man in <Video 2>, with short wavy brown hair and a dark-grey hoodie with drawstrings.
<Audio 1> is the voice-timbre reference for <Subject 3> (S1), containing a spoken English vocal layer.

summary:
[reference generation + audio reference] The target video shows <Subject 3> eating a cookie in <Subject 1>. <Subject 4> enters with <Subject 2>, which lunges toward the cookie. The three-shot exchange uses <Audio 1> as the voice-timbre reference for <Subject 3> and ends with a canned audience laugh.

retention_analysis:
<Subject 1> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - the exposed brick wall, orange tufted sofa, patterned pillows, neon sign, and wooden coffee table are retained.
<Subject 2> (appears in [Shot 1], [Shot 2]): fully_preserved - the Samoyed's thick white fur, pointed ears, dark nose, and curved tail are retained.
<Subject 3> (appears in [Shot 1], [Shot 2], [Shot 3]): fully_preserved - the blonde woman's identity, long hair, and light-pink shirt are retained.
<Subject 4> (appears in [Shot 1], [Shot 2]): fully_preserved - the young man's short wavy brown hair and dark-grey hoodie are retained.
<Audio 1>: reference - its vocal timbre guides the dialogue delivery of <Subject 3> without copying the original signal.

detailed_description:
The target video uses a realistic multi-camera sitcom style with warm indoor lighting.
[Shot 1] A medium shot establishes <Subject 1>, the coffee shop with its exposed brick wall, orange tufted sofa, patterned pillows, neon sign, and wooden coffee table. <Subject 3> (S1), the young woman with long blonde hair and a light-pink button-down shirt with rolled-up sleeves, sits on the sofa holding a chocolate-chip cookie. From the left, <Subject 4>, the young man with short wavy brown hair and a dark-grey hoodie with drawstrings, enters holding the leash of <Subject 2>, the thick-furred white Samoyed with pointed ears, a dark nose, and a curved tail. The dog lunges toward the cookie and pulls the leash taut. <Subject 3> (S1) jerks her hand back and, using the clear youthful voice timbre referenced from <Audio 1>, exclaims with light annoyance, <d>[English] Hey! Watch your dog!</d> She closes her lips and guards the cookie while <Subject 4> pulls the dog back.
[Shot 2] At 00:03.000, the shot cuts to a close-up of <Subject 4> (S2), the young man in the dark-grey hoodie from Shot 1, sitting beside <Subject 3> on the sofa and holding <Subject 2> securely in his arms. <Subject 4> (S2) says in a casual young male voice with a playful tone and an easy conversational pace, <d>[English] He just likes cookies more than me.</d> He closes his mouth into an apologetic smile and strokes the dog's thick white fur.
[Shot 3] At 00:05.000, the shot cuts to a close-up of <Subject 3> (S1), the blonde woman in the light-pink shirt from Shot 1. Her annoyance softens as she looks toward the Samoyed. <Subject 3> (S1) replies in the same clear youthful voice referenced from <Audio 1> with an amused cadence, <d>[English] Well, he has good taste at least.</d> She smiles and raises the cookie in a small toast-like gesture. A classic canned audience laugh begins immediately after the line and continues through the final frame.

overall_soundscape:
Soft indoor coffee-shop room tone continues throughout the scene.

non_diegetic_music:
N/A
```

</details>
