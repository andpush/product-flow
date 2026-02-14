# Product Flow - Claude Code Plugin

This repository contains the `prod-flow` plugin for AI-first product development workflows.

## Repository Structure

```
prod-flow/                    # Plugin directory
├── .claude-plugin/           # Plugin manifest (plugin.json)
├── commands/                 # Slash commands (auto-discovered)
├── agents/                   # Specialized agents (auto-discovered)
├── skills/                   # Skills (auto-discovered)
└── templates/                # Document templates
rules/                        # Reusable coding standards
```

## Plugin Development Conventions

**Skills** (SKILL.md):
- YAML frontmatter: `name`, `description` (required)
- Description format: "This skill should be used when..." (third-person, with trigger phrases)
- Writing style: imperative/infinitive form, not second person
- Keep concise (1,500-2,000 words), move details to `references/`

**Commands** (.md files):
- YAML frontmatter: `name`, `description`
- Auto-discovered from `commands/` directory

**Agents** (.md files):
- YAML frontmatter: `name`, `description`, `model`, `color`
- Auto-discovered from `agents/` directory

## Testing

Test plugin locally:
```bash
cc --plugin-dir /path/to/product-flow/prod-flow
```
