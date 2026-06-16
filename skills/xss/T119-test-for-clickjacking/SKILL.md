---
name: t119-test-for-clickjacking
description: Before you start, determine your supported browsers and test domains (pages with important functions that are enabled by clicking and therefore need to be tested). Two types of tests are suggested here: - **Type One** is based on the verifi
---

# T119: Test for clickjacking

**Category:** CODE_FIX  
**SD Elements:** [T119](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T119/)  
**Priority:** 7  
**Domain:** xss

## Affected Areas in This Repository

templates/*.html (Jinja2), static/dashboard.js and static/merchant.js (client-side DOM rendering)

## Required Fix

Keep Jinja2 autoescaping enabled and contextually escape all untrusted output; avoid `innerHTML`/unsafe DOM sinks in JS; send a Content-Security-Policy and `X-Frame-Options: DENY` (or CSP frame-ancestors) to block injection and clickjacking.

## Implementation Guidance (SD Elements)

Before you start, determine your supported browsers and test domains (pages with important functions that are enabled by clicking and therefore need to be tested).

Two types of tests are suggested here:

- **Type One** is based on the verification of headers that may only work for browsers that support those headers.
    - Older browsers may be vulnerable despite passing the test.

- **Type Two** needs more resourceful testers and looks at the behavior of the application. 

You can choose to perform the Type One test or both.

## Type One: Verification of Headers

- Verify that all the web pages with important actions are set to one of the following:
    - X-Frame-Options: DENY
    - X-Frame-Options: SAMEORIGIN
    ___or___
    - X-Frame-Options: ALLOW-FROM https://yoursite.com/

- Verify that the pages include at least one of the three Content Security Policy (CSP) settings:

    - Content-Security-Policy: frame-ancestors 'none'
    - Content-Security-Policy: frame-ancestors 'self'
      ___or___
    - Content-Security-Policy: frame-ancestorshttps://yoursite.com/

To validate these in Chrome: 

1. Go to View > Developer > Developer Tools.
2. Select the __Network tab__ in the tools header. 
3. Navigate to the page you want to test. 
4. Under __Name__ in Developer Tools, select the base web page (and optionally, Type of Document). 
5. Select the __Headers__ tab
6. Find the the Content Security Policy and X-Frame-Options settings in the Response Headers. 

Confirm how the headers are set with your developers. If they are set by the web server for every page, then validate them on a few pages at random. If they are being set through the web application's software, then you will need to confirm that they are being set on every page.

## Type Two: Testing JavaScript Frame-busting

Three How-tos are provided for this test. Use the three types of templates and replace "target.html" with the address of the page you are testing. 

For each page and for each browser that is supported, follow these steps:

1. Test that the frame-busting technique used by the page is robust and cannot be bypassed by __JavaScript__ code.
    - Use the template provided in the How-to for this countermeasure and replace the `target.html` in the templates with the address of the page that you are testing.
    - Try to open the HTML test template. 

    This test __fails__ if the page that you are testing loads inside the iFrame.

2. Check that your page is not vulnerable to __double framing attacks__.
    - Use the provided template.

    This test __fails__ if the page loads inside an iFrame.

3. Check that the __anti-XSS capabilities__ of the browser cannot be used to disable frame-busting techniques.
    - Use the provided template.

    This test __fails__ if the page loads inside an iFrame.


This test __only passes__ if all three tests pass for each combination of page and browser.

## Success Criteria

- The control "Test for clickjacking" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
