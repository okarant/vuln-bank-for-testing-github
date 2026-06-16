---
name: t2283-configure-graphql-correctly
description: GraphQL's default configuration is often insecure for the production environment. Follow the guidelines below to secure a GraphQL application: - Disable GraphiQL and Introspection - Make sure the `NODE_ENV` environment variable has a value.
---

# T2283: Configure GraphQL correctly

**Category:** CODE_FIX  
**SD Elements:** [T2283](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2283/)  
**Priority:** 9  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

GraphQL's default configuration is often insecure for the production environment. Follow the guidelines below to secure a GraphQL application:

- Disable GraphiQL and Introspection
- Make sure the `NODE_ENV` environment variable has a value. For production use, set `NODE_ENV` to **production**, and for development, set the value to **test**. If setting `NODE_ENV` is not possible, pass `debug:false` to the Apollo server constructor.
- In some implementations of GraphQL, even though Introspection and GraphiQL are disabled, an attacker is able to guess the field names based on the hint that GraphQL's response gives them. Use [ShapeShifter](https://github.com/szski/shapeshifter) which is a tool designed to help with disabling this feature. For more information on secure error handling, see [T159](/library/tasks/T159)
- To remove sensitive information from error messages before they are sent to a user or Apollo Studio or get logged with stack messages, see [this link](https://www.apollographql.com/docs/apollo-server/data/errors/#masking-and-logging-errors)

## Reference
[OWASP's GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html#secure-configurations)

## Success Criteria

- The control "Configure GraphQL correctly" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
