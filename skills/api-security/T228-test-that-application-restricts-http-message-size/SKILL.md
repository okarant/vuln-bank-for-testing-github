---
name: t228-test-that-application-restricts-http-message-size
description: Consider the following parameters for HTTP message size restrictions: 1. The maximum number and length of request headers and bodies: - Request body size. - Number of request header fields. - Request header fields size. - Request line size.
---

# T228: Test that application restricts HTTP message size

**Category:** CODE_FIX  
**SD Elements:** [T228](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T228/)  
**Priority:** 9  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Consider the following parameters for HTTP message size restrictions:

1. The maximum number and length of request headers and bodies:

    - Request body size.
    - Number of request header fields.
    - Request header fields size.
    - Request line size.
    - XML request body size.

2. The maximum timeout values:

    - Request read timeout.
    - Keep-alive timeout.

3. The maximum number of concurrent connections and connections backlog capacity.

For each of these items, complete the following steps:

1. Ask developers and review documentation, or server settings, for the maximum value for the attribute.
    - If you are unable to obtain this information, assume it is an excessively large, but reasonable value as the upper bound.

2. Attempt to send an HTTP request (or a set of concurrent requests) with the attribute slightly larger than the maximum value determined in step 1.
    - You can use [Burp Suite](http://portswigger.net/burp/) or [Postman](http://www.getpostman.com/) to create and send arbitrary HTTP requests.
    - [Apache JMeter](http://jmeter.apache.org/) is a useful tool for establishing concurrent connections to the server.

    This test __fails__ if the server accepts the request and sends back a regular HTTP 200 response.

3. Make sure that the request sent in step 2 did not fail due to an unrelated reason, such as an invalid session.
    - If in doubt, review server logs to determine the cause of failure. 
    
    This test __fails__ if the invalid message reaches the application layer or fails for other reasons.

## Success Criteria

- The control "Test that application restricts HTTP message size" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
