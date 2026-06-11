# Test for clickjacking

**CM ID:** T31905-T119
**Classification:** CODE_FIX
**Domain:** web-security
**Priority:** 7

## Objective

Fix the existing security vulnerability: Test for clickjacking.

## Affected Files

- `app.py` (lines: response headers): No X-Frame-Options or CSP frame-ancestors header

## Implementation Steps

1. Add X-Frame-Options: DENY header to all responses
2. Add Content-Security-Policy: frame-ancestors 'none' header
3. Create a Flask after_request handler to set security headers
4. Test that the application cannot be embedded in iframes

## Verification

After implementing the fix:

1. Run the application test suite
2. Verify the specific vulnerability is addressed
3. Update the countermeasure status in SD Elements (Project 31905, T119)

## References

- SD Elements Project: 31905
- Countermeasure: T31905-T119
- Classification: CODE_FIX