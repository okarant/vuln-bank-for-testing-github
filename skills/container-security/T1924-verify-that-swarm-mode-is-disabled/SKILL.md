---
name: t1924-verify-that-swarm-mode-is-disabled
description: Review the output of the docker info command. If the output includes `Swarm: active` it indicates that swarm mode has been activated on the Docker engine. Confirm if swarm mode on the docker engine instance is actually needed.
---

# T1924: Verify that swarm mode is disabled

**Category:** INFRA  
**SD Elements:** [T1924](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1924/)  
**Priority:** 6  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Review the output of the docker info command. If the output includes `Swarm: active` it indicates that swarm mode has been activated on the Docker engine. Confirm if swarm mode on the docker engine instance is actually needed.

## Success Criteria

- The requirement "Verify that swarm mode is disabled" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
