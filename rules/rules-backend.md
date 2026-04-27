# Rules for Backend Development

Use Tech Stack:

- Kotlin 2.3.20+
- JDK 25
- Quarkus 3.34.5+ (with REST, Jackson, Jakarta Validation)
- Database: PostgreSQL 18+, PostGIS 3.6.2+, JDBI 3.52.1, Flyway 12.4+
- Observability: Micrometer, OpenTelemetry
- Test: Testcontainers, JUnit 5
- Gradle for builds

Architecture:

- Use Simplified Layered Architecture: Service -> Store -> Database.
- Group by feature in package/directory structure, not by layer (vertical decomposition).
- Exposed services by REST unless other protocol explicetly specified.
- Only create DTOs if data shapes differ from entities.
- Stores (repositories, e.g. UserStore) are JDBI SQL annotated interfaces to minimize boilerplate.
- Prepare code for containerization and GCP Cloud Run deployment.
