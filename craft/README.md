# craft

A lightweight engineering workflow: make the decisions that are expensive to get wrong (product,
architecture, feature design) and capture them in durable, scannable files — so the build is just
execution against a clear spec.

Engineering counterpart to the [impeccable](https://impeccable.style) design plugin (which owns
the visual/UX side, `DESIGN.md`).

## Skills

| Skill | Produces |
| --- | --- |
| `prod` | `PRODUCT.md` — purpose, users, value, constraints, MVP scope |
| `arch` | `ARCHITECTURE.md` — components, stack, boundaries, conventions |
| `spec` | `docs/specs/*.md` — one buildable feature spec with verifiable acceptance criteria |

Each works greenfield (define with you) or brownfield (derive from existing code, then confirm),
and adopts existing files rather than clobbering them.

```text
prod → arch → spec → build (/goal, a subagent, or any agent)
```

The spec's acceptance criteria double as the build's stop-condition. Conventions and the decision
rule live in `ARCHITECTURE.md`, not in each spec. Decisions and deferred ideas go to `DECISIONS.md`
and `IDEAS.md` as one-liners. Resume any time by reading these files — no archaeology.

## Usage

Invoke the skills by name in your agent host:

```text
prod            # define the product
arch            # define the architecture
spec <feature>  # frame a feature into a spec
```

For local Claude plugin testing:

```bash
claude --plugin-dir /path/to/craft
```
