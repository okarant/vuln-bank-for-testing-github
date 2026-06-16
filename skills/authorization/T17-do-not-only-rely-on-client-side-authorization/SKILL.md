---
name: t17-do-not-only-rely-on-client-side-authorization
description: Do not only rely on client-side code to authorize users, such as a JavaScript library, because users can bypass client-side security controls. Authorization checks on a user should be done on the server itself, or users can forcibly browse 
---

# T17: Do not only rely on client-side authorization

**Category:** CODE_FIX  
**SD Elements:** [T17](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T17/)  
**Priority:** 8  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Do not only rely on client-side code to authorize users, such as a JavaScript library, because users can bypass client-side security controls.

Authorization checks on a user should be done on the server itself, or users can forcibly browse or guess the URL of a page that normally requires authorization.

## Success Criteria

- The control "Do not only rely on client-side authorization" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
