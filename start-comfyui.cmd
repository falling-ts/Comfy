@echo off
rem ============================================
rem  Start ComfyUI (conda env: ComfyUI, with Manager)
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

"C:\Users\zghyu\miniconda3\envs\ComfyUI\python.exe" main.py --enable-manager
pause
