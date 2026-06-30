---
name: t1235-test-that-only-trusted-users-can-control-the-docker-daemon
description: Execute the following command on the docker host and ensure that only trusted users are members of the 'docker' group: getent group docker
---

# T1235: Test that only trusted users can control the Docker daemon (Docker)

**Category:** INFRA  
**SD Elements:** [T1235](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1235/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Execute the following command on the docker host and ensure that only trusted users are members of the 'docker' group:

          getent group docker

## Success Criteria

- The requirement "Test that only trusted users can control the Docker daemon (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
