---
name: t536-restrict-the-size-of-incoming-messages-in-services
description: Use the following guidelines for restricting the size of incoming messages in services: - Limit the size of input messages that services accept to protect them against Denial of Service (DoS) attacks. - If services call other services as pa
---

# T536: Restrict the size of incoming messages in services

**Category:** CODE_FIX  
**SD Elements:** [T536](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T536/)  
**Priority:** 8  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Use the following guidelines for restricting the size of incoming messages in services:

- Limit the size of input messages that services accept to protect them against Denial of Service (DoS) attacks.
    - If services call other services as part of their operation, make sure the message sizes are within a range.
    - Some servers allow setting these values in configuration files.

__Notes:__ 

- According to NIST 800-95, oversized XML documents can also cause XML parsers to collapse. Configure the server the service is running on to only accept messages up to a certain size.

- This countermeasure might not be required if your architecture is designed in a way that you have low load on your server by using techniques such as DNS or TCP/IP load balancing. Check whether your application is still vulnerable to amplification attacks after using such techniques. If so, then apply the requirements in this countermeasure.

## Success Criteria

- The control "Restrict the size of incoming messages in services" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
