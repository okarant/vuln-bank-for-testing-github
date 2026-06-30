---
name: t2284-prevent-dos-attacks-graphql
description: Use the following guideline to prevent DoS attacks in GraphQL: - Limit incoming queries by adding depth and amount limitations. Each query has depth by default, and each requested object in a query can have a defined amount. As both can be 
---

# T2284: Prevent DoS attacks (GraphQL)

**Category:** CODE_FIX  
**SD Elements:** [T2284](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2284/)  
**Priority:** 8  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Use the following guideline to prevent DoS attacks in GraphQL:

- Limit incoming queries by adding depth and amount limitations. Each query has depth by default, and each requested object in a query can have a defined amount. As both can be unlimited and can potentially enable a DoS attack, setting some limits on depth and amount through a custom implementation is strongly recommended. A reasonable depth limit might be 4-7 levels of nested fields, depending on the complexity of your data and the resources available to your server.
- Consider setting a maximum incoming request rate per IP or user (or both).
- Limit the amount of data that can be returned in a single response by adding pagination. In GraphQL, some fields return a list of values, so developers can use different pagination models to apply different capabilities for limiting the response.
- Enforce a maximum number of queries based on a query cost analysis.
- Apply batching and caching techniques on the server side. This technique allows multiple requests for data from a backend, gathered over a short period of time, to be sent in a single request to a database or microservice by applying a tool such as Facebook's DataLoader.

## Reference
[OWASP's GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html#dos-prevention)

## Success Criteria

- The control "Prevent DoS attacks (GraphQL)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
