---
name: t558-authenticate-all-other-components-before-any-network-commun
description: Authenticate application components that communicate through a network before exchanging any kind of information. - This includes mobile applications that communicate with a cloud-based web service, or embedded devices that communicates wit
---

# T558: Authenticate all other components before any network communication with them

**Category:** INFRA  
**SD Elements:** [T558](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T558/)  
**Priority:** 9  
**Domain:** network-infra

## Affected Areas in This Repository

Deployment topology (Flask development server on port 5000, no TLS/reverse proxy in repo)

## Why Not Directly Code-Fixable in This Repository

These controls require infrastructure not present in the repository (reverse proxy/WAF, TLS termination, network segmentation, HTTP request-smuggling protections). Document the required infrastructure change.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Authenticate application components that communicate through a network before exchanging any kind of information.

  - This includes mobile applications that communicate with a cloud-based web service, or embedded devices that communicates with a controller.

  - Implicit and inherent trust of other components leads to external cyberattack avenues.
    - For example, if your web server uses a database located on a separate machine and communicates with it through the network, it should authenticate the database before using it.
    - As another example, your mobile application should authenticate your cloud service before uploading user information.

 - Use authenticated transport and identity verification that fit your environment (for example, verified TLS endpoints, signed tokens, or device/service credentials) instead of trusting internal network location alone.

## Success Criteria

- The requirement "Authenticate all other components before any network communication with them" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
