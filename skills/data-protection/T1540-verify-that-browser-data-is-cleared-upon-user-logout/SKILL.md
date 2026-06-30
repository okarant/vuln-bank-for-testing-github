---
name: t1540-verify-that-browser-data-is-cleared-upon-user-logout
description: Upon user logout, locally stored data should be cleared from the browser using the `Clear-Site-Data` header. The following steps allow you to verify the correct behavior of the application. 1. Use a browser that [supports](https://developer
---

# T1540: Verify that browser data is cleared upon user logout

**Category:** CODE_FIX  
**SD Elements:** [T1540](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1540/)  
**Priority:** 8  
**Domain:** data-protection

## Affected Areas in This Repository

database.py (virtual_cards.cvv and users.password stored in plaintext; PII in users), static/dashboard.js (JWT in localStorage)

## Required Fix

Encrypt sensitive data at rest, never store card CVV, salt+hash passwords, and avoid keeping long-lived secrets in browser storage.

## Implementation Guidance (SD Elements)

Upon user logout, locally stored data should be cleared from the browser using the `Clear-Site-Data` header.

The following steps allow you to verify the correct behavior of the application.

1. Use a browser that [supports](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Clear-Site-Data) the `Clear-Site-Data` header
2. Use the application in a regular way, causing data to be stored in the browser
    * E.g., log in so that the application sets a cookie
3. Use the browser's developer tools to inspect the locally stored data
4. Logout of the application
5. Use the developer tools to inspect the different storage areas (cookies, Local Storage, Session Storage, ...)

This test __fails__ if sensitive data is still available in the browser after the user has logged out.

## Success Criteria

- The control "Verify that browser data is cleared upon user logout" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
