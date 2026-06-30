---
name: t420-prevent-client-side-template-injection-csti
description: Prevent client side Template injection using the following instructions: - Validate users' inputs if your Template dynamically embeds user input into a page. Refer to [Countermeasure 31](/library/tasks/T31) for more information about input 
---

# T420: Prevent Client-Side Template Injection (CSTI)

**Category:** CODE_FIX  
**SD Elements:** [T420](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T420/)  
**Priority:** 6  
**Domain:** injection

## Affected Areas in This Repository

auth.py (sqlite3 string-concatenated queries, e.g. login L97, check_balance L132, transfer L158-166), app.py (psycopg2 queries built via f-strings/`%`), transaction_graphql.py (f-string SQL at L46/78/106/155), merchant_payments.py

## Required Fix

Use parameterized queries everywhere: psycopg2 `cursor.execute(sql, params)` with `%s` placeholders and sqlite3 with `?` placeholders. Never interpolate user input into SQL/template/command strings. For template injection, keep Jinja2 autoescaping enabled and never render user-controlled template strings; avoid `eval`/`exec`/dynamic `import`.

## Implementation Guidance (SD Elements)

Prevent client side Template injection using the following instructions:

- Validate users' inputs if your Template dynamically embeds user input into a page. Refer to [Countermeasure 31](/library/tasks/T31) for more information about input validation.
- Avoid passing untrusted user input to unsecure functions like `eval`. This can cause improper evaluation and execution of malicious expressions within a browser.
- Do not rely on sandboxes as a security feature since they have limitations and can be bypassed. 
- Avoid mixing any server-side Templates with the client-side ones. Client-side Templates render HTML content in the browser using a JavaScript library.  


For more information, see the documentation on [Template Injection: Client Side](https://vulncat.fortify.com/en/detail?id=desc.dataflow.javascript.client_side_template_injection).

## Success Criteria

- The control "Prevent Client-Side Template Injection (CSTI)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
