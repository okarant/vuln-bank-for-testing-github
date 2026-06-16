---
name: t1167-verify-that-data-exchanged-between-containers-on-different
description: Run the below command and ensure that each overlay network has been encrypted. docker network ls --filter driver=overlay --quiet | xargs docker network inspect --format '{{.Name}} {{ .Options }}'
---

# T1167: Verify that data exchanged between containers on different nodes on the overlay network is encrypted (Docker)

**Category:** INFRA  
**SD Elements:** [T1167](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1167/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Run the below command and ensure that each overlay network has been encrypted.

    docker network ls --filter driver=overlay --quiet | xargs docker network inspect --format '{{.Name}} {{ .Options }}'

## Success Criteria

- The requirement "Verify that data exchanged between containers on different nodes on the overlay network is encrypted (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
