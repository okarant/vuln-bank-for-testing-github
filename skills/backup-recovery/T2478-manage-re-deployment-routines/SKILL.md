---
name: t2478-manage-re-deployment-routines
description: Ensure that the application, its configuration, and all of its dependencies can be re-deployed in a reasonable time in one of the following ways: * Use automated deployment scripts. * Build from a tested and documented runbook. * Restore fr
---

# T2478: Manage re-deployment routines

**Category:** INFRA  
**SD Elements:** [T2478](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2478/)  
**Priority:** 6  
**Domain:** backup-recovery

## Affected Areas in This Repository

No backup/restore tooling exists in the repository

## Why Not Directly Code-Fixable in This Repository

Backup, restore and re-deployment routines are operational/infrastructure controls with no corresponding code in this repository. Document the required process and infrastructure.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Ensure that the application, its configuration, and all of its dependencies can be re-deployed in a reasonable time in one of the following ways: 

* Use automated deployment scripts.
* Build from a tested and documented runbook.
* Restore from backups.

Some widely used automation tools include Ansible and Jenkins.


##References 
- [OWASP Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/)

## Success Criteria

- The requirement "Manage re-deployment routines" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
