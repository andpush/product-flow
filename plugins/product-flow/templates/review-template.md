<!-- Use this template when creating `product/features/{feature_id}/review-YYYY-MM-DD.md` with the `/feature-review` command. -->

# Code Review Results

**Overall Assessment**: {Excellent | Good | Acceptable | Needs Improvement | Poor}

## Review Scope

**Files Reviewed**: [number]
**Lines of Code**: +{additions} -{deletions} lines
**Focus Areas**: [functionality/security/performance/architecture/all]

## Functionality Review

### Requirements Compliance

- [ ] **All acceptance criteria implemented**: [Status and notes]
- [ ] **User workflows function correctly**: [Status and notes]
- [ ] **Edge cases handled appropriately**: [Status and notes]
- [ ] **Error handling comprehensive**: [Status and notes]
- [ ] **Integration points working**: [Status and notes]

### Functional Issues Found
[If no issues, state "No functional issues identified"]

#### 🔴 Critical Functional Issues
- **Issue**: [Description of critical functional problem]
  - **Location**: [file_path:line_number]
  - **Impact**: [How this affects functionality]
  - **Fix Required**: [Specific action needed]

#### 🟡 Important Functional Issues
- **Issue**: [Description of important functional problem]
  - **Location**: [file_path:line_number]
  - **Impact**: [How this affects functionality]
  - **Recommendation**: [Suggested improvement]

## Code Quality Review

### Code Structure and Design
- [ ] **Single Responsibility Principle**: Functions/classes have focused purpose
- [ ] **DRY Principle**: No unnecessary code duplication
- [ ] **Separation of Concerns**: Clear boundaries between layers
- [ ] **Consistent Patterns**: Follows established project conventions
- [ ] **Appropriate Abstractions**: Good balance of abstraction vs simplicity

### Code Readability
- [ ] **Clear Naming**: Variables, functions, classes have descriptive names
- [ ] **Appropriate Comments**: Complex logic explained, why not what
- [ ] **Consistent Formatting**: Follows project style guide
- [ ] **Logical Organization**: Code flows logically and is easy to follow
- [ ] **Reasonable Complexity**: Functions/methods are appropriately sized

### Code Quality Issues Found

#### 🟡 Important Code Quality Issues
- **Issue**: [Description of code quality problem]
  - **Location**: [file_path:line_number]
  - **Current Code**:
    ```[language]
    [Current problematic code]
    ```
  - **Suggested Improvement**:
    ```[language]
    [Improved code example]
    ```
  - **Rationale**: [Why this improvement is better]

#### 🟢 Code Quality Suggestions
- **Suggestion**: [Minor improvement suggestion]
  - **Location**: [file_path:line_number]
  - **Benefit**: [How this would improve the code]

## Security Review

### Security Checklist
- [ ] **No hardcoded secrets**: API keys, passwords, tokens in environment variables
- [ ] **Input validation**: All user inputs validated and sanitized
- [ ] **SQL injection prevention**: Parameterized queries/ORM used consistently
- [ ] **XSS protection**: Output properly escaped, CSP headers configured
- [ ] **Authentication verification**: Proper authentication checks in place
- [ ] **Authorization controls**: Permission checks for sensitive operations
- [ ] **HTTPS enforcement**: Secure communication protocols used
- [ ] **Error handling**: No sensitive information leaked in error messages

### Security Issues Found
[If no issues, state "No security vulnerabilities identified"]

#### 🔴 Critical Security Issues
- **Vulnerability**: [Description of security vulnerability]
  - **Location**: [file_path:line_number]
  - **Risk Level**: {High | Medium | Low}
  - **Potential Impact**: [What could happen if exploited]
  - **Fix Required**: [Specific security fix needed]
  - **Code Example**:
    ```[language]
    // Current vulnerable code
    [Vulnerable code]

    // Secure alternative
    [Secure code]
    ```

#### 🟡 Important Security Concerns
- **Concern**: [Description of security concern]
  - **Location**: [file_path:line_number]
  - **Risk**: [Potential security risk]
  - **Recommendation**: [Security improvement suggestion]

## Performance Review

### Performance Considerations
- [ ] **Efficient algorithms**: No obvious algorithmic inefficiencies
- [ ] **Database optimization**: Queries optimized, proper indexing
- [ ] **Caching strategy**: Appropriate use of caching mechanisms
- [ ] **Resource management**: Proper cleanup of resources and connections
- [ ] **Bundle optimization**: Frontend assets optimized for loading speed
- [ ] **Memory usage**: No obvious memory leaks or excessive usage

### Performance Issues Found
[If no issues, state "No performance issues identified"]

#### 🟡 Important Performance Issues
- **Issue**: [Description of performance problem]
  - **Location**: [file_path:line_number]
  - **Impact**: [How this affects performance]
  - **Current Approach**:
    ```[language]
    [Current inefficient code]
    ```
  - **Optimization Suggestion**:
    ```[language]
    [Optimized code]
    ```
  - **Expected Improvement**: [Quantified performance benefit]

#### 🟢 Performance Suggestions
- **Optimization**: [Performance optimization suggestion]
  - **Benefit**: [Expected performance improvement]
  - **Implementation**: [How to implement optimization]

## Testing Review

### Test Coverage Assessment
- [ ] **Unit tests present**: New functionality has unit tests
- [ ] **Integration tests**: API endpoints and workflows tested
- [ ] **Test quality**: Tests verify behavior, not just coverage
- [ ] **Edge cases covered**: Boundary conditions and error scenarios tested
- [ ] **Mock usage**: External dependencies properly mocked
- [ ] **Test maintainability**: Tests are clear and maintainable

### Test Coverage Metrics
- **Unit Test Coverage**: [percentage]% ({target}% target)
- **Integration Test Coverage**: [status]
- **E2E Test Coverage**: [status]

### Testing Issues Found
[If no issues, state "Testing coverage and quality are adequate"]

#### 🟡 Important Testing Issues
- **Issue**: [Description of testing gap]
  - **Missing Coverage**: [What scenarios are not tested]
  - **Risk**: [Potential issues from missing tests]
  - **Recommendation**: [Specific tests to add]

#### 🟢 Testing Suggestions
- **Enhancement**: [Testing improvement suggestion]
  - **Value**: [Benefit of additional testing]

## Architecture Compliance

### Architecture Review
- [ ] **Pattern consistency**: Follows established architectural patterns
- [ ] **Dependency management**: Appropriate dependencies, no circular refs
- [ ] **Layer separation**: Clear separation between presentation, business, data
- [ ] **Interface design**: Well-defined interfaces and contracts
- [ ] **Scalability considerations**: Design supports expected growth
- [ ] **Documentation updates**: Architectural decisions documented

### Architecture Issues Found
[If no issues, state "Implementation follows architectural guidelines"]

#### 🟡 Important Architecture Issues
- **Issue**: [Description of architectural deviation]
  - **Pattern Violated**: [Specific architectural principle violated]
  - **Impact**: [Long-term implications]
  - **Recommendation**: [How to align with architecture]

## Documentation Review

### Documentation Assessment
- [ ] **Code comments**: Complex logic appropriately commented
- [ ] **API documentation**: Public interfaces documented
- [ ] **README updates**: User-facing documentation updated
- [ ] **Technical decisions**: Major decisions documented
- [ ] **Setup instructions**: Installation/configuration documented

### Documentation Issues
[If adequate, state "Documentation is sufficient"]

#### 🟢 Documentation Suggestions
- **Enhancement**: [Documentation improvement suggestion]
  - **Benefit**: [How this helps future developers]

## Positive Highlights

### Excellent Implementation Aspects
- **Code Quality**: [Specific examples of good code quality]
- **Problem Solving**: [Clever solutions or good design decisions]
- **Best Practices**: [Examples of best practices followed]
- **Innovation**: [Creative approaches or improvements]

## Summary and Recommendations

### Critical Actions Required (Must Fix Before Merge)
[If none, state "No critical issues require immediate attention"]
1. [Critical issue 1 summary]
2. [Critical issue 2 summary]

### Important Improvements (Should Address Before Merge)
[If none, state "No important issues identified"]
1. [Important issue 1 summary]
2. [Important issue 2 summary]

### Optional Enhancements (Nice to Have)
[If none, state "No additional suggestions"]
1. [Suggestion 1 summary]
2. [Suggestion 2 summary]

### Overall Recommendation
**Decision**: {Approve | Approve with Changes | Needs Major Revision | Reject}

**Rationale**: [1-2 sentences explaining the decision]

**Next Steps**:
{If approved: Ready for merge after addressing any critical issues}
{If needs changes: Address feedback and request re-review}
{If rejected: Significant rework required before re-submission}

## Review Metrics

### Code Quality Score: [score]/10
- **Functionality**: [score]/10
- **Code Quality**: [score]/10
- **Security**: [score]/10
- **Performance**: [score]/10
- **Testing**: [score]/10
- **Architecture**: [score]/10

### Issue Summary
- 🔴 **Critical Issues**: [count]
- 🟡 **Important Issues**: [count]
- 🟢 **Suggestions**: [count]
- 💭 **Questions**: [count]

---

<!-- AI Instructions -->

## Template Usage Instructions

1. **Be Specific**: Include file paths, line numbers, and code examples
2. **Use Severity Levels**: Consistently apply 🔴🟡🟢💭 severity indicators
3. **Provide Examples**: Show current code and suggested improvements
4. **Be Constructive**: Focus on improvement, not criticism
5. **Quantify When Possible**: Use metrics for coverage, performance, complexity

## Severity Guidelines

### 🔴 Critical (Must Fix)
- Security vulnerabilities
- Functionality completely broken
- Data corruption risks
- Architecture violations affecting system stability

### 🟡 Important (Should Fix)
- Performance issues
- Code quality problems affecting maintainability
- Missing error handling
- Incomplete test coverage

### 🟢 Suggestions (Nice to Have)
- Code style improvements
- Optimization opportunities
- Additional documentation
- Better naming conventions

### 💭 Questions (Need Clarification)
- Unclear implementation decisions
- Missing context or rationale
- Alternative approach considerations

## Review Quality Standards

A thorough code review should:
- [ ] Examine all changed files
- [ ] Verify functionality against acceptance criteria
- [ ] Check security implications
- [ ] Assess performance impact
- [ ] Evaluate test coverage and quality
- [ ] Ensure architectural compliance
- [ ] Provide actionable feedback
- [ ] Include positive recognition