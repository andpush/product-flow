# Conventions seed: Tests

<!-- Seed for the `arch` skill. Adapt and fold into ARCHITECTURE.md's Conventions section.
     Keep only what isn't obvious to a competent engineer. -->
- **TDD** for APIs and before refactoring: RED → GREEN → REFACTOR.
- **Pyramid**: many unit (fast), some integration, few end-to-end (Playwright) — slow but load-bearing.
- Test behavior through the public surface, not implementation details; one clear intent per test, named for the behavior it pins.
- Fake only true boundaries (network, filesystem, clock, randomness, payments); never mock your own business logic.
- Cover the acceptance criteria and the non-trivial/error paths — not lines for their own sake.
- Coverage targets live in ARCHITECTURE.md, not hardcoded here.
