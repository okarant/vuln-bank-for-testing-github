---
name: t589-verify-that-all-the-components-are-authenticated-explicitly
description: Verify that your application authenticates all other components explicitly before any kind of network communication with them. Additionally, ensure that it does not rely on an implicit trust of other components.
---

# T589: Verify that all the components are authenticated explicitly

**Category:** INFRA  
**SD Elements:** [T589](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T589/)  
**Priority:** 9  
**Domain:** network-infra

## Affected Areas in This Repository

Deployment topology (Flask development server on port 5000, no TLS/reverse proxy in repo)

## Why Not Directly Code-Fixable in This Repository

These controls require infrastructure not present in the repository (reverse proxy/WAF, TLS termination, network segmentation, HTTP request-smuggling protections). Document the required infrastructure change.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Verify that your application authenticates all other components explicitly before any kind of network communication with them.

Additionally, ensure that it does not rely on an implicit trust of other components.

## Success Criteria

- The requirement "Verify that all the components are authenticated explicitly" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
