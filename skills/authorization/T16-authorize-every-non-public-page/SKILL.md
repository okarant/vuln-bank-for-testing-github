---
name: t16-authorize-every-non-public-page
description: Use an explicit authorization check on every non-public server page. To ensure that only authorized users can access non-public pages, create a white-list of all public pages that do not require authorization, such as about pages, and help 
---

# T16: Authorize every non-public page

**Category:** CODE_FIX  
**SD Elements:** [T16](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T16/)  
**Priority:** 6  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Use an explicit authorization check on every non-public server page.

To ensure that only authorized users can access non-public pages, create a white-list of all public pages that do not require authorization, such as about pages, and help pages.

Additionally, include the authorization code or directives in all the other pages.

Make sure there are no less secure or alternative access paths to those pages.

## Success Criteria

- The control "Authorize every non-public page" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
