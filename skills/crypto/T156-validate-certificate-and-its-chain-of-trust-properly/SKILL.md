---
name: t156-validate-certificate-and-its-chain-of-trust-properly
description: Validate all certificates and their chains of trust, such as X509 certificates. Any application using __SSL__ or __public key infrastructure (PKI)__ based authentication must do the following at the very least: * Follow the chain of trust f
---

# T156: Validate certificate and its chain of trust properly

**Category:** INFRA  
**SD Elements:** [T156](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T156/)  
**Priority:** 7  
**Domain:** crypto

## Affected Areas in This Repository

auth.py (HS256 with weak hardcoded secret), merchant_payments.py (`hashlib.sha256` over a 4-digit code for API keys), app.py (`random.randint` reset PIN)

## Why Not Directly Code-Fixable in This Repository

Use approved algorithms and key lengths, generate all tokens/PINs/keys with the `secrets` module, never use fast hashes for secrets, and protect data in transit with TLS.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Validate all certificates and their chains of trust, such as X509 certificates. Any application using __SSL__ or __public key infrastructure (PKI)__ based authentication must do the following at the very least:

 * Follow the chain of trust for certificate validation.
    * Verify that each node in the chain has a valid certificate by itself and has the authority to sign the child certificate.

 * Validate host specific data of certificates to make sure it matches the expected destination.
    * For instance, make sure the Common Name matches the expected value.

 * Validate the expiry date of the certificate.

 * Check certificate revocation.
    * Use certificate revocation lists (CRLs) or online certificate status protocol (OCSP).
 
 * Re-check certificate revocation periodically after the initial revocation check. 
    * You can do this by either:
        * Re-checking the revocation list for every connection (avoid caching).
        * Setting the cache to expire after a period of time (one week, or 24 hours in more security-sensitive environments).
 
 * Do not accept or initiate SSL connections for which the certificate misses one or more of the validation steps above.

__Note__: Authentication/SSL systems should be designed and implemented in a way that certificate validation, revocation status verification, and user authentication do not impose impeding latency on the system.

Libraries like OpenSSL or operating system interfaces might automatically perform certificate validation.

 * Ensure you review the specifications of the specific SSL library/interface and make sure that proper settings/parameters are used to activate all the checks listed above.

 * Handle all potential warnings and errors that might arise from any of these checks failing.

 * Use the latest versions of your library and check for vulnerabilities in the specific version of the library/interface that you are using that might be used to bypass the validation process.

As the number of certificate authorities grows, there is more and more risk associated with certificates. Forging valid certificates by compromised signing authorities and social engineering for impersonation during the certificate issuing process are becoming increasingly common. To reduce the risk associated with certificate-based trusting you may wish to include the following additional measures:

 * Only use reputable signing authorities for your own certificates.

 * Ensure that clients validate the specific signing authority your organization uses.
    * For example, by hard-coding and checking the fingerprint of the signing authorities.
 
 * Only use Extended Validation (EV) certificates and limit accepted certificates to EV certificates on the client side.

## Success Criteria

- The requirement "Validate certificate and its chain of trust properly" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
