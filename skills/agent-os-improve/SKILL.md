---
name: agent-os-improve
description: Self-improvement trigger — reads ERROR_LOG.md, extracts patterns, proposes rule updates to CLAUDE.md, and logs all changes. Run after accumulating errors to upgrade your Agent OS. Invoke with /improve.
license: MIT
---

# /improve — Self-Improvement Cycle

You are running the Agent OS self-improvement cycle. Execute each step in order. Do not skip steps.

## Step 1: Read

Read `ERROR_LOG.md` in the current project directory.

- If the file doesn't exist: "ERROR_LOG.md not found. Run /setup to initialize Agent OS files."
- If the file is empty or contains only the header: "No errors to process. Keep working and capture mistakes as they occur."
- Otherwise: continue.

## Step 2: Analyze

For all entries in ERROR_LOG.md:

1. Group entries by category: ASSUMPTION | COMPLEXITY | SCOPE_CREEP | WRONG_TOOL | MISSED_CONTEXT
2. Identify patterns — errors that share a root cause, even if categorized differently
3. For each distinct pattern, formulate one concrete preventive rule

**Rule quality standard:**
- Good rule: prevents a specific error, checkable before implementation, applicable by anyone without context
- Bad rule: too general ("be careful"), unverifiable, or duplicates an existing rule

## Step 3: Propose

Present each proposed rule clearly:

```
Pattern: [what keeps going wrong]
Errors it covers: [N entries, dates]
Proposed rule: [exact text to add to CLAUDE.md]
Section: [which section of CLAUDE.md it belongs in]
```

Ask: "Apply these [N] rules to CLAUDE.md? (yes / no / edit)"

## Step 4: Apply

On confirmation:

1. **CLAUDE.md** — add each approved rule to the appropriate section
2. **LESSONS_LEARNED.md** — move all processed ERROR_LOG entries here with a datestamp
3. **ERROR_LOG.md** — clear processed entries, keep header intact
4. **RULE_UPDATE_LOG.md** — append:
   ```
   ## v[X] — [YYYY-MM-DD]
   Errors processed: [N]
   New rules added:
   - [rule 1]
   - [rule 2]
   Patterns eliminated:
   - [pattern 1]
   ```
5. **VERSION_LOG.md** — append:
   ```
   ## [YYYY-MM-DD] — v[X]
   Rules added: [N] | Errors processed: [N] | Total rules: [N]
   ```

Determine the next version number from the last entry in VERSION_LOG.md. Start at v1.1 if none exists.

## Step 5: Report

"Improvement cycle complete.
- [N] errors processed
- [N] new rules added
- System upgraded to v[X]

Next: keep working. Capture new errors with `/improve` as they occur."
