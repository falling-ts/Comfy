@echo off
setlocal

set "PORT=8188"
set "ROOT=%~dp0"
set "COMFY_DIR=%ROOT%ComfyUI"
set "LOG=%TEMP%\comfy-server-%PORT%.log"
set "PYTHON=%ROOT%.venv\Scripts\python.exe"

echo [1/3] Stopping existing service on port %PORT%...
for /f "tokens=5" %%P in ('netstat -ano ^| findstr /c:":%PORT%" ^| findstr /c:"LISTENING"') do (
    taskkill /F /T /PID %%P >nul 2>&1
)

echo [2/3] Starting ComfyUI in the background...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$psi = New-Object System.Diagnostics.ProcessStartInfo; $psi.FileName = 'cmd.exe'; $psi.Arguments = '/d /c cd /d %COMFY_DIR% && set PYTHONNOUSERSITE=1 && \"%PYTHON%\" main.py --enable-manager --disable-pinned-memory --fast-disk > %LOG% 2>&1'; $psi.WorkingDirectory = '%COMFY_DIR%'; $psi.UseShellExecute = $false; $psi.CreateNoWindow = $true; [System.Diagnostics.Process]::Start($psi) | Out-Null"
if errorlevel 1 (
    echo Failed to start the background process.
    pause
    exit /b 1
)

echo [3/3] Waiting for port %PORT%...
set /a TRIES=0
:wait
ping -n 4 127.0.0.1 >nul
set /a TRIES+=1
netstat -ano | findstr /c:":%PORT%" | findstr /c:"LISTENING" >nul
if not errorlevel 1 goto ready
if %TRIES% geq 40 (
    echo ERROR: port %PORT% did not open within 120 seconds.
    echo Last log lines:
    powershell -NoProfile -ExecutionPolicy Bypass -Command "if (Test-Path '%LOG%') { Get-Content '%LOG%' -Tail 40 }"
    pause
    exit /b 1
)
goto wait

:ready
echo ComfyUI is listening on http://127.0.0.1:%PORT%/
exit /b 0
