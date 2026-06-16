---
name: t94-test-that-session-ids-are-not-leaked-through-urls
description: Use the following guidelines to test for session IDs leaking through URLs: 1. This test __fails__ if you notice the session ID in the URL at any point in the application. 2. Using a cookie editor, take note of the session ID. - Using a diff
---

# T94: Test that session IDs are not leaked through URLs

**Category:** CODE_FIX  
**SD Elements:** [T94](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T94/)  
**Priority:** 6  
**Domain:** session-management

## Affected Areas in This Repository

auth.py (JWT accepted from header/args/form/cookies), static/dashboard.js (JWT in localStorage)

## Required Fix

Issue unique session identifiers, set `Secure`/`HttpOnly`/`SameSite` on session cookies, expire/invalidate sessions on logout, and never place tokens/session IDs in URLs.

## Implementation Guidance (SD Elements)

Use the following guidelines to test for session IDs leaking through URLs:

1. This test __fails__ if you notice the session ID in the URL at any point in the application.

2. Using a cookie editor, take note of the session ID.
    - Using a different browser or computer, attempt to navigate to an authenticated page with the session ID in the URL. 
    - For example: `http://www.example.com/page;jsessionid=12345678914?param1=val`. 
    
    This test __fails__ if you are able to access the page successfully.

## Success Criteria

- The control "Test that session IDs are not leaked through URLs" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
