---
name: t1232-create-a-separate-partition-for-containers-docker
description: Create a separate partition for Docker files. All Docker containers and their data and metadata are stored under `/var/lib/docker` directory. By default, `/var/lib/docker` would be mounted under `/` or `/var` partitions based on availabilit
---

# T1232: Create a separate partition for containers (Docker)

**Category:** INFRA  
**SD Elements:** [T1232](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1232/)  
**Priority:** 6  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Create a separate partition for Docker files. All Docker containers and their data and metadata are stored under `/var/lib/docker` directory. By default, `/var/lib/docker` would be mounted under `/` or `/var` partitions based on availability.

## Success Criteria

- The requirement "Create a separate partition for containers (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
