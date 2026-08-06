# LiblibAI(哩布哩布)模型库搜索方法(2026-08-06 逆向实录)

调研日期:2026-08-06。用途:LiblibAI 模型库按「底模 × 下载量」搜索/排行的可复现方法。Liblib 网页本身**没有"下载量"排序档**(仅推荐/最新/最热),正确姿势是拉全量后用返回的 `downloadCount` 字段本地排序。

## 1. 核心接口

```
POST https://www.liblib.art/api/www/model/search
Content-Type: application/json
```

**请求头**(实测无需复杂签名):

| 头 | 值 | 说明 |
|---|---|---|
| User-Agent | Mozilla/5.0 ... | 必填 |
| Referer | https://www.liblib.art/search | 必填 |
| Content-Type | application/json | 必填 |
| token | 可为空字符串 | 未登录也能搜 |
| webid | 任意字符串 | 本地生成即可 |

## 2. 请求参数(实测有效组合)

```json
{
  "keyword": "",
  "page": 1,
  "pageSize": 50,
  "types": [37],
  "models": [5],
  "tagIds": [],
  "scene": "ImgGenerator",
  "cid": "",
  "requestId": "任意字符串"
}
```

> 坑:不带 `cid`/`requestId` 时,`keyword` 会被服务器忽略,返回默认热门列表(混入大量 SD3.5 等不相关模型)。带空 `cid` + 任意 `requestId` 后 keyword 才生效。`pageSize` 最大 50(传 100 也只回 50)。

## 3. 底模类型(types)枚举 —— 从前端 JS 逆向

来源:网站 `_app-*.js` 内 baseType 枚举。**Qwen-Image(37)与 Qwen-Image-Edit(39)是分开的底模类型**。

| types 值 | 底模 |
|---|---|
| 19 | F1 / FLUX |
| 37 | QwenImage(文生图) |
| 39 | QwenEdit(图像编辑) |
| 21 | SD3.5 系 |
| 24 | Hunyuan |
| 27 | IMG1 |
| 30 / 55 | Seedream / Seedream45 |
| 31 | Kontext |
| 40 / 70 | Nano / Nano2 |
| 42 | Midjourney |
| 50 / 51 | F2Pro / F2Flex |
| 53 | ZImageTurbo |

## 4. 返回字段(按下载量排序用)

`data.data[]` 每条包含:

| 字段 | 说明 |
|---|---|
| `uuid` | 模型 ID,详情页 = `https://www.liblib.art/modelinfo/<uuid>` |
| `name` / `nickname` | 模型名 / 作者 |
| `downloadCount` | 下载量(排序依据) |
| `runCount` | 使用量(线上生成次数) |
| `heat` / `likeCount` / `commentCount` | 热度 / 点赞 / 评论 |
| `triggerWord` | 触发词(常为 null,需进详情页) |
| `baseType` / `modelType` | 底模数组(如 [37]) / 模型类型(5=LoRA) |
| `createTime` | 创建时间(用于版本窗口判定) |

## 5. 完整流程(按下载量排行)

1. 对目标底模调用搜索接口,`page` 从 1 递增,直到 `data.hasMore = false`(`total` 恒等于单页返回数,不可作为总数);
2. 跨页按 `id` 去重合并;
3. 按 `downloadCount` 降序排序;
4. 需要国漫/风格过滤时,对 `name`(必要时抓详情页 `versionDesc`)做关键词匹配;
5. 导出结果。

## 6. 底模版本(2512 / 2511)确认方法

Liblib 公开接口与 SSR 数据不提供版本级基模字段(只有大类 `baseType`)。版本确认采用:

- 名称/描述含 `2512` / `2511` 直接确认;
- 否则按发布窗口推断:Qwen-Image-2512 于 2025-12-31 发布,`createTime >= 2025-12-31` 的 QwenImage(37)LoRA 视为基于 2512;Qwen-Image-Edit-2511 于 2025-12-23 发布,`createTime >= 2025-12-23` 的 QwenEdit(39)LoRA 视为基于 Edit-2511(早于此窗口的可能是 1.0 / Edit-2509);
- 最严谨的确认:进模型详情页读作者描述(versionDesc)中"适合搭配大模型 / 基于 XX 训练"的原文。

## 7. 逆向路径备忘(接口变更后自查)

1. 搜索页 HTML 的 `__NEXT_DATA__` 提供 buildId 与 chunk 文件名;
2. 搜索业务在 `pages/search-*.js`(需 --compressed/gzip 解压);API client 在 `pages/_app-*.js`(请求拦截器只加 token + webid 头,无签名);
3. 搜索方法 `getModelSearchByKeyword` 在 `_app` 的 API 模块 p1 中,路径 `/api/www/model/search`;
4. 详情页在 `pages/modelinfo/[uuid]-*.js`,SEO meta 拼接 `versions[0].baseType`;
5. baseType 枚举也在 `_app` JS 中(QwenImage=37、QwenEdit=39)。

## 8. 注意

- 匿名可搜(返回公开数据);下载模型文件需登录,部分需积分/会员;
- 静态 JS 走阿里云 OSS CDN,下载时需带 `Referer: https://www.liblib.art/`,否则返回 445 字节 OSS 错误;
- 接口路径/枚举若变更,按 §7 重新逆向。
