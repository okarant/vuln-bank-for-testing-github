---
name: t15-centralize-authorization
description: Use the following guidelines for centralizing authorization: - Centralize authorization into a __single module, layer, or location__. - All views, application programming interfaces (APIs), and other interfaces should pass through the same 
---

# T15: Centralize authorization

**Category:** CODE_FIX  
**SD Elements:** [T15](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T15/)  
**Priority:** 9  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Use the following guidelines for centralizing authorization:

- Centralize authorization into a __single module, layer, or location__.
    - All views, application programming interfaces (APIs), and other interfaces should pass through the same security code to ensure authorization is consistent.

- Avoid hard-coding authorization logic into the presentation layers, especially for web applications.
    - This makes authorization maintenance more complex and inconsistent because it leads to a risk of duplicating authorization features.
    - In certain conditions, attackers can exploit these inconsistencies and bypass authorization checks entirely.

## Success Criteria

- The control "Centralize authorization" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
