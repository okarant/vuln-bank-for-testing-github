---
name: t151-use-cryptographically-secure-random-numbers
description: Only use cryptographically secure random numbers for security purposes. For example, session ID numbers must be random numbers or strings that cannot be guessed by attackers. Most programming languages come with simple random number tools, 
---

# T151: Use cryptographically secure random numbers

**Category:** CODE_FIX  
**SD Elements:** [T151](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T151/)  
**Priority:** 7  
**Domain:** crypto

## Affected Areas in This Repository

auth.py (HS256 with weak hardcoded secret), merchant_payments.py (`hashlib.sha256` over a 4-digit code for API keys), app.py (`random.randint` reset PIN)

## Required Fix

Use approved algorithms and key lengths, generate all tokens/PINs/keys with the `secrets` module, never use fast hashes for secrets, and protect data in transit with TLS.

## Implementation Guidance (SD Elements)

Only use cryptographically secure random numbers for security purposes. For example, session ID numbers must be random numbers or strings that cannot be guessed by attackers.

Most programming languages come with simple random number tools, such as rand() in C, which don't have enough entropy. In many cases, these Pseudo Random Number Generators (PRNGs) use a predictable value to seed a predictable sequence of random numbers, such as the system time. 

Use methods for the generation of cryptographic keys and other material (such as IVs), which have entropy that meets the minimum effective strength requirements of the cryptographic primitives and keys

Provide sufficient entropy in related processes, where cryptographic keys are generated through processes that require direct user interaction, such as through the entry of a passphrase or the use of __random__ user interaction with the software. Specifically:

 - Enforce an input domain that is able to provide sufficient entropy for any methods used for generating keys directly from a password/passphrase , so that the total possible inputs are at least equal to that of the equivalent bit strength of the key being generated (e.g., a 32-hex-digit input field for an AES128 key).

- Make sure that a work factor of at least 10,000 is applied where the passphrase is passed through an industry-standard key-derivation function, such as PBKDF2 or bcrypt, which extends the work factor for any attempt to brute-force the passphrase value. 

Most programming languages also provide cryptographically secure random number generators, which have passed security tests for pseudo-randomness. For example, the SecureRandom class in Java or Microsoft CryptoAPI. Use these libraries instead.

A typical case of using cryptographically secure random number generators could be generating v4 GUIDs. Details are mentioned in the additional requirement **ASVS Requirements - GUID v4 algorithm.** 

**Note**: The SHA1PRNG algorithm that is widely used for random number generation is no longer considered cryptographically strong and should be avoided in critical applications.

### ASVS Requirements - GUID v4 algorithm

Use a GUID v4 algorithm and a cryptographically-secure pseudo-random number generator (CSPRNG) to generate random globally unique identifiers (GUIDs), also known as universally unique identifiers (UUIDs). 

Since the GUID v4 is not cryptographically secure, it is recommended to use a CSPRNG to achieve both uniqueness and cryptographically secure pseudo-randomness. CSPRNGs are designed to meet the strict requirements for security and randomness, including unpredictability, resistance to tampering, and non-repeatability.

##References
[Recommendation for Random Number Generation Using Deterministic Random Bit Generators](https://csrc.nist.gov/publications/detail/sp/800-90a/rev-1/final)

## Success Criteria

- The control "Use cryptographically secure random numbers" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
