---
name: t537-test-that-the-size-of-incoming-messages-in-services-is-rest
description: Use the following guidelines to check the size of incoming messages for services: - Perform load testing for services to make sure they are not vulnerable to Denial of Service (DoS) attacks as a result of unrestricted incoming message sizes
---

# T537: Test that the size of incoming messages in services is restricted

**Category:** CODE_FIX  
**SD Elements:** [T537](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T537/)  
**Priority:** 8  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Use the following guidelines to check the size of incoming messages for services:

- Perform load testing for services to make sure they are not vulnerable to Denial of Service (DoS) attacks as a result of unrestricted incoming message sizes.
    - There are different load testing tools available to check whether the maximum size of payload is configured for the services. These tools include Appache JMeter, WebLOAD, and loadUI.
- The tool needs to be able to send requests with different sizes and check the performance.

    This test __fails__ if large requests break the services.

__Notes:__ 

- You should also pay attention to external services that are called within your services. If you receive input from other services within your code, you should also test that your system cannot be brought down by a malicious or malfunctioning external service.

- This countermeasure might not be required if your architecture is designed in a way that a single request creates consistent and low load on your server by using DDoS protection techniques such as an approved DNS or TCP/IP load balancing. Check whether your application is still vulnerable to amplification attacks after using such techniques. If so, then apply the requirements in this countermeasure .

## Success Criteria

- The control "Test that the size of incoming messages in services is restricted" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
