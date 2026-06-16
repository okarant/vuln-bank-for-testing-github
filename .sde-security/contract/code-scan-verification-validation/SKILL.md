---
name: code-scan-verification-validation
description: Verifies that security countermeasures are actually mitigated in code and records Verification Notes to SD Elements. Supports handoff mode (reads .sde-apply-handoff.json from apply-security-fixes) and standalone mode (fetches countermeasures from SDE via MCP with AI-driven file discovery). Before posting each verification note, fetches existing verification notes (via `verification op=list`) to preserve prior verification details (read-then-append pattern, behaviour=combine). Forced-fail CMs receive posted notes for SDE visibility. Use when verifying security fixes, scanning code for countermeasure compliance, or validating mitigation after apply-fixes or manual remediation.
---

> **SUBAGENT / DELEGATION POLICY -- READ THIS FIRST**
>
> 1. **Same model as the parent, ALWAYS.** Any spawned subagent MUST run on the SAME model as the parent agent -- set the `model` parameter explicitly to the parent's model. If you cannot set the subagent's model, do NOT spawn -- run inline.
> 2. **NEVER Composer 2.** `composer-2.5-fast` (Composer 2) is FORBIDDEN as a subagent model in ANY environment -- it silently abandons loops, skips CMs, uses wrong endpoints for note POSTs, loses context, and produces unreliable verdicts. In Cursor the DEFAULT subagent is Composer 2, so you MUST override `model` to the parent's model explicitly; if you cannot override it, run inline.
> 3. **Parent owns completeness.** Delegation NEVER transfers responsibility for completeness. The parent re-derives every CM from SDE + disk (tri-source invariant) regardless of who did the work. Every subagent MUST emit `[PROGRESS]`/`[VERIFY]` lines and return a verifiable JSON result; the parent verifies every item.
>
> Subagent batching (Step A6 / Phase B) is permitted in ANY environment (including Cursor) under this policy; inline execution is the fallback only when the subagent `model` cannot be set to the parent's model.
>
> Output at skill start: `[CHECKPOINT] Subagent policy: same-model-as-parent | Composer 2 FORBIDDEN | parent owns completeness (tri-source)`

# Code Scan Verification Validation

> **STOP -- PHASE A RUNS IN PLAN MODE. DO NOT SWITCH TO AGENT MODE UNTIL PHASE B.**
>
> This skill has 7 mandatory interactive steps (A0 through A7) that MUST be completed sequentially in **plan mode** using `ask_question` calls. All Phase A steps are read-only (MCP reads, file reads, user questions). You MUST NOT:
> - Switch to agent mode before Phase A is complete
> - Create a plan (via `CreatePlan`) before completing Phase A
> - Infer or assume any Phase A input (mode, scope, batch size, fail-rollback) from context
> - Default to `all` scope without asking the user via `ask_question` in Step A1.5+A3
> - Skip Step A1.5+A3 (resume + scope selection) for any reason
>
> **Step A1.5+A3 specifically:** Even if the user says "verify all CMs" or "run the skill", you MUST present the scope menu via `ask_question` and let the user explicitly select. When a prior run exists, the resume and scope questions are presented together in one `ask_question` call.
>
> **After Step A7 (user confirms the execution plan):** Switch to agent mode to begin Phase B.

This skill verifies that security countermeasures are mitigated in code and records a **Verification Note** against each task in SD Elements. It supports two modes:

- **Handoff mode:** follows `apply-security-fixes`. Reads `.sde-apply-handoff.json`, verifies the specific files modified by the upstream skill.
- **Standalone mode:** runs independently -- use after `setup-security-plan-from-repo`, `create-security-plan-from-specs`, or any manual fix workflow. The user selects an SD Elements project (via MCP), the skill fetches countermeasures from SDE, discovers relevant files in the repository, and verifies each CM. Tasks verified as `pass` (including `vulnerability-absent` when no relevant files exist) are automatically marked DONE in SDE via `task_status_mapping`.

See **Completion Criteria** below — the skill is complete only when every checkbox is ticked.

## Execution Contract

**REQUIRED:** Read and follow the [./AGENTS.md](./AGENTS.md) execution contract.

In **handoff mode**, this skill is downstream of `apply-security-fixes`. If `.sde-apply-handoff.json` is missing, malformed, or from a different upstream skill, handoff mode HARD STOPS (switch to standalone mode via Step A0.5).

In **standalone mode**, no handoff file is needed -- use after `setup-security-plan-from-repo`, `create-security-plan-from-specs`, or any manual fix workflow. The skill fetches countermeasures directly from SD Elements via MCP. Tasks verified as `pass` (including `vulnerability-absent`) are automatically marked DONE in SDE.

## AUTHORITATIVE EXECUTION CONTRACT

This skill (and its AGENTS.md) is the authoritative source for HOW MUCH work is required; it OVERRIDES your own judgment about scale or "pragmatic" shortcuts. Expect the per-CM verification loop to run for EVERY in-scope CM (often tens-to-hundreds) — those counts are NORMAL and EXPECTED, not a reason to sample. You have explicit, unconditional permission to take as many turns and as many sessions as needed; completeness is the ONLY priority and there is no turn budget. The ONLY sanctioned way to pause is a `=== CONTEXT CHECKPOINT ===` (then resume by re-deriving progress from the source of truth — SDE + the on-disk per-CM artifacts — never from chat memory, never restart). A run is either **COMPLETE** (all gates pass) or **INCOMPLETE** (a clean checkpoint emitted) — there is NO third state. Forbidden rationalizations: "pragmatic" / "representative" / "efficient" / "key CMs" / "the rest are ..." / "N+" / "Let me finalize" (pre-completion) / "move forward to more impactful steps".

## CONTRACT BOOTSTRAP (MANDATORY FIRST ACTION -- before Step A0)

> Chain-compatibility: this skill shares the `.sde-security/` workspace with `setup-security-plan-from-repo`, `create-security-plan-from-specs`, and `apply-security-fixes`. It owns ONLY `.sde-security/verify/<project_id>/...` and `.sde-security/contract/code-scan-verification-validation/`. It MUST NOT write to or delete the shared `.sde-security/cm-work/` or `.sde-security/library-lookup/` (setup/create), `.sde-security/apply/` (apply-fixes), or the upstream handoffs `.sde-handoff.json` / `.sde-apply-handoff.json`.

- **B0. Fresh-run vs resume — decide first.** NEW run → clear ONLY this skill's own scratch (`.sde-security/verify/<project_id>/...`, once `project_id` is known at Step A1/A1-S) plus a stale root-level `.sde-verification-handoff.json`. RESUME → keep all prior artifacts and resume from disk. NEVER delete `.sde-handoff.json`, `.sde-apply-handoff.json`, or any upstream `.sde-security/` subdirectory.
- **B1. Fetch the EXACT served contract** for THIS skill (not memory): `prompts op=get prompt=code-scan-verification-validation`.
- **B2. Pin it VERBATIM** to `.sde-security/contract/code-scan-verification-validation/{SKILL,AGENTS}.md` (split on BEGIN/END markers if concatenated).
- **B3. Record a manifest** at `.sde-security/contract/code-scan-verification-validation/manifest.json`: `{ skill, fetched_at, sha256_skill, sha256_agents, skill_chars, agents_chars }`.
- **B4. Staleness check (WARN, do NOT deadlock):** the contract you were GIVEN to execute is authoritative. If `prompts op=get` errors / is empty / lacks this skill, WARN "served prompt stale" and pin from the best available source (served-if-valid > on-disk source > given text). HARD STOP only if no source exists.
- **B5. Emit:** `[CONTRACT PINNED] skill=code-scan-verification-validation | path=.sde-security/contract/code-scan-verification-validation/ | SKILL chars={n} sha256={short} | AGENTS chars={n}`

### STEP PREFLIGHT CONVENTION (every step AND every batch)
- **Before each step:** reload that step's section from the pinned `.sde-security/contract/code-scan-verification-validation/SKILL.md` (read ONLY that step's heading→next-heading range — context-light), THEN emit `[STEP] entering {step} | reloaded §{step} from disk? YES | sentinel: "{a verbatim line copied from that step's section on disk}"`. You cannot produce the correct sentinel without having re-read the section.
- **Heavy/looping steps (Phase B):** ALSO reload at every batch boundary and include the sentinel in the `[RUNNING CHECK]`.
- A missing/incorrect sentinel = running from memory = **CONTRACT VIOLATION**. STOP and reload.

## SHELL TOOL USAGE POLICY (CANONICAL -- applies to this ENTIRE skill)

The AI owns ALL vulnerability analysis, verdicts, and note authoring (inline); scripts are allowed ONLY for mechanical/IO + SDE calls with completeness-verify + retry.

| Work | Owner | Rule |
|------|-------|------|
| Reading code; vuln ANALYSIS (B2); VERDICT (B3); finding/note authoring | AI only | inline (subagent or parent); NO script may read code, decide a verdict, or author findings |
| Per-CM result OFFLOAD (write the AI's already-produced verdict/findings JSON), disk count, assemble-from-disk, Layer-2 verify script | script OK | mechanical only; implement the helper routines yourself from the pseudocode in this contract |
| SDE note POST | per-CM `verification op=create` WITH verify + retry | **NO Composite API** — verification notes are posted ONE CM at a time via the dedicated tool; never batch note POSTs into a composite call |
| git / file reads / `/tmp` scratch | OK | |

**AI ANALYSIS IS NEVER OFFLOADED.** The disk-offload (Phase B per-CM loop; helpers in Step D / T6) stores the OUTPUT of the AI's analysis (the verdict + findings the AI already produced). It is NEVER a substitute for doing the analysis: B2 (read + analyze the code) and B3 (derive `pass`/`partial`/`fail` via the No-False-Positives Invariant) MUST run as AI reasoning inline, never by a script and never "deferred to disk in place of doing it."

---

## ⚠️ AI CODE ANALYSIS REQUIRED - NO GREP-ONLY VERDICTS ⚠️

Verification verdicts MUST come from **reading the relevant files with `read_file`** (modified files in handoff mode; discovered files in standalone mode) and reasoning about whether the code actually mitigates the vulnerability described in `ctx.problem` (the vulnerability) and the recommended fix described in `ctx.text` (the canonical fix narrative). `ctx.how_tos[]` is **optional, corroborative input** — many SDE CMs have empty or partially populated `how_tos[]`, and the verdict logic must work correctly in that case (see Step B3 verdict matrix; Q2 is skipped when `ctx.how_tos[]` is empty or has no language-applicable entries). Grep is acceptable only as a pre-filter to locate residual markers; it is never sufficient by itself to declare `pass`.

| ❌ FORBIDDEN | ✅ REQUIRED |
|-------------|-------------|
| `pass` because `files_modified` is non-empty | `read_file` each modified file, confirm fix is present and correct |
| `fail` based on a hunch | `fail` requires a cited residual pattern or marker |
| Skipping CMs whose files no longer exist | HARD STOP, report the inconsistency |
| Posting any verdict (pass/partial/fail) to a Documented-only CM | Filter excludes from `all` / `one_by_one`; under `selected_cms`, Step B0a records `skipped_out_of_scope`; no API call in either case (SAST convention; nothing on disk to scan) |
| Marking `fail` because the canonical mitigation pattern was not found | The vulnerability described in `ctx.problem` being absent is canonical; recognition of the mitigation is corroborative. Use the no-false-positives invariant in Step B3 — `fail` requires CITED evidence (residual pattern, residual marker, or — handoff mode only — upstream `Skipped` or empty `files_modified[]` for code CMs) |
| Marking `fail` or `partial` because `ctx.how_tos[]` is empty or has no applicable entries | Q2 is OPTIONAL. The matrix collapses to Q1 + Q3 + marker scan; `Q1=absent_high_confidence` + clean markers always yields `pass`/`high` — `how_tos` is corroborative-only |
| Marking `partial` because the developer used a different mitigation style than the how-to | If Q1 is `absent_high_confidence`, the verdict is `pass` regardless of Q2/Q3. `partial` is reserved for genuine analysis ambiguity (Q1 = `ambiguous`) or context-fetch failures |

---

## Status concepts: verification status vs. countermeasure status

SD Elements has **two separate, independent status concepts** ([User Guide reference](https://docs.sdelements.com/master/guide/docs/integrations/security_tools/overview/verification_status.html)):

| Concept | Values | API resource | What it means |
|---------|--------|--------------|---------------|
| **Countermeasure (task) status** — workflow state | `TODO` (Incomplete) / `DONE` (Complete) / `NA` (Not Applicable) | `/api/v2/task-statuses/` | The work-item state. Customizable via custom statuses with one of the three "meanings". |
| **Verification status** — verification outcome | `pass` / `partial` / `fail` / `none` | `/api/v2/verification-statuses/` | Whether the countermeasure has actually been verified as completed. Independent of countermeasure status. |

This skill writes **verification status** by creating a Verification Note via `verification op=create`. It can also atomically update **countermeasure (task) status** via the optional `task_status_mapping` field on the same payload (see Step B3). The two are distinct fields in the SDE data model and in the SDE UI; this skill never conflates them.

Throughout this skill, "verdict" = verification status. "Workflow status" / "task status" = countermeasure status. Never use one to refer to the other.

---

## Scope of static verification

SD Elements treats this skill the same way it treats any SAST scanner posted via Manual Verification: it only emits Verification Notes for countermeasures whose mitigation is **in code or config files**. This matches the convention used by Veracode, Checkmarx, Snyk Code, Fortify, Semgrep, etc. when they report into SDE.

**Handoff mode:** Documentation-only countermeasures (`ML_DOC`, and `INFRA` CMs that `apply-fixes` recorded as `Documented`) are **out of scope for static analysis**. The skill skips them without a verification note POST — the SDE UI honestly shows "No Verification Status" until a human or a different verifier weighs in. Beyond the SAST convention, there is a hard operational reason: `apply-fixes` Step 7 deletes the `skills/` directory before this skill runs. Documented CMs have empty `files_modified[]` and **no surviving local artifact to read**. The skill defers to SDE's existing surfaces — the `[AI-Documented] ...` comment that `apply-fixes` posted via `project_countermeasures op=addNote`, plus the CM's `how_tos` and `text` fields.

**Standalone mode:** There is no upstream `Documented`/`Skipped`/`Applied` status. All CMs that pass the SDE status filters (Step A1-S.3) are in scope. The file discovery step (B1.7) determines whether relevant code exists; if no relevant files are found, the verdict is `pass` with `vulnerability-absent` (the vulnerability does not appear in the codebase).

### Handoff-mode discriminator

The skill reads `status` from `.sde-apply-handoff.json` for each entry. Filtering happens at `filter_by_scope` (before the loop), so the loop only sees in-scope CMs:

| `cm.status` | Lane | Filter (`all` / `one_by_one`) | Filter (`selected_cms`) | Loop action |
|-----------------------|------|-------------------------------|-------------------------|-------------|
| `Applied` | In scope | included | included if listed | Per-CM verification (via batched subagent or inline — see Step A6): B1 (fetch CM context via MCP) + B2 (AI analysis on modified files) + B3 (verdict) + B4 (fetch existing notes) + B5 (POST Verification Note via MCP) per CM in batch |
| `Documented` | **Out of scope** | **excluded by filter** | included if listed (after warning) | Step B0a defensive guard (parent loop): record `skipped_out_of_scope`, emit `[SKIP-OOS]`; no subagent dispatch, no SDE fetch, no API call |
| `Skipped` | In scope (forced fail) | **excluded by filter** | included if listed | Step B0b forced-fail lane (parent loop): record `verdict=fail / confidence=high` with finding "CM was skipped by apply-fixes; no mitigation present"; no subagent dispatch; parent runs B4+B5 inline to POST the forced-fail note to SDE |

Net effect: Documented and upstream-Skipped CMs are filtered out of the bulk scopes (`all` / `one_by_one`) symmetrically. They can only enter the loop via an explicit user decision in `selected_cms`. Pure `PROCESS` CMs are absent from `.sde-apply-handoff.json` entirely (filtered upstream by `setup-security-plan-from-repo`), so they never reach this loop under any scope.

### Standalone-mode discriminator

All CMs from the SDE project that pass the user's task-status and verification-status filters (Step A1-S.3) are in scope. There is no `Documented`/`Skipped`/`Applied` distinction — the B0a/B0b/B0b2/B0b3 parent short-circuits do not apply. Every CM proceeds to file discovery (B1.7) and analysis (B2) — via a batched subagent when `execution_mode == "subagent"`, or inline in the parent when `execution_mode == "inline"` (see Step A6).

---

## Prerequisites

**Both modes:**

1. SDE MCP server is connected and reachable
2. Target repository is accessible and the git working tree is **clean** (no uncommitted changes)

**Handoff mode (additional):**

3. `apply-security-fixes` has completed successfully in a prior session
4. `.sde-apply-handoff.json` exists at the selected repository root with `source_skill == "apply-security-fixes"`

**Standalone mode (additional):**

3. An SD Elements project exists with countermeasures to verify

Note: `setup-security-plan-from-repo` writes a separate file called `.sde-handoff.json`. That file is **out of scope for this skill** — never read, write, rename, or delete it. In handoff mode, the only input is `.sde-apply-handoff.json`.

If any prerequisite is violated, the skill must HARD STOP with a remediation message and refuse to proceed.

---

## Context-Agnostic Policy

This skill is **repository-agnostic** and **verdict-agnostic**. The following rationalizations are FORBIDDEN and MUST NOT influence verdicts:

- "This is a training / intentionally-vulnerable repo, mark everything pass"
- "This CM is low priority, skip it"
- "The previous skill already marked it Applied, so it must be mitigated"
- "The file is large, a grep is good enough"
- "I don't want to fail this CM because it would roll back the task status"

Verdicts are a function of **code evidence only**. The scope of work is a function of **the CM source (handoff file or SDE project) and the user's scope selection only**. Nothing else.

---

## Completion Criteria

This skill is complete ONLY when all of the following are true:

- [ ] MCP connection verified
- [ ] Mode selected (Step A0.5): `handoff` or `standalone`
- [ ] Repository path confirmed
- [ ] **Handoff mode:** `.sde-apply-handoff.json` loaded and validated; user confirmed handoff values
- [ ] **Standalone mode:** SDE project selected; countermeasures fetched; SDE status filters applied; user confirmed
- [ ] `git status --porcelain` returned empty BEFORE any `git checkout`
- [ ] Branch checked out (handoff: `security_branch` if present; standalone: user-selected or current)
- [ ] Risk policy displayed and confirmed by the user (Step A1.6)
- [ ] User selected a verification scope (`all` / `selected_cms` / `one_by_one`); for `one_cm`/`multi_cm`, CM IDs were collected immediately in Step A1.5+A3
- [ ] User answered the fail-rollback opt-in question (Step A4)
- [ ] Batch size resolved (Step A5): auto-set to 1 for single-CM scope, or user-selected / default (10) for multi-CM scopes
- [ ] Subagent capability probed (Step A6); `execution_mode` set to `subagent` or `inline`
- [ ] Phase A verification block output with `MATCH = YES`; user confirmed execution plan (Step A7)
- [ ] Every in-scope CM has: full SDE context fetched, relevant files read (modified files in handoff mode; discovered files in standalone mode), verdict derived, existing notes fetched via B4 (POST-eligible CMs only — user-skipped and Documented-under-`selected_cms` CMs are recorded without fetch/read)
- [ ] Every in-scope CM has a recorded result entry: a Verification Note created via `verification op=create` (or a logged failure with cause) for POST-eligible CMs; a `record_skipped` / `record_out_of_scope` entry for the no-POST classes — no CM is silently dropped
- [ ] `.sde-verification-handoff.json` written to repository root
- [ ] Completion verification block output with `Sum check = YES`
- [ ] **Posted-note coverage re-derived from SDE** (`verification op=list` per POST-eligible CM, matched on `finding_ref`) == NP — NOT trusted from the in-memory results array
- [ ] **Handoff mode:** Upstream `.sde-apply-handoff.json` was NOT modified or deleted by this skill

---

## Mandatory Checkpoints

Output these at the indicated points:

| After | Required Output |
|-------|-----------------|
| MCP verified | `[CHECKPOINT] MCP connection successful` |
| Mode + repo selected (A0.5) | `[CHECKPOINT] Mode: {verification_mode}; repository: {repository_path}` |
| Handoff loaded (handoff mode) | `[CHECKPOINT] Handoff loaded: {N} CMs ({A} Applied / {D} Documented / {S} Skipped) from {source_skill}` |
| Standalone CMs fetched (standalone mode) | `[CHECKPOINT] Standalone mode: {N} countermeasures fetched from project {project_name} (ID: {project_id}) \| task_status_filter: {filter} \| verification_filter: {filter}` |
| Risk policy confirmed (A1.6) | `[CHECKPOINT] Risk policy: {policy_name} (ID: {policy_id}) — confirmed` (or `Risk policy: (none set) — confirmed`) |
| Resume + scope status (A1.5+A3) | `[CHECKPOINT] Resume: {already_done} CMs from prior run; {still_todo} remaining` OR `Resume: starting fresh` followed by `[CHECKPOINT] Scope: {scope}` |
| Git clean check | `[CHECKPOINT] Git tree clean; checked out {branch_name}` |
| Scope + rollback selected | `[CHECKPOINT] Scope: {scope}; fail-rollback: {yes_rollback \| no_verification_only}` |
| Batch size (A5) | `[CHECKPOINT] Batch size: {batch_size}; parallel subagents: 5` |
| Subagent probe (A6) | `[CHECKPOINT] Execution mode: {subagent \| inline}` |
| Phase A verified + user confirmed plan (A7) | `[CHECKPOINT] Phase A complete: {count}/{expected} inputs gathered; user confirmed execution plan` |
| Empty in-scope set (after `filter_by_scope`) | `[INFO] No in-scope CMs after filtering. Nothing to verify; writing empty handoff.` |
| Batch dispatched | `[VERIFY-DISPATCH] batch {batch_num}/{total_batches} | {N} CMs: [{cm_ids}] | {subagent launched \| inline}` |
| Each CM (normal verification return) | `[VERIFY] {done}/{in_scope_total} | {full_cm_id} | verdict={pass\|partial\|fail} | confidence={high\|low} | note={POSTED\|FAILED:{reason}}` |
| Forced fail — B0b (upstream Skipped) | `[VERIFY] {done}/{in_scope_total} | {full_cm_id} | verdict=fail | confidence=high | note={POSTED\|FAILED:{reason}}` |
| Forced fail — B0b2 (code CM, empty `files_modified`, v2) | `[VERIFY] {done}/{in_scope_total} | {full_cm_id} | verdict=fail | confidence=high | note={POSTED\|FAILED:{reason}} (parent B0b2)` |
| Malformed subagent return (batch) | `[VERIFY] {done}/{in_scope_total} | {full_cm_id} | verdict=partial | confidence=low | note=FAILED:subagent-malformed` (emitted per CM in batch) |
| Subagent timeout (all retries exhausted) | `[VERIFY] {done}/{in_scope_total} | {full_cm_id} | verdict=partial | confidence=low | note=FAILED:subagent-timeout` (emitted per CM in batch) |
| Auth failure (any subagent's 401/403) | `[VERIFY] {done}/{in_scope_total} | {full_cm_id} | verdict={status} | confidence={conf} | note=NOT_SENT_AUTH_FAILURE` followed by `[STOP] Auth failure at {full_cm_id}; aborted run; recorded {N} unreached CMs to preserve Sum-check identity. Refresh credentials and re-run.` |
| Documented CM under `selected_cms` (parent B0a) | `[SKIP-OOS] {done}/{in_scope_total} | {full_cm_id} | out-of-scope (Documented)` |
| Parent B0b3 (non-code CM with empty `files_modified[]`, v2 only) | `[SKIP-OOS] {done}/{in_scope_total} | {full_cm_id} | out-of-scope (parent B0b3: {category}, empty files_modified)` |
| Subagent L-OOS-sub (non-code CM with empty `files_modified[]`, v1) | `[SKIP-OOS] {done}/{in_scope_total} | {full_cm_id} | out-of-scope (subagent L-OOS-sub: {reason})` |
| User skip in `one_by_one` | `[SKIP-USER] {done}/{in_scope_total} | {full_cm_id} | user skipped` |
| User stop in `one_by_one` | `[STOP] User stopped at {done}/{in_scope_total}; recorded {N} CMs as user-stopped to preserve Sum-check identity` |
| Own handoff | `[CHECKPOINT] Verification handoff written: .sde-verification-handoff.json ({N} records)` |
| Completion | Verification block (see below) + `✅ COMPLETION GATE PASSED` |

---

## Phase A: Interactive Setup

All interactive user input happens in Phase A. Phase B runs to completion without further prompts (except explicit per-CM approval in `one_by_one` scope). **The agent MUST complete ALL Phase A steps before starting ANY Phase B step.**

### Step A0. Verify MCP Connection

Call a trivial SDE MCP tool (e.g., list projects with a tiny page size) to confirm the server is reachable. If it fails, abort with a clear remediation.

**[CHECKPOINT]** `MCP connection successful`

### Step A0.5. Mode + Repository Selection

Two questions determine how the skill discovers countermeasures and where it scans.

**Q1 — Repository path:**

Ask via `ask_question`:
- **Prompt:** "Which repository should I verify?"
- **Options:**
  - `{"id": "current", "label": "Current repository ({cwd})"}`
  - `{"id": "browse", "label": "Enter a different repository path"}`

If `browse`: follow-up text prompt for the absolute path. Validate that the path exists and contains a `.git/` directory (i.e., is a git repo). If validation fails, HARD STOP with remediation.

Store `repository_path`. Derive `repo_name = basename(repository_path)` (e.g., `my-app` from `/home/user/my-app`).

**Q2 — Verification mode:**

Ask via `ask_question`:
- **Prompt:** "How should I discover countermeasures?"
- **Options:**
  - `{"id": "handoff", "label": "From handoff file (.sde-apply-handoff.json in the repo) — use after apply-security-fixes"}`
  - `{"id": "standalone", "label": "From SD Elements project (no handoff needed — use after setup-security-plan, create-security-plan, or manual fixes)"}`

Store `verification_mode = "handoff" | "standalone"`.

**[CHECKPOINT]** `Mode: {verification_mode}; repository: {repository_path}`

If `verification_mode == "handoff"` → proceed to **Step A1** (handoff validation).
If `verification_mode == "standalone"` → proceed to **Step A1-S** (SDE project selection).

### Step A1. Detect and Validate Handoff (handoff mode only)

```python
handoff_path = f"{repository_path}/.sde-apply-handoff.json"
if not exists(handoff_path):
    HARD_STOP(f"""
    This skill requires .sde-apply-handoff.json produced by apply-security-fixes.
    It is not present at {handoff_path}. Run apply-security-fixes first,
    or switch to standalone mode (re-run and choose "From SD Elements project").
    """)

handoff = json.load(open(handoff_path))

if handoff.get("source_skill") != "apply-security-fixes":
    HARD_STOP(f"""
    .sde-apply-handoff.json has source_skill={handoff.get('source_skill')!r}.
    This skill only accepts handoffs from apply-security-fixes.
    """)

if handoff.get("handoff_version") not in ("1", "2"):
    WARN("Unknown handoff_version; proceed at your own risk.")

handoff_has_category = (handoff.get("handoff_version") == "2")

required_keys = ["repository_path", "project_id", "countermeasures"]
missing = [k for k in required_keys if k not in handoff]
if missing:
    HARD_STOP(f"Handoff is malformed: missing {missing}")
```

Show the user a summary of `repository_path`, `project_name`, `project_id`, scope, totals, and ask:

> "Use this handoff? [Use handoff / Cancel]"

If the user declines, the skill aborts. In handoff mode there is no manual fallback because `files_modified[]` cannot be reconstructed without the handoff. (To verify without a handoff, re-run and select standalone mode at Step A0.5.)

**[CHECKPOINT]** `Handoff loaded: {N} CMs ({A} Applied / {D} Documented / {S} Skipped) from apply-security-fixes`

After the checkpoint, proceed to **Step A1.6** (Risk Policy Check + Confirm) and then **Step A1.5+A3** (resume + scope selection).

### Step A1-S. SDE Project Selection (standalone mode only)

This step replaces Step A1 when `verification_mode == "standalone"`. The skill fetches countermeasures directly from SD Elements via MCP — no handoff file needed.

#### A1-S.1: Project Selection

List available projects and let the user pick one:

1. Call `project` with `op: "list"` and `page_size: 100` to retrieve the project list.
2. Ask via `ask_question`:
   - **Prompt:** "Select the SD Elements project to verify against:"
   - **Options:** Each project as `{"id": "{project_id}", "label": "{project_name} (ID: {project_id})"}`
3. **Wait for user response** — do not auto-select.
4. Validate with `project_countermeasures op=list project_id={selected_id} page_size=1` to confirm access.
5. Store `project_id`, `project_name`.

#### A1-S.2: Fetch Countermeasures from SDE

SDE tracks per-CM **task status** (`DONE` / `TODO` / `NA`) and **verification status** (`pass` / `partial` / `fail` / `none`). The MCP tool exposes both:

```python
cms_raw = project_countermeasures(op="list", project_id=project_id,
                                  page_size=250,
                                  expand="text,status,problem,tags,how_tos,phase")
```

Paginate if the project has more than 250 CMs (follow `next` links or increment `page` until exhausted).

#### A1-S.3: Scope Filter by SDE Status

After fetching, ask the user which CMs to include based on SDE's own status data.

**Q-S3 — Task status filter:**

Ask via `ask_question`:
- **Prompt:** "Which countermeasures should be in scope based on their SDE task status?"
- **Options:**
  - `{"id": "done_only", "label": "Only DONE (Complete) — verify that completed CMs are actually mitigated (recommended)"}`
  - `{"id": "todo_only", "label": "Only TODO (Incomplete) — scan for unmitigated vulnerabilities"}`
  - `{"id": "all_statuses", "label": "All statuses (DONE + TODO) — full scan"}`

Store `task_status_filter`.

**Q-S4 — Verification status filter:**

Ask via `ask_question`:
- **Prompt:** "Filter by existing verification status?"
- **Options:**
  - `{"id": "unverified", "label": "Only unverified (none) — skip CMs that already have a pass/partial/fail verdict"}`
  - `{"id": "unverified_and_fail", "label": "Unverified + previously failed — re-check failures"}`
  - `{"id": "no_filter", "label": "No filter — verify all regardless of prior verification status"}`

Store `verification_status_filter`.

Apply both filters to build the in-memory CM list. Each entry gets:
- `id`, `full_id` (from SDE response)
- `sde_task_status` — the actual SDE task status (`DONE` / `TODO` / `NA`), preserved for audit
- `files_modified = []` (empty — standalone mode has no apply-fixes record; file discovery happens in subagent B1.7)
- `category` — from the SDE CM's phase/category field (available in the `expand` response)

CMs with task status `NA` are always excluded (not applicable = nothing to verify).

**[CHECKPOINT]** `Standalone mode: {N} countermeasures fetched from project {project_name} (ID: {project_id}) | task_status_filter: {task_status_filter} | verification_filter: {verification_status_filter}`

User confirmation:
> "Found {N} countermeasures in project {project_name} matching your filters (task_status={task_status_filter}, verification={verification_status_filter}). Proceed to scope selection? [Proceed / Cancel]"

If the user declines, the skill aborts.

After the checkpoint, proceed to **Step A1.6** (Risk Policy Check + Confirm) and then **Step A1.5+A3** (resume + scope selection). **DO NOT start Phase B or launch subagents yet -- the user MUST select a scope via `ask_question` first.**

### Step A1.6. Risk Policy Check + Confirm

> Runs in ALL modes once `project_id` is known (handoff: from the handoff file; standalone: Step A1-S). Read-only: the skill DISPLAYS the project's current SDE risk policy and asks the user to confirm. It does NOT change the policy.

1. Call `project` with `op: "get"` and `project_id` (reuse a prior `project op=get` response if one was already fetched) and read the current `risk_policy`.
2. Display:
   - If set: `Current risk policy for this project: {policy_name} (ID: {policy_id})`
   - If unset: `Current risk policy for this project: (none set)`
3. Ask via `ask_question`:
   - **Prompt:** "This project's risk policy (shown above) determines which countermeasures are in scope. Proceed with verification using this risk policy?"
   - **Options:**
     - `{"id": "proceed", "label": "Proceed — verify against this risk policy"}`
     - `{"id": "cancel", "label": "Cancel — I'll change the risk policy in SD Elements first, then re-run"}`
4. On `cancel` → **HARD STOP**: "Aborted at user request. Change the project's risk policy in SD Elements, then re-run this skill." The skill NEVER modifies the risk policy.
5. Store `risk_policy_id` and `risk_policy_name` (for the Step A7 plan summary and the handoff record).

**[CHECKPOINT]** `Risk policy: {policy_name} (ID: {policy_id}) — confirmed` (or `Risk policy: (none set) — confirmed`)

### Step A1.5+A3. Resume from Prior Verification Run + Scope Selection

> **When a prior run exists, this step presents BOTH the resume choice and the scope choice in a single `ask_question` call (two questions, one batch).** This eliminates unnecessary back-and-forth. When no prior run exists, only the scope question is presented.
>
> **HARD GATE (scope): The scope MUST be selected by the user via `ask_question`. You MUST NOT infer, assume, or default to any scope. If the user's initial message implies a scope (e.g., "verify all CMs"), you still MUST present the `ask_question` menu and let the user explicitly confirm. If scope is not collected here, Step A7's MATCH check will fail (scope is one of the required inputs — 9 in handoff mode, 11 in standalone; see Step A7) and Phase B cannot start.**

**Phase 1 — Detect and reconcile prior run:**

Check whether a `.sde-verification-handoff.json` already exists at `{repository_path}/.sde-verification-handoff.json`. If it does:

1. **Load and validate** it (must have `source_skill == "code-scan-verification-validation"` and a valid `verification_results[]`).
2. **Extract the set of already-verified CM IDs** — all entries in `verification_results[]` that have `status` in `{pass, partial, fail}` (i.e., CMs where a verdict was derived, regardless of whether the POST succeeded).
3. **Reconcile against the canonical CM source** using set subtraction. The canonical source depends on the mode:
   - **Handoff mode:** `handoff["countermeasures"]` where `cm["status"] == "Applied"`
   - **Standalone mode:** the filtered CM list from Step A1-S.3
   ```python
   # Handoff mode:
   canonical_cm_ids = {cm["full_id"] for cm in handoff["countermeasures"] if cm["status"] == "Applied"}
   # Standalone mode:
   canonical_cm_ids = {cm["full_id"] for cm in standalone_cm_list}

   prior_verified_ids = {r["full_cm_id"] for r in prior["verification_results"] if r["status"] in ("pass", "partial", "fail")}
   already_done = canonical_cm_ids & prior_verified_ids
   still_todo = canonical_cm_ids - prior_verified_ids
   spurious = prior_verified_ids - canonical_cm_ids
   ```
4. **Warn about spurious entries** (CMs in the prior verification results that are NOT in the canonical set):
   ```
   [WARN] Prior verification contains {len(spurious)} entries not in canonical CM set: {list(spurious)[:10]}
   These will be ignored during reconciliation.
   ```
5. Set `has_prior_run = true`.

If no `.sde-verification-handoff.json` exists, set `has_prior_run = false`.

**Phase 2 — Combined ask_question:**

**When `has_prior_run == true`:** present TWO questions in a single `ask_question` call:

- **Q1 — Resume:** "Found prior verification run ({len(already_done)} CMs already verified, {len(still_todo)} remaining). Resume or start fresh?"
  - `{"id": "resume", "label": "Resume — skip the {len(already_done)} already-verified CM(s), verify the remaining {len(still_todo)}"}`
  - `{"id": "fresh", "label": "Start fresh — ignore prior run, re-verify from scratch"}`

- **Q2 — Scope:** "Which countermeasures should I verify?"
  - `{"id": "one_cm", "label": "Verify a single CM by ID"}`
  - `{"id": "multi_cm", "label": "Verify multiple specific CMs by ID"}`
  - `{"id": "all", "label": "Verify all in-scope CMs (handoff: Applied only — Skipped and Documented excluded; standalone: all filtered CMs from SDE)"}`
  - `{"id": "one_by_one", "label": "One-by-one mode: walk through each in-scope CM with individual yes/skip/stop confirmation"}`

Both Q1 and Q2 MUST be in the same `ask_question` call so the user answers them together.

- If Q1 = `resume`: filter `in_scope` to `still_todo` only; carry forward `already_done` results into the final handoff.
- If Q1 = `fresh`: ignore the prior file; proceed as if no prior run exists.

**When `has_prior_run == false`:** present only the scope question (Q2 above) in a single `ask_question` call. Emit `[CHECKPOINT] Resume: starting fresh (no prior run)`.

**Phase 3 — CM ID follow-up (if needed):**

**Immediately after the user selects `one_cm` or `multi_cm` in Q2, prompt for the CM ID(s) BEFORE proceeding to Step A4.** This ensures the execution plan (Step A7) already contains the resolved CM list.

- **`one_cm` shortcut:** `"Enter the CM ID to verify (e.g., T123):"` -> validates exactly 1 ID.
- **`multi_cm` shortcut:** `"Enter one or more CM IDs separated by commas (e.g., T123,T145,T200):"` -> validates 1+ IDs.

The `one_cm` and `multi_cm` menu shortcuts both resolve to the canonical internal scope `selected_cms` (the only difference is the follow-up prompt copy and how many IDs are accepted). This skill's **verification** handoff (`.sde-verification-handoff.json`) stores the three canonical values: `all` / `selected_cms` / `one_by_one`. Note: the **upstream** apply-fixes handoff (`.sde-apply-handoff.json`) may contain legacy scope values (`domain=...`, `single_cm=...`, `one_by_one`) from apply-fixes' own scope selection — this field is read-only audit metadata and is NOT used to drive `filter_by_scope`. Verification always uses the user's own scope selection from this step. (The pre-3.2.0 `domain` scope was removed in beta-3.2.0 — `.sde-apply-handoff.json` does not carry CM domain data, so domain-scoped filtering was never realisable at the filter stage. Use `selected_cms` to verify a curated subset.)

`scope_args` for `selected_cms` is `{"cm_ids": [str, ...]}` (length >= 1, all IDs must exist in the canonical CM source — handoff mode: `handoff["countermeasures"]`; standalone mode: Step A1-S.3 filtered CM list — or HARD STOP).

**`Skipped` and `Documented` CMs are excluded by default** from `all` and `one_by_one` — there is nothing to statically verify (see "Scope of static verification" section). They reach the loop only via `selected_cms` when the user explicitly lists their IDs.

**`selected_cms` warning hooks (after ID collection, before loop):**

1. If any selected ID has `cm.status == "Documented"`, prompt once:
   > "You selected {N_doc} documentation-only CM(s): {ids}. Static verification will silently skip these (out of scope; see 'Scope of static verification'). Continue?"
   - `{"id": "yes_skip_docs", "label": "Yes — skip those silently, verify the rest"}` (proceeds with the full list; B0 short-circuits the doc-only ones inside the loop)
   - `{"id": "drop_docs", "label": "Drop the doc-only IDs and continue with the rest"}` (filters them out before the loop)
   - `{"id": "cancel", "label": "Cancel and re-pick"}`

2. If any selected ID has `cm.status == "Skipped"`, surface an info-only line (no prompt — the forced-`fail` lane is well-defined):
   > "Note: {N_skipped} CM(s) you selected were marked Skipped by apply-fixes ({ids}); they will receive a forced fail / high verdict."

If `one_by_one` is selected and the in-scope count is **> 20**, warn:

> "You selected one_by_one for {N} CMs. This will require {N} confirmations. Proceed? [Yes / Switch to all]"

**Legacy compatibility:** older handoffs and scripts may pass `scope: "single_cm"` (the pre-3.1.3 name). The skill aliases `single_cm` -> `selected_cms` on load and emits a one-time deprecation warning.

**[CHECKPOINT]** `Resume: {len(already_done)} CMs from prior run; {len(still_todo)} remaining` OR `Resume: starting fresh (no prior run or user declined)`

**[CHECKPOINT]** `Scope: {scope}` (emitted immediately after both resume and scope are resolved)

### Step A2. Git Tree Safety + Branch Checkout

Before ANY `git checkout`:

```bash
cd {repository_path}
git status --porcelain
```

- If output is **non-empty** → **HARD STOP** with:
  > "Working tree is dirty. Stash or commit your changes before running code-scan-verification-validation."
- If output is **empty** → proceed.

**Branch checkout (mode-dependent):**

- **Handoff mode:** if `handoff.security_branch` is set, run `git checkout {handoff.security_branch}`. If the branch does not exist locally, report it and ask the user whether to proceed on the current branch (degraded mode — verdicts may be misleading).
- **Standalone mode:** no `security_branch` is available from a handoff. Ask via `ask_question`:
  - **Prompt:** "Which branch should I verify? (current: `{current_branch}`)"
  - **Options:**
    - `{"id": "current", "label": "Stay on current branch ({current_branch})"}`
    - `{"id": "other", "label": "Switch to a different branch"}`
  - If `other`: follow-up text prompt for branch name; run `git checkout {branch}`. If the branch does not exist, HARD STOP.

**[CHECKPOINT]** `Git tree clean; checked out {branch_name}`

### Step A3. (Merged into Step A1.5+A3)

Scope selection has been merged into Step A1.5+A3 above. If you reach this step, scope and resume have already been collected. Proceed to Step A4.

### Step A4. Fail-Verdict Status-Rollback Opt-In

Creating a Verification Note via `verification op=create` updates the task's derived **verification status** (`pass` / `partial` / `fail` / `none`). It can also atomically set the task's **countermeasure (task) status** (`TODO` / `DONE` / `NA`) via the optional `task_status_mapping` field. These are two separate concepts (see "Status concepts" section above). A `pass` verdict should always bump the task to `DONE`. A `fail` verdict, however, could undo the `DONE` that `apply-fixes` set, which is destructive if the user is mid-review.

Ask the user:

- **Prompt:** "If a CM verifies as FAIL, should I also roll its SDE task status back to TODO?"
- **Options:**
  - `{"id": "no_verification_only", "label": "No — only update verification_status, leave workflow status alone (recommended)"}`
  - `{"id": "yes_rollback", "label": "Yes — also set task status to TODO on fail"}`

Regardless of the answer, `pass → DONE` is **always** sent. Partial verdicts never touch workflow status.

**[CHECKPOINT]** `Scope: {scope}; fail-rollback: {yes_rollback | no_verification_only}`

### Step A5. Batch Size Selection

**Auto-skip guard:** If `scope == "selected_cms"` and the resolved CM list contains exactly 1 CM, set `batch_size = 1` and skip this step entirely (there is nothing to batch). Output:
```
[CHECKPOINT] Batch size: 1 (auto — single CM selected); parallel subagents: 1
```

Otherwise, ask the user via `ask_question`:

- **Prompt:** "How many CMs should each verification batch contain? (Each batch processes N CMs sequentially. Higher = fewer launches but more per-batch context usage. If inline fallback activates in Step A6, batch size is forced to 1.)"
- **Options:**
  - `{"id": "1", "label": "1 — one CM per subagent (original behavior, slowest but most isolated)"}`
  - `{"id": "5", "label": "5 — small batches"}`
  - `{"id": "10", "label": "10 — recommended for 100+ CMs (default)"}`
  - `{"id": "20", "label": "20 — aggressive batching (for very large projects)"}`

Store `batch_size` as an integer. Default is 10 if the user does not override.

**[CHECKPOINT]** `Batch size: {batch_size}; parallel subagents: 5`

### Step A6. Subagent Capability Probe

Per the SUBAGENT / DELEGATION POLICY (top of this file), subagent batching is permitted in ANY environment (including Cursor) provided the subagent `model` is set explicitly to the parent's model and is NEVER `composer-2.5-fast`. Run the probe:

1. Determine the parent agent's model. Attempt to launch a trivial `generalPurpose` subagent with `model` set explicitly to the parent's model (e.g., a prompt that returns a known string). If it succeeds, set `execution_mode = "subagent"` and proceed to Step A7.
2. If you CANNOT set the subagent's `model` to the parent's model (or the launch fails / `generalPurpose` is unavailable), activate **inline fallback mode**: set `execution_mode = "inline"`. Inline is the fallback ONLY when same-model delegation is unavailable — it is NOT forced by environment.

**Inline fallback mode activation:**

```
[WARN] This MCP client does not support subagent generation.
Verification will run INLINE in the parent context.
Large CM sets may exhaust the context window.
Batch size forced to 1; parallel dispatch disabled.
```

- `batch_size` is forced to `1` (process CMs one at a time inline). The user's Step A5 selection is overridden.
- Parallel dispatch is disabled (only one CM processed at a time).
- **Context-window warnings:**
  - If `in_scope_total > 20`: `"[WARN] {in_scope_total} CMs will run inline. Context exhaustion is likely. Consider reducing scope to selected_cms with a smaller set."`
  - If `in_scope_total > 50`: `"[HARD RECOMMEND] {in_scope_total} CMs inline will almost certainly exhaust the context window. Strongly recommend reducing scope to selected_cms (max ~20 CMs) or using one_by_one mode. Proceed anyway? [Proceed / Reduce scope]"` — if `Reduce scope`, return to Step A1.5+A3.
- **Context checkpointing:** After every 5 CMs processed inline, the agent outputs a `=== CONTEXT CHECKPOINT ===` block (see Context Limit Handling below) so the user can resume if the window runs out.
- **Rule 12 relaxation (AGENTS.md Rule 9):** In inline fallback mode, B1 fetch, B2 analysis, B3 verdict, B4 note-fetch, and B5 POST run in the parent context instead of a subagent. This is the ONLY exception to Rule 12's "subagents only" constraint.

**[CHECKPOINT]** `Execution mode: {subagent | inline}` (if inline, also `batch_size forced to 1; context-window warning issued`)

### Step A7. Execution Plan Summary + Confirmation

After the subagent probe, the agent MUST output the Phase A verification block summarizing every collected input (including `execution_mode` from A6) and wait for user confirmation. This serves as both the Phase A verification gate and the execution plan the user reviews before authorizing the run.

```
=== PHASE A VERIFICATION — EXECUTION PLAN ===
Mode: {verification_mode}
Repository: {repository_path}
Branch: {branch_name}
CM source:
  (handoff)    Handoff file: {N} CMs ({A} Applied / {D} Documented / {S} Skipped)
  (standalone) SDE project: {project_name} (ID: {project_id}), {N} CMs
               task_status_filter: {task_status_filter}
               verification_filter: {verification_status_filter}
Risk policy: {risk_policy_name} (ID: {risk_policy_id}) [confirmed] | (none set) [confirmed]
Resume: {resuming from prior ({already_done} done, {still_todo} remaining) | fresh start}
Scope: {scope} {scope_args if selected_cms} (user-selected in A1.5+A3: YES)
Fail-rollback: {yes_rollback | no_verification_only}
Execution mode: {subagent | inline}
Batch size: {batch_size} | parallel: {5 if subagent, 1 if inline}
Estimated launches: {ceil(in_scope_total / batch_size)} {subagent batches | inline iterations}

Inputs gathered: {count}/{expected}
MATCH: {count} == {expected}? {YES/NO}
==============================================
```

Print the line matching the current `verification_mode`; omit the other.

**Scope gate (before counting):**
```python
assert scope_was_user_selected, \
    "HARD STOP: scope was not collected via ask_question in Step A1.5+A3. Return to A1.5+A3."
```
If `scope` is not set or was not gathered via an explicit `ask_question` call in Step A1.5+A3, the MATCH check below MUST fail. Do NOT infer a default scope to make it pass.

**Expected input count:** handoff mode = 10 (MCP, mode+repo, handoff confirm, risk-policy confirm, resume, git, scope, fail-rollback, batch size, subagent probe); standalone mode = 12 (adds project selection and SDE status filters). The Step A1.6 risk-policy confirm is gathered in ALL modes.

**If MATCH = NO:** return to the first missing Phase A step and re-collect. Do NOT proceed until YES.

**If MATCH = YES:** ask via `ask_question`:
- **Prompt:** "Proceed with this execution plan?"
- **Options:**
  - `{"id": "proceed", "label": "Proceed — start Phase B verification"}`
  - `{"id": "cancel", "label": "Cancel — abort the skill"}`

If `cancel`, the skill aborts. Only on `proceed` does Phase B begin.

**[CHECKPOINT]** `Phase A complete: {count}/{expected} inputs gathered; user confirmed execution plan`

---

## Phase B: Per-CM Verification Loop

Phase B is a **parent-orchestrator + batched-verification** architecture. The parent loop does scope filtering, short-circuit lanes (mode-dependent — see below), the `one_by_one` user prompt, progress output, and result-recording — nothing else. For each batch of in-scope CMs that survive the parent short-circuits: when `execution_mode == "subagent"`, the parent dispatches **one `generalPurpose` subagent per batch** which performs the full B1 + [B1.5 or B1.7] + B2 + B3 + B4 + B5 cycle for each CM in its batch, sequentially, within its own isolated context (fetch ctx via MCP -> AI analysis on files -> fetch existing notes -> POST verification note via MCP), and returns a **JSON array** of small structured results; when `execution_mode == "inline"` (Step A6 fallback), the parent itself executes the same B1+B2+B3+B4+B5 cycle in-context with `batch_size=1`. When `execution_mode == "subagent"`, no `ctx`, no file contents, no payload ever lives in the parent's conversation history. When `execution_mode == "inline"`, context does accumulate in the parent — see Step A6 context checkpoints.

**Mode-dependent parent short-circuits:**

- **Handoff mode:** two to four lanes — B0a (Documented out-of-scope), B0b (upstream-Skipped forced-fail), and when `handoff_version == "2"` provides `cm.category`: B0b2 (code-CM empty-files forced-fail), B0b3 (non-code-CM empty-files out-of-scope). When `handoff_version == "1"` (no `cm.category`), the empty-`files_modified[]` discriminator is enforced inside the subagent (L-FF2-sub / L-OOS-sub in B1.5).
- **Standalone mode:** no handoff-derived short-circuits (B0a/B0b/B0b2/B0b3 are all inapplicable because there is no upstream `status` or `files_modified[]` from apply-fixes). All CMs pass through to per-CM verification (via subagent or inline — see Step A6). The verification context performs **file discovery** (B1.7) before analysis (B2). The only parent-level gate is B0c (`one_by_one` user prompt).

The architecture exists to bound parent context across large projects: a 431-CM project with inline execution would accumulate ~431 ctx blobs (incl. fat `how_tos[]`) + ~1000+ file contents + 431 prompts + 431 payloads in the parent, blowing out the context window. With batched-subagent dispatch (default `batch_size=10`), the parent retains only ~431 small verdict-summary records across ~44 subagent launches (instead of 431). Each subagent's context holds ~10 MCP responses + ~10-30 file reads, well within subagent context limits.

### Batching and Retry/Timeout

**Batch size** is configurable via Step A5 (default 10). CMs that survive the parent short-circuits (handoff mode: B0a/B0b/B0b2/B0b3/B0c — where B0b2/B0b3 fire only when `handoff_version == "2"`; standalone mode: B0c only) are collected into batches of `batch_size` CMs. When `execution_mode == "subagent"`, each batch is dispatched to one `generalPurpose` subagent and up to 5 subagents may be dispatched in parallel per round (so each round processes up to `5 × batch_size` CMs). When `execution_mode == "inline"`, batches are processed sequentially in-context with `batch_size=1` (see Step A6 inline fallback).

### Batch plan + per-batch mini-gate (T5 — anti-sampling)

**ANCHORING RULE:** the loop denominator `in_scope_total` MUST come from the source of truth (the scope-filtered CM set from Step A1.5+A3 — handoff `verification_results` source or the standalone A1-S.3 filtered list), NEVER from "CMs processed so far." Emit the batch plan ONCE before the loop; it IS your execution contract:

```
=== PHASE B BATCH PLAN ===
in_scope_total (from source of truth): {N}
Batch size: {B}   Total batches: {ceil(N/B)}
Batch 1/{t}: {cm_ids...}   ...   Batch {t}/{t}: {cm_ids...}
==========================
```

Per batch, after the subagent returns (or inline processing completes) AND each result is offloaded to disk (T6):

```
--- BATCH {k}/{t} COMPLETE ---
Expected (this batch): {b_k}   [VERIFY] lines emitted: {c}   Disk artifacts written this batch: {d}   BATCH PASS: {c}=={b_k} AND {d}=={b_k}? {YES/NO}
[RUNNING CHECK] disk artifacts total {disk}/{N} | batches {k}/{t} | on track? {Y/N} | reloaded §Phase B from disk? YES | sentinel: "{verbatim line}"
---
```

If `BATCH PASS = NO`: reprocess the missing CMs in THIS batch and re-run the mini-gate; do NOT advance until YES. The count of individually processed CMs (per-CM `[VERIFY]` + per-CM disk artifact) is the ONLY basis for the completion gate — never a summary judgment.

**Gate-the-gate precondition (Phase B completion block is INVALID if unmet):** the `=== PHASE B BATCH PLAN ===` header was emitted, AND a `--- BATCH k/t COMPLETE ---` mini-gate appeared for EVERY batch (count of mini-gates == total batches).

### Anti-sampling (T8 — 3 layers + ban-phrase HARD STOP)

Three independent layers prevent the loop from stopping early or sampling:
1. **Durable per-CM disk proof** — one `.sde-security/verify/{project_id}/cm-work/{full_cm_id}.json` per in-scope CM (T6); `verify_disk_vs_sde` counts them.
2. **Gate-the-gate** — the completion block cannot be filled until the BATCH PLAN + a mini-gate for EVERY batch exist (above).
3. **Ban-language HARD STOP** — if ANY of these phrases appears in your reasoning about loop scope, STOP, discard the conclusion, return to the BATCH PLAN, and process every remaining in-scope CM: "key CMs" / "across all categories" / "the pattern is clear" / "the rest have/are" / "only N ..." / "N+" / "representative" / "pragmatic" / "efficient" / "Let me finalize" (pre-completion) / "move forward to more impactful steps".

The count of individually processed CMs (per-CM `[VERIFY]` + per-CM disk artifact) is the ONLY basis for the completion gate — never a summary judgment or in-memory tally.

**Retry/timeout** protects against subagent startup stalls:

- **Timeout:** If a subagent does not return within `subagent_timeout_ms` (default 300000 = 5 minutes), the parent kills it and re-launches with the same batch.
- **Max retries:** 2 retries per batch (3 total attempts). After exhaustion, every CM in the batch is recorded as `partial`/`low` with finding category `subagent-timeout` and `note_post_status="FAILED:subagent-timeout"`.
- Timeout/retry is transparent to the subagent — the subagent prompt and procedure are identical on each attempt.

### No-False-Positives Invariant (CANONICAL)

> **No false positives. Negative signal is canonical; positive signal is corroborative. Recognition is corroborative; absence-of-vulnerability is canonical.**
>
> A `fail` verdict requires **CITED, CONCRETE EVIDENCE** of a vulnerability — exactly four sources are allowed:
> 1. a residual vulnerable pattern matching `ctx.problem`, cited at a specific file:line, OR
> 2. a residual marker comment (`vuln-code-snippet`, `VULNERABLE`, `TODO: fix`, etc.), cited at a specific file:line, OR
> 3. an upstream forced-fail signal: `cm.status == "Skipped"` (parent short-circuit B0b) **(handoff mode only)**, OR
> 4. empty `files_modified[]` for a CODE_FIX/ML_CODE CM (parent B0b2 when `handoff_version == "2"`, subagent L-FF2-sub when v1) **(handoff mode only)**.
>
> **Standalone mode uses only sources (1) and (2).** Sources (3) and (4) are inapplicable because standalone mode has no upstream `Skipped` status or apply-fixes `files_modified[]`.
>
> **Absence of the canonical mitigation pattern is NEVER a `fail` criterion.**
> **Failure to recognise the developer's mitigation style is NEVER a `fail` criterion.**
> **If Q1 is `absent_high_confidence` and the marker scan is clean, the verdict is `pass` — regardless of Q2 (canonical mitigation match) and Q3 (alternative mitigation recognition).**
> **An empty or partially populated `ctx.how_tos[]` is NOT a degraded path. Q2 is OPTIONAL — it runs only when `ctx.how_tos[]` is non-empty AND has at least one language-applicable entry. Otherwise Q2 is skipped entirely and the matrix collapses to Q1 + Q3 + marker scan; `Q1 = absent_high_confidence` + clean markers yields `pass`/`high` regardless of whether Q2 ran.**
>
> `partial` is reserved for **genuine analysis ambiguity** (Q1 = `ambiguous`: AI cannot determine whether the vulnerability is present — obfuscated code, indirect data flow, partial coverage) and for context-fetch failures (404/5xx/timeout/network). It is **NOT** a substitute for `pass` when the AI is confident no vulnerability exists. `partial` is also the verdict for malformed subagent returns (a parse error is not vulnerability evidence; recording it as `fail` would itself be a false positive).
>
> Q2 (canonical mitigation pattern from `ctx.how_tos`, optional — see above) and Q3 (semantic-equivalence alternative mitigation) are corroborative — they enrich findings and rationale. They do **NOT** gate the verdict.

This invariant appears in five places: this section (full callout), Step B3 verdict matrix preamble (full callout, content-identical), the Numbered Enforcement Rules (Rule 5, abbreviated reference + 4-source list), AGENTS.md Rule 5 (full callout, content-identical with this section), and the Subagent Prompt Template appendix (the template is plain text inside a code fence so it cannot use Markdown blockquote syntax, and uses section headers to distinguish handoff/standalone fail sources instead of inline annotations). All five mentions are content-equivalent: they convey the same four fail sources, the same "(handoff mode only)" scope restriction on sources (3) and (4), and the same standalone-mode clarification.

### Parent loop pseudocode

```python
# CM source depends on mode
if verification_mode == "handoff":
    cm_source = handoff["countermeasures"]
else:  # standalone
    cm_source = standalone_cm_list  # built in Step A1-S.3

in_scope = filter_by_scope(cm_source, scope, scope_args)
in_scope_total = len(in_scope)
done = 0
results = []

if in_scope_total == 0:
    print("[INFO] No in-scope CMs after filtering. Nothing to verify; writing empty handoff.")
    # falls through to handoff emission with all-zero totals; Sum check 0 == 0 → YES

# ── Phase 1: Parent short-circuits ────────────────────────────────────
# These run per-CM BEFORE batching. CMs consumed here never enter a batch.
# In handoff mode: B0a/B0b always fire; B0b2/B0b3 fire only when handoff v2.
# In standalone mode: B0a/B0b/B0b2/B0b3 are all SKIPPED (no upstream status
#   or files_modified from apply-fixes). Only B0c (one_by_one prompt) applies.
subagent_eligible = []
aborted = False
for cm in in_scope:
    done += 1

    # ── Handoff-mode-only short-circuits ──
    if verification_mode == "handoff":

        # Step B0a. Documented under selected_cms — defensive guard.
        if cm.status == "Documented":
            results.append(record_out_of_scope(cm, reason="documentation-only CM; static verification not applicable"))
            print(f"[SKIP-OOS] {done}/{in_scope_total} | {cm.full_id} | out-of-scope (Documented)")
            continue

        # Step B0b. Upstream-Skipped — forced fail/high + B4+B5 POST.
        if cm.status == "Skipped":
            verdict = forced_fail(cm, reason="CM was skipped by apply-fixes; no mitigation present", category="residual-vulnerable-pattern")
            existing_notes = fetch_existing_notes(project_id, cm.full_id)  # B4 inline
            post_status = post_verification_note(project_id, cm, verdict, existing_notes)  # B5 inline
            results.append(record_verified(cm, verdict, note_post_status=post_status))
            print(f"[VERIFY] {done}/{in_scope_total} | {cm.full_id} | verdict=fail | confidence=high | note={post_status}")
            continue

        # Step B0b2. Parent code-CM forced-fail (handoff v2 only) + B4+B5 POST.
        if handoff_has_category and cm.category in ("CODE_FIX", "ML_CODE") and len(cm.files_modified) == 0:
            verdict = forced_fail(cm, reason="code CM (CODE_FIX/ML_CODE) with no modified files", category="residual-vulnerable-pattern")
            existing_notes = fetch_existing_notes(project_id, cm.full_id)  # B4 inline
            post_status = post_verification_note(project_id, cm, verdict, existing_notes)  # B5 inline
            results.append(record_verified(cm, verdict, note_post_status=post_status))
            print(f"[VERIFY] {done}/{in_scope_total} | {cm.full_id} | verdict=fail | confidence=high | note={post_status} (parent B0b2)")
            continue

        # Step B0b3. Parent non-code-CM out-of-scope (handoff v2 only).
        if handoff_has_category and cm.category in ("INFRA", "ML_DOC") and len(cm.files_modified) == 0:
            results.append(record_out_of_scope(cm, reason="non-code CM with no modified files; static verification not applicable (parent B0b3)"))
            print(f"[SKIP-OOS] {done}/{in_scope_total} | {cm.full_id} | out-of-scope (parent B0b3: {cm.category}, empty files_modified)")
            continue

    # (standalone mode: no handoff-derived short-circuits — all CMs proceed to batching)

    # Step B0c. one_by_one user prompt (parent loop).
    if scope == "one_by_one":
        show_cm_summary(cm)
        resp = ask_question("Verify this CM?", ["yes", "skip", "stop"])
        if resp == "skip":
            results.append(record_skipped(cm, reason="user skipped"))
            print(f"[SKIP-USER] {done}/{in_scope_total} | {cm.full_id} | user skipped")
            continue
        if resp == "stop":
            results.append(record_skipped(cm, reason="user stopped (loop terminated at this CM)"))
            for c in in_scope[done:]:
                results.append(record_skipped(c, reason="user stopped (loop terminated; not reached)"))
            remaining_recorded = 1 + (in_scope_total - done)
            print(f"[STOP] User stopped at {done}/{in_scope_total}; recorded {remaining_recorded} CMs as user-stopped to preserve Sum-check identity")
            aborted = True
            break

    subagent_eligible.append(cm)

# ── Phase 2: Batched subagent dispatch ─────────────────────────────────
# CMs that survived B0a/B0b/B0b2/B0b3/B0c are split into batches of `batch_size`.
# Up to `parallel_subagents` (default 5) batches are dispatched concurrently.
# Each subagent processes its batch sequentially (B1+B2+B3+B4+B5 per CM) and
# returns a JSON array of per-CM results. Retry/timeout protects against stalls.

SUBAGENT_TIMEOUT_MS = 300_000   # 5 minutes
MAX_RETRIES         = 2         # 2 retries = 3 total attempts

if not aborted:
    batches = [subagent_eligible[i:i+batch_size] for i in range(0, len(subagent_eligible), batch_size)]
    batch_done = 0

    for round_start in range(0, len(batches), parallel_subagents):
        round_batches = batches[round_start : round_start + parallel_subagents]

        if execution_mode == "subagent":
            for batch in round_batches:
                cm_ids = [cm.full_id for cm in batch]
                print(f"[VERIFY-DISPATCH] batch {batch_done+1}/{len(batches)} | {len(batch)} CMs: {cm_ids} | subagent launched")
            parallel_results = launch_subagents_parallel(
                [render_batch_subagent_prompt(batch, project_id, security_branch,
                                              task_status_mapping_opt_in, ...)
                 for batch in round_batches],
                timeout_ms=SUBAGENT_TIMEOUT_MS,
                max_retries=MAX_RETRIES,
            )
        else:  # execution_mode == "inline"
            # batch_size == 1, round_batches has exactly one single-CM batch
            cm_ids = [cm.full_id for cm in round_batches[0]]
            print(f"[VERIFY-DISPATCH] batch {batch_done+1}/{len(batches)} | {len(round_batches[0])} CMs: {cm_ids} | inline")
            parallel_results = [run_inline_verification(round_batches[0], ...)]

        for batch, sub_raw in zip(round_batches, parallel_results):
            batch_done += 1

            # Timeout exhaustion: subagent never returned after all retries
            if sub_raw is TIMEOUT:
                for cm in batch:
                    v = make_verdict("partial", "low",
                        findings_for_sde=[{"desc": f"[AI-SAST via Code Scan Verification Validation | {model}] Subagent timed out after retries | verdict=partial confidence=low", "count": "1"}],
                        findings_for_handoff=[{"file": "(n/a)", "line": 0,
                            "description": "subagent did not return within timeout after max retries",
                            "category": "subagent-timeout"}])
                    results.append(record_verified(cm, v, note_post_status="FAILED:subagent-timeout"))
                    done_offset = in_scope.index(cm) + 1
                    print(f"[VERIFY] {done_offset}/{in_scope_total} | {cm.full_id} | verdict=partial | confidence=low | note=FAILED:subagent-timeout")
                continue

            # Parse the JSON array returned by the subagent
            parsed_array = parse_and_validate_batch_output(sub_raw, expected_ids=[cm.full_id for cm in batch])

            if parsed_array.is_error:
                # Entire batch malformed — record all CMs as partial/low
                for cm in batch:
                    v = make_verdict("partial", "low",
                        findings_for_sde=[{"desc": f"[AI-SAST via Code Scan Verification Validation | {model}] Subagent analysis uncertain: malformed return | verdict=partial confidence=low", "count": "1"}],
                        findings_for_handoff=[{"file": "(n/a)", "line": 0,
                            "description": f"subagent returned malformed output: {parsed_array.error}",
                            "category": "analysis-uncertain"}])
                    results.append(record_verified(cm, v, note_post_status="FAILED:subagent-malformed"))
                    done_offset = in_scope.index(cm) + 1
                    print(f"[VERIFY] {done_offset}/{in_scope_total} | {cm.full_id} | verdict=partial | confidence=low | note=FAILED:subagent-malformed")
                continue

            # Process each per-CM result from the batch array
            for cm, parsed in zip(batch, parsed_array.results):
                done_offset = in_scope.index(cm) + 1

                if parsed.is_error:
                    v = make_verdict("partial", "low",
                        findings_for_sde=[{"desc": f"[AI-SAST via Code Scan Verification Validation | {model}] Subagent analysis uncertain: malformed return | verdict=partial confidence=low", "count": "1"}],
                        findings_for_handoff=[{"file": "(n/a)", "line": 0,
                            "description": f"subagent returned malformed output for this CM: {parsed.error}",
                            "category": "analysis-uncertain"}])
                    results.append(record_verified(cm, v, note_post_status="FAILED:subagent-malformed"))
                    print(f"[VERIFY] {done_offset}/{in_scope_total} | {cm.full_id} | verdict=partial | confidence=low | note=FAILED:subagent-malformed")
                    continue

                if parsed.result_kind == "out_of_scope":
                    results.append(record_out_of_scope(cm, reason=parsed.reason))
                    print(f"[SKIP-OOS] {done_offset}/{in_scope_total} | {cm.full_id} | out-of-scope (subagent L-OOS-sub: {parsed.reason})")
                    continue

                if parsed.auth_failure:
                    results.append(record_verified(cm, parsed.verdict, note_post_status="NOT_SENT_AUTH_FAILURE"))
                    # Mark all remaining CMs (rest of this batch + all future batches) as skipped
                    remaining_cms = batch[batch.index(cm)+1:]
                    for future_batch in batches[round_start + round_batches.index(batch) + 1:]:
                        remaining_cms.extend(future_batch)
                    for c in remaining_cms:
                        results.append(record_skipped(c, reason=f"run aborted: auth failure at {cm.full_id}; not reached"))
                    print(f"[VERIFY] {done_offset}/{in_scope_total} | {cm.full_id} | verdict={parsed.verdict.status} | confidence={parsed.verdict.confidence} | note=NOT_SENT_AUTH_FAILURE")
                    print(f"[STOP] Auth failure at {cm.full_id}; aborted run; recorded {len(remaining_cms)} unreached CMs to preserve Sum-check identity. Refresh credentials and re-run.")
                    aborted = True
                    break

                # Normal path
                results.append(record_verified(cm, parsed.verdict, parsed.note_post_status))
                print(f"[VERIFY] {done_offset}/{in_scope_total} | {cm.full_id} | verdict={parsed.verdict.status} | confidence={parsed.verdict.confidence} | note={parsed.note_post_status}")

            if aborted:
                break
        if aborted:
            break
```

Sum-check identity `P + PT + F + S + S_oos == in_scope_total` holds across all paths:

- Parent B0a (Documented under `selected_cms`) contributes to **S_oos**.
- Parent B0b (upstream-`Skipped` forced-fail) contributes to **F**. B4+B5 POST runs inline; contributes to **NP** on success.
- Parent B0b2 (code CM with empty `files_modified[]`, `handoff_version == "2"` only) contributes to **F**. B4+B5 POST runs inline; contributes to **NP** on success.
- Parent B0b3 (non-code CM with empty `files_modified[]`, `handoff_version == "2"` only) contributes to **S_oos**.
- Parent B0c (`one_by_one` user `skip`/`stop`) contributes to **S** (the current CM and every unreached CM).
- Subagent L-FF2-sub (code CM with empty `files_modified[]`, `result_kind="verified"` + `fail`; `handoff_version == "1"` only) contributes to **F**.
- Subagent L-OOS-sub (non-code CM with empty `files_modified[]`, `result_kind="out_of_scope"`; `handoff_version == "1"` only) contributes to **S_oos** (parent dispatches `record_out_of_scope` from the `parsed.result_kind == "out_of_scope"` branch).
- Subagent auth-abort (B1 401/403 or B5 401/403, `auth_failure: true`, `result_kind="verified"`) contributes to **whichever of {P, PT, F} `parsed.verdict.status` maps to** (the current CM — `partial`/low for B1 auth-failure, the B3-computed verdict for B5 auth-failure) **+** S (every unreached CM in all remaining batches, recorded by parent via `record_skipped`).
- Subagent timeout (all retries exhausted) contributes to **PT** (`partial`/low/subagent-timeout) for every CM in the timed-out batch.
- Malformed subagent return contributes to **PT** (`partial`/low/analysis-uncertain) for every CM in the batch.
- Normal subagent return (`result_kind="verified"`, no auth failure) contributes to whichever of {P, PT, F} the verdict resolves to.

`record_out_of_scope(cm, reason)` returns a result entry with `status="skipped_out_of_scope"`, `note_post_status="NOT_SENT_OUT_OF_SCOPE"`, empty `findings_for_handoff`, and no `payload`. The `reason` argument is persisted on the entry's `reason` field (see Step D schema) so downstream tooling can distinguish out-of-scope sub-cases without consulting console logs. These entries are counted in the `Skipped (out of scope)` bucket of the completion block (distinct from user-initiated skips). Note: this `reason` field is per-entry on `verification_results[]`; it is distinct from the existing `failed_cms_for_rework[].reason` field (which only fires for `fail` entries).

`record_skipped(cm, reason)` returns a result entry with `status="skipped"`, `note_post_status="NOT_SENT"`, `confidence="n/a"`, empty `findings`/`findings_for_handoff`, and no `payload`. The `reason` argument is persisted on the entry's `reason` field (see Step D schema) and is free-text; it distinguishes the user-initiated and run-abort no-POST sub-cases: `"user skipped"` (per-CM `skip` in `one_by_one`), `"user stopped (loop terminated at this CM)"` (the `stop` CM the user landed on), `"user stopped (loop terminated; not reached)"` (CMs after the `stop` point), and `"run aborted: auth failure at {full_cm_id}; not reached"` (CMs after a subagent's 401/403). All four are counted in the `Skipped (user)` bucket of the completion block (distinct from `skipped_out_of_scope`). The result entry is **mandatory** for every user-skip / user-stop / run-aborted CM — agents MUST NOT omit it (this is what keeps the Sum-check identity `P + PT + F + S + S_oos == in_scope_total` valid for all paths). Note: this per-entry `reason` field is distinct from `failed_cms_for_rework[].reason` (which only fires for `fail` entries).

`record_verified(cm, verdict, note_post_status)` returns a result entry with `status` from `verdict.status`, `confidence` from `verdict.confidence`, the verdict's `findings_for_handoff` list, and the supplied `note_post_status` ("POSTED" / "FAILED:{reason}" / "NOT_SENT_FORCED_FAIL" / "NOT_SENT_AUTH_FAILURE" / "FAILED:subagent-malformed" / "FAILED:subagent-timeout").

`forced_fail(cm, reason, category)` returns a verdict with `status="fail"`, `confidence="high"`, one `findings_for_sde` entry (`desc=f"[AI-SAST via Code Scan Verification Validation | {model}] {reason} | verdict=fail confidence=high"`, `count="1"`), and one `findings_for_handoff` entry (`file=cm.files_modified[0]` if any else `"(n/a)"`, `line=0`, `description=reason`, `category=category`). The parent runs B4 (fetch existing notes) + B5 (POST verification note) inline for forced-fail lanes — this is a scoped exception to the pure-orchestrator rule (these CMs never enter the subagent pipeline). Any preserved upstream notes from B4 are included as `upstream-note-preserved` findings. If the POST fails after retries, `note_post_status` is `FAILED:{reason}` (the forced-fail verdict is still recorded locally in the handoff).

### Step B-Subagent. Batched Verification (B1 + B2 + B3 + B4 + B5 × N CMs)

When `execution_mode == "subagent"`: each batch is dispatched to a `generalPurpose` task agent (chosen because it has MCP access — required for both `project_countermeasures op=get` in B1 and `verification op=create` in B5; the readonly `explore` type cannot call MCP). The parent renders the canonical Subagent Prompt Template (Appendix) with placeholders substituted and dispatches one subagent per **batch** of surviving in-scope CMs. When `execution_mode == "inline"`: the parent itself executes the same B1 + B2 + B3 + B4 + B5 sequence in-context for `batch_size=1` (see Step A6 inline fallback and Rule 12). In both modes, the verification iterates over its batch sequentially — in handoff mode performing B1 + B1.5 + B2 + B3 + B4 + B5 per CM; in standalone mode performing B1 + B1.7 + B2 + B3 + B4 + B5 per CM — and returns a **JSON array** of per-CM results.

**Subagent input (rendered into the prompt by the parent):**

- `batch[]` — array of CM descriptors, each containing:
  - `cm.full_id` (full SDE task id, e.g., `"31768-T123"`)
  - `cm.id` (numeric task id)
  - `cm.status` — in handoff mode will be `"Applied"` (the `Skipped` and `Documented` lanes are handled by parent short-circuits); in standalone mode this field carries the SDE task status (`DONE` / `TODO`)
  - `cm.files_modified[]` — absolute paths (handoff mode); empty `[]` (standalone mode — file discovery happens in B1.7)
- `verification_mode` — `"handoff"` or `"standalone"` (controls whether B1.5 short-circuits and B1.7 file discovery apply)
- `repository_path` — absolute path to the repo root (used by B1.7 in standalone mode for file discovery)
- `repo_name` — basename of `repository_path` (e.g., `my-app`); used in `finding_ref`
- `project_id`
- `security_branch`
- `task_status_mapping_opt_in` — boolean from Step A4 (whether parent allows `task_status_mapping.fail: TODO` in the payload)
- The verbatim **No-False-Positives Invariant** (see callout above)
- The verbatim **B-Sub procedure** (B1 fetch + B1.5 short-circuit + B1.7 file discovery [standalone only] + B2 analyse + B3 verdict + B4 fetch existing notes + B5 POST, including all retry rules and auth-failure handling — see Appendix)
- The verbatim **Step B3 verdict matrix** (handoff mode: 2 to 4 short-circuit lanes already consumed by parent (B0a, B0b; plus B0b2, B0b3 when `handoff_version == "2"`) + 5 subagent-side lanes + 6-row matrix + mixed-file aggregation rule; standalone mode: no parent short-circuits consumed, subagent B1.5 skipped, B1.7 file discovery added)
- The verbatim **hardcoded residual-marker list**: `vuln-code-snippet`, `VULNERABLE`, `INSECURE`, `TODO: fix`, `FIXME: security`, `<!-- VULNERABLE -->`, `# SECURITY ISSUE`, `// TODO: fix`
- The verbatim **strict JSON return schema** (below — now an array)

**Handoff-mode note:** When `handoff_version == "1"`, `cm.category` is **not** passed by the parent (the field is absent from the handoff). The subagent obtains `ctx.category` from B1's `project_countermeasures op=get` response and uses it in B1.5 to dispatch the subagent-side short-circuit lanes L-FF2-sub and L-OOS-sub. When `handoff_version == "2"`, the parent already has `cm.category` and uses it for B0b2/B0b3 parent-side short-circuits — CMs caught there never reach a subagent. CMs that survive B0b2/B0b3 will still have `ctx.category` fetched in B1 (it's part of the response) and B1.5 acts as a redundant guard.

**Standalone-mode note:** B1.5 is skipped entirely (no upstream `files_modified[]` to gate on). After B1 fetch, the subagent runs **B1.7 File Discovery** to identify which files in the repository are relevant to this CM, then proceeds to B2 with the discovered files.

**Subagent procedure (verbatim in the prompt):**

1. **B1 (fetch):** call MCP `project_countermeasures op=get` with `expand=text,problem,tags,how_tos,name`. On HTTP 401/403 -> set `result_kind="verified"`, set verdict `partial`/`low` with one `context-fetch-failed` finding (description: `"[AI-SAST via Code Scan Verification Validation | {model}] Could not fetch CM context from SDE: HTTP {401|403} | verdict=partial confidence=low"`), set `note_post_status="NOT_SENT_AUTH_FAILURE"`, set `auth_failure: true`, and return immediately (no B1.5, no B2, no B5). The verdict is REQUIRED by the strict-JSON return schema even when `auth_failure: true`. On 404/5xx/timeout/network -> skip B1.5/B2, set `result_kind="verified"`, set verdict `partial`/`low` with one `context-fetch-failed` finding (description: `"[AI-SAST via Code Scan Verification Validation | {model}] Could not fetch CM context from SDE: HTTP {code} | verdict=partial confidence=low"`), skip B5, set `note_post_status="FAILED:fetch-{code}"`, return.
1.5. **B1.5 (subagent short-circuit — handoff mode only, runs only after B1 succeeds):** read `ctx.category` (one of `CODE_FIX | ML_CODE | INFRA | ML_DOC`) from the B1 response. **Skip this step entirely in standalone mode** (proceed to B1.7).
   - **L-FF2-sub** — if `ctx.category in {CODE_FIX, ML_CODE}` AND `len(cm.files_modified) == 0`: a code CM with no modified files IS the cited evidence for `fail`. Set `result_kind="verified"`, verdict `fail`/`high` with one `residual-vulnerable-pattern` finding (`file="(n/a)"`, `line=0`, `description="[AI-SAST via Code Scan Verification Validation | {model}] code CM (CODE_FIX/ML_CODE) with no modified files | verdict=fail confidence=high"`), `reason="code CM with no modified files"`. Skip B2. **Proceed to B4 (fetch existing notes) + B5 (POST)** to ensure the forced-fail verdict is visible in SDE with any upstream note context preserved. Set `note_post_status` from B5 result (`POSTED` on success, `FAILED:{reason}` on failure). Return.
   - **L-OOS-sub** — if `ctx.category in {INFRA, ML_DOC}` AND `len(cm.files_modified) == 0`: a non-code CM with no modified files has nothing on disk to statically verify (apply-fixes Step 7 deletes `skills/`; the SDE UI already shows the relevant context via the `[AI-Documented]` note from upstream and the CM's own `text`/`how_tos`). Set `result_kind="out_of_scope"`, leave `verdict` absent, `reason="non-code CM with no modified files; static verification not applicable"`, `note_post_status="NOT_SENT_OUT_OF_SCOPE"`, skip B2, skip B5, return.
   - **Otherwise** (non-empty `files_modified[]`): proceed to B2.
1.7. **B1.7 (file discovery — standalone mode only, runs after B1 succeeds):** In standalone mode, `cm.files_modified` is always `[]` because there is no apply-fixes record. The subagent must discover which files in the repository are relevant to this CM.
   - **Step 1:** Extract search terms from `ctx.problem` + `ctx.text` + `ctx.how_tos[]` — vulnerability keywords, API/function names, framework patterns, file extensions/types.
   - **Step 2:** Use `grep`/`glob` (via shell tools) within `{repository_path}` to find candidate files matching the search terms. Exclude common non-source directories (`node_modules/`, `.git/`, `__pycache__/`, `dist/`, `build/`, `vendor/`). **Cap:** MAX 200 candidate matches per search term; MAX 500 total candidates before ranking. If limits are exceeded, narrow search terms with more specific patterns or use directory scoping.
   - **Step 3:** AI-rank the candidates by relevance to the CM's vulnerability description (`ctx.problem`). Prioritize files that contain code patterns related to the vulnerability surface (e.g., SQL queries for SQL injection CMs, authentication handlers for auth CMs).
   - **Step 4:** Select top N files (cap at 10 per CM to stay within context budget). Store as `discovered_files[]`.
   - **Step 5:** If no relevant files are found: set `result_kind="verified"`, verdict `pass`/`high` with one `vulnerability-absent` finding (`file="(repo-wide scan)"`, `line=0`, `description="[AI-SAST via Code Scan Verification Validation | {model}] No files relevant to this CM's vulnerability surface found in repository | verdict=pass confidence=high"`), `note_post_status` from B4+B5 (fetch existing notes, then POST), return after B5.
   - **Otherwise** (`discovered_files[]` is non-empty): proceed to B2 using `discovered_files[]` in place of `cm.files_modified[]`.
2. **B2 (analyse) — for each file in `cm.files_modified[]` (handoff mode) or `discovered_files[]` (standalone mode):** ground all reasoning in `ctx.problem` and `ctx.text` (the canonical statement of the vulnerability and the recommended fix). `ctx.how_tos[]` is **optional and corroborative**: many SDE CMs have empty or partially populated `how_tos[]`, and the verdict logic must work correctly in that case.
   - **Detect language/framework** (extension/shebang/manifest hints).
   - **Filter `ctx.how_tos[]` to applicable language(s)** if non-empty. Record skipped how-tos as `not-applicable-how-to-skipped` audit findings (no verdict impact). If `ctx.how_tos[]` is empty or no entries are language-applicable, Q2 is skipped entirely (see below) — this is a normal, not a degraded, path.
   - **Q1 (per file, negative-canonical) — Vulnerability presence.** Driven by `ctx.problem` and `ctx.text` (NOT by `ctx.how_tos[]`). Determine which of three explicit states applies:
     - `absent_high_confidence` — confident vulnerability described in `ctx.problem` is NOT present in this file (clean code path, sink not reachable, parameterised/validated input, etc.).
     - `present_cited` — found a residual vulnerable pattern matching `ctx.problem`; emit `residual-vulnerable-pattern` finding cited at file:line.
     - `ambiguous` — cannot determine (obfuscated code, indirect data flow, partial coverage). Any uncertainty defaults to `ambiguous`, NOT `absent_high_confidence`.
   - **Q2 (per applicable how-to, positive-corroborative) — Canonical mitigation match. OPTIONAL — runs ONLY when `ctx.how_tos` is non-empty AND has at least one language-applicable entry.** For each applicable how-to: is its canonical mitigation pattern present? If yes -> emit `mitigation-confirmed` finding citing the how-to id. Q2 is corroborative only — it never gates the verdict. When Q2 is skipped (empty/non-applicable how-tos), proceed straight to Q3.
   - **Q3 (per file, semantic-equivalence-corroborative) — Alternative mitigation.** ASKED when (a) `ctx.how_tos` is empty or has no applicable entries (Q2 skipped), OR (b) every applicable Q2 returned no. Is some other recognisable mitigation present that prevents `ctx.problem` by the same security property? If yes -> emit `alternative-mitigation-accepted` finding with rationale ("file uses SQLAlchemy ORM `session.query(...).filter_by(...)` which prevents string-concat SQL by the same property as parameter binding described in `ctx.text`"). Q3 is corroborative only.
   - **Marker scan (per file):** scan for the hardcoded marker list. A hit -> emit `residual-marker` finding cited at file:line.
3. **B3 (verdict):** apply the verdict matrix below. The No-False-Positives Invariant is canonical: Q1 is the gate; Q2 and Q3 are corroborative; an empty/inapplicable `ctx.how_tos[]` does NOT degrade confidence — `Q1=absent_high_confidence` + clean markers = `pass`/`high` even when Q2 was skipped.
3.5. **B4 (fetch existing notes — read-then-append):** before building the POST payload, fetch any existing **verification** notes on this CM to preserve prior verification detail. Call `verification` with `op: "list"`, `project_id: {project_id}`, `task_id: {cm.full_id}` to retrieve existing verification/analysis notes. (Note: this is the **verification-note** channel only; apply-fixes' `[AI-Applied]/[AI-Documented]` audit comments live in the separate **countermeasure-note** channel via `project_countermeasures op=addNote` and are intentionally NOT merged here — the three note channels are kept distinct.) If the CM has prior verification notes from earlier runs, extract their description text and store as `existing_notes[]`. On HTTP 404/5xx/timeout/network error: B4 is **non-fatal** — set `existing_notes = []`, emit one `upstream-note-fetch-failed` finding (`file="(n/a)"`, `line=0`, `description="Could not fetch existing notes: {error}"`, `category="upstream-note-fetch-failed"`), and proceed to B5. On HTTP 401/403: treat as auth failure (same as B1 auth path — set `auth_failure: true` and return). When `existing_notes[]` is non-empty, B5 includes an `upstream-note-preserved` finding in the payload (see B5).
4. **B5 (post):** build the payload (`behaviour=combine`, `confidence`, `status`, aggregated `findings`, `finding_ref`, `pinned=false`, `task_status_mapping`). If `existing_notes[]` from B4 is non-empty, append one `upstream-note-preserved` finding per preserved note (`desc="[AI-SAST via Code Scan Verification Validation | {model}] Prior note preserved: {upstream_note_summary, <=200ch} | (audit-only, no verdict impact)"`, `count="1"`). Call `verification` with `op: "create"`, `project_id`, `task_id: {full_id}`, and the payload fields (`behaviour`, `confidence`, `status`, `findings`, `finding_ref`, `pinned`, `task_status_mapping`). Retry/back-off: HTTP 429 sleep 1s + retry once; 5xx retry once after 1s; network retry once after 1s; 401/403 STOP and return `auth_failure: true`; 4xx (other) record `note_post_status="FAILED:{server body}"` and return verdict.

**Loop scopes (read carefully):** Q1 runs **once per file** (not per how-to); Q2 runs **once per (file × applicable how-to)**; Q3 runs **once per file** (only when all Q2 results were no); marker scan runs **once per file**.

**Subagent output (strict JSON array; parent parses and validates):**

The subagent returns a JSON **array** with one element per CM in the batch, in the same order as the input `batch[]` array. Each element has the same schema as the pre-batch single-CM result:

```json
[
  {
    "full_id": "{project_id}-T{n}",
    "result_kind": "verified | out_of_scope",
    "verdict": {
      "status": "pass | partial | fail",
      "confidence": "high | low",
      "findings_for_sde": [{"desc": "...", "count": "N"}],
      "findings_for_handoff": [
        {
          "file": "...",
          "line": 0,
          "description": "...",
          "category": "residual-marker | residual-vulnerable-pattern | mitigation-confirmed | alternative-mitigation-accepted | vulnerability-absent-mitigation-unrecognized | vulnerability-absent | not-applicable-how-to-skipped | analysis-uncertain | context-fetch-failed | scope-mismatch | upstream-note-preserved | upstream-note-fetch-failed"
        }
      ]
    },
    "note_post_status": "POSTED | FAILED:{reason} | NOT_SENT_FORCED_FAIL | NOT_SENT_OUT_OF_SCOPE | NOT_SENT_AUTH_FAILURE",
    "auth_failure": false,
    "reason": "free-text; required when result_kind=='out_of_scope' or for L-FF2-sub forced-fail; empty string otherwise",
    "rationale_summary": "<=300 chars; what the subagent observed and why it picked this verdict (or, for result_kind=='out_of_scope', why the CM was OOS)"
  }
]
```

The array MUST contain exactly `len(batch)` elements. The `full_id` in each element MUST match the corresponding `batch[i].full_id`. If the subagent encounters an `auth_failure` mid-batch, it MUST still return results for all CMs processed so far (including the auth-failure CM) and fill the remaining slots with `result_kind="verified"`, `verdict={status:"partial", confidence:"low", ...}`, `auth_failure: true`, `note_post_status="NOT_SENT_AUTH_FAILURE"`.

**Per-element field semantics** (identical to the pre-batch schema):

- **`result_kind`** is a discriminator. `"verified"` means the subagent produced a verdict (B3 matrix, L-FF2-sub forced fail, or B1 fetch failure). `"out_of_scope"` means the L-OOS-sub lane fired and the parent must record `skipped_out_of_scope`.
- **`verdict`** is REQUIRED when `result_kind=="verified"` and MUST be omitted when `result_kind=="out_of_scope"`.
- **`note_post_status`** is REQUIRED in both branches. Valid values when `result_kind=="out_of_scope"` are `NOT_SENT_OUT_OF_SCOPE` only; when `result_kind=="verified"` any of the other values may apply.
- **`auth_failure`** is REQUIRED in both branches; only ever `true` for the B1/B5 401/403 paths (and those are always `result_kind=="verified"`).
- **`reason`** is free-text and is preserved on the `verification_results[]` entry's `reason` field. REQUIRED for `result_kind=="out_of_scope"` and for the L-FF2-sub forced-fail branch; may be empty string otherwise.

The category `missing-fix` is **NOT** in the enum (deprecated in beta-3.2.0 — was a false-positive vector under the old "no canonical pattern found = problem" rule).

**Subagent failure handling (parent-side):**

- **Timeout (all retries exhausted)** -> parent records every CM in the batch as `verdict=partial` / `confidence=low` / one finding with category `subagent-timeout` and description `"subagent did not return within timeout after max retries"`; `note_post_status="FAILED:subagent-timeout"`. Never `fail` — a timeout is not vulnerability evidence.
- **Malformed JSON / parse error / schema validation failure (entire batch)** -> parent records every CM in the batch as `verdict=partial` / `confidence=low` / one finding with category `analysis-uncertain` and description `"subagent returned malformed output: {error}"`; `note_post_status="FAILED:subagent-malformed"`. Never `fail`.
- **Malformed individual element** -> parent records that specific CM as `partial`/`low`/`analysis-uncertain`; other CMs in the batch use their own parsed results.
- **`auth_failure: true`** (any element in any subagent's batch) -> parent HARD STOPs the loop, records the auth-failure CM with `note_post_status="NOT_SENT_AUTH_FAILURE"`, records every unreached CM (remaining in this batch + all future batches) via `record_skipped(c, reason="run aborted: auth failure at ...; not reached")`, surfaces the remediation message (`Refresh credentials and re-run`), and exits. This preserves Sum-check identity.

### Step B3. Verdict Matrix (CANONICAL)

The verdict matrix is governed by the No-False-Positives Invariant (full callout, byte-identical with the Phase B preamble and AGENTS.md Rule 5):

> **No false positives. Negative signal is canonical; positive signal is corroborative. Recognition is corroborative; absence-of-vulnerability is canonical.**
>
> A `fail` verdict requires **CITED, CONCRETE EVIDENCE** of a vulnerability — exactly four sources are allowed:
> 1. a residual vulnerable pattern matching `ctx.problem`, cited at a specific file:line, OR
> 2. a residual marker comment (`vuln-code-snippet`, `VULNERABLE`, `TODO: fix`, etc.), cited at a specific file:line, OR
> 3. an upstream forced-fail signal: `cm.status == "Skipped"` (parent short-circuit B0b) **(handoff mode only)**, OR
> 4. empty `files_modified[]` for a CODE_FIX/ML_CODE CM (parent B0b2 when `handoff_version == "2"`, subagent L-FF2-sub when v1) **(handoff mode only)**.
>
> **Standalone mode uses only sources (1) and (2).** Sources (3) and (4) are inapplicable because standalone mode has no upstream `Skipped` status or apply-fixes `files_modified[]`.
>
> **Absence of the canonical mitigation pattern is NEVER a `fail` criterion.**
> **Failure to recognise the developer's mitigation style is NEVER a `fail` criterion.**
> **If Q1 is `absent_high_confidence` and the marker scan is clean, the verdict is `pass` — regardless of Q2 (canonical mitigation match) and Q3 (alternative mitigation recognition).**
> **An empty or partially populated `ctx.how_tos[]` is NOT a degraded path. Q2 is OPTIONAL — it runs only when `ctx.how_tos[]` is non-empty AND has at least one language-applicable entry. Otherwise Q2 is skipped entirely and the matrix collapses to Q1 + Q3 + marker scan; `Q1 = absent_high_confidence` + clean markers yields `pass`/`high` regardless of whether Q2 ran.**
>
> `partial` is reserved for **genuine analysis ambiguity** (Q1 = `ambiguous`: AI cannot determine whether the vulnerability is present — obfuscated code, indirect data flow, partial coverage) and for context-fetch failures (404/5xx/timeout/network). It is **NOT** a substitute for `pass` when the AI is confident no vulnerability exists. `partial` is also the verdict for malformed subagent returns (a parse error is not vulnerability evidence; recording it as `fail` would itself be a false positive).
>
> Q2 (canonical mitigation pattern from `ctx.how_tos`, optional — see above) and Q3 (semantic-equivalence alternative mitigation) are corroborative — they enrich findings and rationale. They do **NOT** gate the verdict.

Two to four short-circuit lanes run in the **parent loop** before per-CM verification begins (handoff mode only). The first two (B0a L-OOS, B0b L-FF1) always fire in handoff mode. The next two (B0b2 L-FF2-parent, B0b3 L-OOS-parent) fire **only when `handoff_version == "2"`** (which includes `cm.category`); when `handoff_version == "1"`, these conditions are instead caught inside the per-CM verification context (subagent or inline) via L-FF2-sub/L-OOS-sub. Five more lanes run inside the per-CM verification context (B1.5 + B1 fetch failures): two B1.5 lanes that branch on `ctx.category` for empty `files_modified[]` (redundant with B0b2/B0b3 when handoff v2 but still enforced for v1), and three B1-fetch lanes (one for non-auth fetch errors, two for the auth-failure split B1 vs B5). The 6-row matrix is the AI's analysis-driven verdict for surviving cases (non-empty `files_modified[]`).

**Parent short-circuit lanes (no per-CM verification dispatched):**

| Lane | Trigger | Result | Confidence | Finding | `note_post_status` |
|------|---------|--------|------------|---------|--------------------|
| L-OOS (B0a) | `cm.status == "Documented"` AND `scope == selected_cms` | `skipped_out_of_scope` | n/a | n/a (recorded with `reason`) | `NOT_SENT_OUT_OF_SCOPE` |
| L-FF1 (B0b) | `cm.status == "Skipped"` | `fail` | high | `residual-vulnerable-pattern` ("CM was skipped by apply-fixes; no mitigation present") | `POSTED` (B4+B5 inline; `FAILED:{reason}` if POST fails) |
| L-FF2-parent (B0b2) | `handoff_has_category` AND `cm.category in {CODE_FIX, ML_CODE}` AND `len(cm.files_modified) == 0` | `fail` | high | `residual-vulnerable-pattern` ("code CM with no modified files") | `POSTED` (B4+B5 inline; `FAILED:{reason}` if POST fails) |
| L-OOS-parent (B0b3) | `handoff_has_category` AND `cm.category in {INFRA, ML_DOC}` AND `len(cm.files_modified) == 0` | `skipped_out_of_scope` | n/a | n/a (recorded with `reason`) | `NOT_SENT_OUT_OF_SCOPE` |

**Per-CM verification lanes (run inside the subagent or inline context in B1.5 + B1 fetch error handling, before the matrix):**

| Lane | Trigger | `result_kind` | Verdict | Confidence | Finding | `note_post_status` |
|------|---------|---------------|---------|------------|---------|--------------------|
| L-FF2-sub | B1.5: `ctx.category in {CODE_FIX, ML_CODE}` AND `len(cm.files_modified) == 0` | `verified` | `fail` | high | `residual-vulnerable-pattern` ("code CM (CODE_FIX/ML_CODE) with no modified files") | `POSTED` (B4+B5 runs; `FAILED:{reason}` if POST fails) |
| L-OOS-sub | B1.5: `ctx.category in {INFRA, ML_DOC}` AND `len(cm.files_modified) == 0` | `out_of_scope` | (omitted) | n/a | n/a (recorded with `reason="non-code CM with no modified files; static verification not applicable"`) | `NOT_SENT_OUT_OF_SCOPE` (no B2, no POST) |
| L-FETCH | B1 fetch returns 404 / 5xx / timeout / network error | `verified` | `partial` | low | `context-fetch-failed` | `FAILED:fetch-{code}` (no POST attempted) |
| L-AUTH-B1 | B1 fetch returns 401 / 403 | `verified` | `partial` | low | `context-fetch-failed` ("Could not fetch CM context from SDE: 401/403") | `NOT_SENT_AUTH_FAILURE`; subagent ALSO sets `auth_failure: true`; parent HARD STOPs |
| L-AUTH-B5 | B5 POST returns 401 / 403 (verdict already determined in B3) | `verified` | `pass` / `partial` / `fail` (from B3) | high / low (from B3) | findings already aggregated in B3 | `NOT_SENT_AUTH_FAILURE`; subagent ALSO sets `auth_failure: true`; parent HARD STOPs |

**Main verdict matrix (per-file aggregated; each row is "all files in `cm.files_modified[]` (handoff) or `discovered_files[]` (standalone) agree on this row"):**

| Q1 (per file) | Q2 (per applicable how-to; *skipped when ctx.how_tos empty or no applicable entries*) | Q3 (per file; runs when Q2 was skipped or all Q2=no) | Marker scan (per file) | Verdict | Confidence | Primary finding |
|---|---|---|---|---|---|---|
| `absent_high_confidence` | any Yes (Q2 ran) | -- | clean | `pass` | high | `mitigation-confirmed` (cites how-to id) |
| `absent_high_confidence` | all No (Q2 ran) OR Q2 skipped | Yes (AI rationale) | clean | `pass` | high | `alternative-mitigation-accepted` (cites observed code + security property; cites how-to id only if a how-to existed) |
| `absent_high_confidence` | all No (Q2 ran) OR Q2 skipped | No | clean | `pass` | high | `vulnerability-absent-mitigation-unrecognized` (AI confirms vuln from `ctx.problem` is absent even though it cannot identify the specific mitigation strategy; this is the canonical "negative-signal-canonical" outcome and applies whether or not how-tos existed) |
| `ambiguous` | -- | -- | clean | `partial` | low | `analysis-uncertain` (cites the ambiguity reason) |
| `present_cited` | -- | -- | -- | `fail` | high | `residual-vulnerable-pattern` (cites file:line) |
| -- | -- | -- | hit | `fail` | high | `residual-marker` (cites file:line) |

**Note on empty `ctx.how_tos[]`:** when `ctx.how_tos[]` is empty or has no language-applicable entries, Q2 is skipped entirely. The matrix collapses to Q1 + Q3 + marker scan, which is fully sufficient: `Q1=absent_high_confidence` + clean markers always yields `pass`/`high` regardless of whether Q2 ran. This is by design — the No-False-Positives Invariant treats Q2 as corroborative-only.

**Mixed-file aggregation rule.** If files in the analysis set (`cm.files_modified[]` in handoff mode, `discovered_files[]` in standalone mode) produce different rows, the verdict for the CM is the worst row hit, in this order:
1. any `present_cited` OR any marker hit -> `fail`/high (cite all hits)
2. any `ambiguous` -> `partial`/low
3. all `absent_high_confidence` -> `pass`/high

Findings from ALL files are concatenated (no de-duplication of file-level evidence).

**Hard rules (from the No-False-Positives Invariant):**

- Every `fail` MUST emit at least one finding CITED with `file` + `line` (or, for parent forced-fail lanes L-FF1 / B0b2 and the subagent forced-fail lane L-FF2-sub, with a structured upstream reason and `line=0`).
- **Handoff mode:** the four — and ONLY four — sources of `fail` evidence are: (1) cited `residual-vulnerable-pattern`, (2) cited `residual-marker`, (3) upstream `Skipped` audit status (parent L-FF1), (4) empty `files_modified[]` for CODE_FIX/ML_CODE (parent B0b2 when v2, subagent L-FF2-sub when v1). **Standalone mode:** only sources (1) and (2) apply (there is no upstream `Skipped` status and `files_modified` is always empty by design).
- "Failure to recognise a mitigation" is NEVER a `fail` source.
- "Failure to recognise a mitigation" is NEVER a `partial` source either — `partial` is reserved for AI-side ambiguity (Q1=`ambiguous`), context-fetch failures (L-FETCH), and malformed-subagent-output handling.

#### Aggregating findings for the SDE payload

The subagent collects per-location observations as it analyses each modified file. Before POSTing, observations are **grouped by category** and **one `{desc, count}` entry per non-empty category** is emitted to the SDE payload:

| Category | `desc` template (MANDATORY `[AI-SAST ...]` prefix + detail) | Verdict impact |
|----------|--------------------------|----------------|
| `residual-marker` | `[AI-SAST via Code Scan Verification Validation \| {model}] Residual vulnerability marker(s) in {file_basenames} \| verdict={verdict} confidence={confidence}` | `fail` (canonical) |
| `residual-vulnerable-pattern` | `[AI-SAST via Code Scan Verification Validation \| {model}] Residual vulnerable pattern in {file_basenames}: {ctx.problem summary, ≤120ch} \| verdict={verdict} confidence={confidence}` | `fail` (canonical) |
| `mitigation-confirmed` | `[AI-SAST via Code Scan Verification Validation \| {model}] Mitigation confirmed in {file_basenames}: how-to {how_to_id} pattern present \| verdict={verdict} confidence={confidence}` | corroborative (informs `pass` rationale) |
| `alternative-mitigation-accepted` | `[AI-SAST via Code Scan Verification Validation \| {model}] Alternative mitigation in {file_basenames}: {AI rationale, ≤200ch} \| verdict={verdict} confidence={confidence}` | corroborative (informs `pass` rationale) |
| `vulnerability-absent-mitigation-unrecognized` | `[AI-SAST via Code Scan Verification Validation \| {model}] Vulnerability absent in {file_basenames}: pattern from ctx.problem confidently absent; accepted under no-false-positives invariant \| verdict={verdict} confidence={confidence}` | corroborative (informs `pass` rationale) |
| `not-applicable-how-to-skipped` | `[AI-SAST via Code Scan Verification Validation \| {model}] How-to {how_to_id} ({lang}) skipped: not applicable to {detected_lang} in {file_basenames}` | none (audit) |
| `analysis-uncertain` | `[AI-SAST via Code Scan Verification Validation \| {model}] Analysis uncertain in {file_basenames}: {ambiguity reason} \| verdict={verdict} confidence={confidence}` | `partial` |
| `context-fetch-failed` | `[AI-SAST via Code Scan Verification Validation \| {model}] Context fetch failed: could not retrieve CM data from SDE \| verdict={verdict} confidence={confidence}` | `partial` |
| `scope-mismatch` | `[AI-SAST via Code Scan Verification Validation \| {model}] Scope mismatch in {file_basenames}: CM scope extends beyond repository files \| verdict={verdict} confidence={confidence}` | `partial` |
| `subagent-timeout` | `[AI-SAST via Code Scan Verification Validation \| {model}] Subagent timed out after max retries \| verdict={verdict} confidence={confidence}` | `partial` |
| `upstream-note-preserved` | `[AI-SAST via Code Scan Verification Validation \| {model}] Prior note preserved: {upstream_note_summary, ≤200ch} \| (audit-only, no verdict impact)` | none (audit) |
| `upstream-note-fetch-failed` | `[AI-SAST via Code Scan Verification Validation \| {model}] Could not fetch existing notes: {error} \| (audit-only, no verdict impact)` | none (audit) |

**Template placeholders:** `{model}` = LLM model identifier at runtime (e.g., `claude-4-sonnet`, `gpt-4o`). `{file_basenames}` = comma-separated basenames from the analysis file set (`cm.files_modified[]` in handoff mode, `discovered_files[]` in standalone mode). The `[AI-SAST via Code Scan Verification Validation | {model}]` prefix is **MANDATORY** on every `findings[].desc` value in the SDE payload — it identifies the tool and model to reviewers in the SDE UI.

`count` is the number of per-location observations in that bucket, **stringified** (e.g., `"3"`) to match the SDE spec's example.

Per-location detail (`{file, line, description, category}`) goes into `.sde-verification-handoff.json` `verification_results[].findings[]` unchanged — that file is the source-of-truth artefact pointed at by `finding_ref` (see below).

The deprecated category `missing-fix` (pre-3.2.0) MUST NOT appear in any new payload or handoff.

#### Verification Note Payload

Build the payload (subagent does this in B5; parent only sees the post status afterwards):

```json
{
  "behaviour": "combine",
  "confidence": "high",
  "status": "pass",
  "findings": [
    { "desc": "[AI-SAST via Code Scan Verification Validation | {model}] Mitigation confirmed in {file_basenames}: how-to ht-12 pattern present | verdict=pass confidence=high", "count": "1" }
  ],
  "finding_ref": "Agent: code-scan-verification-validation | Model: {model} | Repo: {repo_name} | CM: {full_cm_id} | Run: 2026-04-21T14:03:11Z | Handoff: .sde-verification-handoff.json",
  "pinned": false,
  "task_status_mapping": {
    "pass": "DONE"
  }
}
```

For a `fail` verdict, the same payload but with aggregated negative findings:

```json
{
  "behaviour": "combine",
  "confidence": "high",
  "status": "fail",
  "findings": [
    { "desc": "[AI-SAST via Code Scan Verification Validation | {model}] Residual vulnerability marker(s) in {file_basenames} | verdict=fail confidence=high", "count": "3" },
    { "desc": "[AI-SAST via Code Scan Verification Validation | {model}] Residual vulnerable pattern in {file_basenames}: {ctx.problem summary} | verdict=fail confidence=high", "count": "1" }
  ],
  "finding_ref": "Agent: code-scan-verification-validation | Model: {model} | Repo: {repo_name} | CM: {full_cm_id} | Run: 2026-04-21T14:03:11Z | Handoff: .sde-verification-handoff.json",
  "pinned": false,
  "task_status_mapping": {
    "pass": "DONE",
    "fail": "TODO"
  }
}
```

`task_status_mapping` rules (subagent enforces; passed via `task_status_mapping_opt_in` in the prompt):

- `"pass": "DONE"` is **always** included.
- `"fail": "TODO"` is included **only if** the user chose `yes_rollback` in Step A4 AND the current verdict is `fail`.
- `partial` never maps to a workflow status.

`behaviour: "combine"` is the SDE spec's "combine with all previous results" mode. It preserves prior verification notes (the audit trail) while adding the new one. SDE's derived `verification_status` on the task reflects the most-recent note, so state remains correct and re-runs preserve history.

`finding_ref` is the SDE UI's "Report Reference" field — it's expected to point at a retrievable artefact where a viewer can find more detail. The subagent writes the `finding_ref` using the format `Agent: code-scan-verification-validation | Model: {model} | Repo: {repo_name} | CM: {full_cm_id} | Run: {iso8601_utc} | Handoff: .sde-verification-handoff.json` — the primary fields (Agent, Model, Repo) are immediately visible in the SDE UI's Report Reference column. The CM and Run fields let a human locate the full reasoning in `.sde-verification-handoff.json` and distinguish per-CM, per-run notes. `{repo_name}` is the basename of `repository_path` (e.g., `my-app` from `/home/user/my-app`), captured in Phase A and forwarded to subagents.

#### Verification mode: manual (by design)

Notes from this skill are posted **without** an `analysis_session` ID, so SDE classifies them as **Manual Verification** (`automatic: false` on the resulting note resource). This is intentional — the AI agent is not a registered SDE Verification Connection plugin, and the SD Elements User Guide's [Manual verification](https://docs.sdelements.com/master/guide/docs/integrations/security_tools/overview/verification_status.html) path applies. Implications:

- The SDE UI groups these notes under "Manual Verification" rather than under a scanner name (Veracode, Fortify, etc.).
- Per the API spec, a `fail` note in **automatic** mode requires at least one finding; in **manual** mode it does not. This skill always emits at least one finding for `fail` regardless, so the SDE UI consistently shows the cited evidence.
- DO NOT mint a synthetic `analysis_session` ID to "promote" notes to automatic mode — without a registered Verification Connection plugin on the SDE side, the server will reject the payload and the audit trail will be lost.

If/when the AI agent is registered as a real SDE Verification Connection (out of scope for this skill), this section becomes obsolete and the payload will need an `analysis_session` field; the rest of the schema stays the same.

#### Verification tool call (subagent's B5)

```json
{
  "tool": "verification",
  "op": "create",
  "project_id": "{project_id}",
  "task_id": "{cm.full_id}",
  "behaviour": "combine",
  "confidence": "{confidence}",
  "status": "{verdict}",
  "findings": [/* aggregated findings */],
  "finding_ref": "{finding_ref}",
  "task_status_mapping": {/* see Step B3 */}
}
```

**Note on `{cm.full_id}`:** The `verification` tool auto-normalizes `task_id` via `normalizeProjectTaskId()` — it accepts `"T123"`, `"123-T123"`, `42`, etc. The handoff stores the full form (`full_id`, e.g. `"31768-T123"`); using it verbatim is recommended for clarity but no longer causes a 404 if a bare slug is passed.

---

## Step D. Write Own Handoff File

After the loop completes (or exits via user `stop`), write `.sde-verification-handoff.json` to `{repository_path}`. In handoff mode, **do not overwrite `.sde-apply-handoff.json`** — the upstream file must remain intact so the user can re-run `apply-fixes` or `code-scan-verification-validation` without losing audit data.

### Per-CM disk-offload + assemble-from-disk (T6 — context-window survival)

> The per-CM result RECORD (the AI's already-produced verdict + findings) is offloaded to disk AS IT IS PRODUCED in Phase B, so the parent context stays small (200K-survivable, multi-session normal). **This stores the OUTPUT of the AI's analysis — it NEVER replaces B2/B3 (the AI vuln analysis + verdict stay AI-only inline; SHELL TOOL USAGE POLICY).** The handoff `verification_results[]` is then ASSEMBLED FROM DISK, never from in-context memory. Namespaced dir (chain-compat): `.sde-security/verify/{project_id}/cm-work/{full_cm_id}.json` (NEVER the shared `.sde-security/cm-work/`).

These helper routines are MECHANICAL (IO only) — implement them yourself from this pseudocode (PoC-proven before shipping). The closed per-CM record schema is exactly `{ full_cm_id, status, confidence, findings, note_post_status }`.

```python
CM_WORK = f".sde-security/verify/{project_id}/cm-work"   # namespaced; NOT the shared cm-work/
REQUIRED_KEYS = {"full_cm_id", "status", "confidence", "findings", "note_post_status"}
VALID_STATUS  = {"pass", "partial", "fail", "skipped", "skipped_out_of_scope"}

def offload_cm_result(full_cm_id, result):
    # Phase B: write the AI's ALREADY-PRODUCED result. Mechanical; performs NO analysis.
    os.makedirs(CM_WORK, exist_ok=True)
    write_json(f"{CM_WORK}/{full_cm_id}.json", result)   # one file per CM
    src = len(result.get("findings", []))                # FIDELITY: emit per CM
    print(f"[FIDELITY] {full_cm_id}: status={result['status']} findings={src} offloaded=YES")

def assemble_handoff():
    # Step D: build verification_results[] by READING DISK (never in-context memory).
    results = []
    for name in sorted(os.listdir(CM_WORK)):
        if not name.endswith(".json"): continue
        rec = read_json(f"{CM_WORK}/{name}")
        assert set(rec) == REQUIRED_KEYS, f"{name}: schema mismatch"
        assert rec["status"] in VALID_STATUS and rec["full_cm_id"] == name[:-5]
        results.append(rec)
    return results            # merged with carried-forward prior entries on resume

def verify_disk_vs_sde(expected_count):
    # Layer-2 (terminal verification): count disk artifacts; non-zero exit on shortfall.
    n = len([x for x in os.listdir(CM_WORK) if x.endswith(".json")])
    return 0 if n == expected_count else 1   # context-light: counts only, never reads bodies
```

In Phase B, immediately after a CM's result entry is recorded (every disposition lane — verdict, `record_skipped`, `record_out_of_scope`), call `offload_cm_result(full_cm_id, entry)`. In Step D, build `verification_results[]` via `assemble_handoff()` (then apply resume-merge below). The expected denominator for `verify_disk_vs_sde` is `in_scope_total` (the Anchoring Rule) — never "work so far."

**Resume merge logic:** If Step A1.5+A3 loaded a prior verification run and the user chose to resume, the handoff MUST merge prior results with new results. `verification_results[]` is the concatenation of carried-forward prior entries (`already_done`) and newly-derived entries from this session. Totals are recomputed from the merged set. The `resumed_from` field records the prior handoff's `generated_at` timestamp for audit traceability.

```json
{
  "source_skill": "code-scan-verification-validation",
  "handoff_version": "1",
  "verification_mode": "handoff | standalone",
  "execution_mode": "subagent | inline",
  "resumed_from": "{prior_generated_at or null}",
  "generated_at": "{iso8601_utc}",
  "upstream_handoff": ".sde-apply-handoff.json | null",
  "project_id": "{project_id}",
  "risk_policy_id": "{risk_policy_id or null}",
  "repository_path": "{repository_path}",
  "scope": "all | selected_cms | one_by_one",
  "scope_args": { "cm_ids": ["..."] },
  "fail_rollback_opt_in": "yes_rollback | no_verification_only",
  "totals": {
    "verified_pass": P,
    "verified_partial": PT,
    "verified_fail": F,
    "skipped": S,
    "skipped_out_of_scope": S_oos,
    "note_failed": NF
  },
  "verification_results": [
    {
      "full_cm_id": "{project_id}-T123",
      "title": "...",
      "status": "pass | partial | fail | skipped | skipped_out_of_scope",
      "confidence": "high | low | n/a",
      "findings": [
        { "file": "src/auth.ts", "line": 42, "description": "Parameterised query; matches ctx.text guidance.", "category": "mitigation-confirmed" }
      ],
      "findings_aggregated_for_sde": [
        { "desc": "[AI-SAST via Code Scan Verification Validation | {model}] Mitigation confirmed in {file_basenames}: how-to {how_to_id} pattern present | verdict=pass confidence=high", "count": "1" }
      ],
      "finding_ref": "Agent: code-scan-verification-validation | Model: {model} | Repo: {repo_name} | CM: {project_id}-T123 | Run: {iso8601_utc} | Handoff: .sde-verification-handoff.json",
      "note_post_status": "POSTED | FAILED:{reason} | NOT_SENT | NOT_SENT_OUT_OF_SCOPE | NOT_SENT_FORCED_FAIL | NOT_SENT_AUTH_FAILURE",
      "reason": ""
    }
  ],
  "failed_cms_for_rework": [
    { "full_cm_id": "{project_id}-T145", "reason": "residual marker vuln-code-snippet at src/x.ts:88" }
  ]
}
```

`failed_cms_for_rework[]` is a convenience list populated from entries where `status == "fail"`. It lets a future rework skill (or a second pass of `apply-fixes`) target exactly the broken mitigations.

`skipped_out_of_scope` entries **(handoff mode only)** record CMs that were skipped without a verification note POST because `cm.status == "Documented"` (parent B0a), because the parent's B0b3 lane fired (non-code CM with empty `files_modified[]`, `handoff_version == "2"`), or because the subagent's L-OOS-sub lane fired (non-code CM with empty `files_modified[]`, `handoff_version == "1"`). In standalone mode, B1.5 is skipped entirely (no L-OOS-sub); the B1.7 file discovery step handles the "no relevant files" case with a `pass`/`high`/`vulnerability-absent` verdict instead — standalone mode does not produce `skipped_out_of_scope` entries. These handoff-mode sub-cases behave differently under scope filtering: **Documented CMs** are excluded by `filter_by_scope` under `all` / `one_by_one` and only enter the loop via `selected_cms` (where B0a fires); **Applied non-code CMs with empty `files_modified[]`** pass the scope filter under all scopes (they are Applied, not Documented) and produce `skipped_out_of_scope` entries via B0b3 (v2) or L-OOS-sub (v1) inside the loop. For all `skipped_out_of_scope` entries, `findings` is `[]`, `findings_aggregated_for_sde` is `[]`, `confidence` is `"n/a"`, `note_post_status` is `"NOT_SENT_OUT_OF_SCOPE"`, and no payload was constructed or sent — but the entry is still recorded so audit/totals reconciliation works downstream. `skipped` (user) entries follow the same shape as `skipped_out_of_scope` entries — `findings`/`findings_aggregated_for_sde` are `[]`, `confidence` is `"n/a"`, no payload was constructed — except `note_post_status` is `"NOT_SENT"` (no out-of-scope qualifier). They are produced by `record_skipped(cm, reason)` in two paths: the `one_by_one` per-CM `skip` path (one entry per skipped CM) and the `one_by_one` `stop` path (one entry for the `stop` CM plus one entry for every remaining in-scope CM). All such entries are mandatory and preserve the Sum-check identity. All `record_skipped` / `record_out_of_scope` entries persist the `reason` string on the entry's `reason` field (Step D schema, alongside `note_post_status`) — this is how downstream tooling distinguishes the three user-initiated no-POST sub-cases (and the Documented out-of-scope case) without consulting console logs.

**[CHECKPOINT]** `Verification handoff written: .sde-verification-handoff.json ({N} records)`

---

## Completion Verification Block (REQUIRED before "complete")

```
=== COMPLETION VERIFICATION ===
Skill: code-scan-verification-validation
MCP connection: ✓
Mode: {verification_mode}
CM source:
  (handoff)    Handoff loaded: ✓ ({N} CMs)
  (standalone) SDE project: ✓ ({project_name}, {N} CMs)
Git tree safety: ✓
Scope: {scope}
Fail-rollback opt-in: {yes_rollback | no_verification_only}

Per-CM verdicts (SDE UI labels):
- Pass:                  {P}
- Partial Pass:          {PT}
- Fail:                  {F}
- Skipped (user):        {S}
- Skipped (out of scope): {S_oos}

Verification Notes:
- POSTED: {NP}
- FAILED: {NF}  (IDs: {list or "none"})

Own handoff written: ✓ (.sde-verification-handoff.json)
Upstream handoff:
  (handoff)    preserved: ✓ (.sde-apply-handoff.json untouched)
  (standalone) N/A

Sum check: {P + PT + F + S + S_oos} == {in_scope_total}? {YES/NO}
Posted-note coverage (re-derived from SDE, NOT the in-memory results array):
  for each POST-eligible in-scope CM, verification op=list -> a note for THIS run
  exists (match on finding_ref)? {YES/NO}  (re-derived count == NP?)
===============================
```

Print the line matching the current `verification_mode`; omit the other.

### Terminal verification (T9 — 3 layers, AI-performed; gate-the-gate precondition)

**Gate-the-gate precondition (this block is INVALID if unmet):** the `=== PHASE B BATCH PLAN ===` was emitted AND a `--- BATCH k/t COMPLETE ---` mini-gate exists for EVERY batch (T5). If not, return to Phase B.

The completion gate is the conjunction of three independent layers. The AI performs Layers 1 and 3 itself; Layer 2 is the one mechanical (scripted) layer.

- **Layer 1 — inline re-derivation from disk (AI):** re-derive every count above from the per-CM disk artifacts `.sde-security/verify/{project_id}/cm-work/*.json` (NOT an in-memory tally), plus a **run-marker proof** (each artifact's `finding_ref`/run stamp belongs to THIS run, not a pre-existing file) and a **surviving-output check** (status alone is insufficient — the per-CM artifact actually exists on disk). The `Sum check` and `Posted-note coverage` lines above are Layer 1.
- **Layer 2 — verify script (mechanical):** run `verify_disk_vs_sde(in_scope_total)` (Step D helper) — disk-only, context-light, counts artifacts and exits non-zero on any shortfall. Paste its result.
- **Layer 3 — from-scratch clean-room tri-source (AI):** trusting NOTHING from the run, re-derive independently and assert the tri-source invariant: **SDE source-of-truth (the in-scope CM set) == disk artifacts (`cm-work/*.json` count) == handoff rows (`verification_results[]`) == `in_scope_total`**. Posted-note coverage re-derived from SDE (`verification op=list`, match on `finding_ref`) == `NP`.

ALL THREE layers must be YES before the run is **COMPLETE**.

**If Sum check = NO**, **posted-note coverage = NO**, **Layer 2 exits non-zero**, **the tri-source invariant fails**, or **`NF > 0` without documented cause** → output `INCOMPLETE` and loop back to retry failed notes (or re-fetch / re-offload to reconcile) before declaring completion. Do NOT trust the in-memory POSTED/FAILED flags alone — the coverage line MUST be re-derived from SDE via `verification op=list`.

**If Sum check = YES and NF cause is recorded:**

```
✅ COMPLETION GATE PASSED
Verified {P} Pass / {PT} Partial Pass / {F} Fail / {S} Skipped (user) / {S_oos} Skipped (out of scope)
Rework candidates: {F} (see .sde-verification-handoff.json → failed_cms_for_rework)
```

---

## Numbered Enforcement Rules

1. **Handoff is a hard requirement in handoff mode.** Missing, wrong `source_skill`, or declined by user → HARD STOP. No manual fallback. In standalone mode, SDE project selection (Step A1-S) replaces the handoff requirement. Missing SDE project selection in standalone mode → HARD STOP.
2. **Git tree must be clean BEFORE any checkout.** `git status --porcelain` empty or HARD STOP.
3. **Upstream `.sde-apply-handoff.json` MUST NOT be modified or deleted by this skill.** Write only to `.sde-verification-handoff.json`.
4. **"In-scope" has one canonical meaning: whatever `filter_by_scope` returned.** Filter behaviour: under `all` / `one_by_one` the filter excludes Documented and Skipped CMs (nothing on disk to scan or no mitigation to verify); under `selected_cms` the filter includes whatever IDs the user explicitly listed (subject to the Step A1.5+A3 warning prompts for Documented and Skipped). `in_scope_total = len(in_scope)` is computed after the filter and used everywhere (loop bound, Sum check, completion block). Every in-scope CM has a recorded result entry: CMs that pass through per-CM verification (B-Subagent or inline) receive a POST attempt and any failure is logged (not silently dropped); user-skipped CMs (`one_by_one`), Documented CMs (under `selected_cms`), non-code CMs with empty `files_modified[]` (parent B0b3 for v2, subagent L-OOS-sub for v1, recorded as `skipped_out_of_scope`), and run-aborted CMs after a subagent auth failure are recorded without an API call (`note_post_status` set to `NOT_SENT` / `NOT_SENT_OUT_OF_SCOPE` / `NOT_SENT_AUTH_FAILURE` respectively) — no POST, but the audit-trail entry is still written. Forced-fail CMs — upstream-Skipped (parent B0b), empty-files-modified code CMs (parent B0b2 for v2, subagent L-FF2-sub for v1) — now receive a B4+B5 POST (inline for parent, inside subagent for L-FF2-sub) with `note_post_status` set to `POSTED` on success or `FAILED:{reason}` on failure. (User-`skip` and user-`stop` in `one_by_one` mode are explicit user choices, not agent-initiated early exits — see Rule 10 for the loop-termination contract.) CMs with `cm.status == "Documented"` are filtered out under `all` / `one_by_one`; they can only enter the loop via `selected_cms` after an explicit user decision, in which case Step B0a short-circuits them as `skipped_out_of_scope` — no subagent dispatch, no SDE fetch, no file reads, no API call, no `task_status_mapping` touch. Pure `PROCESS` CMs never reach this skill (filtered upstream).
5. **No false positives. Negative signal is canonical; positive signal is corroborative.** *(See the verbatim "No-False-Positives Invariant" callout in Phase B.)* If Q1 is `absent_high_confidence` and the marker scan is clean, the verdict is `pass` — regardless of Q2 and Q3. **Q2 is OPTIONAL** — it runs only when `ctx.how_tos[]` is non-empty AND has at least one language-applicable entry; an empty/inapplicable `how_tos[]` is a normal path, not a degraded one. **Never default to `pass` or `fail` on uncertainty.** Uncertainty maps to `partial` with `low` confidence. `fail` is allowed from exactly four cited evidence sources: (1) cited `residual-vulnerable-pattern`, (2) cited `residual-marker`, (3) upstream `Skipped` audit status (parent B0b) **(handoff mode only)**, (4) empty `files_modified[]` for CODE_FIX/ML_CODE (parent B0b2 when `handoff_version == "2"`, subagent L-FF2-sub when v1) **(handoff mode only)**. Standalone mode uses only sources (1) and (2). Failure to recognise the developer's mitigation style is NEVER a `fail` or `partial` source.
6. **Progress output is mandatory.** Every per-CM transition emits exactly one of the canonical checkpoint formats listed in the Mandatory Checkpoints table (`[VERIFY]` for normal subagent return / forced-fail / malformed-subagent / auth-failure-current-CM; `[VERIFY-DISPATCH]` immediately before each batch dispatch (subagent launch or inline execution start); `[SKIP-OOS]` for Documented under `selected_cms` (parent B0a), parent B0b3 (non-code CM with empty files, v2), AND subagent L-OOS-sub returns (`parsed.result_kind == "out_of_scope"`, v1); `[SKIP-USER]` for `one_by_one` per-CM `skip`; `[STOP]` for `one_by_one` `stop` AND for the auth-failure aborted run, in both cases bulk-summarising the unreached CMs; `[INFO]` for the empty-in-scope short-circuit). The unreached CMs after `stop` or auth-failure are recorded individually in `verification_results[]` (preserving Sum-check) but share a single `[STOP]` line — that is the contract.
7. **`task_status_mapping.fail: TODO` is ONLY sent if the user opted in at Step A4.** Default behaviour leaves workflow status untouched on fail. The opt-in flag is forwarded to each subagent via the `task_status_mapping_opt_in` placeholder in the prompt template.
8. **Residual vulnerability markers are a fail criterion**, even if the logic appears fixed. The hardcoded marker list MUST appear verbatim in the subagent prompt template.
9. **Completion verification block is required** before any use of the words "complete", "finished", "done", "summary".
10. **No agent-initiated early exit.** Two user-initiated early-exit paths are allowed in `one_by_one` scope, and BOTH preserve the Sum-check identity `P + PT + F + S + S_oos == in_scope_total`:
    - **per-CM `skip`** — records `record_skipped(cm, reason="user skipped")` and continues to the next CM.
    - **`stop`** — records `record_skipped(cm, reason="user stopped (loop terminated at this CM)")` for the current CM AND `record_skipped(c, reason="user stopped (loop terminated; not reached)")` for every remaining in-scope CM (`in_scope[done:]`), then terminates the loop.

    A third *involuntary* run-terminating path exists: subagent `auth_failure: true` (401/403). Parent records the current CM with `NOT_SENT_AUTH_FAILURE` and every unreached CM via `record_skipped(c, reason="run aborted: auth failure at ...; not reached")`. This preserves the Sum-check identity even though the run did not complete successfully.

    No other path may bypass the per-CM verification cycle (B1 + B2 + B3 + B4 + B5) for an in-scope CM — whether that cycle runs inside a subagent (`execution_mode == "subagent"`) or inline in the parent (`execution_mode == "inline"`, Step A6 fallback). No agent-initiated condition (context limits, "critical ones done", repository intent) is a valid early exit.
11. **API payload + concept model MUST conform to the SDE spec.**
    - `behaviour` MUST be one of `combine` / `replace-scanner` / `replace`. `append` is invalid.
    - Each `findings[]` element MUST include `desc` and `count` (aggregated; per-location detail goes in the local handoff).
    - Every `fail` verdict MUST emit at least one finding.
    - Verification status (`pass`/`partial`/`fail`/`none`) and countermeasure status (`TODO`/`DONE`/`NA`) are separate concepts; never conflate them.
    - Notes without `analysis_session` register as Manual Verification by design; do NOT fake an `analysis_session`.
    - `finding_ref` MUST use the `Agent: code-scan-verification-validation | Model: {model} | Repo: {repo_name} | CM: {full_cm_id} | Run: {iso8601_utc} | Handoff: .sde-verification-handoff.json` form.
    - References: [Verification Notes API](https://docs.sdelements.com/master/api/docs/analysis-notes/), [Verification status (User Guide)](https://docs.sdelements.com/master/guide/docs/integrations/security_tools/overview/verification_status.html).
12. **Per-CM verification MUST be performed by a `generalPurpose` subagent (batched)** — unless `execution_mode == "inline"` (Step A6 fallback; see also AGENTS.md Rule 9). When `execution_mode == "subagent"`, the parent loop is a pure orchestrator — no inline B1 fetch, no inline B2 analysis, no inline B4 note-fetch, no inline B5 POST for any in-scope CM that survives the parent short-circuit lanes. CMs are grouped into batches of `batch_size` (default 10, configurable in Step A5). Each batch is dispatched to one `generalPurpose` subagent which processes its CMs sequentially and returns a JSON array. Up to 5 batches may run in parallel per round. **Exception:** When the MCP client does not support subagent generation (`execution_mode == "inline"` from Step A6), B1/B2/B3/B4/B5 run inline in the parent context with `batch_size=1`, no parallel dispatch, and mandatory context checkpoints every 5 CMs. This is the ONLY valid exception to the subagent-only rule.
13. **Subagent contract is non-negotiable.** Subagent type MUST be `generalPurpose`. Input MUST include the batch array, the verbatim No-False-Positives Invariant, B-Sub procedure, B3 verdict matrix, hardcoded marker list, batch iteration procedure, and strict JSON array return schema (rendered from the Subagent Prompt Template appendix). The subagent MUST return a strict JSON array with no extra prose; the parent MUST validate against the schema (array length == batch size, each element's `full_id` matches).
14. **Malformed subagent output is `partial`/low/`analysis-uncertain`, NEVER `fail`.** A parse error is not vulnerability evidence; recording it as `fail` would itself be a false positive. If the entire batch output is malformed, every CM in the batch is recorded as `partial`/low. If an individual element within a valid array is malformed, only that CM is recorded as `partial`/low; other CMs use their own parsed results.
15. **Subagent `auth_failure: true` triggers immediate parent HARD STOP.** Continuing would silently fail every remaining CM and corrupt totals. Record the auth-failure CM and every unreached CM (remaining in the batch + all future batches) via `record_skipped`, and surface a remediation message.
16. **Subagent timeout triggers retry, then graceful degradation.** If a subagent does not return within `subagent_timeout_ms` (default 300000 = 5 minutes), the parent kills it and re-launches the same batch (up to `max_retries=2` retries, 3 total attempts). After exhaustion, every CM in the batch is recorded as `partial`/low with finding category `subagent-timeout` and `note_post_status="FAILED:subagent-timeout"`. A timeout is not vulnerability evidence; recording it as `fail` would be a false positive.

---

## Forbidden Actions

| Action | Why Forbidden | Consequence |
|--------|---------------|-------------|
| (Handoff mode) Running without `.sde-apply-handoff.json` | File is the only source of `files_modified` in handoff mode | HARD STOP |
| (Standalone mode) Running without SDE project selection | No source for countermeasures in standalone mode | HARD STOP |
| Auto-proceeding after handoff load or SDE CM fetch without user confirm | Violates user-confirmation rule | Ask before Phase B |
| `git checkout` on dirty tree | Destroys local work | HARD STOP at Step A2 |
| Overwriting `.sde-apply-handoff.json` | Upstream audit trail is sacred | Write to `.sde-verification-handoff.json` instead |
| Marking `pass` because apply-fixes marked Applied | Status is not evidence | Per-CM verification re-reads files and verifies code |
| Marking `fail` without a cited residual pattern or marker | Defaults on uncertainty are forbidden | Use `partial` + `low` confidence |
| Marking `fail` because the canonical mitigation pattern was not found | False-positive vector — Q2 (canonical mitigation match) is corroborative, not gating | Apply the No-False-Positives Invariant; if Q1 is `absent_high_confidence`, verdict is `pass` |
| Marking `partial` because the developer used a different mitigation style than the how-to | Same false-positive vector | If Q1 is `absent_high_confidence` and marker scan is clean, verdict is `pass` regardless of Q2/Q3 |
| Marking malformed-subagent-output as `fail` | Parse error is not vulnerability evidence | Record `partial`/low with `analysis-uncertain` finding |
| Running B1, B2, B3, B4, or B5 inline in the parent context (when `execution_mode == "subagent"`) | Context-budget contract — parent is a pure orchestrator | Dispatch batched `generalPurpose` subagents (batch_size CMs per subagent). Exception: `execution_mode == "inline"` (Step A6 fallback) runs B1/B2/B3/B4/B5 inline with batch_size=1 and context checkpoints. Additional exception: parent B0b/B0b2 forced-fail short-circuits run B4+B5 inline (see Rule 9 forced-fail POST exception) |
| Marking subagent-timeout as `fail` | Timeout is not vulnerability evidence | Record `partial`/low with `subagent-timeout` finding |
| Skipping the parent forced-fail short-circuits (B0b, B0b2/B0b3 for v2) before per-CM verification | Forced-fail evidence is the upstream `Skipped` audit signal (B0b) or empty `files_modified[]` with known category (B0b2/B0b3); proceeding to verification is wasteful and risks re-deriving the wrong verdict | Always run B0a/B0b/B0b2/B0b3 BEFORE dispatching a subagent or starting inline verification |
| Accepting subagent output without JSON-schema validation | Malformed verdicts corrupt totals | Validate; on parse error record `partial`/low/`analysis-uncertain` |
| Continuing the loop after a subagent reports `auth_failure: true` | Every subsequent subagent will fail identically; partial run corrupts totals | HARD STOP, record all unreached CMs as `record_skipped`, surface remediation |
| Using `project_countermeasures op=update` to set verification | That field is read-only there | Subagent uses `verification op=create` |
| Sending `task_status_mapping.fail: TODO` without A4 opt-in | User did not consent to workflow rollback | Omit the fail mapping (controlled via `task_status_mapping_opt_in` placeholder) |
| Skipping the residual-marker check | Markers indicate incomplete cleanup | Include the marker list verbatim in the subagent prompt template |
| Grep-only verdict | Grep can't read semantics | Subagent must `read_file` + perform AI analysis (Q1/Q2/Q3) |
| Agent-initiated early exit before all `in_scope_total` CMs are processed (Sum check ≠ YES) | Contract violation | Continue the loop |
| Requesting elevated shell permissions for local file ops | Unnecessary and triggers approval prompts | Use default sandbox |
| Skipping B4 (fetch existing notes) to save time | Rich upstream note details will be lost; verification notes will overwrite rather than preserve prior context | Always fetch existing notes before POST; B4 failure is non-fatal but the attempt is mandatory |
| **Spawning a subagent on Composer 2 (`composer-2.5-fast`) or any model other than the parent's** | Composer 2 / weaker models silently abandon CM verification loops, skip CMs, use wrong API endpoints for note POSTs, lose context, and produce unreliable verdicts | Set the subagent `model` explicitly to the parent's model (SUBAGENT/DELEGATION POLICY); in Cursor override the Composer-2 default; if you cannot set the model, run inline (`execution_mode = "inline"`) |
| **Delegating in a way that lets CMs be silently skipped, or treating delegation as transferring completeness** | The parent ALWAYS re-derives coverage for every in-scope CM from SDE + disk (tri-source) regardless of who did the work | Delegate only bounded, verifiable batches; every subagent emits `[VERIFY]`/`[PROGRESS]` and the parent verifies every CM against the Sum-check |

---

## Troubleshooting

| Symptom | Likely Cause | Action |
|---------|--------------|--------|
| `.sde-apply-handoff.json` not found | apply-fixes not run, or ran in a different repository | Re-run apply-fixes in this repository first, or switch to standalone mode |
| `source_skill` is not `apply-security-fixes` | Wrong upstream skill, stale file | HARD STOP; ask user to clean up |
| `git status --porcelain` non-empty | Local uncommitted changes | HARD STOP; user stashes or commits |
| `security_branch` not present locally | Handoff refers to a remote-only branch | Fetch, or ask user to proceed on current branch (degraded mode) |
| `files_modified[]` empty for a CODE_FIX CM | apply-fixes bug or skipped CM | Verdict `fail`, finding: "code CM with no modified files" |
| SDE `project_countermeasures op=get` returns 404 | CM re-indexed, project wiped | `partial` + `low` confidence; log the error |
| `verification op=create` returns 429 | SDE rate limit | Sleep 1s, retry once, then record FAILED |
| `verification op=create` or `project_countermeasures op=get` returns 401 / 403 | Project token lacks read or analysis-note write scope | Subagent returns `auth_failure: true`; parent HARD STOPs and records all unreached CMs as `record_skipped` to preserve Sum-check; ask user to refresh credentials |
| Subagent returns malformed JSON | Subagent strayed from the strict-JSON instruction or returned partial output | Parent records `partial`/low/`analysis-uncertain` for every CM in the batch (NEVER `fail`); continue to next batch |
| Subagent stalls at "Starting up" for minutes | Platform-level subagent startup issue | Retry/timeout handles this automatically: parent kills after `subagent_timeout_ms` (default 5 min), retries up to `max_retries` (default 2), then records `partial`/low/`subagent-timeout` for the batch. Increase `batch_size` to reduce total launches. |
| Residual `vuln-code-snippet` marker found | apply-fixes cleanup was incomplete | Verdict `fail`; include marker location in findings |
| User selected `one_by_one` for 50 CMs by mistake | Misclick | Offer the "Switch to all" option at the warning prompt |
| SDE task shows many verification notes over time | Intended audit trail (we use `behaviour: "combine"`) | Each run adds a note distinguished by its `finding_ref` timestamp; SDE UI can filter to the latest. Not a bug. |
| B4 note-fetch returns 404/5xx for a CM | CM has no prior notes in SDE, or SDE connectivity issue | Non-fatal; proceed to B5 POST without upstream context; record `upstream-note-fetch-failed` finding (audit-only, no verdict impact) |
| Forced-fail POST returns 4xx/5xx after retries | SDE API issue for the forced-fail CM | Record `FAILED:{reason}` as `note_post_status`; the forced-fail verdict is still recorded locally in the handoff. The CM appears in `failed_cms_for_rework` regardless of POST success. |
| Rework candidate CM has no visible note in SDE | Prior behavior (pre B4+B5 forced-fail POST) — forced-fail CMs used `NOT_SENT_FORCED_FAIL` | Re-run verification for those CMs via `selected_cms` scope to POST notes retroactively |

---

## Handoff to Next Skill

After the completion verification block shows `Sum check = YES`:

```
✅ SKILL COMPLETE: Code scan verification validation finished

=== FINAL COUNTS (SDE UI labels) ===
Pass:                    {P}
Partial Pass:            {PT}
Fail:                    {F}
Skipped (user):          {S}
Skipped (out of scope):  {S_oos}
Verification Notes POSTED: {NP} / {NP + NF}
(POST attempts = P + PT + F = in_scope_total - S - S_oos. User-skipped and out-of-scope CMs receive no API call.)
====================================

Stored values for downstream use (.sde-verification-handoff.json):
- verification_mode: {handoff | standalone}
- upstream_handoff: {.sde-apply-handoff.json | null}
- project_id: {id}
- repository_path: {path}
- scope: {scope}
- fail_rollback_opt_in: {yes_rollback | no_verification_only}
- failed_cms_for_rework: {F} entries

Next skill: (optional) @sde-skills/apply-security-fixes (re-run, scoped to failed_cms_for_rework) OR human review in SD Elements UI.
```

### Downstream Skill Expectations

The downstream skill MUST:
1. Read `.sde-verification-handoff.json` if present.
2. ALWAYS ask the user to confirm loaded values (NEVER auto-proceed).
3. Fall back to full question flow if the user declines.

---

## Appendix: Subagent Prompt Template (CANONICAL — render verbatim)

The parent's `render_batch_subagent_prompt(...)` function MUST emit exactly this template with placeholders substituted. This is the single source of truth for what a verification subagent does. Drift from this template — even paraphrasing — is a contract violation.

```
You are a batched code-scan-verification-validation subagent. You operate in your own
isolated context — there is no shared state with the parent. You will process
a BATCH of countermeasures sequentially. For EACH CM in the batch, you will
perform B1 (fetch CM context from SDE), then mode-dependent steps:
  - Handoff mode: B1.5 (short-circuit) + B2 (AI code analysis on modified files)
  - Standalone mode: B1.7 (file discovery) + B2 (AI code analysis on discovered files)
then B3 (verdict), B4 (fetch existing notes for read-then-append preservation),
and B5 (POST verification note to SDE), and collect the per-CM result.
After processing all CMs, return a strict-JSON ARRAY of results (one
element per CM, in the same order as the input batch). You MUST NOT exceed
this scope: do not modify source files, do not run git, do not write any
local files, do not call other MCP tools beyond `project_countermeasures
op=get`, `verification op=list` (for B4 note fetch), and `verification op=create`
(and in standalone mode, grep/glob/read_file for file discovery in B1.7).

============================================================================
INPUTS (substituted by parent)
============================================================================
BATCH (array of CM descriptors — process each sequentially):
{batch_json}

verification_mode             = {verification_mode}  ("handoff" or "standalone")
repository_path               = {repository_path}
repo_name                     = {repo_name}  (basename of repository_path; used in finding_ref)
project_id                    = {project_id}
security_branch               = {security_branch}
task_status_mapping_opt_in    = {task_status_mapping_opt_in}  (true|false; from Step A4)

Each CM in the batch has: full_id, id, status, files_modified[].
  - Handoff mode: status will be "Applied"; files_modified[] has absolute paths.
  - Standalone mode: status is the SDE task status (DONE/TODO); files_modified[]
    is empty (file discovery happens in B1.7 below).

NOTE (handoff mode only): cm.category may or may not be passed by the parent
(it is present in handoff_version "2" but absent in "1"). Regardless, you MUST
obtain ctx.category from the B1 fetch response (field `category` on the
countermeasure object) and use it in B1.5 (subagent short-circuit lanes
L-FF2-sub and L-OOS-sub). When handoff v2, the parent's B0b2/B0b3 may have
already caught empty-files CMs; surviving CMs still run B1.5 as a redundant
guard. In standalone mode, B1.5 is SKIPPED entirely — proceed to B1.7.

============================================================================
BATCH ITERATION PROCEDURE
============================================================================
Initialize an empty results array. For each CM in the batch (in order):
  1. Run the B-Sub PROCEDURE below for this CM.
  2. Collect the per-CM result object.
  3. Append it to the results array.
  4. If the CM triggered auth_failure (401/403 from B1, B4, or B5):
     - For every REMAINING CM in the batch (not yet processed), append a
       result with result_kind="verified", verdict={status:"partial",
       confidence:"low", findings_for_sde:[{desc:"[AI-SAST via Code Scan
       Verification Validation | {model}] Auth failure on prior CM; batch aborted |
       verdict=partial confidence=low", count:"1"}],
       findings_for_handoff:[{file:"(n/a)", line:0,
       description:"Auth failure on prior CM; not processed",
       category:"context-fetch-failed"}]}, auth_failure:true,
       note_post_status:"NOT_SENT_AUTH_FAILURE", reason:"", rationale_summary:
       "batch aborted due to auth failure on earlier CM".
     - STOP processing further CMs. Return the results array immediately.
After all CMs are processed (or batch is aborted), return the results array.

============================================================================
NO-FALSE-POSITIVES INVARIANT (CANONICAL — verbatim)
============================================================================
No false positives. Negative signal is canonical; positive signal is
corroborative. Recognition is corroborative; absence-of-vulnerability is
canonical.

A `fail` verdict requires CITED, CONCRETE EVIDENCE of a vulnerability.

Handoff mode — four sources are allowed:
  1. a residual vulnerable pattern matching ctx.problem, cited at file:line, OR
  2. a residual marker comment (vuln-code-snippet, VULNERABLE, TODO: fix, etc.),
     cited at file:line, OR
  3. an upstream forced-fail signal: cm.status == "Skipped" (parent
     short-circuit B0b — already handled before subagent dispatch), OR
  4. empty files_modified[] for a CODE_FIX/ML_CODE CM (parent B0b2 when
     handoff_version == "2" — already handled before subagent dispatch;
     subagent L-FF2-sub when v1, fired by YOU in B1.5 after ctx.category
     is read from the B1 fetch response).

Standalone mode — only sources (1) and (2) apply (there is no upstream
Skipped status and files_modified is always empty by design; B1.5 is
skipped entirely).

Absence of the canonical mitigation pattern is NEVER a `fail` criterion.
Failure to recognise the developer's mitigation style is NEVER a `fail`
criterion. If Q1 is `absent_high_confidence` and the marker scan is clean,
the verdict is `pass` — regardless of Q2 and Q3.

An empty or partially populated ctx.how_tos[] is NOT a degraded path. Q2 is
OPTIONAL — it runs only when ctx.how_tos[] is non-empty AND has at least one
language-applicable entry. Otherwise Q2 is skipped entirely and the matrix
collapses to Q1 + Q3 + marker scan; Q1=absent_high_confidence + clean
markers yields pass/high regardless of whether Q2 ran.

`partial` is reserved for genuine analysis ambiguity (Q1=`ambiguous`) and
context-fetch failures (404/5xx/timeout/network). It is NOT a substitute for
`pass` when you are confident no vulnerability exists.

Q2 (canonical mitigation pattern from ctx.how_tos, optional — see above) and
Q3 (semantic-equivalence alternative mitigation) are corroborative — they
enrich findings and rationale. They do NOT gate the verdict.

============================================================================
B-Sub PROCEDURE
============================================================================
1. B1 (fetch). Call MCP `project_countermeasures` with:
       op       = "get"
       project_id = {project_id}
       task_id    = {cm.full_id}
       expand     = ["text", "problem", "tags", "how_tos", "name"]
   The response includes ctx.category (one of CODE_FIX | ML_CODE | INFRA |
   ML_DOC). When `handoff_version == "1"`, cm.category is NOT passed by
   the parent — you obtain it here and use it in B1.5 below. When
   `handoff_version == "2"`, the parent already has cm.category and uses
   it for B0b2/B0b3 parent-side short-circuits; CMs that reach this
   subagent have already survived those checks, but ctx.category is still
   available from this response and B1.5 acts as a redundant guard.
   - HTTP 401/403 -> set result_kind = "verified"; set verdict `partial` /
     `low`; emit one finding with category `context-fetch-failed` and
     description "[AI-SAST via Code Scan Verification Validation | {model}] Could
     not fetch CM context from SDE: HTTP {401|403} | verdict=partial
     confidence=low"; set note_post_status = "NOT_SENT_AUTH_FAILURE"; set
     auth_failure: true; return immediately. Do NOT attempt B1.5, B2, or
     B5. The verdict is REQUIRED by the strict-JSON return schema even
     when auth_failure: true (parent calls record_verified(cm,
     parsed.verdict, ...) and parsed.verdict.status determines which
     Sum-check bucket the current CM contributes to).
   - HTTP 404 / 5xx / timeout / network error -> skip B1.5/B2; set
     result_kind = "verified"; set verdict `partial` / `low`; emit one
     finding with category `context-fetch-failed` and description
     "[AI-SAST via Code Scan Verification Validation | {model}] Could not fetch CM
     context from SDE: {error} | verdict=partial confidence=low"; skip B5
     (do not POST); set note_post_status = "FAILED:fetch-{code}"; return.

1.5. B1.5 (subagent short-circuit — HANDOFF MODE ONLY; runs only after
   B1 succeeds). SKIP THIS STEP ENTIRELY in standalone mode (proceed to
   B1.7). Read ctx.category from the B1 response (it MUST be one of
   CODE_FIX | ML_CODE | INFRA | ML_DOC).

   - L-FF2-sub: if ctx.category in {CODE_FIX, ML_CODE} AND
     len(cm.files_modified) == 0:
       set result_kind        = "verified"
       set verdict.status     = "fail"
       set verdict.confidence = "high"
       emit one findings_for_handoff entry:
         { file: "(n/a)", line: 0,
           description: "[AI-SAST via Code Scan Verification Validation | {model}] code CM (CODE_FIX/ML_CODE) with no modified files | verdict=fail confidence=high",
           category: "residual-vulnerable-pattern" }
       emit one findings_for_sde entry:
         { desc: "[AI-SAST via Code Scan Verification Validation | {model}] code CM with no modified files (no mitigation present) | verdict=fail confidence=high",
           count: "1" }
       set reason            = "code CM with no modified files"
       set auth_failure      = false
       Skip B2. Proceed to B4 (fetch existing notes) + B5 (POST) to
       ensure the forced-fail verdict is visible in SDE with any upstream
       note context preserved. Set note_post_status from B5 result
       (POSTED on 2xx, FAILED:{reason} on failure). Return.

   - L-OOS-sub: if ctx.category in {INFRA, ML_DOC} AND
     len(cm.files_modified) == 0:
       set result_kind        = "out_of_scope"
       OMIT the `verdict` key entirely (out-of-scope entries do not
         carry a verdict; parent records skipped_out_of_scope).
       set reason            = "non-code CM with no modified files; static verification not applicable"
       set note_post_status  = "NOT_SENT_OUT_OF_SCOPE"
       set auth_failure      = false
       skip B2 and B5. Return.

   - Otherwise (non-empty cm.files_modified[]): proceed to B2 with
     result_kind = "verified" (set this once now; B3 will populate
     verdict).

1.7. B1.7 (file discovery — STANDALONE MODE ONLY; runs only after B1
   succeeds). SKIP THIS STEP ENTIRELY in handoff mode (proceed to B2 with
   cm.files_modified[]). In standalone mode, cm.files_modified is always []
   because there is no apply-fixes record. Discover relevant files:

   a. Extract search terms from ctx.problem + ctx.text + ctx.how_tos[]:
      vulnerability keywords, API/function names, framework patterns,
      file extensions/types relevant to the vulnerability surface.
   b. Use grep/glob (via shell tools) within {repository_path} to find
      candidate files. Exclude non-source directories: node_modules/,
      .git/, __pycache__/, dist/, build/, vendor/, .venv/.
   c. AI-rank the candidates by relevance to ctx.problem. Prioritize files
      that contain code patterns related to the vulnerability surface
      (e.g., SQL queries for SQL injection CMs, auth handlers for auth CMs).
   d. Select top N files (cap at 10 to stay within context budget).
      Store as discovered_files[].
   e. If NO relevant files found:
        set result_kind        = "verified"
        set verdict.status     = "pass"
        set verdict.confidence = "high"
        emit one findings_for_handoff entry:
          { file: "(repo-wide scan)", line: 0,
            description: "[AI-SAST via Code Scan Verification Validation | {model}] No files relevant to this CM's vulnerability surface found in repository | verdict=pass confidence=high",
            category: "vulnerability-absent" }
        emit one findings_for_sde entry:
          { desc: "[AI-SAST via Code Scan Verification Validation | {model}] No files relevant to this CM's vulnerability surface found in repository | verdict=pass confidence=high",
            count: "1" }
        set reason            = ""
        set auth_failure      = false
        Proceed to B4 (fetch existing notes) + B5 (POST the pass verdict). Skip B2/B3.
   f. Otherwise (discovered_files[] is non-empty): set result_kind =
      "verified"; proceed to B2 using discovered_files[] in place of
      cm.files_modified[].

2. B2 (analyse).
   Files to analyse:
     - Handoff mode: cm.files_modified[] (absolute paths from the handoff)
     - Standalone mode: discovered_files[] (from B1.7)
   Let analysis_files = cm.files_modified[] (handoff) or discovered_files[]
   (standalone).

   PRE-FILTER — scope-mismatch check (runs once per CM, before per-file
   analysis). Read ctx.problem and ctx.text. Determine whether the CM's
   full mitigation scope relates to analysis_files or extends to resources
   outside this repository (infrastructure, runtime config, process controls,
   third-party services, organisational policy). If the scope is external:
     - Emit one `scope-mismatch` finding:
         { file: analysis_files[0] or "(n/a)", line: 0,
           description: "[AI-SAST via Code Scan Verification Validation | {model}] CM scope ({ctx.problem summary, ≤100ch}) extends beyond repository files; partial verdict due to scope mismatch | verdict=partial confidence=low",
           category: "scope-mismatch" }
     - Set verdict = partial / low.
     - Proceed to B4 (fetch existing notes) + B5 (POST the partial verdict). Skip the per-file Q1/Q2/Q3
       analysis below.
   If the scope relates to analysis_files, proceed with the full per-file
   analysis below.

   Ground all reasoning in ctx.problem (the vulnerability)
   and ctx.text (the recommended fix). ctx.how_tos[] is OPTIONAL and
   CORROBORATIVE — many CMs have empty/partial how_tos[], and the verdict
   logic must work correctly in that case. For each file in analysis_files:
   a. read the full current contents.
   b. Detect language/framework from extension/shebang/manifest hints
      (*.py->Python; package.json->Node; pom.xml/*.java->Java; *.go->Go;
      *.cs/*.csproj->.NET; etc.).
   c. If ctx.how_tos[] is non-empty: filter to language-applicable entries.
      For each how-to filtered out, emit one `not-applicable-how-to-skipped`
      finding (audit only — no verdict impact). If ctx.how_tos[] is empty
      OR no entries are language-applicable: Q2 will be SKIPPED entirely
      (this is a normal path, not a degraded one).
   d. Q1 (PER FILE — negative-canonical, vulnerability presence). Driven by
      ctx.problem and ctx.text — NOT by ctx.how_tos[]. Determine one of
      three explicit states:
        absent_high_confidence — confident the vulnerability pattern from
          ctx.problem is NOT present (clean code path; sink not reachable;
          input parameterised/validated/escaped/typed).
        present_cited         — found a residual vulnerable pattern matching
          ctx.problem; emit `residual-vulnerable-pattern` finding cited at
          file:line.
        ambiguous             — cannot determine (obfuscated code; indirect
          data flow; partial coverage; missing dependency code). Default to
          `ambiguous` whenever in doubt — NEVER pick `absent_high_confidence`
          unless you are confident.
   e. Q2 (PER APPLICABLE HOW-TO — positive-corroborative, canonical match).
      OPTIONAL: runs ONLY when ctx.how_tos[] is non-empty AND has at least
      one language-applicable entry from step c. For each applicable how-to:
      is its canonical mitigation pattern present in this file? If yes ->
      emit `mitigation-confirmed` finding citing the how-to id. Q2 is
      corroborative only — it NEVER gates the verdict. When Q2 is skipped
      (empty or no applicable how-tos), proceed directly to Q3.
   f. Q3 (PER FILE — semantic-equivalence-corroborative). Asked when
      (a) ctx.how_tos[] is empty OR has no language-applicable entries
      (Q2 was skipped), OR (b) every applicable Q2 in this file returned
      no. Question: is some other recognisable mitigation present that
      prevents the vulnerability described in ctx.problem by the same
      security property described in ctx.text? If yes -> emit
      `alternative-mitigation-accepted` finding with a specific rationale
      (cite the observed code construct + the security property it shares
      with ctx.text's recommended fix). Q3 is corroborative only.
   g. Marker scan (PER FILE). Scan for the hardcoded marker list:
        vuln-code-snippet, VULNERABLE, INSECURE, TODO: fix,
        FIXME: security, <!-- VULNERABLE -->, # SECURITY ISSUE, // TODO: fix
      Any hit -> emit `residual-marker` finding cited at file:line.

3. B3 (verdict). Apply the verdict matrix.

   Note: Q2 is OPTIONAL — when ctx.how_tos[] is empty or has no
   language-applicable entries, Q2 is skipped and the matrix collapses to
   Q1 + Q3 + marker scan. Q1=absent_high_confidence + clean markers always
   yields pass/high regardless of whether Q2 ran (per the No-False-Positives
   Invariant; Q2 is corroborative-only).

   Per-file rows (each file produces one row):
     Q1=absent_high_confidence + Q2 any-Yes (Q2 ran) + clean markers
                                                              -> pass/high  + mitigation-confirmed
     Q1=absent_high_confidence + (Q2 all-No OR Q2 skipped) + Q3=Yes + clean
                                                              -> pass/high  + alternative-mitigation-accepted
     Q1=absent_high_confidence + (Q2 all-No OR Q2 skipped) + Q3=No  + clean
                                                              -> pass/high  + vulnerability-absent-mitigation-unrecognized
     Q1=ambiguous              + clean markers                -> partial/low + analysis-uncertain
     Q1=present_cited                                          -> fail/high  + residual-vulnerable-pattern
     marker hit (any Q1)                                       -> fail/high  + residual-marker

   Mixed-file aggregation: if files produce different rows, the verdict for
   the CM is the worst row hit, in this order:
     (1) any present_cited OR any marker hit -> fail/high (concatenate all hits)
     (2) any ambiguous -> partial/low
     (3) all absent_high_confidence -> pass/high
   Findings from ALL files are concatenated (no de-duplication).

3.5. B4 (fetch existing notes — read-then-append). Before building the
   POST payload, fetch existing **verification** notes on this CM to preserve
   prior verification detail (verification-note channel only — apply-fixes'
   addNote audit comments are a separate channel and are NOT merged here).
   Call verification with op="list",
   project_id={project_id}, task_id={cm.full_id}.
   If notes exist, extract description text and store as existing_notes[].
   On 404/5xx/timeout/network: non-fatal — set existing_notes=[], emit one
   upstream-note-fetch-failed finding (file="(n/a)", line=0,
   description="Could not fetch existing notes: {error}",
   category="upstream-note-fetch-failed"), proceed to B5.
   On 401/403: treat as auth failure (same as B1 auth path — set
   auth_failure: true and return immediately).

4. B5 (post). Build payload:
     behaviour       = "combine"
     confidence      = verdict.confidence
     status          = verdict.status
     findings        = aggregated by category (one {desc, count} per category;
                       count stringified; each desc MUST begin with
                       "[AI-SAST via Code Scan Verification Validation | {model}] ")
                       PLUS if existing_notes[] is non-empty from B4: append one
                       upstream-note-preserved finding per preserved note
                       (desc="[AI-SAST via Code Scan Verification Validation |
                       {model}] Prior note preserved: {upstream_note_summary,
                       <=200ch} | (audit-only, no verdict impact)", count="1")
     finding_ref     = "Agent: code-scan-verification-validation | Model: {model} | Repo: {repo_name} | CM: {cm.full_id} | Run: {iso8601_utc} | Handoff: .sde-verification-handoff.json"
     pinned          = false
     task_status_mapping = {"pass": "DONE"}
                       PLUS {"fail": "TODO"} ONLY if (task_status_mapping_opt_in
                       AND verdict.status == "fail")
   Call: verification op=create project_id={project_id} task_id={cm.full_id}
   Retry/back-off:
     HTTP 429        -> sleep 1s, retry once. Second 429 -> note_post_status
                        = "FAILED:rate-limited"; return verdict.
     HTTP 5xx        -> retry once after 1s; on second failure
                        note_post_status = "FAILED:5xx-{code}"; return verdict.
     network error   -> retry once after 1s; on second failure
                        note_post_status = "FAILED:network-{error}"; return verdict.
     HTTP 401 / 403  -> return immediately with auth_failure: true and
                        note_post_status = "NOT_SENT_AUTH_FAILURE". Parent will
                        HARD STOP the run.
     HTTP 4xx other  -> note_post_status = "FAILED:{code}-{server-body, ≤200ch}";
                        return verdict.
     2xx             -> note_post_status = "POSTED"; return verdict.

============================================================================
RETURN SCHEMA (STRICT JSON ARRAY — no extra prose, no markdown, no code fences)
============================================================================
Return a JSON ARRAY with exactly one element per CM in the input batch,
in the same order. Each element has this schema:

[
  {
    "full_id": "{cm.full_id}",
    "result_kind": "verified | out_of_scope",
    "verdict": {
      "status": "pass | partial | fail",
      "confidence": "high | low",
      "findings_for_sde": [{"desc": "...", "count": "N"}],
      "findings_for_handoff": [
        {
          "file": "...",
          "line": 0,
          "description": "...",
          "category": "residual-marker | residual-vulnerable-pattern | mitigation-confirmed | alternative-mitigation-accepted | vulnerability-absent-mitigation-unrecognized | vulnerability-absent | not-applicable-how-to-skipped | analysis-uncertain | context-fetch-failed | scope-mismatch | upstream-note-preserved | upstream-note-fetch-failed"
        }
      ]
    },
    "note_post_status": "POSTED | FAILED:{reason} | NOT_SENT_FORCED_FAIL | NOT_SENT_OUT_OF_SCOPE | NOT_SENT_AUTH_FAILURE",
    "auth_failure": false,
    "reason": "free-text; required for result_kind=out_of_scope and for L-FF2-sub forced-fail; empty string otherwise",
    "rationale_summary": "≤300 chars; what you observed and why this verdict (or, for result_kind=out_of_scope, why the CM was OOS)"
  }
]

Field rules (STRICT):
  - The array MUST have exactly len(batch) elements. Each element's full_id
    MUST match the corresponding batch[i].full_id.
  - result_kind is a discriminator. "verified" means a verdict is present.
    "out_of_scope" means the L-OOS-sub lane fired (B1.5 with non-code CM
    AND empty cm.files_modified[]); the parent will record
    skipped_out_of_scope and not POST.
  - verdict is REQUIRED when result_kind="verified"; it MUST be omitted
    entirely when result_kind="out_of_scope".
  - note_post_status is REQUIRED in both branches. For
    result_kind="out_of_scope" the only valid value is
    NOT_SENT_OUT_OF_SCOPE. For result_kind="verified" pick one of the
    others depending on the path you took (POSTED on a 2xx — including
    L-FF2-sub which now runs B4+B5 POST,
    FAILED:{...} on a 4xx-non-auth/5xx/network,
    NOT_SENT_AUTH_FAILURE for 401/403).
  - auth_failure is REQUIRED in both branches.
  - reason is REQUIRED (and non-empty) when result_kind="out_of_scope"
    or when L-FF2-sub fires. Otherwise it MAY be the empty string.
  - If auth_failure fires mid-batch, fill remaining slots with
    auth_failure:true stubs (see BATCH ITERATION PROCEDURE above).

The category `missing-fix` is NOT permitted (deprecated in beta-3.2.0).

Return STRICT JSON ARRAY only. No prose, no markdown, no code fences. The
parent will fail your output if it cannot json.loads() the entire response.
```
