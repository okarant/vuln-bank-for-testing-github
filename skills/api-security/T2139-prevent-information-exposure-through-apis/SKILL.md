---
name: t2139-prevent-information-exposure-through-apis
description: Use the following guidelines to avoid exposing information with APIs: - Remove unused API endpoints. - Never return unrequested sensitive data in API responses, and never rely on the client-side filtering. Attackers can call the API directl
---

# T2139: Prevent information exposure through APIs

**Category:** CODE_FIX  
**SD Elements:** [T2139](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2139/)  
**Priority:** 7  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Use the following guidelines to avoid exposing information with APIs:

  - Remove unused API endpoints.

  - Never return unrequested sensitive data in API responses, and never rely on the client-side filtering. Attackers can call the API directly and receive sensitive data that the client would filter out.

  - Avoid using generic methods that return entire objects without restriction or filtering. Examples include `to_json()` and `to_s()` in Ruby on Rails. Instead, return only the information that is required to satisfy the functionality of that endpoint.

  - Define a schema for all the data returned by API methods including errors, and enforce it by a schema-based response validation mechanism. Use this mechanism as an extra layer of security.

  - Do not use fully populated objects that mirror database records in your code when it isn't necessary.

  - Make sure the data you're returning is appropriate and aligns with what the client is allowed to see. Define what data each endpoint is allowed to return, and consider using unit tests to check that you aren't accidentally exposing extra information.

## Success Criteria

- The control "Prevent information exposure through APIs" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
