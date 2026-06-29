---
name: whereami
description: Use when user asks about the state of the project to reorient fast after a context switch — recall where work was left off, what was being solved, whether it landed, and the likely next step.
---

Reload the user's mental context in seconds. Read the artifacts, infer the story, report it compressed. NOT a code review — surface only what's needed to recall and continue.

## Gather (skip what's absent)

Top-level `docs/specs/`, `docs/next/` and `docs/ideas/` are the live set; their `done/` subfolders are the archive (specs/next-tasks `done`, ideas `pursued`/`rejected`) — read `done/` for the timeline, not as live work.

- `PRODUCT.md` first lines — what this is.
- List specs, live then archived (newest last):
```bash
ls -1 docs/specs/*.md docs/specs/done/*.md 2>/dev/null | sort
```
- Specs that are not done (draft / ready) — the live top level:
```bash
grep -L '^status: done' docs/specs/*.md 2>/dev/null
```
- Next-tasks still `todo` — small ready-to-execute work at the live top level:
```bash
grep -L '^status: done' docs/next/*.md 2>/dev/null
```
- Decisions (`ls -1 docs/adr/*.md 2>/dev/null | tail -5`, or legacy `ADR.md` tail) — recent architectural changes; filenames carry date + slug, open only if needed.
- Ideas (`grep -H '^status:\|^priority:' docs/ideas/*.md docs/ideas/done/*.md 2>/dev/null`) — candidates, not commitments; report them parked, not as tasks. Top-level `open`/`deferred` are the live pool; `done/` holds archived `pursued`/`rejected` (timeline only). Filenames carry date + slug; don't open the files. Weight the live pool by priority: lead with `high`, fold `low` into a count, and flag ideas with no `priority` as awaiting triage.
- Misplaced (closed but still at top level — bookkeeping):
```bash
grep -l '^status: done' docs/specs/*.md docs/next/*.md 2>/dev/null
grep -lE '^status: (pursued|rejected)' docs/ideas/*.md 2>/dev/null
```

## Infer

- Last contribution: newest spec/commits — what was being solved.
- Stuck? WIP/revert/fixup churn, dangling uncommitted edits.
- Next: open next-tasks, spec drafts or ready for impl, parked ideas, uncommitted files, feature branches not merged.

## Report

Produce **two** things: a glanceable HTML dashboard (the deliverable) and a 3-line chat recap (so the user need not open the file to get the gist).

### 1. HTML dashboard → `docs/YYYY-MM-DD-whereami.html`

Filename date = `date +%F`. Overwrite if it already exists (one snapshot per day). `mkdir -p docs` first.

Audience is the user reorienting at a glance, plus a non-technical stakeholder — frame it like an old JIRA status report: **business outcomes over git mechanics**. Translate artifacts into plain language ("Export to CSV — in progress", not commit hashes). Use status pills (color), font hierarchy, and monospace ASCII bars so the situation lands in one glance.

Keep it cheap: one self-contained file, inline CSS, **no JS, no images, no external fonts**. Aim ≤ ~200 lines. Emit only sections that have content.

Fill this template (drop empty rows/sections; pick the header badge `b-ok` on-track / `b-warn` slow-or-untidy / `b-stuck` blocked):

```html
<!doctype html><meta charset=utf-8><title>Where am I · {PROJECT} · {DATE}</title>
<style>
:root{--bg:#0d1117;--card:#161b22;--line:#30363d;--fg:#e6edf3;--mut:#8b949e;--green:#3fb950;--amber:#d29922;--red:#f85149;--blue:#58a6ff;--purple:#bc8cff}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.55 -apple-system,Segoe UI,Roboto,sans-serif;padding:24px}
.wrap{max-width:840px;margin:auto}.head{display:flex;justify-content:space-between;align-items:flex-start;gap:12px}
h1{font-size:12px;letter-spacing:.16em;color:var(--mut);text-transform:uppercase;margin:0 0 4px}
.proj{font-size:26px;font-weight:700;margin:0}.sub{color:var(--mut);margin:2px 0 0}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 18px;margin:14px 0}
.card h2{font-size:11px;letter-spacing:.12em;text-transform:uppercase;color:var(--mut);margin:0 0 9px}
.now{font-size:18px;font-weight:600;margin:0}.badge{padding:3px 11px;border-radius:20px;font-size:12px;font-weight:700;letter-spacing:.04em;white-space:nowrap}
.b-ok{background:rgba(63,185,80,.16);color:var(--green)}.b-warn{background:rgba(210,153,34,.16);color:var(--amber)}.b-stuck{background:rgba(248,81,73,.16);color:var(--red)}
table{width:100%;border-collapse:collapse;font-size:14px}td,th{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line)}tr:last-child td{border-bottom:0}
th{color:var(--mut);font-weight:600;font-size:11px;letter-spacing:.08em;text-transform:uppercase}
.pill{font-size:11px;font-weight:700;padding:1px 8px;border-radius:5px}.p-done{background:rgba(63,185,80,.16);color:var(--green)}.p-prog{background:rgba(210,153,34,.16);color:var(--amber)}.p-todo{background:rgba(88,166,255,.16);color:var(--blue)}.p-idea{background:rgba(188,140,255,.16);color:var(--purple)}
.bar{font-family:ui-monospace,Menlo,monospace;letter-spacing:-1px}.fill{color:var(--green)}.empty{color:var(--line)}
.mut{color:var(--mut)}.mono{font-family:ui-monospace,Menlo,monospace;font-size:13px}.tidy{border-color:var(--amber)}
ul{margin:0;padding-left:18px}li{margin:3px 0}.here{color:var(--amber);font-weight:700}
</style>
<div class=wrap>
 <div class=head><div><h1>Where am I</h1><p class=proj>{PROJECT NAME}</p><p class=sub>{one line: what it is} · {DATE}</p></div><span class="badge b-ok">ON TRACK</span></div>

 <div class=card><h2>Now</h2><p class=now>{current focus / last thing touched}</p>{if stuck: <p class=mut>{why — WIP/revert churn, dangling edits}</p>}</div>

 <div class=card><h2>Delivery</h2><span class="bar"><span class=fill>██████</span><span class=empty>░░░░</span></span> {X of N specs shipped} · {M in progress} · {K queued}</div>

 <div class=card><h2>Next — what moves it forward</h2><ul><li>{committed next-task or ready spec}</li>…</ul></div>

 <div class=card><h2>Workstreams</h2><table><tr><th>Item</th><th>Type</th><th>Status</th></tr>
  <tr><td>{plain-language name}</td><td class=mut>spec</td><td><span class="pill p-prog">in progress</span></td></tr>
  … pills: p-done done · p-prog in progress · p-todo queued/draft · p-idea idea
 </table></div>

 <div class=card><h2>Parked ideas</h2><p>{N awaiting validation. Lead with high-priority names; fold low into a count; flag M untriaged.}</p></div>

 <div class="card tidy"><h2>⚠ Tidy up</h2><p>{closed files still at top level — suggest git mv into done/. Omit whole card when clean.}</p></div>

 <div class=card><h2>Timeline</h2><table>
  <tr><td class=mut>2026-06-01</td><td><span class="pill p-todo">spec</span></td><td>Export data to CSV <span class=here>← you are here</span></td></tr>
  … up to 15, newest last, business-readable titles
 </table></div>

 <div class=card><h2>Activity</h2><p class=mut>{1 line: e.g. "3 branches, 1 unmerged (feature/x) · 4 uncommitted files — local edits to …"}</p></div>
</div>
```

ASCII bar rule: 10 cells, fill = round(done/total·10) green blocks `█`, rest grey `░`. Use it for the Delivery rollup; reuse for any item with a clear %.

### 2. Chat recap (3 lines, then stop)

```
PROJECT  <one line>
NOW      <focus / last touched / why-stuck if any>
NEXT     <single most useful next move>
→ docs/YYYY-MM-DD-whereami.html
```

Make the path a clickable markdown link. Do not dump git output or the timeline into chat — that detail lives in the report.

