# Memo: merge forge into craft

**Status:** planned, not executed (2026-06-11). One plugin remains: `craft`.

## Import into craft

- `forge/skills/uiux-design` → craft skill `design` — fills a real gap: spec-template defers visual tokens to `DESIGN.md`, but nothing produces it. Rework to emit `DESIGN.md` (+ optional HTML mockups), same terse style as other craft skills.
- `forge/skills/slides` → craft as-is — self-contained utility (md2pptx script), no overlap.

## Drop or merge with existing

- Skills `ba`, `sa`, `code-explorer`, `code-reviewer` — overlap `prod`/`spec`, `arch`, `whereami`/built-in Explore, and vendor review skills (`/code-review`, `simplify`) respectively.
- Agents `code-reviewer`, `test-generator` — review is delegated to vendor skills; spec mandates the testing approach. Keep `ui-mockup-designer` only if the `design` skill wants a backing agent; otherwise drop.
- Commands `/1`–`/9`, `figma-mockup`, `compare-code`, `forge/templates/*` — the opinionated pipeline; Figma ruled out.

## Mechanics

1. Move the two skills into `craft/skills/`; adapt frontmatter/descriptions.
2. Delete `forge/`; git history preserves it.
3. Remove forge entry from `.claude-plugin/marketplace.json`; bump craft version.
4. Trim root `README.md` to craft-only (drop forge workflow diagram and sections).
5. `/plugin uninstall forge` locally.
