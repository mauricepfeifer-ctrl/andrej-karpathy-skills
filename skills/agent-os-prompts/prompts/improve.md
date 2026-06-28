# /improve — Self-Improvement Proposal Loop

**Purpose:** Analyze accumulated logs to identify failure patterns, extract lessons, and propose rule changes. Issues an Approval Card. Stops.

**Safety:** This prompt is proposal-only. It does NOT modify `CLAUDE.md`, `AGENTS.md`, or any productive configuration. Human approval is required before any rule is applied.

---

## Inputs (read these files)

1. `ERROR_LOG.md`
2. `LESSONS_LEARNED.md`
3. `FAILURE_MODES.md`
4. `DECISION_LOG.md`
5. Current task context (if available)

If `ERROR_LOG.md` does not exist: stop. Report: "ERROR_LOG.md not found. Initialize Agent OS files first."

If `ERROR_LOG.md` has no OPEN entries: stop. Report: "No open errors. Keep working and capture mistakes as they occur."

---

## Step 1: Read

Report what you found:
```
Open errors: [N]
Date range: [earliest] to [latest]
Categories present: [list]
Already processed in LESSONS_LEARNED.md: [N]
Known failure modes in FAILURE_MODES.md: [N]
```

---

## Step 2: Identify Repeated Failure

Group OPEN errors by root cause (not surface symptom):

```
Failure Group [N]:
  Root cause: ...
  Error entries: [dates/titles]
  Frequency: [N occurrences]
  Pattern: [what's common across entries]
```

Prioritize groups with 2+ occurrences.
Single-occurrence errors are noted but not promoted to rule proposals.

---

## Step 3: Classify Failure Mode

For each group with 2+ occurrences:

```
Failure Mode: [NAME]
Category: ASSUMPTION | COMPLEXITY | SCOPE_CREEP | WRONG_TOOL | MISSED_CONTEXT | PLANNING | OTHER
Description: [1–2 sentences — what keeps going wrong]
Trigger condition: [when does this happen]
Existing rule that should have prevented this: [or NONE]
Gap: [why the existing rule didn't prevent it]
```

---

## Step 4: Root Cause

For the top failure mode:

```
Root Cause Analysis:
  Immediate cause: ...
  Systemic cause: ...
  Why existing rules missed it: ...
  Confidence: HIGH | MEDIUM | LOW
```

If confidence is LOW: report "Root cause unclear — more data needed. Recommend not issuing a rule proposal yet."

---

## Step 5: Lesson Learned Draft

```
Lesson Draft [N]:
  Statement: [one clear sentence — what to do or not do]
  Based on: [error entries — dates/titles]
  Verified: PENDING — awaits human confirmation
  Proposed for: LESSONS_LEARNED.md
```

---

## Step 6: Rule Change Proposal

```
RULE CHANGE PROPOSAL

ID: RCP-[YYYY-MM-DD]-[N]
Status: PROPOSED
Lesson: [from Step 5]

Proposed rule:
  [Exact text to add to CLAUDE.md or AGENTS.md]

Target:
  File: CLAUDE.md | AGENTS.md
  Section: [section name]
  Position: after "[existing rule text]"

Patch (add exactly this text):
---
[exact text]
---

Replaces: [existing rule] | NEW
Justification: [why this prevents the failure mode]
```

---

## Step 7: Risk Check

```
RISK CHECK for RCP-[ID]

  [ ] Conflicts with a Karpathy Guideline?
  [ ] Conflicts with an existing Agent OS Core rule?
  [ ] Risks over-constraining future tasks?
  [ ] Risks unintended side effects?
  [ ] Requires clarification before applying?

Risk level: LOW | MEDIUM | HIGH
Notes: ...
```

If risk is HIGH: add "HIGH RISK — recommend additional human review before approval."

---

## Step 8: Approval Card

```
═══════════════════════════════════════════════════════
AGENT OS IMPROVEMENT PROPOSAL
ID: RCP-[ID]
Date: [YYYY-MM-DD]
═══════════════════════════════════════════════════════
Summary: [1 sentence]
Failure mode addressed: [name]
Errors prevented: [N entries]
Risk level: [LOW | MEDIUM | HIGH]

Proposed change (apply manually if approved):
[patch text]

APPROVAL REQUIRED:
  "APPROVE RCP-[ID]" → apply the patch above manually
  "REJECT RCP-[ID] — [reason]"
  "DEFER RCP-[ID] — [condition for revisit]"

⚠️  This proposal does NOT auto-apply. Human action required.
═══════════════════════════════════════════════════════
```

---

## Step 9: STOP

Do not apply any changes.
Do not modify `CLAUDE.md`.
Do not modify `AGENTS.md`.
Do not write to any log file.

Wait for human response to the Approval Card.

After human responds:
- `APPROVED` → confirm: "RCP-[ID] approved. Please apply the patch manually to [file]. Then log to CHANGELOG_AGENT.md."
- `REJECTED` → note for future reference only
- `DEFERRED` → suggest adding to `IMPROVEMENT_BACKLOG.md`
