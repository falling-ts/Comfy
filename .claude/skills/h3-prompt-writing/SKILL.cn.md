---
name: h3-prompt-writing
description: |
  为 MiniMax H3 视频生成编写提示词,支持 T2VA、I2VA、FL2VA、L2VA 与完整参考 Ref2VA 五种模式。当需要把多模态请求改写成 H3 提示词结构、撰写 integrated_multimodal_description / overall_soundscape / non_diegetic_music、对齐关键帧、或为图片/视频/音频定义参考标签时使用。
trigger-words: [H3提示词, H3 prompt, 视频提示词, T2VA, I2VA, FL2VA, L2VA, Ref2VA, 参考生视频, 参考视频, integrated_multimodal_description, 多模态描述, 关键帧对齐]
---

# H3 提示词写作

## 工作流

1. 识别输入模式:T2VA、I2VA、FL2VA、L2VA,或完整参考 Ref2VA。
2. 基础文本/关键帧模式:阅读 `references/base-cn.md`(中文版;英文原版 `base-en.txt`)并按其最终提示词结构编写。
3. 完整参考模式:阅读 `references/ref-cn.md`(中文版;英文原版 `ref-en.txt`)并按其六段式改写格式编写。
4. 严格保留所选指南中的**字段名、段落顺序、标签和时间标记写法**(大小写一致,不可改动)。

> 说明:`references/` 下同时提供中文版(`base-cn.md` / `ref-cn.md`)与英文原版(`base-en.txt` / `ref-en.txt`)。其中的字段名(`integrated_multimodal_description` 等)与时间标记(`At 00:SS.mmm`、`S.SS-second`)必须按原样书写,中英文版一致;中文版便于理解,英文原版用于精确保留字段格式。

## 基础模式

- **T2VA**:从文本构建完整的音视频时间线。
- **I2VA**:从首帧出发,沿时间线向前连续发展。
- **FL2VA**:描述首帧与尾帧之间的连续路径(推荐单镜头)。
- **L2VA**:推断一个合理的开场,并收敛到给定的尾帧。

按 `references/base-cn.md` 所示顺序使用三个核心字段:`integrated_multimodal_description`、`overall_soundscape`、`non_diegetic_music`。

## 完整参考模式(Ref2VA)

Ref2VA 改写按以下**六段式**顺序组织:`subject_definitions`、`summary`、`retention_analysis`、`detailed_description`、`overall_soundscape`、`non_diegetic_music`。

参考标签(`<Subject N>` / `<Picture N>` / `<Video N>` / `<Audio N>`)在全部段落中保持同一含义。

阅读 `references/ref-cn.md` 获取标签规则、保留分析(retention_analysis)和完整示例。

## 输出规则

- 改写段落用英文撰写;对话、歌词和画面内可见文字保留原文语言。
- 每个镜头按构图、主体、环境、动作、运镜、声音,以及参考内容出现的**精确时间点**来描述。
- 避免:写成剧情梗概、悬而未决的参考标签、与请求时长不符的时间标记。

---

## 附:两种模式的提示词骨架

### 基础模式(T2VA/I2VA/FL2VA/L2VA)

```text
[I2VA 示例对齐指令]
For the target video, at 0.00 seconds into the target video, <Picture 1> (from [Shot 1]) is fully referenced.

integrated_multimodal_description: [Shot 1] 风格,景别,主体与构图;随后动作/运镜/台词... [Shot 2] At 00:03.500, the camera cuts to ...
overall_soundscape: 环境声、动作声、非语言人声...
non_diegetic_music: 背景音乐风格...
```

### 完整参考模式(Ref2VA)六段式

```text
subject_definitions: <Subject 1> is ... ; <Picture 2> is ... ; <Video 1> is ... ; <Audio 1> is ...
summary: 任务类型、目标视频、主要参考关系...
retention_analysis: 各参考项出现位置与保留/转移/复用情况...
detailed_description: [Shot 1] ... [Shot 2] At 00:SS.mmm ...
overall_soundscape: ...
non_diegetic_music: ...
```
