# Agent OS Core + Prompts Kit V1 — Build Report

**Status: GREEN**
**Date:** 2026-06-28
**Branch:** claude/karpathy-agent-os-kit-jecmpv
**Repo:** mauricepfeifer-ctrl/andrej-karpathy-skills

---

## 1. Status: GREEN

All required components built. No forbidden actions taken.
`/improve` is proposal-only. No autonomous rule promotion. No productive config mutations.

---

## 2. Repos

| Repo | Branch | Status |
|------|--------|--------|
| mauricepfeifer-ctrl/andrej-karpathy-skills | claude/karpathy-agent-os-kit-jecmpv | ACTIVE |

Note: `mauricepfeifer-ctrl/free-llm-api-resources` was not modified. No Agent OS files were placed there as it is out of scope for this kit.

---

## 3. Created Files

### skills/agent-os-core/
- `SKILL.md`
- `templates/ERROR_LOG.md`
- `templates/LESSONS_LEARNED.md`
- `templates/DECISION_LOG.md`
- `templates/FAILURE_MODES.md`
- `templates/RULE_CHANGE_PROPOSAL.md`
- `templates/SELF_IMPROVEMENT_LOOP.md`
- `templates/RETRO_TEMPLATE.md`
- `templates/CHANGELOG_AGENT.md`

### skills/agent-os-prompts/
- `SKILL.md`
- `prompts/improve.md`
- `prompts/retro.md`
- `prompts/debug.md`
- `prompts/review.md`
- `prompts/plan.md`

### kits/agent-os-starter-kit/
- `README.md`
- `CLAUDE.md`
- `AGENTS.md`
- `ERROR_LOG.md`
- `LESSONS_LEARNED.md`
- `DECISION_LOG.md`
- `FAILURE_MODES.md`
- `RULE_CHANGE_PROPOSAL.md`
- `SELF_IMPROVEMENT_LOOP.md`

### Root
- `AGENT_OS_CORE_PROMPTS_KIT_V1_REPORT.md` (this file)

---

## 4. Changed Files

- `.claude-plugin/plugin.json` — updated to v2.0.0, skills array corrected
- `.claude-plugin/marketplace.json` — updated metadata + product promise
- `README.md` — minimal update with new product positioning

---

## 5. Verification Checklist

| Check | Result |
|-------|--------|
| `skills/karpathy-guidelines` unverändert? | ✅ JA — nicht angefasst |
| Globale CLAUDE.md / AGENTS.md verändert? | ✅ NEIN |
| Produktive Hermes/OpenClaw-Configs verändert? | ✅ NEIN |
| Git Push auf main? | ✅ NEIN — nur Feature Branch |
| Legal/Private/Secret-Daten verarbeitet? | ✅ NEIN |
| /improve ist proposal-only? | ✅ JA — siehe Abschnitt 6 |
| Auto-Regel-Promotion? | ✅ NEIN — Human Approval Pflicht |
| Cron / Autostart? | ✅ NEIN |

---

## 6. /improve Safety Verification

`skills/agent-os-prompts/prompts/improve.md` defines exactly 9 steps:

1. Read → 2. Identify Repeated Failure → 3. Classify Failure Mode → 4. Root Cause → 5. Lesson Draft → 6. Rule Change Proposal → 7. Risk Check → 8. Approval Card → **9. STOP**

Step 9 states verbatim:
> "Do not apply any changes. Do not modify CLAUDE.md. Do not modify AGENTS.md. Do not write to any log file. Wait for human response to the Approval Card."

**Verdict: /improve is proposal-only. ✅**

---

## 7. Note: Incorrect Files from Prior Commit

A first commit was made before the full spec was received. That commit created files at incorrect paths:

- `skills/agent-os-improve/SKILL.md` — wrong path, wrong behavior (was auto-applying)
- `skills/agent-os-solve/SKILL.md` — wrong path
- `skills/agent-os-setup/SKILL.md` — wrong path
- `templates/*.md` — wrong location (should be inside `skills/agent-os-core/templates/`)

These files are superseded by the correct structure in this commit. They remain on the feature branch but do not affect any productive configuration. Cleanup recommended before merge.

---

## 8. Next Approval

**APPROVE AGENT OS CORE + PROMPTS KIT REVIEW ONLY**

Awaiting human review of:
- `skills/agent-os-core/SKILL.md` — core operating rules
- `skills/agent-os-prompts/prompts/improve.md` — the proposal loop
- `kits/agent-os-starter-kit/README.md` — product documentation
- `kits/agent-os-starter-kit/CLAUDE.md` — starter rules template

After review:
- `APPROVED` → open PR for merge, clean up stale files from prior commit
- `CHANGES NEEDED` → specify which files and what to change
