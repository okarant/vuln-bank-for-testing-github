---
name: t85-test-server-side-enforcement-of-authorization
description: Use the following guidelines for testing authorization for any page or function that appears to enforce an authorization check: 1. Attempt to browse to a page you do not have access to. 2. Use an HTTP-proxy tool to modify the request sent t
---

# T85: Test server-side enforcement of authorization

**Category:** CODE_FIX  
**SD Elements:** [T85](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T85/)  
**Priority:** 8  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Use the following guidelines for testing authorization for any page or function that appears to enforce an authorization check:

1. Attempt to browse to a page you do not have access to.

2. Use an HTTP-proxy tool to modify the request sent to the unauthorized page.

This test __fails__ if you are able to successfully view the page.

## Success Criteria

- The control "Test server-side enforcement of authorization" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
