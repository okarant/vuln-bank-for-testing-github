---
name: t2665-protect-sensitive-data-at-rest-with-encryption
description: Database servers should use file system encryption, which is performed at the operating system level. Examples include FDE (Full Disk Encryption) in Linux or BitLocker in Windows. Additionally: - If your database provides integrated at-rest
---

# T2665: Protect sensitive data at rest with encryption

**Category:** INFRA  
**SD Elements:** [T2665](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2665/)  
**Priority:** 8  
**Domain:** crypto

## Affected Areas in This Repository

auth.py (HS256 with weak hardcoded secret), merchant_payments.py (`hashlib.sha256` over a 4-digit code for API keys), app.py (`random.randint` reset PIN)

## Why Not Directly Code-Fixable in This Repository

Use approved algorithms and key lengths, generate all tokens/PINs/keys with the `secrets` module, never use fast hashes for secrets, and protect data in transit with TLS.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Database servers should use file system encryption, which is performed at the operating system level. Examples include FDE (Full Disk Encryption) in Linux or BitLocker in Windows. 

Additionally:
- If your database provides integrated at-rest data encryption (such as TDE, or Transparent Data Encryption), this feature should be enabled.
- If your database does not provide integrated at-rest encryption, review your organization's security policy and compliance requirements to determine if file system encryption is sufficient. A development-time mitigation is to use application-side encryption on specific fields, but this increases complexity and can cause vulnerabilities related to key management. Other options include using trusted database extensions or platform services that can provide at-rest database encryption.

## Success Criteria

- The requirement "Protect sensitive data at rest with encryption" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
