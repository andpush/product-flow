# Common Remediation Patterns

This document provides remediation patterns for common security vulnerabilities.

## SQL Injection

**Solution:** Always use parameterized queries or ORM methods that handle escaping automatically.

- Python: Use parameterized queries with `%s` placeholders
- Node.js: Use parameterized queries with `$1, $2` placeholders
- Java: Use PreparedStatement
- Always use ORMs (Django ORM, SQLAlchemy, Sequelize) which handle this automatically

## Cross-Site Scripting (XSS)

**Solution:** Use framework-provided escaping mechanisms.

- Modern frameworks (React, Vue, Angular, Flask/Jinja2) auto-escape by default
- Never bypass escaping unless absolutely necessary
- Implement Content Security Policy (CSP) headers
- Sanitize rich text input using libraries like DOMPurify

## Command Injection

**Solution:** Never use shell commands with user input.

- Use language-specific APIs instead of shell commands
- If shell commands are necessary, use argument arrays (not string concatenation)
- Validate input against strict allowlists
- Consider containerization to limit impact

## Path Traversal

**Solution:** Validate that resolved paths stay within allowed directories.

- Use path resolution functions to get absolute paths
- Check that resolved path starts with the allowed base directory
- Use allowlists for permitted filenames
- Never construct paths by concatenating user input directly

## Hard-coded Credentials

**Solution:** Use environment variables and secret management systems.

- Store secrets in environment variables (`.env` for local, never committed)
- Use secret management services (AWS Secrets Manager, HashiCorp Vault, Azure Key Vault)
- Rotate secrets regularly
- Use different secrets for each environment

## Weak Cryptography

**Solution:** Use modern, strong cryptographic algorithms.

**Password Hashing:**
- Use bcrypt, scrypt, or Argon2
- Never use MD5, SHA1, or unsalted hashes

**Encryption:**
- Use AES-256 for symmetric encryption
- Use established libraries (cryptography.io, Node crypto)
- Never implement custom crypto

## Missing Authentication

**Solution:** Implement authentication checks on all sensitive endpoints.

- Use authentication middleware/decorators
- Check both authentication (who are you?) and authorization (what can you do?)
- Implement role-based access control (RBAC)
- Default to denying access

## CSRF Protection

**Solution:** Implement CSRF tokens for state-changing operations.

- Use framework-provided CSRF protection
- Include CSRF tokens in forms and AJAX requests
- Validate tokens on the server
- Use SameSite cookie attribute

## Insecure Deserialization

**Solution:** Use safe serialization formats and validate structure.

- Prefer JSON over language-specific formats
- Validate deserialized data against expected schema
- Never deserialize untrusted data with unsafe formats
- Use schema validation libraries

## Missing Rate Limiting

**Solution:** Implement rate limiting on authentication and sensitive endpoints.

- Limit login attempts (e.g., 5 per minute per IP)
- Implement exponential backoff
- Rate limit API endpoints
- Consider using CAPTCHA for repeated failures

## Security Headers

**Solution:** Add security headers to all HTTP responses.

**Essential Headers:**
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `X-XSS-Protection: 1; mode=block`
- `Strict-Transport-Security: max-age=31536000`
- `Content-Security-Policy: default-src 'self'`

Use libraries like Helmet (Node.js) or Flask-Talisman (Python).

## Input Validation

**Solution:** Validate all user input against expected format and constraints.

- Use validation libraries (marshmallow, joi, express-validator)
- Validate type, length, format, and range
- Use allowlists over denylists
- Validate on both client and server (never trust client-only validation)

## General Best Practices

1. **Principle of Least Privilege** - Grant minimum permissions needed
2. **Defense in Depth** - Multiple security layers
3. **Fail Securely** - Default to secure state on errors
4. **Keep Dependencies Updated** - Regular security updates
5. **Security Testing** - Automated tests in CI/CD
6. **Code Review** - Security-focused reviews
7. **Logging & Monitoring** - Track security events
8. **Security Training** - Regular team education

## Framework-Specific Resources

**Python/Django:**
- Django Security Docs: https://docs.djangoproject.com/en/stable/topics/security/

**Python/Flask:**
- Flask Security: https://flask.palletsprojects.com/en/latest/security/

**Node.js/Express:**
- Express Security Best Practices: https://expressjs.com/en/advanced/best-practice-security.html

**Java/Spring:**
- Spring Security: https://spring.io/projects/spring-security

**Ruby/Rails:**
- Rails Security Guide: https://guides.rubyonrails.org/security.html
