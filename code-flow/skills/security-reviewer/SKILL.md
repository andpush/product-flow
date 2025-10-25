---
name: security-reviewer
description: |
  Perform comprehensive security audits using SAST tools (Semgrep, Bandit, npm audit, Trivy)
  combined with AI analysis. Generate structured vulnerability reports with severity ratings
  (CR/HI/ME/LO), file references, code snippets, impact analysis, and remediation guidance.
  Output format: ./security-issues-YYYY-MM-DD/{CR/HI/ME/LO}-NNN.md files plus summary.md.

  Use this skill when:
  - User requests a security audit, security review, or vulnerability scan
  - User asks to "check for security issues" or "find vulnerabilities"
  - Before production releases or after major feature additions
  - During security compliance audits or penetration test preparation
---

# Code Security Review Skill

## Overview

This skill conducts systematic security audits of codebases using industry-standard SAST (Static Application Security Testing) tools combined with Claude's contextual analysis. It detects vulnerabilities like SQL injection, XSS, hard-coded secrets, weak cryptography, and more, then generates professional vulnerability reports organized by severity.

**Key Features:**
- Multi-tool SAST scanning (Semgrep, Bandit, npm audit, Trivy)
- Automatic language/framework detection
- Deduplication of findings across tools
- AI-enhanced analysis with contextual fixes
- Structured markdown reports per vulnerability
- Summary statistics and prioritization

## When to Use This Skill

Invoke this skill when users request:
- "Perform a security audit on this codebase"
- "Run a security review and generate vulnerability reports"
- "Check this project for security issues"
- "Scan for vulnerabilities"
- "Security analysis of [project/file]"

**Appropriate contexts:**
- Before production releases
- After major feature additions
- During security compliance audits
- When onboarding legacy codebases
- As part of penetration test preparation

## Prerequisites

Before running security scans, verify tool availability:

**Required:**
- **Semgrep** (multi-language SAST tool)
  - Installation: `pip install semgrep` or `brew install semgrep`
  - Verification: `semgrep --version`

**Optional (language-specific):**
- **Bandit** (Python): `pip install bandit`
- **npm/yarn** (Node.js): Built-in with Node.js
- **Trivy** (dependencies): `brew install trivy` or download from GitHub

For detailed installation instructions, refer to `references/tool-configuration.md`.

## Security Audit Workflow

### Step 1: Understand the Request

When a user requests a security audit:
1. Confirm the target path (default: current directory)
2. Ask if there are specific concerns or areas to focus on
3. Clarify if this is for a specific environment (dev/staging/prod)

### Step 2: Run the Security Scan

Run the main orchestrator script:

```bash
cd ~/.claude/skills/security-reviewer/scripts
python3 run_security_scan.py /path/to/target/codebase
```

**Options:**
- `--output ./custom-output-dir` - Specify output directory
- `--project "Project Name"` - Set project name in reports

**What the script does:**
1. Detects languages and frameworks in the codebase
2. Runs applicable SAST tools (Semgrep always, others based on detection)
3. Parses JSON output from each tool
4. Normalizes severity levels to CR/HI/ME/LO
5. Deduplicates findings across tools
6. Generates individual vulnerability reports
7. Creates summary.md with statistics

**Expected output structure:**
```
security-issues-YYYY-MM-DD/
├── CR-001.md
├── CR-002.md
├── HI-001.md
├── HI-002.md
├── HI-003.md
├── ME-001.md
├── ...
└── summary.md
```

### Step 3: Review and Analyze Findings

As a **moderate analyzer**, your role is to:

1. **Read the generated reports** - Review all CR and HI findings first
2. **Validate in context** - Check if findings are true positives or false positives
3. **Assess real-world impact** - Consider the specific application context
4. **Enrich findings** - Add deeper analysis based on codebase understanding
5. **Generate specific fixes** - Provide code-specific remediation, not generic advice

**Analysis approach:**

For each critical/high finding:
- Read the vulnerable code file to understand context
- Check if there are compensating controls (e.g., input validation elsewhere)
- Assess exploitability in this specific application
- Look for related vulnerabilities in the same pattern
- Consider business logic and data sensitivity

**Use reference documentation:**
- `references/vulnerability-categories.md` - OWASP Top 10 and CWE mappings
- `references/severity-guidelines.md` - Severity classification criteria
- `references/remediation-patterns.md` - Fix patterns by vulnerability type

### Step 4: Present Findings to User

Structure your response:

1. **Executive Summary**
   - Total vulnerabilities found
   - Breakdown by severity
   - Overall risk assessment
   - Immediate action items

2. **Critical Findings** (if any)
   - List each CR finding with file:line references
   - Explain the security impact
   - Provide specific fix recommendations
   - Highlight if immediate action is needed

3. **High Priority Findings**
   - Summarize HI findings
   - Group by category if many
   - Suggest remediation timeline

4. **Report Location**
   - Point user to the generated reports directory
   - Explain the naming convention (CR-001.md, etc.)
   - Highlight summary.md for statistics

5. **Next Steps**
   - Prioritized action plan
   - Recommendations for process improvements
   - Suggestions for integrating SAST into CI/CD

### Step 5: Interactive Remediation (Optional)

If the user wants help fixing vulnerabilities:

1. **Prioritize** - Start with CR, then HI findings
2. **Read vulnerable code** - Use Read tool to examine context
3. **Propose fixes** - Provide specific code changes
4. **Explain rationale** - Why the fix addresses the vulnerability
5. **Consider side effects** - Ensure fix doesn't break functionality
6. **Offer to implement** - Use Edit tool if user approves

Refer to `references/remediation-patterns.md` for common fix patterns.

## Your Role as Moderate Analyzer

**What "moderate analyzer" means:**

✅ **Do:**
- Run SAST tools and parse results
- Read code context for each finding
- Validate if findings are exploitable in context
- Add specific remediation guidance
- Explain security implications clearly
- Filter obvious false positives
- Suggest related code to review

❌ **Don't:**
- Perform deep manual code review of entire codebase (unless requested)
- Attempt to find logic vulnerabilities not detected by tools
- Spend excessive time on low-severity findings
- Get overwhelmed by tool output - focus on CR/HI first

**Balance:** Use tools for breadth, use AI for depth on important findings.

## Understanding the Output

### Individual Vulnerability Reports

Each `{SEVERITY}-{NUMBER}.md` file contains:
- **Title** - Vulnerability name
- **Severity** - CR/HI/ME/LO with full name
- **Category** - Type of vulnerability (e.g., SQL injection)
- **CWE** - Common Weakness Enumeration ID with link
- **Tool** - Which SAST tool detected it
- **Description** - What the vulnerability is
- **Affected Files** - File path and line numbers
- **Vulnerable Code** - Code snippet showing the issue
- **Impact** - Security implications
- **Remediation** - How to fix it
- **Resources** - Reference links

### Summary Report (summary.md)

Contains:
- Executive summary with risk level
- Statistics by severity and category
- Breakdown table by category
- List of critical and high findings
- Files with most issues
- Prioritized recommendations

## Custom Semgrep Rules

This skill includes custom security rules in `assets/semgrep-rules/security-best-practices.yaml`.

**To use custom rules:**
```bash
semgrep scan --config=assets/semgrep-rules/security-best-practices.yaml .
```

The custom rules detect common security anti-patterns including hardcoded secrets, weak cryptography, injection vulnerabilities, and insecure configurations.

## Common Scenarios

### Scenario 1: Full Codebase Audit

**User:** "Run a security audit on this codebase"

**Action:**
1. Run `python3 run_security_scan.py .`
2. Wait for scan completion (may take 1-5 minutes)
3. Review generated reports
4. Present summary with critical findings first
5. Offer to help fix vulnerabilities

### Scenario 2: Pre-Production Security Check

**User:** "We're about to deploy to production. Check for security issues."

**Action:**
1. Emphasize criticality - focus on CR/HI only
2. Run scan with project name: `--project "Production Release v2.0"`
3. Flag any CR findings as blockers
4. Provide immediate remediation for critical issues
5. Suggest quick wins for high-severity items

### Scenario 3: Focus on Specific Vulnerability Type

**User:** "Check for SQL injection vulnerabilities"

**Action:**
1. Run full scan (tools may find related issues)
2. Filter results to SQL injection category
3. Review each finding in depth
4. Check for parameterized query usage
5. Suggest ORM usage if appropriate

### Scenario 4: Legacy Code Assessment

**User:** "I inherited this codebase. What security issues should I worry about?"

**Action:**
1. Run scan and get overview
2. Prioritize findings by severity
3. Group findings by category for better understanding
4. Explain what each category means
5. Create phased remediation plan (immediate, short-term, long-term)
6. Suggest security best practices for ongoing development

## Limitations and Considerations

**Tool Limitations:**
- SAST tools cannot detect all vulnerabilities (e.g., business logic flaws)
- False positives are possible - always validate in context
- Tools miss context that manual review would catch
- Dependency scanners may report vulnerabilities in unused code paths

**Recommendations:**
- Combine SAST with manual security review
- Perform dynamic testing (DAST) for runtime issues
- Consider penetration testing for critical applications
- Integrate tools into CI/CD for continuous scanning
- Regular security training for development team

## Skill Resources

### Scripts (`scripts/`)
- **run_security_scan.py** - Main orchestrator (use this to run scans)
- **parsers/** - Tool output parsers (Semgrep, Bandit, npm audit, Trivy)
- **generators/** - Report generators (individual and summary)
- **utils/** - Utilities (severity mapper, deduplicator, language detector)

### References (`references/`)
- **vulnerability-categories.md** - OWASP Top 10, CWE classifications
- **severity-guidelines.md** - How to classify vulnerability severity
- **remediation-patterns.md** - Common fix patterns by vulnerability type
- **tool-configuration.md** - SAST tool installation and configuration

### Assets (`assets/`)
- **semgrep-rules/** - Custom Semgrep security rules
- **templates/** - Report templates (used by generators)

## Example Interaction

```
User: "Can you run a security audit on this codebase?"

Claude: "I'll perform a comprehensive security audit using multiple SAST tools.
Let me scan the codebase now..."

[Runs: python3 run_security_scan.py .]

Claude: "Security audit complete! I found 23 potential vulnerabilities:
- 2 Critical (CR)
- 7 High (HI)
- 10 Medium (ME)
- 4 Low (LO)

Critical findings require immediate attention:
1. CR-001: SQL Injection in src/database/queries.py:45
2. CR-002: Hardcoded API key in src/config/settings.py:12

I've generated detailed reports in ./security-issues-2025-10-25/

Would you like me to help fix the critical vulnerabilities first?"

User: "Yes, please fix the SQL injection issue."

Claude: [Reads src/database/queries.py, provides specific fix with parameterized queries]
```

## Integration with CI/CD

For continuous security scanning, integrate tools into your CI/CD pipeline:

**GitHub Actions:**
```yaml
- name: Security Scan
  run: |
    pip install semgrep bandit
    python3 ~/.claude/skills/security-reviewer/scripts/run_security_scan.py .
```

**GitLab CI:**
```yaml
security_scan:
  script:
    - pip install semgrep bandit
    - python3 ~/.claude/skills/code-security-review/scripts/run_security_scan.py .
  artifacts:
    paths:
      - security-issues-*/
```

See `references/tool-configuration.md` for more CI/CD examples.

## Troubleshooting

**Issue:** "Semgrep not found"
**Solution:** Install with `pip install semgrep` or `brew install semgrep`

**Issue:** "No vulnerabilities found but I expected some"
**Solution:** Check that files aren't excluded. Review `.gitignore` and tool configs.

**Issue:** "Too many false positives"
**Solution:** Review findings in context. Configure tool exclusions for known safe patterns.

**Issue:** "Scan is very slow"
**Solution:** Exclude large directories (node_modules, venv) or use incremental scanning.

## Summary

This skill provides a systematic, tool-based approach to security auditing enhanced by AI analysis. Use it to detect, analyze, and remediate security vulnerabilities in codebases across multiple languages and frameworks. The combination of deterministic SAST tools and contextual AI analysis provides both breadth and depth in security assessment.
