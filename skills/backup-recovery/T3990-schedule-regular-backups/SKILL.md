---
name: t3990-schedule-regular-backups
description: Use AWS Backup to back up data in AWS storage resources (S3, EBS, EFS, and so on). Follow these best practices: - __Perform automated backups on a set schedule.__ Follow a formal backup policy that specifies the frequency of backups and the
---

# T3990: Schedule regular backups

**Category:** INFRA  
**SD Elements:** [T3990](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T3990/)  
**Priority:** 6  
**Domain:** backup-recovery

## Affected Areas in This Repository

No backup/restore tooling exists in the repository

## Why Not Directly Code-Fixable in This Repository

Backup, restore and re-deployment routines are operational/infrastructure controls with no corresponding code in this repository. Document the required process and infrastructure.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Use AWS Backup to back up data in AWS storage resources (S3, EBS, EFS, and so on). Follow these best practices:
 
 - __Perform automated backups on a set schedule.__ Follow a formal backup policy that specifies the frequency of backups and the retention period based on the data classification.
 - __Monitor backup operations.__ Trigger notifications for failed backup operations using Amazon SNS or CloudWatch alarms. Or, configure an automated response to backup events using Amazon EventBridge.
 - __Establish automated lifecycle processes.__ For example, lifecycle process can move backed up data to cold storage or delete it permanently.
 - __Use AWS Backup Audit Manager to validate compliance.__ Check that the backup requirements you have defined (such as backup frequency and backup encryption) are being implemented.
 - __Protect backup data from unauthorized access.__ Ensure that backup data is encrypted and that access to backup encryption keys is restricted.
 - __Protect backup data from malicious deletion.__ Restrict the ability to delete a restore point. Use AWS Backup Vault Lock to create an immutable backup of critical data. These defenses prevent accidents and limit your exposure to ransomware attacks.
 - __Perform regular data recovery tests.__ Restore the backup to a test environment to verify the correctness of your backup configuration and the availability of backup data.
 
 ## Note
 Different AWS services and resources have different backup requirements.
 - AWS Backup supports data storage resources (including S3, EBS, EFS)
 - Some services provide their own service-specific backup features, which transfer data to an S3 bucket (for example, CloudTrail). Your backup strategy should include evaluating these features and, depending on compliance and business requirements, deciding whether they need S3 versioning or additional backups.

*Advisory: The content of this Countermeasure is currently in Beta and may be generic. Your feedback is valuable to us as we strive to enhance and refine it further.*

## Success Criteria

- The requirement "Schedule regular backups" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
