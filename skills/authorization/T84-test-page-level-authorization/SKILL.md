---
name: t84-test-page-level-authorization
description: Attempt to browse each unique server page in the authenticated portion of the site **without prior authentication and authorization**. Delete any cookies for cookie-based authentication. This test __fails__ if you can access any of those pa
---

# T84: Test page-level authorization

**Category:** CODE_FIX  
**SD Elements:** [T84](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T84/)  
**Priority:** 6  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Attempt to browse each unique server page in the authenticated portion of the site **without prior authentication and authorization**. Delete any cookies for cookie-based authentication. 

This test __fails__ if you can access any of those pages.

 Try alternative names and access paths for pages, if available. You must only be able to access and see pages that are public or listed in a white-list of authorization-free pages, such as about pages, and help pages.

## Success Criteria

- The control "Test page-level authorization" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
