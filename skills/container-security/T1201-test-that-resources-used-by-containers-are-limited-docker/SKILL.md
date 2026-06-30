---
name: t1201-test-that-resources-used-by-containers-are-limited-docker
description: Execute the following command: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Memory={{ .HostConfig.Memory }}' If the above command returns 0, it means the memory limits are not in place. If the above command returns a 
---

# T1201: Test that resources used by containers are limited (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1201](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1201/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

Execute the following command:

    docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Memory={{ .HostConfig.Memory }}'

If the above command returns 0, it means the memory limits are not in place. If the above command returns a non-zero value, it means memory limits are in place.

Run the below command and ensure that PidsLimit is not set to 0 or -1. A PidsLimit of 0 or -1 means that any number of processes can be forked inside the container concurrently.

    docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: PidsLimit={{ .HostConfig.PidsLimit }}'

## Success Criteria

- The control "Test that resources used by containers are limited (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
