# Conventions seed: Backend

<!-- Seed for forge teach. Adapt and fold into ARCHITECTURE.md's Conventions section.
     Keep only what isn't obvious to a competent backend engineer. -->
- Use Simplified Layered Architecture: Service -> Store -> Database.
- Group by feature in package/directory structure, not by layer.
- Exposed services by REST unless other protocol explicetly specified.
- One data class per concept reused across API/service/store. No separate `*Dto` unless the
  wire shape genuinely differs from the domain/store shape.
- Stores (repositories, e.g. UserStore) are JDBI SQL annotated interfaces to minimize boilerplate.
- Prepare for containerization and cloud deployment.
