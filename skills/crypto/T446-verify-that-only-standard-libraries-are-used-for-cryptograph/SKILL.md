---
name: t446-verify-that-only-standard-libraries-are-used-for-cryptograp
description: Use the following guidelines for verifying that you only use standard libraries for cryptography: - Create a list of libraries used for cryptography, including: - Encryption - Signature generation/verification - Key generation - Message dig
---

# T446: Verify that only standard libraries are used for cryptography

**Category:** CODE_FIX  
**SD Elements:** [T446](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T446/)  
**Priority:** 8  
**Domain:** crypto

## Affected Areas in This Repository

auth.py (HS256 with weak hardcoded secret), merchant_payments.py (`hashlib.sha256` over a 4-digit code for API keys), app.py (`random.randint` reset PIN)

## Required Fix

Use approved algorithms and key lengths, generate all tokens/PINs/keys with the `secrets` module, never use fast hashes for secrets, and protect data in transit with TLS.

## Implementation Guidance (SD Elements)

Use the following guidelines for verifying that you only use standard libraries for cryptography:

- Create a list of libraries used for cryptography, including:
    - Encryption
    - Signature generation/verification
    - Key generation
    - Message digest generation

- Verify that only standard libraries are used, and no outstanding vulnerabilities are reported for those libraries.

## Success Criteria

- The control "Verify that only standard libraries are used for cryptography" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
