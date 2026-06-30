---
name: t2142-verify-that-function-level-authorization-is-implemented-in
description: Verify the following items to avoid function-level broken authorization: - Test all existing API endpoints for potential authorization flaws. - This test __passes__ if : 1. an __authorization check__ function based on users, groups, and rol
---

# T2142: Verify that function level authorization is implemented in API

**Category:** CODE_FIX  
**SD Elements:** [T2142](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2142/)  
**Priority:** 8  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Verify the following items to avoid function-level broken authorization: 

- Test all existing API endpoints for potential authorization flaws.
- This test __passes__ if :

    1.  an __authorization check__ function based on users, groups, and roles in administrative abstract controller (a base controller for controlling access permissions) has been implemented.

    2. an administrative controller __inherits__ administrative abstract controller.

    3. an __authorization check__ function has been implemented for administrative functions in regular controller.

    4.  all access is denied by default with: `.anyRequest().denyAll()` and requests with `.hasRole` are explicitly allowed.

## Success Criteria

- The control "Verify that function level authorization is implemented in API" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
