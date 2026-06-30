---
name: t122-test-for-remote-file-include
description: Major web servers such as IIS, Apache, Nginx, and Lighttpd evaluate Server Side Includes (SSI) directives while serving the page. Use the following test to determine whether injecting SSI into web pages is possible: 1. Identify the page tha
---

# T122: Test for remote file include

**Category:** CODE_FIX  
**SD Elements:** [T122](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T122/)  
**Priority:** 10  
**Domain:** injection

## Affected Areas in This Repository

auth.py (sqlite3 string-concatenated queries, e.g. login L97, check_balance L132, transfer L158-166), app.py (psycopg2 queries built via f-strings/`%`), transaction_graphql.py (f-string SQL at L46/78/106/155), merchant_payments.py

## Required Fix

Use parameterized queries everywhere: psycopg2 `cursor.execute(sql, params)` with `%s` placeholders and sqlite3 with `?` placeholders. Never interpolate user input into SQL/template/command strings. For template injection, keep Jinja2 autoescaping enabled and never render user-controlled template strings; avoid `eval`/`exec`/dynamic `import`.

## Implementation Guidance (SD Elements)

Major web servers such as IIS, Apache, Nginx, and Lighttpd evaluate Server Side Includes (SSI) directives while serving the page.

Use the following test to determine whether injecting SSI into web pages is possible: 

1. Identify the page that you want to test for SSI directives injection.
    - The page must take user input in the form of cookie content, text input field, query string, or HTTP headers and respond accordingly.

2. Create an SSI directive in the form of `<!--#directive parameter=value parameter=value -->`.
    - For example: 
        `<!--#include virtual="/link/to/myfile.txt" -->` includes the content of `myfile.txt` in a served HTML file.

3. Put `myfile.txt` on a location that is accessible by your server. Get a link or path to the file.
4. Navigate to the pages that you identified in step 1.
5. Choose a set of parameters or input fields to test.
6. For each parameter or input field from step 5, submit the crafted SSI directive from step 2.

This test __fails__ if the page renders content from `myfile.txt` in step 2.

Try other SSI directives that are supported by your server. For instance, if `#exec` or `#echo` are supported, test if they are adequately neutralized.

## Success Criteria

- The control "Test for remote file include" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
