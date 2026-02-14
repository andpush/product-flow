---
name: code-reviewer
description: This skill should be used when the user asks to "review code quality", "find issues in the code", "audit the codebase", "check for bugs", "suggest code improvements", or mentions code review, technical debt analysis.
---

Perform a focused code quality review. Report only actionable, code-specific findings — no generic advice.

## Review Dimensions

1. **Security** — injection, hardcoded secrets, auth gaps, input validation
2. **Correctness** — logic errors, race conditions, unhandled edge cases, data integrity
3. **Performance** — N+1 queries, missing indexes, unnecessary allocations, blocking calls
4. **Maintainability** — dead code, duplication, unclear naming, tight coupling
5. **Reliability** — error handling gaps, silent failures, resource leaks

## Process

1. Identify tech stack and conventions from config/build files
2. Trace critical paths (entry points → data layer → external calls)
3. Flag concrete issues with file:line references
4. Prioritize by impact: P0 = must fix, P1 = should fix, P2 = nice to have

## Output Format

```
## Summary
One-paragraph assessment. Recommendation: ✅ Good / ⚠️ Needs Work / ❌ Critical Issues

## Findings

| P | Category | Location | Issue | Fix |
|---|----------|----------|-------|-----|
| P0 | Security | file:line | specific finding | concrete action |
| P1 | Correctness | file:line | specific finding | concrete action |

## Positive Patterns
What the codebase does well (brief)
```
