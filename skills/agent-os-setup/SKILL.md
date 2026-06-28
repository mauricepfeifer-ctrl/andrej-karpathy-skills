---
name: agent-os-setup
description: One-time project initialization — creates all 6 Agent OS tracking files in the current project directory. Safe to run on existing projects; skips files that already exist. Invoke with /setup.
license: MIT
---

# /setup — Agent OS Project Setup

Initialize Agent OS tracking files in the current project. Safe to run multiple times — existing files are never overwritten.

## What to do

For each file below, check if it already exists in the project root. If it does not exist, create it with the starter content specified. If it does exist, skip it.

At the end, report:
```
Agent OS initialized.
Created: [list of files created]
Skipped (already exist): [list of files skipped]

Next steps:
1. Work as normal
2. When an error occurs, capture it: /improve
3. When stuck on a problem, use: /solve [describe the problem]
4. After accumulating errors, run: /improve
```

---

### ERROR_LOG.md

Create with this content:

```
# Error Log

Capture mistakes here as they occur.
Run `/improve` to process these into rule updates.

**Format:**
```
## [YYYY-MM-DD] [CATEGORY]
**What happened:** ...
**What should have happened:** ...
**Root cause:** ...
**Proposed rule:** ...
```

**Categories:** ASSUMPTION | COMPLEXITY | SCOPE_CREEP | WRONG_TOOL | MISSED_CONTEXT

---
```

### LESSONS_LEARNED.md

Create with this content:

```
# Lessons Learned

Distilled lessons extracted from ERROR_LOG.md during `/improve` cycles.
Each entry is a processed error that became a rule update.

---
```

### RULE_UPDATE_LOG.md

Create with this content:

```
# Rule Update Log

History of all rule changes made by the self-improvement loop.

---
```

### IMPROVEMENT_BACKLOG.md

Create with this content:

```
# Improvement Backlog

Proposed improvements not yet applied to CLAUDE.md.
Populated by `/solve` and `/improve` when patterns emerge.

| Priority | Proposal | Source | Date Added |
|----------|----------|--------|------------|
```

### VERSION_LOG.md

Create with this content (substitute today's date for [DATE]):

```
# Version Log

## [DATE] — v1.0
Agent OS initialized.
Rules: 5 (4 Karpathy core + self-improvement loop) | Errors processed: 0
```

### SOLUTION_LOOP_CARD.md

Create with this content:

```
# Solution Loop Cards

Documented problem-solution pairs from `/solve` cycles.

---
```
