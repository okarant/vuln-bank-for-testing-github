---
name: t27-turn-off-session-rewriting
description: Do not allow session rewriting on the application. Application servers might include session IDs in their URLs if the user's browser does not support session cookies. These URLs can cause the following weaknesses: - Leak session IDs to exte
---

# T27: Turn off session rewriting

**Category:** CODE_FIX  
**SD Elements:** [T27](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T27/)  
**Priority:** 6  
**Domain:** session-management

## Affected Areas in This Repository

auth.py (JWT accepted from header/args/form/cookies), static/dashboard.js (JWT in localStorage)

## Required Fix

Issue unique session identifiers, set `Secure`/`HttpOnly`/`SameSite` on session cookies, expire/invalidate sessions on logout, and never place tokens/session IDs in URLs.

## Implementation Guidance (SD Elements)

Do not allow session rewriting on the application.

Application servers might include session IDs in their URLs if the user's browser does not support session cookies. These URLs can cause the following weaknesses:

- Leak session IDs to external sites through hyperlinks.
- Lead to attacks such as session fixation.
- Leave the session ID in logs, such as the user's browsing history.

## Success Criteria

- The control "Turn off session rewriting" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
