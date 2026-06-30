---
name: t2274-test-to-confirm-that-the-principle-of-least-privilege-is-s
description: Follow these guidelines to confirm that the principle of least privilege is implemented appropriately: - Test to confirm that all privileges are restricted as much as possible. - Test to confirm that all privileges are granted as late as po
---

# T2274: Test to confirm that the principle of least privilege is strongly implemented

**Category:** CODE_FIX  
**SD Elements:** [T2274](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2274/)  
**Priority:** 9  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Follow these guidelines to confirm that the principle of least privilege is implemented appropriately:

- Test to confirm that all privileges are restricted as much as possible.
- Test to confirm that all privileges are granted as late as possible.
- Test to confirm that all privileges are revoked as soon as possible.

## Success Criteria

- The control "Test to confirm that the principle of least privilege is strongly implemented" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
