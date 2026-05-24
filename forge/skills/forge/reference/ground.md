# forge ground

Establish the durable engineering context for a project. Run once at the start, and again only
when the foundations change.

## Roles and their homes

Map these five roles to files. Use the repo's existing filenames if present; otherwise the default.

| Role | Holds | Default file | Owner |
|---|---|---|---|
| Product | purpose, users, constraints | `PRODUCT.md` | impeccable — don't author here |
| Architecture | components, stacks, boundaries, layout, entrypoints | `ARCHITECTURE.md` | `ground`'s output |
| Conventions | how code is written, per stack | `rules.md` (+ `rules-<stack>.md`) | `ground` |
| Decisions | why choices were made | `ADR.md` \| `DECISIONS.md` | appended over time |
| Front door | human onboarding | `README.md` | human; read as a source |

`ARCHITECTURE.md` is the canonical contract `frame`/`build`/`review` rely on. Keep each fact in one
file; README links to `ARCHITECTURE.md` for structure rather than restating it.

## Detect first

Map roles to existing files before creating any: check casing/variants — `ARCHITECTURE.md` /
`docs/architecture.md`, `rules*.md` / `CONVENTIONS.md` / `STYLE.md`, `ADR.md` / `DECISIONS.md` /
`docs/adr/*`, plus `README.md`, `PRODUCT.md`, `CLAUDE.md`, `AGENTS.md`. Adopt the repo's names;
only fall back to defaults for roles with no home.

## Greenfield: define with the user

1. Read `PRODUCT.md` for purpose, users, constraints.
2. Propose architecture and stack — proven over trendy, complexity matched to the problem. Present
   real forks (monolith vs. services, datastore, etc.) as pro/contra via `AskUserQuestion`; don't
   bikeshed settled defaults.
3. Write `ARCHITECTURE.md` using [architecture-template.md](architecture-template.md).
4. Write `rules.md` from the matching seed in [stacks/](stacks/): read it, adapt with the user,
   keep only conventions that aren't obvious or that this project deviates on. Include the standing
   decision rule (below).
5. Record macro decisions tersely — see [decisions.md](decisions.md).

## Brownfield: derive from the code, then confirm

1. Explore build files, layout, entry points, data layer, external calls. Read `README.md` as a
   source but verify it against the code.
2. Draft `ARCHITECTURE.md` ([architecture-template.md](architecture-template.md)) describing the
   system as it *is*.
3. Surface questionable parts (dead seams, inconsistent patterns, risky deps) as findings — don't
   discard working decisions.
4. Confirm with the user, then write `ARCHITECTURE.md` and any `rules*.md` matching the conventions
   the code follows. If README restates structure, slim it to a pointer to `ARCHITECTURE.md`.

## Conventions: split only when warranted

Start with one `rules.md`. Split into `rules-<stack>.md` when a second stack appears, not by reflex.
A component declares which convention files apply.

Plant this standing rule in the conventions file (it then applies in `build`/`review`/ad-hoc work):

> On any architectural choice: surface the trade-off, prefer the simpler option, challenge a weak
> default, and record the decision in `ADR.md`/`DECISIONS.md`.

## Wire CLAUDE.md / AGENTS.md

Ensure both exist as thin pointers — never copy bulk in. Keep their existing style if present:

```markdown
# Project context
Read `./ARCHITECTURE.md` for components, stacks, and layout.
Read `./rules.md` (and any `rules-<stack>.md`) for conventions.
Read `./README.md` for the overview, `./ADR.md` for decision history.
```

## Done

Report which role mapped to which file (created vs. adopted) and the next step
(`forge frame <first feature>`). A few lines.
