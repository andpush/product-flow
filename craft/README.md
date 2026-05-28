# Craft. From guided discovery to delegated generation.

A lightweight SDD workflow: **prod** -> **arch** -> **spec** -> **build** for:

- guided discovery
- visible decisions
- active conversational steering
- delegated generation
- minimum burnt tokens: no detailed planning unless it changes the outcome

Make expensive decisions visible early: product, architecture, feature design. Capture them in
durable, scannable files so build becomes execution against a clear spec.


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
rule live in `ARCHITECTURE.md`, not in each spec. Decisions go to `ADR.md` by default, or existing
`DECISIONS.md`; deferred ideas go to `IDEAS.md`. Resume any time by reading these files — no
archaeology.

## Usage

Invoke the skills by name in your agent host:

```text
/prod            # define the product with user
/arch            # define the architecture with user
/spec <feature>  # frame a feature into a spec with user
/clear          # clear context
/goal <spec_file> # work on spec till done - unattended.
```
