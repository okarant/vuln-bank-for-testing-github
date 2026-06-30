---
name: t373-design-and-regulate-access-to-unauthenticated-parts-of-the
description: Follow these guidelines to identify, specify and regulate access to unauthenticated parts of the application (an unauthenticated, or authentication-free, part of an application consists of all the resources in the application, such as pages
---

# T373: Design and regulate access to unauthenticated parts of the application

**Category:** CODE_FIX  
**SD Elements:** [T373](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T373/)  
**Priority:** 8  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Follow these guidelines to identify, specify and regulate access to unauthenticated parts of the application (an unauthenticated, or authentication-free, part of an application consists of all the resources in the application, such as pages and services for which authentication is not necessary):

- Create a white-list of services, pages, and directories that are accessible to the public.

- Make sure that the items on the list are clearly specified as this list will be used later for authentication and authorization purposes.

- Consider using light-weight technologies for those parts.
    - For example, simple HTML pages.

- Consider moving the non-authenticated parts of the application to another server (which may be subject to denial of service attacks, and usually receive a higher number of requests).
    - This may involve changes to the design of the application.

## Success Criteria

- The control "Design and regulate access to unauthenticated parts of the application" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
