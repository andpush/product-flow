---
name: doc-refactor
description: "Refactor document(s) into a single deduplicated, restructured document — removing word-for-word and same-meaning duplication, re-projecting onto a clearer hierarchy, and conserving all content. Triggers: 'merge these docs without duplication', 'remove repeated ideas', 'tighten for agent hand-off'
---

# doc-refactor — consolidate & deduplicate document(s)

Especially apt when merging multiple sources, where cross-document duplication and conflicts are common. The skill decomposes inputs into claims, derives the concerns they serve, dedupes across the union, re-projects, and emits a removed-claims changelog.

## Principles
- **Aim for information density** by cutting *duplicate claims* rather than compress *phrasing*.
- **Hierarchy is a chosen projection.** Duplication is often an artifact of the *wrong* projection — an idea sits in two places because neither is its home. Re-project and the duplicate dissolves. So content (claims) and structure (skeleton) are handled separately.
- **Flag conflicts.** Clarify with user if possible, otherwise fold a `Contradictions found` section.

## Pipeline

1. **Skeletons.** Record each input's heading tree as a separate artifact, tagged by source. Preserved by default — never rebuilt from claims, so structure can't dissolve silently.
2. **Decompose → claims.** Break inputs into atomic claims; split conjoined assertions ("fast **and** secure" → two). Each claim carries: `id`, `text` (short paraphrase, no long verbatim spans), `source`, `address` (path in its skeleton), `scope` (qualifier bounding its truth). No concern tags yet.
3. **Concern basis.** Cluster claims *across all inputs* into concerns; tag each claim with its concern-**set**. One basis spans the union — this is what catches cross-document repeats.
4. **Detect duplicates.** Cluster by *meaning*; classify per the taxonomy below. Operative test is **same claim, same scope** — never surface similarity alone.
5. **CHECKPOINT (human).** Present the concern basis + a proposed target structure (as a diff against the input skeletons) for approval before any rewrite. Skip only if explicitly told the run is unattended — an agent approving its own projection re-introduces the black box.
6. **Reconstruct.** Build the approved structure: each claim gets **exactly one** home; cross-cutting claims get one home + a cross-reference (not a copy); scope-distinct pairs keep both. Flatten to **≤3 heading levels** (`#`/`##`/`###`) + lists; a needed 4th level signals a sibling section or its own doc. Restate a constraint at its point of use *only* to kill a long-range dependency, and mark it intentional.
7. **Changelog.** List every removed/merged claim (id + reason: verbatim / semantic / merged-into `Cxxx`) and an old→new address map for survivors.

## Duplicate taxonomy

| Class | Test | Verdict |
|---|---|---|
| Verbatim | Identical wording | Cut — keep one |
| Semantic | Same claim, same scope, different words | Cut — keep one canonical *(the class LLMs miss)* |
| Cross-cutting | Same claim serves multiple concerns/sections | Keep — one home + cross-reference |
| Point-of-use | Constraint restated where applied, killing a long-range dependency | Keep + mark intentional |
| Scope-distinct | Similar text, **different scope** | Keep both — not a duplicate |
| Conflict | Same claim slot, **incompatible values** across sources | Keep both — flag for human resolution |

## Constraints
- **Preservation invariant:** every input claim appears in the output **or** the changelog. Nothing leaves silently. (A claim in neither is a defect.)
- **No fabrication:** every output claim traces to an input claim.
- **Cut claims, not phrasing:** length drops by removing duplicates, not by cramming clauses.
- Depth cap is a *step-6* heuristic, not a decomposition rule — capture true structure however deep in steps 1–4.
- Don't assume orthogonal concerns; don't exceed the approved projection (flag, don't act).
- On any multi-pass run, reconstruct from the **written** artifacts, not conversation memory.

## VERIFY (fresh context, advisory)
Run separately with **only** the input document(s), the output, and the changelog — no decomposition notes. The empty context prevents grading one's own homework. Three mechanical checks:
1. **Claim conservation** — every input claim is in the output or changelog.
2. **Reverse-duplication** — re-run steps 2–4 on the output; surviving verbatim/semantic clusters mean dedup failed.
3. **No-fabrication** — every output claim has a source.