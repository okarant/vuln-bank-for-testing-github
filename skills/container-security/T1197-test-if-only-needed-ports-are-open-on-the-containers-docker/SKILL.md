---
name: t1197-test-if-only-needed-ports-are-open-on-the-containers-docke
description: List all the running instances of containers and their port mapping by executing the below command: docker ps --quiet | xargs docker inspect --format '{{ .Id }}: Ports={{ .NetworkSettings.Ports }}' Review the list and ensure that the ports 
---

# T1197: Test if only needed ports are open on the containers (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1197](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1197/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

List all the running instances of containers and their port mapping by executing the below command:

    docker ps --quiet | xargs docker inspect --format '{{ .Id }}: Ports={{ .NetworkSettings.Ports }}'

Review the list and ensure that the ports mapped are the ones that are really needed for the container.

## Success Criteria

- The control "Test if only needed ports are open on the containers (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
