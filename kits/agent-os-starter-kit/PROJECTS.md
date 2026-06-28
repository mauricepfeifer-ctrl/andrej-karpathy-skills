# Project Registry

Single source of truth for all projects in this workspace.
Read before starting anything new. Updated when status changes.

**Last updated:** [DATE]
**Total:** 0 projects | Run `/archaeology` to populate this file.

---

## Status Legend

| Status | Meaning |
|--------|---------|
| `OPERATIONAL` | Running, tested, actually used in production |
| `INCOMPLETE` | Started, not finished, still intended to complete |
| `PROTOTYPE` | Proof of concept, not production-ready |
| `ABANDONED` | No longer active, kept for reference only |
| `UNKNOWN` | Not yet assessed |

**OPERATIONAL** means: runs without intervention, produces correct output, has been used for its actual purpose, no known blocking issues. "Could work" is not OPERATIONAL.

---

## Priority Incomplete Projects

> These are the projects closest to OPERATIONAL. Finish one before starting anything new.

*None yet — run `/archaeology` to identify priorities.*

---

## All Projects

*Run `/archaeology` to populate. Format below.*

---

## Entry Format

```
## [Project Name]
**Status:** OPERATIONAL | INCOMPLETE | PROTOTYPE | ABANDONED | UNKNOWN
**Path:** /absolute/path/to/project
**What it does:** [one sentence]
**Working:** YES | NO | PARTIAL | UNKNOWN
**Last verified:** [YYYY-MM-DD] | UNKNOWN
**Dependencies:** [project names this depends on] | NONE
**Open tasks:** [what's blocking OPERATIONAL status] | NONE
**Notes:** [optional context]
```

---

## How Hermes Uses This File

1. Read at start of every session
2. Checked before any new project is proposed
3. Updated immediately when project status changes
4. Used to identify overlap before building anything new

If a proposed new project overlaps with an INCOMPLETE entry here, Hermes will ask: "Should we finish [existing project] instead?"
