---
description: Create a comprehensive product definition from initial documents and stakeholder input
argument-hint: product name
allowed-tools: Read, Write, Bash, Glob
---
# Instructions

## Validation gate

![ -d "product/initial-docs" ] || { echo "❌ Missing product/initial-docs/"; exit 1; }

## Your Mission

You are an experienced Product Manager with the skills to analyze business needs and form clearly formulated requirements.

Create a comprehensive product definition from initial documents and stakeholder input.

User provided [PRODUCT_NAME] as an argument to this command: $ARGUMENTS .
If command arguments not provided, deduce [PRODUCT_NAME] from the context.

## Read

Explore all files in `product/initial-docs/` folder and its subfolders:

!ls -AR product/initial-docs/

Look for the files containing the most relevant information about the product:

- Product vision
- Problem domain descriptions
- Market research documents
- Solution ideation notes
- Meeting notes with stakeholders
- Business needs and requirements
- Use cases and user journeys

Load the UI materials if present:

- Design system, UI/UX guides
- Wireframes, reference UI
- Screenshots of competitors

Read `product/product.md` if the file already exist, in order to update it.

Read `.claude/templates/product-template.md` to understand required sections. The values in the template file are servces as example This template file does not serves as source of values, only to specify format and expected data.

## Task

1. **Analyse all initial documents**: THINK about the problem, actors, actions, data, constraints.
2. **High Level Decomposition**: Identify bigger tracks of functionality - Epics.
3. **Functional Decomposition**: THINK about features to deliver, including what track (epic) it belongs to, what user stories the feature assumes and other related requiremets as you see in the tamplate.
4. **Identify Gaps and Inconsistencies**: Figure out gaps in requirements. Check for inconsistencies and ambiguous language. Think what clarifications are absolutely necessary in order to start solutioning.
5. **Ask Questions**: Clarify uncertainties with the user as explained in the Clarifications section.
6. **Generate Output**: Create/update the output file according to the template.

## Analysis Guidelines

- THINK product features decomposition:
  - what Epic the Feature belongs?
  - are features right-sized for agile development?
    - Features must NOT be too granular
    - Features must have clear business goal
    - Features may contain 0..5 User Stories
    - Features later decomposed into more granular Tasks
    - Features can span several components (unlike Tasks)
  - is the feature set consitutes a complete set for achieve the intended business value?
  - focus on MVP scope - what's absolutely necessary
- Consider technical feasibility and resource constraints

## Decomposition Principles

### Overview

```text
Epic (largest, may span several releases)
  └─ Feature (business-oriented capability, largest delivered piece of functionality)
      └─ User Story (specific user need/scenario, spans several components)
          └─ SubTask (atomic unit of work within one component)
```

### Epics

Epics are bigger tracks of functionality that may span several release.

- Functional Groupings: Epics serve as high-level containers that group related features together based on functionality or business capability.
- Independence: Epics represent independent groups of features that can be understood, prioritized, and potentially delivered separately from other Epics.
- Examples: "Landing Page", "Shopping Cart", "Admin Console".

### Features and User Stories

Both Features and User Stories represent deliverable pieces of functionality. Both:

- Belong to one Epic.
- May and usually span several components.

**Features**:

- Business-facing language
- Describes a capability or piece of functionality
- Example: "Product Search", "Email Notifications", "Payment Processing"

**User Stories**:

- User-facing language
- Follows the format: "As a [user], I want [goal], so that [benefit]"
- Example: "As a customer, I want to filter products by price, so that I can find items within my budget"
More granular and implementation-focused: a feature may consist of 3-10 Stories.

## Clarifications

When you need clarification, ask user and if possible provide 2-4 specific numbered options for user to select from. Be concise and clear to simplify user decision making. Ask one question at a time.

Use this format:

---
**Question**: [Specific question about unclear requirement]

**Why it matters**: [A very brief explanation of what it affects]

**Options**:

1. Most likely or recommended option with brief rationale
2. Alternative, with trade-offs
A. Another - Please Specify [let the user to write]
E. Explain more context about this decision and ask again
P. Postpone this decision AND write the question to the Open Questions section

Your choice:

---

## Next Steps

Suggest user next steps:

- Run `/define-architecture` to define technical approach
