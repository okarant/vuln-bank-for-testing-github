---
name: t2140-test-that-apis-do-not-expose-sensitive-information
description: Test that only legitimate data is exposed through APIs. In particular, ensure that responses from APIs match your customers' needs and there is no excessive information in the response. Review if APIs return any sensitive data and [PII](/li
---

# T2140: Test that APIs do not expose sensitive information

**Category:** CODE_FIX  
**SD Elements:** [T2140](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2140/)  
**Priority:** 7  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Test that only legitimate data is exposed through APIs. 

In particular, ensure that responses from APIs match your customers' needs and there is no excessive information in the response. Review if APIs return any sensitive data and [PII](/library/glossary/G8/), and make sure these responses do not pose any security risk.

## Success Criteria

- The control "Test that APIs do not expose sensitive information" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
