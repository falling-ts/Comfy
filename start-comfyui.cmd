@echo off
rem ============================================
rem  Start ComfyUI (conda env: ComfyUI, with Manager)
rem  Optimized for 8GB VRAM MiniMax H3.
rem  Args:
rem    --disable-pinned-memory  fix 0.30.x pinned-memory loading regression
rem    --fast-disk              disk-backed offload for low RAM (NVME)
rem
rem  H3 acceleration notes (2026-08-06):
rem    * Core speedup = torch cu130 -> comfy-kitchen CUDA backend is enabled
rem      (see startup log: comfy_kitchen backend cuda: disabled=False)
rem    * SageAttention 2.2.0 installed; enable via workflow NODES, not CLI:
rem        - KJNodes "Patch Sage Attention KJ" (sage_attention=auto)
rem        - or chain: H3 Loader -> SageAttention -> NB H3 HyperStep -> Sampler
rem    * Do NOT add --use-sage-attention: global attention replacement caused
rem      black images on this GPU; CUDA illegal memory access cannot be caught.
rem    * Optional VRAM flags (uncomment if needed):
rem        --reserve-vram 0.5    reserve VRAM for desktop/browser
rem        --vram-headroom 0.3   extra DynamicVRAM headroom
rem    * --enable-triton-backend is for ROCm/AMD only; NVIDIA uses CUDA backend.
rem  * Current flags are optimal for 8GB VRAM / 16GB RAM + 20-39GB models
rem    (models >16GB cannot stay in RAM; --fast-disk loads from disk on demand)
rem  * Do NOT add: --highvram / --gpu-only / --high-ram (OOM), --fp16-vae (black),
rem    --use-pytorch-cross-attention (torch 2.13 SDPA bug), --fast (crash).
rem  * See docs\ folder for full launch-args reference and tuning notes.
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
