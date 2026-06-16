---
name: t1155-verify-that-docker-registries-are-secure-docker
description: Run docker info or execute the below command to find out if any insecure registries are used: ``` ps -ef | grep dockerd ``` Ensure that the `--insecure-registry` parameter is not present.
---

# T1155: Verify that Docker registries are secure (Docker)

**Category:** INFRA  
**SD Elements:** [T1155](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1155/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Run docker info or execute the below command to find out if any insecure registries are used:

```
ps -ef | grep dockerd
```

Ensure that the `--insecure-registry` parameter is not present.

## Success Criteria

- The requirement "Verify that Docker registries are secure (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
