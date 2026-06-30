---
name: t184-perform-authorization-checks-on-restful-web-services
description: Consider the following points when performing authorization checks on RESTful web services: - Ensure that the user accessing the web service has sufficient permissions to access the URL and uses the HTTP verb. - For example, a user may have
---

# T184: Perform authorization checks on RESTful web services

**Category:** CODE_FIX  
**SD Elements:** [T184](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T184/)  
**Priority:** 9  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Consider the following points when performing authorization checks on RESTful web services:

- Ensure that the user accessing the web service has sufficient permissions to access the URL and uses the HTTP verb.
    - For example, a user may have access to GET a resource, but may not have permission to DELETE or PUT the same resource.

- Authorize clients for accessing the method in question and provide enough privileges for accessing the requested resources.

- Limit access to administrative and management functions to web service administrators only.

- Use a secure authentication mechanism for authenticating the third parties that access the web services.

## Success Criteria

- The control "Perform authorization checks on RESTful web services" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
