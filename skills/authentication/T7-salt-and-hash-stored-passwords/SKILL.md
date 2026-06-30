---
name: salt-and-hash-stored-passwords
description: Securely salt and hash stored passwords using strong, unique salts and slow KDFs; use when passwords or long-lived credentials are stored or verified and simple/weak hashing is detected.
---

# Salt and hash stored passwords

## What This Skill Does
Replaces plaintext or weakly hashed password storage with secure, salted, slow password hashing. It enforces high-entropy random salts, per-password salt uniqueness, modern password hashing/KDFs (e.g., PBKDF2-HMAC-SHA256, bcrypt, Argon2), and sufficient work factors so stolen password databases are hard to crack.

## Decision Table
| Situation | Action |
|-----------|--------|
| Passwords are stored in plaintext or reversible encryption | Replace with salted, slow one-way password hashing (PBKDF2/bcrypt/Argon2) and remove plaintext/reversible storage |
| Code uses `md5`, `sha1`, single-round `sha256`, or username/email-based salts | Replace with PBKDF2-HMAC-SHA256 (or bcrypt/Argon2) using `crypto.randomBytes`-generated salts and a high iteration/cost factor |
| Same salt reused for multiple users or derived from predictable data (username, user ID, constants) | Introduce per-password, CSPRNG-generated salts and store each salt alongside its hash in the user record |
| Password hashing parameters (iterations/cost/memory) are hard-coded in multiple places | Centralize configuration (one config object/module) and use it for both hashing and verification; store parameters needed for verification with each record |
| Code already uses PBKDF2/bcrypt/Argon2 with random per-password salts and adequate work factor | No action needed beyond periodic review of parameters and algorithm versioning/migration |

## Boundaries

### Can Do
- Detect and replace weak password hashing patterns (plaintext, fast hashes, predictable salts) with secure salted KDFs.
- Introduce per-password, high-entropy salts using a cryptographically secure RNG and store them correctly with hashes.
- Centralize and enforce password hashing configuration (algorithm, iterations/cost, salt length, key length).
- Add constant-time comparison for password verification to avoid timing leaks.
- Preserve existing function signatures by delegating to a secure internal implementation while fixing the underlying cryptography.

### Cannot Do
- Recover or “fix” already-compromised passwords; it can only improve future storage and verification.
- Decide regulatory or policy-specific parameter values (e.g., exact iteration count for your hardware/compliance); it can only suggest sane minimums.
- Replace or refactor external authentication systems (OAuth, SSO, IDaaS) that you do not control.
- Guarantee defense against extremely weak user-chosen passwords; password hashing mitigates cracking, not poor password selection.
- Implement language- or framework-specific migrations for every stack; examples are primarily Node.js/JavaScript, but concepts must be adapted per environment.

## Gotchas
- Using usernames/emails as salts: Predictable, low-entropy salts allow precomputation and correlation of hashes. Always use `crypto.randomBytes` (or equivalent CSPRNG) to generate salts, and never derive them from user identifiers or static strings.
- Single, global salt for all passwords: A shared salt only slightly slows attackers; it does not prevent them from cracking many hashes at once. Always use a unique salt per stored password and store it alongside the hash.
- Fast hash with iterations too low: Using PBKDF2/bcrypt/Argon2 with an iteration/cost factor that is too small (e.g., <1000 PBKDF2 iterations) leaves passwords easy to brute-force. Choose parameters so each hash takes a noticeable but acceptable amount of time (on the order of tens to hundreds of milliseconds) and store cost parameters with each record.
- Dropping or regenerating salts during verification: If verification regenerates a new salt instead of reusing the stored one, hashes will never match and security assumptions break. Always read and reuse the original salt and parameters during verification.
- Comparing hashes with `===` only: Direct string comparison can leak timing information. Use constant-time comparison (`crypto.timingSafeEqual` or equivalent) for verifying password hashes.

## Quick Verification
```bash
# 1) Search for weak password hashing patterns
grep -R --line-number -E "createHash\('sha1'|\bmd5\b|plaintext_password|password\s*=" .

# 2) Search for predictable or reused salts (username-/email-based, static prefixes)
grep -R --line-number -E "SALT_|salt.*username|username.*salt|email.*salt" .

# 3) Run unit tests or a small script to ensure:
#    - Two hashes of the same password produce different salts and hashes.
#    - Verification succeeds only for the correct password.

node - <<'EOF'
const { hashPassword, loginUser, registerUser } = require('./app_fix_original_code.js');

(async () => {
  const p = 'TestPassword123!';
  const r1 = hashPassword(p);
  const r2 = hashPassword(p);
  console.log('Different salts:', r1.salt !== r2.salt);
  console.log('Different hashes:', r1.hash !== r2.hash);

  registerUser('alice', p);
  console.log('Verify correct:', loginUser('alice', p));
  console.log('Verify wrong:', loginUser('alice', 'wrong'));
})();
EOF
```