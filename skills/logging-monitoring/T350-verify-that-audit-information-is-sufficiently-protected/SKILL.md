---
name: t350-verify-that-audit-information-is-sufficiently-protected
description: Review the system's/application's audit protection policies and safeguards: - Attempt to change the logs and review the permissions for write, delete, and modification of audit artifacts, such as audit data, audit settings and audit reports
---

# T350: Verify that audit information is sufficiently protected

**Category:** INFRA  
**SD Elements:** [T350](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T350/)  
**Priority:** 7  
**Domain:** logging-monitoring

## Affected Areas in This Repository

app.py (debug_info with IP/User-Agent returned in responses, `print` statements, Flask debug=True)

## Why Not Directly Code-Fixable in This Repository

Use structured logging, never return debug/stack data to clients, redact sensitive fields, protect log access, and disable debug mode in production.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Review the system's/application's audit protection policies and safeguards:

- Attempt to change the logs and review the permissions for write, delete, and modification of audit artifacts, such as audit data, audit settings and audit reports.
    - Try to access and change this data.
    - This test __fails__ if you can modify the data without having the required permissions.

- If the requirements ask for storage of audit information on write-once-read-many (WORM) devices and media, test if they are met.

- Verify that any changes to audit records are recorded according to the adopted policies.

- Work with developers to verify that authorized users can only access audit records on a read-only basis if this is mandated by the policy's regulations.

## Success Criteria

- The requirement "Verify that audit information is sufficiently protected" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
