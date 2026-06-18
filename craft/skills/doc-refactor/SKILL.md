---
name: doc-refactor
description: "Refactor document(s) into a single deduplicated, restructured document — preserving contained knowledge. Triggers: 'merge docs A, B, C -> B without duplication', 'remove repeated ideas', 'tighten for agent hand-off'."
---

# doc-refactor — document normalization

Normalize a document by cutting word-for-word and same-meaning duplication, and re-projecting onto a clearer hierarchy, while preserving all content.

Most valuable when:
- merging multiple sources
- normalizing source with repeated ideas
- preparing a document for hand-off to another agent (human or LLM) that will need to understand it without reading the inputs.

Inspired by ML concept of feature extraction, applied to human knowledge. As Autoencoder reduce dimensionality preserving required features, we need to hand-off minimal document preserving required knowledge dimensions.

User specifies a set of input documents, output document and (optionally) the goal. If the goal is not specified and not clear from the context or user motives, work in lossless mode - preserve all knowledge found.

How it works:
- decompose the inputs into claims,
- cluster the concerns,
- dedupe across the union,
- re-project onto a clearer structure.

The result is a denser, more navigable document that still contains all the original knowledge.


## Principles
- **Terse, pragmatic tone.** But do not overcompress phrasing: achieve density by cutting duplicate claims.
- **Hierarchy is a projection.** Duplication is often an artifact of the *wrong* one — an idea sits in two places because neither is its home; re-project and the duplicate dissolves. So handle knowledge claims and structure (skeleton) separately. If no misplacement - keep the input structure. Unsure - ask the user.
- **Flag conflicts** — ask the user if possible.
- Don't assume orthogonal concerns; don't exceed the approved projection (flag, don't act).
- On multi-pass runs, reconstruct from the **written** artifacts, not memory.

## Pipeline
1. **Skeletons.** Record each input's heading tree as a separate artifact, tagged by source. Never rebuilt from claims, so structure can't dissolve silently.
2. **Decompose → claims.** Break inputs into atomic claims; split conjunctions ("fast **and** secure" → two). Each carries `id`, `text` (short paraphrase, no long verbatim spans), `source`, `address` (path in its skeleton), `scope` (qualifier bounding its truth). No concern tags yet.
3. **Concern basis.** Cluster claims *across all inputs* into concerns; tag each with its concern-**set**. One basis over the union is what catches cross-document repeats.
4. **Detect duplicates.** Cluster by *meaning*; classify per the taxonomy. Test is **same claim, same scope** — never similarity alone.
5. **CHECKPOINT (human).** Present the concern basis + proposed structure (as a diff against the input skeletons) before any rewrite. Skip only if told the run is unattended — an agent approving its own projection re-introduces the black box.
6. **Reconstruct.** Default to the input skeleton; change it only where step 4 forces it. Flatten to **≤4 heading levels** + lists; a needed 5th signals a sibling section or its own doc, tell the user. Each claim gets **exactly one** home; scope-distinct pairs keep both. The **Intro/Overview is a home like any other**. A second mention of a cross-cutting claim is a **pointer** (e.g.: "... — see `Data model`"), never a restatement.
7. **Report.** Produce a removed-claims report containing every claim not present in the final document, with `source`, original `address`, `disposition`, and a short reason. Allowed dispositions: `verbatim`, `semantic`, `merged`, `conflict`, `out-of-scope`. Also report summary statistics: compression %, total input claims, duplicate counts by category, and total output claims. Flag separately: claims that changed home.

## Duplicate taxonomy
| Class | Test | Verdict |
|---|---|---|
| Verbatim | Identical wording | Cut — keep one |
| Semantic | Same claim, same scope, different words | Cut — keep one canonical |
| Cross-cutting | Same claim serves several sections | Keep — one home; every other mention is a **pointer** |
| Reader-aid | Avoids a long-range dependency or misreading in rare cases | As an exception - keep shortened + point to full claim |
| Scope-dependnent | Similar, but **different scope** changes it's meaning | Keep both — not a duplicate |
| Conflict | Same slot, **incompatible values** | Ask user which holds true, or cut both and flag in the report |

## VERIFY (subagent, fresh context)
Spawn a subagent given **only** the inputs, output, and removed-claims report — no decomposition notes, so it can't grade its own homework.
1. **Reconstruction** — a fresh agent can regenerate every input claim from the output + report alone (present-but-dead claims fail this).
2. **Reverse-duplication** — re-run steps 2–4 on the output; surviving verbatim/semantic clusters mean dedup failed.
3. **No-fabrication** — every output claim traces to an input claim.
