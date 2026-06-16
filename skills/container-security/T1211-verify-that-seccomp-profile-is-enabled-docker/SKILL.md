---
name: t1211-verify-that-seccomp-profile-is-enabled-docker
description: To verify that _seccomp_ profile is configured, use the following command and check if it returns `<no value>` or your modified _seccomp_ profile. If it returns `[seccomp:unconfined]`, that means this recommendation is non-compliant and the
---

# T1211: Verify that seccomp profile is enabled (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1211](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1211/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

To verify that _seccomp_ profile is configured, use the following command and check if it returns `<no value>` or your modified _seccomp_ profile. If it returns `[seccomp:unconfined]`, that means this recommendation is non-compliant and the container is running without any _seccomp_ profiles.

````
- docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: SecurityOpt={{.HostConfig.SecurityOpt }}'
````

## Success Criteria

- The control "Verify that seccomp profile is enabled (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
