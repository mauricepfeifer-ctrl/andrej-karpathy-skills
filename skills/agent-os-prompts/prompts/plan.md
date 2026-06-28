# /plan — Task Planning with Success Criteria

**Purpose:** Transform a task into a verifiable plan with explicit success criteria. Applies Goal-Driven Execution from Karpathy Guidelines.

**Output:** Numbered plan with verify steps, stated assumptions, and definition of done.

---

## Step 1: Understand

```
Task: [one sentence]
Requester's actual goal: [what they're trying to achieve, not just what they asked]
Ambiguities: [list]
```

If ambiguities exist: ask to resolve them before continuing.

## Step 2: State Assumptions

```
Assumptions:
1. [assumption] — basis: [why you believe this]
2. ...

If assumption [N] is wrong: [what would change in the plan]
```

## Step 3: Break Down

```
Step [N]: [action]
  → verify: [how to confirm this step is correct]
  → depends on: [previous step or NONE]
```

## Step 4: Define Done

```
Done when:
- [criterion 1 — verifiable]
- [criterion 2 — verifiable]

NOT done until:
- [anti-criterion — common shortcut to avoid]
```

## Step 5: Risk Check

```
Risks:
- [risk 1] → mitigation: ...

Scope creep risk:
- [what might expand this task] → guard against by: ...
```

## Step 6: Log Decision

Append to `DECISION_LOG.md`:
```
## [DATE] Plan: [task title]
**Approach:** [summary]
**Alternatives rejected:** [and why]
**Key assumptions:** [list]
```

## Step 7: Present and Confirm

Present the complete plan. Ask: "Does this match your intent? Should I proceed?"

Do not start implementation until confirmed.
