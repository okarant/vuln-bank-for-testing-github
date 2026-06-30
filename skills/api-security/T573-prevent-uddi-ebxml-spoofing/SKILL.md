---
name: t573-prevent-uddi-ebxml-spoofing
description: Use the following guidelines for preventing UDDI and ebXML spoofing: __For applications that rely on registry/discovery services:__ - Only trust messages from *Universal Description, Discovery and Integration (UDDI)*, *Electronic Business X
---

# T573: Prevent UDDI/ebXML spoofing

**Category:** CODE_FIX  
**SD Elements:** [T573](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T573/)  
**Priority:** 8  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Use the following guidelines for preventing UDDI and ebXML spoofing:

__For applications that rely on registry/discovery services:__

- Only trust messages from *Universal Description, Discovery and Integration (UDDI)*,  *Electronic Business XML(ebXML)*, or similar discovery/registry services that are signed and verified by a trusted party.
- This prevents spoofing attacks in which attackers can craft malicious UDDI entries to reference harmful web services.

__For registry/discovery services:__

- Provide users/callers a means to check the authenticity of those entries.
- Protect the directory and do not allow unauthorized entities to add information to the service directory without proper analysis and verification by qualified individuals.

## Success Criteria

- The control "Prevent UDDI/ebXML spoofing" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
