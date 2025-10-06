# Testing rules

- **TDD Required**: TESTS FIRST - always for APIs and refactoring: RED → GREEN → REFACTOR
- **Coverage**: 80% minimum
- **Tests pyramid**:
  - Unit tests: fast, cheap - add many
  - Integration test - moderate
  - End-to-end tests - slow, but important, use Playwrite
- **Mock**: External APIs, filesystem, time, payments
- **Don't mock**: own business logic
