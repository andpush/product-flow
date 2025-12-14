# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Product Flow is a Claude Code plugin marketplace containing two plugins for AI-first software development:

- **prod-flow** - AI-first product development workflow (idea → production)
- **code-flow** - Code quality tools (security review, codebase analysis, test generation)

## Repository Structure

```
/
├── .claude-plugin/           # Marketplace registration (marketplace.json)
├── prod-flow/                # Product development workflow plugin
│   ├── commands/             # Slash commands (/define-product, /plan-feature, etc.)
│   ├── agents/               # Specialized agents (code-reviewer, test-generator, ui-mockup-designer)
│   ├── skills/               # Skills (architecture, ba, product-validation, slides, uiux-design)
│   └── templates/            # Document templates (feature, plan, review, ADR)
├── code-flow/                # Code quality tools plugin
│   └── skills/               # Skills (security-reviewer, codebase-analyzer, test-generator)
├── rules/                    # Coding rules (general, backend, mobile, tests, ui, webapp)
└── product/                  # Example output directory structure
```

## Plugin Architecture

Each plugin follows Claude Code plugin conventions:
- **Commands**: Markdown files in `commands/` with YAML frontmatter (description, argument-hint, allowed-tools)
- **Skills**: SKILL.md files defining specialized agent behavior with references subdirectories
- **Agents**: Markdown files defining agent personas and capabilities

## Key Workflows

### prod-flow Workflow
```
product/initial-docs/     → /define-product    → product/product.md
                          → /define-architecture → product/architecture.md
                          → /add-feature        → product/features/F001-*/feature.md
                          → /plan-feature       → product/features/F001-*/plan.md
                          → /implement-feature  → feature branch with code
                          → /review-feature     → product/features/F001-*/review.md
```

### code-flow Workflow
- **security-reviewer**: Runs SAST tools (Semgrep, Bandit, npm audit, Trivy), generates `security-issues-YYYY-MM-DD/` reports
- **codebase-analyzer**: Three-level exploration (Quick Scan, Deep Analysis, Comprehensive Audit)
- **test-generator**: Framework-aware test generation (Jest, pytest, RSpec, PHPUnit, Go, JUnit, Flutter)

## Architectural Conventions (from rules/rules-general.md)

- **Layered Architecture**: Service → Store → Database
- **Package Structure**: Group by feature, not by layer
- **Services**: Exposed via REST by default
- **DTOs**: Only create if data shapes differ from entities
- **Stores**: JDBI SQL annotated interfaces (Java/Kotlin)
- **Monorepo Layout**: Component folders (backend/, mobile/, web/) in root

## Documentation Standards

Maintain these files in target projects:
- `README.md`: Project overview, components, commands
- `CHANGELOG.md`: User-facing changes log
- `ADR.md`: Architectural decisions with date, decision, motivation

## Feature Sizing

Features use T-shirt sizes: XS, S, M, L, XL

## Feature ID Convention

Features are numbered: `F001-FeatureName`, `F002-AnotherFeature`
