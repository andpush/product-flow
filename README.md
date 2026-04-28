# Product Flow

Product development workflow for agentic development. From idea to production.

## Installation

```claude
/plugin marketplace add andpush/product-flow
/plugin install prod-flow
```

## Workflow Overview

Product Flow guides you through structured product development:

```
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────────────┐
│ Your vision docs │     │ /1-define-product│     │ /2-mockup-product        │
│ docs/initial/**  │────▶│ docs/product.md  │────▶│ docs/mockups/ (optional) │
└──────────────────┘     └───┬──────────────┘     └──────────────────────────┘
                             │
                     ┌───────┴──────────┐
                     ▼                  ▼
         ┌────────────────────────┐  ┌────────────────────────┐
         │ /3-define-architecture │  │ /4-add-mvp-features    │
         │ architecture.md        │  │ docs/features/F001-*/  │
         └────────────────────────┘  │ feature.md             │
                                     └───────┬────────────────┘
                                             │
                                             ▼
                                  ┌─────────────────-----------─┐
                                  │ /6-mockup-feature           │
                                  │ F001-*/mockups/ (optional)  │
                                  └────────┬───────-----------──┘
                                           │
                                           ▼
                                  ┌─────────────────────┐
                                  │ /7-plan-feature     │
                                  │ F001-*/plan.md      │
                                  └────────┬────────────┘
                                           │
                                           ▼
                                  ┌──────────────────────┐
                                  │ /8-implement-feature │
                                  │ feature branch       │
                                  │ code + tests         │
                                  └────────┬─────────────┘
                                           │
                                           ▼
                                  ┌───────────────────┐
                                  │ /9-review-feature │
                                  │ F001-*/review.md  │
                                  └───────────────────┘
```

## Quick Start Example

**1. Create your vision documents:**
```bash
mkdir -p docs/initial
# Add your product vision, requirements, user research...
```

**2. Define your product:**
```claude
/1-define-product my-startup
```
Creates `docs/product.md` with structured specs: problem, solution, features, success metrics.

**3. Design UI mockups:**
```claude
/2-mockup-product
```
Generates interactive HTML mockups in `docs/mockups/`.

**4. Define architecture:**
```claude
/3-define-architecture
```
Creates `docs/architecture.md` with tech stack, components, data model, deployment plan.

**5. Break down into features:**
```claude
/4-add-mvp-features
```
Generates feature specs in `docs/features/F001-*/feature.md`.

**6. Plan a feature:**
```claude
/5-plan-feature F001-UserAuth
```
Creates implementation plan in `docs/features/F001-UserAuth/plan.md`.

**7. Build the feature:**
```claude
/8-implement-feature F001-UserAuth
```
Creates feature branch, implements code and tests.

**8. Review the code:**
```claude
/9-review-feature F001-UserAuth
```
Generates comprehensive review in `docs/features/F001-UserAuth/review.md`.

## What Gets Created

Product Flow organizes everything in a `docs/` directory:

```
docs/
├── initial/        # Your input: vision, requirements, research
├── product.md           # Generated: structured product definition
├── architecture.md      # Generated: tech stack, components, data model
├── adr.md               # Generated: Architecture Decision Records
├── mockups/             # Generated: product-level UI mockups (HTML)
├── features/
│   └── F001-*/
│       ├── feature.md   # Generated: feature specification
│       ├── plan.md      # Generated: implementation plan
│       ├── review.md    # Generated: code quality review
│       └── mockups/     # Generated: feature-level UI mockups
```

## Skills & Agents

**Skills** (invoke with "use the X skill"):
- `ba` - Business analysis and requirements decomposition
- `sa` - Software architecture design
- `code-explorer` - Codebase exploration and understanding
- `code-reviewer` - Code quality review and improvements
- `slides` - Create presentation decks from markdown
- `uiux-design` - UI/UX design expertise

**Agents** (autonomous specialists):
- `code-reviewer` - Automated code review agent
- `test-generator` - Test generation agent
- `ui-mockup-designer` - UI mockup design agent

## License

MIT
