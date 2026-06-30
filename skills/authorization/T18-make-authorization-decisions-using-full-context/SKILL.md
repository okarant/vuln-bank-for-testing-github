---
name: t18-make-authorization-decisions-using-full-context
description: Authorization decisions must be made using full security context: - Software architecture partitioned into separate layers or tiers must propagate enough contextual data so that the dependent layer can make a correct security decision. - Fo
---

# T18: Make authorization decisions using full context

**Category:** CODE_FIX  
**SD Elements:** [T18](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T18/)  
**Priority:** 9  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Authorization decisions must be made using full security context:

- Software architecture partitioned into separate layers or tiers must propagate enough contextual data so that the dependent layer can make a correct security decision.
    - For example, a web application that decouples view logic from model logic may need to access the end user's permissions so that it can make authorization decisions.
    - In this case, ensure that the model can access a user's permission data.

- In a multi-tiered enterprise application, a web service on a separate server may need contextual data about the end user to make authorization decisions.

## Success Criteria

- The control "Make authorization decisions using full context" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
