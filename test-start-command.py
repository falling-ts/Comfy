#!/usr/bin/env python
# scripts/test-start-command.py
"""「运行前命令」测试脚本: 在系统右下角弹一条 Windows 通知。

用法 —— 把下面这行填进 ComfyUI 的 系统设置 → 其它 → 开始前命令:

    .venv\\Scripts\\python.exe scripts\\test-start-command.py

之后每次点「运行」/按 Ctrl+Enter, 提交之前都会先跑本脚本: 右下角弹出
「Comfy 开始前命令」通知 = 前置命令确实执行了, 而且退出码为 0, 本次运行没有被拦下。
(命令行直接跑同一条命令也可以, 用来先确认本机能不能弹通知。)

设计约束(为什么写成这样):

- **必须立刻退出**: 后端会一直等到命令跑完才提交本次运行(`pre-run/nodes.py` 的
  `_run_command`), 所以通知一律交给**后台 PowerShell 子进程**去弹, 本脚本最多等
  `_WAIT_S` 秒就走; 不能在这里 `sleep` 等通知消失;
- **永远退出 0**: 非 0 退出码会被后端当成"前置命令失败"并**取消本次运行** ——
  让"通知没弹出来"这种无关紧要的事把工作流拦掉是不可接受的, 故一切失败只打印不报错
  (要故意测失败路径时用 `--fail N`);
- **不引入第三方库**(不装 win10toast/BurntToast): 先用 PowerShell 的 WinRT 原生 Toast
  (右下角 + 进通知中心), 失败再退回 NotifyIcon 气泡提示;
- PowerShell 脚本经 `-EncodedCommand`(UTF-16LE + base64)传入, 免去临时 .ps1 文件的
  编码问题 —— Windows PowerShell 5.1 会把无 BOM 的 UTF-8 脚本按 ANSI 读, 中文必乱码。

⚠️ 排查痕迹: 每次执行都往 `logs\\test-start-command.log` 追加一行(时间/通知结果/参数),
后端也会把本脚本的 stdout 记进 `ComfyUI\\user\\comfyui_<port>.log`; 两个都不需要了就删掉。
"""

from __future__ import annotations

import argparse
import base64
import datetime as dt
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile

# 通知标题: 与插件设置项同名, 一眼能对上
TITLE = "Comfy 开始前命令"

# 等后台 PowerShell 的秒数(WinRT Toast 是异步投递, 通常 1s 内就返回)
_WAIT_S = 8

_LOG = pathlib.Path(__file__).resolve().parent.parent / "logs" / "test-start-command.log"

# PowerShell 通知脚本(__TITLE__ / __MESSAGE__ 由 Python 以单引号字面量替换)。
# 保持纯 ASCII 源码, 中文只从参数进 —— 这样用户级/机器级执行策略、代码页都不会干扰。
_TOAST_PS = r"""
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'
$title = __TITLE__
$message = __MESSAGE__
# 未注册 AppID 的经典写法: 借用 Windows PowerShell 的 AUMID, 通知照常显示
$appId = '{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe'

function Show-Toast {
    [void][Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType=WindowsRuntime]
    [void][Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom, ContentType=WindowsRuntime]
    $xml = [Windows.UI.Notifications.ToastNotificationManager]::GetTemplateContent([Windows.UI.Notifications.ToastTemplateType]::ToastText02)
    $texts = $xml.GetElementsByTagName('text')
    [void]$texts.Item(0).AppendChild($xml.CreateTextNode($title))
    [void]$texts.Item(1).AppendChild($xml.CreateTextNode($message))
    $toast = New-Object Windows.UI.Notifications.ToastNotification $xml
    [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier($appId).Show($toast)
}

function Show-Balloon {
    Add-Type -AssemblyName System.Windows.Forms
    Add-Type -AssemblyName System.Drawing
    $icon = New-Object System.Windows.Forms.NotifyIcon
    $icon.Icon = [System.Drawing.SystemIcons]::Information
    $icon.Text = 'Comfy'
    $icon.Visible = $true
    $icon.ShowBalloonTip(10000, $title, $message, [System.Windows.Forms.ToolTipIcon]::Info)
    Start-Sleep -Seconds 10
    $icon.Visible = $false
    $icon.Dispose()
}

try {
    Show-Toast
    Write-Output 'OK toast'
} catch {
    Write-Output ('WARN toast: ' + $_.Exception.Message)
    try {
        Show-Balloon
        Write-Output 'OK balloon'
    } catch {
        Write-Output ('FAIL balloon: ' + $_.Exception.Message)
    }
}
"""


def _fix_console() -> None:
    """把 stdout/stderr 钉成 UTF-8: 宿主可能是 GBK 控制台, 打中文会 UnicodeEncodeError。"""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


def _powershell() -> str | None:
    """优先 Windows PowerShell 5.1(WinRT 投影最稳), 再退 PowerShell 7。"""
    for name in ("powershell.exe", "pwsh.exe", "powershell", "pwsh"):
        found = shutil.which(name)
        if found:
            return found
    return None


def _ps_quote(text: str) -> str:
    """PowerShell 单引号字面量(里面只有单引号需要翻倍)。"""
    return "'" + text.replace("'", "''") + "'"


def _read(path: pathlib.Path) -> str:
    try:
        return path.read_bytes().decode("utf-8", errors="replace")
    except OSError:
        return ""


def _status_line(text: str) -> str:
    """挑出 PowerShell 的状态行。

    ⚠️ 输出里可能混着 CLIXML 噪声(`#< CLIXML ...`): Windows PowerShell 把"模块首次使用"
    这类进度写 stderr, 而我们 `stderr=STDOUT` 合并了它 —— 直接拿整段文本判前缀会误判成失败。
    """
    for raw in text.splitlines():
        line = raw.strip()
        if line.startswith(("OK ", "WARN ", "FAIL ")):
            return line
    return text.strip()[:200] or "(无输出)"


def _notify(title: str, message: str) -> tuple[bool, str]:
    """弹系统通知, 返回 (是否已投递, 说明)。绝不抛异常、绝不长时间阻塞。"""
    if os.name != "nt":
        return False, "非 Windows 平台, 跳过系统通知"

    shell = _powershell()
    if not shell:
        return False, "找不到 powershell, 跳过系统通知"

    script = _TOAST_PS.replace("__TITLE__", _ps_quote(title)).replace(
        "__MESSAGE__", _ps_quote(message)
    )
    encoded = base64.b64encode(script.encode("utf-16-le")).decode("ascii")
    # ⚠️ 不能用 DETACHED_PROCESS: 没有控制台的 powershell.exe 5.1 会把输出整个丢掉
    # (实测 rc=0 但文件 0 字节), CREATE_NO_WINDOW 给一个隐藏控制台则一切正常。
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0) | getattr(
        subprocess, "CREATE_NEW_PROCESS_GROUP", 0
    )

    fd, out_name = tempfile.mkstemp(prefix="prerun-toast-", suffix=".txt")
    os.close(fd)
    out = pathlib.Path(out_name)
    try:
        with out.open("w+b") as fh:
            proc = subprocess.Popen(
                [
                    shell,
                    "-NoProfile",
                    "-NonInteractive",
                    "-STA",
                    "-WindowStyle",
                    "Hidden",
                    "-EncodedCommand",
                    encoded,
                ],
                stdin=subprocess.DEVNULL,
                stdout=fh,
                stderr=subprocess.STDOUT,
                creationflags=flags,
                close_fds=True,
            )
        try:
            proc.wait(timeout=_WAIT_S)
        except subprocess.TimeoutExpired:
            # 多半是气泡分支在 sleep: 通知已经投递, 剩下的收尾交给子进程自己
            return True, f"已投递(等待 {_WAIT_S}s 未退出, 后台自行收尾)"
        status = _status_line(_read(out))
        return status.startswith("OK"), status
    finally:
        # 子进程可能还占着这个文件, 删不掉就算了(temp 目录本来就会被清)
        try:
            out.unlink()
        except OSError:
            pass


def _append_log(line: str) -> None:
    try:
        _LOG.parent.mkdir(parents=True, exist_ok=True)
        with _LOG.open("a", encoding="utf-8") as fh:
            fh.write(line + "\n")
    except OSError:
        pass


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="「运行前命令」测试脚本: 右下角弹系统通知, 用来确认前置命令被执行了",
    )
    parser.add_argument("--title", default=TITLE, help=f"通知标题(默认 {TITLE})")
    parser.add_argument("--note", default="", help="附加到通知正文末尾的备注, 便于区分多次运行")
    parser.add_argument("--no-notify", action="store_true", help="只打印/记日志, 不弹通知")
    parser.add_argument(
        "--fail",
        type=int,
        default=0,
        metavar="N",
        help="故意返回非 0 退出码, 用来测「前置命令失败 → 取消本次运行」这条路径",
    )
    return parser.parse_args()


def main() -> int:
    _fix_console()
    args = _parse_args()

    now = dt.datetime.now()
    note = f" · {args.note}" if args.note else ""
    message = f"✔ 开始前命令已执行 · {now:%H:%M:%S} · PID {os.getpid()}{note}"

    if args.no_notify:
        ok, detail = False, "按 --no-notify 跳过"
    else:
        try:
            ok, detail = _notify(args.title, message)
        except Exception as exc:  # 任何意外都不许把本次运行拦掉
            ok, detail = False, f"通知异常: {exc!r}"

    line = (
        f"{now:%Y-%m-%d %H:%M:%S} 通知={'OK' if ok else 'NO'} {detail}"
        f" | 内容={args.title} / {message}"
        f" | pid={os.getpid()} argv={' '.join(sys.argv[1:]) or '(无)'}"
    )
    print(f"[test-start-command] {line}", flush=True)
    _append_log(line)

    if args.fail:
        print(f"[test-start-command] 按 --fail={args.fail} 返回非 0(后端会拦下本次运行, 属预期)", flush=True)
    return args.fail


if __name__ == "__main__":
    sys.exit(main())
