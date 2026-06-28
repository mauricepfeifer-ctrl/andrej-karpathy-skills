# Karpathy Agent OS Starter Kit

> Stop collecting AI knowledge. Install a system that applies it, measures results, and learns from mistakes.

Based on [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls — extended with a self-improving loop.

**The core invariant:**
> A mistake is only processed when the system prevents it next time.

---

## The Problem

From Andrej's post:

> "The models make wrong assumptions on your behalf and just run along with them without checking. They don't manage their confusion, don't seek clarifications, don't surface inconsistencies, don't present tradeoffs, don't push back when they should."

> "They really like to overcomplicate code and APIs, bloat abstractions, don't clean up dead code."

> "They still sometimes change/remove comments and code they don't sufficiently understand as side effects."

The deeper problem: most solutions to this are **static**. You add rules to CLAUDE.md once. The rules don't update when new mistakes happen. You keep correcting the same errors.

## The Solution

A system that improves itself:

```
WORK → error occurs → /improve → rules updated → error prevented next time
```

### 5 Principles

| # | Principle | Addresses |
|---|-----------|----------|
| 1 | **Think Before Coding** | Wrong assumptions, hidden confusion |
| 2 | **Simplicity First** | Overcomplication, bloated abstractions |
| 3 | **Surgical Changes** | Orthogonal edits, touching code you shouldn't |
| 4 | **Goal-Driven Execution** | Leverage through verifiable success criteria |
| 5 | **Self-Improvement Loop** | Repeating the same mistakes |

### 3 Commands

| Command | What it does |
|---------|-------------|
| `/setup` | Initializes Agent OS tracking files in your project |
| `/improve` | Analyzes ERROR_LOG.md, proposes rule updates, applies them |
| `/solve` | Structured hypothesis loop for debugging and problem-solving |

### 6 Tracking Files

Installed in your project root by `/setup`:

| File | Purpose |
|------|---------|
| `ERROR_LOG.md` | Raw error captures |
| `LESSONS_LEARNED.md` | Distilled lessons from processed errors |
| `RULE_UPDATE_LOG.md` | History of every rule change |
| `IMPROVEMENT_BACKLOG.md` | Proposed improvements not yet applied |
| `VERSION_LOG.md` | System version and improvement history |
| `SOLUTION_LOOP_CARD.md` | Documented problem-solution pairs |

---

## Install

**Claude Code Plugin (recommended)**

```
/plugin marketplace add mauricepfeifer-ctrl/andrej-karpathy-skills
/plugin install andrej-karpathy-skills@karpathy-agent-os
```

Then initialize in your project:

```
/setup
```

**Manual (CLAUDE.md)**

```bash
curl -o CLAUDE.md https://raw.githubusercontent.com/mauricepfeifer-ctrl/andrej-karpathy-skills/main/skills/agent-os-core/SKILL.md
```

Copy tracking file templates to your project:

```bash
curl -o ERROR_LOG.md https://raw.githubusercontent.com/mauricepfeifer-ctrl/andrej-karpathy-skills/main/templates/ERROR_LOG.md
curl -o LESSONS_LEARNED.md https://raw.githubusercontent.com/mauricepfeifer-ctrl/andrej-karpathy-skills/main/templates/LESSONS_LEARNED.md
curl -o RULE_UPDATE_LOG.md https://raw.githubusercontent.com/mauricepfeifer-ctrl/andrej-karpathy-skills/main/templates/RULE_UPDATE_LOG.md
curl -o IMPROVEMENT_BACKLOG.md https://raw.githubusercontent.com/mauricepfeifer-ctrl/andrej-karpathy-skills/main/templates/IMPROVEMENT_BACKLOG.md
curl -o VERSION_LOG.md https://raw.githubusercontent.com/mauricepfeifer-ctrl/andrej-karpathy-skills/main/templates/VERSION_LOG.md
curl -o SOLUTION_LOOP_CARD.md https://raw.githubusercontent.com/mauricepfeifer-ctrl/andrej-karpathy-skills/main/templates/SOLUTION_LOOP_CARD.md
```

**Cursor**

See [CURSOR.md](./CURSOR.md) for Cursor rules setup.

---

## How to Use It

**Day to day:**
1. Work normally
2. When Claude makes a mistake, tell it to log the error: `"Log this to ERROR_LOG.md"`
3. When stuck on a recurring problem: `/solve [describe problem]`

**Weekly (or when errors accumulate):**
1. Run `/improve`
2. Review proposed rule updates
3. Confirm — CLAUDE.md is updated, errors are processed, version increments

**You know it's working when:**
- Errors you've seen before stop happening
- CLAUDE.md grows with rules specific to your codebase
- VERSION_LOG.md shows a track record of improvements
- Diffs are cleaner: only the lines that were asked for change

---

## How It's Different from Static CLAUDE.md

| Static CLAUDE.md | Karpathy Agent OS |
|-----------------|------------------|
| Rules fixed at setup | Rules evolve with your errors |
| You update it manually | `/improve` updates it automatically |
| Same rules for every project | Rules specific to your codebase and patterns |
| No history | Full audit trail in RULE_UPDATE_LOG.md |
| No measurement | VERSION_LOG.md tracks improvement |

---

## Structure

```
andrej-karpathy-skills/
  skills/
    karpathy-guidelines/     # Core 4 principles (standalone)
    agent-os-core/           # 5-principle system (always-on)
    agent-os-improve/        # /improve skill
    agent-os-solve/          # /solve skill
    agent-os-setup/          # /setup skill
  templates/                 # Starter files for your project
    ERROR_LOG.md
    LESSONS_LEARNED.md
    RULE_UPDATE_LOG.md
    IMPROVEMENT_BACKLOG.md
    VERSION_LOG.md
    SOLUTION_LOOP_CARD.md
```

---

## Cursor

See [CURSOR.md](./CURSOR.md) for setup with Cursor rules.

## License

MIT
