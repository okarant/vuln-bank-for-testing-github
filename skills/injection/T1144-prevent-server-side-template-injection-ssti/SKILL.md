---
name: t1144-prevent-server-side-template-injection-ssti
description: Prevent SSTI using the following techniques: - Use a safe Template engine that only allows white-list functions and are syntax safe. - Use the validation functions of the Template engine if it provides them. - Sandbox your Template engine i
---

# T1144: Prevent Server-Side Template Injection (SSTI)

**Category:** CODE_FIX  
**SD Elements:** [T1144](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1144/)  
**Priority:** 8  
**Domain:** injection

## Affected Areas in This Repository

auth.py (sqlite3 string-concatenated queries, e.g. login L97, check_balance L132, transfer L158-166), app.py (psycopg2 queries built via f-strings/`%`), transaction_graphql.py (f-string SQL at L46/78/106/155), merchant_payments.py

## Required Fix

Use parameterized queries everywhere: psycopg2 `cursor.execute(sql, params)` with `%s` placeholders and sqlite3 with `?` placeholders. Never interpolate user input into SQL/template/command strings. For template injection, keep Jinja2 autoescaping enabled and never render user-controlled template strings; avoid `eval`/`exec`/dynamic `import`.

## Implementation Guidance (SD Elements)

Prevent SSTI using the following techniques:
 
- Use a safe Template engine that only allows white-list functions and are syntax safe.
- Use the validation functions of the Template engine if it provides them.
- Sandbox your Template engine inside a locked down container so that arbitrary code executes inside the container.
- Create a safe environment by hardening the kernel and using read-only file systems. 
- Perform server-side input validation and sanitization.
- Allowlist acceptable user input. For example, if the data is a string, allowlist the characters that are not control characters of the Template engine. Refer to [Countermeasure 31](/library/tasks/T31/) for more information about input validation.

## Success Criteria

- The control "Prevent Server-Side Template Injection (SSTI)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
