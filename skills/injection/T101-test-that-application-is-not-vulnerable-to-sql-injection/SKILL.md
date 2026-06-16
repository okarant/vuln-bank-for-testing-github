---
name: t101-test-that-application-is-not-vulnerable-to-sql-injection
description: SQL injection is difficult to assess through runtime testing without an actual exploit. The following test will help you to identify potential SQL injection vectors: 1. For all forms of input, attempt to send malicious SQL injection charact
---

# T101: Test that application is not vulnerable to SQL injection

**Category:** CODE_FIX  
**SD Elements:** [T101](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T101/)  
**Priority:** 10  
**Domain:** injection

## Affected Areas in This Repository

auth.py (sqlite3 string-concatenated queries, e.g. login L97, check_balance L132, transfer L158-166), app.py (psycopg2 queries built via f-strings/`%`), transaction_graphql.py (f-string SQL at L46/78/106/155), merchant_payments.py

## Required Fix

Use parameterized queries everywhere: psycopg2 `cursor.execute(sql, params)` with `%s` placeholders and sqlite3 with `?` placeholders. Never interpolate user input into SQL/template/command strings. For template injection, keep Jinja2 autoescaping enabled and never render user-controlled template strings; avoid `eval`/`exec`/dynamic `import`.

## Implementation Guidance (SD Elements)

SQL injection is difficult to assess through runtime testing without an actual exploit. The following test will help you to identify potential SQL injection vectors: 

1. For all forms of input, attempt to send malicious SQL injection characters and inspect the response.

    This test __fails__ if the response renders a database error.

2. If this test doesn't return an error, try comparing regular input with malicious SQL injection characters. 
    - For example, try `parameter=1`, and then `parameter=1'`. 

    This test __fails__ if the results differ and there is no error message.

## Success Criteria

- The control "Test that application is not vulnerable to SQL injection" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
