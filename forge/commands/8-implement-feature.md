---
description: Implement a planned feature following the detailed plan
argument-hint: [feature_id]
---
# Command Instructions

Implement feature "$1" following the detailed implementation plan.

## Prerequisites Validation

Verify both `features/$1/feature.md` and `features/$1/plan.md` exist. If `feature.md` is missing, stop and tell the user to run `/5-add-feature $1`; if `plan.md` is missing, `/7-plan-feature $1`. Confirm the feature has testable acceptance criteria and the plan has an unchecked task breakdown before starting. `ARCHITECTURE.md` is recommended for coding standards — if it's missing, note that and proceed.

## Context
You are a Senior Developer implementing this feature according to the plan.

**Required Reading:**
- `features/$1/plan.md` - Implementation plan and task breakdown
- `features/$1/feature.md` - Feature requirements and acceptance criteria
- `ARCHITECTURE.md` - Technical architecture and coding standards
- Any mockups in the feature directory for UI reference

## Task
1. **Create Feature Branch**: Create and switch to feature branch `feature/$1`
2. **Follow the Plan**: Implement tasks in the order specified in the plan
3. **Write Tests First**: Create tests before implementing functionality (TDD)
4. **Implement Incrementally**: Complete one task fully before moving to the next
5. **Maintain Quality**: Follow architecture standards and coding conventions
6. **Document Changes**: Update relevant documentation as you implement
7. **Validate Continuously**: Test each component as it's built

## Implementation Guidelines
- **Test-Driven Development**: Write failing tests, then implement to make them pass
- **Atomic Commits**: Commit completed tasks with clear, descriptive messages
- **Code Quality**: Follow established patterns, naming conventions, and style guides
- **Error Handling**: Include proper error handling and validation
- **Performance**: Consider performance implications of implementation choices
- **Security**: Follow security best practices for authentication, data handling, etc.

## Quality Standards
- **Coverage**: Meet the coverage targets in `ARCHITECTURE.md` if defined; otherwise cover the acceptance criteria and the non-trivial logic.
- **Documentation**: Comment the *why* for non-obvious logic.
- **For UI features**: verify accessibility, responsive behavior, and target browsers as specified in `ARCHITECTURE.md`.

## Testing Strategy
Match the architecture's testing strategy. Typically: unit tests for logic and edge cases, integration tests for component/API interactions, and end-to-end tests for critical workflows. Always verify the feature's acceptance criteria.

## Interaction Pattern
If you encounter blockers or need clarification:
```
Implementation Issue: [What's blocking progress]

1. [Recommended solution]: [Approach] | Impact: [scope of change]
2. [Alternative solution]: [Approach] | Impact: [scope of change]
3. [Workaround]: [Temporary approach] | Impact: [scope of change]
A. Another approach (please specify)
E. Explain the technical implications
S. Skip for now (add to technical debt)
```

## Progress Tracking
- Mark completed tasks in the plan document
- Note any deviations from the original plan
- Document new tasks discovered during implementation
- Update time estimates based on actual implementation

## Filling Test Gaps

TDD already produces the primary tests during implementation. After the feature is complete, optionally use the `test-generator` subagent to **fill remaining gaps** — uncovered edge cases, error paths, and integration points the TDD cycle didn't reach. Do not regenerate a parallel suite; extend what exists. Review the additions and run the full suite to confirm everything passes.

## Output Requirements
- Complete implementation of all planned tasks
- Tests covering acceptance criteria and edge cases, all passing
- Updated documentation reflecting implementation
- Code follows architecture standards and passes quality checks
- Document significant architectural decisions in `docs/adr/` using the ADR template