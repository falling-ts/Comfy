#!/usr/bin/env bash
# ComfyUI Linux 后台启动脚本(与 comfy-server.cmd 对标)
#   - 面向本机 AutoDL 容器 RTX 4080 32GB: llama.cpp 服务占用约 27GB 显存,
#     故 --reserve-vram 26 把这部分留给其它服务; 系统内存 503GB 充足,
#     大模型动态卸载走内存, 不需要 --fast-disk
#   - Python 环境: conda 环境 comfy (/root/miniconda3/envs/comfy, Python 3.13), 不使用 .venv
#   - 三步: 停旧服务 → 后台启动 → 等待就绪
#   - 用法: ./comfy-server.sh
#   - 可覆盖: PORT / RESERVE_VRAM / PY_BIN / LOG
set -euo pipefail

cd "$(dirname "$0")"                      # 项目根目录(本脚本所在处)

PORT="${PORT:-8188}"
RESERVE_VRAM="${RESERVE_VRAM:-26}"        # 保留给其它服务的显存(GB),按需调整
PY_BIN="${PY_BIN:-/root/miniconda3/envs/comfy/bin/python}" # conda 环境 comfy 解释器
COMFY_DIR="$PWD/ComfyUI"
LOG="${LOG:-/tmp/comfy-server-${PORT}.log}"

# 停掉占用指定端口的旧服务(fuser 优先,退回 /proc 解析,容器里可能两者都缺)
kill_port() {
  if command -v fuser >/dev/null 2>&1; then
    fuser -k "$1/tcp" >/dev/null 2>&1 || true
    return
  fi
  local port_hex inodes pid
  port_hex=$(printf '%04X' "$1")
  inodes=$(awk -v p="$port_hex " '$2 ~ ":" p "\\$" && $4 == "0A" {print $10}' /proc/net/tcp /proc/net/tcp6 2>/dev/null | sort -u)
  for inode in $inodes; do
    for fd in /proc/[0-9]*/fd/*; do
      [ "$(readlink "$fd" 2>/dev/null)" = "socket:[$inode]" ] || continue
      pid=$(echo "$fd" | cut -d/ -f3)
      kill "$pid" 2>/dev/null || true
    done
  done
  # 等端口释放; 10 秒后仍在则强杀(有些进程会挂起不响应 TERM)
  local i
  for i in $(seq 1 10); do
    inodes=$(awk -v p="$port_hex " '$2 ~ ":" p "\\$" && $4 == "0A" {print $10}' /proc/net/tcp /proc/net/tcp6 2>/dev/null | sort -u)
    [ -z "$inodes" ] && return 0
    sleep 1
  done
  for inode in $inodes; do
    for fd in /proc/[0-9]*/fd/*; do
      [ "$(readlink "$fd" 2>/dev/null)" = "socket:[$inode]" ] || continue
      pid=$(echo "$fd" | cut -d/ -f3)
      kill -9 "$pid" 2>/dev/null || true
    done
  done
  sleep 1
}

[ -x "$PY_BIN" ] || { echo "未找到解释器: $PY_BIN (先建好 conda 环境 comfy, 或用 PY_BIN 指定)" >&2; exit 1; }
[ -d "$COMFY_DIR" ] || { echo "未找到 ComfyUI 目录: $COMFY_DIR" >&2; exit 1; }

echo "[1/3] 停掉 $PORT 上的旧服务..."
kill_port "$PORT"

echo "[2/3] 后台启动 ComfyUI (PID 见下方, log: $LOG)"
cd "$COMFY_DIR"
PYTHONNOUSERSITE=1 setsid nohup "$PY_BIN" main.py \
  --enable-manager \
  --reserve-vram "$RESERVE_VRAM" \
  >"$LOG" 2>&1 &
echo "  已启动, PID=$!  log: $LOG"

echo "[3/3] 等待 $PORT 就绪..."
for _ in $(seq 1 60); do
  if curl -sf "http://127.0.0.1:$PORT/system_stats" >/dev/null 2>&1; then
    echo "ComfyUI 就绪: http://127.0.0.1:$PORT/"
    exit 0
  fi
  sleep 1
done

echo "错误: $PORT 60 秒内未就绪, 最近日志:" >&2
tail -n 40 "$LOG" 2>/dev/null || true
exit 1
