---
name: t1145-verify-if-web-page-template-is-vulnerable-to-ssti
description: To verify whether your Template is vulnerable to SSTI, in a Template field that accepts user input and returns the input as part of its response, insert an executable payload. For example, suppose a template gets the name from the user and 
---

# T1145: Verify if web page template is vulnerable to SSTI

**Category:** CODE_FIX  
**SD Elements:** [T1145](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1145/)  
**Priority:** 8  
**Domain:** injection

## Affected Areas in This Repository

auth.py (sqlite3 string-concatenated queries, e.g. login L97, check_balance L132, transfer L158-166), app.py (psycopg2 queries built via f-strings/`%`), transaction_graphql.py (f-string SQL at L46/78/106/155), merchant_payments.py

## Required Fix

Use parameterized queries everywhere: psycopg2 `cursor.execute(sql, params)` with `%s` placeholders and sqlite3 with `?` placeholders. Never interpolate user input into SQL/template/command strings. For template injection, keep Jinja2 autoescaping enabled and never render user-controlled template strings; avoid `eval`/`exec`/dynamic `import`.

## Implementation Guidance (SD Elements)

To verify whether your Template is vulnerable to SSTI, in a Template field that accepts user input and returns the input as part of its response, insert an executable payload. For example, suppose a template gets the name from the user and shows a greeting on the page along with the name as below :

````
Hello {name}
````
To verify if the Template is vulnerable, replace `name` with an arbitrary code like `{'5'*5}` . If the Template doesn't perform validation and executes the payload, this test __fails__ . For example, the output of `Hello {{'5'*5}}` in a vulnerable _Twig_ engine would be `Hello 25`, and in _Jinja2_ it would be `Hello 55555` . Therefore, the output can reveal the Template engine because it can be different in different Template engines. 
After finding the Template in use, analyze the Template documentation to find vulnerabilities in syntax, variables, methods, the execution of arbitrary remote code, and so on. 

_Note:_ The syntaxes and payloads you use for testing can be different and depends on the language of the template you are using.


__Note:__ Certain automated detection tools, such as BurpSuite, can help you detect SSTI, but some blackbox security assessments are likely to miss it.

## Success Criteria

- The control "Verify if web page template is vulnerable to SSTI" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
