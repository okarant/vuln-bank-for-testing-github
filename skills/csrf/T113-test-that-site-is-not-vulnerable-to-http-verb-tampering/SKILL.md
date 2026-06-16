---
name: t113-test-that-site-is-not-vulnerable-to-http-verb-tampering
description: Use the following guidelines to test that your site is not vulnerable to HTTP verb tampering: 1. Using an HTTP-proxy tool, attempt to browse to an authenticated web page without a valid session. 2. Modify the HTTP verb from "GET" or "POST" 
---

# T113: Test that site is not vulnerable to HTTP verb tampering

**Category:** CODE_FIX  
**SD Elements:** [T113](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T113/)  
**Priority:** 6  
**Domain:** csrf

## Affected Areas in This Repository

app.py (state-changing POST routes: /transfer, /request_loan, /update_bio, /admin/*, /api/*)

## Required Fix

Add anti-CSRF tokens to state-changing requests (e.g. Flask-WTF CSRFProtect or a synchronizer token), use `SameSite` cookies, and restrict each route to the correct HTTP methods.

## Implementation Guidance (SD Elements)

Use the following guidelines to test that your site is not vulnerable to HTTP verb tampering:

1. Using an HTTP-proxy tool, attempt to browse to an authenticated web page without a valid session.

2. Modify the HTTP verb from "GET" or "POST" to a random set of characters, such as "PWRLWA." 

    This test __fails__ if you can view the page with the random verb, but are unable to view the page with a valid HTTP verb.

3. You can also try using the "HEAD" request instead of "GET." 
    - You are unlikely to receive a response. 
    - Try to ascertain if the request was processed successfully, by viewing the transaction history for example.

    This test __fails__ if the "HEAD" request works, but the "GET" request does not.

## Success Criteria

- The control "Test that site is not vulnerable to HTTP verb tampering" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
