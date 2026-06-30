---
name: t1215-verify-that-containers-are-restricted-from-acquiring-addit
description: The following command should return all the security options currently configured for the containers. `no-new-privileges` should also be one of them. ```` docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: SecurityOpt={{ .H
---

# T1215: Verify that containers are restricted from acquiring additional privileges (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1215](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1215/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

The following command should return all the security options currently configured for the containers. `no-new-privileges` should also be one of them.
````
docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: SecurityOpt={{ .HostConfig.SecurityOpt }}'
````

## Success Criteria

- The control "Verify that containers are restricted from acquiring additional privileges (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
