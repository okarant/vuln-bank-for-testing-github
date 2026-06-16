---
name: t1919-use-json-web-token-jwt-securely
description: Secure [JSON Web Token (JWT)](/library/glossary/G112/) with JavaScript Object Signing and Encryption (JOSE). Use proper JOSE cryptographic function that serves your purpose: - **HMAC** (Hashed Message Authentication Code): is an efficient h
---

# T1919: Use JSON Web Token (JWT) securely

**Category:** CODE_FIX  
**SD Elements:** [T1919](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T1919/)  
**Priority:** 9  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Secure [JSON Web Token (JWT)](/library/glossary/G112/) with JavaScript Object Signing and Encryption  (JOSE). Use proper JOSE cryptographic function that serves your purpose:

- **HMAC** (Hashed Message Authentication Code): is an efficient hash that requires a **secret key** and provides authenticity as well as integrity.
- **Digital Signature**: is similar to HMAC but also adds cryptographic non-repudiation. It requires a **public/private key pair**, where the private key is used by the signer to create the signature and the public key is used by others to check if the signature is valid.
- **Authenticated Encryption**: adds confidentiality requirements to JWT as well as the authenticity and integrity requirements (just like HMAC). JOSE supports **public/private key**, **secret key** as well as **password-based** encryptions

Perform the following best practices with respect to each of the cryptographic functions:

## HMAC
Use HMAC with `HS256`, `HS384`, or `HS512` [JOSE algorithms](https://tools.ietf.org/html/rfc7518) for securing (preserving the authenticity and the integrity of) tokens and stateless session cookies. HMAC is different from digital signatures as it uses a shared secret key for its computation, which is usually shared out-of-band. Sharing the secret key used for HMAC will give the ability to the other party to create HMAC hash using the same key, which annuls the non-repudiation.

## Digital Signatures
Use digital signatures ([JSON Web Signature](https://tools.ietf.org/html/rfc7515)) where the authenticity and integrity of the claims must be verifiable by other parties and non-repudiations is important (i.e. no other party could have created the same digital signature but the one who posses the corresponding private key). Example use cases of JWT with digital signatures include identity tokens created by an OpenID provider, where the relying party must be able to verify the signature of the provider to make sure it is in fact issued by that provider. Another example is the access tokens issued by OAuth 2.0 server, where the resource server and/or the web API must be able to verify the signature before serving the request.

Digital signatures use public key (asymmetric) cryptography. The party generating the signature uses its private key to create it. Other parties use the public key of the generating party to verify the digital signature. As mentioned above, OpenID Connect servers use digital signatures for the JWT tokens. They also publish their public keys in a known URL in [JSON Web Key (JWK)](https://tools.ietf.org/html/rfc7517) format.

Choose the best [algorithm](https://tools.ietf.org/html/rfc7518) that suits your use-case:

- `RS256` and above (with 2048 or more key length) are based on **[RSA PKCS #1](https://tools.ietf.org/html/rfc8017)** and are widely used. They use little CPU cycles and are relatively fast to verify.
- `ES256` and above are based on **Elliptic Curve** cryptography, where you want to save in the space as opposed to time. Their keys and resulting signatures are much smaller than those of RSA-based ones but it takes longer to verify them.
- `Ed25519` and `Ed448` are based on **Edwards-curve DSA** cryptography and offer the best performance of signing and verifying among all algorithms. They are fairly new and may not be supported across the board.

## Authenticated Encryption
Use encryption when the confidentiality of claims needs to be protected. The examples are: the claims that contain Personally Identifiable data; ID tokens (OpenID Connect); and self-contained access tokens (OAuth 2.0). In this mode, the JWT payload would be encrypted using AES Algorithm and a secret AES key (also known as **Content Encryption Key - CEK**). The length of CEK depends on *enc* (encryption method) header (A128GCM, A192GCM, A256GCM, etc.).

CEK itself can be created and managed in different ways (specified by *alg* JWE header parameter):

- **[Direct Encryption with a Shared Symmetric Key (CEK)](https://tools.ietf.org/html/rfc7518#section-4.5)**:

    If the claims are internally consumed or the **secret key** has been shared out-of-band among the trusted parties, the shared secret key then can be directly used as CEK as follows:

    - Use *dir* (direct) as *alg* header (`alg: "dir"`).
    - An empty octet sequence is used as **JWE Encrypted Key** value.

- **[Key (CEK) wrapping using Secret/Private Key (Symmetric) cryptography (AES GCM)](https://tools.ietf.org/html/rfc7518#section-4.7)** and [Key Agreement with Elliptic Curve Diffie-Hellman Ephemeral Static (ECDH-ES)](https://tools.ietf.org/html/rfc7518#section-4.6):

    In this method, ECDH-ES algorithm is used for agreement on a key-encrypting key and the resulting key is used for encrypting CEK:

    - Use `alg: "ECDH-ES+A128KW"` or `alg: "ECDH-ES+A192KW"` or `alg: "ECDH-ES+A256KW"`.
    - **JWE Encrypted Key** value would be the encrypted value of CEK.

    The resulting key from ECDH can also be used directly as CEK if you put `alg: "ECDH-ES"` (similar to the previous point).

    For more details refer to [Key Agreement with Elliptic Curve Diffie-Hellman Ephemeral Static (ECDH-ES)](https://tools.ietf.org/html/rfc8037#section-3.2).

- **Key (CEK) encryption using Public Key (Asymmetric) cryptography**:

    This can be used when JWT sender and receiver have their own public/private keys. For example, OpenID providers usually share their public key (in [JWK format](https://tools.ietf.org/html/rfc7517)) at a public URL. They can then encrypt the CEK with their private key. The receiver, on the other hand, decrypts it with the OpenID provider's public key. 

    - Use `alg: "RSA1_5"` for encrypting CEK with [RSAES-PKCS1-v1_5](https://tools.ietf.org/html/rfc7518#section-4.2) or `alg: "RSA-OAEP-256"` for encrypting CEK with [RSAES using Optimal Asymmetric Encryption Padding (OAEP)](https://tools.ietf.org/html/rfc7518#section-4.3).
    - A key of size 2048 bits or larger MUST be used with these algorithms.

- **[Key (CEK) encryption using Password-based (PBES) cryptography](https://tools.ietf.org/html/rfc7518#section-4.8)**:

    This method is used whenever you want to use a passphrase or password to encrypt the JWT data. At first, a key-encryption key is derived from a user-supplied password using PBES2 schemes. Then the JWE CEK is encrypted using the derived key.

    - Use `alg: "PBES2-HS256+A128KW"` or `alg: "PBES2-HS384+A192KW"` or `alg: "PBES2-HS512+A256KW"` .

## Success Criteria

- The control "Use JSON Web Token (JWT) securely" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
