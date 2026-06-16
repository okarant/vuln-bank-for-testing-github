---
name: t38-bind-variables-in-sql-statements
description: Use the following guidelines for binding variables in SQL statements: - Ensure that you always bind variables correctly and never dynamically concatenate SQL statements with untrusted data. - Most persistence frameworks provide a feature to
---

# T38: Bind variables in SQL statements

**Category:** CODE_FIX  
**SD Elements:** [T38](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T38/)  
**Priority:** 10  
**Domain:** injection

## Affected Areas in This Repository

auth.py (sqlite3 string-concatenated queries, e.g. login L97, check_balance L132, transfer L158-166), app.py (psycopg2 queries built via f-strings/`%`), transaction_graphql.py (f-string SQL at L46/78/106/155), merchant_payments.py

## Required Fix

Use parameterized queries everywhere: psycopg2 `cursor.execute(sql, params)` with `%s` placeholders and sqlite3 with `?` placeholders. Never interpolate user input into SQL/template/command strings. For template injection, keep Jinja2 autoescaping enabled and never render user-controlled template strings; avoid `eval`/`exec`/dynamic `import`.

## Implementation Guidance (SD Elements)

Use the following guidelines for binding variables in SQL statements:

- Ensure that you always bind variables correctly and never dynamically concatenate SQL statements with untrusted data.
    - Most persistence frameworks provide a feature to bind runtime variables with pre-generated SQL statements.
    - Generally, these bind functions automatically escape special SQL characters and effectively mitigate SQL injection.

- Investigate whether a new persistence framework, programming language, or Object-Relationship Manager (ORM) binds variables, and determine if they explicitly protect against SQL injection.
    - In rare cases, researchers have found that persistence frameworks do not properly escape bound variables and may still be vulnerable to SQL injection.

- Use database-stored procedures for binding variables.
    - Many databases allow you to dynamically create and execute an SQL statement within the stored procedure.
    - This approach may be vulnerable to SQL injection as well.

__Note:__ Whenever binding variables is not possible, sanitize input to prevent SQL injection.

**In addition:**

- Where applicable, use **allow-list input validation** (e.g. conditionals so only predefined values reach the SQL layer) to prevent user input from introducing commands.
- Restrict **permissions of the account that executes stored procedures** to the minimum required; avoid granting excessive privileges so that compromise of that user is contained.

## Success Criteria

- The control "Bind variables in SQL statements" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
