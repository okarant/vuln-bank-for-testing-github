---
name: t167-test-that-the-application-is-not-vulnerable-to-json-hijacki
description: Use an HTTP-proxy/inspection tool to ensure that the returned JSON format for AJAX endpoints uses the correct MIME-type, **application/json**, AND conforms to at least one of these secure formats: * Use JSON objects (dictionary) as the high
---

# T167: Test that the application is not vulnerable to JSON Hijacking

**Category:** CODE_FIX  
**SD Elements:** [T167](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T167/)  
**Priority:** 7  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Use an HTTP-proxy/inspection tool to ensure that the returned JSON format for AJAX endpoints uses the correct MIME-type, **application/json**, AND conforms to at least one of these secure formats:

 * Use JSON objects (dictionary) as the highest level construct.
 * Use Comment Filtered JSON format.

You can use any inspection suite, such as Burpsuite, Fiddler, Firebug, or IE Developer Tools, to view the AJAX messages. Check the first few characters of each JSON message. 

 * Set the filter to XHR (XMLHttpRequest) to capture only AJAX messages, if your tool allows that.

 * Inspect AJAX responses.
    * If the first non-white-space character is `[` (an array constructor), then the AJAX endpoint is vulnerable to JSON hijacking.
    * Otherwise, if it starts with `/*` (comment), or `{` (object constructor), then it is not vulnerable.

 * Check the MIME type. 
    * The correct MIME-type is `application/json` or `text/json-comment-filtered`.

## Success Criteria

- The control "Test that the application is not vulnerable to JSON Hijacking" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
