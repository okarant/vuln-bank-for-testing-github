---
name: t554-verify-that-rest-web-services-are-securely-designed
description: Verify that the following security requirements are considered in the design of your RESTful web services. For a checklist and more detail of items to check, refer to [Countermeasure 553](/library/tasks/T553/). Verify that all aspects of se
---

# T554: Verify that REST web services are securely designed

**Category:** CODE_FIX  
**SD Elements:** [T554](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T554/)  
**Priority:** 6  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Verify that the following security requirements are considered in the design of your RESTful web services. For a checklist and more detail of items to check, refer to [Countermeasure 553](/library/tasks/T553/). 

Verify that all aspects of security are included in the design:

- __Confidentiality:__ Verify that secure channels are used (such as SSL/TLS).
- __Access Control:__ Verify that a secure authentication and authorization mechanism is designed.
- __Integrity and Non Repudiation__: Verify that signature and integrity checks are considered in design.
- __Availability__: Verify that checking the maximum size of message throughput is included in design.

## Success Criteria

- The control "Verify that REST web services are securely designed" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
