---
description: Explore unfamiliar codebase
allowed-tools: Read, Write, Bash, Glob
---
# Explore Code Command

Analyze this repository as a senior engineer preparing to contribute.

## Tasks

1. **Structure Analysis**
   - Scan config files, build scripts, directory layout → identify tech stack, modules, dependencies
   - Check docs (note staleness)

2. **Code Analysis**
   - Entry points, APIs, data flow
   - Core entities, dependencies, component interactions

3. **Generate `repo-overview-NNN.md`**

   ### Core Functionality

   Purpose, problem solved, key features

   ### Architecture

   Components with reposponsibilities (table format)
   Tech stack per layer (Languages, Frameworks, Infrastructure)
   Mermaid diagrams: C4 / system structure / sequence / data flow

   ### Development Practices

   Build/test commands, CI/CD, deployment

   ### Actionable Improvements

   Code-based issues only (no generic advice):

   |Priority|Category|Location|Issue|Suggested Fix|
   |---|---|---|---|---|
   |P0-P2|Security/Perf/Maintain/Stability|file:line|specific finding|concrete action|
