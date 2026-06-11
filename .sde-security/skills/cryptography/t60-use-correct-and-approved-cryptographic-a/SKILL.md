# Use correct and approved cryptographic algorithms, parameters, and key lengths

**CM ID:** T31905-T60
**Classification:** CODE_FIX
**Domain:** cryptography
**Priority:** 8

## Objective

Fix the existing security vulnerability: Use correct and approved cryptographic algorithms, parameters, and key lengths.

## Affected Files

- `auth.py` (lines: 7): ALGORITHMS = ["HS256", "none"] allows none algorithm
- `auth.py` (lines: 6): Weak JWT secret "secret123"

## Implementation Steps

1. Remove 'none' from ALGORITHMS list in auth.py
2. Use only HS256 or stronger (RS256) for JWT signing
3. Generate a cryptographically secure JWT secret (minimum 256 bits)
4. Store the secret securely using environment variables
5. Implement key rotation mechanism
6. Verify all tokens are validated with proper algorithm enforcement

## Verification

After implementing the fix:

1. Run the application test suite
2. Verify the specific vulnerability is addressed
3. Update the countermeasure status in SD Elements (Project 31905, T60)

## References

- SD Elements Project: 31905
- Countermeasure: T31905-T60
- Classification: CODE_FIX