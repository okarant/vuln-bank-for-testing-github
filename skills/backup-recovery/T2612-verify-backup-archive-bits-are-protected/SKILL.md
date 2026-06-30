---
name: t2612-verify-backup-archive-bits-are-protected
description: Verify that archive bits are only changed when the files are open and modified, and no other system or application activity can alter the archive bits.
---

# T2612: Verify backup archive bits are protected

**Category:** INFRA  
**SD Elements:** [T2612](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2612/)  
**Priority:** 7  
**Domain:** backup-recovery

## Affected Areas in This Repository

No backup/restore tooling exists in the repository

## Why Not Directly Code-Fixable in This Repository

Backup, restore and re-deployment routines are operational/infrastructure controls with no corresponding code in this repository. Document the required process and infrastructure.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Verify that archive bits are only changed when the files are open and modified, and no other system or application activity can alter the archive bits.

## Success Criteria

- The requirement "Verify backup archive bits are protected" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
