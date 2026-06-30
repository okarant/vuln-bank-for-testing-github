---
name: ct435-bind-variables-in-sql-statements-oleg-test
description: - **Bind variables and avoid dynamic concatenation:** Ensure that you always bind variables correctly and never dynamically concatenate SQL statements with untrusted data. - **Use parameterized queries:** Pass untrusted values as bound para
---

# CT435: Bind variables in SQL statements - Oleg Test

**Category:** CODE_FIX  
**SD Elements:** [CT435](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-CT435/)  
**Priority:** 10  
**Domain:** injection

## Affected Areas in This Repository

auth.py (sqlite3 string-concatenated queries, e.g. login L97, check_balance L132, transfer L158-166), app.py (psycopg2 queries built via f-strings/`%`), transaction_graphql.py (f-string SQL at L46/78/106/155), merchant_payments.py

## Required Fix

Use parameterized queries everywhere: psycopg2 `cursor.execute(sql, params)` with `%s` placeholders and sqlite3 with `?` placeholders. Never interpolate user input into SQL/template/command strings. For template injection, keep Jinja2 autoescaping enabled and never render user-controlled template strings; avoid `eval`/`exec`/dynamic `import`.

## Implementation Guidance (SD Elements)

- **Bind variables and avoid dynamic concatenation:** Ensure that you always bind variables correctly and never dynamically concatenate SQL statements with untrusted data.
  - **Use parameterized queries:** Pass untrusted values as bound parameters, never via string concatenation, formatting, or template expansion.
  - **Avoid dynamic SQL construction with untrusted data:** Prohibit building SQL with untrusted input in query strings, including query fragments, filters, and predicates.
  - **Use ORM/query APIs safely:** Prefer ORM or query-builder methods that generate parameterized SQL and avoid raw SQL entry points.


- **Evaluate frameworks and ORMs for safe binding:** Investigate whether a new persistence framework, programming language, or Object-Relationship Manager (ORM) binds variables, and determine if they explicitly protect against SQL injection.
  - **Verify binding behavior:** Confirm that the framework always uses bound parameters for its standard query APIs and never interpolates values into SQL text.
  - **Restrict to safe APIs:** Use only the framework’s APIs that preserve parameterization and avoid raw SQL helpers unless you manually bind parameters.
  - **Document safe patterns:** Define and enforce approved data-access patterns that keep SQL structure separate from data.


- **Use stored procedures with bound parameters:** Use database-stored procedures for binding variables.
  - **Bind procedure parameters:** Call stored procedures with bound parameters, not by concatenating arguments into `CALL` or execution strings.
  - **Avoid unsafe dynamic SQL inside procedures:** Ensure any dynamic SQL inside procedures does not concatenate untrusted input and instead uses the database’s parameterization mechanisms.
  - **Treat procedure calls as data access layer:** Centralize complex data operations in procedures that always receive untrusted input as parameters.


- **Sanitize input when binding is not possible:** Whenever binding variables is not possible, sanitize input to prevent SQL injection.
  - **Use strict whitelisting:** Implement validation that only allows expected characters and formats (for example, alphanumeric and underscore for identifiers, numeric-only for IDs).
  - **Whitelist identifiers:** Maintain explicit allow-lists for dynamic structural elements such as table names, column names, and sort directions.
  - **Fail closed on invalid input:** Reject or error on any input that does not match the strict whitelist before constructing SQL.


- **Validate and constrain all untrusted input:** Apply server-side validation to every untrusted value that influences SQL behavior.
  - Enforce type conversion (for example, to integers or booleans) and reject values that cannot be safely converted.
  - Normalize and constrain free-form inputs (such as search terms) to safe length and character sets before passing them to parameterized queries.


**CWE Reference:** [CWE-89](https://cwe.mitre.org/data/definitions/89.html)


> See How-To for Python code examples


---


## Solution

1. **Identify:** Locate all SQL construction paths where untrusted input appears in query strings or raw SQL helpers.

2. **Implement:**
   - Apply **parameterized queries** (recommended) or **ORM/query APIs** that generate parameterized SQL.
   - Add **identifier whitelisting** when using dynamic table names, column names, or sort directions.
   - Apply **sanitize input to prevent SQL injection** when parameter binding is not possible for specific elements.

3. **Verify:** Execute queries with injection-style payloads (for example, `"' OR 1=1--"`) and confirm they do not alter the logical result set or query structure.


## Acceptance criteria

- Attack test confirms safe result for your chosen approach.
- Identifier whitelisting: reject unknown or malformed columns, tables, and sort directions.

## Success Criteria

- The control "Bind variables in SQL statements - Oleg Test" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
