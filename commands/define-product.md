---
description: Create a comprehensive product definition from initial documents and stakeholder input
argument-hint: product name
allowed-tools: Read, Write, Bash, Glob
---
# Command Instructions

## Your Mission

Use the `product-discovery` skill to create a comprehensive Product Definition in `product/product.md`.

## Context

User provided [PRODUCT_NAME] as an argument to this command: $ARGUMENTS .
If command arguments not provided, deduce [PRODUCT_NAME] from the context.

Explore the following files:

```bash
product/
├── initial-docs/**    # Initial documents to research
├── product.md         # (if exists) previous definition to update
```

`!ls -AR "product/initial-docs"`

Look for the files containing the most relevant and up-to-date information about the product:

- Product vision
- Business domain
- Problem statement
- Market research
- Solution ideation notes
- Meeting notes with stakeholders
- Business needs and requirements
- Use cases and user journeys

Load the UI materials if present:

- Design system, UI/UX guides
- Wireframes, reference UI
- Screenshots of competitors, similar or related solutions

## Task

1. **Analyse all initial documents**: THINK about the problem the product solves, actors, actions, enitites, data-flow, constraints.
2. **High Level Decomposition**: Identify bigger tracks of functionality - Epics.
3. **Functional Decomposition**: THINK about features to deliver:
   - Focus on MVP scope.
   - Features should be business-oriented, right-sized (not too granular), with clear business goals.
   - Consider technical feasibility and resource constraints.
4. **Identify Gaps and Inconsistencies**: Figure out gaps in requirements. Check for inconsistencies and ambiguous language. Think what clarifications are absolutely necessary in order to start solutioning.
5. **Ask User**:
   - Ask clarifying questions one at a time
   - Wait user definite answer before asking another question
   - Provide 2-4 numbered options when possible
   - Include brief rationale for recommended option

   ```markdown
   ---
   **Question**: [Specific question about unclear requirement]

   **Why it matters**: [A very brief explanation of what it affects]

   **Options**:

   1. Most likely or recommended option with brief rationale
   2. Alternative, with trade-offs
   A. Another - Please Specify [let the user to write]
   P. Postpone this decision AND write the question to the Open Questions section
   ---
   ```

6. **Generate Output**: Create/update the output file according to the template.

## Next Steps

Suggest user next steps:

- Run `/define-architecture` to define technical approach
