---
name: t89-test-that-site-is-not-vulnerable-to-xss
description: Use the following guidelines for testing your site for a vulnerability to XSS: 1. Attempt to send a set of known XSS meta-characters for each of the following items: - HTTP parameter name - HTTP parameter value - HTTP header name - HTTP hea
---

# T89: Test that site is not vulnerable to XSS

**Category:** CODE_FIX  
**SD Elements:** [T89](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T89/)  
**Priority:** 8  
**Domain:** xss

## Affected Areas in This Repository

templates/*.html (Jinja2), static/dashboard.js and static/merchant.js (client-side DOM rendering)

## Required Fix

Keep Jinja2 autoescaping enabled and contextually escape all untrusted output; avoid `innerHTML`/unsafe DOM sinks in JS; send a Content-Security-Policy and `X-Frame-Options: DENY` (or CSP frame-ancestors) to block injection and clickjacking.

## Implementation Guidance (SD Elements)

Use the following guidelines for testing your site for a vulnerability to XSS:

1. Attempt to send a set of known XSS meta-characters for each of the following items:
    - HTTP parameter name
    - HTTP parameter value
    - HTTP header name
    - HTTP header value
    - Cookie name
    - Cookie value

2. Inspect the results. 

3. If the results appear to have the same meta-characters without any encoding in the resulting web page, JavaScript file, or Cascading Style Sheet (CSS) file, attempt to include a full script attack, such as: 
    - `<script>alert('xss')</script>`, 
    - `' onmouseover=alert(/XSS/)`, or
    - `javascript:alert('xss')`. 

For more potential vectors, see the [XSS Filter Evasion Cheat Sheet](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet). 

This test __fails__ if you are able to create an on-screen pop-up box.

**Note:** There may be cases where your browser is immune to XSS, but other browsers are vulnerable. Where possible, attempt these attacks with all supported browsers.

## Success Criteria

- The control "Test that site is not vulnerable to XSS" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
