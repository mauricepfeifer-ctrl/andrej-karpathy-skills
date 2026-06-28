# Karpathy Agent OS — Starter Kit

**Agent OS Kit turns Karpathy-style coding discipline into a reusable operating layer for coding agents: logs, lessons, failure modes, retros, and safe rule improvement proposals.**

---

## What This Kit Is

A complete project starter for teams using Claude Code, Cursor, or other AI coding agents. It combines:

1. **Karpathy Guidelines** — coding discipline (4 core principles)
2. **Agent OS Core** — operating discipline (log, learn, propose — never auto-apply)
3. **Tracking Files** — structured logs for errors, decisions, lessons, and failure modes
4. **Slash Commands** — `/improve`, `/retro`, `/debug`, `/review`, `/plan`

## Who Should Use This

- Developers using Claude Code or Cursor on real projects
- Teams who want AI agent work to improve over time, not repeat the same mistakes
- Anyone tired of correcting the same AI errors session after session

## The Core Loop

```
You work
  → AI makes a mistake
  → you log it to ERROR_LOG.md
  → 2+ similar mistakes → FAILURE_MODES.md
  → run /improve
      → patterns identified
      → lesson drafted
      → rule proposed in RULE_CHANGE_PROPOSAL.md
      → Approval Card issued
      → STOPS
  → you approve
  → you manually apply rule to CLAUDE.md / AGENTS.md
  → next session: error prevented
```

## Why No Autonomous Rule Promotion

AI agents must not self-modify their own operating rules without oversight:
- Rule conflicts go undetected
- Audit trail is lost
- Trust in the system erodes

**Agent OS proposes. You decide. You apply.**

## Files in This Kit

| File | Purpose |
|------|---------|
| `CLAUDE.md` | Coding + operating rules (pre-filled, customize for your project) |
| `AGENTS.md` | Agent operating instructions |
| `ERROR_LOG.md` | Error capture (write here when mistakes happen) |
| `LESSONS_LEARNED.md` | Human-verified lessons from processed errors |
| `DECISION_LOG.md` | Non-obvious decisions with reasoning |
| `FAILURE_MODES.md` | Recurring error patterns (2+ occurrences) |
| `RULE_CHANGE_PROPOSAL.md` | Proposals from `/improve` — never auto-applied |
| `SELF_IMPROVEMENT_LOOP.md` | Loop state and version history |

## How to Install

1. Copy all files from this kit to your project root
2. Install the Claude Code plugin (see main repo README)
3. Customize `CLAUDE.md` with your project-specific rules
4. Start working
5. Log errors as they occur
6. Run `/improve` when you have 3+ open errors

## How It Works with Karpathy Guidelines

| Layer | What it covers |
|-------|----------------|
| Karpathy Guidelines (rules 1–4) | How to write code |
| Agent OS Core (rule 5 + infrastructure) | How to operate as an agent over time |

They stack. Karpathy Guidelines cannot be weakened by any Agent OS update.

## Safety Boundaries

- No private, legal, or secret data in any log file
- No automatic rule promotion
- No changes to external configs without approval
- Human approval required for every rule change
- Karpathy Guidelines always preserved

## License

MIT
