---
sorting-spec: |
    target-folder: /*
    < true a-z
---

# 文件浏览器排序规则(Custom File Explorer sorting)

本文件是 **Custom File Explorer sorting** 插件的排序规格(`sortspec`), 由
`.obsidian/plugins/custom-sort`(源码在 `stories/plugins/custom-sort`, git 子模块)读取。

## 为什么要这一条

Obsidian 文件浏览器自带的「按名称 A→Z」**不是**逐字节字典序, 而是自然排序 ——
它内部写死 `new Intl.Collator(void 0, {usage:"sort", sensitivity:"base", numeric:!0})`,
`numeric:true` 会把连续数字当**数值**比较, 于是资料表的 5 位编号会被拆散:

| 排序口径 | `00110_万物建模2.1.md` 的位置 |
|---|---|
| Obsidian 原生(numeric) | 排在 `0020` 之后, 被甩到最后 |
| `< true a-z`(本配置) | 紧跟 `0011_万物建模.md`, 与 `0012_万物变化.md` 相邻 |

`< true a-z` 触发插件的 "true alphabetical" 模式, 即逐字符比较(UTF-16 code unit),
数字段不再数值化, 所以同族编号(`0011` / `00110`)会聚在一起。

## 生效方式

`target-folder: /*` 表示应用到 vault 内所有文件夹及其子文件夹。
改动本文件后, 点左侧边栏的 custom-sort ribbon 图标重新解析并应用。
