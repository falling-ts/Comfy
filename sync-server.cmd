@echo off
setlocal

set "PORT=8384"
set "ROOT=%~dp0"
if not defined SYNCTHING set "SYNCTHING=C:\Program Files\Syncthing\syncthing.exe"
set "LOG=%TEMP%\syncthing-server-%PORT%.log"

echo [1/3] Stopping existing Syncthing instances...
taskkill /F /IM syncthing.exe >nul 2>&1
ping -n 2 127.0.0.1 >nul

if not exist "%SYNCTHING%" (
    echo ERROR: Syncthing not found at %SYNCTHING%
    pause
    exit /b 1
)

echo [2/3] Starting Syncthing in the background...
powershell -NoProfile -ExecutionPolicy Bypass -Command "$psi = New-Object System.Diagnostics.ProcessStartInfo; $psi.FileName = 'cmd.exe'; $psi.Arguments = '/d /c \"%SYNCTHING%\" serve > %LOG% 2>&1'; $psi.UseShellExecute = $false; $psi.CreateNoWindow = $true; [System.Diagnostics.Process]::Start($psi) | Out-Null"
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
echo Syncthing is listening on http://127.0.0.1:%PORT%/
exit /b 0
