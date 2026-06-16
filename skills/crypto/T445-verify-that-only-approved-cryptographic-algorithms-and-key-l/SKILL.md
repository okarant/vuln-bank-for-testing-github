---
name: t445-verify-that-only-approved-cryptographic-algorithms-and-key
description: Use the following guidelines for verifying that you only use approved cryptographic algorithms and key lengths: - List all the cryptographic algorithms and key lengths used by developers in the application. - Verify that they are validated 
---

# T445: Verify that only approved cryptographic algorithms and key lengths are used

**Category:** CODE_FIX  
**SD Elements:** [T445](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T445/)  
**Priority:** 8  
**Domain:** crypto

## Affected Areas in This Repository

auth.py (HS256 with weak hardcoded secret), merchant_payments.py (`hashlib.sha256` over a 4-digit code for API keys), app.py (`random.randint` reset PIN)

## Required Fix

Use approved algorithms and key lengths, generate all tokens/PINs/keys with the `secrets` module, never use fast hashes for secrets, and protect data in transit with TLS.

## Implementation Guidance (SD Elements)

Use the following guidelines for verifying that you only use approved cryptographic algorithms and key lengths:

- List all the cryptographic algorithms and key lengths used by developers in the application.
    - Verify that they are validated to be secure and reliable.

- Check the algorithms against the [FIPS 140-3 validation list](https://csrc.nist.gov/projects/cryptographic-module-validation-program). [Annex A Section 14](https://csrc.nist.gov/CSRC/media/Projects/cryptographic-module-validation-program/documents/fips%20140-3/Draft%20FIPS-140-3-CMVP%20Management%20Manual%2009-18-2020.pdf) provides a list of approved security algorithms applicable to FIPS 140-3.

- Check that the initialization vectors (IVs) are randomized securely for cipher-block chaining (CBC) and other algorithms.

- Check that encryption is performed in CBC mode instead of Electronic Codebook (ECB) mode, which encrypts separate blocks of input.
    - Unless there is a justification for not using CBC.

## Success Criteria

- The control "Verify that only approved cryptographic algorithms and key lengths are used" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
