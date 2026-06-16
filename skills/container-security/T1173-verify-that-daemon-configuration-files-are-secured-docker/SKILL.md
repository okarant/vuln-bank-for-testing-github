---
name: t1173-verify-that-daemon-configuration-files-are-secured-docker
description: - Find docker.service file location: systemctl show -p FragmentPath docker.service If the file does not exist, this recommendation is not applicable. If the file exists, execute the below commands with the correct file path to verify that t
---

# T1173: Verify that daemon configuration files are secured (Docker)

**Category:** INFRA  
**SD Elements:** [T1173](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1173/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

- Find docker.service file location:

        systemctl show -p FragmentPath docker.service

    If the file does not exist, this recommendation is not applicable. If the file exists, execute the below commands with the correct file path to verify that the file is owned and group-owned by 'root' and the file permissions are set to '644' or more restrictive.

        stat -c %U:%G /usr/lib/systemd/system/docker.service | grep -v root:root

    The above command should not return anything.

        stat -c %a /usr/lib/systemd/system/docker.service

- Find docker.socket file location:

    systemctl show -p FragmentPath docker.socket

    If the file does not exist, this recommendation is not applicable. If the file exists, execute the below commands with the correct file path to verify that the file is owned and group-owned by 'root' and the file permissions are set to '644' or more restrictive.

        stat -c %U:%G /usr/lib/systemd/system/docker.socket | grep -v root:root

    The above command should not return anything.

        stat -c %a /usr/lib/systemd/system/docker.socket

- Execute the below command to verify that the /etc/docker directory is owned and group-owned by 'root':

        stat -c %U:%G /etc/docker | grep -v root:root

    The above command should not return anything.

- Execute the below command to verify that /etc/docker directory has permissions of '755' or more restrictive:

        stat -c %a /etc/docker

- Execute the below command to verify that the registry certificate files are owned and group-owned by 'root':

        stat -c %U:%G /etc/docker/certs.d/* | grep -v root:root

    The above command should not return anything.

- Execute the below command to verify that the registry certificate files have permissions of '444' or more restrictive:

        stat -c %a /etc/docker/certs.d/<registry-name>/*

- Execute the below command to verify that the TLS CA certificate file is owned and group-owned by 'root':

        stat -c %U:%G <path to TLS CA certificate file> | grep -v root:root

    The above command should not return anything.

- Execute the below command to verify that the TLS CA certificate file has permissions of '444' or more restrictive:

        stat -c %a <path to TLS CA certificate file>

- Execute the below command to verify that the Docker server certificate file is owned and group-owned by 'root':

        stat -c %U:%G <path to Docker server certificate file> | grep -v root:root

    The above command should not return anything.

- Execute the below command to verify that the Docker server certificate file has permissions of '444' or more restrictive:

        stat -c %a <path to Docker server certificate file>

- Execute the below command to verify that the Docker server certificate key file is owned and group-owned by 'root':

        stat -c %U:%G <path to Docker server certificate key file> | grep -v root:root

    The above command should not return anything.

- Execute the below command to verify that the Docker server certificate key file has permissions of '400':

        stat -c %a <path to Docker server certificate key file>

- Execute the below command to verify that the Docker socket file is owned by 'root' and group-owned by 'docker':

        stat -c %U:%G /var/run/docker.sock | grep -v root:docker

    The above command should not return anything.

- Execute the below command to verify that the Docker socket file has permissions of '660' or more restrictive:

        stat -c %a /var/run/docker.sock

- Execute the below command to verify that the daemon.json file is owned and group-owned by 'root':

        stat -c %U:%G /etc/docker/daemon.json | grep -v root:root

    The above command should not return anything.

- Execute the below command to verify that the daemon.json file permissions are correctly set to '644' or more restrictive:

        stat -c %a /etc/docker/daemon.json

- Execute the below command to verify that the /etc/default/docker file is owned and group-owned by 'root':

        stat -c %U:%G /etc/default/docker | grep -v root:root

    The above command should not return anything.

- Execute the below command to verify that the /etc/default/docker file permissions are correctly set to '644' or more restrictive:

        stat -c %a /etc/default/docker

- Execute the command below to verify that the /etc/sysconfig/docker file is indiviually owned and group owned by `root`:

        stat -c %U:%G /etc/sysconfig/docker | grep -v root:root

    The above command should not return anything.

- Execute the command below to verify that the /etc/sysconfig/docker file permissions are correctly set to `644` or more restrictively:

        stat -c %a /etc/sysconfig/docker

## Success Criteria

- The requirement "Verify that daemon configuration files are secured (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
