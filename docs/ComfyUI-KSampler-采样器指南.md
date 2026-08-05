# ComfyUI KSampler 采样器指南

> 来源:ComfyUI 0.30.0 源码 `comfy/k_diffusion/sampling.py` + 运行中 `/object_info/KSampler` 官方列表(共 44 个采样器)。
> 更新日期:2026-08-05

## 一、官方完整列表

```
euler, euler_cfg_pp, euler_ancestral, euler_ancestral_cfg_pp,
heun, heunpp2, exp_heun_2_x0, exp_heun_2_x0_sde,
dpm_2, dpm_2_ancestral, lms, dpm_fast, dpm_adaptive,
dpmpp_2s_ancestral, dpmpp_2s_ancestral_cfg_pp,
dpmpp_sde, dpmpp_sde_gpu,
dpmpp_2m, dpmpp_2m_cfg_pp,
dpmpp_2m_sde, dpmpp_2m_sde_gpu, dpmpp_2m_sde_heun, dpmpp_2m_sde_heun_gpu,
dpmpp_3m_sde, dpmpp_3m_sde_gpu,
ddpm, lcm, ipndm, ipndm_v, deis,
res_multistep, res_multistep_cfg_pp, res_multistep_ancestral, res_multistep_ancestral_cfg_pp,
gradient_estimation, gradient_estimation_cfg_pp,
er_sde, seeds_2, seeds_3, sa_solver, sa_solver_pece,
ddim, uni_pc, uni_pc_bh2
```

## 二、按算法族分组说明

### 1. 一阶基础

| 采样器 | 核心作用 | 使用场景 |
|---|---|---|
| `euler` | 一阶欧拉,每步直线前进 | **通用首选**;Lightning/Turbo 蒸馏模型**必须用它**(训练轨迹一致);Qwen-Image 官方默认 |
| `euler_ancestral` | euler + 每步额外加噪(祖先噪声) | 想要更多变化/创造性细节,能接受不可复现 |

### 2. 二阶预测校正(质量好,耗时约 2 倍)

| 采样器 | 核心作用 | 使用场景 |
|---|---|---|
| `heun` | 二阶预测-校正 | 步数少(10~20)时质量优于 euler |
| `heunpp2` | heun 改进版 | 同上,质量更好 |
| `dpm_2` | DPM-Solver 二阶 | 中低步数高质量,较少用 |
| `dpm_2_ancestral` | dpm_2 + 祖先噪声 | 需要二阶质量 + 随机变化 |
| `exp_heun_2_x0` | 指数 Heun(x0 参数化) | **Flux/整流流模型官方推荐** |
| `exp_heun_2_x0_sde` | 其随机版 | Flux 想要更多变化时 |

### 3. 多步/高阶(确定性,通用高质量)

| 采样器 | 核心作用 | 使用场景 |
|---|---|---|
| `dpmpp_2m` | DPM-Solver++ 二阶多步 | **通用高质量首选**,10~30 步;SD/SDXL/Qwen 都适合 |
| `lms` | 四阶线性多步 | 步数够多时细腻;步数少易过冲 |
| `ipndm` / `ipndm_v` | 高阶伪数值方法(4 阶) | 少步数高质量,较少用 |
| `deis` | 高阶指数积分器 | 少步数(5~15)高质量,追求效率 |
| `res_multistep` | 残差多步(新) | 新求解器可试;`_ancestral` 为随机版 |
| `gradient_estimation` | 梯度估计法(新) | 实验性,少步数场景可试 |
| `seeds_2` / `seeds_3` | SEEDS 二阶/三阶(新) | 少步数高质量新方案 |
| `sa_solver` / `sa_solver_pece` | SA-Solver(PECE 模式) | 少步数(5~10)高质量,速度 + 精度兼顾 |
| `ddim` | DDIM 确定性采样 | 老式工作流/科研,通用性一般 |
| `uni_pc` / `uni_pc_bh2` | UniPC 均匀预测校正 | 少步数高质量,曾流行 |

### 4. SDE/随机(更细腻,更慢,更不可复现)

| 采样器 | 核心作用 | 使用场景 |
|---|---|---|
| `dpmpp_2s_ancestral` | DPM++ 2S + 祖先噪声 | **SDXL 插画/质感流行款**,细节丰富有灵气 |
| `dpmpp_sde` | DPM++ 随机微分方程 | 高质量不赶时间,细节最细腻 |
| `dpmpp_2m_sde` / `_heun` / `_gpu` | 2M + SDE 噪声 | 想要 2M 稳定性又带随机细节 |
| `dpmpp_3m_sde` / `_gpu` | 三阶 SDE | 最高质量档,慢 |
| `er_sde` | 指数积分 SDE(新) | 实验性高质量档 |

### 5. 蒸馏专用

| 采样器 | 核心作用 | 使用场景 |
|---|---|---|
| `lcm` | LCM 蒸馏模型专用(1~4 步) | LCM LoRA/模型快速出图 |

### 6. CFG++ 引导变体

`euler_cfg_pp`、`euler_ancestral_cfg_pp`、`dpmpp_2s_ancestral_cfg_pp`、`dpmpp_2m_cfg_pp`、`res_multistep_cfg_pp`、`res_multistep_ancestral_cfg_pp`、`gradient_estimation_cfg_pp`

- 核心作用:换用 CFG++ 引导公式,**提示词遵循更强、色彩过饱和更少**
- 使用场景:提示词难服从、画面发腻发艳时;配合对应基础采样器使用

### 7. 自适应

| 采样器 | 核心作用 | 使用场景 |
|---|---|---|
| `dpm_fast` | 自动选阶数/步数 | 不想调参、求省事 |
| `dpm_adaptive` | 按误差自适应步长 | 同上,质量稳定但耗时不可控 |

## 三、实践推荐速查

| 场景 | 推荐采样器 |
|---|---|
| Qwen-Image 4 步(Lightning LoRA) | **`euler` + `simple`(唯一选择,蒸馏轨迹固定)** |
| Qwen-Image 20 步 | `euler` + `simple`(官方默认);想抠细节可试 `dpmpp_2m` |
| Flux / Klein 分块重绘 | `euler`(官方路径)或 `exp_heun_2_x0`(Flux 高质量) |
| 一般 SD/SDXL 高质量 | `dpmpp_2m`(稳)或 `dpmpp_2s_ancestral`(有灵气) |
| 快速试稿(非蒸馏) | 低步数 `dpmpp_2m` / `sa_solver` |
| 蒸馏快速出图 | Lightning/Turbo → `euler`;LCM → `lcm` |
| 提示词不听、颜色发艳 | 对应采样器换 `_cfg_pp` 版 |
| 想要变化/多样性 | `euler_ancestral`、`dpmpp_2s_ancestral`、`*_sde` 系列 |
| 视频工作流 | 以官方 `euler` 为主 |

## 四、本机已知坑

- **Qwen-Image fp8 + Sage Attention 4 步必黑屏**(euler/dpmpp 都一样),根源是 fp16 注意力溢出;4 步请关 `--use-sage-attention`,或用 20 步 + sage。
- **4 步 Lightning 不要换 dpmpp_2m**:即使不黑屏,也偏离蒸馏轨迹,画质不对。
