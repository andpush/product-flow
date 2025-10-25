# SAST Tool Configuration Guide

This document provides installation and configuration guidance for the SAST tools used in this skill.

## Required Tools

### Semgrep (Required)

**Description:** Multi-language static analysis tool with extensive rule library.

**Installation:**

```bash
# macOS
brew install semgrep

# Linux/macOS with pip
pip install semgrep

# Using pipx (recommended)
pipx install semgrep
```

**Verification:**
```bash
semgrep --version
```

**Configuration:**

Create `.semgrep.yml` in your project root to customize rules:

```yaml
rules:
  - id: custom-sql-injection
    patterns:
      - pattern: execute($QUERY)
      - pattern-not: execute("...")
    message: Possible SQL injection
    severity: ERROR
    languages: [python]
```

**Usage:**
```bash
# Scan with auto config (recommended)
semgrep scan --config=auto .

# Scan with specific ruleset
semgrep scan --config=p/security-audit .

# Scan and output JSON
semgrep scan --config=auto --json --output=results.json .
```

---

## Optional Language-Specific Tools

### Bandit (Python)

**Description:** Security linter for Python code.

**Installation:**

```bash
pip install bandit
```

**Verification:**
```bash
bandit --version
```

**Configuration:**

Create `.bandit` or `bandit.yaml` in your project:

```yaml
exclude_dirs:
  - /test
  - /tests
  - /venv
  - /.venv

tests:
  - B201  # Flask debug mode
  - B301  # Pickle usage
  - B501  # SSL/TLS issues

skips:
  - B404  # Import of subprocess (too noisy)
```

**Usage:**
```bash
# Scan recursively
bandit -r . -f json -o bandit-results.json
```

---

### npm audit (Node.js/JavaScript)

**Description:** Built-in Node.js dependency vulnerability scanner.

**Installation:**
- Comes with npm (no separate installation needed)

**Verification:**
```bash
npm --version
```

**Configuration:**

Create `.npmrc` to configure:

```
audit-level=moderate
```

**Usage:**
```bash
# Run audit and get JSON output
npm audit --json > npm-audit-results.json

# For yarn projects
yarn audit --json > yarn-audit-results.json
```

---

### Trivy (Dependencies & Containers)

**Description:** Comprehensive vulnerability scanner for containers and dependencies.

**Installation:**

```bash
# macOS
brew install trivy

# Linux
curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin

# Using Docker
docker pull aquasec/trivy
```

**Verification:**
```bash
trivy --version
```

**Configuration:**

Create `trivy.yaml`:

```yaml
severity:
  - CRITICAL
  - HIGH
  - MEDIUM
  - LOW

vulnerability:
  type:
    - os
    - library

scan:
  skip-dirs:
    - node_modules
    - venv
```

**Usage:**
```bash
# Scan filesystem
trivy fs --format json --output trivy-results.json .

# Scan container image
trivy image --format json myimage:tag

# Scan specific languages only
trivy fs --scanners vuln --security-checks vuln .
```

---

## Tool Comparison Matrix

| Tool | Languages | Strengths | Limitations |
|------|-----------|-----------|-------------|
| **Semgrep** | 30+ languages | Fast, customizable rules, low false positives | Rule-based only (no data flow) |
| **Bandit** | Python only | Python-specific, detailed findings | Single language |
| **npm audit** | JavaScript/Node.js | Dependency vulnerabilities, built-in | Dependencies only, no code analysis |
| **Trivy** | Multiple (via deps) | Container & dependency scanning, comprehensive | Primarily dependency-focused |

---

## Recommended Tool Combinations

### Python Project
```bash
semgrep scan --config=auto .
bandit -r . -f json -o bandit.json
trivy fs --format json .
```

### Node.js Project
```bash
semgrep scan --config=auto .
npm audit --json > npm-audit.json
trivy fs --format json .
```

### Full Stack Project
```bash
semgrep scan --config=auto .
bandit -r backend/ -f json -o bandit.json
npm audit --prefix frontend/ --json > npm-audit.json
trivy fs --format json .
```

---

## CI/CD Integration

### GitHub Actions

```yaml
name: Security Scan

on: [push, pull_request]

jobs:
  security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run Semgrep
        uses: returntocorp/semgrep-action@v1
        with:
          config: auto

      - name: Run Trivy
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          format: 'sarif'
          output: 'trivy-results.sarif'
```

### GitLab CI

```yaml
security_scan:
  stage: test
  image: returntocorp/semgrep
  script:
    - semgrep scan --config=auto --json --output=semgrep.json .
  artifacts:
    reports:
      sast: semgrep.json
```

---

## Performance Optimization

### For Large Codebases

1. **Exclude directories:**
```bash
semgrep scan --config=auto --exclude='node_modules' --exclude='venv' .
```

2. **Scan incrementally:**
```bash
# Only scan changed files
git diff --name-only main... | xargs semgrep scan --config=auto
```

3. **Use parallel scanning:**
```bash
semgrep scan --config=auto --jobs=4 .
```

4. **Cache results:**
```bash
# Trivy uses cache by default
trivy fs --cache-dir=/tmp/trivy-cache .
```

---

## Troubleshooting

### Semgrep Issues

**Problem:** Too many false positives
**Solution:** Use `--exclude` or create `.semgrepignore` file

**Problem:** Slow scans
**Solution:** Use `--exclude` for large directories, increase `--jobs`

### Bandit Issues

**Problem:** Too noisy
**Solution:** Configure `.bandit` to skip specific tests

**Problem:** Missing vulnerabilities
**Solution:** Ensure all tests are enabled in configuration

### npm audit Issues

**Problem:** Too many low-severity warnings
**Solution:** Set `audit-level=high` in `.npmrc`

**Problem:** Unfixable vulnerabilities
**Solution:** Use `npm audit fix` or update dependencies manually

### Trivy Issues

**Problem:** Slow first scan
**Solution:** Normal - Trivy downloads vulnerability database on first run

**Problem:** Network errors
**Solution:** Use `--offline` mode with pre-downloaded DB

---

## Version Compatibility

Minimum recommended versions:
- Semgrep: >= 1.45.0
- Bandit: >= 1.7.5
- npm: >= 8.0.0
- Trivy: >= 0.48.0

Check for updates regularly:
```bash
# Semgrep
semgrep --version

# Bandit
bandit --version

# npm
npm --version

# Trivy
trivy --version
```

---

## Additional Resources

- [Semgrep Documentation](https://semgrep.dev/docs/)
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [npm audit Documentation](https://docs.npmjs.com/cli/v8/commands/npm-audit)
- [Trivy Documentation](https://aquasecurity.github.io/trivy/)
