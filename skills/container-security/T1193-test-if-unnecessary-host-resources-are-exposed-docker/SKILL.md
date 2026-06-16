---
name: t1193-test-if-unnecessary-host-resources-are-exposed-docker
description: - Execute the following command: ``` docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Volumes={{ .Mounts }}' ``` The above commands would return the list of current mapped directories and whether they are mounted in read-
---

# T1193: Test if unnecessary host resources are exposed (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1193](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1193/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

- Execute the following command:
```
docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Volumes={{ .Mounts }}'
```
The above commands would return the list of current mapped directories and whether they are mounted in read-write mode for each container instance.

- Execute the following command:
```
docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: PidMode={{ .HostConfig.PidMode }}'
```
If the above command returns `host`, it means the host PID namespace is shared with the container else this recommendation is compliant.

- Execute the following command:
```
docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: IpcMode={{ .HostConfig.IpcMode }}'
```
If the above command returns `host`, it means the host IPC namespace is shared with the container. If the above command returns nothing, then the host's IPC namespace is not shared. This recommendation is then compliant.

- Execute the following command:
```
docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Devices={{ .HostConfig.Devices }}'
```
The above command would list out each device with below information:

 * CgroupPermissions - For example, rwm
 * PathInContainer - Device path within the container
 * PathOnHost - Device path on the host

Verify that the host device is needed to be accessed from within the container and the permissions required are correctly set. If the above command returns [], then the container does not have access to host devices. This recommendation can be assumed to be compliant.

- Execute the following command:
```
docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: UTSMode={{ .HostConfig.UTSMode }}'
```
If the above command returns 'host', it means the host UTS namespace is shared with the container and this recommendation is non-compliant. If the above command returns nothing, then the host's UTS namespace is not shared. This recommendation is then compliant.

- Run the below command and ensure that it does not return any value for UsernsMode. If it returns a value of host, it means the host user namespace is shared with the containers.
```
docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: UsernsMode={{ .HostConfig.UsernsMode }}'
```
- Execute the following command:
```
docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Volumes={{ .Mounts }}' | grep docker.sock
```
The above command would return any instances where docker.sock had been mapped to a container as a volume.

## Success Criteria

- The control "Test if unnecessary host resources are exposed (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
