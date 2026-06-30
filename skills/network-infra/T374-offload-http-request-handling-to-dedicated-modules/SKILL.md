---
name: t374-offload-http-request-handling-to-dedicated-modules
description: Follow these guidelines to protect your HTTP server against external attacks: 1. Offload parts of the request handling processes onto the operating system if supported. - Some operating systems provide the web server with specific optimizat
---

# T374: Offload HTTP request handling to dedicated modules

**Category:** INFRA  
**SD Elements:** [T374](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T374/)  
**Priority:** 7  
**Domain:** network-infra

## Affected Areas in This Repository

Deployment topology (Flask development server on port 5000, no TLS/reverse proxy in repo)

## Why Not Directly Code-Fixable in This Repository

These controls require infrastructure not present in the repository (reverse proxy/WAF, TLS termination, network segmentation, HTTP request-smuggling protections). Document the required infrastructure change.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Follow these guidelines to protect your HTTP server against external attacks:

1. Offload parts of the request handling processes onto the operating system if supported.
    - Some operating systems provide the web server with specific optimization capabilities for a listening socket.
    - For example, not sending HTTP requests to the server until the entire request is received.

2. Configure available server-specific modules to protect the HTTP server against resource exhaustion attacks.
    - For example, firewall, QoS, or security modules can restrict certain client behaviors and thereby mitigate risk of weaknesses that lead to denial of service (DoS) problems.

## Success Criteria

- The requirement "Offload HTTP request handling to dedicated modules" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
