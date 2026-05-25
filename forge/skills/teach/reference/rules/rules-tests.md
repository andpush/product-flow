# Conventions seed: Tests

<!-- Seed for forge teach. Adapt and fold into ARCHITECTURE.md's Conventions section.
     Keep only what isn't obvious to a competent engineer. -->
- **TDD**: Always for APIs and before refactoring: RED → GREEN → REFACTOR
- **Tests pyramid**:
  - Unit tests: fast, cheap - add many
  - Integration test - moderate
  - End-to-end tests - slow, but important, use Playwright
- **Mock**: External APIs, filesystem, time, payments
- **Don't mock**: own business logic
- Test behavior through the public surface, not implementation details.
- Prefer real collaborators; fake only true boundaries (network, clock, filesystem, randomness).
- One clear intent per test; name tests by the behavior they pin.
- Cover the acceptance criteria and the non-trivial/error paths — not lines for their own sake.
- Coverage targets live in ARCHITECTURE.md, not hardcoded here.

