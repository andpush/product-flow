---
description: Implement a planned feature following the detailed plan
argument-hint: [feature_id]
---
# Command Instructions

Implement feature "$1" following the detailed implementation plan.

## Prerequisites Validation

First, verify all prerequisites are met before starting implementation:

```bash
# Check feature definition exists
!if [ ! -f "product/features/$1/feature.md" ]; then
    echo "❌ Feature definition missing: product/features/$1/feature.md"
    echo "Run /define-feature $1 first"
    exit 1
fi

# Check implementation plan exists
if [ ! -f "product/features/$1/plan.md" ]; then
    echo "❌ Implementation plan missing: product/features/$1/plan.md"
    echo "Run /plan-feature $1 first"
    exit 1
fi

# Check for acceptance criteria in feature definition
if ! grep -q "## Acceptance Criteria" "product/features/$1/feature.md"; then
    echo "❌ Feature definition lacks acceptance criteria"
    echo "Update product/features/$1/feature.md with acceptance criteria"
    exit 1
fi

# Check for task breakdown in plan
task_count=$(grep -c "^- \[ \]" "product/features/$1/plan.md" 2>/dev/null || echo "0")
if [ "$task_count" -eq 0 ]; then
    echo "❌ Implementation plan lacks task breakdown"
    echo "Update product/features/$1/plan.md with specific tasks"
    exit 1
fi

# Check architecture definition (optional but recommended)
if [ ! -f "product/architecture.md" ]; then
    echo "⚠️ Architecture definition missing: product/architecture.md"
    echo "Consider running /define-architecture to define technical standards"
    read -p "Continue without architecture definition? (y/N): " confirm
    if [ "$confirm" != "y" ] && [ "$confirm" != "Y" ]; then
        exit 1
    fi
fi

echo "✅ Prerequisites validated - ready for implementation"
echo "📋 Feature: $1"
echo "📝 Tasks to complete: $task_count"
```

## Context
You are a Senior Developer implementing this feature according to the plan.

**Required Reading:**
- `product/features/$1/plan.md` - Implementation plan and task breakdown
- `product/features/$1/feature.md` - Feature requirements and acceptance criteria
- `product/architecture.md` - Technical architecture and coding standards
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
- **Code Coverage**: Aim for >80% test coverage for new code
- **Documentation**: Include clear comments for complex logic
- **Accessibility**: Ensure UI components meet accessibility standards
- **Responsive Design**: Test UI components across different screen sizes
- **Browser Compatibility**: Test in target browsers specified in architecture

## Testing Strategy
- **Unit Tests**: Test individual functions and components in isolation
- **Integration Tests**: Test interactions between components
- **End-to-End Tests**: Test complete user workflows
- **Manual Testing**: Verify acceptance criteria are met

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

## Test Generation

After implementation is complete, use the `test-generator` subagent to generate a comprehensive test suite:

1. Launch the `test-generator` subagent via the Task tool with the feature_id "$1"
2. The subagent will analyze the implemented code and generate tests covering:
   - Unit tests for individual functions and components
   - Integration tests for component interactions
   - Edge cases and error handling
3. Review generated tests and adjust as needed
4. Run the full test suite to verify all tests pass

## Output Requirements
- Complete implementation of all planned tasks
- Comprehensive test suite with good coverage (generated via test-generator subagent)
- Updated documentation reflecting implementation
- All acceptance criteria from feature definition met
- Code follows architecture standards and passes quality checks
- Document significant architectural decisions in `product/adr.md` using ADR template