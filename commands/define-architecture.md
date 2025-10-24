---
description: Define technical architecture, development standards based on product requirements
allowed-tools: Read, Write, Bash, Glob
---
# Command Instructions

You are a Senior Software Architect with extensive experience in system design.
Create a well-thought-out architecture and technical documentation based on the product requirements.

## Context

First, verify that `product/product.md` exists. If not, user should run `/define-product` first to define the product.

**Required Reading:**

- Read `product/product.md` - Product definition, requirements and constraints
- Read documents referenced in the Bibliography section to get even more context
- Read `product/architecture.md` (if exists) - Existing architectural decisions (that may need updating)
- Read `CLAUDE.md`, `AGENTS.md`(if exists) - Development preferences and standards

**Architecture Template Structure:**

When creating `product/architecture.md`, include these sections:

- Executive Summary (2-3 sentences on technical approach)
- System Architecture with diagrams (mermaid format): High-Level Design, Sequence, Data Flow, Component Overview
- Technology Stack Decisions (Frontend, Backend, Data Layer, Caching, Infrastructure)
- Development Standards (Code Organization, Coding Conventions, Testing Strategy, API Design)
- Security Requirements (Authentication, Data Protection, Security Checklist)
- Performance Requirements (Response Time Targets, Scalability, Optimization)
- Deployment & Operations (Environments, Process, Monitoring)
- Open Technical Questions

## Task

1. **Analyze Requirements**: Understand functional and non-functional needs from product definition
2. **Architectural Approaches**: Think hard about possible architectures and design choices including:
    - architectural styles (monolyth vs. microservices)
    - components decomposition and layers
    - frameworks and libraries
    - programming languages
    - databases and data model
    - integrations and dependencies
    - API design (e.g. REST vs GraphQL)
    - authentication and security
    - communication protocols
    - infrastructure and deployment options
    - caching and other means to meet performance and scalability reruiements
3. **Think Alternatives**: There are many ways that lead to the expected result. Consider ready-made products to be used instead of developing all functionality from ground up.
4. **Compare and Propose**:
    - Choose appropriate patterns, technologies, and system structure to propose to the user
    - Consider complexity, labor, costs. Give preference to simple proven solutions.
    - Think on concise presentition of benefits and trade-offs to provide user with sufficient context to take decision.
5. **Ask and Document**:
    - Involve user to make final decision when unsure. Example:

    ```example
    Decision: [Technology/pattern to choose]

    1. [Recommended option]: [Benefits] | Trade-offs: [Limitations]
    2. [Alternative]: [Benefits] | Trade-offs: [Limitations]
    ...
    A. Another approach (invite user to specify their own decision)
    E. Explain more the implications
    P. Postpone (TBD later, e.g. during implementation)
    ```

    - Document the question and the decision
    - Provide clear rationale for major technical choices, including options and their trade-offs

6. **Define Standards**:
   - coding conventions and best practices adequate to the chosen programming language
   - definition of done
   - testing approaches
   - development workflow: Git strategy, CI/CD, review process, testing approach

7. **Create/Update**: Generate or enhance `product/architecture.md` following the Architecture Template Structure defined above
