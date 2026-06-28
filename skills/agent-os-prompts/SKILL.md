---
name: agent-os-prompts
description: Agent OS Prompts — slash-command and prompt templates for structured agent work. Provides /improve, /retro, /debug, /review, /plan. All prompts are analysis and proposal only — no productive configs are changed automatically.
license: MIT
---

# Agent OS Prompts

Executable prompt and slash-command layer for Agent OS. Structured templates that turn agent work into systematic learning.

**Safety constraint:** Every prompt in this collection is analysis and proposal only. No prompt may automatically modify `CLAUDE.md`, `AGENTS.md`, Hermes rules, OpenClaw configs, or any productive configuration.

---

## Available Prompts

| Prompt | Trigger | Purpose |
|--------|---------|--------|
| `improve.md` | `/improve` | Analyze logs → classify failure → propose rule change → Approval Card → STOP |
| `retro.md` | `/retro` | End-of-session retrospective |
| `debug.md` | `/debug` | Structured hypothesis-based debugging |
| `review.md` | `/review` | Code and decision review |
| `plan.md` | `/plan` | Task planning with explicit success criteria |

## Rules for All Prompts

1. Prompts may read any project log file
2. Prompts may generate proposals, patches, and approval cards
3. Prompts may NOT write to `CLAUDE.md`, `AGENTS.md`, or productive configs
4. Every proposal must include a Risk Check section
5. Every proposal must end with an explicit Approval Question before stopping
6. When uncertain, prompts stop and ask — they do not proceed

## How to Add New Prompts

1. Create `skills/agent-os-prompts/prompts/[name].md`
2. Define: purpose, inputs, steps, output format, approval requirement
3. Add to the table above in this SKILL.md
4. Test with real `ERROR_LOG.md` data before using in production
