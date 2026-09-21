# AutoDL 市场搜索接口与本次抓取过程（2026-08-06）

## 0. 结论速览

- 市场列表网页 `https://www.autodl.com/market/list` 是 Vue SPA,数据不在 HTML 里,由前端 JS 调接口获取。
- 核心接口:**`POST https://www.autodl.com/api/v1/machine/search`**(按量市场全量搜索)。
- 辅助接口:`GET https://www.autodl.com/api/v1/machine/gpu_type`(全部 GPU 型号列表)。
- 认证方式:**`Authorization: <token>`(直接放 token,不带 Bearer)**;带 `Bearer ` 前缀反而报「登录超时」。
- ⚠️ **token 属于敏感凭据:本文件不保存真实 token**,按项目既有约定(RunningHub 指南同款)只记录方法;token 从浏览器登录态或用户提供处获取。

## 1. 前端反推过程(怎么找到接口的)

1. 抓 `https://www.autodl.com/market/list` HTML → 得到入口 JS `/assets/index.3cee420f.js`(仅 2.9KB,是路由壳)。
2. 由入口 JS 的 import 找到分包:`service-code.1d10a170.js`、`components.3fce0056.js`、`vendor.9ce653cc.js`、`index.37bc62fd.js` 等。
3. 在 `index.37bc62fd.js` 的路由表里找到市场列表组件:`/assets/index.14d7445c.js`(路由 `market/list` → `market-instance-list`)。
4. 在 `index.14d7445c.js` 中看到请求体构造:

```js
{
  charge_type: "payg",
  region_sign_list: [],
  gpu_type_name: [],
  machine_tag_name: [],
  gpu_idle_num: 0,
  mount_net_disk: false,
  instance_disk_size_order: "",
  date_range: "", date_from: "", date_to: "",
  page_index: 1,
  page_size: 10,
  pay_price_order: "",
  gpu_idle_type: "",
  default_order: true
}
```

5. 在 `service-code.1d10a170.js` 确认接口路径:`De = { findAll:"api/v1/user/machine/list", search:"api/v1/machine/search", ... }`;市场列表实际用 **`api/v1/machine/search`**(实测返回 `result_total=3194` 台按量机器;`user/machine/list` 返回的是自己名下的实例,注意区分)。

## 2. 接口详情

### 2.1 市场搜索(本报告主用)

- `POST https://www.autodl.com/api/v1/machine/search`
- Headers:`Authorization: <token>`、`Content-Type: application/json`
- Body(关键字段):
  - `charge_type`:"payg"(按量计费)/ "daily" / "weekly" / "monthly" / "yearly"
  - `gpu_type_name`:数组,如 `["RTX 5090 D"]`,空数组 = 全部
  - `region_sign_list`:数组,空 = 全部区域
  - `gpu_idle_num`:0 = 含空闲为 0 的机器;大于 0 可过滤“必须有空闲卡”
  - `page_index` / `page_size`:`page_size` 实测最大 100,超过按 100 截断;翻页需循环直到 `list.length < page_size` 或达到 `result_total`
  - `pay_price_order` / `default_order`:实测传空 + `default_order=true` 即可;`pay_price_order` 需配合前端 URL query 使用,建议本地排序更稳
- 返回:`data.list[]`,每条机器含:
  - `gpu_name` / `gpu_number`(整机卡数)/ `gpu_memory`(字节)/ `gpu_idle_num`(空闲卡数)
  - `region_name`(如“西北B区”)/ `region_sign`(如 `west-E`,下单用)
  - `machine_sku_info[]` 中 `type=="payg"` 的 `current_price`(**单位:厘**,即 1000 厘 = ¥1/时);另有 `level_config`(普通用户 100%,会员 95%)
  - `cpu_per_gpu` / `mem_per_gpu` / `highest_cuda_version` / `driver_version` / `machine_id`

### 2.2 GPU 型号列表

- `GET https://www.autodl.com/api/v1/machine/gpu_type`
- 返回 `data[]`,含 `gpu_name`、`gpu_memory`(字节);本次实测到 28 个型号,含 `RTX 5090 D`、`RTX 5090`、`RTX 4090/4090D/3090`、`vGPU-32/48GB`、`A100-PCIE-40GB`、`A800-80GB`、`H20/H800`、`RTX PRO 6000`、`RTX 6000D`、`V100-32GB` 等。

## 3. 本次抓取记录

- 时间:2026-08-06(实时行情,价格会波动,报告仅供当天参考)。
- 候选卡型 14 种,全部分页拉取,共 **2705 台**按量机器:
  - RTX 3090(206)、vGPU-32GB(374)、RTX 4090(654)、RTX 4090D(318)、V100-32GB(30)、RTX 5090 D(29)、RTX 5090(571)、vGPU-48GB(137)、A100-PCIE-40GB(28)、A800-80GB(58)、RTX 6000D(20)、RTX PRO 6000(250)、H20-NVLink(18)、H800(12)。
- 原始数据临时保存在 `%TEMP%\autodl_market_payg_full.json`(本次会话临时文件,不在仓库内)。
- 筛选逻辑:显存 ≥24GB → 排除 V100(旧架构)/vGPU-32GB(虚拟卡)/<24GB → 按最低价升序 → 结合模型栈给出首选(5090 D)。

## 4. 常见问题

- 带 `Bearer ` 前缀报「登录超时」→ 改回裸 token。
- 返回 `code=AuthorizeFailed` / 登录超时 → token 过期或无效(JWT `exp` 字段约 2026-10);重新从登录态获取。
- 只要价格 → 直接对返回 JSON 按 `machine_sku_info` 里 payg 的 `current_price` 排序;注意单位是厘。
- 只想要有货的 → 过滤 `gpu_idle_num > 0`,或请求体 `gpu_idle_num: 1`。

## 5. 云上模型库读取方法(autodl.art,2026-08-06 实测)

> 页面 `https://www.autodl.art/app/common/model` 是 **AutoDL.Art 社区站**(域名独立,登录态与 autodl.com 不通用)。
> 同一账号可在 autodl.art 登录后从浏览器 Network 复制 token;autodl.com 市场的 token 在这里无效。

### 5.1 认证方式

- 请求头:`Authorization: <token>`(**裸 token,不带 Bearer**,与 autodl.com 市场一致)
- autodl.art 签发的 JWT:`aud = cg_website`(社区站);autodl.com 的是 `aud = website`,两者不通用
- ⚠️ **token 属于敏感凭据:不写入本文件、不提交 git**(与 §0 同约定)
- 失败特征:裸 token 有效时返回 `{"code":"Success","data":{...}}`;无效/过期返回 `{"code":"AuthorizeFailed","msg":"认证失败; 登录超时"}`;带 `Bearer ` 前缀也会失败

### 5.2 模型文件搜索(核心接口)

- 接口:`POST https://www.autodl.art/api/v1/application/model/file/search`
- Body(**注意参数名**):

```json
{
  "page_index": 1,
  "page_size": 100,
  "file_name": "qwen_image_2512",
  "model_repository": ""
}
```

- `file_name` / `model_repository` 二选一(分别按文件名、模型仓库名过滤);**传 `keyword` 会被忽略**(实测任意关键词都返回同一批最新上传,100 条封顶)
- `page_size` 实测最大 100
- 返回 `data.list[]`,每条含:
  - `model_name` / `file_name`(文件名可能带 `<em>` 高亮标签,需清洗)
  - `file_size`(字节)、`md5`(可校验一致性)、`model_repository`(来源仓库)
  - `instance_path`(如 `/.autodl/93/e7/54/<md5>`,云上存储路径)
  - `user_info.username`(上传者)、`created_at` / `updated_at`

#### 5.2.1 2026-09-17 复核修正(接口已比初版完善)

- 返回体 `data` 现含 **`result_total` / `max_page` / `offset` / `page_index` / `page_size` / `page`**。
  初版记的「`data.total` 恒为 null」**已过时**:本次实测 `result_total = 4887`、`max_page = 49`,可直接用于分页。
- **终止条件必须用 `max_page` 循环**,不要用「返回条数 < page_size」:超出 `max_page` 后接口**重复返回最后一页**
  (实测第 50、60 页均返回与第 49 页相同的 87 条),按条数判断会重复计数。
- **必须按 `id` 去重**:跨页顺序不稳定 —— 实测第 48 页末条 `updated_at = 2025-10-30` 反而比第 47 页的 `2025-09-23` 更新,
  说明排序会抖动、翻页可能漏或重。本次按 `max_page` 拉全(48 页 ×100 + 87 = 4887),以 `id` 为键去重后恰为
  4887 条,与 `result_total` 完全吻合,无重复无遗漏。
- 条目实际字段:`id` / `created_at` / `updated_at` / `deleted_at` / `uid` / `model_name` / `file_name` /
  `model_repository` / `md5` / `note` / `file_size` / `file_status` / `instance_path` / `user_info` /
  `architecture_taxonomies` / `training_paradigms`。
  其中 **`model_name` 是归类时最有价值的信号**(同一 `model_name` 下的分片必属同一本地目录,可直接传播);
  `architecture_taxonomies` / `training_paradigms` 实测多为 `others`,暂无区分力。
- 更新脚本 `scripts/autodl-update-models.py`:token 走环境变量 `AUTODL_TOKEN`(不落盘);
  `models.md` 的「本地目录」列优先沿用旧 md 的 `instance_path` 映射(归类含人工判断,无法纯规则复现),
  再依次按 `model_name` 传播 → 仓库传播 → 文件名规则判定,判不出的标「未识别(需人工核对)」。

#### 5.2.2 2026-09-21 复核(4956 条)与脚本三处修复

- 本次抓取:`result_total = 4956`(较 09-17 的 4887 增加 69),新增实例路径 44、消失 0。
- ⚠️ **`max_page` 随请求的 `page_size` 变化**:`page_size=2` 时 `max_page=2478`、`page_size=100` 时 `max_page=50`,
  都等于 `ceil(result_total / page_size)`。用脚本默认的 100 即可,别拿小 page_size 试探时的 `max_page` 当固定值。
- 修复的三个归类缺陷(此前会让扩充的规则**永远不生效**,表现为新条目大量落进「未识别」):
  1. **「未识别」不再沿用**:旧值是「未识别」时清空 `_oldcat`,交给规则按新版本重判。
     否则按文件名(`@name:` 键)命中的旧结论会把新规则挡在外面 —— 同文件多次上传时尤其明显。
  2. **传播不传「未识别」**:`model_name` / 仓库传播只以**已识别**的归类作传播源,
     否则同组条目会被一起钉死在「未识别」上,同样进不了规则判定。
  3. **删掉 `guess()` 里「仓库名含 `/` 即 `return None`」的提前返回**:该判断位于文件名规则**之前**,
     使 `ace_step_1.5_turbo_aio`、`Realistic_Vision_V5.1` 之类被误判;目录型(二级槽位)本就由调用方按
     `g and "/" in r and g in SLOTS` 处理,无需提前返回。
- 归类规则同步扩充:Qwen3-VL 文本编码器、MoGe/VGGT 几何估计、MatAnyone/BiRefNet 抠像、
  ACE-Step/Stable Audio 音频 checkpoint、H3 系 Bridge/LoRA、Krea 系 LoRA、AnimeSharp/RCAN 放大等。
- 重跑方式(**不重新抓取,用缓存**):`AUTODL_USE_CACHE=1` + `AUTODL_OLD_MD=<旧备份 md>`,秒级完成;
  以旧备份为基准可保证已归好的条目照旧沿用,只有新条目走新规则,零回归风险(实测「已识别→未识别」退化 0 条)。

### 5.3 前端反推过程(接口变更后自查)

1. 抓 `https://www.autodl.art/app/common/model` HTML → 入口 JS `/assets/index.27e3033b.js`(772KB,主 bundle)
2. 主 bundle 路由表里找 `path:"common/model"` → 组件分包 `./model-search.40b72d2b.js`
3. `model-search.40b72d2b.js` 从 `./deploy.458d13b0.js` 导入接口函数
4. `deploy.458d13b0.js` 内定义:`Y = async a => (await t.post(`${r}/application/model/file/search`, a)).data`(`r = "/api/v1"`),导出为 `w` 供搜索页使用
5. 请求体参数在 `model-search.40b72d2b.js` 里构造:`{page_index, page_size, file_name, model_repository}`(搜索下拉只有「文件名 / 模型仓库名」两档)

### 5.4 实测结果摘要(2026-08-06)

- 库内含大量 Comfy-Org 官方 repackage 文件(上传者 `cg`)与社区上传(zealman / nahz202 / aistudent / O_O 等),热门模型基本齐全
- 已确认可用:Qwen-Image-2512 fp8(19.03G)、Qwen-Edit-2511 bf16(38.05G)/ fp8mixed(19.12G)、FLUX.2 Klein 9B fp8(8.79G)、MiniMax H3 fl2va/ref2va pruned int8(19.53G)、H3 VAE 与 4 步 LoRA、qwen3vl_32b nvfp4(注意:同名文件为 25.28G,与本地 14.61G 版本不同,勿混用)、Stable Audio 3、Qwen3-TTS 全系 zip、放大模型等
- 缺失:qwen3.5_2b_bf16(音频文本编码器)、4xNomos8kDAT、SenseVoiceSmall
- 拷贝到实例后:模型落在 `/root/autodl-tmp/`,需 `ln -s` 到 ComfyUI models 或配置 `extra_model_paths.yaml`,并确认文件名与工作流引用一致
