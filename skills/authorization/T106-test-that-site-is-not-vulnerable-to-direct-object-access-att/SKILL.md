---
name: t106-test-that-site-is-not-vulnerable-to-direct-object-access-at
description: Use the following guidelines to test whether your site is vulnerable to direct object access attacks: 1. Look for all parts of the web application that provide access to files on the application or on other servers, excluding static files n
---

# T106: Test that site is not vulnerable to direct object access attacks

**Category:** CODE_FIX  
**SD Elements:** [T106](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T106/)  
**Priority:** 8  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Use the following guidelines to test whether your site is vulnerable to direct object access attacks:

1. Look for all parts of the web application that provide access to files on the application or on other servers, excluding static files normally served by a web server.
    - This includes HTML, JavaScript, and Cascading Style Sheets.

2. For each part of the application, inspect the mechanism that specifies the file name. 
    - For example, the file name is specified as an HTTP parameter. 

3. Once you've identified the mechanism, use an HTTP-proxy tool to try to change the values to files that you are not allowed to have access to.
    - For example, change `account158.pdf` to `account186.pdf`, or `../../../WEB-INF/web.xml`. 

This test __fails__ if you can access a file that you are not authorized to.

## Success Criteria

- The control "Test that site is not vulnerable to direct object access attacks" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
