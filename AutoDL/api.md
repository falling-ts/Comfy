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
