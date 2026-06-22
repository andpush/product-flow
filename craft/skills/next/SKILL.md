---
name: next
description: Use to record a small, ready-to-execute task as a terse handoff doc in docs/next/ — for a focused change (typically one component) that's too concrete for `idea` and too small for a full `spec`. Explore the relevant code, confirm you understood the intent, resolve gaps, then write a self-contained brief an implementor executes from cold without further questions. Use for quick fixes, scoped enhancements, chores, and "just do X" tasks.
---

Turn a small, concrete request into a build-ready handoff doc. The bet: a few minutes confirming intent and scoping the code now saves the implementor a round-trip later. The deliverable is the doc, not code — don't implement here.

`next` sits between `idea` (unvalidated capture, no execution intent) and `spec` (non-trivial change needing architecture work). It assumes the *what* is already roughly decided and the change is small — usually one component, no architecture decisions. Its whole job is to remove ambiguity before handoff.

## When to escalate to `spec`

If exploration reveals the task spans several components, forces an architecture decision (new boundary, data model change, source-of-truth shift, new dependency), or carries real design risk — stop and recommend `spec` instead. Don't quietly grow a `next` doc into a spec; say so and let the user choose.

## Process

Keep it tight — this is a quick exchange, not a spec session.

### 1. Frame & explore
Reflect the request back in one line. Locate the affected component and read the relevant code — enough to ground the task in real files and names, no more. Note what already exists that the implementor will touch or follow.

### 2. Confirm & close gaps
Ask only the sharp unknowns that change the outcome — the ones the implementor would otherwise have to stop and ask. Surface anything ambiguous, then state your understanding and the gaps you spotted. Bring a recommendation to each open point; don't make the user author from scratch. Get the nod before writing.

This is the core value: an implementor should be able to execute from the doc cold, without coming back to the user.

### 3. Write the doc
`docs/next/YYYY-MM-DD-<slug>.md` (`<slug>` = kebab task name — the filename is the index). A next doc is a brief, not a spec: aim for one screen. Keep it terse; cut any section that adds nothing. If it's growing past a screen with diagrams and layered decisions, that's the signal it wanted to be a `spec`.

```markdown
---
status: todo        # todo | done
updated: YYYY-MM-DD
target: <component / area>
---

# <Task in one line>

**Goal:** what to do and why, in a sentence or two.

**Context:** the files/component to touch and any existing code, pattern, or convention to follow. Link, don't restate.

**Do:** the concrete change — bullet steps if it helps.

**Acceptance:** the verifiable done condition. Minimum: builds, runs, lint clean, behavior observable; tests where they pin intent.

**Notes:** decisions resolved in this session and constraints the implementor must respect — one line each, the decision not the debate, so nothing has to be re-asked. Omit if none.
```

### 4. Report
One or two lines: file created, plus the one-line `/goal <file>` (or subagent brief) that executes it. If you recommended escalating to `spec`, say that instead.

## Lifecycle

Mirrors specs. `status: todo` while live at top level; on completion the implementor flips `status: done`, bumps `updated`, and moves the file to `docs/next/done/` so the top level stays the live queue. `whereami` lists open next-tasks as actionable work and flags any `done` file still sitting at top level. Deleting a task file is the user's call, never yours.
