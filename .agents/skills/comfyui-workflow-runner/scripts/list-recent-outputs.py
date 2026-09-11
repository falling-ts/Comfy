"""列出 ComfyUI 最近任务的输出文件路径, 定位用户刚生成的视频。"""

import json
import urllib.request

API = "http://127.0.0.1:8188"


def main() -> int:
    h = json.load(urllib.request.urlopen(f"{API}/history?max_items=15", timeout=60))
    rows = []
    for pid, e in h.items():
        st = e.get("status", {})
        msgs = st.get("messages", [])
        start = next((m[1].get("timestamp") for m in msgs if m[0] == "execution_start"), None)
        end = next((m[1].get("timestamp") for m in msgs if m[0] in ("execution_success", "execution_error")), None)
        dur = f"{(end - start) / 1000:.1f}s" if start and end else "-"
        outs = []
        for nid, o in (e.get("outputs") or {}).items():
            for kind in ("images", "videos", "gifs", "audio"):
                for item in o.get(kind) or []:
                    if isinstance(item, dict) and item.get("filename"):
                        outs.append(f"{item.get('subfolder', '')}/{item['filename']}")
                    elif isinstance(item, str):
                        outs.append(item)
        rows.append((start or 0, pid, st.get("status_str"), dur, outs))

    rows.sort(reverse=True)
    for start_ms, pid, status, dur, outs in rows:
        import datetime
        ts = datetime.datetime.fromtimestamp(start_ms / 1000).strftime("%m-%d %H:%M:%S") if start_ms else "?"
        print(f"[{ts}] {status:8} {dur:>8}  {pid[:8]}")
        for o in outs[:6]:
            print(f"      -> {o}")
        if not outs:
            print("      (无文件输出)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
