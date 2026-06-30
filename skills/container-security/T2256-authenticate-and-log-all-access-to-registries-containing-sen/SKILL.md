---
name: t2256-authenticate-and-log-all-access-to-registries-containing-s
description: Take the following steps to ensure only authorized users can access sensitive images: - Use private registries to store and share sensitive images. - Disable any type of anonymous access to registries (public, default users). - Limit read a
---

# T2256: Authenticate and log all access to registries containing sensitive or proprietary images

**Category:** INFRA  
**SD Elements:** [T2256](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2256/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Take the following steps to ensure only authorized users can access sensitive images: 

- Use private registries to store and share sensitive images.
- Disable any type of anonymous access to registries (public, default users).
- Limit read and write access to registries to trusted entities.
- Implement strong role-based access controls to access registries or centralize registry authentication with existing accounts to take advantage of security controls already in place for those accounts.
- Log and audit all access to registries that contain proprietary or sensitive images.

## Success Criteria

- The requirement "Authenticate and log all access to registries containing sensitive or proprietary images" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
