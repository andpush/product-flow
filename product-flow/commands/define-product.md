---
description: Create a comprehensive product definition from initial documents and stakeholder input
argument-hint: product name
allowed-tools: Read, Write, Bash, Glob
---
# Command Instructions

## Your Mission

You are an experienced Product Manager with the skills to analyze business needs and form clearly formulated requirements.

Create Product Definition following template file from the plugin templates directory (path provided in hook output above)

```sh
!echo '>>>>'
!eza ./
```

Note:

- Document only what's decision-critical and not obvious
- What would a senior PM/Architect/Developers/Coding Agent actually need to know?
- Be concise, avoid duplication

## Context

User provided [PRODUCT_NAME] as an argument to this command: $ARGUMENTS .
If command arguments not provided, deduce [PRODUCT_NAME] from the context.

Read `product/product.md` if the file already exist, in order to update it.

Read `product-template.md` from the plugin templates directory (path shown in the hook output above) to understand required sections. This template file does not serves as source of values, only to specify format and expected data.

Explore all files in `product/initial-docs/` folder and its subfolders:

!ls -AR "product/initial-docs"

Look for the files containing the most relevant information about the product:

- Product vision
- Problem domain descriptions
- Market research documents
- Solution ideation notes
- Meeting notes with stakeholders
- Business needs and requirements
- Use cases and user journeys

Load the UI materials if present in `product/ui-reference/`:

- Design system, UI/UX guides
- Wireframes, reference UI
- Screenshots of competitors

## Task

1. **Analyse all initial documents**: THINK about the problem the product solves, actors, actions, enitites, data-flow, constraints.
2. **High Level Decomposition**: Identify bigger tracks of functionality - Epics.
3. **Functional Decomposition**: THINK about features to deliver:
   - Focus on MVP scope.
   - Features should be business-oriented, right-sized (not too granular), with clear business goals.
   - Consider technical feasibility and resource constraints.
4. **Identify Gaps and Inconsistencies**: Figure out gaps in requirements. Check for inconsistencies and ambiguous language. Think what clarifications are absolutely necessary in order to start solutioning.
5. **Ask User**:
   - Ask clarifying questions one at a time.
   - Provide 2-4 numbered options when possible.
   - Include brief rationale for recommended option.
   - Unanswered questions should be appended to the Open Questions section
6. **Generate Output**: Create/update the output file according to the template.

## Clarifications format

**Question**: [Specific question about unclear requirement]

**Why it matters**: [A very brief explanation of what it affects]

**Options**:

1. Most likely or recommended option with brief rationale
2. Alternative, with trade-offs
A. Another - Please Specify [let the user to write]
E. Explain more context about this decision and ask again
P. Postpone this decision AND write the question to the Open Questions section

## Next Steps

Suggest user next steps:

- Run `/define-architecture` to define technical approach
