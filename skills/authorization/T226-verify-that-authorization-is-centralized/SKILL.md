---
name: t226-verify-that-authorization-is-centralized
description: Improve access control by centralizing all authorization decisions: 1. **Review the source code for authorization decisions**: Examine the source code to identify where authorization decisions are made. For example, when a user accesses an 
---

# T226: Verify that authorization is centralized

**Category:** CODE_FIX  
**SD Elements:** [T226](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T226/)  
**Priority:** 9  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Improve access control by centralizing all authorization decisions:

1. **Review the source code for authorization decisions**: Examine the source code to identify where authorization decisions are made. For example, when a user accesses an account balances page in a banking web application, check how the application determines whether the user is allowed to access the bank balance.
   - Code Sample: `app.checkAuthorization(user, function)` or `app.userHasPermission(user, permission)`.

2. **Ensure authorization checks are centralized**: Verify that the authorization checks call a central module or use a central Access Management system. This ensures that all authorization decisions are made consistently.
   - Code Sample: Avoid checks like `if (user.name == 'Bob') then do_privileged_function` as they are not centralized and can lead to security vulnerabilities.

__Note__: These verification countermeasures require familiarity with source code structure and the manual review of a significant portion of the presentation layer source code.

## Success Criteria

- The control "Verify that authorization is centralized" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
