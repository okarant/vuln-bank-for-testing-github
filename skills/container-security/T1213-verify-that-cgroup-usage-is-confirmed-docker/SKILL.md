---
name: t1213-verify-that-cgroup-usage-is-confirmed-docker
description: Use the following command to determine under which containers the _cgroup_ is running. If it is blank, it means containers are running under default docker _cgroup_. In that case, this recommendation is compliant. ```` - docker ps --quiet -
---

# T1213: Verify that cgroup usage is confirmed (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1213](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1213/)  
**Priority:** 7  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

Use the following command to determine under which containers the _cgroup_ is running. If it is blank, it means containers are running under default docker _cgroup_. In that case, this recommendation is compliant. 

````
- docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: CgroupParent={{ .HostConfig.CgroupParent }}'
````
 
If the containers are found to be running under _cgroup_ other than the one that was expected, this test __fails__.

## Success Criteria

- The control "Verify that cgroup usage is confirmed (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
