# Codebase Exploration Checklists

## Level 1: Quick Scan Checklist

### Directory Structure Survey
- [ ] List all top-level directories
- [ ] Identify src/, lib/, app/, or similar source directories
- [ ] Locate tests/, test/, __tests__, or spec/ directories
- [ ] Find docs/, documentation/ directories
- [ ] Note config/, settings/, or environment directories
- [ ] Check for scripts/, bin/, or tools/ directories
- [ ] Identify public/, static/, assets/ directories (frontend)
- [ ] Look for unusual or domain-specific directory names

### Tech Stack Detection
- [ ] Scan for package manager files in root:
  - [ ] package.json (Node.js)
  - [ ] requirements.txt, Pipfile, pyproject.toml (Python)
  - [ ] composer.json (PHP)
  - [ ] Gemfile (Ruby)
  - [ ] go.mod (Go)
  - [ ] pom.xml, build.gradle, build.gradle.kts (Java)
  - [ ] Cargo.toml (Rust)
  - [ ] Package.swift (Swift)
  - [ ] pubspec.yaml (Flutter/Dart)
- [ ] Read and parse primary dependency file
- [ ] Identify framework (if any) with confidence level
- [ ] List top 5-10 critical dependencies
- [ ] Note package manager version (lock files)
- [ ] Check for multiple language usage (polyglot repo)

### Build Tool Identification
- [ ] webpack.config.js, vite.config.js, rollup.config.js
- [ ] tsconfig.json, jsconfig.json
- [ ] babel.config.js, .babelrc
- [ ] Makefile, Rakefile, Gruntfile, Gulpfile
- [ ] Dockerfile, docker-compose.yml
- [ ] CI/CD configs (.github/workflows/, .gitlab-ci.yml, etc.)

### Entry Points Discovery
- [ ] Locate main application file:
  - [ ] index.js, server.js, app.js, main.js (Node)
  - [ ] main.py, app.py, wsgi.py, manage.py (Python)
  - [ ] index.php, public/index.php (PHP)
  - [ ] main.go (Go)
  - [ ] Main.java, Application.java (Java)
  - [ ] lib/main.dart (Flutter/Dart)
  - [ ] Main.kt, Application.kt (Kotlin)
- [ ] Find configuration files:
  - [ ] .env.example, config.example
  - [ ] settings.py, config.js, application.yml
  - [ ] Database configuration files
  - [ ] pubspec.yaml (Flutter/Dart)
  - [ ] build.gradle.kts, build.gradle (Kotlin/Java)
- [ ] Identify API routes/endpoints (if backend)
- [ ] Locate CLI command definitions (if applicable)
- [ ] Find UI entry points (if frontend)

### Architecture Pattern Recognition
- [ ] Detect MVC pattern (models/, views/, controllers/)
- [ ] Identify microservices (multiple service directories)
- [ ] Recognize monorepo (nx.json, turbo.json, workspaces)
- [ ] Check for layered architecture (api/, services/, data/)
- [ ] Look for event-driven patterns (events/, handlers/)
- [ ] Note DDD structure (domain/, application/, infrastructure/)

### Quick Quality Checks
- [ ] Check if README exists and is informative
- [ ] Look for LICENSE file
- [ ] Note presence of CONTRIBUTING.md
- [ ] Check for .gitignore appropriateness
- [ ] Scan for .env or secrets in version control (RED FLAG)
- [ ] Verify test directory exists

### Output Preparation
- [ ] Document primary language with confidence
- [ ] List detected framework with confidence
- [ ] Note architecture pattern with confidence
- [ ] List 3-5 key findings
- [ ] Document uncertainties requiring deeper investigation
- [ ] Recommend specialists based on stack

---

## Level 2: Deep Analysis Checklist

### Architecture Mapping
- [ ] Identify all major components/modules
- [ ] Map data flow from entry points:
  - [ ] Request handling (routes → controllers/views)
  - [ ] Business logic layer (services, use cases)
  - [ ] Data access layer (repositories, models, ORM)
  - [ ] Response generation
- [ ] Document abstraction layers clearly
- [ ] Identify component boundaries and interfaces
- [ ] Map cross-cutting concerns:
  - [ ] Authentication/Authorization
  - [ ] Logging and monitoring
  - [ ] Error handling
  - [ ] Caching strategy
  - [ ] Validation
  - [ ] Rate limiting

### Feature Tracing (Select 2-3 Features)
For each feature:
- [ ] Identify entry point (file:line)
- [ ] Trace execution path step-by-step
- [ ] Document data transformations at each step
- [ ] Note state changes and side effects
- [ ] List all functions/methods called
- [ ] Identify database queries or external API calls
- [ ] Document error handling approach
- [ ] Note integration points with other features
- [ ] List all files involved

### Pattern Analysis
- [ ] Identify design patterns in use:
  - [ ] Factory pattern
  - [ ] Repository pattern
  - [ ] Strategy pattern
  - [ ] Observer pattern
  - [ ] Singleton pattern (note if overused)
  - [ ] Dependency Injection
  - [ ] Others (list)
- [ ] Document coding conventions:
  - [ ] Naming conventions (camelCase, snake_case, etc.)
  - [ ] File organization patterns
  - [ ] Import/require organization
  - [ ] Comment style
  - [ ] Error handling patterns
- [ ] Note architectural decisions and trade-offs
- [ ] Identify code smells:
  - [ ] God objects/classes
  - [ ] Tight coupling
  - [ ] Code duplication
  - [ ] Magic numbers/strings
  - [ ] Long parameter lists
  - [ ] Long methods/functions

### Dependency Analysis
- [ ] Map internal module dependencies
- [ ] Create dependency graph (mental or visual)
- [ ] Identify circular dependencies (PROBLEM)
- [ ] Note tightly coupled components
- [ ] Document external service integrations:
  - [ ] Third-party APIs
  - [ ] Message queues
  - [ ] Cache services
  - [ ] Search engines
  - [ ] File storage services
- [ ] List all database interactions

### Testing Approach Analysis
- [ ] Identify testing framework(s)
- [ ] Understand test organization:
  - [ ] Unit tests location and coverage
  - [ ] Integration tests
  - [ ] End-to-end tests
  - [ ] Performance tests
- [ ] Note testing patterns (mocking, fixtures, factories)
- [ ] Check for test utilities and helpers
- [ ] Assess test quality (brittle vs robust)

### Code Quality Observations
- [ ] Document strengths (3-5 items):
  - [ ] Well-structured code
  - [ ] Good separation of concerns
  - [ ] Comprehensive tests
  - [ ] Clear naming
  - [ ] Good documentation
  - [ ] Others
- [ ] Document issues (3-5 items):
  - [ ] Areas of complexity
  - [ ] Missing tests
  - [ ] Poor error handling
  - [ ] Unclear naming
  - [ ] Lack of documentation
  - [ ] Others
- [ ] Note technical debt areas
- [ ] Identify improvement opportunities

### Essential Files Identification
- [ ] List 10-15 absolutely essential files with reasons:
  - [ ] Main entry points
  - [ ] Core business logic files
  - [ ] Critical configuration files
  - [ ] Key model/schema definitions
  - [ ] Important service/controller files
  - [ ] Central utility/helper files
  - [ ] Test examples

### Output Preparation
- [ ] Create architecture diagram (Mermaid or ASCII)
- [ ] Document component table with purposes
- [ ] Detail feature traces with file:line references
- [ ] List patterns and conventions discovered
- [ ] Summarize quality observations
- [ ] Provide essential files list

---

## Level 3: Comprehensive Audit Checklist

### Quality Metrics Collection
- [ ] Calculate lines of code:
  - [ ] Total LOC
  - [ ] Source code only (exclude generated/vendor)
  - [ ] Comments vs code ratio
  - [ ] Breakdown by language/module
- [ ] Measure cyclomatic complexity:
  - [ ] Average complexity per file
  - [ ] Average complexity per function
  - [ ] Identify worst offenders (>15 complexity)
  - [ ] Calculate percentage of high-complexity code
- [ ] Assess test coverage:
  - [ ] Overall coverage percentage
  - [ ] Coverage by module/package
  - [ ] Identify untested critical paths
  - [ ] Note missing test types (unit/integration/e2e)
- [ ] Detect code duplication:
  - [ ] Percentage of duplicated code
  - [ ] Identify duplication hotspots
  - [ ] Note copy-paste programming instances
- [ ] Count TODO/FIXME comments:
  - [ ] Total count
  - [ ] Distribution by severity/type
  - [ ] Age of oldest TODOs

### Security Assessment
- [ ] Scan for hardcoded secrets:
  - [ ] API keys
  - [ ] Passwords
  - [ ] Tokens
  - [ ] Private keys
  - [ ] Database credentials
- [ ] Review authentication:
  - [ ] Authentication mechanism (JWT, sessions, OAuth)
  - [ ] Password storage (hashing, salting)
  - [ ] Session management
  - [ ] Token expiration and rotation
- [ ] Review authorization:
  - [ ] Access control implementation
  - [ ] Role-based or permission-based
  - [ ] Privilege escalation risks
  - [ ] Resource ownership checks
- [ ] Check for common vulnerabilities:
  - [ ] SQL injection risks (check for raw queries)
  - [ ] XSS vulnerabilities (input sanitization)
  - [ ] CSRF protection enabled
  - [ ] Path traversal risks
  - [ ] Command injection risks
  - [ ] Insecure deserialization
- [ ] Review dependency security:
  - [ ] Check for known CVEs in dependencies
  - [ ] Note outdated packages with security issues
  - [ ] Assess dependency freshness
- [ ] Examine error handling:
  - [ ] Sensitive information in error messages
  - [ ] Stack traces exposed to users
  - [ ] Proper error logging
- [ ] Check HTTPS/TLS usage:
  - [ ] Enforce HTTPS
  - [ ] Certificate validation
  - [ ] Secure cookie flags
- [ ] Review input validation:
  - [ ] User input validation
  - [ ] Type checking
  - [ ] Boundary validation
  - [ ] Whitelist vs blacklist approach

### Performance Analysis
- [ ] Identify algorithmic bottlenecks:
  - [ ] N+1 query problems
  - [ ] Nested loops with high complexity
  - [ ] Inefficient sorting/searching
  - [ ] Unbounded recursion
- [ ] Review data structures:
  - [ ] Appropriate data structure choices
  - [ ] Memory-efficient implementations
  - [ ] Lazy loading where applicable
- [ ] Check database performance:
  - [ ] Missing indexes
  - [ ] Inefficient queries
  - [ ] Lack of query optimization
  - [ ] Connection pooling
- [ ] Examine caching:
  - [ ] Caching strategy present
  - [ ] Cache invalidation logic
  - [ ] Cache hit/miss considerations
  - [ ] Appropriate cache TTLs
- [ ] Review asynchronous operations:
  - [ ] Blocking I/O operations
  - [ ] Opportunities for async/parallelization
  - [ ] Background job usage
  - [ ] Queue management
- [ ] Check for memory leaks:
  - [ ] Proper resource cleanup
  - [ ] Event listener removal
  - [ ] Connection closures
  - [ ] Large object retention

### Dependency Health Assessment
- [ ] Check dependency freshness:
  - [ ] List outdated dependencies
  - [ ] Note major version gaps
  - [ ] Identify breaking change risks
- [ ] Assess deprecated packages:
  - [ ] List deprecated dependencies
  - [ ] Find replacement recommendations
  - [ ] Estimate migration effort
- [ ] Review license compatibility:
  - [ ] List all dependency licenses
  - [ ] Identify incompatible licenses
  - [ ] Note GPL/copyleft risks
- [ ] Evaluate maintenance status:
  - [ ] Check last update dates
  - [ ] Note abandoned packages
  - [ ] Assess community activity
  - [ ] Look for active forks if needed
- [ ] Analyze dependency tree:
  - [ ] Identify deep dependency chains
  - [ ] Note duplicate dependencies (different versions)
  - [ ] Find opportunities for tree shaking

### Overall Health Scoring
- [ ] Calculate health score (0-10) considering:
  - [ ] Code quality (complexity, duplication, style)
  - [ ] Test coverage and quality
  - [ ] Security posture
  - [ ] Performance characteristics
  - [ ] Dependency health
  - [ ] Documentation quality
  - [ ] Maintainability
- [ ] Document scoring rationale
- [ ] Compare against industry standards

### Risk Identification
- [ ] Identify top 3 critical risks:
  - [ ] Security vulnerabilities
  - [ ] Performance bottlenecks
  - [ ] Scalability limitations
  - [ ] Data loss risks
  - [ ] Compliance issues
- [ ] Assess impact of each risk
- [ ] Estimate likelihood of occurrence

### Prioritized Recommendations
- [ ] Create prioritized action list:
  - [ ] P0 (Critical): Security fixes, data loss prevention
  - [ ] P1 (High): Major bugs, performance issues
  - [ ] P2 (Medium): Quality improvements, tech debt
  - [ ] P3 (Low): Nice-to-haves, optimizations
- [ ] For each action item include:
  - [ ] Description
  - [ ] Category (Security/Performance/Quality/Maintenance)
  - [ ] Recommended specialist/owner
  - [ ] Estimated effort
  - [ ] Expected impact
- [ ] Suggest delegation to specialists

### Documentation Review
- [ ] Assess README quality
- [ ] Check API documentation completeness
- [ ] Review inline code documentation
- [ ] Note missing architecture documentation
- [ ] Identify undocumented decisions

### Output Preparation
- [ ] Executive summary with health score and top 3 risks
- [ ] Architecture overview with detailed diagrams
- [ ] Complete dependency analysis table
- [ ] Quality metrics table with targets and status
- [ ] Security assessment with severity levels
- [ ] Performance assessment with priorities
- [ ] Technical debt summary
- [ ] Prioritized action items table
- [ ] Open questions for maintainers
- [ ] Appendix with methodology and limitations

---

## Cross-Level Common Tasks

### File Reading Strategy
- [ ] Start with README and top-level docs
- [ ] Read main entry point files
- [ ] Examine configuration files
- [ ] Review core business logic files
- [ ] Check test files for usage examples
- [ ] Read package/dependency manifests
- [ ] Scan for unusual or custom patterns

### Note-Taking Best Practices
- [ ] Use file:line references consistently
- [ ] Mark confidence levels (High/Medium/Low)
- [ ] Document assumptions and uncertainties
- [ ] Note questions for maintainers
- [ ] Track follow-up investigation areas
- [ ] Record surprising or unexpected findings

### Communication Guidelines
- [ ] Use clear, concise language
- [ ] Provide specific examples with locations
- [ ] Avoid jargon where possible
- [ ] Explain technical terms when needed
- [ ] Include context for recommendations
- [ ] Prioritize actionable insights
