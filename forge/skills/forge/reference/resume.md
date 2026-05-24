# forge resume

Zero-friction restart. Reconstruct where work stopped and propose the next move, in a few
lines — no re-reading novels.

## Gather state (read-only, fast)

- **Memory**: latest entries in `DECISIONS.md`/`ADR.md` and `IDEAS.md`.
- **Specs**: the most recent `docs/specs/*` — and whether it has unresolved open items.
- **Git**: recent commits, current branch, and uncommitted/working changes.
- **Tasks**: any state in the harness's native task tracking.

## Report (brief)

State, in a short list:
1. **Where we are** — last decision/spec and what the git state implies is in flight.
2. **What's done vs. open** — at a glance, not file-by-file.
3. **Next move** — the single most sensible next action, named as a command
   (`forge frame …` / `forge build …` / `forge review …`), with a one-line why.

Don't summarize the whole project history. Surface only what's needed to pick the work
back up without thinking. If state is contradictory (e.g. a spec with open items but code
already changed), flag that as the first thing to resolve.
