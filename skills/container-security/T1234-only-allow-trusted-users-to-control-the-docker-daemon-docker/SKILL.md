---
name: t1234-only-allow-trusted-users-to-control-the-docker-daemon-dock
description: Remove any users from the 'docker' group that are not trusted. Additionally, do not create a mapping of sensitive directories on the host to the container volumes. The impact is that the rights to build and execute containers as a normal us
---

# T1234: Only allow trusted users to control the Docker daemon (Docker)

**Category:** INFRA  
**SD Elements:** [T1234](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1234/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Remove any users from the 'docker' group that are not trusted. Additionally, do not create a mapping of sensitive directories on the host to the container volumes. The impact is that the rights to build and execute containers as a normal user would be restricted. 

The Docker daemon currently requires 'root' privileges. If the user is added to the 'docker' group, it gives them full 'root' access rights.

Alternatively, you can run the [Docker daemon as a non-root user (Rootless mode)](https://docs.docker.com/engine/security/rootless/).

## Success Criteria

- The requirement "Only allow trusted users to control the Docker daemon (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
