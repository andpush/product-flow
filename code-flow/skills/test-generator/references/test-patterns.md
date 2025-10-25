# Test Patterns and Templates

This document provides language-specific test patterns, templates, and best practices for generating high-quality unit tests.

## General Principles

### Arrange-Act-Assert (AAA) Pattern

```
// Arrange: Set up test data and dependencies
const input = createTestData();
const mockService = createMock();

// Act: Execute the function under test
const result = functionUnderTest(input, mockService);

// Assert: Verify the expected outcome
expect(result).toBe(expectedValue);
```

### Test Naming Conventions

- **JavaScript/TypeScript**: `should [expected behavior] when [condition]`
- **Python**: `test_[what]_[when]_[expected]`
- **Ruby**: `[context] [expected behavior]`
- **Go**: `Test[FunctionName]_[Scenario]`
- **Java**: `[methodName]_[condition]_[expectedBehavior]`
- **Dart/Flutter**: `should [expected behavior] when [condition]`

---

## JavaScript/TypeScript Patterns

### Jest/Vitest

#### Basic Test Structure

```typescript
import { describe, it, expect, beforeEach, afterEach, vi } from 'vitest';
import { Calculator } from './calculator';

describe('Calculator', () => {
  let calculator: Calculator;

  beforeEach(() => {
    calculator = new Calculator();
  });

  afterEach(() => {
    // Cleanup if needed
  });

  describe('add', () => {
    it('should return sum of two positive numbers', () => {
      // Arrange
      const a = 5;
      const b = 3;

      // Act
      const result = calculator.add(a, b);

      // Assert
      expect(result).toBe(8);
    });

    it('should handle negative numbers', () => {
      expect(calculator.add(-5, -3)).toBe(-8);
    });

    it('should handle zero', () => {
      expect(calculator.add(0, 5)).toBe(5);
    });
  });
});
```

#### Testing Async Functions

```typescript
describe('fetchUser', () => {
  it('should fetch user data successfully', async () => {
    // Arrange
    const userId = '123';
    const expectedUser = { id: '123', name: 'John' };

    // Act
    const user = await fetchUser(userId);

    // Assert
    expect(user).toEqual(expectedUser);
  });

  it('should throw error when user not found', async () => {
    // Arrange
    const invalidId = 'invalid';

    // Act & Assert
    await expect(fetchUser(invalidId)).rejects.toThrow('User not found');
  });
});
```

#### Mocking with Vitest/Jest

```typescript
import { vi } from 'vitest';
import { UserService } from './user-service';
import { ApiClient } from './api-client';

// Mock the entire module
vi.mock('./api-client');

describe('UserService', () => {
  let userService: UserService;
  let mockApiClient: any;

  beforeEach(() => {
    mockApiClient = {
      get: vi.fn(),
      post: vi.fn(),
    };
    userService = new UserService(mockApiClient);
  });

  it('should fetch user by id', async () => {
    // Arrange
    const userId = '123';
    const mockUser = { id: '123', name: 'John' };
    mockApiClient.get.mockResolvedValue(mockUser);

    // Act
    const result = await userService.getUser(userId);

    // Assert
    expect(mockApiClient.get).toHaveBeenCalledWith(`/users/${userId}`);
    expect(result).toEqual(mockUser);
  });

  it('should create user with valid data', async () => {
    // Arrange
    const userData = { name: 'Jane', email: 'jane@example.com' };
    const createdUser = { id: '456', ...userData };
    mockApiClient.post.mockResolvedValue(createdUser);

    // Act
    const result = await userService.createUser(userData);

    // Assert
    expect(mockApiClient.post).toHaveBeenCalledWith('/users', userData);
    expect(result).toEqual(createdUser);
  });
});
```

#### Testing React Components

```typescript
import { render, screen, fireEvent } from '@testing-library/react';
import { Button } from './Button';

describe('Button', () => {
  it('should render with text', () => {
    // Arrange & Act
    render(<Button>Click me</Button>);

    // Assert
    expect(screen.getByText('Click me')).toBeInTheDocument();
  });

  it('should call onClick when clicked', () => {
    // Arrange
    const handleClick = vi.fn();
    render(<Button onClick={handleClick}>Click me</Button>);

    // Act
    fireEvent.click(screen.getByText('Click me'));

    // Assert
    expect(handleClick).toHaveBeenCalledTimes(1);
  });

  it('should be disabled when disabled prop is true', () => {
    // Arrange & Act
    render(<Button disabled>Click me</Button>);

    // Assert
    expect(screen.getByRole('button')).toBeDisabled();
  });
});
```

#### Parameterized Tests

```typescript
describe.each([
  { a: 1, b: 1, expected: 2 },
  { a: 2, b: 2, expected: 4 },
  { a: -1, b: 1, expected: 0 },
])('add($a, $b)', ({ a, b, expected }) => {
  it(`should return ${expected}`, () => {
    expect(calculator.add(a, b)).toBe(expected);
  });
});
```

---

## Python Patterns

### pytest

#### Basic Test Structure

```python
import pytest
from calculator import Calculator

class TestCalculator:
    @pytest.fixture
    def calculator(self):
        """Fixture that creates a Calculator instance for each test."""
        return Calculator()

    def test_add_positive_numbers(self, calculator):
        # Arrange
        a = 5
        b = 3

        # Act
        result = calculator.add(a, b)

        # Assert
        assert result == 8

    def test_add_negative_numbers(self, calculator):
        assert calculator.add(-5, -3) == -8

    def test_add_with_zero(self, calculator):
        assert calculator.add(0, 5) == 5
```

#### Testing Exceptions

```python
def test_divide_by_zero_raises_error(calculator):
    # Arrange
    a = 10
    b = 0

    # Act & Assert
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculator.divide(a, b)
```

#### Parameterized Tests

```python
@pytest.mark.parametrize("a,b,expected", [
    (1, 1, 2),
    (2, 2, 4),
    (-1, 1, 0),
    (0, 0, 0),
])
def test_add_multiple_cases(calculator, a, b, expected):
    assert calculator.add(a, b) == expected
```

#### Fixtures and Mocking

```python
import pytest
from unittest.mock import Mock, patch
from user_service import UserService

@pytest.fixture
def mock_api_client():
    """Create a mock API client."""
    return Mock()

@pytest.fixture
def user_service(mock_api_client):
    """Create UserService with mocked dependencies."""
    return UserService(api_client=mock_api_client)

class TestUserService:
    def test_get_user_by_id(self, user_service, mock_api_client):
        # Arrange
        user_id = "123"
        expected_user = {"id": "123", "name": "John"}
        mock_api_client.get.return_value = expected_user

        # Act
        result = user_service.get_user(user_id)

        # Assert
        mock_api_client.get.assert_called_once_with(f"/users/{user_id}")
        assert result == expected_user

    def test_create_user_with_valid_data(self, user_service, mock_api_client):
        # Arrange
        user_data = {"name": "Jane", "email": "jane@example.com"}
        created_user = {"id": "456", **user_data}
        mock_api_client.post.return_value = created_user

        # Act
        result = user_service.create_user(user_data)

        # Assert
        mock_api_client.post.assert_called_once_with("/users", user_data)
        assert result == created_user
```

#### Testing Async Functions

```python
import pytest

@pytest.mark.asyncio
async def test_fetch_user_async():
    # Arrange
    user_id = "123"
    expected_user = {"id": "123", "name": "John"}

    # Act
    user = await fetch_user(user_id)

    # Assert
    assert user == expected_user
```

#### Patching External Dependencies

```python
@patch('user_service.requests.get')
def test_fetch_user_from_api(mock_get):
    # Arrange
    mock_response = Mock()
    mock_response.json.return_value = {"id": "123", "name": "John"}
    mock_get.return_value = mock_response

    # Act
    result = fetch_user_from_api("123")

    # Assert
    mock_get.assert_called_once_with("https://api.example.com/users/123")
    assert result["name"] == "John"
```

---

## Ruby Patterns

### RSpec

#### Basic Test Structure

```ruby
require 'spec_helper'
require_relative '../lib/calculator'

RSpec.describe Calculator do
  let(:calculator) { Calculator.new }

  describe '#add' do
    context 'with positive numbers' do
      it 'returns the sum' do
        # Arrange
        a = 5
        b = 3

        # Act
        result = calculator.add(a, b)

        # Assert
        expect(result).to eq(8)
      end
    end

    context 'with negative numbers' do
      it 'returns the correct sum' do
        expect(calculator.add(-5, -3)).to eq(-8)
      end
    end

    context 'with zero' do
      it 'returns the non-zero value' do
        expect(calculator.add(0, 5)).to eq(5)
      end
    end
  end
end
```

#### Testing Exceptions

```ruby
describe '#divide' do
  context 'when dividing by zero' do
    it 'raises an ArgumentError' do
      expect { calculator.divide(10, 0) }.to raise_error(ArgumentError, /Cannot divide by zero/)
    end
  end
end
```

#### Mocking and Stubbing

```ruby
require 'spec_helper'

RSpec.describe UserService do
  let(:api_client) { instance_double('ApiClient') }
  let(:user_service) { UserService.new(api_client) }

  describe '#get_user' do
    it 'fetches user by id' do
      # Arrange
      user_id = '123'
      expected_user = { id: '123', name: 'John' }
      allow(api_client).to receive(:get).with("/users/#{user_id}").and_return(expected_user)

      # Act
      result = user_service.get_user(user_id)

      # Assert
      expect(api_client).to have_received(:get).with("/users/#{user_id}")
      expect(result).to eq(expected_user)
    end
  end

  describe '#create_user' do
    it 'creates user with valid data' do
      # Arrange
      user_data = { name: 'Jane', email: 'jane@example.com' }
      created_user = { id: '456', **user_data }
      allow(api_client).to receive(:post).with('/users', user_data).and_return(created_user)

      # Act
      result = user_service.create_user(user_data)

      # Assert
      expect(api_client).to have_received(:post).with('/users', user_data)
      expect(result).to eq(created_user)
    end
  end
end
```

#### Shared Examples

```ruby
RSpec.shared_examples 'a collection' do
  it 'is empty when created' do
    expect(subject).to be_empty
  end

  it 'can add items' do
    subject.add('item')
    expect(subject.size).to eq(1)
  end
end

RSpec.describe Array do
  it_behaves_like 'a collection'
end
```

---

## Go Patterns

### testing + testify

#### Basic Test Structure

```go
package calculator

import (
    "testing"
    "github.com/stretchr/testify/assert"
)

func TestAdd(t *testing.T) {
    // Arrange
    calc := NewCalculator()
    a := 5
    b := 3

    // Act
    result := calc.Add(a, b)

    // Assert
    assert.Equal(t, 8, result, "5 + 3 should equal 8")
}

func TestAddNegativeNumbers(t *testing.T) {
    calc := NewCalculator()
    assert.Equal(t, -8, calc.Add(-5, -3))
}

func TestAddWithZero(t *testing.T) {
    calc := NewCalculator()
    assert.Equal(t, 5, calc.Add(0, 5))
}
```

#### Table-Driven Tests

```go
func TestAdd_TableDriven(t *testing.T) {
    calc := NewCalculator()

    tests := []struct {
        name     string
        a        int
        b        int
        expected int
    }{
        {"positive numbers", 5, 3, 8},
        {"negative numbers", -5, -3, -8},
        {"with zero", 0, 5, 5},
        {"both zero", 0, 0, 0},
    }

    for _, tt := range tests {
        t.Run(tt.name, func(t *testing.T) {
            result := calc.Add(tt.a, tt.b)
            assert.Equal(t, tt.expected, result)
        })
    }
}
```

#### Testing Errors

```go
func TestDivide_ByZero(t *testing.T) {
    // Arrange
    calc := NewCalculator()

    // Act
    result, err := calc.Divide(10, 0)

    // Assert
    assert.Error(t, err, "Expected error when dividing by zero")
    assert.Equal(t, 0, result)
    assert.EqualError(t, err, "cannot divide by zero")
}
```

#### Mocking with testify/mock

```go
package userservice

import (
    "testing"
    "github.com/stretchr/testify/assert"
    "github.com/stretchr/testify/mock"
)

// MockApiClient is a mock of ApiClient interface
type MockApiClient struct {
    mock.Mock
}

func (m *MockApiClient) Get(url string) (map[string]interface{}, error) {
    args := m.Called(url)
    return args.Get(0).(map[string]interface{}), args.Error(1)
}

func TestGetUser(t *testing.T) {
    // Arrange
    mockClient := new(MockApiClient)
    service := NewUserService(mockClient)

    expectedUser := map[string]interface{}{
        "id":   "123",
        "name": "John",
    }

    mockClient.On("Get", "/users/123").Return(expectedUser, nil)

    // Act
    result, err := service.GetUser("123")

    // Assert
    assert.NoError(t, err)
    assert.Equal(t, expectedUser, result)
    mockClient.AssertExpectations(t)
}
```

---

## Flutter/Dart Patterns

### flutter_test

#### Basic Widget Test

```dart
import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';
import 'package:myapp/widgets/counter_widget.dart';

void main() {
  group('CounterWidget', () {
    testWidgets('should display initial count', (WidgetTester tester) async {
      // Arrange & Act
      await tester.pumpWidget(
        const MaterialApp(
          home: CounterWidget(initialCount: 0),
        ),
      );

      // Assert
      expect(find.text('0'), findsOneWidget);
      expect(find.text('1'), findsNothing);
    });

    testWidgets('should increment count when button is pressed',
        (WidgetTester tester) async {
      // Arrange
      await tester.pumpWidget(
        const MaterialApp(
          home: CounterWidget(initialCount: 0),
        ),
      );

      // Act
      await tester.tap(find.byIcon(Icons.add));
      await tester.pump();

      // Assert
      expect(find.text('1'), findsOneWidget);
      expect(find.text('0'), findsNothing);
    });
  });
}
```

#### Unit Tests for Dart Classes

```dart
import 'package:flutter_test/flutter_test.dart';
import 'package:myapp/models/calculator.dart';

void main() {
  group('Calculator', () {
    late Calculator calculator;

    setUp(() {
      calculator = Calculator();
    });

    test('should add two positive numbers', () {
      // Arrange
      const a = 5;
      const b = 3;

      // Act
      final result = calculator.add(a, b);

      // Assert
      expect(result, equals(8));
    });

    test('should handle negative numbers', () {
      expect(calculator.add(-5, -3), equals(-8));
    });

    test('should handle zero', () {
      expect(calculator.add(0, 5), equals(5));
    });
  });
}
```

#### Testing with Mockito

```dart
import 'package:flutter_test/flutter_test.dart';
import 'package:mockito/mockito.dart';
import 'package:mockito/annotations.dart';
import 'package:myapp/services/user_service.dart';
import 'package:myapp/api/api_client.dart';

// Generate mocks
@GenerateMocks([ApiClient])
import 'user_service_test.mocks.dart';

void main() {
  group('UserService', () {
    late MockApiClient mockApiClient;
    late UserService userService;

    setUp(() {
      mockApiClient = MockApiClient();
      userService = UserService(apiClient: mockApiClient);
    });

    test('should fetch user by id', () async {
      // Arrange
      const userId = '123';
      final expectedUser = User(id: '123', name: 'John');

      when(mockApiClient.get('/users/$userId'))
          .thenAnswer((_) async => expectedUser);

      // Act
      final result = await userService.getUser(userId);

      // Assert
      expect(result, equals(expectedUser));
      verify(mockApiClient.get('/users/$userId')).called(1);
    });

    test('should throw exception when user not found', () async {
      // Arrange
      const userId = 'invalid';

      when(mockApiClient.get('/users/$userId'))
          .thenThrow(Exception('User not found'));

      // Act & Assert
      expect(
        () => userService.getUser(userId),
        throwsException,
      );
    });
  });
}
```

#### Testing Async Functions

```dart
test('should fetch user data asynchronously', () async {
  // Arrange
  const userId = '123';
  final expectedUser = User(id: '123', name: 'John');

  when(mockApiClient.get('/users/$userId'))
      .thenAnswer((_) async => expectedUser);

  // Act
  final result = await userService.getUser(userId);

  // Assert
  expect(result, equals(expectedUser));
});
```

#### Golden Tests (Screenshot Testing)

```dart
testWidgets('should match golden file', (WidgetTester tester) async {
  // Arrange & Act
  await tester.pumpWidget(
    const MaterialApp(
      home: MyWidget(),
    ),
  );

  // Assert
  await expectLater(
    find.byType(MyWidget),
    matchesGoldenFile('golden/my_widget.png'),
  );
});
```

#### Testing State Management (Provider)

```dart
import 'package:flutter_test/flutter_test.dart';
import 'package:provider/provider.dart';
import 'package:myapp/providers/counter_provider.dart';

void main() {
  group('CounterProvider', () {
    test('should start with initial value', () {
      // Arrange & Act
      final provider = CounterProvider();

      // Assert
      expect(provider.count, equals(0));
    });

    test('should increment count', () {
      // Arrange
      final provider = CounterProvider();

      // Act
      provider.increment();

      // Assert
      expect(provider.count, equals(1));
    });

    test('should notify listeners when count changes', () {
      // Arrange
      final provider = CounterProvider();
      var notified = false;
      provider.addListener(() {
        notified = true;
      });

      // Act
      provider.increment();

      // Assert
      expect(notified, isTrue);
    });
  });
}
```

---

## PHP Patterns

### PHPUnit

#### Basic Test Structure

```php
<?php

use PHPUnit\Framework\TestCase;

class CalculatorTest extends TestCase
{
    private Calculator $calculator;

    protected function setUp(): void
    {
        $this->calculator = new Calculator();
    }

    public function testAddPositiveNumbers(): void
    {
        // Arrange
        $a = 5;
        $b = 3;

        // Act
        $result = $this->calculator->add($a, $b);

        // Assert
        $this->assertEquals(8, $result);
    }

    public function testAddNegativeNumbers(): void
    {
        $this->assertEquals(-8, $this->calculator->add(-5, -3));
    }

    public function testAddWithZero(): void
    {
        $this->assertEquals(5, $this->calculator->add(0, 5));
    }
}
```

#### Testing Exceptions

```php
public function testDivideByZeroThrowsException(): void
{
    $this->expectException(InvalidArgumentException::class);
    $this->expectExceptionMessage('Cannot divide by zero');

    $this->calculator->divide(10, 0);
}
```

#### Data Providers (Parameterized Tests)

```php
/**
 * @dataProvider additionProvider
 */
public function testAddWithDataProvider(int $a, int $b, int $expected): void
{
    $result = $this->calculator->add($a, $b);
    $this->assertEquals($expected, $result);
}

public function additionProvider(): array
{
    return [
        'positive numbers' => [5, 3, 8],
        'negative numbers' => [-5, -3, -8],
        'with zero' => [0, 5, 5],
        'both zero' => [0, 0, 0],
    ];
}
```

#### Mocking

```php
public function testGetUserById(): void
{
    // Arrange
    $apiClient = $this->createMock(ApiClient::class);
    $apiClient->expects($this->once())
              ->method('get')
              ->with('/users/123')
              ->willReturn(['id' => '123', 'name' => 'John']);

    $userService = new UserService($apiClient);

    // Act
    $result = $userService->getUser('123');

    // Assert
    $this->assertEquals('John', $result['name']);
}
```

---

## Java Patterns

### JUnit 5

#### Basic Test Structure

```java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CalculatorTest {
    private Calculator calculator;

    @BeforeEach
    void setUp() {
        calculator = new Calculator();
    }

    @Test
    void shouldAddPositiveNumbers() {
        // Arrange
        int a = 5;
        int b = 3;

        // Act
        int result = calculator.add(a, b);

        // Assert
        assertEquals(8, result, "5 + 3 should equal 8");
    }

    @Test
    void shouldAddNegativeNumbers() {
        assertEquals(-8, calculator.add(-5, -3));
    }

    @Test
    void shouldAddWithZero() {
        assertEquals(5, calculator.add(0, 5));
    }
}
```

#### Parameterized Tests

```java
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;

class CalculatorTest {
    @ParameterizedTest
    @CsvSource({
        "5, 3, 8",
        "-5, -3, -8",
        "0, 5, 5",
        "0, 0, 0"
    })
    void shouldAddNumbers(int a, int b, int expected) {
        Calculator calculator = new Calculator();
        assertEquals(expected, calculator.add(a, b));
    }
}
```

#### Testing Exceptions

```java
@Test
void shouldThrowExceptionWhenDividingByZero() {
    Calculator calculator = new Calculator();

    Exception exception = assertThrows(
        ArithmeticException.class,
        () -> calculator.divide(10, 0)
    );

    assertEquals("Cannot divide by zero", exception.getMessage());
}
```

#### Mocking with Mockito

```java
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;
import org.junit.jupiter.api.extension.ExtendWith;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class UserServiceTest {
    @Mock
    private ApiClient apiClient;

    @Test
    void shouldGetUserById() {
        // Arrange
        String userId = "123";
        User expectedUser = new User("123", "John");
        when(apiClient.get("/users/123")).thenReturn(expectedUser);

        UserService userService = new UserService(apiClient);

        // Act
        User result = userService.getUser(userId);

        // Assert
        assertEquals(expectedUser, result);
        verify(apiClient).get("/users/123");
    }
}
```

---

## Common Edge Cases to Test

### Null and Undefined

```typescript
// JavaScript/TypeScript
it('should handle null input', () => {
  expect(() => processData(null)).toThrow('Input cannot be null');
});

it('should handle undefined input', () => {
  expect(() => processData(undefined)).toThrow('Input cannot be undefined');
});
```

```python
# Python
def test_handles_none_input():
    with pytest.raises(ValueError, match="Input cannot be None"):
        process_data(None)
```

```dart
// Dart
test('should handle null input', () {
  expect(
    () => processData(null),
    throwsA(isA<ArgumentError>()),
  );
});
```

### Empty Collections

```typescript
it('should handle empty array', () => {
  expect(sumArray([])).toBe(0);
});

it('should handle empty string', () => {
  expect(processString('')).toBe('');
});
```

### Boundary Values

```typescript
it('should handle maximum integer', () => {
  expect(processNumber(Number.MAX_SAFE_INTEGER)).toBeDefined();
});

it('should handle minimum integer', () => {
  expect(processNumber(Number.MIN_SAFE_INTEGER)).toBeDefined();
});
```

### Special Characters

```typescript
it('should handle special characters in string', () => {
  const input = "Hello, World! @#$%^&*()";
  expect(() => validateString(input)).not.toThrow();
});
```

---

## Best Practices Summary

### DO
- ✓ Write descriptive test names
- ✓ Follow AAA pattern (Arrange-Act-Assert)
- ✓ Test one concept per test
- ✓ Use fixtures/setup for common initialization
- ✓ Mock external dependencies
- ✓ Test edge cases and error conditions
- ✓ Keep tests independent
- ✓ Make tests fast and deterministic

### DON'T
- ✗ Test implementation details
- ✗ Write tests that depend on execution order
- ✗ Use production data in tests
- ✗ Skip cleanup (teardown)
- ✗ Ignore flaky tests
- ✗ Copy-paste test code (use helpers)
- ✗ Make vague assertions
- ✗ Test framework code or third-party libraries
