---
name: t2109-enable-signed-image-enforcement-docker
description: The Universal Control Plane includes the ability to enforce running of only images that have been signed by members of a particular group. Enable this capability to prevent unsigned images from being deployed to your cluster. Combined with 
---

# T2109: Enable signed image enforcement (Docker)

**Category:** INFRA  
**SD Elements:** [T2109](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2109/)  
**Priority:** 9  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

The Universal Control Plane includes the ability to enforce running of only images that have been signed by members of a particular group. Enable this capability to prevent unsigned images from being deployed to your cluster.

Combined with the Docker Content Trust recommendations, signed image enforcement in UCP gives you more control over the validity and origination of your Docker images prior to deployment. Signed image enforcement can prohibit images that are unsigned, have malformed signatures, and/or compromised signatures from being deployed.

## Success Criteria

- The requirement "Enable signed image enforcement (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
