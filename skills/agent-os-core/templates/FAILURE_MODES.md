# Failure Modes

Recurring error patterns identified from `ERROR_LOG.md`.
Each entry represents a root cause seen 2+ times.

**Promotion path:**
```
ERROR_LOG.md (2+ similar entries)
  → here (pattern recognized)
  → RULE_CHANGE_PROPOSAL.md (rule proposed)
  → human approval
  → CLAUDE.md / AGENTS.md
```

**Format:**
```
## FM-[N]: [NAME]
**Category:** ASSUMPTION | COMPLEXITY | SCOPE_CREEP | WRONG_TOOL | MISSED_CONTEXT | PLANNING | OTHER
**Description:** [what keeps going wrong]
**Trigger:** [when does this occur]
**Source errors:** [list of ERROR_LOG.md entry dates/titles]
**Frequency:** [N occurrences]
**Rule gap:** [why existing rules didn't prevent this]
**Status:** ACTIVE | RULE_PROPOSED | RULE_APPROVED | RESOLVED
```

---
