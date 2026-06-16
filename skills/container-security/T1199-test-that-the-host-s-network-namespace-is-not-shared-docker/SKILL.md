---
name: t1199-test-that-the-host-s-network-namespace-is-not-shared-docke
description: Execute the following command: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: NetworkMode={{ .HostConfig.NetworkMode }}' If the above command returns 'NetworkMode=host', it means '--net=host' option was passed when cont
---

# T1199: Test that the host's network namespace is not shared (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1199](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1199/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

Execute the following command:

        docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: NetworkMode={{ .HostConfig.NetworkMode }}'

If the above command returns 'NetworkMode=host', it means '--net=host' option was passed when container was started. This would be non-compliant. It should return bridge, none, or container:$Container_Instance to be compliant.

## Success Criteria

- The control "Test that the host's network namespace is not shared (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
