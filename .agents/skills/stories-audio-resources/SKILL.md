---
name: stories-audio-resources
description: Audio and extraction resource types for the story library — video frame extraction, video audio extraction, background music, ambient sound, effect sound, text-to-speech voice, reference voice, and audio clipping. Use when writing or editing an audio resource table or performing frame/audio extraction.
---

# 故事库音频与拆解类资源规范

> 所有类型共用 `stories/AGENTS.md` 的「资源 ID 规则」与「表格 md 文件规范说明」（后者见技能 `stories-resource-tables`）。

### 视频拆帧

即通过节点获取视频所有帧数的图片，包含ID，原视频(VIDEO)

#### 写入时机

**需要我明确说明写入哪些内容时，才可以写入**；分析正文内容时，**不允许自动写入**。

### 视频拆音

即通过节点获取视频的音频，并支持截取指定秒数的音频，包含ID，原视频(VIDEO)，开始秒数(INT)，结束秒数(INT)

#### 写入时机

**需要我明确说明写入哪些内容时，才可以写入**；分析正文内容时，**不允许自动写入**。

### 背景音乐

即通过提示和秒数获取背景音乐，包含ID，音乐提示词(TEXT)，秒数(INT)

#### 写入时机

**需要我明确说明写入哪些内容时，才可以写入**；分析正文内容时，**不允许自动写入**。

### 环境音效

即通过提示和秒数获取环境音效，包含ID，音效提示词(TEXT)，秒数(INT)

#### 写入时机

**需要我明确说明写入哪些内容时，才可以写入**；分析正文内容时，**不允许自动写入**。

### 效果音效

即通过提示和秒数获取效果音效，包含ID，音效提示词(TEXT)，秒数(INT)

#### 写入时机

**需要我明确说明写入哪些内容时，才可以写入**；分析正文内容时，**不允许自动写入**。

### 文生人声

即通过提示和情绪获取说话的声音，包含ID，内容(TEXT)，情绪(TEXT)

#### 写入时机

**需要我明确说明写入哪些内容时，才可以写入**；分析正文内容时，**不允许自动写入**。

### 参考人声

即通过原人声，提示和情绪获取音色一致的其它说话内容，包含ID，原人声(AUDIO)，内容(TEXT)，情绪(TEXT)

#### 写入时机

**需要我明确说明写入哪些内容时，才可以写入**；分析正文内容时，**不允许自动写入**。

### 截取声音

即通过节点获取指定时间段的声音，包含ID，原声音(AUDIO)，开始秒数(INT)，结束秒数(INT)

#### 写入时机

**需要我明确说明写入哪些内容时，才可以写入**；分析正文内容时，**不允许自动写入**。
