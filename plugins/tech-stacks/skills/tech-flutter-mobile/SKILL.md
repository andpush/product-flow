---
name: tech-flutter-mobile
description: Flutter + Dart mobile development with Riverpod state management
version: 1.0.0
---

# Flutter + Dart Mobile Development

Best practices and standards for building cross-platform mobile applications with Flutter.

## Description

Provides technical expertise for building mobile applications with Dart and Flutter, following modern mobile development practices and Material Design guidelines.

## When to Activate

Activate when:
- Repository contains `.dart` files
- Working in `mobile/` or `app/` directory
- User mentions mobile app, iOS, Android, or Flutter development
- Implementing mobile features
- Project uses Flutter framework

## Tech Stack

### Core Technologies
- **Language**: Dart 3.8+
- **Framework**: Flutter 3.32+
- **State Management**: Riverpod 3.0+
- **Architecture**: Feature-based structure with clean architecture principles

### Key Features
- Cross-platform (iOS + Android)
- Hot reload for fast development
- Rich widget ecosystem
- Material Design and Cupertino widgets
- Native performance

## Dart Best Practices

### Follow Effective Dart Style Guide

Reference: https://dart.dev/effective-dart

**Key Points:**
- Use lowerCamelCase for variables, methods, parameters
- Use UpperCamelCase for classes, enums, typedefs
- Use lowercase_with_underscores for libraries, packages, directories, source files
- Use `log` from `dart:developer` rather than `print` or `debugPrint`

**Example:**
```dart
// Good
class UserProfile {}
void fetchUserData() {}
final userName = 'John';

// Bad
class user_profile {}
void FetchUserData() {}
final UserName = 'John';
```

### Type Safety

```dart
// Always specify types
final String name = 'John';
final List<User> users = [];

// Use type inference when obvious
final name = 'John'; // String is inferred
final users = <User>[]; // List<User> is inferred

// Avoid dynamic
void processData(dynamic data) {} // Bad
void processData(Map<String, Object> data) {} // Good
```

## Flutter Architecture

### Project Structure

```
mobile/
├── lib/
│   ├── features/              # Feature modules
│   │   ├── auth/
│   │   │   ├── data/         # Data layer (repositories, DTOs)
│   │   │   ├── domain/       # Domain layer (models, use cases)
│   │   │   ├── presentation/ # UI layer (widgets, providers)
│   │   │   └── auth_module.dart
│   │   └── user/
│   │       └── ...
│   ├── core/                  # Shared utilities
│   │   ├── theme/
│   │   ├── widgets/          # Shared widgets
│   │   ├── utils/
│   │   └── constants/
│   ├── app.dart              # Root app widget
│   └── main.dart             # Entry point
├── test/                      # Tests
├── assets/                    # Images, fonts
└── pubspec.yaml              # Dependencies
```

**Ensure proper separation of concerns by creating a suitable folder structure.**

### Layered Architecture

```
Presentation Layer (Widgets + Providers)
    ↓
Domain Layer (Models + Use Cases)
    ↓
Data Layer (Repositories + API)
```

## State Management with Riverpod

### Providers

```dart
// Simple state
final counterProvider = StateProvider<int>((ref) => 0);

// Async data
final usersProvider = FutureProvider<List<User>>((ref) async {
  final repository = ref.watch(userRepositoryProvider);
  return repository.fetchUsers();
});

// Computed state
final activeUsersProvider = Provider<List<User>>((ref) {
  final users = ref.watch(usersProvider).value ?? [];
  return users.where((u) => u.isActive).toList();
});

// State notifier for complex state
class UserNotifier extends StateNotifier<UserState> {
  UserNotifier(this._repository) : super(UserState.initial());

  final UserRepository _repository;

  Future<void> loadUser(String id) async {
    state = state.copyWith(isLoading: true);
    try {
      final user = await _repository.getUser(id);
      state = state.copyWith(user: user, isLoading: false);
    } catch (e) {
      state = state.copyWith(error: e.toString(), isLoading: false);
    }
  }
}

final userProvider = StateNotifierProvider<UserNotifier, UserState>((ref) {
  final repository = ref.watch(userRepositoryProvider);
  return UserNotifier(repository);
});
```

### Usage in Widgets

```dart
class UserScreen extends ConsumerWidget {
  const UserScreen({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final userState = ref.watch(userProvider);

    return Scaffold(
      appBar: AppBar(title: const Text('User')),
      body: userState.isLoading
          ? const Center(child: CircularProgressIndicator())
          : userState.error != null
              ? Text('Error: ${userState.error}')
              : UserDetails(user: userState.user!),
    );
  }
}
```

## Widget Best Practices

### Prefer Small Composable Widgets

```dart
// Good - Small, focused widgets
class UserCard extends StatelessWidget {
  const UserCard({required this.user, super.key});

  final User user;

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Column(
        children: [
          UserAvatar(url: user.avatarUrl),
          UserInfo(user: user),
          UserActions(user: user),
        ],
      ),
    );
  }
}

// Bad - Monolithic widget
class UserCard extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Card(
      child: Column(
        children: [
          // 100+ lines of nested widgets...
        ],
      ),
    );
  }
}
```

### Extract Widgets Early

When a subtree gets complex, extract it:

```dart
// Extract this into its own widget
Widget _buildComplexSection() {
  return Container(
    // Many nested widgets...
  );
}

// Better
class ComplexSection extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Container(
      // Many nested widgets...
    );
  }
}
```

## Responsive Layouts

### Use Flex Values Over Hardcoded Sizes

```dart
// Good - Adapts to screen size
Row(
  children: [
    Expanded(flex: 2, child: LeftPanel()),
    Expanded(flex: 3, child: MainContent()),
  ],
)

// Bad - Fixed sizes may overflow
Row(
  children: [
    SizedBox(width: 200, child: LeftPanel()),
    SizedBox(width: 400, child: MainContent()),
  ],
)
```

### Media Query for Breakpoints

```dart
class ResponsiveLayout extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final screenWidth = MediaQuery.of(context).size.width;

    if (screenWidth < 600) {
      return MobileLayout();
    } else if (screenWidth < 1200) {
      return TabletLayout();
    } else {
      return DesktopLayout();
    }
  }
}
```

### LayoutBuilder for Adaptive Widgets

```dart
class AdaptiveGrid extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return LayoutBuilder(
      builder: (context, constraints) {
        final columns = constraints.maxWidth > 600 ? 3 : 1;
        return GridView.count(
          crossAxisCount: columns,
          children: items.map((item) => ItemCard(item)).toList(),
        );
      },
    );
  }
}
```

## Theming

### Material Theme in MaterialApp

```dart
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'My App',
      theme: ThemeData(
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.blue),
        useMaterial3: true,
        textTheme: GoogleFonts.robotoTextTheme(),
        cardTheme: CardTheme(
          elevation: 2,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(12),
          ),
        ),
      ),
      darkTheme: ThemeData.dark().copyWith(
        colorScheme: ColorScheme.fromSeed(
          seedColor: Colors.blue,
          brightness: Brightness.dark,
        ),
      ),
      home: HomeScreen(),
    );
  }
}
```

**Theming should be done by setting the `theme` in the `MaterialApp`, rather than hardcoding colors and sizes in widgets themselves.**

### Accessing Theme in Widgets

```dart
class ThemedButton extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final theme = Theme.of(context);

    return ElevatedButton(
      style: ElevatedButton.styleFrom(
        backgroundColor: theme.colorScheme.primary,
        foregroundColor: theme.colorScheme.onPrimary,
      ),
      onPressed: () {},
      child: Text('Button', style: theme.textTheme.labelLarge),
    );
  }
}
```

## API Integration

### Repository Pattern

```dart
abstract class UserRepository {
  Future<List<User>> fetchUsers();
  Future<User> getUserById(String id);
  Future<void> updateUser(User user);
}

class UserRepositoryImpl implements UserRepository {
  UserRepositoryImpl(this._apiClient);

  final ApiClient _apiClient;

  @override
  Future<List<User>> fetchUsers() async {
    try {
      final response = await _apiClient.get('/users');
      return (response as List)
          .map((json) => User.fromJson(json))
          .toList();
    } catch (e) {
      log('Failed to fetch users: $e', name: 'UserRepository');
      rethrow;
    }
  }

  @override
  Future<User> getUserById(String id) async {
    final response = await _apiClient.get('/users/$id');
    return User.fromJson(response);
  }

  @override
  Future<void> updateUser(User user) async {
    await _apiClient.put('/users/${user.id}', user.toJson());
  }
}

// Provider
final userRepositoryProvider = Provider<UserRepository>((ref) {
  final apiClient = ref.watch(apiClientProvider);
  return UserRepositoryImpl(apiClient);
});
```

### Error Handling

```dart
class Result<T> {
  Result.success(this.data) : error = null;
  Result.failure(this.error) : data = null;

  final T? data;
  final String? error;

  bool get isSuccess => data != null;
  bool get isFailure => error != null;
}

// Usage
Future<Result<User>> fetchUser(String id) async {
  try {
    final user = await repository.getUserById(id);
    return Result.success(user);
  } catch (e) {
    return Result.failure(e.toString());
  }
}
```

## Forms and Validation

```dart
class LoginForm extends StatefulWidget {
  @override
  State<LoginForm> createState() => _LoginFormState();
}

class _LoginFormState extends State<LoginForm> {
  final _formKey = GlobalKey<FormState>();
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();

  @override
  void dispose() {
    _emailController.dispose();
    _passwordController.dispose();
    super.dispose();
  }

  String? _validateEmail(String? value) {
    if (value == null || value.isEmpty) {
      return 'Email is required';
    }
    if (!value.contains('@')) {
      return 'Email is invalid';
    }
    return null;
  }

  String? _validatePassword(String? value) {
    if (value == null || value.isEmpty) {
      return 'Password is required';
    }
    if (value.length < 8) {
      return 'Password must be at least 8 characters';
    }
    return null;
  }

  Future<void> _handleSubmit() async {
    if (_formKey.currentState!.validate()) {
      // Submit form
      final email = _emailController.text;
      final password = _passwordController.text;
      // Call API...
    }
  }

  @override
  Widget build(BuildContext context) {
    return Form(
      key: _formKey,
      child: Column(
        children: [
          TextFormField(
            controller: _emailController,
            decoration: const InputDecoration(labelText: 'Email'),
            validator: _validateEmail,
            keyboardType: TextInputType.emailAddress,
          ),
          TextFormField(
            controller: _passwordController,
            decoration: const InputDecoration(labelText: 'Password'),
            validator: _validatePassword,
            obscureText: true,
          ),
          ElevatedButton(
            onPressed: _handleSubmit,
            child: const Text('Login'),
          ),
        ],
      ),
    );
  }
}
```

## Logging

**Use `log` from `dart:developer`:**

```dart
import 'dart:developer' as developer;

void fetchData() async {
  developer.log('Fetching data...', name: 'DataService');

  try {
    final data = await api.getData();
    developer.log('Data fetched successfully', name: 'DataService');
  } catch (e, stackTrace) {
    developer.log(
      'Failed to fetch data',
      name: 'DataService',
      error: e,
      stackTrace: stackTrace,
    );
  }
}
```

## Performance Best Practices

### Const Constructors

```dart
// Use const for immutable widgets
const Text('Hello') // Good
Text('Hello')        // Bad (creates new instance every rebuild)

// Mark constructors as const
class MyWidget extends StatelessWidget {
  const MyWidget({super.key}); // Good

  @override
  Widget build(BuildContext context) {
    return const Text('Hello');
  }
}
```

### Keys for Lists

```dart
ListView.builder(
  itemCount: items.length,
  itemBuilder: (context, index) {
    final item = items[index];
    return ItemCard(
      key: ValueKey(item.id), // Important for list performance
      item: item,
    );
  },
)
```

### Avoid Rebuilds

```dart
// Use Consumer instead of ConsumerWidget for targeted rebuilds
class UserScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('User')),
      body: Consumer(
        builder: (context, ref, child) {
          final user = ref.watch(userProvider);
          return UserDetails(user: user);
        },
      ),
    );
  }
}
```

## Testing

### Unit Tests

```dart
void main() {
  group('UserService', () {
    late UserService service;
    late MockUserRepository repository;

    setUp(() {
      repository = MockUserRepository();
      service = UserService(repository);
    });

    test('fetchUsers returns list of users', () async {
      when(() => repository.fetchUsers())
          .thenAnswer((_) async => [User(id: '1', name: 'John')]);

      final users = await service.fetchUsers();

      expect(users, hasLength(1));
      expect(users.first.name, equals('John'));
    });
  });
}
```

### Widget Tests

```dart
void main() {
  testWidgets('UserCard displays user name', (tester) async {
    final user = User(id: '1', name: 'John Doe');

    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: UserCard(user: user),
        ),
      ),
    );

    expect(find.text('John Doe'), findsOneWidget);
  });
}
```

## Instructions

When this skill is active:

1. **Follow Effective Dart**: Naming conventions, style guide
2. **Use Riverpod**: For state management
3. **Small Widgets**: Prefer composable over monolithic
4. **Responsive Design**: Use flex, MediaQuery, LayoutBuilder
5. **Theme in MaterialApp**: Don't hardcode colors/sizes
6. **Proper Structure**: Feature-based with separation of concerns
7. **Type Safety**: Avoid dynamic, use explicit types
8. **Log Properly**: Use `log` from `dart:developer`
9. **Const Widgets**: Use const for immutable widgets
10. **Handle Errors**: Always handle async errors gracefully

## Integration with Other Skills

- **product-flow-core**: Provides overall workflow and architecture
- **ui-ux-design**: Translates design mockups into Flutter widgets
- Works alongside backend skill (tech-java-quarkus)

Focus on mobile implementation - let other skills handle their domains.
