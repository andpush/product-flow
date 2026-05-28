---
name: prod
description: Use to define the product — WHAT we are building and WHY - the purpose, users, solution, value, constraints, and scope — into a durable PRODUCT.md that `arch` and `spec` rely on.
---

Establish the durable product context — who it's for, what it does, why it matters, what's in and out — either by defining it with the user (greenfield) or deriving it from existing material (brownfield), into a `PRODUCT.md` that the rest of craft builds on.

Run once at project start; again only when the product direction shifts.

`prod` owns the product definition; `arch` consumes it.

For design-led projects `PRODUCT.MD` can be created by the impeccable plugin (https://impeccable.style): `/impeccable teach`.

If a `PRODUCT.md` already exists — from impeccable or by hand — adopt and extend it; never write a second one.

## Detect first

Check for `PRODUCT.md` before creating one. Also check casing/variants like `docs/product.md` to avoid missing existing context: if a variant exists but `PRODUCT.md` does not, use the variant as source material, then create `PRODUCT.md` as the durable craft file and mention the duplicate/rename decision to the user. Read `README.md`, any brief/notes/seed docs the user points to, and `IDEAS.md` if present.

Don't synthesize a product from nothing — interview the user to elicit the product context. If the user provides a product description in the initial request, treat it as a proposed vision to be refined, not the final problem statement.

Use [reference/product-template.md](reference/product-template.md) as a guide for the content and structure of `PRODUCT.md`, adapt as needed.

## Greenfield: define with the user

1. Read whatever seed material exists (brief, notes, README). Treat the initial request as a proposed solution, not the problem.
2. Interview to pin down: the **problem** and **who has it**, the **solution** (the product concept that solves it — not the technical design), the **core value**, the hard **constraints** (tech, budget, timeline, compliance, non-negotiables), and what **success** looks like. Surface assumptions; challenge vague or contradictory answers.
3. Settle **MVP scope**: what ships first vs. what's explicitly deferred. Park non-essential ideas in `IDEAS.md` rather than widening scope.
4. Write `PRODUCT.md` using [reference/product-template.md](reference/product-template.md).

## Brownfield: derive, then confirm

1. Read `README.md`, existing docs, and enough code to infer what the product does and for whom. Verify docs against the code.
2. Draft `PRODUCT.md` describing the product as it *is*; surface gaps, contradictions, or unstated assumptions as findings — don't invent intent.
3. Discuss and confirm with the user, then write `PRODUCT.md`. If `README.md` restates the product, slim it to a pointer.

## Done

Report whether `PRODUCT.md` was created vs. adopted, any open product questions the user must still resolve, and the next step (`arch`). A few lines, no narrative.
