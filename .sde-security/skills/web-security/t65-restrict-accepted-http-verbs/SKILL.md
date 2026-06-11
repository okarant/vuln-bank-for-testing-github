# Restrict accepted HTTP verbs

**CM ID:** T31905-T65
**Classification:** CODE_FIX
**Domain:** web-security
**Priority:** 6

## Objective

Fix the existing security vulnerability: Restrict accepted HTTP verbs.

## Affected Files

- `app.py` (lines: route decorators): Routes without explicit methods= restriction

## Implementation Steps

1. Audit all Flask route decorators for explicit methods= parameter
2. Add methods=['GET'] or methods=['POST'] as appropriate to each route
3. Reject unexpected HTTP methods with 405 Method Not Allowed
4. Test all endpoints with various HTTP methods

## Verification

After implementing the fix:

1. Run the application test suite
2. Verify the specific vulnerability is addressed
3. Update the countermeasure status in SD Elements (Project 31905, T65)

## References

- SD Elements Project: 31905
- Countermeasure: T31905-T65
- Classification: CODE_FIX