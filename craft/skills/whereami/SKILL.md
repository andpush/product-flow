---
name: whereami
description: Use when user asks about the state of the project to reorient fast after a context switch — recall where work was left off, what was being solved, whether it landed, and the likely next step.
---

Reload the user's mental context in seconds. Read the artifacts, infer the story, report it compressed. NOT a code review — surface only what's needed to recall and continue.

## Gather (skip what's absent)

- `PRODUCT.md` first line — what this is.
- `docs/specs/*.md` — list, newest by filename date. Read the 1–2 most recent and not done.
- Git barnches status:
```bash
git branch --format='%(HEAD) %(refname:short) -> [%(upstream:short) %(upstream:track)] %(committerdate:relative): %(contents:subject)'
```
- `git log --oneline -15` and `git status -s` — recent moves + uncommitted work.
- `ADR.md` tail — recent architectural changes, if any.
- `IDEAS.md` — parked work / likely TBD.

## Infer

- **Last contribution**: newest spec/commits — what was being solved.
- **Solved?**: spec acceptance boxes + whether commits/tests followed. Unchecked boxes or uncommitted changes = in-flight.
- **Stuck?**: spec open but stale commits, WIP/revert/fixup churn, dangling uncommitted edits.
- **Next**: open acceptance items > top `IDEAS.md` entry.

## Report (terse — fits one screen)

```
PROJECT  <one line: what it is>
NOW      <current focus / last thing touched / if stuck indicators, explain why>
NEXT     <infer from IDEAS or current specs>

TIMELINE
2026-05-28 spec done - Auth with OAuth
2026-05-29 idea open - Caching mechanism for API responses
2026-05-29 adr  done - Billing integration with Stripe
2026-06-01 spec TODO - Export data to CSV ← here
  Summary of the current (not done) spec.

GIT BRANCHES <indicate current, upstream, ahead/behind, days since last commit, last commit message>
UNMERGED BRANCHES
RECENT MOVES
2026-05-28 <branch> <commit_id> - Implemented OAuth flow
2026-06-01 feature/stripe - Stripe dependnency added, tests in progress ←
2 uncommitted files: <infer what's there>
```
