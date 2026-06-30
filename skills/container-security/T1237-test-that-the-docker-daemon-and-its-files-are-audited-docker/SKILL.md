---
name: t1237-test-that-the-docker-daemon-and-its-files-are-audited-dock
description: - Verify that there is an audit rule for the Docker daemon. For example, execute this command: auditctl -l | grep /usr/bin/docker This should list a rule for the Docker daemon. - Verify that there is an audit rule corresponding to /var/lib/
---

# T1237: Test that the Docker daemon and its files are audited (Docker)

**Category:** INFRA  
**SD Elements:** [T1237](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1237/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

- Verify that there is an audit rule for the Docker daemon. For example, execute this command:

        auditctl -l | grep /usr/bin/docker

This should list a rule for the Docker daemon.

- Verify that there is an audit rule corresponding to /var/lib/docker directory. For example, execute this command:

        auditctl -l | grep /var/lib/docker

This should list a rule for /var/lib/docker directory.

- Verify that there is an audit rule corresponding to /etc/docker directory. For example, execute this command:

        auditctl -l | grep /etc/docker

This should list a rule for /etc/docker directory.

- Find out the file location:

        systemctl show -p FragmentPath docker.service
 
If the file does not exist, this recommendation is not applicable. If the file exists, verify that there is an audit rule corresponding to the file. For example, execute this command:

        auditctl -l | grep docker.service

This should list a rule for docker.service as per its location.

- Find out the file location:

        systemctl show -p FragmentPath docker.socket

If the file does not exist, this recommendation is not applicable. If the file exists, verify that there is an audit rule corresponding to the file. For example, execute the this command:

        auditctl -l | grep docker.socket

This should list a rule for docker.socket as per its location.

- Verify that there is an audit rule corresponding to /etc/default/docker file. For example, execute this command:

        auditctl -l | grep /etc/default/docker

This should list a rule for /etc/default/docker file.

- Verify that there is an audit rule corresponding to /etc/docker/daemon.json file. For example, execute this command:

        auditctl -l | grep /etc/docker/daemon.json

 This should list a rule for /etc/docker/daemon.json file.

- Verify that there is an audit rule corresponding to /usr/bin/docker-containerd file. For example, execute this command:

        auditctl -l | grep /usr/bin/docker-containerd

 

 This should list a rule for /usr/bin/docker-containerd file.

- Verify that there is an audit rule corresponding to /usr/bin/docker-runc file. For example, execute this command:

        auditctl -l | grep /usr/bin/docker-runc

 
This should list a rule for /usr/bin/docker-runc file.

## Success Criteria

- The requirement "Test that the Docker daemon and its files are audited (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
