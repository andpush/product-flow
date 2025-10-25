---
name: codebase-explorer
description: This skill should be used when exploring unfamiliar codebases, analyzing large repositories, understanding legacy systems, or performing comprehensive code audits. Use this for tech stack detection, architecture mapping, quality assessment, or preparing for refactoring, onboarding, and security reviews.
---

# Codebase Explorer

## Overview

Systematically explore and document codebases at three levels of depth: Quick Scan (tech stack and structure), Deep Analysis (architecture and patterns), and Comprehensive Audit (full quality, security, and performance assessment). Each level builds on the previous, providing progressively detailed insights.

## Exploration Levels

Choose the appropriate exploration depth based on the task:

- **Level 1: Quick Scan** - Initial understanding, tech stack detection (5-10 minutes)
- **Level 2: Deep Analysis** - Architecture mapping, pattern recognition (20-30 minutes)
- **Level 3: Comprehensive Audit** - Full quality, security, and performance review (1-2 hours)

## Level 1: Quick Scan

**Use when**: First encounter with codebase, need rapid tech stack identification, routing to specialists.

### Workflow

1. **Survey Directory Structure**
   - List top-level directories and identify organization patterns
   - Look for conventional layouts (src/, lib/, tests/, docs/)
   - Note any unusual or domain-specific organization

2. **Detect Tech Stack**
   - Scan for package managers and dependency files:
     - `package.json`, `package-lock.json` (Node.js/npm)
     - `requirements.txt`, `Pipfile`, `pyproject.toml` (Python)
     - `composer.json` (PHP)
     - `Gemfile` (Ruby)
     - `go.mod` (Go)
     - `pom.xml`, `build.gradle`, `build.gradle.kts` (Java/Kotlin)
     - `Cargo.toml` (Rust)
     - `pubspec.yaml` (Flutter/Dart)
   - Read dependency files to identify frameworks and libraries
   - Check for build tools and task runners

3. **Identify Entry Points**
   - Locate main application entry points (main.py, index.js, app.py, server.go)
   - Find configuration files (config/, .env.example, settings.py)
   - Discover API routes, CLI commands, or UI entry points

4. **Pattern Recognition**
   - Detect architectural patterns (MVC, microservices, monorepo)
   - Identify design patterns in use
   - Note framework-specific conventions

### Output Format

```markdown
## Quick Scan Report: <project-name>

### Tech Stack
- **Primary Language**: [language + version]
- **Framework**: [framework + version] (Confidence: High/Medium/Low)
- **Package Manager**: [tool]
- **Build Tools**: [list]
- **Key Dependencies**: [top 5-10 critical libraries]

### Project Structure
- **Architecture Pattern**: [MVC/Microservices/Monorepo/etc.]
- **Confidence**: [High/Medium/Low]
- **Entry Points**: [list with file paths]
- **Configuration**: [config file locations]

### Specialist Recommendations
Based on detected stack, recommend:
- [framework-specific-specialist] for backend work
- [frontend-specialist] for UI components
- [language-specialist] for core logic

### Key Findings
- [3-5 bullet points of notable observations]

### Uncertainties
- [Areas requiring clarification or deeper investigation]
```

Use `references/tech-stack-patterns.md` for common framework detection patterns and confidence scoring criteria.

## Level 2: Deep Analysis

**Use when**: Planning new features, understanding existing features, preparing for refactoring, onboarding new developers.

### Workflow

1. **Architecture Mapping**
   - Trace data flow from entry points through layers
   - Map abstraction layers (presentation → business logic → data)
   - Document component boundaries and interfaces
   - Identify cross-cutting concerns (auth, logging, caching, error handling)

2. **Feature Discovery and Tracing**
   - Select 2-3 representative features to trace comprehensively
   - Follow execution paths from entry to completion
   - Document state changes and side effects
   - Note integration points with external systems

3. **Pattern Analysis**
   - Identify design patterns in use (Factory, Repository, Strategy, etc.)
   - Document coding conventions and style
   - Note architectural decisions and trade-offs
   - Recognize code smells or anti-patterns

4. **Dependency Analysis**
   - Map internal module dependencies
   - Identify tightly coupled components
   - Note circular dependencies
   - Document external integrations

### Exploration Strategy

**Parallel exploration**: When analyzing complex systems, explore multiple aspects simultaneously:

- **Aspect 1**: Trace a specific feature end-to-end
- **Aspect 2**: Map high-level architecture and abstractions
- **Aspect 3**: Analyze similar features for patterns
- **Aspect 4**: Examine testing approaches and quality standards

### Output Format

```markdown
## Deep Analysis Report: <project-name>

### Architecture Overview
[Mermaid diagram or ASCII art showing main components and data flow]

| Component | Purpose | Key Files | Dependencies |
|-----------|---------|-----------|--------------|
| ...       | ...     | ...       | ...          |

### Feature Tracing: [Feature Name]
**Entry Point**: `file.ext:line`
**Flow**:
1. [Step] in `file:line` - [what happens, data transformation]
2. [Step] in `file:line` - [what happens, data transformation]
...

**Key Components**:
- `ComponentName` (`file:line`) - [responsibility]
- `ServiceName` (`file:line`) - [responsibility]

**Dependencies**: [list internal and external dependencies]

### Patterns & Conventions
- **Design Patterns**: [list with examples]
- **Coding Conventions**: [style, naming, organization]
- **Architectural Decisions**: [key choices and rationale]

### Code Quality Observations
- **Strengths**: [3-5 positive aspects]
- **Issues**: [3-5 concerns or improvement areas]
- **Technical Debt**: [notable areas]

### Essential Files
[List 10-15 absolutely essential files to understand this area]
- `file1:line` - [why essential]
- `file2:line` - [why essential]
```

Use `references/exploration-checklist.md` for comprehensive analysis guidelines.

## Level 3: Comprehensive Audit

**Use when**: Pre-refactoring assessment, security review, performance optimization, technical debt analysis, onboarding documentation.

### Workflow

1. **Quality Metrics Collection**
   - Run `scripts/analyze_codebase.py` to collect:
     - Lines of code (excluding generated/vendor code)
     - Cyclomatic complexity (avg and worst offenders)
     - Test coverage percentage
     - Code duplication metrics
   - Identify high-complexity files and functions
   - Locate untested or under-tested areas

2. **Security Assessment**
   - Scan for hardcoded secrets (API keys, passwords, tokens)
   - Check authentication and authorization patterns
   - Identify SQL injection, XSS, CSRF vulnerabilities
   - Review dependency versions for known CVEs
   - Examine error handling and information disclosure

3. **Performance Analysis**
   - Identify algorithmic bottlenecks (N+1 queries, nested loops)
   - Look for inefficient data structures
   - Check for excessive memory usage
   - Note synchronous operations that could be async
   - Examine caching strategy

4. **Dependency Health**
   - Check for outdated dependencies
   - Identify deprecated packages
   - Note license incompatibilities
   - Assess maintenance status of critical dependencies
   - Use `scripts/generate_dependency_graph.py` to visualize relationships

5. **Comprehensive Synthesis**
   - Calculate overall health score (0-10)
   - Prioritize findings by severity
   - Create actionable recommendations
   - Suggest specialist delegation for issues

### Output Format

```markdown
## Comprehensive Audit Report: <project-name>
**Date**: <YYYY-MM-DD>
**Commit**: <hash>

### Executive Summary
- **Purpose**: [1-2 sentence project description]
- **Tech Stack**: [complete stack]
- **Architecture Style**: [pattern]
- **Health Score**: [0-10] - [explanation]
- **Top 3 Risks**:
  1. [Critical risk with impact]
  2. [Major risk with impact]
  3. [Important risk with impact]

### Architecture Overview
[Detailed diagram with component interactions]

| Component | Purpose | Key Files | Direct Dependencies | Health |
|-----------|---------|-----------|---------------------|--------|
| ...       | ...     | ...       | ...                 | ✓/⚠/✗  |

### Data & Control Flow
[Narrative description with sequence diagrams for critical paths]

### Dependency Analysis
**Third-Party Libraries**:
| Library | Version | Latest | Status | Risk |
|---------|---------|--------|--------|------|
| ...     | ...     | ...    | ✓/⚠/✗  | ...  |

**Internal Module Dependencies**:
- [Module dependency graph summary]
- **Circular Dependencies**: [list if any]
- **Tight Coupling**: [problematic areas]

### Quality Metrics
| Metric | Value | Target | Status | Notes |
|--------|-------|--------|--------|-------|
| Lines of Code | [X] | - | ℹ | [generated vs handwritten] |
| Test Coverage | [X]% | >80% | ✓/⚠/✗ | Missing: [areas] |
| Avg Complexity | [X] | <10 | ✓/⚠/✗ | Worst: `file:line` (complexity [Y]) |
| Code Duplication | [X]% | <5% | ✓/⚠/✗ | Hotspots: [files] |
| TODO/FIXME Count | [X] | - | ℹ | [distribution] |

### Security Assessment
| Issue | Location | Severity | Impact | Recommendation |
|-------|----------|----------|--------|----------------|
| Hardcoded API key | `config.py:42` | Critical | Data breach | Use environment variables + secrets manager |
| Missing CSRF protection | `views.py:*` | High | Request forgery | Enable Django CSRF middleware |
| SQL injection risk | `queries.py:78` | High | Data loss | Use parameterized queries |
| ...   | ...      | ...      | ...    | ...            |

**Overall Security Score**: [0-10] - [explanation]

### Performance Assessment
| Bottleneck | Evidence | Impact | Suggested Fix | Priority |
|------------|----------|--------|---------------|----------|
| N+1 queries in user list | `views.py:156` | 2000+ DB queries per page | Use select_related/prefetch_related | P0 |
| Synchronous API calls | `service.py:89` | 5s page load | Convert to async or background job | P1 |
| ...        | ...      | ...    | ...           | ...      |

**Performance Score**: [0-10] - [explanation]

### Technical Debt & Code Smells
**High-Priority Debt**:
- [Description] in `file:line` - [impact] - **Estimated effort**: [hours/days]
- [Description] in `file:line` - [impact] - **Estimated effort**: [hours/days]

**Code Smells**:
- **God Objects**: [list with file references]
- **Duplicated Code**: [specific examples]
- **Dead Code**: [unused files/functions]
- **Magic Numbers**: [hardcoded values needing constants]

### Recommended Actions (Prioritized)
| Priority | Action | Category | Owner | Effort | Impact |
|----------|--------|----------|-------|--------|--------|
| P0 | Rotate exposed API keys | Security | security-specialist | 2h | Critical |
| P0 | Fix SQL injection in search | Security | security-specialist | 4h | Critical |
| P1 | Enable CSRF protection | Security | backend-specialist | 2h | High |
| P1 | Optimize N+1 queries | Performance | performance-optimizer | 1d | High |
| P2 | Add tests for auth module | Quality | testing-specialist | 3d | Medium |
| P2 | Update Django to latest LTS | Maintenance | backend-specialist | 1d | Medium |
| ...  | ...    | ...      | ...   | ...    | ...    |

### Open Questions / Unknowns
- [Question requiring clarification from maintainers]
- [Unclear architectural decision or missing documentation]
- [Ambiguous requirements or edge cases]

### Appendix
**Methodology**: [Tools used, analysis approach]
**Scope**: [What was analyzed, what was excluded]
**Limitations**: [Known gaps in analysis]
```

Run `scripts/analyze_codebase.py` before generating this report to collect objective metrics.

## Adaptive Exploration

Adjust depth based on codebase characteristics:

**Small codebases (<1000 LOC)**: Start at Level 2, skip Level 1
**Microservices**: Run Level 1 on each service, Level 2 on critical services
**Monorepos**: Level 1 on whole repo, Level 2 on specific packages
**Legacy systems**: Full Level 3 audit recommended

## Integration with Other Skills

After exploration, delegate to specialists:

- **Security issues** → security auditor skill
- **Performance bottlenecks** → performance optimization skill
- **Documentation gaps** → documentation generator skill
- **Testing gaps** → test generation skill
- **Refactoring needs** → code refactoring skill

## Resources

### scripts/analyze_codebase.py
Automated metrics collection: LOC count, complexity analysis, test coverage calculation, dependency freshness checks.

**Usage**:
```bash
python scripts/analyze_codebase.py /path/to/codebase --output metrics.json
```

### scripts/generate_dependency_graph.py
Visualize internal module dependencies and external package relationships.

**Usage**:
```bash
python scripts/generate_dependency_graph.py /path/to/codebase --format mermaid
```

### references/tech-stack-patterns.md
Comprehensive patterns for detecting frameworks, architectures, and technologies with confidence scoring criteria.

### references/exploration-checklist.md
Detailed checklists for each exploration level, ensuring comprehensive coverage of all relevant aspects.
