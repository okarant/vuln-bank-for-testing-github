---
name: t2603-protect-backup-archive-bits
description: Full and incremental backups set the archive bit for backed-up files to 0 when finished so the file won't be included in a subsequent backup. When someone opens and saves a file, the archive bit is changed to 1, and is then included in the 
---

# T2603: Protect backup archive bits

**Category:** INFRA  
**SD Elements:** [T2603](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2603/)  
**Priority:** 7  
**Domain:** backup-recovery

## Affected Areas in This Repository

No backup/restore tooling exists in the repository

## Why Not Directly Code-Fixable in This Repository

Backup, restore and re-deployment routines are operational/infrastructure controls with no corresponding code in this repository. Document the required process and infrastructure.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Full and incremental backups set the archive bit for backed-up files to 0 when finished so the file won't be included in a subsequent backup. When someone opens and saves a file, the archive bit is changed to 1, and is then included in the next backup.

- Ensure there's nothing else in your system or application that changes the archive bits or your backups may be at risk of missing files and changes that should be backed up.

## Success Criteria

- The requirement "Protect backup archive bits" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
