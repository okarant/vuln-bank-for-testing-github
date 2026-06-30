---
name: t26-expire-sessions-on-logout
description: Use the following guidelines for expiring sessions: - Expire a session when a user logs out to prevent old sessions from being accessed by others on shared machines or devices. - Additionally, terminate any process associated with the user'
---

# T26: Expire sessions on logout

**Category:** CODE_FIX  
**SD Elements:** [T26](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T26/)  
**Priority:** 6  
**Domain:** session-management

## Affected Areas in This Repository

auth.py (JWT accepted from header/args/form/cookies), static/dashboard.js (JWT in localStorage)

## Required Fix

Issue unique session identifiers, set `Secure`/`HttpOnly`/`SameSite` on session cookies, expire/invalidate sessions on logout, and never place tokens/session IDs in URLs.

## Implementation Guidance (SD Elements)

Use the following guidelines for expiring sessions:

- Expire a session when a user logs out to prevent old sessions from being accessed by others on shared machines or devices.

- Additionally, terminate any process associated with the user's session unless it is designed to continue after the session is terminated.

- If a user has not explicitly logged out previously to end a session (such as by using a logout button), provide them with a reminder to do so when they next log in.

- If the user is unable to log out, or the logout function does not terminate the session completely, data may continue to be collected (such as tracking sites the user visits elsewhere).

## Success Criteria

- The control "Expire sessions on logout" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
