---
name: secure-password-reset-mechanism
description: Harden password-reset flows against token abuse, username enumeration, weak questions, and stale sessions; use when fixing Weak Password Reset Mechanism for Forgotten Passwords (P526)
---

# Secure the password reset mechanism

## What This Skill Does
Hardens password reset flows so attackers cannot enumerate valid users, forge or reuse reset tokens, bypass security questions, or keep access through old sessions after a password change. It focuses on generic responses, strong token lifecycle, safe security questions with lockout, optional session invalidation, and non-leaky confirmation emails.

## Decision Table
| Situation | Action |
|-----------|--------|
| Password reset initiation distinguishes between existing and non-existing usernames via messages, cookies, HTTP status, or timing | Make the endpoint always return generic responses and structurally similar cookies/headers, and add basic anti-automation (rate limiting/CAPTCHA) |
| Reset tokens are deterministic, long-lived, stored in plaintext, or reusable | Replace with cryptographically strong, random tokens; store only a hash; enforce strict TTL and one-time use during validation |
| Reset link handling returns different errors for invalid/expired tokens or locked accounts | Return a single generic error/status and atomically invalidate tokens that are expired, reused, or tied to locked accounts |
| Security questions are free‑form, OSINT‑friendly, compared in plaintext, or have no lockout | Restrict to a vetted question set, store normalized hashed answers, compare with timing‑safe equality, and enforce lockout after repeated failures (while keeping behavior indistinguishable for nonexistent users) |
| After reset, existing sessions remain valid with no user control | Add a session version or revocation flag checked on every authenticated request and bump it on reset when the user chooses “log out of all devices” |
| Password change confirmation email includes secrets or reveals whether an account exists | Send a generic, non-secret email (no password, no full reset URL) with wording independent of initiation path and without confirming account existence to unauthenticated parties |

## Boundaries

### Can Do
- Normalize and harden password reset initiation so it is generic, rate-limited, and non‑enumerating.
- Introduce or refactor reset token handling to use strong randomness, hashing, TTLs, and one-time use.
- Strengthen security questions and lockout logic (including no-email variants) and keep flows indistinguishable for invalid usernames.
- Add server-side session invalidation via a session version or similar attribute tied to password resets.
- Refine password change confirmation emails so they notify users without leaking secrets or confirming existence.

### Cannot Do
- Cannot design or integrate full UI/UX flows (email templates, front-end screens) beyond backend-safe patterns.
- Cannot retrofit complex third‑party auth/IdP providers that hide or abstract the reset flow; can only suggest configuration patterns.
- Cannot guarantee compliance with all regulatory or corporate policies (e.g., retention, logging, MFA rules) without human review.

## Gotchas
- Treating token invalidation as a separate step: If token validation and invalidation are not atomic, a token might be reused in parallel requests. Always mark tokens used (or delete them) inside the same validation transaction.
- Using different error messages or HTTP status codes for “expired”, “invalid”, and “locked account” tokens: This leaks state and supports enumeration; keep responses generic and log details server-side only.
- Forgetting to check session version on every authenticated request: Bumping a version at reset time is useless unless all session checks enforce it; ensure middleware consistently validates it before granting access.

## Quick Verification
```bash
# 1. Username enumeration
# Call reset-init with existing and non-existing usernames; diff responses:
curl -i -X POST http://localhost:3000/password-reset -d 'username=alice' \
  | sed 's/\(reset_ctx=\)[^;]*/\1<redacted>/'
curl -i -X POST http://localhost:3000/password-reset -d 'username=nonexistent' \
  | sed 's/\(reset_ctx=\)[^;]*/\1<redacted>/'

# 2. Token one-time use and expiry
# Use a valid reset token twice; second call must fail with the same generic error:
curl -X POST http://localhost:3000/password-reset/confirm -d "token=$TOKEN&newPassword=p1"
curl -X POST http://localhost:3000/password-reset/confirm -d "token=$TOKEN&newPassword=p2"

# 3. Security question lockout
# Submit wrong answers until the lockout threshold is exceeded and confirm further attempts fail:
node -e 'const mod=require("./app_fix_gpt51_code"); for(let i=0;i<5;i++) console.log(mod.validateSecurityAnswerNoEmail({username:"alice",answer:"wrong"}));'

# 4. Session invalidation
# After a reset with terminateSessions=true, ensure old tokens (old version) are rejected:
node -e 'const m=require("./app_fix_gpt51_code"); console.log(m.completePasswordReset({token:"<valid>",newPassword:"x",terminateSessions:true}));'

# 5. Email contents
# Inspect sentMails (or your mail logs) and verify no passwords or full reset URLs are present:
node -e 'const m=require("./app_fix_gpt51_code"); console.log(m.sentMails);'
```