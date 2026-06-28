# /retro — Session Retrospective

**Purpose:** End-of-session structured review. Surfaces what worked, what didn't, and whether to run `/improve`.

**Output:** Filled retrospective entry + recommendation on next action.

---

## Step 1: Gather

What happened this session?
```
Errors logged to ERROR_LOG.md: [N]
Decisions logged to DECISION_LOG.md: [N]
Tasks completed: [list]
Tasks not completed: [list with reason]
```

## Step 2: Reflect

```
What went well:
  [specific — not generic]

What went wrong:
  [link to ERROR_LOG.md entries]

What was surprising:
  [anything unexpected]

What would you do differently:
  [if starting this task again]
```

## Step 3: Classify Errors

For each error logged this session:
```
[Date/Title]: [CATEGORY]
Pattern match: [existing FM-N] | NEW
```

## Step 4: Ready Check

```
Open errors in ERROR_LOG.md: [N]
Recurring patterns visible (2+ same root cause): YES | NO
Recommendation: RUN /improve | WAIT FOR MORE DATA
```

## Step 5: Write

Append a completed `RETRO_TEMPLATE.md` entry to the project retro log (create `RETRO_LOG.md` if it doesn't exist).

## Step 6: Report

```
Retro complete.
Errors reviewed: [N]
Decisions logged: [N]
Recommendation: [RUN /improve | WAIT]
```
