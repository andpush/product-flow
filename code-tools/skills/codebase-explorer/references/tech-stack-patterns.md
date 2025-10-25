# Tech Stack Detection Patterns

## Framework Detection Patterns

### Python Frameworks

| Signal | Framework | Confidence | Additional Checks |
|--------|-----------|------------|-------------------|
| `django` in requirements.txt | Django | High | Check for `manage.py`, `settings.py` |
| `flask` in requirements.txt | Flask | High | Check for `app.py` or `application.py` |
| `fastapi` in requirements.txt | FastAPI | High | Check for `main.py` with FastAPI imports |
| `pyramid` in requirements.txt | Pyramid | High | Check for `development.ini` |
| `tornado` in requirements.txt | Tornado | Medium | Check for tornado-specific patterns |
| `sqlalchemy` without web framework | SQLAlchemy ORM | Medium | Likely data layer only |
| `pytest` or `unittest` | Testing framework | High | - |

### JavaScript/TypeScript Frameworks

| Signal | Framework | Confidence | Additional Checks |
|--------|-----------|------------|-------------------|
| `"next"` in package.json deps | Next.js | High | Check for `pages/` or `app/` directory |
| `"react"` in package.json | React | High | Check for JSX files |
| `"vue"` in package.json | Vue.js | High | Check for `.vue` files |
| `"@angular/core"` in package.json | Angular | High | Check for `angular.json` |
| `"express"` in package.json | Express.js | High | Backend framework |
| `"nuxt"` in package.json | Nuxt.js | High | Vue SSR framework |
| `"gatsby"` in package.json | Gatsby | High | Static site generator |
| `"svelte"` in package.json | Svelte | High | Check for `.svelte` files |
| `"nest"` in package.json | NestJS | High | TypeScript backend |

### PHP Frameworks

| Signal | Framework | Confidence | Additional Checks |
|--------|-----------|------------|-------------------|
| `"laravel/framework"` in composer.json | Laravel | High | Check for `artisan` file |
| `"symfony/symfony"` in composer.json | Symfony | High | Check for `bin/console` |
| `"cakephp/cakephp"` in composer.json | CakePHP | High | - |
| `"yiisoft/yii2"` in composer.json | Yii2 | High | - |
| `"codeigniter4/framework"` | CodeIgniter | High | - |

### Ruby Frameworks

| Signal | Framework | Confidence | Additional Checks |
|--------|-----------|------------|-------------------|
| `gem 'rails'` in Gemfile | Ruby on Rails | High | Check for `config/routes.rb` |
| `gem 'sinatra'` in Gemfile | Sinatra | High | Lightweight framework |
| `gem 'hanami'` in Gemfile | Hanami | Medium | - |

### Go Frameworks

| Signal | Framework | Confidence | Additional Checks |
|--------|-----------|------------|-------------------|
| `gin-gonic/gin` in go.mod | Gin | High | Web framework |
| `gorilla/mux` in go.mod | Gorilla Mux | High | Router |
| `echo` in go.mod | Echo | High | Web framework |
| `fiber` in go.mod | Fiber | High | Express-inspired |

### Java Frameworks

| Signal | Framework | Confidence | Additional Checks |
|--------|-----------|------------|-------------------|
| `spring-boot-starter` in pom.xml/build.gradle | Spring Boot | High | - |
| `javax.servlet` dependency | Java Servlet | High | - |
| `quarkus-core` dependency | Quarkus | High | - |
| `micronaut-core` dependency | Micronaut | High | - |

### Flutter/Dart Frameworks

| Signal | Framework | Confidence | Additional Checks |
|--------|-----------|------------|-------------------|
| `flutter` in pubspec.yaml dependencies | Flutter | High | Check for `lib/main.dart`, `android/`, `ios/` directories |
| `sdk: flutter` in pubspec.yaml | Flutter SDK | High | Mobile/web/desktop framework |
| `cupertino_icons` in pubspec.yaml | Flutter iOS | Medium | iOS-specific widgets |
| `provider`, `bloc`, `riverpod` in pubspec.yaml | State Management | Medium | Common Flutter state solutions |
| `get` in pubspec.yaml | GetX | Medium | Flutter navigation/state framework |

### Kotlin Frameworks

| Signal | Framework | Confidence | Additional Checks |
|--------|-----------|------------|-------------------|
| `org.jetbrains.kotlin:kotlin-stdlib` in build.gradle | Kotlin | High | Check for `.kt` files |
| `org.springframework.boot:spring-boot-starter-*` + `.kt` files | Spring Boot (Kotlin) | High | Kotlin-based Spring |
| `io.ktor:ktor-*` in build.gradle.kts | Ktor | High | Kotlin web framework |
| `org.http4k:http4k-*` in dependencies | http4k | High | Kotlin HTTP toolkit |
| `io.micronaut:micronaut-*` + `.kt` files | Micronaut (Kotlin) | High | Kotlin microservices |
| `com.android.application` + `.kt` files | Android (Kotlin) | High | Check for AndroidManifest.xml |
| `androidx.*` dependencies + `.kt` files | Android Jetpack | High | Modern Android development |
| `org.jetbrains.exposed:exposed-*` | Exposed | Medium | Kotlin SQL framework |
| `org.jetbrains.kotlinx:kotlinx-coroutines-*` | Kotlin Coroutines | High | Async programming |

## Architecture Pattern Detection

### Monorepo Patterns

| Signal | Pattern | Confidence | Notes |
|--------|---------|------------|-------|
| `nx.json` present | Nx Monorepo | High | Check for `workspace.json` |
| `turbo.json` present | Turborepo | High | Check for `packages/` directory |
| `lerna.json` present | Lerna | High | Legacy monorepo tool |
| `pnpm-workspace.yaml` | PNPM Workspace | High | - |
| Multiple `package.json` in subdirs | Yarn/NPM Workspace | Medium | Check root package.json for `workspaces` |

### MVC Pattern

| Signal | Pattern | Confidence | Notes |
|--------|---------|------------|-------|
| `models/`, `views/`, `controllers/` dirs | MVC | High | Classic MVC structure |
| Django `models.py`, `views.py` | Django MVC | High | Django convention |
| Rails `app/models/`, `app/views/`, `app/controllers/` | Rails MVC | High | Rails convention |

### Microservices Pattern

| Signal | Pattern | Confidence | Notes |
|--------|---------|------------|-------|
| Multiple service directories with own dependencies | Microservices | High | Each service has package.json/requirements.txt |
| `docker-compose.yml` with multiple services | Containerized Services | High | Check for service definitions |
| `kubernetes/` or `k8s/` directory | K8s Deployment | High | Microservices infrastructure |
| API Gateway pattern (e.g., Kong, Nginx configs) | API Gateway | Medium | - |

### Layered Architecture

| Signal | Pattern | Confidence | Notes |
|--------|---------|------------|-------|
| `presentation/`, `business/`, `data/` dirs | Layered | High | Clean architecture |
| `api/`, `services/`, `repositories/` dirs | Service Layer | High | Common pattern |
| `domain/`, `application/`, `infrastructure/` | DDD | Medium | Domain-Driven Design |

### Event-Driven Architecture

| Signal | Pattern | Confidence | Notes |
|--------|---------|------------|-------|
| Kafka, RabbitMQ, Redis Streams in deps | Event-Driven | High | Message broker present |
| `events/`, `handlers/`, `listeners/` dirs | Event-Driven | Medium | Event-based structure |

## Build Tool Detection

| Signal | Tool | Confidence |
|--------|------|------------|
| `webpack.config.js` | Webpack | High |
| `vite.config.js` | Vite | High |
| `rollup.config.js` | Rollup | High |
| `tsconfig.json` | TypeScript | High |
| `babel.config.js` | Babel | High |
| `Makefile` | Make | High |
| `Dockerfile` | Docker | High |
| `.github/workflows/` | GitHub Actions | High |
| `.gitlab-ci.yml` | GitLab CI | High |
| `.travis.yml` | Travis CI | Medium |

## Database Detection

| Signal | Database | Confidence | Notes |
|--------|----------|------------|-------|
| `psycopg2` or `pg` in deps | PostgreSQL | High | - |
| `mysql-connector` or `mysqlclient` | MySQL | High | - |
| `mongodb` or `pymongo` in deps | MongoDB | High | - |
| `redis` in deps | Redis | High | Cache or data store |
| `sqlite3` usage | SQLite | High | Often dev/test DB |
| `cassandra-driver` | Cassandra | High | - |
| Prisma schema file | Prisma ORM | High | Multi-DB support |
| TypeORM config | TypeORM | High | - |

## Confidence Scoring Criteria

### High Confidence (90-100%)
- Explicit framework dependency in lock file with version
- Framework-specific directory structure matches conventions
- Configuration files present (e.g., `angular.json`, `next.config.js`)
- Multiple confirming signals align

### Medium Confidence (60-89%)
- Framework dependency without version lock
- Partial directory structure match
- One or two confirming signals
- Could be legacy or custom implementation

### Low Confidence (30-59%)
- Framework mentioned in comments or docs only
- Directory structure loosely resembles pattern
- No lock files or explicit configuration
- Might be deprecated or experimental

### Very Low Confidence (<30%)
- Only indirect evidence
- Conflicting signals
- Unusual or custom structure
- Further investigation required

## Testing Framework Detection

| Signal | Framework | Language | Confidence |
|--------|-----------|----------|------------|
| `jest` in package.json | Jest | JS/TS | High |
| `pytest` in requirements | Pytest | Python | High |
| `phpunit` in composer.json | PHPUnit | PHP | High |
| `rspec` in Gemfile | RSpec | Ruby | High |
| `junit` in dependencies | JUnit | Java | High |
| `mocha` + `chai` | Mocha/Chai | JS | High |
| `vitest` in package.json | Vitest | JS/TS | High |

## Common Tech Stack Combinations

### MERN Stack
- MongoDB + Express + React + Node.js
- Signals: `express`, `react`, `mongodb` in package.json

### MEAN Stack
- MongoDB + Express + Angular + Node.js
- Signals: `@angular/core`, `express`, `mongodb` in package.json

### Django Full Stack
- Django + PostgreSQL + Celery + Redis
- Signals: `django`, `psycopg2`, `celery`, `redis` in requirements.txt

### Rails Full Stack
- Rails + PostgreSQL + Sidekiq + Redis
- Signals: Rails in Gemfile, `pg`, `sidekiq`, `redis` gems

### JAMstack
- JavaScript + APIs + Markup (static site)
- Signals: Gatsby/Next.js/Nuxt + headless CMS dependencies
