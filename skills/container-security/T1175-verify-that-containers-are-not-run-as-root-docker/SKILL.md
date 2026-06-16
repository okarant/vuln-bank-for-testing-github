---
name: t1175-verify-that-containers-are-not-run-as-root-docker
description: Run this command: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: User={{ .Config.User }}' It should return container username or user ID. If it is blank it means, the container is running as root.
---

# T1175: Verify that containers are not run as root (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1175](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1175/)  
**Priority:** 9  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

Run this command:

    docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: User={{ .Config.User }}'

It should return container username or user ID. If it is blank it means, the container is running as root.

## Success Criteria

- The control "Verify that containers are not run as root (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
