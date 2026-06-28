---
name: agent-os-core
description: Agent OS Core — operating rules for AI-assisted coding. Logs errors, identifies failure modes, extracts lessons, and proposes rule changes. All rule promotions require human approval. Built on Karpathy Guidelines.
license: MIT
---

# Agent OS Core

Operating layer for AI-assisted coding agents. Transforms one-off corrections into systematic improvement — with human approval at every step.

**Relationship to Karpathy Guidelines:** Karpathy Guidelines define coding discipline (how to write code). Agent OS Core defines operating discipline (how to work, log, learn, and improve). They stack; neither weakens the other.

---

## Purpose

- Log errors and decisions as they happen
- Identify recurring failure modes from error patterns
- Extract verified lessons from failures
- Propose rule changes for human review
- Track what changed, why, and when

## When to Use

- When starting work in a project using Agent OS
- When an error occurs and needs to be captured
- When preparing a `/improve` or `/retro` run
- When reviewing patterns across sessions

## When NOT to Use

- Do not use to bypass or weaken Karpathy Guidelines
- Do not log private, legal, or secret data
- Do not use to auto-promote rules without human approval
- Do not run autonomously without human oversight

---

## Required Inputs

- Project working directory
- `ERROR_LOG.md` (or empty on first session)
- `LESSONS_LEARNED.md` (or empty)
- `DECISION_LOG.md` (or empty)
- `FAILURE_MODES.md` (or empty)
- Current task context

## Output Artifacts

- Updated `ERROR_LOG.md` (new entries appended)
- Updated `DECISION_LOG.md` (decisions captured)
- `RULE_CHANGE_PROPOSAL.md` (proposals only — never applied automatically)
- Updated `SELF_IMPROVEMENT_LOOP.md` (current loop state)

---

## Core Rules

1. **Errors are logged.** Every mistake captured in `ERROR_LOG.md` immediately.
2. **Recurring errors become Failure Modes.** Same root cause 2+ times → entry in `FAILURE_MODES.md`.
3. **Lessons require verification.** No lesson is final until a human confirms it.
4. **Rule changes are proposed, not applied.** `RULE_CHANGE_PROPOSAL.md` only.
5. **No autonomous rule promotion.** Human approval required before any rule enters `CLAUDE.md` or `AGENTS.md`.
6. **No private/legal/secret data in logs.** Sanitize before writing.
7. **No changes to productive configs.** `CLAUDE.md`, `AGENTS.md`, Hermes/OpenClaw configs are read-only without explicit human approval.
8. **Karpathy Guidelines are never weakened.** Agent OS extends them; never replaces or dilutes them.

---

## Error Capture Format

When an error occurs, append to `ERROR_LOG.md`:

```
## [YYYY-MM-DD] [CATEGORY]
**Task:** [what were you working on]
**What happened:** [observable mistake]
**What should have happened:** [correct behavior]
**Root cause hypothesis:** [your best guess]
**Proposed lesson:** [what rule might prevent this]
**Status:** OPEN
```

Categories: `ASSUMPTION` | `COMPLEXITY` | `SCOPE_CREEP` | `WRONG_TOOL` | `MISSED_CONTEXT` | `PLANNING` | `OTHER`

## Failure Mode Promotion

When the same root cause appears 2+ times in `ERROR_LOG.md`:

1. Create or update entry in `FAILURE_MODES.md`
2. Link source error entries
3. Flag for `/improve` review
4. Do NOT auto-update `CLAUDE.md`

## Human Approval Rules

Before any rule enters productive configs:

1. `RULE_CHANGE_PROPOSAL.md` must contain the exact proposed change
2. Risk assessment must be documented
3. Human must respond: `APPROVED` / `REJECTED` / `DEFER`
4. Only after `APPROVED`: human manually applies the change

## Failure Mode Handling

If this skill produces uncertain output:
- Stop and report: "Agent OS Core uncertain. Human review required."
- Do not proceed with rule promotion
- Log the uncertainty to `ERROR_LOG.md`

## Rule Promotion Policy

```
ERROR_LOG.md (capture)
  → FAILURE_MODES.md (pattern: 2+ occurrences)
  → LESSONS_LEARNED.md (lesson drafted and human-verified)
  → RULE_CHANGE_PROPOSAL.md (exact patch proposed)
  → Human APPROVED
  → Human manually applies to CLAUDE.md / AGENTS.md
  → CHANGELOG_AGENT.md updated
```

No step can be skipped. No step is automated past "proposal."
