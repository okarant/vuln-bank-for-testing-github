---
name: t587-verify-that-cryptographically-secure-algorithms-are-used-fo
description: Follow these steps to verify that secure, well-documented, and adequately tested random number generation algorithms are used in the source code: - Find all the instances of random generation. - Verify that secure random generator functions
---

# T587: Verify that cryptographically secure algorithms are used for random number generation

**Category:** CODE_FIX  
**SD Elements:** [T587](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T587/)  
**Priority:** 7  
**Domain:** crypto

## Affected Areas in This Repository

auth.py (HS256 with weak hardcoded secret), merchant_payments.py (`hashlib.sha256` over a 4-digit code for API keys), app.py (`random.randint` reset PIN)

## Required Fix

Use approved algorithms and key lengths, generate all tokens/PINs/keys with the `secrets` module, never use fast hashes for secrets, and protect data in transit with TLS.

## Implementation Guidance (SD Elements)

Follow these steps to verify that secure, well-documented, and adequately tested random number generation algorithms are used in the source code:

- Find all the instances of random generation.
- Verify that secure random generator functions and classes are used.
- List the random generation algorithms that are specified as the parameters to those function. It is usually better to use the default random generator, such as `SecureRandom()` in Java, than specifying a random generator algorithm that has not been adequately analyzed.
- Verify that those algorithms are secure, and the seeds are properly provided to the functions.

__Note__: The _SHA1PRNG_ algorithm that is widely used for random number generation is no longer considered cryptographically strong and should be avoided in critical applications.

## Success Criteria

- The control "Verify that cryptographically secure algorithms are used for random number generation" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
