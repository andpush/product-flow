---
description: Compare two codebases (repos or folders): analyse their quality output the winner.
argument-hint: [repo1] [repo2]
skills: code-explorer, code-reviewer
---

Compare two repos:
      - Repo 1: $1
      - Repo 2: $2

Explore code in each repo in parallel, and perform review in several dimentions:
      - Clarity: clear goals, directory structure, self-explaratory namings.
      - Architecture: sensible components decomposition, current tech stack, justified complexity.
      - Code quality: minimal tech debt (code smells, antipatterns, temporary/dirty code), code is readable and maintaibable.
      - Test coverage: tests for all major pieces of functinality.
      - Completeness: no gaps in implementation, not only success path, but forseeable failure scenarious, errors and edge case are properly handled.
      - UX (if applicable): thoughtfulness of UI, ergonomics.

Each dimension estimate in range 0-5 stars. Provide summary table and examples that illustrate the difference between repos. Provide final verdict.
