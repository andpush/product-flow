---
name: whereami
description: Use when user asks about the state of the project to reorient fast after a context switch — recall where work was left off, what was being solved, whether it landed, and the likely next step.
---

Reload the user's mental context in seconds. Read the artifacts, infer the story, report it compressed. NOT a code review — surface only what's needed to recall and continue.

## Gather (skip what's absent)

- `PRODUCT.md` first lines — what this is.
- List specs (newest last):
```bash
ls -1 docs/specs/*.md 2>/dev/null | sort
```
- Specs that are not done (draft / ready):
```bash
grep -L '^status: done' docs/specs/*.md 2>/dev/null
```
- Decisions (`ls -1 docs/adr/*.md 2>/dev/null | tail -5`, or legacy `ADR.md` tail) — recent architectural changes; filenames carry date + slug, open only if needed.
- Ideas (`grep -H '^status:' docs/ideas/*.md 2>/dev/null`) — candidates, not commitments; report them parked, not as tasks. `open`/`deferred` are the live pool. Filenames carry date + slug; don't open the files.

## Infer

- Last contribution: newest spec/commits — what was being solved.
- Stuck? WIP/revert/fixup churn, dangling uncommitted edits.
- Next: Spec drafts or ready for impl, parked ideas, uncommitted files, feature branches not merged.

## Report (terse — fits one screen)

Emit every section below. The last three are verbatim pass-throughs of the gathered git output — never summarize or drop them because TIMELINE overlaps; they are separate on purpose.

PROJECT  <one line: what it is>
NOW      <current focus / last thing touched / if stuck indicators, explain why>

NEXT     <infer from current state: unfinished specs, branches, uncommitted edits, ideas, project goals — what moves the project forward. Recorded ideas are candidates, not commitments.>

PARKED   <one line: N ideas in docs/ideas/ awaiting validation; name 1-3 standouts. "none" if empty>

TIMELINE (up to 15 entries)
<Example:
2026-05-28 spec done - Auth with OAuth
2026-05-29 idea open - Caching mechanism for API responses
2026-05-29 adr  done - Billing integration with Stripe
2026-06-01 spec TODO - Export data to CSV ← here
  Summary of the current (not done) spec.
>
GIT BRANCHES
<verbatim
```bash
git branch --format='%(HEAD) %(refname:short) -> [%(upstream:short) %(upstream:track)] %(committerdate:relative): %(contents:subject)'
```
>
UNMERGED BRANCHES
<verbatim `git branch --no-merged` output; "none" if empty>
RECENT COMMITS
<verbatim
```bash
git log --oneline -10 --all --graph --format='%h %cd %s' --date=short
git status --porcelain
```>
N uncommitted files: <Infer what changes are there>

