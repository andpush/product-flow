---
description: Generate interactive UI mockups for a defined feature
argument-hint: [feature_id]
---
# Command Instructions

Generate interactive UI mockups for feature "$1" using the ui-mockup-generator subagent.

First, verify that the feature definition exists at `product/features/$1/feature.md`. If not, run `/define-feature $1` first.

## Task

Use the ui-mockup-generator subagent to create interactive HTML mockups based on the feature definition.

The subagent will:
1. Read and analyze the feature definition
2. Create self-contained HTML mockups with inline CSS and JavaScript
3. Generate multiple variants if beneficial
4. Save mockups in the feature directory

## Output
- Interactive HTML mockups saved to `product/features/$1/`
- File naming: `mockup-variant1.html`, `mockup-variant2.html`, etc.
- Each mockup is self-contained with all styling and interactions included

Use the Task tool to launch the ui-mockup-generator subagent with the feature_id "$1".
