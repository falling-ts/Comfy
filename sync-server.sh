#!/usr/bin/env bash
# sync-server.sh — Syncthing 统一后台启动脚本(跨平台: Linux + Windows Git Bash)
#
# 取代原 sync-server.cmd(Windows), 参照 comfy-server.sh 风格, 三步:
# 停旧服务 → 后台启动 → 等待端口就绪。
#
# 用法:
#   bash sync-server.sh                   # 默认端口 8384 (Syncthing API 端口)
#   PORT=8385 bash sync-server.sh         # 自定义端口
#   WAIT=300 bash sync-server.sh          # 加长启动等待
#   SYNCTHING=... bash sync-server.sh     # 自定义 syncthing 可执行文件
#   LOG=... bash sync-server.sh           # 自定义日志路径
#
# 平台自适应:
#   - Windows (Git Bash): 默认 "C:\Program Files\Syncthing\syncthing.exe"
#   - Linux: 默认 /usr/bin/syncthing, 缺失时回退 PATH 中的 syncthing,
#     有 setsid 时 detach 会话(SSH 断开后存活)
#   - 日志默认写**调用时所在目录** sync-server-<port>.log(两平台一致, 同 comfy-server.sh)
#
# 说明: 就绪检测用 bash 内建 /dev/tcp 探测端口(两平台均可用);
# Syncthing 同时监听 GUI 22000 与 API $PORT(默认 8384), 探测 API 端口即可。
set -u

ROOT="$(cd "$(dirname "$0")" && pwd)"
PORT="${PORT:-8384}"
WAIT_SECS="${WAIT:-120}"
LOG="${LOG:-$(pwd)/sync-server-${PORT}.log}"   # 日志写调用时所在目录

IS_WINDOWS=0
case "$(uname -s 2>/dev/null)" in
  MINGW*|MSYS*|CYGWIN*) IS_WINDOWS=1 ;;
esac

if [ "$IS_WINDOWS" -eq 1 ]; then
  SYNCTHING="${SYNCTHING:-/c/Program Files/Syncthing/syncthing.exe}"
else
  SYNCTHING="${SYNCTHING:-/usr/bin/syncthing}"
  [ -x "$SYNCTHING" ] || SYNCTHING="$(command -v syncthing || true)"
fi

# [1/3] 停掉占用端口的旧服务
kill_port() {
  if [ "$IS_WINDOWS" -eq 1 ]; then
    # syncthing 同进程占多个端口(22000 GUI / $PORT API 等), 按进程名杀覆盖全部
    MSYS_NO_PATHCONV=1 taskkill /F /IM syncthing.exe >/dev/null 2>&1 || true
    sleep 1
    # 若仍在占用, 按端口 PID 再杀(同 comfy-server.sh)
    local PIDS PID
    PIDS="$(netstat -ano 2>/dev/null | tr -d '\r' | grep -E "[:.]${PORT}[[:space:]]" | grep -iE 'LISTEN' | awk '{print $NF}' | sed 's/\/.*//' | sort -u)"
    if [ -n "$PIDS" ]; then
      for PID in $PIDS; do
        MSYS_NO_PATHCONV=1 taskkill /F /T /PID "$PID" >/dev/null 2>&1 || true
      done
      sleep 1
    else
      echo "      (none found)"
    fi
    return
  fi
  # Linux: fuser 优先; 容器里可能没有, 退回 /proc/net/tcp{,6} 解析 inode → pid
  if command -v fuser >/dev/null 2>&1; then
    fuser -k "$PORT/tcp" >/dev/null 2>&1 || true
    sleep 1
    return
  fi
  local port_hex inodes fd pid i
  port_hex=$(printf '%04X' "$PORT")
  inodes="$(awk -v p=":$port_hex" 'substr($2, length($2)-length(p)+1) == p && $4 == "0A" {print $10}' /proc/net/tcp /proc/net/tcp6 2>/dev/null | sort -u)"
  for inode in $inodes; do
    for fd in /proc/[0-9]*/fd/*; do
      [ "$(readlink "$fd" 2>/dev/null)" = "socket:[$inode]" ] || continue
      pid="${fd#/proc/}"; pid="${pid%%/*}"
      kill "$pid" 2>/dev/null || true
    done
  done
  # 等端口释放; 10 秒后仍在则强杀(有些进程挂起不响应 TERM)
  for i in $(seq 1 10); do
    inodes="$(awk -v p=":$port_hex" 'substr($2, length($2)-length(p)+1) == p && $4 == "0A" {print $10}' /proc/net/tcp /proc/net/tcp6 2>/dev/null | sort -u)"
    [ -z "$inodes" ] && return 0
    sleep 1
  done
  for inode in $inodes; do
    for fd in /proc/[0-9]*/fd/*; do
      [ "$(readlink "$fd" 2>/dev/null)" = "socket:[$inode]" ] || continue
      pid="${fd#/proc/}"; pid="${pid%%/*}"
      kill -9 "$pid" 2>/dev/null || true
    done
  done
  sleep 1
}

[ -n "$SYNCTHING" ] && [ -x "$SYNCTHING" ] || { echo "ERROR: 未找到 syncthing 可执行文件 (安装 Syncthing 或用 SYNCTHING 指定)" >&2; exit 1; }

echo "[1/3] 停掉 $PORT 上的旧 Syncthing 服务..."
kill_port

echo "[2/3] 后台启动 Syncthing (log: $LOG)..."
# Linux 用 setsid 完全脱离终端(SSH 断开后存活); Git Bash 无 setsid, nohup 已够
LAUNCH=(nohup)
if [ "$IS_WINDOWS" -eq 0 ] && command -v setsid >/dev/null 2>&1; then
  LAUNCH=(setsid nohup)
fi
"${LAUNCH[@]}" "$SYNCTHING" serve >"$LOG" 2>&1 &
SRV_PID=$!
echo "      (server PID $SRV_PID, log: $LOG)"

echo "[3/3] 等待端口 $PORT (最长 ${WAIT_SECS}s)..."
i=0
while [ "$i" -lt "$WAIT_SECS" ]; do
  if (exec 3<>"/dev/tcp/127.0.0.1/$PORT") 2>/dev/null; then
    echo "OK: Syncthing 就绪 -> http://127.0.0.1:$PORT/ (API; GUI 见 22000)"
    exit 0
  fi
  i=$((i + 1))
  sleep 1
done
echo "ERROR: 端口 $PORT 在 ${WAIT_SECS}s 内未就绪, 最近日志:"
tail -n 40 "$LOG" 2>/dev/null
exit 1
