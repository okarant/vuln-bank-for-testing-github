---
name: t4747-limit-container-privileges
description: The purpose of implementing the principle of least privilege (PoLP) for containers is to minimize the risk of exploitation by ensuring that containers only have the minimum privileges necessary to perform their functions. This reduces the p
---

# T4747: Limit container privileges

**Category:** CODE_FIX  
**SD Elements:** [T4747](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4747/)  
**Priority:** 10  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

The purpose of implementing the principle of least privilege (PoLP) for containers is to minimize the risk of exploitation by ensuring that containers only have the minimum privileges necessary to perform their functions. This reduces the potential damage if a container is compromised. 

1. Avoid running containers as root unless absolutely necessary. Running containers as root can expose the system to significant security risks if the container is compromised.
2. Use user namespaces to isolate the privileges of containers. This helps in mapping container user IDs to different host user IDs, providing an additional layer of security.
3. Implement security contexts to control the access and capabilities of containers. Security contexts allow you to define the security settings for a pod or container, such as setting the user ID, group ID, and capabilities.

After implementing this countermeasure, a secure system will have containers running with only the necessary privileges, reducing the risk of privilege escalation and limiting the impact of any potential security breaches.

## Success Criteria

- The control "Limit container privileges" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
