---
name: project-registry
description: Project Registry — maintains PROJECTS.md as single source of truth for all projects. Agents must consult this before starting anything new. Prevents rebuilding what already exists. Includes /archaeology sprint for initial inventory.
license: MIT
---

# Project Registry

Single source of truth management. Agents cannot build what they cannot see — and neither can you.

**The core constraint:** Projects accumulate. Nothing is truly finished. New projects start on top of incomplete ones. The system has no memory of what exists.

**The fix:** One file. One protocol. One rule.

---

## The Rule

> Before proposing or starting any new project, module, or system: read PROJECTS.md. If something INCOMPLETE or OPERATIONAL already covers this use case, ask whether to finish that first.

This rule changes the cost structure of starting new things.

---

## Agent Protocol

### At the start of every session:

1. Read `PROJECTS.md`
2. Identify the current project's entry
3. If no entry exists: create one before doing anything else
4. Note any `**PRIORITY**` INCOMPLETE projects — mention them if relevant to the session

### Before proposing or starting any new project, module, or system:

1. Read `PROJECTS.md`
2. Search for entries with `Status: INCOMPLETE` or `Status: OPERATIONAL` that overlap with the proposed work
3. If overlap found:
   ```
   Report: "[Project Name] already exists at [path] with status [status].
   Open tasks: [list].
   Should we complete this instead of starting new?"
   ```
4. Wait for explicit human decision before proceeding
5. If no overlap: proceed, then add new entry to `PROJECTS.md` before writing any code

### When project status changes:

Update `PROJECTS.md` immediately — not at end of session, not later.

Status transitions that require immediate update:
- Any → `OPERATIONAL`: only when it's actually running and used in production
- Any → `INCOMPLETE`: when serious development starts on a prototype
- Any → `ABANDONED`: when the decision to stop is made
- `Working: NO` → `Working: YES`: when a blocking issue is resolved

### Definition of OPERATIONAL (strict):

A project is `OPERATIONAL` only when ALL of these are true:
- It runs without manual intervention
- It produces correct output consistently
- It has been used for its actual purpose at least once
- There are no known blocking issues

"It could work" is not OPERATIONAL. "I think it works" is not OPERATIONAL.

---

## /archaeology — Initial Inventory Sprint

**Purpose:** One-time sprint to create `PROJECTS.md` from scratch. Imperfect entries beat missing entries. Done beats perfect.

**Time limit:** 2 hours maximum. Stop when time is up, not when complete.

### Step 1: List (15 min)

Generate a flat list of all project directories — do not open any files yet:

- Scan all top-level directories in known locations
- Add anything from memory not in a standard location
- Include: complete projects, broken projects, experiments, abandoned work, anything that was ever "a thing"

Output: numbered list of paths and names only.

### Step 2: Triage from Memory (30 min)

For each project, assign status from memory only — do not open files:

```
[Name]: OPERATIONAL | INCOMPLETE | PROTOTYPE | ABANDONED | UNKNOWN
```

`UNKNOWN` is valid. Any entry is better than no entry.

If you cannot remember what a project does: mark `ABANDONED` unless you know it's needed.

### Step 3: One-Line Description (20 min)

For each project, one sentence: "This project [verb] [what]."

If you can't remember: `"Purpose unclear — needs archaeology review."`

### Step 4: Working Check (15 min)

For OPERATIONAL and INCOMPLETE projects only:
- Is it actually running right now? `YES | NO | UNKNOWN`
- If NO or UNKNOWN: note it. Do not fix it now. Just note it.

Anything that should be OPERATIONAL but is `Working: NO` → immediately downgrade to `INCOMPLETE`.

### Step 5: Write PROJECTS.md (30 min)

Write all entries using the format in `PROJECTS.md`.

For each entry, answer only what you know. Leave unknown fields as `UNKNOWN` rather than guessing.

### Step 6: Identify Priorities (10 min)

From all INCOMPLETE entries, select the 3 that are:
- Closest to OPERATIONAL (least remaining work)
- Most valuable if actually finished

Mark them `**PRIORITY**` in `PROJECTS.md`.

### Step 7: Report

```
Archaeology complete.
Total projects inventoried: [N]
OPERATIONAL: [N]
INCOMPLETE: [N] ([N] marked PRIORITY)
PROTOTYPE: [N]
ABANDONED: [N]
UNKNOWN: [N]

Top 3 priorities:
1. [Name] — [why it's closest to done]
2. [Name]
3. [Name]

Recommendation: Finish one of these before starting anything new.
```

---

## Maintenance Rules

1. `PROJECTS.md` is the first file read, every session
2. New projects get an entry before any code is written
3. Status is updated when it changes — not deferred
4. `INCOMPLETE` projects are acknowledged before starting anything new
5. OPERATIONAL means actually running — not theoretically capable
6. Hermes/agents update `PROJECTS.md` as part of completing work, not as a separate task
