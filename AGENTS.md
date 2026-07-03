# vuln-bank

<!-- SDE-SECURITY-HARDENING-START -->
## Security Hardening (SD Elements)

### Project Overview

| Field | Value |
|-------|-------|
| Application | oleg-vuln-bank-live-20260703 |
| SD Elements Project | [oleg-vuln-bank-live-20260703](https://cd.sdelements.com/bunits/oleg-vb-live-bu-20260703/oleg-vb-live-app-20260703/oleg-vuln-bank-live-20260703/) |
| Project ID | 31942 |
| Total Countermeasures (selected scope) | 10 |
| Source | Codebase |

### Countermeasure Summary by Category

| Category | Count |
|----------|-------|
| CODE_FIX | 5 |
| ML_CODE | 1 |
| ML_DOC | 1 |
| INFRA | 1 |
| PROCESS (note-only, no files) | 2 |

### Countermeasures by Domain

#### sql-injection

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T38 | Bind variables in SQL statements | skills/sql-injection/T38-bind-variables-in-sql-statements/SKILL.md | 10 | CODE_FIX | Applied | TEMPLATE |

#### xss

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T36 | Escape untrusted data in HTML, HTML attributes, CSS, and JavaScript | skills/xss/T36-javascript/SKILL.md | 8 | CODE_FIX | Applied | LIBRARY:TA8479 |

#### secrets

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T76 | Do not hardcode passwords | skills/secrets/T76-python/SKILL.md | 10 | CODE_FIX | Applied | LIBRARY:TA8509 |

#### csrf

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T29 | Use anti-Cross-Site Request Forgery (CSRF) tokens | skills/csrf/T29-use-anti-csrf-tokens/SKILL.md | 7 | CODE_FIX | Applied | TEMPLATE |

#### llm-security

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T4457 | Prevent prompt injection in Large Language Models (AI/ML Developer) | skills/llm-security/T4457-python/SKILL.md | 7 | ML_CODE | Applied | LIBRARY:TA8621 |
| T4465 | Prevent training data poisoning in Large Language Models (AI/ML Developer) | skills/llm-security/T4465-prevent-training-data-poisoning/SKILL.md | 7 | ML_DOC | Skipped | TEMPLATE |

#### transport-security

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T21 | Ensure all data in transit is encrypted using a secure TLS channel | skills/transport-security/T21-python/SKILL.md | 8 | CODE_FIX | Documented | LIBRARY:TA8620 |

#### container-security

| ID | Title | Skill File | Priority | Category | Status | Source |
|----|-------|-----------|----------|----------|--------|--------|
| T4746 | Ensure container images are secure | skills/container-security/T4746-ensure-container-images-are-secure/SKILL.md | 10 | INFRA | Applied | TEMPLATE |

### Progress Tracking

| Metric | Count |
|--------|-------|
| Total skill files | 8 |
| Applied | 6 |
| Documented | 1 |
| Skipped | 1 |
| Pending | 0 |

### Completion Requirements

- Every skill file above must reach a terminal status (Applied for code, Documented for ML_DOC/INFRA) via `@sde-skills/apply-security-fixes`.
- PROCESS countermeasures (T2348, T178) are noted in SD Elements and require no local files.

### Verification Checklist

- [ ] All CODE_FIX / ML_CODE skill files applied to source
- [ ] All ML_DOC / INFRA skill files documented
- [ ] PROCESS countermeasures noted in SD Elements
- [ ] Fixes verified against SD Elements countermeasure guidance

<!-- SDE-SECURITY-HARDENING-END -->
