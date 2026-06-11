# Test that sessions expire upon logout

**CM ID:** T31905-T93
**Classification:** CODE_FIX
**Domain:** authentication
**Priority:** 6

## Objective

Fix the existing security vulnerability: Test that sessions expire upon logout.

## Affected Files

- `auth.py` (lines: generate_token): JWT exp claim may be too long or missing

## Implementation Steps

1. Set appropriate JWT expiration time (e.g., 30 minutes)
2. Implement token refresh mechanism
3. Add session invalidation on logout
4. Implement idle timeout
5. Store session state server-side with secure token reference

## Verification

After implementing the fix:

1. Run the application test suite
2. Verify the specific vulnerability is addressed
3. Update the countermeasure status in SD Elements (Project 31905, T93)

## References

- SD Elements Project: 31905
- Countermeasure: T31905-T93
- Classification: CODE_FIX