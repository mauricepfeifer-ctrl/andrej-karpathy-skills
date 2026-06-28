# /debug — Structured Debugging Loop

**Purpose:** Systematic root cause analysis. Never guess. Every fix is traced to a confirmed cause.

**Output:** Confirmed root cause + minimal fix + DECISION_LOG entry.

---

## Step 1: Define

State the problem in three parts:
```
Symptom:  [what is observable and wrong right now]
Expected: [what should happen instead]
Scope:    [when does it occur / when doesn't it]
```

If you can't fill all three parts, ask before continuing.

## Step 2: Hypothesize

List 3–5 root cause hypotheses, ordered by likelihood:
```
[N]. [Hypothesis]
    Evidence for: ...
    Evidence against: ...
    Test: [exactly what would confirm or deny this]
```

## Step 3: Test

For each hypothesis (most likely first):
- Run the defined test
- Record: `CONFIRMED` / `DENIED` / `INCONCLUSIVE`
- `CONFIRMED` → Step 4
- `DENIED` → next hypothesis
- `INCONCLUSIVE` → refine test, retry once
- All denied → return to Step 2 with new hypotheses

## Step 4: Fix

Apply the minimal fix for the confirmed root cause:
- No side fixes
- No preemptive improvements
- No "while I'm here" changes

Verify: original symptom from Step 1 is gone.

## Step 5: Log

Append to `DECISION_LOG.md`:
```
## [DATE] Debug: [problem title]
**Root cause confirmed:** ...
**Fix applied:** ...
**Verified:** [how you confirmed it worked]
```

Ask: "Is this a recurring pattern? Should I add it to ERROR_LOG.md?"

## Step 6: Report

```
Debug complete.
Root cause: [cause]
Fix: [what was changed]
Verified: [how]
```
