---
name: t128-test-for-access-control-bypass-through-user-controlled-keys
description: Follow these guidelines to test for access control bypass through user-provided keys: - Inspect the application for areas where user-specific information is accessed based on input from that user. - For example, when account balances can be
---

# T128: Test for access control bypass through user-controlled keys

**Category:** CODE_FIX  
**SD Elements:** [T128](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T128/)  
**Priority:** 8  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Follow these guidelines to test for access control bypass through user-provided keys:

- Inspect the application for areas where user-specific information is accessed based on input from that user.
    - For example, when account balances can be accessed by an HTTP-post parameter.

- Change the key and check if the data objects are accessible.
    - For web applications, you can use an HTTP-proxy tool to modify the input, and then attempt to access another user's data.

This test __fails__ if you are able to view a different user's data where normally you wouldn't be able to due to the lack of sufficient permissions.

## Success Criteria

- The control "Test for access control bypass through user-controlled keys" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
