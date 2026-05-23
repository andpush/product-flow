---
description: Create detailed implementation plan for a defined feature
argument-hint: [feature_id]
---
# Command Instructions

Create a detailed implementation plan for feature "$1" with task breakdown and time estimates.

## Prerequisites Validation

Verify `docs/features/$1/feature.md` exists; if not, stop and tell the user to run `/5-add-feature $1` first.

Then confirm before planning:

- The feature definition has clear, testable acceptance criteria. If not, stop and ask the user to complete `/5-add-feature $1` first.
- `docs/product.md` exists for context (recommended, not required).
- If `docs/features/$1/plan.md` already exists, update/enhance it rather than overwriting.

## Context

You are a Tech Lead creating a detailed implementation plan for a feature.

Read:

- `docs/features/$1/feature.md` - Feature definition and requirements
- `docs/architecture.md` - Technical architecture and standards
- `docs/product.md` - Overall product context
- Any existing mockups in the feature directory

## Execution

- Understand requirements
- Explore related codebase
- Create Task Breakdown, identify task order and blockers
- Ensure plan aligns with architecture standards
- Define clear acceptance criteria for each task
- Identify Risks and mitigation strategies, flag complex or uncertain areas
- Define Test Plan: what Unit, integration, and acceptance tests are required
- Save the plan in `docs/features/$1/plan.md`

## Interaction Pattern

For complex technical decisions, present options:
```
Implementation Decision: [What needs to be decided]

1. [Recommended approach]: [Benefits] | Effort: [time estimate]
2. [Alternative approach]: [Benefits] | Effort: [time estimate]
3. [Simpler approach]: [Benefits] | Effort: [time estimate]
A. Another approach (please specify)
E. Explain the technical implications
P. Postpone (implement simplest version first)
```
