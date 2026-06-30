---
name: t2596-prevent-http-request-smuggling
description: To secure your server chains against HTTP request smuggling vulnerabilities, actively implement these measures: - Deploy HTTP/2 throughout your infrastructure and disable HTTP downgrading to leverage its robust request length determination 
---

# T2596: Prevent HTTP Request Smuggling

**Category:** INFRA  
**SD Elements:** [T2596](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2596/)  
**Priority:** 9  
**Domain:** network-infra

## Affected Areas in This Repository

Deployment topology (Flask development server on port 5000, no TLS/reverse proxy in repo)

## Why Not Directly Code-Fixable in This Repository

These controls require infrastructure not present in the repository (reverse proxy/WAF, TLS termination, network segmentation, HTTP request-smuggling protections). Document the required infrastructure change.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

To secure your server chains against HTTP request smuggling vulnerabilities, actively implement these measures:
- Deploy HTTP/2 throughout your infrastructure and disable HTTP downgrading to leverage its robust request length determination mechanism, which inherently guards against request smuggling. Should HTTP downgrading be unavoidable, rigorously validate rewritten requests according to the HTTP/1.1 specification, notably rejecting requests with newlines in headers, colons in header names, and spaces in the request method.
- Normalize ambiguous requests at the front-end server and have the back-end server reject any remaining ambiguous requests by severing the TCP connection immediately.
- Opt for terminating the connection when server-level exceptions occur during request processing.
- When using a forward proxy, ensure it supports upstream HTTP/2 to enhance security.


[Source: Portswigger ](https://portswigger.net/web-security/request-smuggling#how-to-prevent-http-request-smuggling-vulnerabilities)

## Success Criteria

- The requirement "Prevent HTTP Request Smuggling" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
