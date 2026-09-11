---
name: comfyui-workflow-runner
description: |
  Run local ComfyUI workflows headlessly through the HTTP API without touching the browser: convert a
  saved workflow JSON into the API prompt format, refresh a FallingTS Markdown data table from its md file
  (equivalent to clicking that node's refresh button), submit to /prompt, poll /history to completion, and
  verify the produced artifact by probing it and extracting frames. Use whenever a workflow must be
  executed or re-run autonomously, when a prompt or model edited inside an md data table has to actually
  take effect, or when a render needs objective inspection (duration, fps, audio presence, motion,
  continuity). Also carries measured findings on H3 scene video: which reference/prompt variants actually
  win, rotation speed ceilings, and the OrbitSheets parameter recipe. Not for authoring prompt text or for
  developing custom nodes.
---

# ComfyUI Workflow Runner

Drive the local ComfyUI at `http://127.0.0.1:8188` from scripts: **edit source data → refresh the
data-table node → submit → inspect the artifact**. No browser, no manual Run click, no frontend state
to sync by hand.

## When to use this

- A workflow must be run and its output checked, and the user is not going to click Run for you.
- A prompt living in a `stories/**/*.md` data table was just edited — the workflow JSON still holds the
  **old** text until something refreshes it.
- An A/B comparison or regression check needs real renders plus quantitative inspection.

## The core insight (why nothing needs clicking)

`FallingTSMarkDownTable.execute(data, id)` consumes only the **control state** `data`
(`{md_path, fields, selected}`) that the frontend serializes into the workflow. It never reads the md
file itself. The frontend's refresh button merely calls `GET /fallingts_mdtable/read?path=...` and writes
the returned rows back into that state. Calling the same endpoint and constructing `data` yourself is
therefore equivalent — and needs no browser at all.

## Procedure

1. **Convert and refresh**
   `python scripts/workflow-to-prompt.py "<glob>" --refresh-md --dump prompt.json`
   Confirm the node count, and that the mdtable prompt length changed to the new value (a stale length
   means the refresh did not happen and you would silently re-run the previous prompt).
2. **Dry-run check** — inspect a few critical nodes (loaders, sampler, sigma shift, the data table)
   before spending GPU time. `--dump` then read the JSON.
3. **Submit** — add `--submit`. The script posts to `/prompt`, polls `/history/<id>`, and prints the
   output filenames it produced.
4. **Verify the artifact** — never trust "success" alone; probe it and look at it:
   - `ffmpeg -i file.mp4` → duration, resolution, fps, **and whether an audio stream exists at all**
   - contact sheet: `ffmpeg -y -i f.mp4 -vf "fps=1/N,scale=640:-1,tile=4x2" -frames:v 1 grid.png`
   - read `grid.png` as an image, then judge content, continuity and consistency
   - motion consistency: `-vf "fps=2,scale=160:90,tblend=all_mode=difference,blackframe=amount=0:threshold=10"`
     and compare the `pblack` values; a **constant** value means constant speed, wild swings mean the
     shot stutters or stalls

## Pitfalls (each cost a real debugging round)

- **`widgets_values` includes widgets that were converted into inputs.** A connected widget still occupies
  its slot in the array, so zip against the **full** widget list and *then* skip the linked ones. Filtering
  first shifts everything — `PreviewImageSave.format` silently receives `filename_suffix`'s value. This
  fails **silently**, because the wrong value is still a valid value.
- **`Reroute` does not exist in the API graph.** Resolve every downstream reference through it to the real
  source node, or those inputs lose their link entirely.
- **`MarkdownNote` / `Note` are frontend-only** — skip them.
- **`mode: 4` (bypass) and `mode: 2` (mute)** nodes need explicit handling; the script currently skips them
  and reports it, which is safe for verification but means bypassed nodes will not appear in the prompt.
- **Execution cache**: resubmitting a byte-identical graph returns from cache in seconds. Change the seed
  (or the prompt) for A/B runs, or you will "measure" a 5-second render that never ran.
- **New custom nodes need a ComfyUI restart** before they appear in `/object_info`.
- A killed run leaves no artifact; check `/history` for `execution_error` messages rather than assuming
  the script failed.

## Files

- `scripts/workflow-to-prompt.py` — workflow JSON → API prompt, md refresh, submit and poll.
- `scripts/list-recent-outputs.py` — map recent runs to their output files (temp preview vs saved output).
- `references/workflow-to-prompt.md` — conversion rules and the full pitfall list.
- `references/mdtable-refresh.md` — FallingTS mdtable state shape, endpoints, and refresh mechanism.
- `references/output-verification.md` — probing, contact sheets, and motion/audio analysis recipes.
- `references/h3-scene-generation.md` — **measured findings for H3 scene video**: the variant performance
  table, why a single anchor image beats multi-image references, four prompt rules (positive phrasing,
  fixed camera, one action per shot, never describe the reference's own layout), rotation speed ceilings,
  the OrbitSheets parameter recipe and its limits, plus the parameter-editing and frame-extraction traps.
