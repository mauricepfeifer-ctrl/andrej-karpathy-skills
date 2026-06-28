# /review — Code and Decision Review

**Purpose:** Structured review checklist before committing or shipping. Flags issues before they become ERROR_LOG.md entries.

**Output:** Review report with findings and recommendation.

---

## Step 1: Scope

What is being reviewed?
- [ ] Code change: [description]
- [ ] Agent decision: [description]
- [ ] Plan: [description]
- [ ] Rule change proposal: [RCP-ID]

## Step 2: Karpathy Guidelines Check

- [ ] Minimum code needed? (Simplicity First)
- [ ] Assumptions stated before implementation? (Think Before Coding)
- [ ] Only necessary lines changed? (Surgical Changes)
- [ ] Success criteria verifiable? (Goal-Driven Execution)

## Step 3: Agent OS Check

- [ ] Errors logged during this work?
- [ ] Non-obvious decisions in DECISION_LOG.md?
- [ ] Any rule change in RULE_CHANGE_PROPOSAL.md (not applied directly)?
- [ ] Any productive config changed without explicit approval? (Must be NO)

## Step 4: Issues

For each issue found:
```
Issue [N]:
  Severity: BLOCKING | CONCERN | NOTE
  Description: ...
  Guideline violated: [if applicable]
  Recommendation: ...
```

## Step 5: Summary

```
Review complete.
Reviewed: [list]
Issues: [N blocking, N concerns, N notes]
Recommendation: APPROVE | APPROVE WITH CHANGES | REJECT
```
