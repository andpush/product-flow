---
name: idea
description: Use to capture a user idea into docs/ideas/ — one small file with a quick alignment check against PRODUCT.md. Capture, not elaboration; specing happens later via `spec`.
---

Capture the idea fast and move on. Ideas are candidates, not commitments — `spec` validates lazily on pickup (pursue / defer / reject). This skill only records and sanity-checks; it never opens a spec.

Optional: if the first word of the args is `high` or `low`, treat it as the priority and strip it from the idea text (e.g. `/idea low rename cat→pet`).

## Capture

Distill the idea to one line. If it's too vague to write down, ask one clarifying question — not an interview.

Write `docs/ideas/YYYY-MM-DD-<slug>.md` — one idea per file, same naming as specs. The slug carries the idea: filenames are the index, a directory listing is the scan. Format:

```markdown
---
status: open
priority: high | low      # optional — omit when unset (untriaged)
updated: YYYY-MM-DD
target: <area>
---

# The idea in one line

Why it might matter; attached thinking the user provided, verbatim-ish.
```

`priority` is optional. Set it only if the user signals one at capture ("this matters" / "minor, someday"); otherwise omit it — an unset priority means untriaged, and `whereami` will surface it for triage. It can be added or changed by hand later. `high` = pull forward, `low` = backlog.

Don't elaborate beyond what was said. Deleting an idea is just deleting its file — the user's call, never yours.

## Lifecycle (owned by `spec`, recorded here)

Frontmatter tracks lazy validation — `spec` records the verdict when an idea is picked up:

- `status: open` — captured, unvalidated.
- `status: deferred` — evaluated, not now; stays in the scan pool alongside `open`.
- `status: pursued` — specced; add `spec: specs/YYYY-MM-DD-<slug>.md`.
- `status: rejected` — file kept so the idea isn't re-proposed.

When status leaves `open`, set `verdict:` — the one-line rationale (quote it if it contains a colon) — and bump `updated`.

**Archive on close.** On a terminal status (`pursued` or `rejected`), move the idea file — and any same-basename images — into `docs/ideas/done/`. `open` and `deferred` stay at the top level: that's the live scan pool. Create `done/` if absent (`mkdir -p`), and `git mv` when tracked so history follows.

## Check alignment

Skim `PRODUCT.md`. If the idea conflicts with it or falls outside scope, tell the user in one line and record the tension in the file — still capture it. No verdict: pursue/defer/reject belongs to `spec` on pickup.

If `PRODUCT.md` doesn't exist, capture without the check and say so.

## Images

If the user pastes an image, save it next to the idea as `docs/ideas/YYYY-MM-DD-<slug>.<ext>` (same basename) and embed it from the idea file. On pursue, the spec inherits it.

## Report

One line: file created, plus the alignment note if any.
