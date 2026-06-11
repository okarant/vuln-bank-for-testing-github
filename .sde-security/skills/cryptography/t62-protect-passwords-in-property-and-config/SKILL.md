# Protect passwords in property and configuration files

**CM ID:** T31905-T62
**Classification:** CODE_FIX
**Domain:** cryptography
**Priority:** 6

## Objective

Fix the existing security vulnerability: Protect passwords in property and configuration files.

## Affected Files

- `auth.py` (lines: 6): JWT_SECRET = "secret123" hardcoded
- `app.py` (lines: secret_key): app.secret_key = "secret123" hardcoded
- `docker-compose.yml` (lines: 11-16): DB_PASSWORD=postgres in plaintext

## Implementation Steps

1. Remove hardcoded JWT_SECRET from auth.py
2. Remove hardcoded app.secret_key from app.py
3. Move all secrets to environment variables
4. Use python-dotenv or similar for local development
5. Ensure .env is in .gitignore
6. Rotate all exposed secrets in production

## Verification

After implementing the fix:

1. Run the application test suite
2. Verify the specific vulnerability is addressed
3. Update the countermeasure status in SD Elements (Project 31905, T62)

## References

- SD Elements Project: 31905
- Countermeasure: T31905-T62
- Classification: CODE_FIX