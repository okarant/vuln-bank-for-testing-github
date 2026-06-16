---
name: t2282-test-to-confirm-that-unauthenticated-parts-of-the-applicat
description: __ Try to access unauthenticated parts of the application.__ This test __fails__ if unauthenticated parts of the application or any pages and services that do not need authentication are not accessible.
---

# T2282: Test to confirm that unauthenticated parts of the application are accessible

**Category:** CODE_FIX  
**SD Elements:** [T2282](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2282/)  
**Priority:** 8  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

__ Try to access unauthenticated parts of the application.__ This test __fails__ if unauthenticated parts of the application or any pages and services that do not need authentication are not accessible.

## Success Criteria

- The control "Test to confirm that unauthenticated parts of the application are accessible" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
