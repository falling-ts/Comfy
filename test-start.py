#!/usr/bin/env python
# test-start.py (工作区根)
"""「运行前命令」测试脚本: 打开系统记事本, 里面写着「Comfy 开始了」。

用法 —— 把这行填进 ComfyUI 的 系统设置 → 其它 →「运行前命令」:

    .venv\\Scripts\\python.exe test-start.py

之后每次点「运行」/按 Ctrl+Enter, 提交之前都会先跑本脚本: 桌面上弹出一个记事本窗口,
里面写着「Comfy 开始了」= 运行前命令确实执行了。
(命令行直接跑同一条命令也可以, 用来先确认本机能不能打开记事本。)

设计约束(为什么写成这样):

- **文本先落盘, 再用记事本打开**: "开一个空记事本再逐字打进去"(SendKeys)会受输入法/焦点/
  窗口就绪时机影响 —— 打字打到别处、或窗口还没起来就发键; 打开一个内容已写好的文件才是
  确定性的。内容写在 `logs\\test-start.txt`, 编码 UTF-8 **带 BOM**: 记事本据此认编码, 中文
  不会显示成乱码(无 BOM 的 UTF-8 在老版记事本上会被按 ANSI/GBK 解读);
- **必须立刻退出**: 后端要等命令跑完才提交本次运行(`pre-run/nodes.py` 的 `_run_command`),
  所以记事本用 `Popen` **丢到后台**启动, 绝不 `wait()` —— 否则点了「运行」会一直卡到关掉记事本;
- **子进程三根标准流都接 `DEVNULL`**: 后端是**用管道读命令输出**的, 记事本若继承了管道的写端,
  本脚本即使已经退出, 后端仍要一直等到管道 EOF(= 关掉记事本)才往下走 —— 表现为「运行」永远
  转圈(这个坑与之前的通知脚本同源, 那里靠 `CREATE_NO_WINDOW` + 重定向输出绕开);
- **永远退出 0**: 非 0 退出码会被后端当成"前置命令失败"并**取消本次运行** —— 让"记事本没弹
  出来"这种无关紧要的事把工作流拦掉是不可接受的, 故一切失败只打印、不报错。
"""

from __future__ import annotations

import pathlib
import subprocess
import sys

# 写进记事本的那句话
TEXT = "Comfy 开始了"

# 落盘位置: 工作区根的 logs\(已 gitignore), 路径由本文件位置反推, 故在哪个目录调用都对
NOTE = pathlib.Path(__file__).resolve().parent / "logs" / "test-start.txt"


def _fix_console() -> None:
    """把 stdout/stderr 钉成 UTF-8: 宿主可能是 GBK 控制台, 打中文会 UnicodeEncodeError。"""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


def _write_note() -> None:
    NOTE.parent.mkdir(parents=True, exist_ok=True)
    # utf-8-sig = 带 BOM 的 UTF-8, 记事本靠它认编码
    NOTE.write_text(TEXT + "\n", encoding="utf-8-sig")


def _open_notepad() -> None:
    """后台拉起记事本打开 NOTE; 不等待、不接管它的输出。"""
    flags = getattr(subprocess, "DETACHED_PROCESS", 0) | getattr(
        subprocess, "CREATE_NEW_PROCESS_GROUP", 0
    )
    subprocess.Popen(
        ["notepad.exe", str(NOTE)],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        creationflags=flags,
        close_fds=True,
    )


def main() -> int:
    _fix_console()

    if sys.platform != "win32":
        print(f"[test-start] 非 Windows 平台, 跳过记事本(本该显示: {TEXT})", flush=True)
        return 0

    try:
        _write_note()
        _open_notepad()
    except OSError as exc:  # 记事本没弹出来也不许把本次运行拦掉
        print(f"[test-start] 打开记事本失败(不拦本次运行): {exc}", flush=True)
        return 0

    print(f"[test-start] 记事本已打开, 内容「{TEXT}」: {NOTE}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
