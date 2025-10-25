# Product Flow Plugins

Complete development toolkit with two plugins for modern software development:

- **prod-flow** - AI-first product development workflow. From idea to production.
- **code-flow** - Essential code quality tools: security review, codebase exploration, and test generation.

## Installation

```claude
/plugin marketplace add andpush/product-flow
/plugin install prod-flow
/plugin install code-flow
```

## What You Get

### prod-flow plugin

- **Commands**: `/define-product`, `/define-architecture`, `/add-feature`, `/plan-feature`, `/implement-feature`, `/review-feature`, `/mockup-product`, `/mockup-feature`, `/figma-mockup`
- **Agents**: UI mockup designer, test generator, code reviewer
- **Skills**: Product discovery (requirements, validation, user research), business analysis, UI/UX design
- **Templates**: Product, architecture, feature, plan, review, ADR
- **Tech Stacks**: Java/Quarkus, Svelte, Flutter

### code-flow plugin

- **security-reviewer**: Comprehensive security audits using SAST tools (Semgrep, Bandit, npm audit, Trivy)
- **codebase-explorer**: Systematic codebase exploration at three levels (Quick Scan, Deep Analysis, Comprehensive Audit)
- **test-generator**: Auto-generate unit tests with framework awareness (Jest, pytest, RSpec, PHPUnit, Go, JUnit, Flutter)

## Quick Start: prod-flow

```bash
mkdir -p product/initial-docs
# Add your vision docs, requirements, research...

/define-product my-startup
/mockup-product
/define-architecture
/add-mvp-features
/plan-feature F001-UserAuth
/implement-feature F001-UserAuth
/review-feature F001-UserAuth
```

## Quick Start: code-flow

**Security Review:**

```claude
Use the security-reviewer skill to audit my codebase
```

**Explore Codebase:**

```claude
Use the codebase-explorer skill to do a quick scan of this project
```

**Generate Tests:**

```claude
Use the test-generator skill to create tests for src/auth/
```

## prod-flow Workflow

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
  ↓ /review-feature
product/features/F001-*/review.md  Quality review
```

## Directory Structure

### prod-flow output

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

### code-flow output

```sh
security-issues-YYYY-MM-DD/    # Security audit reports
├── CR-001.md                  # Critical vulnerabilities
├── HI-001.md                  # High severity issues
├── ME-001.md                  # Medium severity issues
└── summary.md                 # Executive summary

test/                          # Generated tests
└── [framework-specific structure]
```

## Repository Structure

```sh
/
├── prod-flow/              # AI-first product development workflow
│   ├── commands/           # Slash commands
│   ├── agents/             # Specialized agents
│   ├── skills/             # Product discovery, UI/UX, BA
│   ├── templates/          # Document templates
│   └── tech-stacks/        # Technology-specific patterns
└── code-flow/              # Code quality tools
    └── skills/
        ├── security-reviewer/
        ├── codebase-explorer/
        └── test-generator/
```

## License

MIT
