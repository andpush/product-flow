---
name: product-flow-core
description: AI-first SDLC workflow coordination, configuration, and path resolution
version: 1.0.0
---

# Product Flow Core

AI-first SDLC workflow system for startup product development.

## Description

Provides structured product development workflow from discovery through implementation. Handles configuration, path resolution, workflow awareness, and prerequisite validation.

## When to Activate

Activate when:
- Repository contains `.claude/commands/define-product.md` or other product-flow commands
- User mentions product definition, features, planning, or SDLC phases
- Working with files in `product/` directory structure
- User asks about workflow or next steps

## Configuration Management

### Path Resolution

Read configuration from `.claude/lib/config.md` to resolve logical paths:

- `{{PRODUCT_ROOT}}` → Default: `product/`
- `{{INITIAL_DOCS}}` → Default: `product/initial-docs/`
- `{{UI_REFERENCE}}` → Default: `product/ui-reference/`

Derived paths (auto-computed):
- `{{FEATURES}}` → `{{PRODUCT_ROOT}}/features/`
- `{{ARCHITECTURE}}` → `{{PRODUCT_ROOT}}/architecture.md`
- `{{PRODUCT_MD}}` → `{{PRODUCT_ROOT}}/product.md`
- `{{ADR}}` → `{{PRODUCT_ROOT}}/adr/`
- `{{MOCKUPS}}` → `{{PRODUCT_ROOT}}/mockups/`

### Configuration Override

If project has custom paths, check for local `.claude/config.md` and use those values instead of defaults.

## Workflow Awareness

Detect current project phase and suggest appropriate next steps:

### Phase Detection

1. **Pre-Discovery Phase**:
   - Indicator: No `{{PRODUCT_MD}}` exists
   - Suggestion: "Start by running `/define-product` to create product definition from initial docs"

2. **Product Defined Phase**:
   - Indicator: `{{PRODUCT_MD}}` exists, but `{{FEATURES}}/` is empty
   - Suggestion: "Run `/add-mvp-features` to create feature definitions from product.md"

3. **Features Defined Phase**:
   - Indicator: Feature folders exist, but no `plan.md` files
   - Suggestion: "Run `/plan-feature [feature-id]` to create implementation plan"

4. **Planning Complete Phase**:
   - Indicator: `plan.md` exists, but no feature branch
   - Suggestion: "Run `/implement-feature [feature-id]` to start implementation"

5. **Implementation Phase**:
   - Indicator: Feature branch exists with code changes
   - Suggestion: "Run `/feature-review [feature-id]` when implementation is complete"

### Workflow Validation

Before executing commands, validate prerequisites:

**For `/add-feature` or `/add-mvp-features`:**
- Verify `{{PRODUCT_MD}}` exists
- If missing: "❌ Product definition required. Run `/define-product` first"

**For `/plan-feature`:**
- Verify feature's `feature.md` exists
- Verify `{{ARCHITECTURE}}` exists (warn if missing)
- If missing: "❌ Feature definition required. Run `/add-feature [id]` first"

**For `/implement-feature`:**
- Verify feature's `feature.md` and `plan.md` exist
- Verify acceptance criteria are defined
- If missing: "❌ Implementation plan required. Run `/plan-feature [id]` first"

## Architecture Principles

### General Development Rules

- **KISS Principle**: Keep implementations simple and straightforward
- **DRY Principle**: Don't repeat yourself - extract common patterns
- **SOLID Principles**: Follow object-oriented design principles
- **YAGNI Principle**: You aren't gonna need it - avoid artificial complexity
- **Immutability**: Prefer immutable data structures
- **Latest Versions**: Use latest stable versions of all dependencies
- **Monorepo Structure**: Use monorepo with component folders (backend/, mobile/, web/)

### Default Architecture Pattern

**Simplified Layered Architecture**:
- Service → Store → Database
- Group by feature in directory structure, not by layer
- Services exposed via REST by default
- DTOs only when data shapes differ from entities
- Stores (repositories) as annotated interfaces to minimize boilerplate
- Prepare code for containerization and cloud deployment (GCP Cloud Run)

### Documentation Standards

Consider updating documentation after significant changes:

- `README.md` - Project overview, quick start, components, commands
- `CHANGELOG.md` - User-facing changes (new features, bug fixes)
- `{{ADR}}/` - Architecture Decision Records for major technical decisions
  - Record: Date, Decision, Motivation
  - When: Pattern applied, design changes, tech stack changes, DB schema changes

### Feature Specification Requirements

Every feature specification should indicate:
- What components it affects
- Integration points
- Dependencies on other features

## Instructions

When this skill is active:

1. **Read Configuration**: Always start by reading `.claude/lib/config.md` to understand current path mappings

2. **Resolve Paths**: When commands or agents reference logical paths like `{{PRODUCT_ROOT}}`, substitute with actual configured values

3. **Validate Prerequisites**: Before executing workflow commands, verify required files/directories exist

4. **Provide Workflow Guidance**:
   - Detect current phase
   - Suggest logical next step
   - Explain what each command does and when to use it

5. **Apply Architecture Principles**: Ensure all development work follows the architecture principles defined above

6. **Maintain Documentation**: Remind about documentation updates when significant changes are made

## Available Commands

Inform users of these workflow commands when relevant:

- `/define-product [name]` - Create comprehensive product definition from initial docs
- `/define-architecture` - Define technical architecture and standards
- `/add-feature [id]` - Define a specific feature with requirements
- `/add-mvp-features` - Create all MVP features from product.md
- `/update-feature [id]` - Sync feature definition with changes
- `/mockup-product` - Generate product-level UI mockups
- `/mockup-feature [id]` - Generate feature-specific mockups
- `/figma-mockup <url>` - Generate mockup from Figma design
- `/plan-feature [id]` - Create detailed implementation plan
- `/implement-feature [id]` - Implement feature following plan
- `/feature-review [id]` - Comprehensive code review

## Integration with Other Skills

This core skill works alongside specialized domain skills:

- `business-analysis` - Activated during product/feature definition
- `ui-ux-design` - Activated during mockup generation
- `lean-startup` - Activated during early discovery phase
- `product-research` - Activated when analyzing user feedback
- Tech stack skills - Activated based on detected technology (Kotlin, React, etc.)

Coordinate with these skills but don't duplicate their domain expertise.
