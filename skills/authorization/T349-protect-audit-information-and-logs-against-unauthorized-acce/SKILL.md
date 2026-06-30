---
name: t349-protect-audit-information-and-logs-against-unauthorized-acc
description: Protect audit information against unauthorized deletion or modification. This countermeasure is as crucial as logging important events itself. Follow these guidelines to protect audit records: - Identify, classify and collect required audit
---

# T349: Protect audit information and logs against unauthorized access

**Category:** INFRA  
**SD Elements:** [T349](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T349/)  
**Priority:** 7  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Why Not Directly Code-Fixable in This Repository

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Protect audit information against unauthorized deletion or modification. This countermeasure is as crucial as logging important events itself.

Follow these guidelines to protect audit records:

- Identify, classify and collect required audit information:
    - Audit information includes not only audit data, but audit settings and audit reports.

- Design and develop extra safeguards:
    - Give audit data a higher level of attention/security, prevent any modification to such data, or at a minimum, record the changes. 
    - The use of write-once-read-many (WORM) media is one way to adequately protect records.
    - If possible, store log data on a different partition than the application and apply proper log rotation to log files (Systematically archive log files). This may not be possible in all the scenarios but is preferable. 

- Develop capabilities to grant access to audit data on a read-only basis for viewing and for report generation.

- Create and keep signatures of records, and verify them when accessing the records again.

- Maintain the original records, and make changes to the copies if the information is of high value.
    - Otherwise, log changes to audit data if modification is allowed.

__Note:__ NIST SP 800-92 (Guide to Computer Security Log Management) provides detailed information on how to design a secure log and auditing system. The following items are listed to protect logs and make a secure logging system:

- Restrict user access to log files (users usually need no more than append access privileges, if any).
- Avoid recording unneeded sensitive data.
- Protect log files by message digests, encryption, and physical protection.
- Limit the processes that generate the logs.
- Implement suitable responses to logging errors.
- Secure the communication channel used to send log data.
- Destroy old logs when not needed.

## Success Criteria

- The requirement "Protect audit information and logs against unauthorized access" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
