---
name: doc-refactor
description: "Refactor document(s) into a single deduplicated, restructured document — removing word-for-word and same-meaning duplication, re-projecting onto a clearer hierarchy, and conserving all content. Triggers: 'merge these docs without duplication', 'remove repeated ideas', 'tighten for agent hand-off'."
---

# doc-refactor — consolidate & deduplicate document(s)

Decompose inputs into claims, cluster the concerns they serve, dedupe across the union, re-project, and report what was removed. Most valuable when merging multiple sources, where duplication and conflicts cluster.

## Principles
- **Density by cutting duplicate claims**, not by compressing phrasing.
- **Hierarchy is a projection.** Duplication is often an artifact of the *wrong* one — an idea sits in two places because neither is its home; re-project and the duplicate dissolves. So handle content (claims) and structure (skeleton) separately. Re-projection is a tool, not a goal: keep the input skeleton unless duplication or misplacement forces a change.
- **Flag conflicts** — ask the user if you can.

## Pipeline
1. **Skeletons.** Record each input's heading tree as a separate artifact, tagged by source. Never rebuilt from claims, so structure can't dissolve silently.
2. **Decompose → claims.** Break inputs into atomic claims; split conjunctions ("fast **and** secure" → two). Each carries `id`, `text` (short paraphrase, no long verbatim spans), `source`, `address` (path in its skeleton), `scope` (qualifier bounding its truth). No concern tags yet.
3. **Concern basis.** Cluster claims *across all inputs* into concerns; tag each with its concern-**set**. One basis over the union is what catches cross-document repeats.
4. **Detect duplicates.** Cluster by *meaning*; classify per the taxonomy. Test is **same claim, same scope** — never similarity alone.
5. **CHECKPOINT (human).** Present the concern basis + proposed structure (as a diff against the input skeletons) before any rewrite. Skip only if told the run is unattended — an agent approving its own projection re-introduces the black box.
6. **Reconstruct.** Default to the input skeleton; change it only where step 4 forces it. Each claim gets **exactly one** home; scope-distinct pairs keep both. A second mention of a cross-cutting claim is a **pointer** ("because Postgres is the source of truth — see Data model"), never a restatement; restating is the point-of-use case below, not a license from thematic overlap. Flatten to **≤3 heading levels** + lists; a needed 4th signals a sibling section or its own doc.
7. **Report.** In your reply (not a file), list each removed/merged claim with a one-word reason — verbatim / semantic / merged / out-of-scope. That's it.

## Duplicate taxonomy
| Class | Test | Verdict |
|---|---|---|
| Verbatim | Identical wording | Cut — keep one |
| Semantic | Same claim, same scope, different words | Cut — keep one canonical *(the class LLMs miss)* |
| Cross-cutting | Same claim serves several sections | Keep — one home; every other mention is a **pointer** |
| Point-of-use | Restated to kill a *long-range* dependency a reader can't otherwise follow | Keep + mark intentional — relevance alone doesn't qualify |
| Scope-distinct | Similar text, **different scope** | Keep both — not a duplicate |
| Conflict | Same slot, **incompatible values** | Keep both — flag for human |

## Constraints
- **Preservation invariant:** every input claim is in the output **or** the removed-claims report — nothing leaves silently. Lossless by default; if the user scopes the output (audience, length, relevance), out-of-scope claims go to the report, not the void.
- **No fabrication:** every output claim traces to an input claim.
- Depth cap is a step-6 heuristic, not a decomposition rule — capture true structure however deep in steps 1–4.
- Don't assume orthogonal concerns; don't exceed the approved projection (flag, don't act).
- On multi-pass runs, reconstruct from the **written** artifacts, not memory.

## VERIFY (subagent, fresh context)
Spawn a subagent given **only** the inputs, output, and removed-claims report — no decomposition notes, so it can't grade its own homework.
1. **Reconstruction** — a fresh agent can regenerate every input claim from the output + report alone (present-but-dead claims fail this).
2. **Reverse-duplication** — re-run steps 2–4 on the output; surviving verbatim/semantic clusters mean dedup failed.
3. **No-fabrication** — every output claim has a source.
