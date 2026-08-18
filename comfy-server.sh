#!/usr/bin/env bash
# ComfyUI Linux 后台启动脚本(与 comfy-server.cmd 对标)
#   - 面向 RTX 5090 服务器: 26G 显存留给其它服务(--reserve-vram 26), 不用硬盘加速(不传 --fast-disk)
#   - 三步: 停旧服务 → 后台启动 → 等待就绪
#   - 用法: ./comfy-server.sh
#   - 可覆盖: PORT / RESERVE_VRAM / PY_BIN / LOG
set -euo pipefail

cd "$(dirname "$0")"                      # 项目根目录(本脚本所在处)

PORT="${PORT:-8188}"
RESERVE_VRAM="${RESERVE_VRAM:-26}"        # 保留给其它服务的显存(GB),按需调整
PY_BIN="${PY_BIN:-$PWD/.venv/bin/python}" # 虚拟环境解释器
COMFY_DIR="$PWD/ComfyUI"
LOG="${LOG:-/tmp/comfy-server-${PORT}.log}"

# 停掉占用指定端口的旧服务(fuser 优先,退回 ss 解析)
kill_port() {
  if command -v fuser >/dev/null 2>&1; then
    fuser -k "$1/tcp" >/dev/null 2>&1 || true
  else
    ss -tlnp 2>/dev/null | awk -v p=":$1 " 'index($0,p){if(m=match($0,/pid=[0-9]+/)) print substr($0,RSTART+4,RLENGTH-4)}' \
      | sort -u | xargs -r kill 2>/dev/null || true
  fi
}

[ -x "$PY_BIN" ] || { echo "未找到解释器: $PY_BIN (服务器上先建好 .venv, 或用 PY_BIN 指定)" >&2; exit 1; }
[ -d "$COMFY_DIR" ] || { echo "未找到 ComfyUI 目录: $COMFY_DIR" >&2; exit 1; }

echo "[1/3] 停掉 $PORT 上的旧服务..."
kill_port "$PORT"

echo "[2/3] 后台启动 ComfyUI (PID 见下方, log: $LOG)"
cd "$COMFY_DIR"
PYTHONNOUSERSITE=1 nohup "$PY_BIN" main.py \
  --enable-manager \
  --reserve-vram "$RESERVE_VRAM" \
  --disable-pinned-memory \
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
