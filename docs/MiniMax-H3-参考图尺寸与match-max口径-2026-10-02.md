# MiniMax H3 参考图尺寸与 match / max 口径（源码级复算）

> 日期：2026-10-02
> 对象：ComfyUI 核心 H3 节点（本机 v0.37.0）+ H3ReferenceSuite 加载器
> 问题：所有「转潜空间」节点的参考图像尺寸策略是什么；`ref_image_size` 的 `match` 与 `max` 差在哪；传 2K / 4K 会怎样、对结果是不是更好
> 依据：口径全部直接读源码，数字按源码公式复算（复跑方法见 §9）
> 相关：`docs/MiniMax-H3-参考保真度调研-2026-09-18.md`（保真度上限、AddGuide 杠杆）、`docs/MiniMax-H3-场景参考方式调研-2026-08-17.md`（多图 / 参考板 / 环绕视频）、`docs/MiniMax-H3-变体与加速方案调研-2026-09-11.md`

---

## 0. 结论摘要

1. **只有 `MiniMaxH3ReferenceToVideo` 的 `ref_image_size` 有 match / max 两种口径**；其余 H3 转潜空间节点都是**固定策略**：首/尾帧与 AddGuide 强行对齐到生成画布，参考视频走 768 短边规则，参考音频只做 32 kHz 重采样。
2. `match`：参考图缩到**与生成画布相同的像素面积**（只缩不放）；`max`：短边压到 **2048**（只缩不放）——后者正是官方参考管线的口径。
3. **同一份 resized 图同时喂 Qwen3-VL 与 VAE**（`ref_items` + `vae.encode`）。所以 match 的「变模糊」不只是像素条件变粗，**文本编码器看到的图像细节也一起降到了生成分辨率**——这是 max 的主要收益来源。
4. **4K 不等于 4K**：max 有「短边 ≤ 2048」硬上限，**3840×2160、7680×4320 与「短边 2048 的图」（16:9 = 3648×2048）在 max 下完全等价**，都变成 3648×2048 / 7296 token。想吃满细节要准备的是短边 2048 的素材，不是 4K / 8K。
5. **2K（2560×1440）与 FHD 不会被缩**（短边 1440 / 1080 < 2048），原样进入；**小于 2048 短边的图也不会被放大**。所以 max 对小素材同样不亏。
6. **分辨率不改变「参考在画面里占多大」**：H3 的 2D RoPE 是 area-normalized（`_axis_from_sqrt_area`），覆盖范围只由**宽高比**决定，分辨率只决定**采样密度**。想改善构图 / 运镜一致性，换 max 是无效的；max 改善的是**身份与细节保真**。
7. 代价：参考图 latent 在 pack 里 `img_update=False`，**从不加噪、每一步采样都参与 full attention**。480p 5s 下单张 4K max 让注意力 FLOPs 约 **2.1×**；768p 下只约 **1.35×**。**真正的额外大头在 Qwen3-VL-32B 的一次性 prefill**（vision token 390 → 7296）。
8. 多图时数量比单张分辨率更危险：**9 张 4K + max 在 480p 下 ≈ 26× 注意力，8 GB 卡基本必 OOM**；同场景改 match 只多 3510 token。

---

## 1. 全部 H3 转潜空间节点及其尺寸口径

核心节点都在 `ComfyUI/comfy_extras/nodes_minimax_h3.py`。

| 节点 | 图像输入 | 尺寸策略 | 源码 | 有 match / max |
|---|---|---|---|---|
| `EmptyMiniMaxH3LatentAV` | — | 只定画布（`CANVAS_MULTIPLE=32` 对齐） | L93-113 | 无 |
| `MiniMaxH3ImageToVideo`（t2va / fl2va） | `first_frame` / `last_frame` | **强制到生成画布**：首帧 `_resize(..., "disabled")` = 拉伸；尾帧 `"center"` = cover 裁切 | L146、L151 | 无 |
| `MiniMaxH3AddGuide` | `image`（单帧或整段 clip） | cover 到画布（`"center"`），clip 帧数裁到 17k+5（<5 帧只取第 1 帧） | L221 | 无 |
| `MiniMaxH3ReferenceToVideo`（ref2va） | `ref_image_0..8` | **match / max** | L296-311 | ✅ 唯一有 |
| 同上 | `ref_video_0..2` | `adapt_canvas`：短边 768、面积上限 768×1344、32 对齐；**源比它更小时回退原尺寸** | L53-64、L320-324 | 无 |
| `MiniMaxH3FunControlNetApply` | control 视频 / mask | `common_upscale(..., width, height, "center")` 到画布 | L428、L457 | 无 |
| `H3RefLoader`（refs/minimax-h3-guide） | input 目录批量选图 | **原样加载，不做任何缩放**（尺寸决策全在 `ref_image_N` 上） | `nodes.py` L44-51 | 无 |

补充口径（`nodes_minimax_h3.py` L29-32）：

```python
CANVAS_MULTIPLE   = 32      # 所有尺寸 32 对齐 ⇒ latent 16 对齐 ⇒ patchify(1,2,2) 整除
BASE_SHORT_EDGE   = 768     # 生成画布 / 参考视频的短边规则
MAX_PIXELS        = 768*1344
REF_IMAGE_SHORT_EDGE = 2048 # max 口径
```

---

## 2. match / max 的精确源码口径

`ComfyUI/comfy_extras/nodes_minimax_h3.py` L296-311（就这 6 行有效逻辑）：

```python
if ref_image_size == "match":
    scale = min(1.0, math.sqrt((width * height) / (w * h)))   # 面积对齐生成画布，只缩不放
else:
    scale = min(1.0, REF_IMAGE_SHORT_EDGE / min(w, h))       # 短边 2048，只缩不放
tw = max(CANVAS_MULTIPLE, round(w * scale / CANVAS_MULTIPLE) * CANVAS_MULTIPLE)
th = max(CANVAS_MULTIPLE, round(h * scale / CANVAS_MULTIPLE) * CANVAS_MULTIPLE)
resized = _resize(img[:1], tw, th, "disabled")               # lanczos，比例已保持故无变形
ref_items.append({"type": "image", "data": resized})          # ① 喂 Qwen3-VL
z = vae.encode(resized)                                       # ② 喂 VAE → latent
ref_blocks.append({"kind": "image", "latent_h": th // 16, "latent_w": tw // 16, "latent": z})
```

四个要点：

- **两支路同源**：① 与 ② 用的是同一份 `resized`（这是「match 会模糊」的根因，也是 max 同时改善语义与像素条件的原因）。
- **只缩不放**：`scale = min(1.0, ...)`——大图才压，小图照收。
- **32 对齐**：`tw / th` 必为 32 的倍数，于是 latent 尺寸是 16 的倍数、且能被 patchify 的 `(1,2,2)` 整除。
- **无变形**：`_resize` 用 `common_upscale(..., "lanczos", crop)`（L67-70）；`tw/th` 已按比例算出，`"disabled"` 的拉伸等价于等比缩放。唯一例外是 `round` 造成的 ±16px 级偏差（如 1080 → 1088）。

---

## 3. token 口径：每 32×32 像素 = 1 个 token

- DiT 侧：`patchify_video(latent, patch_size=(1,2,2))`（`comfy/ldm/minimax/model.py` L42）⇒ 每 token = 2×2 latent = **32×32 像素**；参考图 rows = `(th/32)*(tw/32)`，目标视频每 latent 帧 rows = `(H/32)*(W/32)`。
- Qwen3-VL 侧：`process_video_block(..., patch_size=16, merge_size=2)`（`comfy/text_encoders/minimax.py`）与 `process_qwen2vl_images(patch_size=16, merge_size=2)`（`comfy/text_encoders/qwen_vl.py` L9-19）⇒ factor = 32，语言侧 vision token ≈ `(h_bar/32)*(w_bar/32)`——**与 DiT 侧同口径**。
- **max 的参考 token 有闭式解**：短边 2048 ⇒ `token ≈ 4096 × 宽高比`。16:9 → 7296（对齐误差）；1:1 → 4096；21:9 → 9728。
- **match 的参考 token ≈ 生成画布自己的 token 数**（面积相同）：480p(832×480) → 390；768p(1344×768) → 1008。

⚠️ Qwen 侧还有一道独立限制：`max_pixels = 12845056`（约 12.85 MP，`qwen_vl.py` L39-46）。当短边 2048 且**宽高比 > 3.06:1** 时 Qwen 会二次缩小，而 VAE 用的是节点缩放后的全尺寸 ⇒ **两侧看到的分辨率不一致**。21:9（4864×2048 = 9.96 MP）安全；32:9 会踩到。

---

## 4. 复算表：同一张图在三种口径下的落点

生成档：480p = 832×480，768p = 1344×768。token 列 = Qwen vision token ≈ DiT 参考 rows。

| 参考图输入 | max 实际进入模型 | max token | match@480p | match@768p |
|---|---|---|---|---|
| 1024×1024 | 1024×1024（不放大） | 1024 | 640×640 (400) | 1024×1024 (1024) |
| 1344×768 | 1344×768 | 1008 | 832×480 (390) | 1344×768 (1008) |
| 1920×1080 FHD | 1920×**1088**（+0.7 %） | 2040 | 832×480 (390) | 1344×768 (1008) |
| 2560×1440「2K」 | 2560×1440（**不缩**） | 3600 | 832×480 (390) | 1344×768 (1008) |
| 3648×2048（短边 2048） | 3648×2048 | 7296 | 832×480 (390) | 1344×768 (1008) |
| **3840×2160「4K」** | **3648×2048** | 7296 | 832×480 (390) | 1344×768 (1008) |
| 4096×4096 | 2048×2048 | 4096 | 640×640 (400) | 1024×1024 (1024) |
| **7680×4320「8K」** | **3648×2048** | 7296 | 832×480 (390) | 1344×768 (1008) |
| 5120×2160（21:9） | 4864×2048 | 9728 | 960×416 (390) | 1568×672 (1029) |

---

## 5. 三条反直觉结论

### 5.1 4K / 8K / 短边-2048 图三者等价

max 的硬上限是短边 2048，超出部分**在进 VAE 之前就被丢掉**。所以传 4K、8K 与传一张 3648×2048 的图，模型看到的完全一样（同比例时）。**要"更好"应该准备短边正好 2048 的素材**，而不是更大的文件——更大的文件只多花读取与 lanczos 缩放的时间。

### 5.2 2K(1440p) / FHD 不会被缩，全部原样进入

因为 `scale = min(1.0, 2048/min(w,h))`：2560×1440 的短边 1440 < 2048 ⇒ scale = 1.0，原样 3600 token；1920×1080 同理（仅 `round` 把高度对齐到 1088）。也就是说 **max 是"封顶"而非"归一化"**：小素材保持原样，大素材压到 2048 短边。

### 5.3 分辨率不改变参考在画面里占多大

`comfy/ldm/minimax/model.py` L70-92：`_axis_from_sqrt_area(dim, patch, sqrt_area)` 里 `ratio = dim / sqrt_area`，坐标网格按 `sqrt(h*w)` 归一化；`_frame_grid` 用它生成参考图与目标帧各自的 2D 坐标。**参考图与目标帧各用自己的网格，但落在同一个归一化坐标空间**——覆盖范围只由**宽高比**决定，分辨率只决定**采样密度**。

推论：max 不会让参考内容在成片里变大 / 变小（那是宽高比与内容的函数），它只让同一块构图**采样更细**。因此：

- 想改善**构图 / 运镜 / 镜头一致性** → 换 max 无效，应改宽高比匹配、参考图内容与提示词。
- 想改善**身份 / 细节保真** → max 有效（见 §6）。

---

## 6. 为什么 max 更好（机制），以及哪里"更好"没有用

**更好的机制（三支路同时受益）：**

1. **Qwen3-VL 支路**：match@480p 只给编码器 0.40 MP（832×480，390 token）；max 给到 7.5 MP（3648×2048，7296 token）。人脸特征、logo / 招牌文字、服饰纹样、材质纹理这类细节，**在 match 下于文本编码器阶段就被抹掉了**——生成端再强也拿不回来。
2. **VAE / DiT 支路**：参考 latent 网格从 52×30（480p match）变为 228×128，参考 token 从 390 变为 7296（≈ 19 倍采样密度）。参考 latent `img_update=False`（`model.py` L362-457），**从不加噪、每步都作为条件参与 full attention**。
3. **口径一致性**：节点 tooltip 明说 max 用的是 "the reference pipeline's 2048px short edge"，即训练/官方参考管线就是 2048 短边——max 是"回到官方口径"，match 是本项目为低分辨率生成做的面积对齐近似。

**不会更好的地方：** 构图、镜头运动、场景布局的一致性（§5.3）；以及超过短边 2048 的像素（§5.1）。

**代价与风险：** 显存与时间（§7）；另外「参考绑定更强后，提示词对姿态 / 构图的自由度是否被压低」属于**机制推断，尚无实测证据**（见 §10）。

---

## 7. 成本：480p 上很贵，768p 上便宜

参考图 latent 每步参与 full attention ⇒ 采样阶段成本随序列长度呈 O(S²)。以 5 s（124 帧 → video latent_t = 37）为例，把文本与音频 token 粗估为 ~800：

| 生成档 | 视频 token | match 参考（4K 图） | max 参考（4K 图） | 序列增幅 | 注意力 FLOPs |
|---|---|---|---|---|---|
| 832×480 | 14430 | 390 | 7296 | +44 % | **≈ 2.1×** |
| 1344×768 | 37296 | 1008 | 7296 | +16 % | ≈ 1.35× |

- **采样阶段的增量只是其中一半**：Qwen3-VL-32B 要一次性 prefill 从 390 涨到 7296 个 vision token（vision encoder 过 29184 个 patch）。本机 8 GB 卡跑 27 GB 的 int8 编码器，大量层在 CPU / 内存侧，**"max 慢好几倍"主要慢在这段 prefill，而不是采样步数**。
- **多图要按预算分配**：9 张 4K + max 在 480p 下参考 token = 65664，整条序列 ≈ 80900（≈ **26× 注意力**），8 GB 卡基本必 OOM；同一场景改 match 只多 3510 token（几乎无感）。经验上：**参考 token 总量别超过视频 token 的一半**（用 §3 的 `4096 × 宽高比` 估单张）。

---

## 8. 建议

| 场景 | 建议 |
|---|---|
| 480p 生成 | 默认 `match`（代价可忽略）；**人脸 / 文字 / logo 是主体时，只把关键 1-2 张切到 `max`**，其余留 match |
| 768p 生成 | `max` 的序列代价仅 +16 %（注意力 1.35×），收益最大、性价比最高，可以全用 max |
| 素材准备 | 不需要 4K / 8K；准备**短边正好 2048** 的图（16:9 → 3648×2048），既吃满上限又不浪费；1440p / FHD 也会原样进入 |
| 多图（0032 / 0044 等） | 先按 `4096 × 宽高比` 估 token，超预算就把次要图降到 match，或先缩到 2048 短边 |
| 极端画幅 | 宽高比 > 3.06:1 时注意 Qwen 侧 `max_pixels` 会二次缩放（§3），避免 Qwen 与 VAE 看到不一致的尺寸 |
| 与已有结论衔接 | 「参考图要清晰、要正交、要少而精」（08-17）、「身份保真的强杠杆是 AddGuide 关键帧锚定」（09-18）与本节不冲突：max 是在**参考图支路**上把已有素材吃满，不改提示词结构 |

---

## 9. 复算方法（可自行复跑）

下面这段与源码公式一一对应，纯标准库，可直接丢给 `.venv\Scripts\python.exe`：

```python
import math

CANVAS_MULTIPLE, REF_SHORT, QWEN_MAX = 32, 2048, 12845056

def node_size(w, h, mode, gen_w, gen_h):
    scale = (min(1.0, math.sqrt((gen_w * gen_h) / (w * h))) if mode == "match"
             else min(1.0, REF_SHORT / min(w, h)))
    align = lambda x: max(CANVAS_MULTIPLE, round(x * scale / CANVAS_MULTIPLE) * CANVAS_MULTIPLE)
    return align(w), align(h)

def qwen_size(w, h):                      # qwen_vl.process_qwen2vl_images 的二次缩放
    f, hb, wb = 32, round(h / 32) * 32, round(w / 32) * 32
    if hb * wb > QWEN_MAX:
        beta = math.sqrt((h * w) / QWEN_MAX)
        hb, wb = max(f, math.floor(h / beta / f) * f), max(f, math.floor(w / beta / f) * f)
    return wb, hb

tok = lambda w, h: (w // 32) * (h // 32)   # Qwen vision token ≈ DiT 参考 rows

for w, h in [(1920, 1080), (2560, 1440), (3840, 2160), (7680, 4320), (5120, 2160)]:
    mw, mh = node_size(w, h, "max", 0, 0)
    rw, rh = node_size(w, h, "match", 832, 480)
    print(f"{w}x{h}  max->{mw}x{mh} tok={tok(mw, mh)}  match480->{rw}x{rh} tok={tok(rw, rh)}")
```

---

## 10. 边界与未验证

- **未实测**：本文数字全部来自源码公式复算，**没有跑过生成对比**。待验证的是两件事——(a) 480p 下 1 张关键图 match → max 的身份 / 文字保真提升幅度（建议用 ArcFace 余弦 + SIFT + 目视，口径沿用 09-18 文档）；(b) max 是否真的压低提示词对姿态 / 构图的自由度（§6 的推断）。
- **A/B 方案**：固定 prompt / seed / 时长（480p 5 s），只改 `ref_image_size`，各跑一次，抽帧做联络表对比人脸与文字细节，同时记录耗时与峰值显存；改动前先备份工作流 JSON 到 `backups\`。
- **未覆盖**：参考音频只做 32 kHz 重采样，与分辨率无关；参考视频的 768 短边规则本文只记录口径、未做尺寸-保真度实验。
