---
name: t394-secure-one-time-passwords-otp
description: When generating OTPs, follow these guidelines to ensure their security: #### OTP Generation - Use a **secure random number generator** for making OTPs. - Consult the documentation for the random function that you use. - Avoid predictable or
---

# T394: Secure one-time passwords (OTP)

**Category:** CODE_FIX  
**SD Elements:** [T394](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T394/)  
**Priority:** 7  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

When generating OTPs, follow these guidelines to ensure their security:

#### OTP Generation
- Use a **secure random number generator** for making OTPs.
  - Consult the documentation for the random function that you use.
  - Avoid predictable or weak random number generators.

- Implement __Time-based OTP (TOTP)__ [RFC 6238](https://datatracker.ietf.org/doc/html/rfc6238)
 or __HMAC-based OTP (HOTP)__ [RFC 4226](https://datatracker.ietf.org/doc/html/rfc4226).
  - If neither option is available, use a **secure, non-reversible hash function** (e.g., SHA-2).

- Restrict the **validity period** of the OTP to the shortest reasonable duration.
  - Recommended validity: 5 minutes (in rare cases, up to an hour or a day).

- Ensure OTPs are at least 6-8 digits numeric code for SMS/email-based delivery or longer (16+ alphanumeric characters) if used in apps.

- Ensure OTPs are **single-use** and **invalidate immediately after first use**.

####OTP Storage
- **Do not store OTPs** in databases unless absolutely necessary.
  - If storage is needed, store only a **hashed version** (using HMAC with a secure key).

- **Use rate-limiting and retry limits** to prevent brute-force attacks:
  - Limit the number of OTP entry attempts** per user or IP address within a defined time frame (e.g., 5 attempts per minute).
  - Define the maximum number of incorrect OTP entries allowed before taking additional security measures.

#### OTP Transmission
- Use secure communication channels:
  - **TLS** for internet-based delivery.
  - **End-to-end encryption** for app-based OTPs.
  - **Avoid SMS-based OTPs** when possible due to interception risks (SIM swapping, SS7 attacks).

- **Mask OTPs in logs** and avoid exposing them in cleartext.

By following these best practices, you ensure OTP security against replay attacks, brute-force attempts, and interception threats.

## Success Criteria

- The control "Secure one-time passwords (OTP)" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
