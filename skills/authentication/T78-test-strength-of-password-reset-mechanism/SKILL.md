---
name: t78-test-strength-of-password-reset-mechanism
description: Use the following guidelines for testing the forgotten password feature of a web application: __1. Try to enter an invalid username 10 times in a row.__ - The test __fails__ if either of the following happens: - No CAPTCHA or anti-automatio
---

# T78: Test strength of password reset mechanism

**Category:** CODE_FIX  
**SD Elements:** [T78](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T78/)  
**Priority:** 9  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Use the following guidelines for testing the forgotten password feature of a web application:

__1. Try to enter an invalid username 10 times in a row.__

- The test __fails__ if either of the following happens:
    - No CAPTCHA or anti-automation techniques are used. 
    - Further attempts are not prevented. 

- This feature is vulnerable to __user enumeration__.

__2. Try to request an email to reset your password.__

- This test __fails__ if the email contains a plaintext password.
    - Passwords transmitted in clear text are visible to anyone who can access the message.

__3. Try to answer any forgotten password questions incorrectly 10 times.__ 

- The test __fails__ if either of the following happens:
    - No CAPTCHA or anti-automation techniques are used.
    - Further attempts are not prevented.

- This feature is vulnerable to __brute-forcing__.

__4. Try to answer security questions.__

- The test __fails__ if either of the following happens:
    - The questions are user-generated or easy to guess ("What high school did you go to?" or "What was the color of your first car?"). 
    - The security questions are accessible without following a link from an email.

- This feature is vulnerable to __guess attacks__.

__5. If the application uses cookies when submitting a username, try to submit a valid and an invalid username, then examine the returned cookies.__

- This test __fails__ if the structure or length of the two cookies are different.

- This feature is vulnerable because it __does not adequately protect account information__.

## Success Criteria

- The control "Test strength of password reset mechanism" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
