@echo off
rem ============================================
rem  Start ComfyUI (conda env: ComfyUI, with Manager)
rem  Optimized for 8GB VRAM MiniMax H3:
rem    --disable-pinned-memory  fix 0.30.x pinned-memory loading regression
rem    --fast-disk              disk-backed offload for low RAM (NVME)
rem
rem  H3 加速姿势 (2026-08-06 源码核查):
rem    * 提速核心 = torch cu130: comfy-kitchen CUDA 后端已激活
rem      (启动日志 Found comfy_kitchen backend cuda: disabled=False,
rem       量化权重 INT8/NVFP4 硬件直算, H3 提速 6-8x 的关键)
rem    * SageAttention 2.2.0 已装, 通过【工作流节点】定向启用, 不靠命令行:
rem        - KJNodes: "Patch Sage Attention KJ" 节点, sage_attention=auto
rem        - 或推荐链: H3 Loader -> SageAttention -> NB H3 HyperStep -> Sampler
rem    * 不要加 --use-sage-attention: 它全局替换所有模型 attention(含文生图 T2I),
rem      曾在本机导致黑图; 且 CUDA illegal memory access 无法被 try/except 捕获,
rem      一旦崩溃会污染 CUDA 上下文必须重启.
rem    * 可选显存参数(按需取消注释启用):
rem        --reserve-vram 0.5    给桌面/浏览器预留 0.5GB 显存
rem        --vram-headroom 0.5   DynamicVRAM 额外余量(防止其他程序抢显存)
rem    * 可选 --enable-triton-backend: 仅 ROCm/AMD 路径需要, NVIDIA 用 CUDA 后端即可
rem
rem  ★ 当前参数已是 8GB显存/16GB内存 + 大模型(20-39GB)最佳组合:
rem     模型文件 >16GB 无法驻留 RAM, --fast-disk 让权重从磁盘按需加载(核心)
rem     详细分析见 docs\启动参数推荐-8GB-16GB设备-2026-08-06.md
rem  ★ 不要加:
rem     --highvram/--gpu-only/--high-ram   → 模型驻留 VRAM/RAM, 直接 OOM
rem     --use-pytorch-cross-attention      → torch 2.13 的 SDPA 已损坏(见 docs)
rem     --fp16-vae                         → 源码标注可能黑图
rem     --fast                             → 实验性, 可能崩溃
rem  Usage: double-click or run from cmd
rem ============================================
cd /d D:\Comfy\ComfyUI

rem If ComfyUI is already running on port 8188, exit with a hint
netstat -ano | findstr /R /C:":8188 .*LISTENING" >nul
if not errorlevel 1 (
    echo [WARN] ComfyUI is already running at http://127.0.0.1:8188
    echo        Open the browser, or stop the existing instance first.
    pause
    exit /b 1
)

rem Isolate from user site-packages (was polluted by CPU torch / MINGW numpy)
set PYTHONNOUSERSITE=1

"C:\Users\zghyu\miniconda3\envs\ComfyUI\python.exe" main.py --enable-manager --disable-pinned-memory --fast-disk
pause
