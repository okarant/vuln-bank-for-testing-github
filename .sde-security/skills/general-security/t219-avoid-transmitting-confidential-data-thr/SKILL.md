# Avoid transmitting confidential data through URL parameters

**CM ID:** T31905-T219
**Classification:** CODE_FIX
**Domain:** general-security
**Priority:** 6

## Objective

Fix the existing security vulnerability: Avoid transmitting confidential data through URL parameters.

## Affected Files

- `app.py` (lines: token handling): JWT token potentially passed in URL query params

## Implementation Steps

1. Ensure JWT tokens are only sent in Authorization headers
2. Remove any token passing via URL query parameters
3. Add server-side check to reject tokens in URLs
4. Configure logging to not capture URL parameters
5. Add Referrer-Policy header to prevent token leakage

## Verification

After implementing the fix:

1. Run the application test suite
2. Verify the specific vulnerability is addressed
3. Update the countermeasure status in SD Elements (Project 31905, T219)

## References

- SD Elements Project: 31905
- Countermeasure: T31905-T219
- Classification: CODE_FIX