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
| `spec` | `docs/specs/*.md` — one buildable feature spec with verifiable acceptance criteria (archived to `docs/specs/done/` once `done`) |
| `idea` | `docs/ideas/*.md` — one-file idea capture with a quick PRODUCT.md alignment check |
| `audit` | `docs/audit-YYYY-MM-DD.md` — deep repo health check: structure, maintainability, security |
| `whereami` | report — reorient after a break: current focus, parked ideas, next step |

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
| `docs/adr/*.md` | why choices were made, one decision per file | `arch`/`spec` skills, over time |
| `docs/ideas/*.md` | idea backlog, one file per idea (images beside) — unvalidated candidates, not commitments; optional `priority: high\|low` (set at capture or during triage) steers `whereami`; `spec` validates on pickup (pursue / defer / reject); closed ideas (pursued/rejected) move to `docs/ideas/done/`; delete a file to drop an idea | `idea` skill or manually |
| `docs/audit-YYYY-MM-DD.md` | repo health snapshot — findings, quality scores, action items | `audit` skill |
| `README.md` | human onboarding | human; read as a source |
| `CLAUDE.md` \| `AGENTS.md` | onboarding for agents | `arch` skill or manually |

## Usage

Invoke the skills by name in your agent host:

```text
/craft:init      # small project: run prod then arch in one scaled-down session
/prod            # define the product with user
/arch            # define the architecture with user
/spec <feature>  # frame a feature into a spec with user
/idea <hunch>    # capture an idea into docs/ideas/, checked against PRODUCT.md
/audit           # deep repo health check; writes docs/audit-YYYY-MM-DD.md
/whereami        # reorient: current focus, parked ideas, next step
/clear           # clear context
/goal <spec_file> # work on spec till done - unattended.
```

`/craft:init` is a convenience macro for small/fresh projects — it just chains `prod` then `arch`.
For larger or evolving projects, run `/prod` and `/arch` separately so each can be revisited on its own.
