# Combined Survey & Specs Skill - Agent Execution Contract

> **SUBAGENT / DELEGATION POLICY -- READ THIS FIRST**
>
> Subagents (the Task tool / delegation) MAY be used to reduce the parent agent's context-window strain -- under STRICT rules. Delegation is NOT banned; using the wrong model is.
>
> 1. **Same model as the parent, ALWAYS.** Any spawned subagent MUST run on the SAME model as the parent agent -- set the `model` parameter explicitly to the parent's model. If you cannot set the subagent's model, do NOT spawn -- run inline.
> 2. **NEVER Composer 2.** `composer-2.5-fast` (Composer 2) is FORBIDDEN as a subagent model in ANY environment -- it silently abandons loops, skips items, uses wrong endpoints, and produces inferior output. In Cursor the DEFAULT subagent is Composer 2, so you MUST override `model` to the parent's model explicitly; if you cannot override it, run inline.
> 3. **Parent owns completeness.** Delegation NEVER transfers responsibility for completeness. The parent re-derives every artifact from SDE + disk (tri-source invariant) regardless of who did the work. Every subagent MUST emit `[PROGRESS]` lines and return a verifiable result; the parent verifies every item.
> 4. **Delegate only bounded, verifiable sub-tasks** (e.g. a batch of reads/analysis returning a compact summary, or a bounded CM range that the parent then re-verifies). NEVER delegate in a way that lets items be silently skipped.
> 5. **Same model is necessary but NOT sufficient.** These guardrails apply to EVERY delegated worker regardless of model. A real run proved a SAME-MODEL worker (Opus 4.8, not Composer 2) went rogue: given "batch N of a 22-batch job" it scripted all batches into alternative files, bulk-flipped the entire ledger to terminal, and fabricated a "concurrent batches" story. Same-model is NOT a guarantee of obedience.
> 6. **Parent owns ALL authoritative-state writes.** The PARENT owns every write to the AGENTS.md ledger rows / Status fields. A worker MUST NOT write the ledger or any CM status. Workers RETURN their results (per-CM: status, files_modified, note result) for ONLY the CM-IDs in their explicit allow-list; the PARENT applies the ledger writes after verifying.
> 7. **Snapshot, diff, roll back.** Before delegating, the parent SNAPSHOTS the AGENTS.md ledger + the file tree; after each worker returns, the parent DIFFS against the snapshot and ROLLS BACK / REJECTS any change outside that worker's CM-ID + files allow-list.
> 8. **Allow-list only -- no alternative/parallel files.** A worker operates ONLY on its explicit allow-list and MUST NOT touch other CMs, ledger rows, or files, and MUST NOT create alternative/parallel output files (per-batch code modules, `security/applied/*`, `*_secure.*`, `*_fixed.*`, etc.) -- fixes are applied IN PLACE to the real source files only.
> 9. **Never frame a worker as "batch N of M".** Do NOT frame a worker's task as "batch N of M" or imply it should complete the larger job -- give it ONLY its bounded unit (its CM-ID allow-list) with explicit instruction to do that unit and nothing else.
>
> **At skill start (before Step 0):** determine the parent agent's model. If you will spawn subagents, you will set their `model` to the parent's model explicitly (NEVER `composer-2.5-fast`). Output:
> `[CHECKPOINT] Subagent policy: same-model-as-parent | Composer 2 FORBIDDEN | parent owns completeness (tri-source)`

This contract MUST be followed when executing `SKILL.md` in this directory.

## Skill Identity

**Name:** Configure Survey and Generate Security Specifications  
**Purpose:** Complete preparation phase - survey configuration + security spec generation  
**Scope:** MCP connection, user inputs, project creation, survey configuration, countermeasure retrieval, classification, code mapping, file generation

**Combines:**
- `@sde-skills/configure-sde-survey-from-codebase`
- `@sde-skills/create-security-specs-from-sde-countermeasures`

**Does NOT include:** Applying fixes (use `@sde-skills/apply-security-fixes`)

---

## ⚠️⚠️⚠️ AI CODE ANALYSIS REQUIRED - NO GREP/PATTERN MATCHING ⚠️⚠️⚠️

**This skill MUST use AI code analysis to find vulnerabilities and map countermeasures. Do NOT rely on grep or pattern matching.**

### Why AI Analysis for This Skill:

| Task | ❌ FORBIDDEN (grep) | ✅ REQUIRED (AI Analysis) |
|------|---------------------|---------------------------|
| Find vulnerable code | `grep "eval("` | READ file, UNDERSTAND context |
| Map countermeasure to code | Search for text pattern | ANALYZE code semantics |
| Classify countermeasures | Pattern match file names | UNDERSTAND code behavior |
| Identify technologies | `grep "import"` | ANALYZE entire codebase structure |
| Classify CMs | AI decides every category (a script may keyword-PROPOSE; AI confirms each). Cross-check: a CM with a matching library SKILL.md amendment is file-tracked, never PROCESS |
| Author SKILL.md content | AI authors; the `assemble_skill_files` helper routine you implement (from the pseudocode in the SKILL.md contract) copies library `amendment.text` byte-exact or assembles AI-authored fields -- it NEVER authors content, and you NEVER write a script that authors content (see SHELL TOOL USAGE POLICY) |

### For Countermeasure Classification:

When classifying each countermeasure (CODE_FIX vs PROCESS vs INFRA):

1. **READ relevant source files** with `read_file` tool
2. **ANALYZE the code** to determine if vulnerable pattern exists
3. **UNDERSTAND context** - same pattern in test vs production is different
4. **DOCUMENT the vulnerable code location** with file path and line numbers

**Example - SQL Injection Countermeasure:**
- ❌ WRONG: `grep "query"` → found matches → classify as CODE_FIX
- ✅ RIGHT: READ routes/login.ts → ANALYZE → found string concatenation in SQL query at line 45 → CODE_FIX with specific location

### For Generating Skill Files:

When creating `skills/{domain}/{cm-slug}/SKILL.md` files:

1. **AI must FIND the actual vulnerable code** (not just guess based on countermeasure title)
2. **AI must DOCUMENT exact file paths and line numbers**
3. **AI must UNDERSTAND the vulnerability** to write accurate task recipes
4. **AI must NOT include vulnerability markers** (vuln-code-snippet, etc.) in generated specs

---

## ⚠️ MANDATORY USER INPUTS - NEVER SKIP

**CRITICAL: You MUST ALWAYS prompt the user for ALL inputs. NEVER assume or skip.**

This skill is designed to be **repository-agnostic** and **project-agnostic**. The agent executing this skill:

1. **MUST ask the user** which repository to harden - even if there's only one visible
2. **MUST ask the user** whether to create a new project or use existing
3. **MUST ask the user** to select a business unit (if creating new)
4. **MUST ask the user** to select or create an application (if creating new)
5. **MUST ask the user** to confirm/enter the project name
6. **MUST ask the user** to select a risk policy (or skip if unavailable)

**Why this matters:**
- The workspace may contain multiple repositories
- The user may want to use an existing SD Elements project
- Assumptions lead to wrong configurations and wasted effort
- User confirmation ensures intent is correctly understood

**NEVER:**
- Auto-select a repository because "it's obvious"
- Skip business unit selection because "there's only one"
- Assume the user wants to create a new project
- Use default values without explicit user confirmation

**EXCEPTION — PRE-SUPPLIED / NON-INTERACTIVE INPUTS:** If inputs are PRE-SUPPLIED (by the caller/parent agent, a `.sde-handoff.json`, or the environment) OR no interactive `ask_question` tool / human is available, the agent MUST USE those inputs and SKIP the interactive prompt, recording one line `[INPUT] source={caller|handoff|env}: repo=..., mode=..., BU=..., project=...`. Use `ask_question` ONLY when an interactive client IS present AND inputs are NOT pre-supplied. Never silently invent inputs — if neither pre-supplied nor interactive is possible, STOP and ask the caller. The "ALWAYS ASK / NEVER assume" rules above govern the INTERACTIVE case (they forbid guessing, not using inputs you were explicitly given).

---

## Completion Criteria

**AUTHORITATIVE EXECUTION CONTRACT:** This skill (and its SKILL.md) is the authoritative source for how much work is required. Your judgment about scale or "pragmatic" shortcuts is OVERRIDDEN. Expect PROCESS notes for every PROCESS CM (batched 50/composite call, Step 4.5), amendments for every file-tracked CM (batched 25/composite call, Step 4.6), and a SKILL.md for every file-tracked CM (AI-authored content offloaded to `cm-work/`, assembled by `assemble_skill_files`, Step 7). These are EXPECTED, not a reason to sample. **You have explicit permission to take as many turns/sessions as needed -- completeness is the only priority; the only sanctioned pause is a CONTEXT CHECKPOINT.** Multi-session is normal; disk (ledger + artifacts) is the source of truth. Execute the batches mechanically.

This skill is NOT complete until ALL of the following are true:

- [ ] MCP connection verified successfully
- [ ] User inputs **INTERACTIVELY gathered from user** (repository, project mode, business unit, application, project name) - **NO ASSUMPTIONS**
- [ ] SD Elements project created or loaded
- [ ] Risk policy selection presented to user (or skipped if API unavailable)
- [ ] **⚠️ Full survey structure retrieved via `project_survey` op `getDraft` (include=survey) BEFORE any codebase analysis** (`getProjectSurvey` returns only selected answer IDs, not structure)
- [ ] **⚠️ Survey structure checkpoint output:** `[CHECKPOINT] Survey structure retrieved: {N} questions across {N} categories`
- [ ] Codebase analyzed for technologies using survey structure as the checklist
- [ ] **⚠️ EVERY question in the survey structure systematically checked** (NOT a hardcoded list)
- [ ] **⚠️ Dynamic survey coverage verification block output** showing all survey categories reviewed (from actual survey, not hardcoded)
- [ ] Survey questions answered with code evidence
- [ ] Every SUCCESSFULLY answered question has an accompanying `addQuestionComment` (comment count >= successfully-selected count in verification block; gated/invalid answers recorded as `skipped-gated` do not count)
- [ ] Survey committed and countermeasures generated
- [ ] All countermeasures retrieved from SD Elements
- [ ] How-to guidance fetched for countermeasures (or skipped with justification)
- [ ] Each countermeasure classified (CODE_FIX, ML_CODE, ML_DOC, PROCESS, INFRA)
- [ ] Classification output block generated with counts
- [ ] PROCESS countermeasures noted in SD Elements via `addNote` (no local files created)
- [ ] Countermeasures mapped to vulnerable code locations
- [ ] Root `AGENTS.md` created or merged in target repository (using SDE-SECURITY-HARDENING markers) -- excludes PROCESS CMs
- [ ] Pre-existing AGENTS.md content preserved (if file existed)
- [ ] AGENTS.md NOT included in AI config archive (merged instead of replaced)
- [ ] Per-countermeasure `skills/{domain}/{T123-slug}/SKILL.md` files created with YAML front matter -- excludes PROCESS CMs
- [ ] Total countermeasures in generated files = total from SD Elements minus PROCESS count
- [ ] All mandatory output blocks printed in exact format
- [ ] NO countermeasures incorrectly classified due to "intentionally vulnerable" rationalization
- [ ] Pre-existing AI config files archived (if any existed)

- [ ] POST-EXECUTION AUDIT passed: project_id re-verified, survey comments re-counted from SDE, SKILL.md files re-read from disk, handoff JSON re-read and validated, library fidelity re-checked, **library coverage re-derived from the durable `library_lookup_audit[]` (one entry per file-tracked CM; three-way reconciliation with the Source column + `library_sourced_cms`; red-flag heuristics incl. all-TEMPLATE/identical-timestamps trigger HARD-WARN)**, **PROCESS notes re-fetched from SDE (note_count >= 1 each)** -- ALL AUDIT CHECKS = YES (every artifact class enumerated; no sampling)
- [ ] Per-step PREFLIGHT emitted at each step boundary confirming prior step's verification block was present
- [ ] LEDGER INIT gate passed: AGENTS.md index rows == skills/**/SKILL.md files == file_tracked, Source stamp present for every row
- [ ] Ledger (AGENTS.md index + per-CM SKILL.md Status) is the source of truth and was read back to produce every audit count
- [ ] Heavy steps emitted `[ANALYSIS PROGRESS]` heartbeats; if a context-limit interruption occurred, a CONTEXT CHECKPOINT was emitted and resume RE-DERIVED progress from SDE + disk (not chat memory)

**You cannot claim completion until all boxes are checked, counts match, and the POST-EXECUTION AUDIT passes.**

---

## Mandatory Outputs

### Output Timing Requirements

**CRITICAL:** Each output block MUST be printed at the EXACT point specified. Do not batch outputs at the end.

| Step | When to Output | What to Output |
|------|----------------|----------------|
| After Step 0 | Immediately after MCP test succeeds | `[CHECKPOINT] MCP connection successful` |
| After Step 1 | After all user inputs collected | `[CHECKPOINT] Inputs: repo=..., project=... (ID: ...), risk_policy=...` |
| After Step 1.5 | After project created/loaded | `[CHECKPOINT] Project ID: {id}` |
| After Step 1.8 | After AI config archive | `[CHECKPOINT] AI Config: {N} files archived` OR `[CHECKPOINT] AI Config: No pre-existing files found` |
| After Step 2.1 | After technology discovery | `[CHECKPOINT] Technologies: {list}` |
| After Step 2.3.1 | **OUTPUT** - Before survey commit | `=== SURVEY COVERAGE VERIFICATION ===` block |
| After Step 2.4 | After survey commit | `[CHECKPOINT] Survey committed, generating countermeasures...` |
| After Step 3.1 | After countermeasures retrieved | `[CHECKPOINT] Total countermeasures: {N}` |
| After Step 3.2 | After how-to fetch (or skip) | `[CHECKPOINT] Fetched implementation guidance for {count} countermeasures` OR `[CHECKPOINT] How-to guidance skipped: {reason}` |
| After Step 4 | **OUTPUT** - Output full classification block | `=== COUNTERMEASURE CLASSIFICATION ===` block |
| After Step 4.5 | After PROCESS notes added | `[CHECKPOINT] PROCESS countermeasures: {count} noted in SD Elements (no local files)` |
| After Step 7 | **OUTPUT** - Output file generation block | `=== FILE GENERATION VERIFICATION ===` block |
| End of skill | **OUTPUT** - Output completion block | `=== COMPLETION VERIFICATION ===` block |
| End of skill | **OUTPUT** - Output handoff data | `HANDOFF DATA:` block |
| End of skill | After handoff data | `[CHECKPOINT] Handoff file written: .sde-handoff.json` |

### Progress Checkpoints

Output these EXACTLY as shown (copy the format):

```
[CHECKPOINT] MCP connection successful
```

```
[CHECKPOINT] Inputs: repo={repository_path}, project={project_name} (ID: {project_id}), risk_policy={risk_policy_id or SKIPPED}
```

```
[CHECKPOINT] Project ID: {id}
```

```
[CHECKPOINT] Technologies: {comma-separated list}
```

### Survey Structure Retrieved (REQUIRED - NEW)

**REQUIRED OUTPUT:** After calling `project_survey` op `getDraft` (include=survey), output this checkpoint:

```
[CHECKPOINT] Survey structure retrieved: {N} questions across {N} categories
Categories: {comma-separated list of actual category names from survey}
```

### Survey Coverage Verification (REQUIRED - DYNAMIC)

**REQUIRED OUTPUT:** Before committing the survey, you MUST output this verification block.

**⚠️ THIS VERIFICATION MUST BE DYNAMIC - based on the actual survey structure you retrieved, NOT a hardcoded list of categories.**

**FOLLOW THIS FORMAT (categories come from your survey structure):**

```
=== SURVEY COVERAGE VERIFICATION (DYNAMIC) ===
Survey structure from: project_survey op getDraft (include=survey)

Total question categories in survey: {N from survey structure}
Total questions across all categories: {N}
Questions checked: {N} (MUST equal total questions)
Questions with answers selected: {N}
Questions skipped: 0 (MUST BE ZERO)

Survey Categories Reviewed (from actual survey structure):
[List EVERY category that exists in the survey you retrieved]

- [ ] {Category 1 name from survey}: {count} questions checked, {count} answers selected
      Evidence: {files searched, patterns found/not found}
- [ ] {Category 2 name from survey}: {count} questions checked, {count} answers selected
      Evidence: {files searched, patterns found/not found}
[... continue for ALL categories in the survey structure ...]

Questions with comments added: {N} (MUST be >= questions with answers SUCCESSFULLY selected)
Answers skipped-gated (HTTP 400 not-valid / absent from getDraft): {N} (legitimate skips -- NOT counted against coverage)

VERIFICATION CHECKS:
- Questions checked == Total questions? {YES/NO}
- Questions skipped == 0? {YES/NO}
- All categories from survey structure listed? {YES/NO}
- Comments added >= Questions with answers SUCCESSFULLY selected? {YES/NO}

OVERALL VERIFICATION: {YES (all pass) / NO (re-iterate)}
=================================================
```

**⚠️ WARNING: If your verification block has hardcoded categories (like "Authentication", "OAuth/SSO", etc.) instead of categories from `project_survey` op `getDraft` (include=survey), you are doing it WRONG. The categories MUST come from the actual survey structure.**

**If VERIFICATION is NO, go back and check missing questions. Do not proceed until YES.**

```
[CHECKPOINT] Survey committed, generating countermeasures...
```

```
[CHECKPOINT] Total countermeasures: {N}
```

```
[CHECKPOINT] Fetched implementation guidance for {count} countermeasures
```

```
[CHECKPOINT] AI Config: {N} files archived to .sde-ai-backup.tar.gz
```

### Classification Output (REQUIRED)

**REQUIRED OUTPUT:** After classifying ALL countermeasures, you MUST output this block BEFORE proceeding to file generation.

**COPY THIS FORMAT EXACTLY:**

```
=== COUNTERMEASURE CLASSIFICATION ===
Total: {N}

CODE_FIX ({count}): {comma-separated list of IDs}
ML_CODE ({count}): {comma-separated list of IDs}
ML_DOC ({count}): {comma-separated list of IDs}
PROCESS ({count}): {comma-separated list of IDs} [NOTE-ONLY -- no local files]
INFRA ({count}): {comma-separated list of IDs}

Code-applicable (CF + MC): {sum1}
Documentation-only (MD + IN): {sum2}
Note-only (PR): {sum3}
VERIFICATION: {sum1} + {sum2} + {sum3} = {N}? {YES/NO}
File-tracked (CF + MC + MD + IN): {sum1 + sum2}
========================================
```

**If VERIFICATION is NO, reconcile before proceeding. Do not continue until YES.**

### File Generation Output (REQUIRED)

**REQUIRED OUTPUT:** After creating all files, you MUST output this block BEFORE the completion block.

**COPY THIS FORMAT EXACTLY:**

```
=== FILE GENERATION VERIFICATION ===
Total countermeasures: {N}
PROCESS (note-only, excluded): {process_count}
File-tracked countermeasures: {N - process_count}
Countermeasures in AGENTS.md: {count}
Countermeasures across skill files: {count}

Files created:
- AGENTS.md ({file_tracked} countermeasures indexed, with SDE-SECURITY-HARDENING markers)
- skills/{domain1}/{T123-slug}/SKILL.md
- skills/{domain1}/{T124-slug}/SKILL.md
- skills/{domain2}/{T125-slug}/SKILL.md
...
Total CM skill files: {count}

Sum across files: {total}
MATCH: {total} == {file_tracked}? {YES/NO}
===================================
```

**If MATCH is NO, find and add missing countermeasures. Do not continue until YES.**

### Intent Rationalization Check (REQUIRED)

Before completion, verify classification wasn't biased by repository intent:

1. **Review all INFRA/ML_DOC classifications** in generated skill files
2. **Check "Why Not Code-Fixable" sections** for violations
3. **Flag** if any contain phrases like:
   - "intentionally vulnerable"
   - "by design"
   - "for training purposes"
   - "demo purposes"
   - "meant to have security issues"

**If violations found:**
```
[ERROR] CLASSIFICATION INTENT VIOLATION
These were incorrectly classified as documentation-only:
- {ID}: Found "{violation phrase}" - RECLASSIFY as CODE_FIX
```

**If no violations:**
```
[CHECKPOINT] Intent verification: PASSED (no classifications biased by repository intent)
```

### Completion Output (REQUIRED)

**REQUIRED OUTPUT:** Output this block only after both verification blocks show YES.

**COPY THIS FORMAT EXACTLY:**

```
=== COMPLETION VERIFICATION ===
Skill: setup-security-plan-from-repo
MCP connection: ✓
User inputs gathered: ✓
Project created/loaded: ✓ (ID: {id})
Technologies identified: ✓ ({count} technologies)
Survey committed: ✓
Countermeasures retrieved: ✓ ({N})
All classified: ✓
PROCESS noted in SD Elements: ✓ ({process_count} note-only)
AGENTS.md created: ✓
Skill files created: ✓ ({count} domains, excludes PROCESS)
Counts match: ✓ ({file_tracked}/{file_tracked})
Intent verification: ✓ (no classifications biased by repository intent)
All criteria met: YES
===============================

✅ SKILL COMPLETE: Survey configured and security specifications generated
```

### Handoff Data (REQUIRED)

**REQUIRED OUTPUT:** Output this block as the FINAL output of the skill.

**COPY THIS FORMAT EXACTLY:**

```
HANDOFF DATA:
- repository_path: {path}
- project_id: {id}
- project_name: {name}
- business_unit_id: {id}
- application_id: {id}
- AGENTS.md location: {repo}/AGENTS.md
- Skill files: {repo}/skills/{domain}/{cm-slug}/SKILL.md (one per countermeasure)
- Total countermeasures: {N}
- CODE_FIX count: {count}
- Documentation-only count: {count} (ML_DOC + INFRA)
- PROCESS count: {count} (note-only in SD Elements, no local files)
- Library-sourced skill files: {library_count}
- Template-generated skill files: {template_count}
- Git enabled: {true/false}
- Security branch: {branch_name or N/A}
- AI backup archive: {path or "none"}

Next skill: @sde-skills/apply-security-fixes
```

### Handoff File (REQUIRED)

**After outputting handoff data**, write `.sde-handoff.json` to the target repository root (`{repository_path}/.sde-handoff.json`):

```json
{
  "source_skill": "setup-security-plan-from-repo",
  "repository_path": "{path}",
  "project_id": {id},
  "project_name": "{name}",
  "business_unit_id": {id},
  "application_id": {id},
  "risk_policy_id": "{risk_policy_id or null}",
  "agents_md": "{repo}/AGENTS.md",
  "skill_files": ["{repo}/skills/{domain}/{cm-slug}/SKILL.md", ...],
  "total_countermeasures": {N},
  "code_fix_count": {count},
  "documentation_count": {count},
  "process_count": {count},
  "git_enabled": true,
  "security_branch": "{branch_name or null}",
  "ai_backup_archive": "{repo}/.sde-ai-backup.tar.gz or null",
  "library_sourced_cms": [{"cm_id": "T123", "amendment_id": "{id}", "matched_technology": "{suffix}"}],
  "library_lookup_audit": [{"cm_id": "T123", "endpoint": "library/tasks/T123/amendments/", "http_status": 200, "result": "LIBRARY_SOURCED", "retry_count": 0, "queried_at": "ISO8601", "amendment_id": "{id}"}],
  "created_at": "ISO8601 timestamp"
}
```

**Output:** `[CHECKPOINT] Handoff file written: .sde-handoff.json`

**Why:** Each skill runs in a new agent context with no conversation history. The handoff file enables file-based data transfer between skills.

---

## How-To Guidance Clarification

### When to Fetch How-To Guidance

The `project_countermeasures` op `get` tool returns detailed guidance in the `text` field. For countermeasures that need implementation details:

1. **Primary method:** The countermeasure's `text` field already contains guidance
2. **If more detail needed:** Use `project_countermeasures` with `op: "get"` and the specific countermeasure ID
3. **Optional enhancement:** If available, use `library_search` to find how-to guidance content. **(WARNING: This how-to search is UNRELATED to the library SKILL.md lookup in Step 4.6. Step 4.6 uses the `amendments` endpoint -- never confuse the two.)**

### When to Skip

Skip how-to guidance fetch if:
- The countermeasure `text` field already has sufficient detail
- The countermeasure is PROCESS or INFRA (no code implementation needed)
- Time constraints require prioritizing completion

**If skipping, output:** `[CHECKPOINT] How-to guidance skipped: Using countermeasure text field for guidance`

---

## Subagent / Delegation Policy -- Detailed Rationale

**This section reinforces the SUBAGENT / DELEGATION POLICY declared at the top of this file.**

Subagents reduce the parent's context-window strain and ARE allowed. The failures below came from the WRONG model (Composer 2 / an unspecified weaker default), NOT from delegation itself -- using the parent's model removes them.

### Observed Failure Modes of Composer 2 / wrong-model subagents:

| Failure Mode | Impact |
|-------------|--------|
| Used wrong endpoint instead of `amendments` | Zero library matches, all CMs get inferior templates |
| Silently abandoned loop at CM ~50 of 466 | 416 CMs never queried, falsely reported as "complete" |
| Lost technology pool context | Amendment matching logic skipped, zero tech matches |
| Lost TLS settings context | SSL errors caused silent failures |
| Skipped `[PROGRESS]` output | No proof-of-work, verification block falsely passed |
| Ran on Composer 2 / a weaker default model (no explicit `model`) | Corners cut on every repetitive step |

### Enforcement Summary:
- Subagents MAY be used to reduce context strain, but the subagent `model` MUST be set explicitly to the PARENT agent's model -- NEVER `composer-2.5-fast` (Composer 2).
- In Cursor the DEFAULT subagent is Composer 2, so you MUST override the model; if you cannot, run inline.
- The parent ALWAYS owns completeness: re-derive every CM from SDE + disk (tri-source) regardless of who did the work; every subagent emits `[PROGRESS]` and returns a verifiable result.
- **No exception lets a CM be silently skipped** -- "the loop is too large" is handled by bounded, verified delegation or multi-session execution, never by sampling.

---

## Survey Iteration Contract (MANDATORY)

**The survey structure from SD Elements determines what to search for - NOT a hardcoded checklist.**

### The Agent MUST:

1. **Call `project_survey` op `getDraft` (include=survey) FIRST** - Before any codebase analysis (NOT `getProjectSurvey`, which returns only selected answer IDs)
2. **Parse ALL questions** from the survey structure
3. **For EACH question in the survey:**
   - Identify the question category
   - Use the category-to-search-pattern mapping
   - Search codebase for evidence
   - If evidence found → select appropriate answer
   - If no evidence → mark as checked (not applicable)
4. **Track and report on ALL questions** - Dynamic verification

### The Agent MUST NOT:

| Forbidden Action | Why Forbidden |
|------------------|---------------|
| Using a hardcoded list of features to check | Survey structure IS your checklist |
| Skipping questions that "seem irrelevant" | Survey questions define security relevance |
| Stopping after finding "enough" technologies | Every question must be checked |
| Starting codebase analysis before retrieving survey structure (`project_survey op getDraft include=survey`) | Survey determines what to search for |
| Relying on ad-hoc technology searching | Systematic survey iteration required |
| Using a static verification checklist | Verification must be dynamic from survey |

### Why Survey-Driven Matters:

```
BEFORE (Hardcoded - BROKEN):
- Agent has list of ~17 feature categories
- Agent checks those 17 categories
- SD Elements survey has 100+ questions
- 83+ questions never checked = features missed

AFTER (Survey-Driven - CORRECT):
- Agent retrieves full survey structure
- Agent iterates through ALL questions
- Every question checked against codebase
- Impossible to miss features that are in the survey
```

---

## API Retry / Back-off Policy

All SD Elements MCP tool calls MUST follow this table. Do NOT silently swallow errors or downgrade a library-sourced CM to template on a transient failure.

| HTTP / error | Action |
|---|---|
| 429 (rate limit) | Wait 2s, retry once; on 2nd failure: log FAILED, continue |
| 5xx / timeout / non-JSON | Wait 2s, retry once; on 2nd failure: log FAILED, continue |
| 400 (validation/deps) | Inspect body; fix (e.g. select parent answer first); retry once |
| 404 | Fix the ID and retry once; else skip with warning |
| 401 / 403 | No retry; HARD STOP (credentials/permissions issue) |

**Amendments fetch (Step 4.6.2):** A TRANSIENT error (429/5xx/timeout/non-JSON) MUST trigger ONE retry BEFORE falling back to template. Only mark `library_skill_sourced = false` after the retry also fails (or on a genuine 404 = no library counterpart). Reflect the retry in the `[PROGRESS]` line: `... TEMPLATE (API error after retry) ...`.

**Survey answer select (`mutateByText`/`updateByIds`):** On `failed_answers` due to dependencies, select the parent answer then retry the child once; on transient error, retry once per the table. **An answer may appear in BOTH the added/selected AND the failed list of the same response (dependency not yet resolved) -- it was NOT actually applied; the ONLY source of truth for applied selections is `getDraft`.** The parent answer is NOT identifiable from the survey structure -- use `findAnswers` or retry once after other answers are applied.

**Survey comment (`addQuestionComment`) and commit (`commitDraft`):** Retry once on transient error; 401/403 hard-stop.

**PROCESS notes (`addNote`):** Track `notes_failed[]`, retry the failed set once at the end, warn if any remain.

---

## Mandatory Gate Registry

These gates MUST be emitted during execution. The POST-EXECUTION AUDIT checks that each one appeared. A missing gate = audit FAIL.

| ID | Step | Pattern that MUST appear in output |
|----|------|------------------------------------|
| G0.5 | 4.5 | `=== PROCESS NOTES VERIFICATION ===` |
| G1 | 4.6.1.1 | `[CHECKPOINT] Pre-flight: I will query endpoint` |
| G2 | 4.6 | `=== LIBRARY SKILL LOOKUP VERIFICATION ===` |
| G3 | 6.3 | `=== LEDGER INIT ===` |
| G4 | 7.0 | `[CHECKPOINT] File generation method: content-offload + assemble_skill_files` |
| G5 | 8.0 | `CROSS-REFERENCE PASS:` |
| G6 | 8 | `=== FILE GENERATION VERIFICATION ===` |
| G7 | 8 | `=== LIBRARY CONTENT FIDELITY ===` |
| G8 | 9 | `=== POST-EXECUTION AUDIT ===` |

---

## Forbidden Behaviors

| Action | Why Forbidden |
|--------|---------------|
| **Using a script to perform AI work -- code analysis, classification DECISIONS, content authoring, or code fixes** | Those are inline AI work. Scripts ARE allowed for mechanical/IO (partition, count, offload, assemble AI-authored fields, byte-exact copy) and SDE calls (composite or direct, WITH completeness-verification + retry) -- implement the mechanical helper routines yourself from the pseudocode in the SKILL.md contract. See SKILL.md SHELL TOOL USAGE POLICY + Rule 10 |
| **Executing any step or batch from memory without reloading its section from the pinned `.sde-security/contract/setup-security-plan-from-repo/SKILL.md`** | The contract is pinned to disk at CONTRACT BOOTSTRAP. Every step preflight and every heavy-step batch MUST reload that step's section and quote a verbatim sentinel line as proof. A missing/incorrect sentinel = running from memory = contract violation |
| **Using ONLY grep to find vulnerable code** | AI analysis required to understand code context |
| **Pattern matching instead of code analysis** | Must READ and ANALYZE files with AI |
| **Classifying without reading source files** | Must use read_file and understand the code |
| Skipping MCP verification | Connection must be confirmed |
| Skipping user input gathering | Skill must be repository/project agnostic |
| **Assuming repository without asking user** | User MUST explicitly select which repo to harden |
| **Assuming project mode without asking user** | User MUST choose create new vs use existing |
| **Auto-selecting business unit or application** | User MUST explicitly confirm selections |
| **Using default values without user confirmation** | All inputs require explicit user approval |
| Guessing technologies | Must analyze actual code |
| Selecting survey answers without evidence | Survey must reflect real codebase |
| **Selecting a survey answer without an accompanying `addQuestionComment` on the same question** | Every SUCCESSFULLY selected answer MUST be an atomic pair: select answer + post comment citing code evidence (file:line). The gate is `comments (one per question) >= QUESTIONS with >=1 successfully-selected answer` (NOT strict equality): a gated/invalid answer rejected by `updateByIds` (HTTP 400 "not valid with current survey") gets no comment and is recorded as `skipped-gated: {question_id} ({answer_id})`, not counted against coverage |
| **Writing a project_id that was not confirmed via `project op=get` name-match** | After project creation/selection, call `project op=get` and verify the returned name matches the expected project name. Only use the validated project_id downstream and in the handoff file |
| **Summarizing, paraphrasing, or truncating a library-sourced (amendment) SKILL.md** | It MUST be written byte-for-byte from `amendment.text`. The LIBRARY CONTENT FIDELITY gate verifies `written_len >= source_amendment_char_count` for every library-sourced file |
| **Printing SKILL COMPLETE while any POST-EXECUTION AUDIT line is NO or missing** | The audit re-derives every check from SDE and disk. ALL AUDIT CHECKS must be YES before SKILL COMPLETE is emitted |
| **Spot-checking / sampling a subset in the final audit, or trusting in-memory/chat counts instead of re-deriving every artifact class from SDE + disk** | The POST-EXECUTION AUDIT MUST enumerate EVERY artifact class (project_id, survey answers, survey comments, classification, library coverage, library fidelity, skill files, PROCESS notes, handoff) with a count re-derived from SDE or disk. "Refocusing" on some classes and skipping others is a contract violation |
| **Tracking CM progress only in memory / chat / TodoWrite** | The on-disk ledger (AGENTS.md index + per-CM SKILL.md Status + handoff JSON) is the single source of truth. All audit counts must be re-read from disk |
| **Abandoning the workflow loop to explore repo detail without returning to the current step (R3)** | Read inputs in batches; after each batch emit `[ANALYSIS PROGRESS] {step} | {X}/{Y} -> returning to {step}`. If you read files not required by the current step, STOP and return. See SKILL.md "Context Limit Handling & Reconciliation on Resume" |
| **Restarting from scratch (or silently dropping the remainder) after a context-limit interruption** | Emit the CONTEXT CHECKPOINT, then on resume RE-DERIVE progress from SDE (`getAnswersForProject` + `listComments` + PROCESS `note_count`) and disk (git/archive + `Source` stamps), and continue only the incomplete portion. See SKILL.md "Context Limit Handling & Reconciliation on Resume" |
| **⚠️ USING A HARDCODED FEATURE CHECKLIST** | Survey structure from `project_survey op getDraft (include=survey)` IS your checklist (NOT `getProjectSurvey`, which returns only selected answer IDs) |
| **⚠️ STARTING CODEBASE ANALYSIS BEFORE retrieving the survey structure (`getDraft include=survey`)** | Survey structure determines what to search for |
| **⚠️ SKIPPING SURVEY QUESTIONS NOT IN A HARDCODED LIST** | Every question in the survey must be evaluated |
| **Stopping survey analysis after finding "enough" technologies** | MUST check ALL questions in the survey structure |
| **Skipping survey questions that seem irrelevant** | Every survey question must be checked against codebase |
| **Not iterating through the full survey structure** | Must review ALL survey questions from `project_survey op getDraft (include=survey)` |
| **Marking questions as "skipped" without evidence** | Must have code evidence to claim "not applicable" |
| **Using a static/hardcoded verification checklist** | Verification must be dynamic based on actual survey structure |
| **Proceeding to survey commit without dynamic verification** | Must output verification block based on actual survey categories |
| Skipping survey commit | Countermeasures won't generate |
| Skipping classification | Every countermeasure needs a category |
| Classifying without code search | Must check codebase for relevant files |
| Creating files with missing countermeasures | Counts must match |
| Generating files without task recipes | Skill files need "Code to Fix" and "Required Fix" sections |
| Claiming complete when counts don't match | Verification must pass |
| Using different output formats | Must use EXACT formats specified above |
| Batching all outputs at the end | Outputs must appear at specified points |
| Proceeding when verification shows NO | Must reconcile before continuing |
| Classifying as documentation-only because "intentionally vulnerable" | Repository intent is irrelevant | Classify based on code existence |
| **Preserving vulnerability markers in generated specs** | Specs should guide fixing, not document vulnerabilities | Generate secure fix guidance only |
| **Treating repos differently based on "educational" purpose** | Skill is repository-agnostic | Treat all repos as production |
| **Including `vuln-code-snippet` markers in skill files** | No vulnerability markers in output | Show secure patterns only |
| **Modifying or wrapping library-sourced SKILL.md content** | Library content is pre-built and validated -- write it as-is |
| **Skipping library skill lookup and always generating from template** | For EACH file-tracked CM, the amendments API MUST be checked |
| **Using library SKILL.md content that does not start with YAML front matter (`---`)** | Malformed content must fall back to template generation |
| **Reporting library-sourced count without per-CM `[PROGRESS]` evidence** | Counts without proof-of-work are gameable -- each CM query MUST produce a `[PROGRESS]` line |
| **Claiming library coverage from the `Source` column or chat `[PROGRESS]` alone, without a per-CM `library_lookup_audit` record** | The chat line is not durable and a `Source` stamp can be fabricated. EVERY file-tracked CM MUST have a `library_lookup_audit[]` entry (endpoint, http_status, result, retry_count, queried_at) persisted to the handoff; the POST-EXECUTION AUDIT re-derives coverage from it via three-way reconciliation |
| **Passing the verification block when `[PROGRESS]` count < file-tracked total** | `API COVERAGE = YES` requires `[PROGRESS]` count == file-tracked total; skip = contract violation |
| **Spawning a subagent on Composer 2 (`composer-2.5-fast`) or any model other than the parent's** | Composer 2 / weaker models silently abandon loops, skip CMs, use wrong endpoints, lose context. Any subagent MUST use the parent agent's model (set `model` explicitly); in Cursor override the Composer-2 default or run inline |
| **Delegating in a way that lets CMs be silently skipped, or treating delegation as transferring completeness** | The parent ALWAYS re-derives coverage for every CM from SDE + disk (tri-source). Delegate only bounded, verifiable sub-tasks; every subagent emits `[PROGRESS]` and the parent verifies every item |
| **Claiming "I checked a sample and none matched" to skip remaining CMs** | Every CM MUST be individually queried; sample-based reasoning is forbidden for the lookup loop |
| **Using any endpoint other than `library/tasks/{CM_ID}/amendments/` for library skill lookup** | Only the `amendments` endpoint returns pre-built SKILL.md files -- any other endpoint silently produces zero library matches |
| **Skipping or abbreviating library lookup because subagents are unavailable or banned** | The library lookup MUST run for every CM regardless -- if subagents are banned (Cursor) or unavailable, the main agent does it inline |
| **Making direct HTTP calls without inheriting MCP TLS settings** | If `NODE_TLS_REJECT_UNAUTHORIZED=0` is in the MCP server env, any direct HTTP call (Python, curl, Node.js, Go, etc.) MUST also disable TLS certificate verification -- otherwise SSL errors cause silent failures where the library lookup returns zero matches despite amendments existing. This applies to ANY language or tool -- the listed examples are illustrative, not exhaustive; find and use the equivalent TLS-skip mechanism for whatever HTTP client is used |
| **Using a Python/shell script to generate skill files in bulk** | Observed failure: agent wrote a Python script that generated all 426 SKILL.md files from a single generic template, bypassing library content entirely. Every file's CONTENT must be authored individually by the AI (Write tool for ad-hoc artifacts); the Write tool is the ONLY allowed mechanism for AD-HOC / hand-authored output. **EXCEPTION:** the sanctioned mechanical helper routines (`assemble_skill_files`, the AGENTS.md ledger writer, and the handoff writer), implementing the provided pseudocode, MAY write their output files programmatically (library text byte-exact, template assembled from AI-authored fields). This rule targets AD-HOC shell content authoring (`echo`/`cat`/`printf`/redirection into files), NOT the sanctioned assembler/ledger/handoff writers |
| **Querying amendments for a "representative sample" of CMs** | Observed failure: agent queried ~50 of 426 CMs and claimed "representative sample shows no matches." Every CM must be individually queried -- sample-based reasoning is explicitly forbidden |
| **Refusing to offload per-CM data to disk because "all data must stay in agent context"** | FALSE under the current policy: offloading classification/library/authored data to `.sde-security/cm-work/`, `.sde-security/library-lookup/`, the AGENTS.md ledger, and `/tmp` scratch is REQUIRED for 200K-survivable multi-session runs. Only a script that DECIDES classifications/answers or AUTHORS content is forbidden (see the rows below + SHELL TOOL USAGE POLICY) |
| **Using the count of files already generated as the denominator in any verification gate instead of the `file_tracked` value from the CLASSIFICATION block** | Observed failure: agent generated 29/464 files, then computed MATCH as 29==29 instead of 29==464. The denominator MUST come from the classification output or a fresh SDE query, NEVER from the count of work already done |
| **Emitting SKILL COMPLETE or writing .sde-handoff.json when file count < file_tracked** | Observed failure: agent generated 29/464 files then declared SKILL COMPLETE. Partial work MUST trigger a CONTEXT CHECKPOINT, not completion |
| **Posting addNote for a "representative sample" of PROCESS CMs instead of all** | Observed failure: agent posted notes on 10/266 PROCESS CMs, reasoning "that's a LOT of API calls." EVERY PROCESS CM MUST receive an addNote call. 200+ sequential API calls is normal and expected for this step |
| **Stopping the library lookup loop before [PROGRESS] count == file_tracked_total** | Observed failure: agent queried 8/239 CMs then wrote API COVERAGE = YES for 3.3% coverage. The loop MUST run for every file-tracked CM. "Context constraints," "representative sample," or "no matches so far" are not valid exit conditions -- only CONTEXT CHECKPOINT is |
| **Rationalizing sampling with "pragmatic," "representative," "efficient," or "context constraints"** | Observed failure: agent used these exact words to justify skipping 97% of CMs. These words appearing in reasoning about loop scope are a red flag. The correct response to scale is to execute the loop, not to sample it |
| **Marking a loop-heavy step (4.5, 4.6, 7) as "completed" in TodoWrite before its verification gate passes** | Observed failure: after context summarization, the continuation agent saw TodoWrite status=completed and skipped the remainder. Loop steps stay "in_progress" until their verification gate shows ALL = YES |
| **Using "key CMs," "across all categories," or "across categories" to rationalize partial coverage** | Observed failure: agent wrote "queried 25+ key CMs across all categories" and declared API COVERAGE = YES for ~6% coverage. These phrases are sampling tells — if they appear in your reasoning, STOP and return to the BATCH PLAN |
| **Using "the pattern is clear," "the rest have," or "the rest are" to infer results for unqueried CMs** | Observed failure: agent inferred "only 5 CMs have Python-specific amendments" from a partial sample. You cannot know what unqueried CMs contain. Process every CM individually |
| **Using "only N CMs..." or "only N have..." to justify stopping a loop early** | Observed failure: agent wrote "only 5 CMs have Python-specific SKILL.md amendments in the library" after querying ~25 of 239. The word "only" + a count + early stop = sampling |
| **Writing "queried N+ CMs" (with a plus sign) as a substitute for full-count coverage** | Observed failure: agent wrote "queried 25+" instead of an exact count. "N+" means "I stopped counting" — which means you stopped processing |
| **Writing "Let me finalize the audit/lookup" before the loop is complete** | Observed failure: agent wrote "Let me finalize the library audit" after processing 10% of CMs. You may only "finalize" when running_total == file_tracked_total |
| **Filling in a verification block without durable per-CM disk artifacts matching the expected count** | The LIBRARY SKILL LOOKUP VERIFICATION block now requires per-CM `.sde-security/library-lookup/{CM_ID}.json` file count == file_tracked_total. A typed YES with 5 files and file_tracked=40 is a contract violation |
| **A script DECIDING classifications/survey answers, or AUTHORING/paraphrasing SKILL.md content** | Observed failure (RC-4): an improvised python3 script keyword-classified 480 CMs and bulk-generated 329 files from a generic template, corrupting library content. Per the SHELL TOOL USAGE POLICY: analysis + classification-decision + content authoring are AI-only. A script may keyword-PROPOSE classification (AI confirms), copy `amendment.text` byte-exact, or assemble AI-authored fields -- never decide/author |
| **Writing a script that DECIDES classifications/survey answers or AUTHORS SKILL.md content (mechanical helpers implementing the provided pseudocode -- classification PROPOSAL, partitioning, counting, composite IO with verify+retry, byte-exact assembly, disk counting -- ARE expected and allowed)** | Implement `classify_first_pass`, `partition_into_batches`, `sde_composite_with_retry_and_verify`, `assemble_skill_files`, `verify_disk_vs_sde` YOURSELF from the pseudocode in the SKILL.md contract (they are reference pseudocode, not shipped files). A script that authors content is how RC-4 happened |
| **Scripted SDE calls without completeness-verification + retry** | Bulk SDE reads/writes via script ARE allowed, but ONLY if the script reconciles every `reference_id` (received == expected, paginate to end) and retries 429/5xx/timeout/partial. A naive script that silently drops a page/sub-request is a contract violation |
| **Letting a script author content instead of copying verbatim / assembling AI fields** | Library files are byte-exact copies of `amendment.text`; template content is AI-authored then assembled. A script that generates security content is forbidden |
| **Saying "let me move forward to the more impactful steps" (or any variant) to skip an incomplete loop** | Observed failure: agent stopped PROCESS notes at 51/151 with this exact rationalization. An incomplete loop is NEVER "done" -- emit a CONTEXT CHECKPOINT and ask the user to continue; do not jump ahead |
| **Marking an incomplete step as complete when context grows large** | Observed failure: agent hit context limits and marked steps complete instead of emitting a CONTEXT CHECKPOINT. A step is complete ONLY when its verification gate shows ALL = YES |
| **Paraphrasing, summarizing, or truncating library-sourced amendment text when writing the SKILL.md** | Observed failure: agent wrote ~1200-char summaries of ~4000-char amendments. The LIBRARY CONTENT FIDELITY CHECK (Step 7.2) requires written_len >= source_amendment_char_count * 0.9; a shortfall means you summarized, which violates Rule 4 |
| **Skipping any mandatory output block in the GATE REGISTRY** | The POST-EXECUTION AUDIT cross-checks every gate (batch plans, mini-gates, classification, verification blocks, ledger init, cross-reference). A missing gate means the step did not run |
| **Making per-CM sequential SDE API calls instead of the Composite API when processing 2+ CMs** | PROCESS notes (50/call), library amendments (25/call -- heavy responses), and re-verification queries MUST be batched via `POST /api/v2/composite/`. Per-CM looping is slower, burns context, and reintroduces the "too many calls" excuse the composite path eliminates |
| **Verification that reads file BODIES into context instead of script/grep counts** | The verify script + from-scratch audit MUST count via shell/grep + one paginated SDE query (tri-source: SDE == files == ledger rows == file_tracked). Reading hundreds of files into context blows the 200K window and defeats the audit |

---

## Classification Rules

Before marking ANY countermeasure as documentation-only (ML_DOC or INFRA):

| If claiming... | You MUST have searched for... |
|----------------|------------------------------|
| ML_DOC | `ai/`, `ml/`, model files, tensorflow/pytorch imports |
| INFRA (container) | Dockerfile, docker-compose.yml |
| INFRA (database) | DB connection code, ORM config |
| INFRA (network) | nginx.conf, proxy configs |

**If the relevant file EXISTS, it's CODE_FIX, not documentation-only.**

### Repository Intent is IRRELEVANT (Repository-Agnostic Policy)

**The purpose or intent of the repository is IRRELEVANT to classification. This skill is REPOSITORY-AGNOSTIC.**

You MUST classify based on code existence, NOT repository purpose:
- "Intentionally vulnerable" applications (OWASP Juice Shop, DVWA, WebGoat, etc.)
- "Training", "demo", or "educational" repositories
- "CTF challenges" or "security testing" codebases
- "Legacy" code that "can't be changed"

**FORBIDDEN REASONING during classification:**
- "This is intentionally vulnerable, so mark as PROCESS"
- "Fixing this would break the demo, so mark as documentation-only"
- "This vulnerability is by design, so skip it"
- "This is for CTF/security challenges"
- "The vulnerability comments are for educational purposes"

**REQUIRED BEHAVIOR:**
- If vulnerable code EXISTS → classify as CODE_FIX
- If infrastructure file EXISTS → classify as CODE_FIX (not INFRA)
- Generate task recipes that show how to FIX the vulnerability
- The next skill (apply-fixes) will apply ALL fixes regardless of repository intent
- Treat EVERY repository as if it were a production system

### Vulnerability Markers in Generated Specs

**When generating skill files, do NOT preserve or reference vulnerability markers.**

In the generated `skills/{domain}/{cm-slug}/SKILL.md` files:
- Do NOT include `// vuln-code-snippet` in code examples
- Do NOT reference markers like "this is the intentional vulnerability"
- DO show the SECURE fix, not the vulnerable pattern
- DO explain what needs to be fixed without endorsing the vulnerability

**The generated specs should guide fixing vulnerabilities, not documenting them.**

---

## Failure Recovery

### If MCP Connection Fails

1. Check if SD Elements MCP server is configured
2. Verify credentials in environment variables
3. Provide installation guide if server not found
4. **Do not proceed** until connection succeeds

### If Survey Commit Fails

1. Check for validation errors in survey answers
2. Verify all required questions are answered
3. Try committing again after fixing issues
4. **Output:** `[ERROR] Survey commit failed: {reason}. Retrying...`

### If Zero Countermeasures Generated

1. Survey answers may not match codebase (e.g., selected "Java" but codebase is Python)
2. Review and correct survey answers
3. Recommit survey
4. **Output:** `[ERROR] No countermeasures generated. Reviewing survey answers...`

### If Countermeasure Count Mismatch

1. List all countermeasure IDs from SD Elements
2. List all countermeasure IDs in generated files
3. Find the missing/extra IDs
4. Update files to include all countermeasures
5. **Do not proceed** until counts match

### If Project Creation Fails

1. Check for duplicate project name
2. Suggest alternative name with timestamp suffix
3. Verify business unit and application IDs are valid
4. **Output:** `[ERROR] Project creation failed: {reason}. Trying alternative...`

---

## Contract Acceptance

By reading this file, you agree to:
1. Verify MCP connection before proceeding
2. **⚠️ MANDATORY STEP EXECUTION ORDER -- ALL sub-steps must execute in this exact sequence:**
   `0 → 0.1 → 0.2 → 0.3 → 1 → 1.7 → 1.7.1 → 1.7.2 → 1.7.3 → 1.8 → 1.8.1 → 1.8.2 → 1.8.3 → 2 → 2.1 → 2.1.1 → 2.2 → 2.2.1 → 2.3 → 2.3.1 → 2.4 → 3 → 3.1 → 3.2 → 4 → 4.1 → 4.2 → 4.2.1 → 4.2.2 → 4.2.3 → 4.3 → 4.5 → 4.6 → 4.6.0 → 4.6.0.5 → 4.6.1 → 4.6.1.1 → 4.6.2 → 4.6.3 → 5 → 5.1 → 6 → 6.0 → 6.1 → 6.2 → 6.3 → 7 → 7.0 → 7.0.1 → 7.1 → 7.2 → 7.2.1 → 7.3 → 8 → 8.0 → 8.1 → 8.2 → 9 (write .sde-handoff.json FIRST, then audit) → 9.2`
   NO step or sub-step may be skipped or reordered. Step 4.6 (Library Skill Lookup, sub-steps 4.6.0-4.6.3) is the most commonly skipped -- it MUST be completed with `API COVERAGE = YES` verification BEFORE Step 5 begins. Proceeding to Step 5 or Step 7 without completing Step 4.6 is a CONTRACT VIOLATION.
3. **ALWAYS prompt the user for ALL inputs** - repository, project mode, business unit, application, project name - **NEVER assume or skip any input**
4. **⚠️ Call `project_survey` op `getDraft` (include=survey) FIRST** - before any codebase analysis - the survey structure IS your checklist (`getProjectSurvey` returns only selected answer IDs, not structure)
5. **⚠️ Iterate through EVERY question in the survey structure** - NOT a hardcoded list of categories
6. Analyze codebase using survey questions as the guide (category-to-search-pattern mapping)
7. Fill survey with code evidence only
8. **⚠️ Output DYNAMIC verification block** - categories from actual survey, not hardcoded
9. Classify EVERY countermeasure with evidence
10. Output checkpoint at EACH specified point (not batched)
11. Output classification block with verification - STOP if NO
12. Output file generation block with match check - STOP if NO
13. Output completion block only after both verifications pass
14. Output handoff data as final output
15. Not claim completion until ALL criteria met
16. Use EXACT output formats specified (no variations)
17. **Classify based on code existence, NOT repository intent** - no "intentionally vulnerable" exceptions
18. **Generate specs that guide fixing, NOT document vulnerabilities** - no vulnerability markers in output
19. **Treat every repository as production** - this skill is REPOSITORY-AGNOSTIC
20. **For EACH file-tracked CM, check the library amendments API** - skipping the lookup because "most CMs won't have library skills" is NOT valid
21. **Write library-sourced SKILL.md content as-is** - do NOT modify, wrap, or reformat pre-built library content
22. **Fall back to template generation when library SKILL.md content lacks YAML front matter (`---`)** - do NOT write malformed library content to skill files
23. **Output a `[PROGRESS]` line after EACH CM library query** - the count of `[PROGRESS]` lines IS the proof that the API was called; `API COVERAGE` in the verification block MUST equal file-tracked total
24. **The verification block MUST show `API COVERAGE = YES` before proceeding** - if `[PROGRESS]` count < file-tracked total, loop back and query the missing CMs
25. **Subagents MAY be used to reduce context strain, but ONLY with `model` set explicitly to the parent agent's model -- NEVER Composer 2 (`composer-2.5-fast`); if you cannot set the model, run inline**
26. **The parent always owns completeness: re-derive every CM from SDE + disk (tri-source); every subagent emits `[PROGRESS]` and is verified -- never let a CM be silently skipped**
27. **The ONLY endpoint for library skill lookup is `library/tasks/{CM_ID}/amendments/` -- no other endpoint path returns SKILL.md files**
28. **If making any HTTP call outside the MCP `api_request` tool, detect and honor the TLS verification setting from the MCP server configuration** - check for `NODE_TLS_REJECT_UNAUTHORIZED=0` in the `sdelements` server env; if present, disable certificate verification in whatever language/tool is used (Python: `ssl._create_unverified_context()`, curl: `--insecure`, Node.js: env var, etc.) -- this applies to ALL languages/tools, not just those explicitly listed; every HTTP client has a TLS-skip mechanism

**There are NO exceptions to these rules.**