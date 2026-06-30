---
name: t1236-audit-the-docker-daemon-and-its-files-docker
description: Follow these guidelines to audit Docker daemon and important Docker files and directories: - Audit Docker daemon. - Audit /var/lib/docker directory: It holds all the information about containers. - Audit /etc/docker directory: It holds vari
---

# T1236: Audit the Docker daemon and its files (Docker)

**Category:** INFRA  
**SD Elements:** [T1236](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1236/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Follow these guidelines to audit Docker daemon and important Docker files and directories:

- Audit Docker daemon.
- Audit /var/lib/docker directory: It holds all the information about containers.
- Audit /etc/docker directory: It holds various certificates and keys used for TLS communication between Docker daemon and Docker client.
- Audit docker.service file: The docker.service file might be present if the daemon parameters have been changed by an administrator. It holds various parameters for Docker daemon.
- Audit docker.socket file: It holds various parameters for Docker daemon socket.
- Audit /etc/default/docker file: It holds various parameters for Docker daemon.
- Audit /etc/docker/daemon.json file: It holds various parameters for Docker daemon.
- Audit /usr/bin/docker-containerd file: Docker now relies on `containerd` and `runC` to spawn containers.
- Audit /usr/bin/docker-runc file: Docker now relies on `containerd` and `runC` to spawn containers.

__Note 1:__ Auditing generates quite big log files. Ensure to rotate and archive them periodically. Also, create a separate partition of audit to avoid filling root file system.

__Note 2:__ By default, Docker related files and directories are not audited. Some of these files may not be available on the system. In that case, the recommendations are not applicable.

## Success Criteria

- The requirement "Audit the Docker daemon and its files (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
