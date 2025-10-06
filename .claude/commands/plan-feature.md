---
description: Create detailed implementation plan for a defined feature
argument-hint: [feature_id]
allowed-tools: Read, Write, Bash, Glob
---

# Plan Feature

Create a detailed implementation plan for feature "$1" with task breakdown and time estimates.

## Prerequisites Validation

First, verify that all prerequisites are met before creating the plan:

```bash
# Check feature definition exists
if [ ! -f "product/features/$1/feature.md" ]; then
    echo "❌ Feature definition missing: product/features/$1/feature.md"
    echo "Run /define-feature $1 first"
    exit 1
fi

# Check for acceptance criteria in feature definition
if ! grep -q "## Acceptance Criteria" "product/features/$1/feature.md"; then
    echo "❌ Feature definition lacks acceptance criteria"
    echo "Cannot create implementation plan without clear acceptance criteria"
    echo "Update product/features/$1/feature.md with acceptance criteria first"
    exit 1
fi

# Check product definition exists (recommended)
if [ ! -f "product/product.md" ]; then
    echo "⚠️ Product definition missing: product/product.md"
    echo "Consider running /define-product for better context"
    read -p "Continue without product definition? (y/N): " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        exit 1
    fi
fi

# Check if plan already exists
if [ -f "product/features/$1/plan.md" ]; then
    echo "📝 Existing plan found: product/features/$1/plan.md"
    echo "Will update/enhance the existing plan"
else
    echo "🆕 Creating new implementation plan"
fi

echo "✅ Prerequisites validated - ready for planning"
echo "📋 Feature: $1"
```

## Context
You are a Tech Lead creating a detailed implementation plan for this feature.

**Required Reading:**
- `product/features/$1/feature.md` - Feature definition and requirements
- `product/architecture.md` - Technical architecture and standards
- `product/product.md` - Overall product context
- Any existing mockups in the feature directory

## Task
1. **Analyze Requirements**: Break down feature into implementable tasks
2. **Design Technical Approach**: Define implementation strategy
3. **Create Task Breakdown**: List specific development tasks with estimates
4. **Identify Risks**: Technical challenges and mitigation strategies
5. **Define Testing Strategy**: Unit, integration, and acceptance tests needed
6. **Document Plan**: Create comprehensive `product/features/$1/plan.md`

## Planning Guidelines
- **Granular Tasks**: Each task should be 2-8 hours of work
- **Clear Dependencies**: Identify task order and blockers
- **Realistic Estimates**: Include time for testing and review
- **Risk Assessment**: Flag complex or uncertain areas
- **Quality Gates**: Define when tasks are "done"

## Task Categories
- **Setup**: Development environment, dependencies, configurations
- **Backend**: APIs, database changes, business logic
- **Frontend**: UI components, state management, user interactions
- **Integration**: Connecting frontend and backend, third-party services
- **Testing**: Unit tests, integration tests, end-to-end tests
- **Documentation**: Code comments, API docs, user guides

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

## Output Requirements
- Create `product/features/$1/plan.md` using plan template
- Include detailed task breakdown with time estimates
- Define clear acceptance criteria for each task
- Identify technical risks and mitigation strategies
- Ensure plan aligns with architecture standards