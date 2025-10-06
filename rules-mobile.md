# Mobile App Development Rules

- Use Dart 3.8+ / Flutter 3.32+ with Riverpod 3.0+ for state management
- Follow official Effective Dart Style Guide on dart.dev
- Theming should be done by setting the `theme` in the `MaterialApp`, rather than hardcoding colors and sizes in the widget themselves
- Ensure proper separation of concerns by creating a suitable folder structure
- Prefer small composable widgets over large ones
- Prefer using flex values over hardcoded sizes when creating widgets inside rows/columns, ensuring the UI adapts to various screen sizes.
- Use `log` from `dart:developer` rather than `print` or `debugPrint` for logging