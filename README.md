# Product Flow

AI-first product development workflow plugin for Claude Code. From idea to production.

## Installation

```claude
/plugin marketplace add andpush/product-flow
/plugin install prod-flow
```

## Workflow Overview

Product Flow guides you through structured product development in 4 phases:

```
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 1: DEFINE PRODUCT                                            │
│ ┌──────────────────┐                                               │
│ │ Your vision docs │  →  /define-product  →  product/product.md    │
│ └──────────────────┘                         (structured specs)    │
│                                                                     │
│                         /mockup-product   →  product/mockups/      │
│                                              (UI designs)           │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 2: DEFINE ARCHITECTURE                                       │
│ /define-architecture  →  product/architecture.md                   │
│                          (tech stack, components, data model)       │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 3: PLAN FEATURES                                             │
│ /add-mvp-features     →  product/features/F001-*/feature.md        │
│                          (feature breakdown)                        │
│                                                                     │
│ /mockup-feature       →  product/features/F001-*/mockups/          │
│                          (feature UI mockups)                       │
│                                                                     │
│ /plan-feature         →  product/features/F001-*/plan.md           │
│                          (implementation plan)                      │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 4: BUILD & REVIEW                                            │
│ /implement-feature    →  feature/F001-* branch                     │
│                          (code + tests)                             │
│                                                                     │
│ /review-feature       →  product/features/F001-*/review.md         │
│                          (code quality review)                      │
└─────────────────────────────────────────────────────────────────────┘
```

## Quick Start Example

**1. Create your vision documents:**
```bash
mkdir -p product/initial-docs
# Add your product vision, requirements, user research...
```

**2. Define your product:**
```claude
/define-product my-startup
```
Creates `product/product.md` with structured specs: problem, solution, features, success metrics.

**3. Design UI mockups:**
```claude
/mockup-product
```
Generates interactive HTML mockups in `product/mockups/`.

**4. Define architecture:**
```claude
/define-architecture
```
Creates `product/architecture.md` with tech stack, components, data model, deployment plan.

**5. Break down into features:**
```claude
/add-mvp-features
```
Generates feature specs in `product/features/F001-*/feature.md`.

**6. Plan a feature:**
```claude
/plan-feature F001-UserAuth
```
Creates implementation plan in `product/features/F001-UserAuth/plan.md`.

**7. Build the feature:**
```claude
/implement-feature F001-UserAuth
```
Creates feature branch, implements code and tests.

**8. Review the code:**
```claude
/review-feature F001-UserAuth
```
Generates comprehensive review in `product/features/F001-UserAuth/review.md`.

## What Gets Created

Product Flow organizes everything in a `product/` directory:

```
product/
├── initial-docs/        # Your input: vision, requirements, research
├── product.md           # Generated: structured product definition
├── architecture.md      # Generated: tech stack, components, data model
├── mockups/             # Generated: product-level UI mockups (HTML)
├── features/
│   └── F001-*/
│       ├── feature.md   # Generated: feature specification
│       ├── plan.md      # Generated: implementation plan
│       ├── review.md    # Generated: code quality review
│       └── mockups/     # Generated: feature-level UI mockups
└── adr/                 # Architecture decision records (optional)
```

## Available Commands

| Command | Purpose |
|---------|---------|
| `/define-product` | Create structured product definition from vision docs |
| `/mockup-product` | Generate interactive UI mockups for the product |
| `/define-architecture` | Design technical architecture and tech stack |
| `/add-mvp-features` | Break product into feature specs |
| `/add-feature` | Add a new feature to existing product |
| `/mockup-feature` | Generate UI mockups for a specific feature |
| `/plan-feature` | Create implementation plan for a feature |
| `/implement-feature` | Build the feature (code + tests) |
| `/review-feature` | Comprehensive code quality review |
| `/update-feature` | Update existing feature specification |
| `/figma-mockup` | Convert Figma designs to implementation specs |

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
