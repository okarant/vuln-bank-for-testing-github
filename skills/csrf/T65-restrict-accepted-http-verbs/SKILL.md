---
name: t65-restrict-accepted-http-verbs
description: Restrict the HTTP verbs that your application or web server accepts to the ones required, such as GET, POST, and HEAD. For example, if an endpoint never requires processing a POST or DELETE request, configure your web server to reject such 
---

# T65: Restrict accepted HTTP verbs

**Category:** CODE_FIX  
**SD Elements:** [T65](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T65/)  
**Priority:** 6  
**Domain:** csrf

## Affected Areas in This Repository

app.py (state-changing POST routes: /transfer, /request_loan, /update_bio, /admin/*, /api/*)

## Required Fix

Add anti-CSRF tokens to state-changing requests (e.g. Flask-WTF CSRFProtect or a synchronizer token), use `SameSite` cookies, and restrict each route to the correct HTTP methods.

## Implementation Guidance (SD Elements)

Restrict the HTTP verbs that your application or web server accepts to the ones required, such as GET, POST, and HEAD.

For example, if an endpoint never requires processing a POST or DELETE request, configure your web server to reject such requests.

This verb restriction protects endpoints against DoS attacks that use specific HTTP verbs, by minimizing the attack surface.

## Success Criteria

- The control "Restrict accepted HTTP verbs" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
