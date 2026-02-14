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

Provides workflow for AI-first product development:

```markdown
product/initial-docs/     → /define-product    → product/product.md
                          → /define-architecture → product/architecture.md
                          → /add-feature        → product/features/F001-*/feature.md
                          → /plan-feature       → product/features/F001-*/plan.md
                          → /implement-feature  → feature branch with code
                          → /review-feature     → product/features/F001-*/review.md
```

### code-flow plugin

Provides code quality and security skills:

- **security-reviewer**: Runs SAST tools (Semgrep, Bandit, npm audit, Trivy), generates `security-issues-YYYY-MM-DD/` reports
- **codebase-analyzer**: Three-level exploration (Quick Scan, Deep Analysis, Comprehensive Audit)
- **test-generator**: Framework-aware test generation (Jest, pytest, RSpec, PHPUnit, Go, JUnit, Flutter)

### Reusable rules in `rules/` folder

Optionally select and copy rules for your tech stack from `rules/` folder. These rules can be customized and extended as needed.

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

## Directory Structure assumed by prod-flow

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
