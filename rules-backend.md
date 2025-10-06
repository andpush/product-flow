# Rules for Backend Development

Use Tech Stack:

- Java 21
- JDK 21+
- Quarkus 3.23.3+
- Database: PostgreSQL 17.5+, PostGIS 3.5.3+, Flyway for migrations.
- Framework: Quarkus with REST, Jackson, Postgres, Flyway, JDBI, Micrometer, Jakarta Validation.
- Gradle for builds

Architecture:

- Use Simplified Layered Architecture: Serivce -> Store -> Database.
- Group by feature in package/directory structure, not by layer.
- Exposed services by REST unless other protocol explicetly specified.
- Only create DTOs if data shapes differ from entities.
- Stores (repositories, e.g. UserStore) are JDBI SQL annotated interfaces to minimize boilerplate.
- Prepare code for containerization and GCP Cloud Run deployment.
