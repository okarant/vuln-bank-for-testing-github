---
name: t576-verify-that-uddi-ebxml-spoofing-is-prevented
description: Use the following guidelines for verifying that you prevent UDDI/ebXML spoofing: __For applications that rely on registry/discovery services:__ - Verify that only signed messages (or trusted by other means of authentication) from *Universal
---

# T576: Verify that UDDI/ebXML spoofing is prevented

**Category:** CODE_FIX  
**SD Elements:** [T576](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T576/)  
**Priority:** 8  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Use the following guidelines for verifying that you prevent UDDI/ebXML spoofing:

__For applications that rely on registry/discovery services:__

- Verify that only signed messages (or trusted by other means of authentication) from *Universal Description, Discovery and Integration (UDDI)*, *Electronic Business XML(ebXML)*, or any other similar discovery/registry services that are taken into consideration when finding web services.

- Verify that the system does not crash or unacceptably slow down if the right entries do not exist and restriction are applied on the amount of data added to UDDI upon the registry to prevent Denial of Service (DoS). 

__For registry/discovery services:__

Verify that entries are signed, and protected against unauthorized manipulation.

## Success Criteria

- The control "Verify that UDDI/ebXML spoofing is prevented" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
