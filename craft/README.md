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

## Well known files

| File | Holds | Created by |
|---|---|---|
| `PRODUCT.md` | purpose, users, constraints | `prod` (or `/impeccable teach`) |
| `ARCHITECTURE.md` | components, stacks, boundaries, layout, entrypoints, conventions |  this `arch` skill or manually |
| `ADR.md` \| `DECISIONS.md` | why choices were made | appended over time |
| `IDEAS.md` | parked ideas, future scope, items needing elaboration | appended over time |
| `README.md` | human onboarding | human; read as a source |
| `CLAUDE.md` \| `AGENTS.md` | onboarding for agents | `arch` skill or manually |

## Usage

Invoke the skills by name in your agent host:

```text
/craft:init      # small project: run prod then arch in one scaled-down session
/prod            # define the product with user
/arch            # define the architecture with user
/spec <feature>  # frame a feature into a spec with user
/clear          # clear context
/goal <spec_file> # work on spec till done - unattended.
```

`/craft:init` is a convenience macro for small/fresh projects — it just chains `prod` then `arch`.
For larger or evolving projects, run `/prod` and `/arch` separately so each can be revisited on its own.
