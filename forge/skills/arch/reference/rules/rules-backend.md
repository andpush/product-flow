# Conventions seed: Backend

<!-- Seed for forge arch. Adapt and fold into ARCHITECTURE.md's Conventions section.
     Keep only what isn't obvious to a competent backend engineer. -->
- Simplified layered architecture: Service -> Store -> Database.
- Expose services via REST unless another protocol is explicitly specified.
- Prepare for containerization and cloud deployment.
- Tests: see [rules-tests.md](rules-tests.md).
