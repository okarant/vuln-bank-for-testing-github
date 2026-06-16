---
name: t1205-test-if-the-container-s-root-file-system-is-mounted-as-rea
description: Execute the following command: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: ReadonlyRootfs={{ .HostConfig.ReadonlyRootfs }}' If the above command returns _true_, it means the root filesystem is mounted read-only. If t
---

# T1205: Test if the container's root file system is mounted as read-only (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1205](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1205/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

Execute the following command:

    docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: ReadonlyRootfs={{ .HostConfig.ReadonlyRootfs }}' 

If the above command returns _true_, it means the root filesystem is mounted read-only. If the above command returns _false_, it means the root filesystem is writable.

Additionally, you may use below command to find the differences between the container instance and its corresponding image.

    docker diff $INSTANCE_ID

## Success Criteria

- The control "Test if the container's root file system is mounted as read-only (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
