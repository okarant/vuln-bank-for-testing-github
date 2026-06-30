---
name: t1233-test-that-containers-are-on-a-separate-partition-docker
description: At the Docker host execute the below command: grep /var/lib/docker /etc/fstab This should return the partition details for `/var/lib/docker` mount-point.
---

# T1233: Test that containers are on a separate partition (Docker)

**Category:** INFRA  
**SD Elements:** [T1233](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1233/)  
**Priority:** 6  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

At the Docker host execute the below command:

          grep /var/lib/docker /etc/fstab 

This should return the partition details for `/var/lib/docker` mount-point.

## Success Criteria

- The requirement "Test that containers are on a separate partition (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
