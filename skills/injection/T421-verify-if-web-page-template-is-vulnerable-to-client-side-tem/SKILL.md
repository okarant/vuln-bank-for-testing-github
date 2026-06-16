---
name: t421-verify-if-web-page-template-is-vulnerable-to-client-side-te
description: To verify whether an application that uses client side template is vulnerable to CSTI, inject an expression that can even bypass sandboxing, if it's being used. Depending on the language, the payload can be different. The following example 
---

# T421: Verify if web page template is vulnerable to client side template injection (CSTI)

**Category:** CODE_FIX  
**SD Elements:** [T421](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T421/)  
**Priority:** 6  
**Domain:** injection

## Affected Areas in This Repository

auth.py (sqlite3 string-concatenated queries, e.g. login L97, check_balance L132, transfer L158-166), app.py (psycopg2 queries built via f-strings/`%`), transaction_graphql.py (f-string SQL at L46/78/106/155), merchant_payments.py

## Required Fix

Use parameterized queries everywhere: psycopg2 `cursor.execute(sql, params)` with `%s` placeholders and sqlite3 with `?` placeholders. Never interpolate user input into SQL/template/command strings. For template injection, keep Jinja2 autoescaping enabled and never render user-controlled template strings; avoid `eval`/`exec`/dynamic `import`.

## Implementation Guidance (SD Elements)

To verify whether an application that uses client side template is vulnerable to CSTI, inject an expression that can even bypass sandboxing, if it's being used. Depending on the language, the payload can be different. The following example is very general and it's just for understanding the concept.

Example:

````
myEval = function(script) { eval('alert ("Hi"+username+)' ); }

````
In the above example, an untrusted user input can pass to unsecure _eval_ function and this test __fails__ if it executes. 

For the details of the exploit and more examples in different JavaScripts frameworks, refer to [Client Side Template Injection Examples](https://code.google.com/archive/p/mustache-security/)

## Success Criteria

- The control "Verify if web page template is vulnerable to client side template injection (CSTI)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
