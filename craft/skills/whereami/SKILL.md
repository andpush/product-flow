---
name: whereami
description: Use when user asks about the state of the project to reorient fast after a context switch — recall where work was left off, what was being solved, whether it landed, and the likely next step.
---

Reload the user's mental context in seconds. Read the artifacts, infer the story, report it compressed. NOT a code review — surface only what's needed to recall and continue.

## Gather (skip what's absent)

- `PRODUCT.md` first lines — what this is.
- List specs:
```bash
!ls -1 docs/specs/*.md | sort
```
- Scan specs that are not done:
```bash
!grep -L 'Status:\*\* Done' docs/specs/*.md
```
- Git barnches status:
```bash
!git branch --format='%(HEAD) %(refname:short) -> [%(upstream:short) %(upstream:track)] %(committerdate:relative): %(contents:subject)'
# Unnerged branches:
!git branch --no-merged
```
- Git recent moves:
```bash
!git status -s
!git log --oneline -15 --all --graph --format='%h %cd %s' --date=short
```
- `ADR.md` tail — recent architectural changes, if any.
- `IDEAS.md` — parked work / likely TBD.

## Infer

- Last contribution: newest spec/commits — what was being solved.
- Stuck? WIP/revert/fixup churn, dangling uncommitted edits.
- Next: Spec drafts or ready for impl, parked ideas, uncommitted files, feature branches not merged.

## Report (terse — fits one screen)

```
PROJECT  <one line: what it is>
NOW      <current focus / last thing touched / if stuck indicators, explain why>
NEXT     <infer from IDEAS or current specs>

TIMELINE (up to 15 entries)
<Example:
2026-05-28 spec done - Auth with OAuth
2026-05-29 idea open - Caching mechanism for API responses
2026-05-29 adr  done - Billing integration with Stripe
2026-06-01 spec TODO - Export data to CSV ← here
  Summary of the current (not done) spec.
>
GIT BRANCHES <indicate current, upstream, ahead/behind, days since last commit, last commit message>
UNMERGED BRANCHES
RECENT COMMITS <git log >
N uncommitted files: <infer what's there>
```
