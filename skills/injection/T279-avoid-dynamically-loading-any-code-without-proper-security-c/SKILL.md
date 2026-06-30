---
name: t279-avoid-dynamically-loading-any-code-without-proper-security
description: While dynamic loading of code is possible in some programming languages and frameworks like Java and Android, it is recommended that you avoid this capability as it increases the code complexity and makes your application dependent on an ex
---

# T279: Avoid dynamically loading any code without proper security considerations

**Category:** CODE_FIX  
**SD Elements:** [T279](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T279/)  
**Priority:** 8  
**Domain:** injection

## Affected Areas in This Repository

auth.py (sqlite3 string-concatenated queries, e.g. login L97, check_balance L132, transfer L158-166), app.py (psycopg2 queries built via f-strings/`%`), transaction_graphql.py (f-string SQL at L46/78/106/155), merchant_payments.py

## Required Fix

Use parameterized queries everywhere: psycopg2 `cursor.execute(sql, params)` with `%s` placeholders and sqlite3 with `?` placeholders. Never interpolate user input into SQL/template/command strings. For template injection, keep Jinja2 autoescaping enabled and never render user-controlled template strings; avoid `eval`/`exec`/dynamic `import`.

## Implementation Guidance (SD Elements)

While dynamic loading of code is possible in some programming languages and frameworks like Java and Android, it is recommended that you avoid this capability as it increases the code complexity and makes your application dependent on an external resource. However, If you have to load any module dynamically, consider the following recommendations:

- Avoid loading modules from shared locations, such as from an external storage.

- Avoid loading modules through unencrypted networks. Otherwise, files in transit would be at risk of manipulation.

- If you have to load a class from an external location, generate a signature of the class (binary) and check the signature before loading the class to verify that the integrity of the class is maintained.

## Success Criteria

- The control "Avoid dynamically loading any code without proper security considerations" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
