---
name: idea
description: Use to capture a user idea into docs/ideas/ — one small file with a quick alignment check against PRODUCT.md. Capture, not elaboration; specing happens later via `spec`.
---

Capture the idea fast and move on. Ideas are candidates, not commitments — `spec` validates lazily on pickup (pursue / defer / reject). This skill only records and sanity-checks; it never opens a spec.

## Capture

Distill the idea to one line. If it's too vague to write down, ask one clarifying question — not an interview.

Write `docs/ideas/YYYY-MM-DD-<slug>.md` — one idea per file, same naming as specs. The slug carries the idea: filenames are the index, a directory listing is the scan. Format:

```markdown
# The idea in one line

YYYY-MM-DD · [area] · open

Why it might matter; attached thinking the user provided, verbatim-ish.
```

Don't elaborate beyond what was said. Deleting an idea is just deleting its file — the user's call, never yours.

## Lifecycle (owned by `spec`, recorded here)

The status line tracks lazy validation — `spec` renders the verdict when an idea is picked up:

- `open` — captured, unvalidated; deferred ideas stay `open`, optionally with a note on why not now.
- `pursued → [spec](../specs/YYYY-MM-DD-nnn-<slug>.md)` — specced.
- `rejected (one-line reason)` — file kept so the idea isn't re-proposed.

## Check alignment

Skim `PRODUCT.md`. If the idea conflicts with it or falls outside scope, tell the user in one line and record the tension in the file — still capture it. No verdict: pursue/defer/reject belongs to `spec` on pickup.

If `PRODUCT.md` doesn't exist, capture without the check and say so.

## Images

If the user pastes an image, save it next to the idea as `docs/ideas/YYYY-MM-DD-<slug>.<ext>` (same basename) and embed it from the idea file. On pursue, the spec inherits it.

## Report

One line: file created, plus the alignment note if any.
