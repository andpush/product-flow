# Severity Classification Guidelines

This document provides comprehensive guidelines for classifying security vulnerabilities by severity level.

## Severity Levels

### Critical (CR)

**Definition:** Vulnerabilities that allow an attacker to immediately compromise the system, access sensitive data, or execute arbitrary code with minimal or no user interaction.

**Characteristics:**
- Remote code execution (RCE)
- SQL injection with direct database access
- Authentication bypass allowing admin access
- Privilege escalation to system/admin level
- Direct access to sensitive data (PII, financial, credentials)
- Hard-coded production credentials or API keys
- Command injection vulnerabilities

**Examples:**
- SQL queries constructed with string concatenation
- Hard-coded API keys or database passwords
- Unsafe deserialization of user input
- Direct execution of user-provided commands

**CVSS Score Range:** 9.0 - 10.0

**Response Time:** Immediate (within 24 hours)

---

### High (HI)

**Definition:** Vulnerabilities that significantly compromise security but may require some conditions or user interaction to exploit.

**Characteristics:**
- Stored XSS vulnerabilities
- Authorization bypass
- Insecure deserialization
- SSRF with internal network access
- Weak encryption of sensitive data
- Missing authentication on sensitive endpoints
- CSRF on state-changing operations

**Examples:**
- User content rendered without proper escaping
- Base64 encoding used instead of proper encryption
- Admin endpoints without authentication checks
- Sensitive operations without CSRF tokens

**CVSS Score Range:** 7.0 - 8.9

**Response Time:** Within current sprint (1-2 weeks)

---

### Medium (ME)

**Definition:** Vulnerabilities that could lead to security issues but require specific conditions or have limited impact.

**Characteristics:**
- Reflected XSS
- Information disclosure (non-critical data)
- Missing input validation
- Insecure direct object references (IDOR) on non-sensitive data
- Weak password policies
- Missing security headers
- Unvalidated redirects

**Examples:**
- Query parameters reflected in HTML without sanitization
- Stack traces exposed to users
- Missing rate limiting on login endpoints
- Direct object references without authorization checks

**CVSS Score Range:** 4.0 - 6.9

**Response Time:** Next 2-3 sprints (1-2 months)

---

### Low (LO)

**Definition:** Vulnerabilities with minimal security impact or that require very specific conditions to exploit.

**Characteristics:**
- Non-sensitive information disclosure
- Minor configuration issues
- Missing non-critical security headers
- Weak error messages
- Code quality issues with potential security implications
- Outdated dependencies with no known exploits

**Examples:**
- Verbose error messages revealing email addresses
- Missing X-Content-Type-Options header
- Predictable but authenticated resource locations
- Version information disclosure

**CVSS Score Range:** 0.1 - 3.9

**Response Time:** As part of regular development (next quarter)

---

## Classification Decision Tree

Use this decision tree to help classify vulnerability severity:

```
Can attacker execute arbitrary code or SQL?
├─ Yes → CRITICAL
└─ No
   └─ Can attacker access sensitive data (PII, financial, credentials)?
      ├─ Yes
      │  └─ Direct access without authentication?
      │     ├─ Yes → CRITICAL
      │     └─ No → HIGH
      └─ No
         └─ Can attacker modify data or bypass authorization?
            ├─ Yes
            │  └─ On critical functions?
            │     ├─ Yes → HIGH
            │     └─ No → MEDIUM
            └─ No
               └─ Is there information disclosure or security misconfiguration?
                  ├─ Sensitive info → MEDIUM
                  └─ Non-sensitive → LOW
```

## Context-Specific Considerations

### Authentication & Authorization
- **Critical:** Complete bypass of authentication
- **High:** Authorization bypass, privilege escalation
- **Medium:** Weak password policy, missing MFA
- **Low:** Predictable session IDs (but short-lived)

### Data Exposure
- **Critical:** Direct access to production database, PII, financial data
- **High:** Indirect access via injection, exposed API keys
- **Medium:** Non-critical user data exposure
- **Low:** Public information, version numbers

### Injection Vulnerabilities
- **Critical:** SQL injection, OS command injection
- **High:** LDAP injection, XXE with file access
- **Medium:** XPath injection with limited impact
- **Low:** Header injection without security impact

### Cryptography
- **Critical:** Hard-coded production secrets, no encryption of passwords
- **High:** Weak encryption (DES, MD5 for passwords), ECB mode
- **Medium:** Weak random number generation, SHA1 for non-critical data
- **Low:** Missing salt (but strong hash), deprecated but secure algorithms

### Configuration
- **Critical:** Debug mode in production, default admin credentials
- **High:** Overly permissive CORS, disabled certificate validation
- **Medium:** Missing security headers, verbose errors
- **Low:** Non-critical feature enabled, minor version disclosure

## Adjusting Severity Based on Context

Consider these factors when adjusting severity:

### Increase Severity If:
- Vulnerability affects production environment
- Sensitive data is involved (PII, financial, health)
- Exploit requires no authentication
- Exploit is trivial (automated tools available)
- High-value target (financial, healthcare, government)

### Decrease Severity If:
- Vulnerability only affects development environment
- Exploit requires admin access
- Exploit requires sophisticated techniques
- Data involved is non-sensitive
- Compensating controls exist

## References

- [CVSS v3.1 Calculator](https://www.first.org/cvss/calculator/3.1)
- [OWASP Risk Rating Methodology](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)
- [CWE Scoring](https://cwe.mitre.org/)
