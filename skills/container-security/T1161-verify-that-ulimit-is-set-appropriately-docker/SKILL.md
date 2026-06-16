---
name: t1161-verify-that-ulimit-is-set-appropriately-docker
description: Run this command: ```ps -ef | grep dockerd``` Ensure that the `--default-ulimit` parameter is set as appropriate. Run this command to identify overridden ulimits: ```docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Ulimit
---

# T1161: Verify that ulimit is set appropriately (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1161](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1161/)  
**Priority:** 6  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

Run this command:

```ps -ef | grep dockerd```

Ensure that the `--default-ulimit` parameter is set as appropriate.

Run this command to identify overridden ulimits:

```docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: Ulimits={{ .HostConfig.Ulimits }}'```

The above command should return `Ulimits=<no value>` for each container instance until and unless there is an exception and a need to override the default ulimit settings.

## Success Criteria

- The control "Verify that ulimit is set appropriately (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
