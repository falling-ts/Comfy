# Start ComfyUI (conda env: ComfyUI, with Manager)
# Usage: powershell -ExecutionPolicy Bypass -File D:\Comfy\start-comfyui.ps1
Set-Location 'D:\Comfy\ComfyUI'

# If ComfyUI is already running on port 8188, warn and exit
if (Get-NetTCPConnection -LocalPort 8188 -State Listen -ErrorAction SilentlyContinue) {
    Write-Warning 'ComfyUI is already running at http://127.0.0.1:8188. Open the browser, or stop the existing instance first.'
    exit 1
}

& 'C:\Users\zghyu\miniconda3\envs\ComfyUI\python.exe' main.py --enable-manager
