@echo off
rem ============================================
rem  Start ComfyUI (conda env: ComfyUI, with Manager)
rem  优化参数(2026-08-05, 8GB 显存 MiniMax H3):
rem    --disable-pinned-memory  修复 0.30.x pinned-memory 回归, 加快模型加载
rem    --use-sage-attention     Sage Attention 加速(约 2x), 已装 triton+sageattention
rem    --fast-disk              低内存时把模型交换到 NVME 磁盘, 避免 RAM 撑爆
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

"C:\Users\zghyu\miniconda3\envs\ComfyUI\python.exe" main.py --enable-manager --disable-pinned-memory --use-sage-attention --fast-disk
pause
