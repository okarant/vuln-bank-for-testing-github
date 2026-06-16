---
name: t93-test-that-sessions-expire-upon-logout
description: Follow these steps to make sure a browser's user session expires after they log out: 1. Authenticate into the application in your browser. 2. Navigate to pages where you can view non-public information. 3. Log out. 4. Click the back button 
---

# T93: Test that sessions expire upon logout

**Category:** CODE_FIX  
**SD Elements:** [T93](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T93/)  
**Priority:** 6  
**Domain:** session-management

## Affected Areas in This Repository

auth.py (JWT accepted from header/args/form/cookies), static/dashboard.js (JWT in localStorage)

## Required Fix

Issue unique session identifiers, set `Secure`/`HttpOnly`/`SameSite` on session cookies, expire/invalidate sessions on logout, and never place tokens/session IDs in URLs.

## Implementation Guidance (SD Elements)

Follow these steps to make sure a browser's user session expires after they log out:

1. Authenticate into the application in your browser.
2. Navigate to pages where you can view non-public information.
3. Log out.
4. Click the back button or use the address bar to attempt to revisit the non-public pages.

This test __fails__ if you can access the page successfully or see any non-public information.

Follow these steps to make sure that there is a server-side mechanism that keeps track of the status of the sessions:

1. Authenticate into the application in your browser.
2. Visit a non-public page and use a web inspector tool to capture the server response.
3. Store all session cookies.
4. Log out.
5. Use the web inspector, or a cookie editor tool, to craft an HTTP request to access a non-public page and include all stored session cookies captured in step 3.

This test __fails__ if the server responds without error, or reveals any private information.

## Success Criteria

- The control "Test that sessions expire upon logout" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
