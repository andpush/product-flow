---
name: tech-java-quarkus
description: Java 21 + Quarkus backend development with simplified layered architecture
version: 1.0.0
---
<!-- TODO: NEEDS REVIEW! -->
# Java + Quarkus Backend Development

Best practices and standards for backend development with Java and Quarkus.

## Description

Provides technical expertise for building backend services with Java 21 and Quarkus framework, following simplified layered architecture and modern cloud-native practices.

## When to Activate

Activate when:
- Repository contains `.java` files
- Working in `backend/` directory
- User mentions backend, API, services, or server-side development
- Implementing backend features
- Project uses Quarkus framework

## Tech Stack

### Core Technologies
- **Language**: Java 21
- **JDK**: 21+
- **Framework**: Quarkus 3.23.3+
  - REST (JAX-RS)
  - Jackson (JSON)
  - Jakarta Validation
  - Micrometer (metrics)
- **Database**: PostgreSQL 17.5+, PostGIS 3.5.3+
- **Migrations**: Flyway
- **Data Access**: JDBI (SQL annotated interfaces)
- **Build Tool**: Gradle

### Deployment
- Containerization ready (Docker)
- Target platform: GCP Cloud Run
- Cloud-native patterns

## Architecture Pattern

### Simplified Layered Architecture

```
Service Layer (Business Logic)
    ↓
Store Layer (Data Access)
    ↓
Database
```

**Key Principles:**
- **Service → Store → Database**: Clear separation of concerns
- **Group by feature**: Package structure organized by feature, not by layer
- **REST by default**: Services exposed via REST unless otherwise specified
- **Minimal DTOs**: Only create DTOs when data shapes differ from entities
- **Interface-based repositories**: Stores are JDBI SQL annotated interfaces

### Package Structure

```
src/main/java/com/product/
├── user/                   # Feature: User Management
│   ├── UserService.java    # Business logic
│   ├── UserStore.java      # Data access interface (JDBI)
│   ├── UserResource.java   # REST endpoints
│   ├── User.java           # Entity
│   └── UserDTO.java        # DTO (only if needed)
├── order/                  # Feature: Orders
│   ├── OrderService.java
│   ├── OrderStore.java
│   └── ...
└── common/                 # Shared utilities
    ├── validation/
    └── exceptions/
```

**Group by feature, not by layer!**

## Coding Standards

### Service Layer

**Responsibilities:**
- Business logic and rules
- Orchestration of data operations
- Input validation (using Jakarta Validation)
- Transaction management
- Error handling

**Example:**
```java
@ApplicationScoped
public class UserService {
    @Inject
    UserStore userStore;

    @Transactional
    public User createUser(UserDTO dto) {
        // Business logic here
        validateEmail(dto.email());

        User user = new User(dto.email(), dto.name());
        return userStore.insert(user);
    }

    public List<User> findActiveUsers() {
        return userStore.findByStatus("ACTIVE");
    }
}
```

### Store Layer (Repository)

**Use JDBI SQL annotated interfaces to minimize boilerplate:**

```java
@RegisterBeanMapper(User.class)
public interface UserStore {
    @SqlQuery("SELECT * FROM users WHERE id = :id")
    Optional<User> findById(@Bind("id") Long id);

    @SqlQuery("SELECT * FROM users WHERE status = :status")
    List<User> findByStatus(@Bind("status") String status);

    @SqlUpdate("INSERT INTO users (email, name) VALUES (:email, :name)")
    @GetGeneratedKeys
    Long insert(@BindBean User user);
}
```

### REST Resources

**Keep thin - delegate to services:**

```java
@Path("/users")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class UserResource {
    @Inject
    UserService userService;

    @GET
    @Path("/{id}")
    public Response getUser(@PathParam("id") Long id) {
        return userService.findById(id)
            .map(user -> Response.ok(user).build())
            .orElse(Response.status(404).build());
    }

    @POST
    public Response createUser(@Valid UserDTO dto) {
        User user = userService.createUser(dto);
        return Response.status(201).entity(user).build();
    }
}
```

### Entity vs DTO

**Entities** (Domain Objects):
```java
public record User(
    Long id,
    String email,
    String name,
    LocalDateTime createdAt
) {}
```

**DTOs** (only when shape differs):
```java
public record UserDTO(
    @NotBlank @Email String email,
    @NotBlank String name
) {}
```

**When to use DTOs:**
- API request/response shapes differ from entity
- Need different validation rules
- Want to hide internal fields
- Aggregating data from multiple entities

**When NOT to use DTOs:**
- Entity shape matches API contract
- No special validation needed
- Direct mapping is fine

## Database Migrations

### Flyway Migrations

**File naming**: `V{version}__{description}.sql`

```sql
-- V1__create_users_table.sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(50) NOT NULL DEFAULT 'ACTIVE',
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_users_status ON users(status);
```

**Best practices:**
- One migration per logical change
- Always include indexes for queried columns
- Use NOT NULL when appropriate
- Define foreign keys
- Include sample data for development (in separate migrations)

## Error Handling

### Exception Hierarchy

```java
public class BusinessException extends RuntimeException {
    private final ErrorCode code;

    public BusinessException(ErrorCode code, String message) {
        super(message);
        this.code = code;
    }
}

public enum ErrorCode {
    USER_NOT_FOUND,
    INVALID_EMAIL,
    DUPLICATE_EMAIL
}
```

### Global Exception Handler

```java
@Provider
public class GlobalExceptionHandler implements ExceptionMapper<BusinessException> {
    @Override
    public Response toResponse(BusinessException e) {
        return Response.status(400)
            .entity(new ErrorResponse(e.getCode(), e.getMessage()))
            .build();
    }
}
```

## Validation

### Use Jakarta Validation

```java
public record CreateUserRequest(
    @NotBlank(message = "Email is required")
    @Email(message = "Email must be valid")
    String email,

    @NotBlank(message = "Name is required")
    @Size(min = 2, max = 100, message = "Name must be 2-100 characters")
    String name
) {}
```

### Custom Validators

```java
@Target({FIELD, PARAMETER})
@Retention(RUNTIME)
@Constraint(validatedBy = StrongPasswordValidator.class)
public @interface StrongPassword {
    String message() default "Password must be strong";
    Class<?>[] groups() default {};
    Class<? extends Payload>[] payload() default {};
}
```

## Testing

### Unit Tests (Services)

```java
@QuarkusTest
class UserServiceTest {
    @Inject
    UserService userService;

    @InjectMock
    UserStore userStore;

    @Test
    void shouldCreateUser() {
        // Arrange
        UserDTO dto = new UserDTO("test@example.com", "Test User");
        when(userStore.insert(any())).thenReturn(1L);

        // Act
        User result = userService.createUser(dto);

        // Assert
        assertEquals("test@example.com", result.email());
        verify(userStore).insert(any());
    }
}
```

### Integration Tests (REST)

```java
@QuarkusTest
class UserResourceTest {
    @Test
    void shouldGetUser() {
        given()
            .when().get("/users/1")
            .then()
            .statusCode(200)
            .body("email", equalTo("test@example.com"));
    }
}
```

## Performance Considerations

### Database Queries
- Use indexes on frequently queried columns
- Avoid N+1 queries (use JOINs or batch loading)
- Use pagination for large result sets
- Consider database connection pooling settings

### Caching
- Use `@CacheResult` for expensive operations
- Cache lookup data (rarely changing)
- Set appropriate TTLs
- Consider cache invalidation strategy

### Async Processing
- Use `@Asynchronous` for long-running operations
- Consider message queues for decoupled processing
- Use CompletionStage for non-blocking operations

## Cloud-Native Readiness

### Containerization

**Dockerfile:**
```dockerfile
FROM registry.access.redhat.com/ubi8/openjdk-21:latest
COPY build/quarkus-app /deployments/
CMD ["java", "-jar", "/deployments/quarkus-run.jar"]
```

### Health Checks

```java
@Readiness
public class DatabaseHealthCheck implements HealthCheck {
    @Inject
    DataSource dataSource;

    @Override
    public HealthCheckResponse call() {
        try {
            dataSource.getConnection().close();
            return HealthCheckResponse.up("database");
        } catch (Exception e) {
            return HealthCheckResponse.down("database");
        }
    }
}
```

### Configuration

Use `application.properties` with profile-specific overrides:

```properties
# application.properties
quarkus.datasource.db-kind=postgresql
quarkus.datasource.username=${DB_USER:postgres}
quarkus.datasource.password=${DB_PASSWORD:secret}

# application-prod.properties
quarkus.datasource.jdbc.url=${DATABASE_URL}
```

## Instructions

When this skill is active:

1. **Follow Architecture Pattern**: Service → Store → Database
2. **Group by Feature**: Package by feature, not by layer
3. **Minimize Boilerplate**: Use JDBI interfaces, records, minimal DTOs
4. **Validate Inputs**: Use Jakarta Validation annotations
5. **Handle Errors Gracefully**: Use exception hierarchy and mappers
6. **Write Tests**: Unit tests for services, integration tests for REST
7. **Prepare for Cloud**: Health checks, externalized config, containerization
8. **Optimize Performance**: Indexes, caching, async where appropriate

## Integration with Other Skills

- **product-flow-core**: Provides overall workflow and architecture principles
- **business-analysis**: Translates feature requirements into technical implementation
- Works alongside frontend skills (tech-svelte-frontend, tech-flutter-mobile)

Focus on backend implementation - let other skills handle their domains.
