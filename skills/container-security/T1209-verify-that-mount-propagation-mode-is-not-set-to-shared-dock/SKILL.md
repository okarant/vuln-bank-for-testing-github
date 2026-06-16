---
name: t1209-verify-that-mount-propagation-mode-is-not-set-to-shared-do
description: Use the following command to verify the propagation mode for mounted volumes is __not__ set to __shared__ : ```` docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Propagation={{range $mnt := .Mounts}} {{json $mnt.Propagati
---

# T1209: Verify that mount propagation mode is not set to 'shared' (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1209](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1209/)  
**Priority:** 7  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

Use the following command to verify the propagation mode for mounted volumes is __not__ set to __shared__ :
````
docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Propagation={{range $mnt := .Mounts}} {{json $mnt.Propagation}} {{end}}'
````
The above command might throw errors if there are no mounts. In that case, this recommendation is not applicable.

## Success Criteria

- The control "Verify that mount propagation mode is not set to 'shared' (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
