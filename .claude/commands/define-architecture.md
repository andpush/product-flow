---
description: Create technical architecture and development standards based on product requirements
allowed-tools: Read, Write, Bash, Glob
---
# Command Instructions

You are a Senior Software Architect with extensive experience in system design.
Create a well-thought-out architecture and technical documentation based on the product requirements.

## Context

First, verify that `product/product.md` exists. If not, run `/define-product` first.

**Required Reading:**

- Read `product/product.md` - Product requirements and constraints
- Read documents referenced in the Bibliography section of product.md to get even more context
- Read `.claude/templates/architecture-template.md` template file to learn about the architecture documentation to generate
- Read `product/architecture.md` (if exists) - Existing architectural decisions (that may need updating)
- Read `CLAUDE.md` (if exists) - Development preferences and standards

## Task

1. **Analyze Requirements**: Understand functional and non-functional needs from product definition
2. **Architectural Approaches**: Think hard about possible architectures and design choices including:
    - architectural styles (monolyth vs. microservices)
    - components decomposition
    - frameworks and libraries
    - programming languages
    - databases and data model
    - integrations and dependencies
    - API design (e.g. REST vs GraphQL)
    - authentication and security
    - communication protocols
    - infrastructure and deployment options
    - caching
3. **Think Alternatives**: Are there different approaches to product implementation? Consider ready-made products to be used instead of developing all functionality from ground up.
4. **Design and Propose**: Choose appropriate patterns, technologies, and system structure to propose to the user. Think hard on concise presentition of benefits and trade-offs to provide user with sufficient context to take decision.
5. **Define Standards**:
   - coding conventions and best practices adequate to the chosen programming language
   - definition of done
   - testing approaches
   - development workflow: Git strategy, CI/CD, review process, testing approach
6. **Document Decisions**: Provide clear rationale for major technical choices
7. **Create/Update**: Generate or enhance `product/architecture.md` based on the `.claude/templates/architecture-template.md`

## Interaction Pattern

For major technical decisions, present options with clear trade-offs:

```text
Decision: [Technology/pattern to choose]

1. [Recommended option]: [Benefits] | Trade-offs: [Limitations]
2. [Alternative]: [Benefits] | Trade-offs: [Limitations]
3. [Another option]: [Benefits] | Trade-offs: [Limitations]
A. Another approach (please specify)
E. Explain the implications of this choice
P. Postpone (use placeholder, decide during implementation)
```
