---
name: t169-test-that-the-site-is-not-vulnerable-to-dom-based-xss
description: To test for DOM-based XSS, inspect all the JavaScript content, either inside .js files, or embedded inside HTML files (script tags, event handlers, and so on). Look for and identify user-controlled values (also known as "Sources"), and look
---

# T169: Test that the site is not vulnerable to DOM-based XSS

**Category:** CODE_FIX  
**SD Elements:** [T169](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T169/)  
**Priority:** 8  
**Domain:** xss

## Affected Areas in This Repository

templates/*.html (Jinja2), static/dashboard.js and static/merchant.js (client-side DOM rendering)

## Required Fix

Keep Jinja2 autoescaping enabled and contextually escape all untrusted output; avoid `innerHTML`/unsafe DOM sinks in JS; send a Content-Security-Policy and `X-Frame-Options: DENY` (or CSP frame-ancestors) to block injection and clickjacking.

## Implementation Guidance (SD Elements)

To test for DOM-based XSS, inspect all the JavaScript content, either inside .js files, or embedded inside HTML files (script tags, event handlers, and so on). Look for and identify user-controlled values (also known as "Sources"), and look for places that can render the values/functions (also known as "Sinks").
 
The most commonly known Sources are:
 
    document.URL
    document.URLUnencoded
    document.location (and many of its properties)
    document.referrer
    window.location (and many of its properties)
    location (window.location can be accessed as just location)
 
The commonly used Sinks are:
 
    element.innerHTML = "...";
    element.outerHTML = "...";
    document.write(...);
    document.writeln(...);
 
If the value of a Source variable is directly used for output generation using a Sink method without explicit validation/sanitation of the content, then this test __fails__ and the web site is vulnerable to DOM-based XSS. 

For example, the following code would fail:
 
    document.writeln(document.referrer)
 
**Note**: We recommend performing this test by inspecting the JavaScript source, which is always available, rather than executing runtime tests. Inspecting the source is more reliable.

## Success Criteria

- The control "Test that the site is not vulnerable to DOM-based XSS" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
