# Product Flow

AI-first product development workflow for Claude Code. From idea to production.

## What You Get

`product-flow` plugin includes everything you need - commands, agents, templates, and product discovery expertise:

- **Commands** - `/define-product`, `/plan-feature`, `/implement-feature`, etc.
- **Agents** - UI mockup designer, test generator, code reviewer
- **Skills** - Business analysis, UI/UX design, lean startup, workflow coordination
- **Templates** - Product, feature, plan, architecture, review docs

## Installation

```claude
/plugin marketplace add andpush/product-flow
/plugin install product-flow
```

**Optional** - Add tech stack expertise:

```claude
/plugin install tech-stacks
```

### What's Included

**product-flow** - Complete workflow in one plugin:

- **Commands**: `/define-product`, `/define-architecture`, `/add-feature`, `/plan-feature`, `/implement-feature`, `/feature-review`, `/mockup-product`, `/mockup-feature`, `/figma-mockup`
- **Agents**: UI mockup designer, test generator, code reviewer
- **Skills**: Product discovery (requirements, validation, user research), workflow coordination, UI/UX design
- **Templates**: Product, architecture, feature, plan, review, ADR, mockup

**tech-stacks** (optional):

- Java/Quarkus backend patterns
- Svelte frontend patterns
- Flutter mobile patterns

## Quick Start

```bash
mkdir -p product/initial-docs
# Add your vision docs, requirements, research...

/define-product my-startup
/mockup-product
/define-architecture
/add-mvp-features
/plan-feature F001-UserAuth
/implement-feature F001-UserAuth
/feature-review F001-UserAuth
```

## Workflow

```sequence
product/initial-docs/          Your vision, research, requirements
  ↓ /define-product
product/product.md             Structured product definition
  ↓ /add-mvp-features
product/features/F001-*/       Feature specs
  ↓ /plan-feature
product/features/F001-*/plan.md  Implementation plan
  ↓ /implement-feature
feature/F001-* branch          Code + tests
  ↓ /feature-review
product/features/F001-*/review.md  Quality review
```

## Directory Structure

```sh
product/
├── initial-docs/        # Input: your vision, research, requirements
├── product.md           # Output: structured product definition
├── architecture.md      # Output: technical architecture
├── features/
│   └── F001-Name/
│       ├── feature.md   # Feature specification
│       ├── plan.md      # Implementation plan
│       ├── review.md    # Code review
│       └── mockups/     # UI designs
├── mockups/             # Product-level mockups
└── adr/                 # Architecture decision records
```

## License

MIT
