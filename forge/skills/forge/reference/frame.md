# forge frame [target]

A working session between you (agent) and the human to turn an intent into a
**self-contained spec** that a cleared session, a different model, or a headless
subagent can build from. The human decides; you transfer intent, find gaps, load the
coding context, and surface the real trade-offs.

This is the backbone gate: `build` will not start without the spec this produces.

## 1. Load the coding context first

Before asking the human anything, understand the ground you're building on. Take `ARCHITECTURE.md`
as given and design *within* it — the per-feature delta, not the whole system.
- Entry points and the modules this target touches.
- Existing functions, utilities, and patterns to **reuse** — name real file paths.
- Data model and external calls involved.
- Feasibility constraints and risks specific to this codebase.

Raise architecture/feasibility questions from what you found. If the feature forces a system-level
change (new component, boundary shift, stack addition), flag it as a `ground` update — don't bake
it into the spec.

## 2. Brainstorm intent and decide

- Clarify the goal and the user value. State assumptions explicitly.
- Do gap analysis: what's ambiguous, missing, or contradictory — only what blocks building.
- Surface real forks as concrete **pro/contra** choices (architecture, approach, scope) via
  `AskUserQuestion`. Recommend the option you'd pick and why.
- Apply the project's standing decision rule (planted in `rules*.md` by `ground`): on any
  architectural choice, surface the trade-off, prefer the simpler option, **challenge a weak
  default** with a better concrete one — then move on. No paralysis, no question-answering
  theatre. Ask one thing at a time; don't ask what you can verify.
- Keep scope honest: name what's out of scope and defer non-essential ideas to `IDEAS.md`.

Record significant architectural/product decisions tersely as you settle them, in the project's
decision log — see [decisions.md](decisions.md).

## 3. Emit the spec

Write `docs/specs/YYYY-MM-DD-nnn-<slug>.md` using [spec-template.md](spec-template.md)
(`nnn` = next sequence for the date; `<slug>` = kebab feature name).

The spec is the **handoff artifact**, not a doc the human must re-read. It must be
sufficient to build from cold: goal, resolved context (real paths/patterns found), key
decisions, architecture (explicit, ASCII where it helps), scope/non-goals, affected
components, testing approach, residual open items. Concise but complete — no padding,
no restating `PRODUCT.md`/`rules*.md` (reference them).

## Done

Confirm the spec path and any open items the human still needs to resolve. If none remain,
say it's ready for `forge build <target>`. Keep the closing to a few lines.
