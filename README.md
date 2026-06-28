# Karpathy Agent OS Starter Kit

> Agent OS Kit turns Karpathy-style coding discipline into a reusable operating layer for coding agents: logs, lessons, failure modes, retros, and safe rule improvement proposals.

Based on [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls.

English | [简体中文](./README.zh.md)

---

## The Problem

From Andrej's post:

> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should."

> "They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code."

The deeper problem: most solutions are static. Rules added once, never updated. The same mistakes repeat.

## The Solution

A two-layer system:

1. **Karpathy Guidelines** (4 principles) — coding discipline
2. **Agent OS Core** (operating layer) — log, learn, propose, improve

The key invariant: **Agent OS proposes. You decide. You apply.** No autonomous rule promotion.

## The Loop

```
WORK → error → log to ERROR_LOG.md
  → pattern emerges (2+ errors)
  → /improve → Approval Card issued → STOP
  → you approve → you apply rule manually
  → next WORK: error prevented
```

## Skills

| Skill | Purpose |
|-------|---------|
| `karpathy-guidelines` | Core 4-principle coding discipline |
| `agent-os-core` | Operating rules + error capture protocol |
| `agent-os-prompts` | `/improve`, `/retro`, `/debug`, `/review`, `/plan` |

## Commands

| Command | What it does |
|---------|--------------|
| `/improve` | Analyze logs → classify failure → propose rule → Approval Card → STOP |
| `/retro` | End-of-session retrospective |
| `/debug` | Structured hypothesis-based debugging |
| `/review` | Pre-commit review checklist |
| `/plan` | Task planning with verifiable success criteria |

## Install

**Claude Code Plugin (recommended)**

```
/plugin marketplace add mauricepfeifer-ctrl/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-agent-os
```

**Starter Kit (copy to your project)**

Copy everything from `kits/agent-os-starter-kit/` to your project root.
See `kits/agent-os-starter-kit/README.md` for setup instructions.

**Karpathy Guidelines only (CLAUDE.md)**

```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/mauricepfeifer-ctrl/andrej-karpathy-skills/main/skills/karpathy-guidelines/SKILL.md
```

## Using with Cursor

See [CURSOR.md](./CURSOR.md) for Cursor rules setup.

## Structure

```
andrej-karpathy-skills/
  skills/
    karpathy-guidelines/        # Core 4 principles (standalone, unchanged)
    agent-os-core/              # Operating rules + 8 templates
    agent-os-prompts/           # 5 slash command prompts
  kits/
    agent-os-starter-kit/       # Complete project starter (copy to your project)
```

## License

MIT
