---
description: Review feature implementation code
argument-hint: [feature_id]
---
# Command Instructions

Perform a comprehensive code review for feature `$1` using the `code-reviewer` subagent.

## Prerequisites Validation

Verify both `features/$1/feature.md` and `features/$1/plan.md` exist; if either is missing, stop and tell the user to run `/5-add-feature` and `/7-plan-feature` first.

Before reviewing, confirm the implementation is actually done — the plan's tasks should be checked off (`- [x]`). If it looks unfinished, tell the user and ask whether to review the partial work. A git repository is recommended so changes can be analyzed.

## Task
Use the `code-reviewer` subagent to perform a thorough review of the implemented feature.

The subagent will:
1. Analyze all code changes related to this feature
2. Review security, performance, and maintainability
3. Check test coverage and quality
4. Verify acceptance criteria are met
5. Generate a comprehensive review report

## Review Scope
- **Security Analysis**: Authentication, authorization, input validation, data protection
- **Code Quality**: Architecture compliance, naming conventions, code organization
- **Performance**: Efficiency, scalability considerations, resource usage
- **Testing**: Coverage, test quality, edge cases
- **Documentation**: Code comments, API documentation, user guides
- **Acceptance Criteria**: Verify all requirements from feature definition are met

## Output
- Comprehensive review report saved to `features/$1/review.md`
- Issues categorized by severity (🔴 Critical, 🟡 Important, 🟢 Suggestion)
- Specific recommendations for improvements
- Approval status and any blocking issues

Use the Task tool to launch the code-reviewer subagent with the feature_id "$1".