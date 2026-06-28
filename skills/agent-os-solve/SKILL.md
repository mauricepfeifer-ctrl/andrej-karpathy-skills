---
name: agent-os-solve
description: Structured problem-solving loop — defines the problem precisely, generates root cause hypotheses, tests each systematically, applies the minimal fix, and extracts a lesson. Use when stuck or facing a recurring problem. Invoke with /solve.
license: MIT
---

# /solve — Solution Loop

Structured problem solving. Never guess. Never skip steps. Every solution must be traced to a confirmed root cause.

**Input:** The problem (from user message or current context)

---

## Step 1: Define

Restate the problem in exactly three parts:

```
Symptom:  [what is observable and wrong right now]
Expected: [what should happen instead]
Scope:    [when does it occur / when doesn't it]
```

If you can't fill all three parts, ask the user before continuing.

## Step 2: Hypothesize

List 3–5 possible root causes, ordered by likelihood. For each:

```
[N]. [Root cause hypothesis]
    Evidence for: ...
    Evidence against: ...
    Test: [exactly what would confirm or deny this]
```

## Step 3: Test

Work through hypotheses from most to least likely:

- Run the test you defined in Step 2
- Record: CONFIRMED / DENIED / INCONCLUSIVE
- If CONFIRMED → proceed to Step 4
- If DENIED → move to next hypothesis
- If INCONCLUSIVE → refine the test and retry once
- If all denied → return to Step 2 and generate new hypotheses

## Step 4: Fix

Apply the minimal fix that addresses the confirmed root cause.

- No side fixes
- No preemptive improvements
- No "while I'm here" changes

Verify: the original symptom from Step 1 is gone.

## Step 5: Document

Append to `SOLUTION_LOOP_CARD.md`:

```
## [YYYY-MM-DD] — [Problem title]
**Symptom:** ...
**Root cause:** ...
**Fix:** ...
**Verified by:** ...
```

If SOLUTION_LOOP_CARD.md doesn't exist, create it first.

## Step 6: Extract

Ask yourself:
- Is this a pattern that could recur? → append to `LESSONS_LEARNED.md`
- Does this reveal a gap in the current rules? → append to `IMPROVEMENT_BACKLOG.md`
- Is there enough in ERROR_LOG.md to run `/improve`? → suggest it to the user

If none of the above: done. Report: "Problem solved. Root cause: [cause]. Fix applied and verified."
