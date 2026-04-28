---
description: Create detailed implementation plan for a defined feature
argument-hint: [feature_id]
---
# Command Instructions

Create a detailed implementation plan for feature "$1" with task breakdown and time estimates.

## Prerequisites Validation

First, verify that all prerequisites are met before creating the plan:

```bash
# Check feature definition exists
if [ ! -f "docs/features/$1/feature.md" ]; then
    echo "❌ Feature definition missing: docs/features/$1/feature.md"
    echo "Run /define-feature $1 first"
    exit 1
fi

# Check for acceptance criteria in feature definition
if ! grep -q "## Acceptance Criteria" "docs/features/$1/feature.md"; then
    echo "❌ Feature definition lacks acceptance criteria"
    echo "Cannot create implementation plan without clear acceptance criteria"
    echo "Update docs/features/$1/feature.md with acceptance criteria first"
    exit 1
fi

# Check product definition exists (recommended)
if [ ! -f "docs/product.md" ]; then
    echo "⚠️ Product definition missing: docs/product.md"
    echo "Consider running /define-product for better context"
    read -p "Continue without product definition? (y/N): " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        exit 1
    fi
fi

# Check if plan already exists
if [ -f "docs/features/$1/plan.md" ]; then
    echo "📝 Existing plan found: docs/features/$1/plan.md"
    echo "Will update/enhance the existing plan"
else
    echo "🆕 Creating new implementation plan"
fi

echo "✅ Prerequisites validated - ready for planning"
echo "📋 Feature: $1"
```

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
