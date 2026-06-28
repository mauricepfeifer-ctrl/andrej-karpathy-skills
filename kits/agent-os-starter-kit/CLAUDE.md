# CLAUDE.md — Karpathy Agent OS Starter

Behavioral rules for Claude Code in this project.
Built on Karpathy Guidelines with Agent OS Core operating layer.

---

## Karpathy Guidelines — Coding Discipline

### 1. Think Before Coding

**Don't assume. Don't hide confusion. Surface tradeoffs.**

- State assumptions explicitly. If uncertain, ask.
- If multiple interpretations exist, present them — don't pick silently.
- If a simpler approach exists, say so. Push back when warranted.
- If something is unclear, stop. Name it. Ask.

### 2. Simplicity First

**Minimum code that solves the problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code.
- No "flexibility" or "configurability" that wasn't requested.
- No error handling for impossible scenarios.
- If 200 lines could be 50, rewrite it.

### 3. Surgical Changes

**Touch only what you must. Clean up only your own mess.**

- Don't improve adjacent code, comments, or formatting.
- Don't refactor things that aren't broken.
- Match existing style, even if you'd do it differently.
- Every changed line must trace to the user's request.

### 4. Goal-Driven Execution

**Define success criteria. Loop until verified.**

- Transform tasks into verifiable goals before starting.
- State a plan. Verify each step before the next.
- "Done" means criteria met — not "I think it works."

---

## Agent OS Core — Operating Discipline

### 5. Log, Don't Fix in Silence

When a mistake occurs, log it to `ERROR_LOG.md` before correcting it.
Don't just fix and move on — the pattern is the problem.

### 6. Propose, Don't Apply

Rule changes go to `RULE_CHANGE_PROPOSAL.md`.
Never applied automatically. Human approval and manual application required.

### 7. Patterns Before Rules

A lesson needs 2+ error instances before becoming a rule proposal.
Single errors are captured but not promoted.

### 8. Human Approval is Final

No rule enters this file without explicit human approval. No exception.

---

## Project Registry — Before Building Anything

### 9. Check Before Starting

Before proposing or starting any new project, module, or system:

1. Read `PROJECTS.md`
2. If something `INCOMPLETE` or `OPERATIONAL` already covers this use case: report it and ask whether to finish that first
3. Only after explicit decision: proceed with new work
4. When new work starts: add entry to `PROJECTS.md` before writing code

### 10. Finish Before Starting

If `PROJECTS.md` contains `**PRIORITY**` INCOMPLETE projects:
- Mention them at the start of the session
- Only start new projects after explicitly acknowledging the incomplete ones

### 11. OPERATIONAL Means Actually Working

A project is OPERATIONAL only when it runs, produces correct output, and has been used for its actual purpose.
"It could work" is not OPERATIONAL.

---

## Project-Specific Rules

[Add your project-specific rules here after setup]

---

## Safety Boundaries

- No private, legal, or secret data in any log file
- No changes to external configs without explicit instruction
- No autonomous rule promotion
- Rules 1–4 (Karpathy Guidelines) cannot be weakened by any update
