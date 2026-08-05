$p = Start-Process -FilePath 'C:\Users\zghyu\miniconda3\envs\ComfyUI\python.exe' `
    -ArgumentList 'main.py','--enable-manager','--disable-pinned-memory','--use-sage-attention','--fast-disk' `
    -WorkingDirectory 'D:\Comfy\ComfyUI' `
    -WindowStyle Hidden -PassThru
Start-Sleep -Seconds 3
if ($p.HasExited) { Write-Output "FAILED exit=$($p.ExitCode)"; exit 1 }
Write-Output "OK detached PID=$($p.Id)"
