---
name: t166-protect-against-json-hijacking
description: Use the following guidelines to reduce the risk of JSON hijacking attacks, especially when dealing with older web browsers: * Make the URLs in the system used to retrieve JSON objects unpredictable and unique for each user session. * On the
---

# T166: Protect against JSON hijacking

**Category:** CODE_FIX  
**SD Elements:** [T166](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T166/)  
**Priority:** 7  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

Use the following guidelines to reduce the risk of JSON hijacking attacks, especially when dealing with older web browsers:

* Make the URLs in the system used to retrieve JSON objects unpredictable and unique for each user session.
* On the server side, use a hard to guess random nonce that is unique to the user's session to differentiate between legitimate requests and forged requests similar to protection against Cross-Site Request Forgey (CSRF).
    * Each request from the client to the server should contain this nonce and the server should reject all other requests.
* Use the **application/json** MIME type for all returned JSON responses.
    * Avoid using text/html.
* Do not use arrays as the highest level JSON structure. Use objects (dictionaries) instead.
    * For example, if you need to return `[1,2,3]`, return `{ "result": [1,2,3] }` instead.
* To avoid client-side browser bugs, make it difficult to get access to the JSON object content via the "Script" tag by surrounding the returned JSON message with comment tags. For example, a JSON string like `[1,2,3]` should be commented out like `/* [1,2,3] */` before being sent to the client. If your client-side library allows it (Dojo for example), use Comment Filtered JSON format and "**text/json-comment-filtered**" MIME type and the client would automatically strip the comment tags.
* You may also add other types of surrounding tags or prefixes/postfixes that suit your application to the returned JSON message to make the syntax non-valid for JavaScript. As a result of this, the browser would raise an error if the client-side code tries to load the JSON using the "Acript" tag. You should remove the surrounding tags in your client-side code manually before parsing the JSON message.

## Success Criteria

- The control "Protect against JSON hijacking" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
