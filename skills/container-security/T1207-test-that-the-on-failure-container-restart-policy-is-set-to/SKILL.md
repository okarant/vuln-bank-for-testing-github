---
name: t1207-test-that-the-on-failure-container-restart-policy-is-set-t
description: Execute the following command: docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: RestartPolicyName={{ .HostConfig.RestartPolicy.Name }} MaximumRetryCount={{ .HostConfig.RestartPolicy.MaximumRetryCount }}' * If the above co
---

# T1207: Test that the 'on-failure' container restart policy is set to 5 (Docker)

**Category:** CODE_FIX  
**SD Elements:** [T1207](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1207/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

Execute the following command:

    docker ps --quiet --all | xargs docker inspect --format '{{ .Id }}: RestartPolicyName={{ .HostConfig.RestartPolicy.Name }} MaximumRetryCount={{ .HostConfig.RestartPolicy.MaximumRetryCount }}'

* If the above command returns `RestartPolicyName=always`, then the system is not configured as desired and hence this recommendation is non-compliant.
* If the above command returns `RestartPolicyName=no` or just `RestartPolicyName=`, then the restart policies are not being used and the container would never be restarted of its own. This recommendation is then Not Applicable and can be assumed to be compliant.
* If the above command returns `RestartPolicyName=on-failure`, then verify that the number of restart attempts is set to 5 or less by looking at `MaximumRetryCount`.

## Success Criteria

- The control "Test that the 'on-failure' container restart policy is set to 5 (Docker)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
