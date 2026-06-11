# Test that default accounts are disabled or default passwords are changed

**CM ID:** T31905-T323
**Classification:** CODE_FIX
**Domain:** cryptography
**Priority:** 9

## Objective

Fix the existing security vulnerability: Test that default accounts are disabled or default passwords are changed.

## Affected Files

- `docker-compose.yml` (lines: 11-16): Default postgres/postgres credentials
- `app.py` (lines: secret_key): Hardcoded secret_key = "secret123"

## Implementation Steps

1. Change default PostgreSQL credentials in docker-compose.yml
2. Generate unique credentials per environment
3. Remove or change hardcoded secret_key in app.py
4. Document required credential setup in deployment guide
5. Add startup check to reject default credentials

## Verification

After implementing the fix:

1. Run the application test suite
2. Verify the specific vulnerability is addressed
3. Update the countermeasure status in SD Elements (Project 31905, T323)

## References

- SD Elements Project: 31905
- Countermeasure: T31905-T323
- Classification: CODE_FIX