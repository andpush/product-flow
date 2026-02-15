---
description: Review feature implementation code
argument-hint: [feature_id]
---
# Command Instructions

Perform a comprehensive code review for feature `$1` using the `code-reviewer` subagent.

## Prerequisites Validation

First, verify that the feature is ready for review:

```bash
# Check feature definition exists
if [ ! -f "product/features/$1/feature.md" ]; then
    echo "❌ Feature definition missing: product/features/$1/feature.md"
    echo "Cannot review without feature requirements"
    exit 1
fi

# Check implementation plan exists
if [ ! -f "product/features/$1/plan.md" ]; then
    echo "❌ Implementation plan missing: product/features/$1/plan.md"
    echo "Cannot review without knowing the planned approach"
    exit 1
fi

# Check if implementation appears complete
completed_tasks=$(grep -c "^- \[x\]" "product/features/$1/plan.md" 2>/dev/null || echo "0")
total_tasks=$(grep -c "^- \[\]" "product/features/$1/plan.md" 2>/dev/null || echo "0")
total_tasks=$((total_tasks + completed_tasks))

if [ "$completed_tasks" -eq 0 ]; then
    echo "❌ No completed tasks found in plan"
    echo "Feature appears not to be implemented yet"
    echo "Run /implement-feature $1 first"
    exit 1
fi

if [ "$total_tasks" -gt 0 ]; then
    completion_percentage=$((completed_tasks * 100 / total_tasks))
    echo "📊 Implementation progress: $completion_percentage% ($completed_tasks/$total_tasks tasks)"

    if [ "$completion_percentage" -lt 80 ]; then
        echo "⚠️ Feature appears to be incomplete ($completion_percentage% done)"
        read -p "Continue with review of partial implementation? (y/N): " confirm
        if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
            exit 1
        fi
    fi
fi

# Check for git repository (to analyze changes)
if [ ! -d ".git" ]; then
    echo "⚠️ No git repository found"
    echo "Code review will be limited without version control history"
fi

echo "✅ Prerequisites validated - ready for code review"
echo "📋 Feature: $1"
echo "📈 Implementation: $completion_percentage% complete"
```

## Task
Use the `code-reviewer` subagent to perform a thorough review of the implemented feature.

The subagent will:bghn
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
- Comprehensive review report saved to `product/features/$1/review.md`
- Issues categorized by severity (🔴 Critical, 🟡 Important, 🟢 Suggestion)
- Specific recommendations for improvements
- Approval status and any blocking issues

Use the Task tool to launch the code-reviewer subagent with the feature_id "$1".