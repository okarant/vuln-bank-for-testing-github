---
name: t1362-perform-message-throttling-in-web-apis
description: To protect APIs against brute-force DoS attacks, use a feature that enforces a set number of failed attempts by a certain IP, API key, or request route during a set period. For example, a web API could allow an IP to have a maximum number o
---

# T1362: Perform message throttling in Web APIs

**Category:** CODE_FIX  
**SD Elements:** [T1362](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1362/)  
**Priority:** 8  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

To protect APIs against brute-force DoS attacks, use a feature that enforces a set number of failed attempts by a certain IP, API key, or request route during a set period. For example, a web API could allow an IP to have a maximum number of requests within a second, minute, or hour.

You should also consider using a feature that throttles multiple requests from, or originating from, the same user (API key). This reduces the likelihood of a brute-force attack.

  - If a user goes over the maximum number of requests, the throttling mechanism should automatically do one of the following:
    - Lock the account or node for a set period.
    - Lock the account or node until it is released by an administrator.
    - Delay the processing of subsequent requests using a suitable algorithm. 

You can use a delay algorithm to increase the time a user has to wait between requests until it becomes inconvenient to continue a brute-force attack. Some web APIs might have short delays of the same interval, but others might increase exponentially. If this user were an attacker inputting random API keys one by one, the delay between the processing of requests would be too long for the attack to be worth the trouble.

__Note__: Refer to this amendment's Additional Requirements for more details about Web API throttling types.

### Web API - throttling types

You can apply different types of throttling as follows:

- __Rate-limit throttling__: A simple throttle limits the number of requests passing through during a time interval. A throttle can be based on the number of requests, size of a payload, or content.

- __IP-level throttling__: Make your API accessible only to white-listed IP addresses, or limit the number of requests sent by a specific client IP.

- __Scope-limit throttling__: Restrict access to specific parts of the API, such as certain methods, functions, or procedures that are based on the users' roles. You can take advantage of the same API across your organization by Implementing scope limiting.

- __Concurrent connections limit__: Limit the number of connections from a user/account to avoid a Denial of Service error when your application cannot respond to more than a certain number of connections.

- __Resource-level throttling__: Use resource-level throttling or hard throttling to limit the number of returned records from your API.
For instance, if a certain query returns a large number of records, throttle the request so that your SQL engine limits the number of rows returned by using conditions attributes such as TOP, SKIP, SQL_ATTR_MAX_ROWS, and so on.

- __Tiers of throttling__: Apply throttling at multiple levels in your organization:
    - API-level throttling
    - Application-level throttling
    - User-level throttling
    - Account-level throttling

## References
[How to Rate-Limit an API Query](https://www.progress.com/blogs/how-to-rate-limit-an-api-query-throttling-made-easy)

### Secure API Resource Consumption Guidelines

- Use a solution that makes it easy to limit memory, CPU, number of restarts, file descriptors, and processes, such as Containers / Serverless code (e.g. Lambdas).

- Define and enforce a maximum size of data on all incoming parameters and payloads, such as maximum length for strings, maximum number of elements in arrays, and maximum upload file size (regardless of whether it is stored locally or in cloud storage). Reject requests that require excessive work. Look for work that scales nonlinearly, which means it suddenly requires exponentially more time to complete when you pass a certain threshold. Thorough testing can help you detect issues that you might not catch in a code review.


- Implement a limit on how often a client can interact with the API within a defined timeframe (rate limiting).

- Rate limiting should be fine-tuned based on the business needs. Some API Endpoints might require stricter policies.

- Limit/throttle how many times or how often a single API client/user can execute a single operation (for example, validate an OTP, or request password recovery without visiting the one-time URL).

- Add proper server-side validation for query strings and request body parameters, specifically the one that controls the number of records to be returned in the response.

- Configure spending limits for all service providers/API integrations. When setting spending limits is not possible, billing alerts should be configured instead.
- Deploy techniques that can slow down automated access to sensitive business operations (for example, making and receiving payment, authentication, core business use case and so on) such as device fingerprinting, human detection, non-human pattern analysis, blocking known threat sources and so on.

## Success Criteria

- The control "Perform message throttling in Web APIs" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
