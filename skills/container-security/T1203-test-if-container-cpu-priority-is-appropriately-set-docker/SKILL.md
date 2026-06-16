---
name: t1203-test-if-container-cpu-priority-is-appropriately-set-docker
description: Execute the following command: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: CpuShares={{ .HostConfig.CpuShares }}' If the above command returns 0 or 1024, it means the CPU shares are not in place. If the above command
---

# T1203: Test if container CPU priority is appropriately set (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1203](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1203/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

Execute the following command:

        docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: CpuShares={{ .HostConfig.CpuShares }}'

If the above command returns 0 or 1024, it means the CPU shares are not in place. If the above command returns a non-zero value other than 1024, it means CPU shares are in place.

## Success Criteria

- The control "Test if container CPU priority is appropriately set (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
