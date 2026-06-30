---
name: t1157-verify-that-the-aufs-storage-driver-is-not-used-docker
description: Execute the below command and verify that ***aufs*** is not used as storage driver: ```docker info | grep -e "^Storage Driver:\s*aufs\s*$"``` The above command should not return anything.
---

# T1157: Verify that the aufs storage driver is not used (Docker)

**Category:** INFRA  
**SD Elements:** [T1157](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1157/)  
**Priority:** 8  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Why Not Directly Code-Fixable in This Repository

Apply the secure pattern described by SD Elements guidance below.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Execute the below command and verify that ***aufs*** is not used as storage driver:

```docker info | grep -e "^Storage Driver:\s*aufs\s*$"```

The above command should not return anything.

## Success Criteria

- The requirement "Verify that the aufs storage driver is not used (Docker)" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
