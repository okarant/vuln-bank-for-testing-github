---
name: t553-design-secure-restful-web-services
description: See the following guidelines for a high level overview of security requirements for designing a REST client and server: - Consider security for REST on both client and server sides. - The client side of REST deals with user interfaces and u
---

# T553: Design secure RESTful web services

**Category:** CODE_FIX  
**SD Elements:** [T553](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T553/)  
**Priority:** 6  
**Domain:** api-security

## Affected Areas in This Repository

app.py /api/* REST endpoints and /graphql, transaction_graphql.py (graphene schema)

## Required Fix

Enforce authentication and per-object authorization on every endpoint, return only required fields, throttle requests, cap request/response sizes, and for GraphQL limit query depth/complexity, disable batching abuse and disable introspection in production.

## Implementation Guidance (SD Elements)

See the following guidelines for a high level overview of security requirements for designing a REST client and server:

- Consider security for REST on both client and server sides.
    - The client side of REST deals with user interfaces and user states, and it is developed independently from the server side.
    - The server side on the other hand, deals with functions such as data storage, database connections, and business logic.

- Make sure all aspects of security are protected and considered in the design (as detailed below), including:
    - Confidentiality (such as using secure channels)
    - Integrity (such as using signatures)
    - Availability (such as checking the size of messages)
    - Access control

__Confidentiality__

- Mandate secure channels everywhere with no exception to protect data at rest and data in transit between client and server, including session state, and requests.
    - Use SSL/TLS for channel security.

__Access Control__

- Authenticate and authorize the requests on the server side.
    - To reduce the chance of replay attacks, the server should only accept requests within a reasonable timeframe by comparing the timestamp of the sent request with the current timestamp.
    - Use HTTP access control to only allow API access from trusted URLs.
    - To protect the session state, design a secure session management and use session tokens.
    - Session tokens should be protected on the client and the server.

__Integrity and Non Repudiation__

- Digitally sign and verify messages.
    - JSON Web Token (JWT) can be used to ensure the integrity of messages transmitted as JSON objects between parties and XML signature can be used for XML objects.
- Explicitly check the incoming `Content-Type` to be the expected one, such as *application/xml* or *application/json*.

__Availability__

- Specify the maximum size of message throughput to improve the availability of your web services.

References:

- [REST Security Cheat Sheet](https://www.owasp.org/index.php/REST_Security_Cheat_Sheet)
- [Web Service Security Cheat Sheet](https://www.owasp.org/index.php/Web_Service_Security_Cheat_Sheet)
- [REST API and Security](http://lawsonry.github.io/2014/12/introduction-to-rest-apis-and-security/)

## Success Criteria

- The control "Design secure RESTful web services" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
