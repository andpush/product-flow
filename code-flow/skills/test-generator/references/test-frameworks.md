# Test Framework Detection Patterns

This document provides comprehensive patterns for detecting testing frameworks across different technology stacks with confidence scoring.

## Confidence Scoring

- **High (90-100%)**: Multiple strong indicators (config file + dependencies + test files)
- **Medium (60-89%)**: Some indicators (dependencies OR test directory structure)
- **Low (30-59%)**: Weak indicators (file naming conventions only)

## JavaScript/TypeScript Frameworks

### Jest

**Primary Indicators**:
- `jest.config.js`, `jest.config.ts`, `jest.config.json` in root
- `"jest"` section in `package.json`
- Dependencies in `package.json`:
  - `"jest"` or `"@jest/core"`
  - `"ts-jest"` (TypeScript)
  - `"@testing-library/jest-dom"` (React)

**Secondary Indicators**:
- Test files: `*.test.js`, `*.test.ts`, `*.spec.js`, `*.spec.ts`
- `__tests__/` directory
- Scripts in `package.json`: `"test": "jest"`

**Test Command**:
```bash
npm test
# or
yarn test
# or
pnpm test
```

**Coverage Command**:
```bash
npm test -- --coverage
# or
jest --coverage
```

**Confidence Logic**:
```
if (jest.config.* exists AND "jest" in dependencies): HIGH
else if ("jest" in dependencies OR jest scripts): MEDIUM
else if (*.test.js files exist): LOW
```

### Vitest

**Primary Indicators**:
- `vitest.config.ts`, `vitest.config.js` in root
- `vite.config.ts` with `test` section
- Dependencies in `package.json`:
  - `"vitest"`
  - `"@vitest/ui"` (optional UI)

**Secondary Indicators**:
- Test files: `*.test.ts`, `*.spec.ts`
- Scripts in `package.json`: `"test": "vitest"`
- Usually paired with Vite

**Test Command**:
```bash
npm test
# or
vitest
```

**Coverage Command**:
```bash
vitest --coverage
```

**Confidence Logic**:
```
if (vitest.config.* exists AND "vitest" in dependencies): HIGH
else if ("vitest" in dependencies): MEDIUM
else: LOW
```

### Mocha + Chai

**Primary Indicators**:
- `.mocharc.json`, `.mocharc.js`, `.mocharc.yml` in root
- Dependencies in `package.json`:
  - `"mocha"`
  - `"chai"` (assertion library)

**Secondary Indicators**:
- Test files: `*.test.js`, `*.spec.js`
- `test/` directory
- Scripts: `"test": "mocha"`

**Test Command**:
```bash
npm test
# or
mocha
```

**Coverage Command** (requires nyc):
```bash
nyc mocha
```

**Confidence Logic**:
```
if (.mocharc.* exists AND "mocha" in dependencies): HIGH
else if ("mocha" AND "chai" in dependencies): MEDIUM
else: LOW
```

### Other JavaScript Frameworks

#### Jasmine
- `jasmine.json` in `spec/support/`
- `"jasmine"` in dependencies
- Test files: `*.spec.js`

#### AVA
- `ava.config.js`
- `"ava"` in dependencies
- Test files: `*.test.js`, `test.js`

#### Tape
- `"tape"` in dependencies
- Test files: `test/*.js`

## Python Frameworks

### pytest

**Primary Indicators**:
- `pytest.ini`, `pyproject.toml` with `[tool.pytest.ini_options]`
- `setup.cfg` with `[tool:pytest]` section
- Dependencies in `requirements.txt`, `pyproject.toml`, or `Pipfile`:
  - `pytest`
  - `pytest-cov` (coverage)
  - `pytest-mock` (mocking)

**Secondary Indicators**:
- Test files: `test_*.py`, `*_test.py`
- `tests/` or `test/` directory
- `conftest.py` (pytest fixtures)

**Test Command**:
```bash
pytest
# or
python -m pytest
# or with verbose
pytest -v
```

**Coverage Command**:
```bash
pytest --cov=src --cov-report=html
# or
pytest --cov=. --cov-report=term-missing
```

**Confidence Logic**:
```
if (pytest.ini OR pyproject.toml with pytest section) AND pytest in dependencies: HIGH
else if (pytest in dependencies): MEDIUM
else if (test_*.py files exist): LOW
```

### unittest (Built-in)

**Primary Indicators**:
- `unittest.cfg` (rare)
- Import statements: `import unittest` in test files
- No external dependencies (built into Python)

**Secondary Indicators**:
- Test files: `test_*.py`, `*_test.py`
- Test classes inherit from `unittest.TestCase`
- `tests/` directory

**Test Command**:
```bash
python -m unittest discover
# or
python -m unittest tests/test_module.py
```

**Coverage Command** (requires coverage.py):
```bash
coverage run -m unittest discover
coverage report
coverage html
```

**Confidence Logic**:
```
if (test files with unittest.TestCase classes): MEDIUM
else if (test_*.py files exist AND no other framework): LOW
```

### nose2

**Primary Indicators**:
- `nose2.cfg`, `unittest.cfg`
- Dependencies: `nose2`

**Secondary Indicators**:
- Test files: `test_*.py`
- `tests/` directory

**Test Command**:
```bash
nose2
# or
python -m nose2
```

**Coverage Command**:
```bash
nose2 --with-coverage
```

## Ruby Frameworks

### RSpec

**Primary Indicators**:
- `.rspec` file in root
- `spec/spec_helper.rb` file
- Dependencies in `Gemfile`:
  - `gem 'rspec'`
  - `gem 'rspec-rails'` (Rails)

**Secondary Indicators**:
- Test files: `*_spec.rb`
- `spec/` directory
- `spec/rails_helper.rb` (Rails)

**Test Command**:
```bash
bundle exec rspec
# or
rspec
```

**Coverage Command** (requires simplecov):
```bash
# Add to spec_helper.rb:
# require 'simplecov'
# SimpleCov.start
bundle exec rspec
```

**Confidence Logic**:
```
if (.rspec exists AND spec_helper.rb exists): HIGH
else if ('rspec' in Gemfile): MEDIUM
else if (*_spec.rb files exist): LOW
```

### Minitest

**Primary Indicators**:
- `test/test_helper.rb`
- Dependencies in `Gemfile`:
  - `gem 'minitest'`

**Secondary Indicators**:
- Test files: `test_*.rb`, `*_test.rb`
- `test/` directory
- Test classes inherit from `Minitest::Test`

**Test Command**:
```bash
ruby -Itest test/test_file.rb
# or with rake
rake test
```

**Coverage Command**:
```bash
# Requires simplecov
bundle exec rake test
```

## PHP Frameworks

### PHPUnit

**Primary Indicators**:
- `phpunit.xml`, `phpunit.xml.dist` in root
- Dependencies in `composer.json`:
  - `"phpunit/phpunit"`

**Secondary Indicators**:
- Test files: `*Test.php`
- `tests/` directory
- Test classes extend `PHPUnit\Framework\TestCase`

**Test Command**:
```bash
./vendor/bin/phpunit
# or
composer test
```

**Coverage Command**:
```bash
./vendor/bin/phpunit --coverage-html coverage
# or
./vendor/bin/phpunit --coverage-text
```

**Confidence Logic**:
```
if (phpunit.xml exists AND phpunit in composer.json): HIGH
else if (phpunit in composer.json): MEDIUM
else if (*Test.php files exist): LOW
```

## Go Frameworks

### testing (Built-in)

**Primary Indicators**:
- `go.mod`, `go.sum` files
- Test files: `*_test.go`
- Package declaration: `package mypackage_test` or `package mypackage`

**Secondary Indicators**:
- Functions starting with `Test`
- Import: `import "testing"`

**Test Command**:
```bash
go test ./...
# or verbose
go test -v ./...
```

**Coverage Command**:
```bash
go test -coverprofile=coverage.out ./...
go tool cover -html=coverage.out
# or
go test -cover ./...
```

**Confidence Logic**:
```
if (go.mod exists AND *_test.go files exist): HIGH
else if (*_test.go files exist): MEDIUM
else: LOW
```

### testify (Popular Library)

**Primary Indicators**:
- `go.mod` with `github.com/stretchr/testify`
- Test files use `assert` or `require` packages

**Secondary Indicators**:
- Imports like `github.com/stretchr/testify/assert`
- Suite-based tests using `suite.Suite`

**Test Command**:
```bash
go test ./...
```

**Coverage Command**:
```bash
go test -coverprofile=coverage.out ./...
```

## Java Frameworks

### JUnit 5 (Jupiter)

**Primary Indicators**:
- Dependencies in `pom.xml`:
  - `org.junit.jupiter:junit-jupiter`
  - `org.junit.jupiter:junit-jupiter-api`
- Dependencies in `build.gradle`:
  - `testImplementation 'org.junit.jupiter:junit-jupiter'`

**Secondary Indicators**:
- Test files: `*Test.java`, `*Tests.java`
- `src/test/java/` directory
- Annotations: `@Test`, `@BeforeEach`, `@AfterEach`

**Test Command**:
```bash
# Maven
./mvnw test
# Gradle
./gradlew test
```

**Coverage Command**:
```bash
# Maven (with JaCoCo)
./mvnw test jacoco:report
# Gradle (with JaCoCo)
./gradlew test jacocoTestReport
```

**Confidence Logic**:
```
if (pom.xml/build.gradle exists AND junit-jupiter in dependencies): HIGH
else if (src/test/java/ exists): MEDIUM
else: LOW
```

### JUnit 4

**Primary Indicators**:
- Dependencies:
  - `junit:junit:4.*`
- Annotations: `@Test`, `@Before`, `@After`

**Secondary Indicators**:
- Test files: `*Test.java`
- `src/test/java/` directory

**Test Command**:
```bash
./mvnw test
# or
./gradlew test
```

### TestNG

**Primary Indicators**:
- Dependencies:
  - `org.testng:testng`
- `testng.xml` configuration file

**Secondary Indicators**:
- Annotations: `@Test`, `@BeforeMethod`, `@AfterMethod`
- Test files: `*Test.java`

**Test Command**:
```bash
./mvnw test
# or
./gradlew test
```

## C# Frameworks

### xUnit

**Primary Indicators**:
- Dependencies in `*.csproj`:
  - `<PackageReference Include="xunit" />`
  - `<PackageReference Include="xunit.runner.visualstudio" />`

**Secondary Indicators**:
- Test files: `*Tests.cs`, `*Test.cs`
- Attributes: `[Fact]`, `[Theory]`

**Test Command**:
```bash
dotnet test
```

**Coverage Command**:
```bash
dotnet test /p:CollectCoverage=true
# or with coverlet
dotnet test --collect:"XPlat Code Coverage"
```

**Confidence Logic**:
```
if (*.csproj with xunit package): HIGH
else if (*.csproj exists): MEDIUM
else: LOW
```

### NUnit

**Primary Indicators**:
- Dependencies:
  - `<PackageReference Include="NUnit" />`
  - `<PackageReference Include="NUnit3TestAdapter" />`

**Secondary Indicators**:
- Attributes: `[Test]`, `[TestFixture]`
- Test files: `*Tests.cs`

**Test Command**:
```bash
dotnet test
```

### MSTest

**Primary Indicators**:
- Dependencies:
  - `<PackageReference Include="MSTest.TestFramework" />`
  - `<PackageReference Include="MSTest.TestAdapter" />`

**Secondary Indicators**:
- Attributes: `[TestMethod]`, `[TestClass]`

**Test Command**:
```bash
dotnet test
```

## Flutter/Dart Frameworks

### flutter_test (Official)

**Primary Indicators**:
- `pubspec.yaml` with:
  ```yaml
  dev_dependencies:
    flutter_test:
      sdk: flutter
  ```
- `test/` directory
- Test files: `*_test.dart`

**Secondary Indicators**:
- Imports: `import 'package:flutter_test/flutter_test.dart';`
- Functions: `void main() { test(...) }` or `testWidgets(...)`
- `analysis_options.yaml` file

**Test Command**:
```bash
flutter test
# or specific file
flutter test test/widget_test.dart
```

**Coverage Command**:
```bash
flutter test --coverage
# Generate HTML report
genhtml coverage/lcov.info -o coverage/html
```

**Confidence Logic**:
```
if (pubspec.yaml with flutter_test AND test/ directory): HIGH
else if (pubspec.yaml exists AND *_test.dart files): MEDIUM
else: LOW
```

### test (Dart Package)

**Primary Indicators**:
- `pubspec.yaml` with:
  ```yaml
  dev_dependencies:
    test: ^1.0.0
  ```
- Test files: `*_test.dart`

**Secondary Indicators**:
- Imports: `import 'package:test/test.dart';`
- Functions: `void main() { test(...) }`

**Test Command**:
```bash
dart test
# or
pub run test
```

**Coverage Command**:
```bash
dart test --coverage=coverage
# Format coverage
dart pub global activate coverage
dart pub global run coverage:format_coverage --lcov --in=coverage --out=coverage/lcov.info --report-on=lib
```

### mockito (Dart Mocking)

**Primary Indicators**:
- `pubspec.yaml` with:
  ```yaml
  dev_dependencies:
    mockito: ^5.0.0
    build_runner: ^2.0.0
  ```

**Secondary Indicators**:
- Mock files: `*.mocks.dart`
- Imports: `import 'package:mockito/mockito.dart';`
- Annotations: `@GenerateMocks([ClassName])`

**Mock Generation Command**:
```bash
flutter pub run build_runner build
# or watch mode
flutter pub run build_runner watch
```

## Detection Algorithm

### Step 1: Identify Language

```
1. Check for package/dependency files:
   - package.json → JavaScript/TypeScript
   - requirements.txt/pyproject.toml → Python
   - Gemfile → Ruby
   - composer.json → PHP
   - go.mod → Go
   - pom.xml/build.gradle → Java
   - *.csproj → C#
   - pubspec.yaml → Dart/Flutter

2. If multiple language files exist:
   - Prioritize by file modification time
   - Consider it a polyglot project
```

### Step 2: Detect Framework

```
For each language:
  1. Read configuration files
  2. Parse dependencies
  3. Scan test directory structure
  4. Check test file naming patterns
  5. Calculate confidence score
  6. Return framework with highest confidence
```

### Step 3: Verify Setup

```
1. Check if test command works:
   - Try running test command
   - If fails, check for missing dependencies
   - Suggest installation command

2. Verify coverage tool:
   - Check if coverage command works
   - If missing, suggest coverage tool installation
```

## Framework Priority Matrix

When multiple frameworks are detected, use this priority order:

### JavaScript/TypeScript
1. Vitest (if Vite project)
2. Jest (most common)
3. Mocha
4. Jasmine
5. AVA

### Python
1. pytest (most popular)
2. unittest (built-in)
3. nose2

### Ruby
1. RSpec (Rails standard)
2. Minitest (Ruby standard)

### PHP
1. PHPUnit (de facto standard)

### Go
1. testify (if in go.mod)
2. testing (built-in)

### Java
1. JUnit 5 (modern)
2. JUnit 4 (legacy)
3. TestNG

### C#
1. xUnit (modern)
2. NUnit
3. MSTest

### Dart/Flutter
1. flutter_test (Flutter apps)
2. test (Dart packages)

## Example Detection Output

```json
{
  "language": "TypeScript",
  "framework": "Jest",
  "confidence": "HIGH",
  "indicators": [
    "jest.config.ts exists",
    "jest in package.json dependencies",
    "__tests__ directory found",
    "*.test.ts files found"
  ],
  "testCommand": "npm test",
  "coverageCommand": "npm test -- --coverage",
  "testDirectory": "__tests__",
  "testFilePattern": "*.test.ts",
  "configFile": "jest.config.ts"
}
```

## Troubleshooting Detection

### False Positives

**Issue**: Detecting wrong framework
- **Cause**: Legacy config files, monorepo with multiple frameworks
- **Solution**: Check file modification dates, ask user to confirm

### False Negatives

**Issue**: Not detecting framework
- **Cause**: Non-standard structure, custom configuration
- **Solution**: Fall back to manual framework selection, document custom setup

### Ambiguous Detection

**Issue**: Multiple frameworks with similar confidence
- **Cause**: Migration in progress, test runner that supports multiple frameworks
- **Solution**: Present options to user, recommend most modern framework
