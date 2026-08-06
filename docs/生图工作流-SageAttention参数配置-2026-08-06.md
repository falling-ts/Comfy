# 生图工作流 SageAttention(KJNodes)参数配置(2026-08-06)

适用范围:项目内全部生图(图片类)工作流的 `PathchSageAttentionKJ` 加速节点。统一参数:**`sage_attention = sageattn_qk_int8_pv_fp16_triton`,`allow_compile = False`**。

---

## 一、本机环境实测(2026-08-06)

| 项目 | 值 | 对参数选择的影响 |
|---|---|---|
| GPU | NVIDIA GeForce RTX 4060(8GB,**Ada / SM89**) | 非 Blackwell → **排除 `sageattn3` 系列**(仅 RTX 50 系/B200) |
| 驱动 / CUDA | 驱动 610.88,CUDA **13.0**(torch 2.13.0+cu130) | ≥12.4,fp8 可用;但见下「精度」取舍 |
| sageattention | **2.2.0.post6**(backups 有 wheel 备份) | 提供 `sageattn_qk_int8_pv_*` 全系列 |
| triton | 3.7.1(已装) | `..._triton` 后端可用(备用) |
| torch 注意 | torch 2.13 SDPA 损坏(已验证),ComfyUI 默认 sub_quad 绕过 | 尽量少引入 torch.compile 等变量 |

## 二、参数选择依据

### 为什么选 `sageattn_qk_int8_pv_fp16_triton`

1. **精度最高**:本机 FP64 基准验证 cosine——`pv_fp16_cuda` 与 `pv_fp16_triton` = **0.9999**;`fp8_cuda`、`auto` = 0.9993。生图链路(尤其修线、分块重绘)对细节保真敏感,选 0.9999 档。
2. **省显存**:RTX 4060 仅 8GB,却要跑 20B 的 Qwen-Image-2512 / Edit-2511(fp8/bf16)与 Klein 9B。`qk_int8` 把注意力打分(QKᵀ)压到 INT8,显著降显存、提速度。
3. **PV 保持 FP16(不用 fp8)**:模型本身已是 fp8 量化(2512 / Klein),PV 再降 FP8 会叠加量化误差;分块重绘对拼接/细节极敏感,保持 FP16 更稳。
4. **Triton 后端实测更快(本机 RTX 4060 基准)**:同精度(两端输出余弦 1.00000)下,Triton 比 CUDA 内核快 **7%~17%**(seq 2048~8192、head_dim 128,见下表),采样 20 步累计收益明显;triton 3.7.1 已装且实测稳定,因此选 Triton。

**Triton vs CUDA 后端实测(RTX 4060,head_dim=128,fp16):**

| 序列长度 | 头数 | CUDA | Triton | 提升 |
|---|---|---|---|---|
| 2048 | 12 | 0.728 ms | 0.618 ms | +15% |
| 2048 | 24 | 1.466 ms | 1.276 ms | +13% |
| 4096 | 12 | 2.591 ms | 2.246 ms | +13% |
| 4096 | 24 | 5.113 ms | 4.249 ms | +17% |
| 8192 | 12 | 9.181 ms | 8.488 ms | +8% |
| 8192 | 24 | 19.039 ms | 16.446 ms | +14% |

> 若 Triton 在某模型/形状下报错,可临时切回 `sageattn_qk_int8_pv_fp16_cuda`(同精度,仅慢 7~17%)。

### 为什么 `allow_compile = False`

- False(默认)= 对 sage 函数执行 `torch.compiler.disable()`,关闭 torch.compile;
- 理由:本机 torch 2.13 的 SDPA 已确认损坏,环境处于"减少变量"状态;torch.compile 首次编译有延迟且对 torch/驱动版本敏感;8GB 显存跑 20B 模型,编译收益不明显;
- 若未来升级 torch 修复版,可试点 `allow_compile = True`(需 sageattn 2.2.0+)对比提速。

## 三、已配置节点清单(7 个,全部同参数)

| 工作流 | 节点 | 作用模型 | 链路位置 |
|---|---|---|---|
| 图片-01-文生图 | 5709 | Qwen-Image-2512 fp8(主生成) | UNET → Kook LoRA → Sage → Lightning/开关 → 采样 |
| 图片-01-文生图 | 5710 | Qwen-Image-Edit-2511(修线) | Edit UNET → Lightning → 3DChineseStyle → Sage → 采样 |
| 图片-01-文生图 | 5711 | FLUX.2 Klein 9B(分块重绘) | Klein UNET → Sage → CFGGuider → 分块 |
| 图片-04-人物建模-主图 | 5101 | Qwen-Image-2512(主生成) | UNET → Lightning/开关 → Sage → 采样 |
| 图片-04-人物建模-主图 | 5102 | FLUX.2 Klein(分块重绘) | Klein UNET → Sage → CFGGuider |
| 图片-07-物体建模-主图 | 5101 | Qwen-Image-2512(主生成) | 同 04 |
| 图片-07-物体建模-主图 | 5102 | FLUX.2 Klein(分块重绘) | 同 04 |

> 图片-02/03/05/06/08:03 为纯放大无扩散模型;02/05/06/08 为 Qwen-Edit 子图封装(模型在子图内部),未加 Sage 节点。

## 四、故障与备用方案

| 现象 | 处理 |
|---|---|
| 某模型在该模式下报错/显存不足 | 先切 `auto`(自动选内核,0.9993);仍不行切 `disabled` 临时关闭 |
| Triton 后端异常 | 切回 `sageattn_qk_int8_pv_fp16_cuda`(同精度,慢 7~17%) |
| 想极限提速(可接受略降精度) | `sageattn_qk_int8_pv_fp8_cuda++`(SageAttention2++,需 CUDA 12.4+,本机满足) |
| 换 50 系显卡后 | 可试 `sageattn3` / `sageattn3_per_block_mean`(Blackwell 专属,需 `pip install sageattn3`) |
| 恢复默认注意力 | 该节点下拉选 `disabled` 即可(节点设计为不可旁路,需显式切 disabled) |

---

> 更新说明:2026-08-06 环境实测后统一配置;如更换显卡/升级 torch,按第二节依据重新评估。
