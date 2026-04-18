---
name: code-explorer
description: This skill should be used when the user asks to "explore the codebase", or wants to build understanding of an unfamiliar repository.
---

Map repository structure, architecture, and dependencies as a senior engineer onboarding to an unfamiliar codebase.

## Tasks

1. **Structure Analysis**
   - Scan config files, build scripts, directory layout → identify tech stack, modules, dependencies
   - Check docs (note staleness)

2. **Code Analysis**
   - Entry points, APIs, data flow
   - Core entities, dependencies, component interactions
   - Patterns used (DI, event-driven, layered, etc.)
   - Error handling and logging approach

3. **Quality & Risk Signals**
   - Dead code, unused dependencies, circular imports
   - Missing tests or test coverage gaps
   - Hardcoded values, secrets, config smells
   - Outdated dependencies or deprecated APIs

## Output Format

```
## Overview
Purpose, problem solved, key features

## Tech Stack
| Layer | Technology | Version |
|-------|-----------|---------|

## Architecture
Components with responsibilities (table format)
Diagram: structure and data flow (Mermaid)

## Key Patterns
How the codebase is organized, conventions followed

## Risks & Gaps
| Severity | Category | Location | Finding |
|----------|----------|----------|---------|
| High | maintenance | file:line | specific actionable issue |

(High = blocks contribution, Med = impacts maintenance/perf, Low = minor)

## Onboarding Notes
- How to build/run/test
- Key files to read first
- Non-obvious gotchas
```
