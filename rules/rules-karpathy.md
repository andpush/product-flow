# Engineering Principles (Andrei Karpathy)

All skills and work in this project follow these core disciplines:

## 1. Think Before Coding

- State assumptions explicitly. Don't hide confusion.
- If multiple interpretations exist, surface them—don't pick silently.
- If a simpler approach exists, recommend it. Push back when warranted.
- If something is unclear, stop. Name what's confusing. Ask.

## 2. Simplicity First

- Minimum code/complexity that solves the problem. Nothing speculative.
- No features beyond what was asked.
- No abstractions for single-use cases.
- No error handling for impossible scenarios.
- If you can do it in 50 lines instead of 200, do it.

## 3. Surgical Changes

- Touch only what you must. Match existing style, even if non-ideal.
- When editing: Don't "improve" adjacent code or refactor unrelated issues.
- Remove imports/functions/variables that YOUR changes made unused—not pre-existing dead code.
- Every changed line should trace directly to the request.

## 4. Goal-Driven Execution

- Define verifiable success criteria before starting.
- Transform vague requests into concrete goals: "Fix bug" → "Reproduction test passes."
- Loop until success is verified. Strong criteria prevent babysitting.

---
