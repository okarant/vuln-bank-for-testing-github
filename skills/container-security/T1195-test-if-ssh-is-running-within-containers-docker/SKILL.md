---
name: t1195-test-if-ssh-is-running-within-containers-docker
description: - List all the running instances of containers by executing below command: docker ps --quiet - For each container instance, execute the below command: docker exec $INSTANCE_ID ps -el - Ensure that there is no process for SSH server.
---

# T1195: Test if SSH is running within containers (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1195](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1195/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

- List all the running instances of containers by executing below command:

        docker ps --quiet 

- For each container instance, execute the below command:

        docker exec $INSTANCE_ID ps -el

- Ensure that there is no process for SSH server.

## Success Criteria

- The control "Test if SSH is running within containers (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
