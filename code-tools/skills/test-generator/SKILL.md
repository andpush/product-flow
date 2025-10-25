---
name: test-generator
description: Generates comprehensive unit tests with technology stack awareness. Use for creating tests for untested code, analyzing test coverage, running test suites, and ensuring code quality through automated testing across multiple frameworks (Jest, pytest, RSpec, PHPUnit, Go testing, JUnit, Flutter/Dart).
---

# Test Generator

## Overview

Systematically generate, run, and analyze unit tests across multiple technology stacks. Auto-detects testing frameworks, generates context-aware test cases, measures coverage, and provides actionable insights for improving test quality.

## Workflow Phases

The test generation process follows four phases:

1. **Discovery** - Detect tech stack and testing framework (2-3 minutes)
2. **Analysis** - Run existing tests and measure coverage (3-5 minutes)
3. **Generation** - Create new tests for untested code (5-15 minutes)
4. **Validation** - Run new tests and verify quality (2-5 minutes)

## Phase 1: Discovery

**Goal**: Identify the technology stack, testing framework, and project structure.

### Workflow

1. **Detect Primary Language**
   - Scan for language indicators:
     - `package.json`, `tsconfig.json` → JavaScript/TypeScript
     - `requirements.txt`, `pyproject.toml`, `setup.py` → Python
     - `Gemfile`, `*.gemspec` → Ruby
     - `composer.json` → PHP
     - `go.mod`, `go.sum` → Go
     - `pom.xml`, `build.gradle`, `build.gradle.kts` → Java
     - `*.csproj`, `*.sln` → C#
     - `pubspec.yaml`, `analysis_options.yaml` → Flutter/Dart

2. **Identify Testing Framework**
   - Read dependency files to find testing libraries
   - Look for test configuration files
   - Scan test directory structure
   - Use `references/test-frameworks.md` for detection patterns

3. **Map Test Structure**
   - Locate test directories (`test/`, `tests/`, `spec/`, `__tests__/`)
   - Find test file naming conventions (`*.test.js`, `*_test.go`, `*_spec.rb`)
   - Identify source-to-test mapping patterns
   - Detect test organization (co-located vs. separate directories)

4. **Assess Test Configuration**
   - Read test runner configuration
   - Check coverage tool setup
   - Identify custom test scripts in build files
   - Note any test-specific environment variables

### Output Format

```markdown
## Test Discovery Report

### Technology Stack
- **Language**: [language + version]
- **Testing Framework**: [framework + version]
- **Coverage Tool**: [tool]
- **Test Runner**: [command to run tests]

### Project Structure
- **Source Directory**: `[path]`
- **Test Directory**: `[path]`
- **Test File Pattern**: `[pattern]`
- **Total Test Files**: [count]

### Configuration
- **Config File**: `[path]`
- **Test Command**: `[command]`
- **Coverage Command**: `[command]`
- **Parallel Execution**: [yes/no]

### Baseline Metrics
- **Total Source Files**: [count]
- **Total Test Files**: [count]
- **Test-to-Source Ratio**: [ratio]
```

## Phase 2: Analysis

**Goal**: Run existing tests, measure coverage, and identify gaps.

### Workflow

1. **Run Existing Test Suite**
   ```bash
   # Examples based on framework
   npm test                    # Jest/Vitest
   pytest --verbose            # pytest
   flutter test                # Flutter
   go test ./...               # Go
   bundle exec rspec           # RSpec
   ./gradlew test              # Gradle/JUnit
   ```

2. **Generate Coverage Report**
   ```bash
   # Examples based on framework
   npm test -- --coverage                           # Jest
   pytest --cov=src --cov-report=html               # pytest
   flutter test --coverage                          # Flutter
   go test -coverprofile=coverage.out ./...        # Go
   bundle exec rspec --format documentation         # RSpec
   ./gradlew test jacocoTestReport                  # Gradle/JaCoCo
   ```

3. **Parse Test Results**
   - Extract pass/fail counts
   - Identify failing tests with error messages
   - Note slow-running tests (>1s per test)
   - Check for skipped/ignored tests

4. **Analyze Coverage Gaps**
   - Read coverage reports (HTML, JSON, or terminal output)
   - Identify files with <80% coverage
   - Find uncovered functions/methods
   - Locate uncovered branches and edge cases
   - Prioritize files by business criticality

### Output Format

```markdown
## Test Analysis Report

### Test Execution Results
- **Total Tests**: [count]
- **Passed**: [count] ([percentage]%)
- **Failed**: [count] ([percentage]%)
- **Skipped**: [count]
- **Execution Time**: [seconds]s

### Failing Tests
| Test Name | File | Error | Priority |
|-----------|------|-------|----------|
| [name]    | `[file:line]` | [error summary] | P[0-2] |

### Coverage Summary
- **Overall Coverage**: [percentage]%
- **Line Coverage**: [percentage]%
- **Branch Coverage**: [percentage]%
- **Function Coverage**: [percentage]%

### Coverage Gaps (Priority Order)

**Critical (< 50% coverage)**:
- `[file:line]` - [function/class name] - **[X]% covered**
- `[file:line]` - [function/class name] - **[X]% covered**

**High (50-79% coverage)**:
- `[file:line]` - [function/class name] - **[X]% covered**

**Medium (80-89% coverage)**:
- `[file:line]` - [function/class name] - **[X]% covered**

### Recommended Actions
1. [Action] - **Impact**: [coverage improvement estimate]
2. [Action] - **Impact**: [coverage improvement estimate]
3. [Action] - **Impact**: [coverage improvement estimate]
```

## Phase 3: Generation

**Goal**: Create high-quality unit tests for uncovered code.

### Workflow

1. **Prioritize Test Targets**
   - Start with critical business logic
   - Focus on high-complexity functions (cyclomatic complexity > 5)
   - Target public APIs and exported functions
   - Address security-sensitive code (auth, validation, data handling)

2. **Read Source Code**
   - Understand function signatures and parameters
   - Identify dependencies and side effects
   - Note edge cases and validation logic
   - Look for existing documentation or comments

3. **Generate Test Cases**
   - **Happy path**: Normal inputs with expected outputs
   - **Edge cases**: Null, undefined, empty, boundary values
   - **Error cases**: Invalid inputs, exception handling
   - **Integration**: Dependencies, mocks, and stubs

   Follow framework-specific patterns from `references/test-patterns.md`

4. **Write Test File**
   - Use appropriate file naming convention
   - Include necessary imports and setup
   - Organize tests logically (by feature or scenario)
   - Add descriptive test names and comments
   - Follow project's existing test style

5. **Include Test Data**
   - Create realistic test fixtures
   - Use factories or builders for complex objects
   - Avoid hardcoded magic values (use constants)
   - Consider test data isolation

### Test Generation Principles

- **Arrange-Act-Assert (AAA)**: Clear test structure
- **One assertion per test** (when possible)
- **Descriptive names**: Test name describes what is being tested and expected outcome
- **Independent tests**: No test dependencies or shared state
- **Fast execution**: Mock external dependencies (APIs, databases, file system)
- **Deterministic**: Same input always produces same output

### Framework-Specific Patterns

#### JavaScript/TypeScript (Jest/Vitest)

```javascript
import { describe, it, expect, beforeEach, vi } from 'vitest';
import { functionToTest } from './module';

describe('functionToTest', () => {
  beforeEach(() => {
    // Setup before each test
  });

  it('should handle valid input correctly', () => {
    // Arrange
    const input = 'valid';

    // Act
    const result = functionToTest(input);

    // Assert
    expect(result).toBe('expected output');
  });

  it('should throw error for invalid input', () => {
    // Arrange
    const input = null;

    // Act & Assert
    expect(() => functionToTest(input)).toThrow('Invalid input');
  });
});
```

#### Python (pytest)

```python
import pytest
from module import function_to_test

class TestFunctionToTest:
    @pytest.fixture
    def valid_input(self):
        return "valid"

    def test_handles_valid_input_correctly(self, valid_input):
        # Act
        result = function_to_test(valid_input)

        # Assert
        assert result == "expected output"

    def test_raises_error_for_invalid_input(self):
        # Arrange
        invalid_input = None

        # Act & Assert
        with pytest.raises(ValueError, match="Invalid input"):
            function_to_test(invalid_input)

    @pytest.mark.parametrize("input,expected", [
        ("case1", "output1"),
        ("case2", "output2"),
    ])
    def test_multiple_cases(self, input, expected):
        assert function_to_test(input) == expected
```

#### Flutter/Dart

```dart
import 'package:flutter_test/flutter_test.dart';
import 'package:mockito/mockito.dart';
import 'package:your_app/module.dart';

void main() {
  group('functionToTest', () {
    setUp(() {
      // Setup before each test
    });

    test('should handle valid input correctly', () {
      // Arrange
      final input = 'valid';

      // Act
      final result = functionToTest(input);

      // Assert
      expect(result, equals('expected output'));
    });

    test('should throw error for invalid input', () {
      // Arrange
      final input = null;

      // Act & Assert
      expect(
        () => functionToTest(input),
        throwsA(isA<ArgumentError>()),
      );
    });
  });
}
```

#### Ruby (RSpec)

```ruby
require 'spec_helper'
require_relative '../lib/module'

RSpec.describe '#function_to_test' do
  let(:valid_input) { 'valid' }

  context 'with valid input' do
    it 'returns expected output' do
      result = function_to_test(valid_input)
      expect(result).to eq('expected output')
    end
  end

  context 'with invalid input' do
    it 'raises an error' do
      expect { function_to_test(nil) }.to raise_error(ArgumentError, /Invalid input/)
    end
  end
end
```

#### Go

```go
package mypackage

import (
    "testing"
    "github.com/stretchr/testify/assert"
)

func TestFunctionToTest(t *testing.T) {
    t.Run("handles valid input correctly", func(t *testing.T) {
        // Arrange
        input := "valid"

        // Act
        result, err := FunctionToTest(input)

        // Assert
        assert.NoError(t, err)
        assert.Equal(t, "expected output", result)
    })

    t.Run("returns error for invalid input", func(t *testing.T) {
        // Arrange
        input := ""

        // Act
        result, err := FunctionToTest(input)

        // Assert
        assert.Error(t, err)
        assert.Empty(t, result)
    })
}
```

### Output Format

```markdown
## Test Generation Report

### Generated Test Files
| File | Tests Added | Coverage Target | Lines of Code |
|------|-------------|-----------------|---------------|
| `[test_file:line]` | [count] | `[source_file]` | [loc] |

### Test Coverage

**[TestFileName]** - `[path/to/test_file]`

Testing: `[source_file:line]`

**Test Cases**:
1. ✓ Happy path: [description]
2. ✓ Edge case: [description]
3. ✓ Error case: [description]
4. ✓ [Additional cases...]

**Mocks/Stubs**: [list dependencies that were mocked]

**Estimated Coverage Increase**: +[X]%
```

## Phase 4: Validation

**Goal**: Run new tests and verify they pass and improve coverage.

### Workflow

1. **Run New Tests**
   - Execute test suite with new tests
   - Verify all new tests pass
   - Check for flaky tests (run multiple times)
   - Measure execution time

2. **Verify Coverage Improvement**
   - Re-run coverage analysis
   - Compare before/after metrics
   - Confirm coverage gaps are filled
   - Check for regression in existing coverage

3. **Code Review**
   - Verify test quality:
     - Tests are independent
     - Assertions are meaningful
     - Edge cases are covered
     - Mocks are appropriate
     - Test names are descriptive
   - Ensure tests follow project conventions
   - Check for test code duplication

4. **Optimize if Needed**
   - Refactor duplicated test setup into fixtures/helpers
   - Extract common test data
   - Improve slow tests (if any > 1s)
   - Add missing edge cases

### Output Format

```markdown
## Test Validation Report

### Execution Results
- **New Tests Added**: [count]
- **All Tests Passing**: [yes/no]
- **Execution Time**: [seconds]s ([change from baseline])

### Coverage Improvement
| Metric | Before | After | Change |
|--------|--------|-------|--------|
| Overall | [X]% | [Y]% | +[Z]% |
| Line Coverage | [X]% | [Y]% | +[Z]% |
| Branch Coverage | [X]% | [Y]% | +[Z]% |
| Function Coverage | [X]% | [Y]% | +[Z]% |

### Quality Checks
- ✓ All tests pass
- ✓ Tests are independent
- ✓ Meaningful assertions
- ✓ Edge cases covered
- ✓ Follows project conventions
- ✓ No test code duplication

### Remaining Gaps
[If any areas still need coverage, list them here]

### Next Steps
1. [Recommended action if any gaps remain]
2. [Suggested improvements or refactoring]
```

## Integration with CI/CD

After generating tests, consider adding automated test running to CI/CD:

### GitHub Actions Example

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup [Language]
        uses: [setup-action]
      - name: Install dependencies
        run: [install command]
      - name: Run tests
        run: [test command]
      - name: Generate coverage
        run: [coverage command]
      - name: Upload coverage
        uses: codecov/codecov-action@v3
```

## Best Practices

### Test Quality Guidelines

1. **Test Independence**: Each test should run in isolation
2. **Clear Naming**: `test_[what]_[when]_[expected]`
3. **Single Responsibility**: One concept per test
4. **Avoid Logic**: Tests should be simple and straightforward
5. **Fast Execution**: Mock slow dependencies (DB, API, filesystem)
6. **Deterministic**: No random values or time dependencies without control
7. **Readable**: Anyone should understand what's being tested

### Coverage Goals

- **Critical code**: 90-100% (auth, payments, data integrity)
- **Business logic**: 80-90%
- **Utilities**: 70-80%
- **UI components**: 60-70% (focus on logic, not rendering)
- **Overall project**: 80%+ recommended

### Anti-Patterns to Avoid

- Testing implementation details instead of behavior
- Brittle tests that break with refactoring
- Tests that depend on execution order
- Overmocking (mocking everything)
- Undermocking (testing integration when unit test is needed)
- Vague assertions (`expect(result).toBeTruthy()` instead of specific value)
- Ignoring edge cases

## Reference Files

### references/test-frameworks.md
Comprehensive framework detection patterns, configuration file signatures, and confidence scoring for Jest, Vitest, pytest, RSpec, PHPUnit, Go testing, JUnit, Flutter/Dart, and more.

### references/test-patterns.md
Language-specific test templates, mocking patterns, assertion styles, and best practices for each supported framework.

## Example Usage

### Scenario 1: Full Coverage Analysis

```bash
# User asks: "Analyze test coverage and generate missing tests"

# Phase 1: Discovery
[Detect Jest + TypeScript]

# Phase 2: Analysis
[Run npm test -- --coverage]
[Parse coverage report: 64% overall, auth.ts only 45% covered]

# Phase 3: Generation
[Generate tests for auth.ts focusing on uncovered branches]
[Create test/auth.test.ts with 15 new test cases]

# Phase 4: Validation
[Run npm test]
[Coverage increased to 87% overall, auth.ts now 92%]
```

### Scenario 2: Test Specific File

```bash
# User asks: "Write tests for src/utils/validator.dart"

# Phase 1: Discovery
[Detect Flutter + Dart]

# Phase 2: Analysis
[Find no existing tests for validator.dart]

# Phase 3: Generation
[Read validator.dart]
[Generate test/utils/validator_test.dart with happy path, edge cases, error cases]

# Phase 4: Validation
[Run flutter test]
[All 12 new tests pass, validator.dart now 95% covered]
```

### Scenario 3: Fix Failing Tests

```bash
# User asks: "My tests are failing, help me fix them"

# Phase 2: Analysis (skip Discovery if already known)
[Run test suite]
[3 tests failing in payment.test.ts due to mock configuration]

# Phase 3: Generation (fix mode)
[Analyze failures]
[Update mocks with correct async behavior]

# Phase 4: Validation
[Run tests again]
[All tests now passing]
```

## Advanced Features

### Mutation Testing
Consider suggesting mutation testing tools to verify test quality:
- **JavaScript**: Stryker
- **Python**: mutmut
- **Java**: PIT

### Property-Based Testing
For complex logic, suggest property-based testing:
- **JavaScript**: fast-check
- **Python**: Hypothesis
- **Dart**: test_api with custom generators

### Snapshot Testing
For UI components or large data structures:
- **Jest**: Built-in snapshot testing
- **pytest**: pytest-snapshot
- **Flutter**: Golden tests

## Troubleshooting

### Common Issues

**Issue**: Tests fail in CI but pass locally
- **Cause**: Environment differences, timing issues
- **Fix**: Check environment variables, use deterministic values, increase timeouts

**Issue**: Slow test execution
- **Cause**: Not mocking external dependencies
- **Fix**: Mock HTTP clients, databases, file I/O

**Issue**: Flaky tests
- **Cause**: Race conditions, shared state, time dependencies
- **Fix**: Ensure test isolation, mock time, use proper async/await

**Issue**: Low coverage despite many tests
- **Cause**: Testing same paths multiple times, missing edge cases
- **Fix**: Review coverage report, identify uncovered branches, add edge case tests
