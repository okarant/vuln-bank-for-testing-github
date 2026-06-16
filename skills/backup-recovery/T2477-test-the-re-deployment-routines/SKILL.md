---
name: t2477-test-the-re-deployment-routines
description: Verify that you have at least one of the following: * Automated deployment scripts. * Tested and documented runbook. * Recent backups. The purpose is to ensure the application, its configuration, and all its dependencies can recover and be 
---

# T2477: Test the re-deployment routines

**Category:** INFRA  
**SD Elements:** [T2477](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2477/)  
**Priority:** 6  
**Domain:** backup-recovery

## Affected Areas in This Repository

No backup/restore tooling exists in the repository

## Why Not Directly Code-Fixable in This Repository

Backup, restore and re-deployment routines are operational/infrastructure controls with no corresponding code in this repository. Document the required process and infrastructure.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Verify that you have at least one of the following:

* Automated deployment scripts. 
* Tested and documented runbook. 
* Recent backups.

The purpose is to ensure the application, its configuration, and all its dependencies can recover and be successfully re-deployed in a reasonable time. 

One possible way to pass the test is by re-deploying the application and its related components using your selected methods.

## Success Criteria

- The requirement "Test the re-deployment routines" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
