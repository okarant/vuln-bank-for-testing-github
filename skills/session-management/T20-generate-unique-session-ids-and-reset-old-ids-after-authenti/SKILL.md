---
name: t20-generate-unique-session-ids-and-reset-old-ids-after-authenti
description: Protect against session-fixation attacks by using the following guidelines: - Generate a unique and random session identifier for each session. - Recognize only system-generated session IDs. - Regenerate the session ID after a user is succe
---

# T20: Generate unique session IDs and reset old IDs after authentication

**Category:** CODE_FIX  
**SD Elements:** [T20](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T20/)  
**Priority:** 9  
**Domain:** session-management

## Affected Areas in This Repository

auth.py (JWT accepted from header/args/form/cookies), static/dashboard.js (JWT in localStorage)

## Required Fix

Issue unique session identifiers, set `Secure`/`HttpOnly`/`SameSite` on session cookies, expire/invalidate sessions on logout, and never place tokens/session IDs in URLs.

## Implementation Guidance (SD Elements)

Protect against session-fixation attacks by using the following guidelines:

  - Generate a unique and random session identifier for each session.
  - Recognize only system-generated session IDs.
  - Regenerate the session ID after a user is successfully authenticated.
  - Regenerate the session ID after any changes to user's privilege level.
  - Copy the server-side state of a user's old session to the new session after changing the session ID.

## Success Criteria

- The control "Generate unique session IDs and reset old IDs after authentication" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
