---
name: t305-verify-that-your-application-dynamically-loads-code-only-fr
description: Use the following guidelines to verify that an application only loads code dynamically from secure locations: - Work with developers, or use automatic code scanning tools, to find instances of dynamic loading of any code in the application.
---

# T305: Verify that your application dynamically loads code only from secure locations

**Category:** CODE_FIX  
**SD Elements:** [T305](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T305/)  
**Priority:** 8  
**Domain:** injection

## Affected Areas in This Repository

auth.py (sqlite3 string-concatenated queries, e.g. login L97, check_balance L132, transfer L158-166), app.py (psycopg2 queries built via f-strings/`%`), transaction_graphql.py (f-string SQL at L46/78/106/155), merchant_payments.py

## Required Fix

Use parameterized queries everywhere: psycopg2 `cursor.execute(sql, params)` with `%s` placeholders and sqlite3 with `?` placeholders. Never interpolate user input into SQL/template/command strings. For template injection, keep Jinja2 autoescaping enabled and never render user-controlled template strings; avoid `eval`/`exec`/dynamic `import`.

## Implementation Guidance (SD Elements)

Use the following guidelines to verify that an application only loads code dynamically from secure locations:

- Work with developers, or use automatic code scanning tools, to find instances of dynamic loading of any code in the application.

- Verify that you do not load code from unverified resources.

- Verify that code is not loaded from shared locations and is not loaded through unencrypted networks.
    - For example, any external storage.

- If you have to load a class from an external location, make sure the class is signed and the application validates the signature before loading the class.

## Success Criteria

- The control "Verify that your application dynamically loads code only from secure locations" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
