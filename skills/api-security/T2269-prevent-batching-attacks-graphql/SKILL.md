---
name: t2269-prevent-batching-attacks-graphql
description: Limit incoming requests at the code level so the code will apply the limitation for each batching request. Batching requests or query batching is supported in GraphQL to batch multiple queries or batch requests for various object instances 
---

# T2269: Prevent batching attacks (GraphQL)

**Category:** CODE_FIX  
**SD Elements:** [T2269](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2269/)  
**Priority:** 8  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Limit incoming requests at the code level so the code will apply the limitation for each batching request. Batching requests or query batching is supported in GraphQL to batch multiple queries or batch requests for various object instances in a single network call. To limit requests and thereby reduce the threat of batching attacks, apply one of the following approaches:

- In the code, add an object request rate limit
- Avoid batching sensitive objects
- Limit the number of queries running at the same time

__Note__: Batching attacks lead to several issues such as Application-level DoS attacks, enumeration of objects on the server (like users, emails, user IDs, etc.), and brute-forcing sensitive values
(like passwords, two-factor authentication codes, session tokens, etc.).

## Reference
[OWASP's GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html#batching-attacks)

## Success Criteria

- The control "Prevent batching attacks (GraphQL)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
