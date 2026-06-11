# Product Flow

Product development workflow for agentic development. From idea to production.

This repo ships two plugins:

- **`craft`** *(recommended)* — a lightweight engineering workflow (`prod` → `arch` → `spec`). Best for most projects.
- **`forge`** — the heavyweight, full-ceremony workflow documented below (staged `/1`–`/9` commands). Reach for it when you want the full structured process.

## Installation

```claude
/plugin marketplace add andpush/product-flow
/plugin install craft     # recommended
/plugin install forge     # heavyweight, full workflow
```

It is recommended to have these skills configured:
    - simplify
    - code-review
    - playwright-cli

## `Craft` plugin workflow

You delegate the coding, not the decisions. Fast generation hides early mistakes — wrong data model, accidental boundaries. Craft surfaces expensive-to-undo decisions while they're cheap to change, recommends, lets you steer. Token-frugal: no planning that doesn't change the outcome, no questionnaire theatre.

Core flow: `prod` → `arch` → `spec` → build. Alongside:

1. Call `prod` to collaboratively create (or update) `PRODUCT.md` that is required for further steps. You can also use other skills like `impeccable teach` from https://impeccable.style/, or create it manually. One time, so prefer bigger models/thinking efforts, e.g. Opus/high.
2. Call `arch` to collaboratively create (or update) `ARCHITECTURE.md` that is required for further steps. One time, so prefer bigger models/thinking efforts, e.g. Opus/high.
3. Call `spec` to collaboratively create a solution spec that is ready for the execution. Prefer medium models/efforts combinations: Opus/low, Sonnet/medium, GPT-5.5/medium.
4. Use built-in `/goal` command in a new/clean session to implement the spec till completion. You can use faster models here (Sonnet/low, Gemini 3.5 Flash). This session usually can work unattended or in a headless subagent as long as permissions are granted or auto mode is on.

At any point:

- `idea` — park a hunch in `docs/ideas/`; `spec` validates on pickup (pursue / defer / reject).
- `whereami` — reorient after a break: where you stopped, what's parked, what's next.

Memory is scannable files, not prose: `PRODUCT.md`, `ARCHITECTURE.md`, `docs/specs/`, `docs/ideas/`, `docs/adr/` — one file per spec/idea/decision, filenames are the index. Details: [craft/README.md](craft/README.md).

Optionally you can run `simplify` or `review` skill (not included, use from any vendor you trust) in a clear context to ensure code quality and reuse. Having context cleared helps remove creator bias, using a different model (e.g. GPT-5.5) helps as well.

## `Forge` plugin workflow

`forge` guides you through more structured product development:

```text
┌──────────────────┐     ┌──────────────────┐     ┌──────────────────────────┐
│ Your vision docs │     │ /1-define-product│     │ /2-mockup-product        │
│ docs/**          │────▶│ PRODUCT.md       │────▶│ mockups/ (optional)      │
└──────────────────┘     └───┬──────────────┘     └──────────────────────────┘
                             │
                     ┌───────┴──────────┐
                     ▼                  ▼
         ┌────────────────────────┐  ┌────────────────────────┐
         │ /3-define-architecture │  │ /4-add-mvp-features     │
         │ ARCHITECTURE.md        │  │ features/F001-*/        │
         └────────────────────────┘  │ feature.md              │
                                      └───────┬─────────────────┘
                                             │
                                             ▼
                                  ┌─────────────────-----------─┐
                                  │ /6-mockup-feature           │
                                  │ F001-*/mockups/ (optional)  │
                                  └────────┬───────-----------──┘
                                           │
                                           ▼
                                  ┌─────────────────────┐
                                  │ /7-plan-feature     │
                                  │ F001-*/plan.md      │
                                  └────────┬────────────┘
                                           │
                                           ▼
                                  ┌──────────────────────┐
                                  │ /8-implement-feature │
                                  │ feature branch       │
                                  │ code + tests         │
                                  └────────┬─────────────┘
                                           │
                                           ▼
                                  ┌───────────────────┐
                                  │ /9-review-feature │
                                  │ F001-*/review.md  │
                                  └───────────────────┘
```

## Quick Start Example

**1. Create your vision documents:**
```bash
mkdir -p docs
# Add your product vision, requirements, user research...
```

**2. Define your product:**
```claude
/1-define-product my-startup
```
Creates `PRODUCT.md` with structured specs: problem, solution, features, success metrics.

**3. Design UI mockups:**
```claude
/2-mockup-product
```
Generates interactive HTML mockups in `mockups/`.

**4. Define architecture:**
```claude
/3-define-architecture
```
Creates `ARCHITECTURE.md` with tech stack, components, data model, deployment plan.

**5. Break down into features:**
```claude
/4-add-mvp-features
```
Generates feature specs in `features/F001-*/feature.md`.

**6. Plan a feature:**
```claude
/7-plan-feature F001-UserAuth
```
Creates implementation plan in `features/F001-UserAuth/plan.md`.

**7. Build the feature:**
```claude
/8-implement-feature F001-UserAuth
```
Creates feature branch, implements code and tests.

**8. Review the code:**
```claude
/9-review-feature F001-UserAuth
```
Generates comprehensive review in `features/F001-UserAuth/review.md`.

## What Gets Created

`forge` reads your input from `docs/` and writes generated artifacts to the project root:

```text
docs/                    # Your input: vision, requirements, research (any structure)
PRODUCT.md               # Generated: structured product definition
ARCHITECTURE.md          # Generated: tech stack, components, data model
mockups/                 # Generated: product-level UI mockups (HTML)
features/
└── F001-*/
    ├── feature.md       # Generated: feature specification
    ├── plan.md          # Generated: implementation plan
    ├── review.md        # Generated: code quality review
    └── mockups/         # Generated: feature-level UI mockups
```

## Skills & Agents

**Skills** (invoke with "use the X skill"):

- `ba` - Business analysis and requirements decomposition
- `sa` - Software architecture design
- `code-explorer` - Codebase exploration and understanding
- `code-reviewer` - Code quality review and improvements
- `slides` - Create presentation decks from markdown
- `uiux-design` - UI/UX design expertise

**Agents** (autonomous specialists):

- `code-reviewer` - Automated code review agent
- `test-generator` - Test generation agent
- `ui-mockup-designer` - UI mockup design agent

## License

MIT
