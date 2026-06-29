---
name: tests-optimizer
description: Review a test suite to find and remove low-value tests — trivial assertions, tests for removed functionality, redundant duplicates, over-costly integration/e2e tests that belong lower in the pyramid, and tests left obsolete by refactoring. Use whenever the user wants to prune, clean up, slim down, de-duplicate, or speed up their tests, audit test value, or trim a slow/bloated suite.
---

## Goal

A test suite earns its keep by catching regressions cheaply. Tests that can't fail meaningfully, that duplicate each other, or that cost more to run and maintain than the confidence they buy are liabilities — they slow CI, obscure real signal, and make refactoring painful. Find them, justify each, get the user's sign-off, remove them, and prove the suite is faster and still green.

Flag for removal only. Never weaken real coverage: a test is safe to cut only if its meaningful assertions are subsumed elsewhere, or they target something that no longer warrants testing. When in doubt, keep it and say why.

## Process

1. **Map the suite.** Detect the test framework, runner, and how layers are split (unit / integration / e2e) from config and conventions (test dirs, file suffixes, markers/tags, CI config). State your layer definitions so the user can correct them.
2. **Baseline metrics.** Run the suite (or per-layer) to capture counts and wall-clock time. If running is infeasible, count statically and estimate time from a prior run or markers — say so. Record the **Before** table (see Metrics).
3. **Review across the five dimensions** below. Read tests against the code they cover, not in isolation — a duplicate or stale test is only visible relative to the rest.
4. **Report** flagged tests grouped by dimension, each with `file:line`, a one-line rationale, and the safe-to-cut justification.
5. **Confirm.** Present the report and ask the user to approve removals — per dimension or per test. Do not delete anything before sign-off.
6. **Clean up** the approved set. Where a duplicate cluster has value as a single parametrized case, prefer merging over plain deletion.
7. **Re-measure and prove it.** Re-run the suite: it must stay green and coverage of real code must not drop. Record the **After** table and the delta.

## The five dimensions

1. **Trivial** — asserts a language/framework/library guarantee, a plain getter/setter, a constant's literal value, or a mock returning what it was told to. It cannot fail for a reason that matters.
2. **Stale** — exercises functionality that no longer exists or is dead, or merely asserts that something was removed. Once the feature is gone the test is noise; the type system or its own absence already covers it.
3. **Redundant** — covers the same path as another test with only cosmetically different inputs, such that a real bug fails several at once. One representative (or a single parametrized case spanning the inputs) carries the signal; the rest are maintenance tax. Distinguish from genuine boundary/equivalence-class cases, which are not redundant.
4. **Over-costly (pyramid)** — an integration or e2e test whose logic a fast unit test could cover, or a slow/flaky high-level test duplicating coverage that already exists lower down. The pyramid wants many cheap unit tests, fewer integration, fewest e2e. Recommend pushing coverage down a layer rather than only deleting.
5. **Refactoring repercussion** — code simplification orphaned the test: it targets branches that no longer exist, helpers that were inlined, or internal structure that was collapsed. Often over-mocked and coupled to the old shape.

## Metrics

Report Before and After as a table — rows by layer and by component, columns count and time — plus the delta.

```
| Layer       | Component | Tests (before→after) | Time (before→after) |
|-------------|-----------|----------------------|---------------------|
| unit        | auth      | 48 → 41              | 1.2s → 1.0s         |
| integration | auth      | 12 → 7               | 8.4s → 4.9s         |
| e2e         | checkout  | 6 → 5                | 41s → 33s           |
| **Total**   |           | **N → M**            | **Ts → Us**         |
```

State the headline up front: tests removed/merged by dimension, total time saved, suite still green, coverage unchanged on real code.

## Report format

```
## Test optimization — <repo> — YYYY-MM-DD

### Before
<metrics table>

### Flagged
#### 1. Trivial
| Test | Location | Why | Safe to cut because |
| --- | --- | --- | --- |
... (one table per dimension that has findings)

### Uncertain
Findings you're not confident about — keep unless the user decides otherwise.
```

After cleanup, append the **After** table and delta to the same report. Write it to `docs/tests-optimizer-YYYY-MM-DD.md` unless the user says otherwise. Change only test files during cleanup; never alter production code to make a test removable.
