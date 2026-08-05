# Start ComfyUI (conda env: ComfyUI, with Manager)
# 优化参数(2026-08-05, 8GB 显存 MiniMax H3):
#   --disable-pinned-memory  修复 0.30.x pinned-memory 回归, 加快模型加载
#   --use-sage-attention     Sage Attention 加速(约 2x), 已装 triton+sageattention
#   --fast-disk              低内存时把模型交换到 NVME 磁盘, 避免 RAM 撑爆
# Usage: powershell -ExecutionPolicy Bypass -File D:\Comfy\start-comfyui.ps1
Set-Location 'D:\Comfy\ComfyUI'

# If ComfyUI is already running on port 8188, warn and exit
if (Get-NetTCPConnection -LocalPort 8188 -State Listen -ErrorAction SilentlyContinue) {
    Write-Warning 'ComfyUI is already running at http://127.0.0.1:8188. Open the browser, or stop the existing instance first.'
    exit 1
}

& 'C:\Users\zghyu\miniconda3\envs\ComfyUI\python.exe' main.py --enable-manager --disable-pinned-memory --use-sage-attention --fast-disk
