---
name: t175-test-that-the-client-validates-digital-certificates
description: Use the following test to determine whether a server properly performs certificate validation (verification of the chain of trust), revocation-status verification, and subject authentication: - Create an X509 certificate, such as an OpenSSL
---

# T175: Test that the client validates digital certificates

**Category:** INFRA  
**SD Elements:** [T175](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T175/)  
**Priority:** 7  
**Domain:** crypto

## Affected Areas in This Repository

auth.py (HS256 with weak hardcoded secret), merchant_payments.py (`hashlib.sha256` over a 4-digit code for API keys), app.py (`random.randint` reset PIN)

## Why Not Directly Code-Fixable in This Repository

Use approved algorithms and key lengths, generate all tokens/PINs/keys with the `secrets` module, never use fast hashes for secrets, and protect data in transit with TLS.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Use the following test to determine whether a server properly performs certificate validation (verification of the chain of trust), revocation-status verification, and subject authentication:

- Create an X509 certificate, such as an OpenSSL package, that is self-signed and not signed by a recognized certificate authority without defining the root as trusted on the server.

- Create a certificate with an expired date.

- Create a certificate with a key pair that its public key is not configured on the server.

- Create a certificate and include it in the certificate revocation list on the server.
    - Or use another method by which the server checks the certificate revocation status such as OCSP.

- Create a certificate with a subject that is not defined as a valid user on the server.

Use the above certificates (as client certificates) and attempt to connect to the server and authenticate.
    
    - This test __fails__ if authentication is successful in any of the cases above.

In addition, create a valid certificate and try to log into the system.

This test __fails__ if the latency introduced by the authentication unit is not tolerable for the system.

## Black-box testing

In black-box testing, you will need to use a proxy to replace the destination's TLS/SSL certificate.

1. Set up a proxy that can intercept TLS/SSL traffic by decoding the TLS/SSL. 
    - For example, the Burp Suite or Charles proxies.

2. Set the proxy to listen in on the access point, and enable TLS/SSL decoding using self-signed certificate replacement.

3. Set the client to use the proxy by choosing the access point and the port to be used.

4. If the client does not support proxies:
    - You can use a proxifier to redirect traffic through the setup proxy.
    - Or you set up transparent proxy mode and force network traffic by setting the proxy on the routing gateway of the network.

5. This test fails if the application continues to operate without giving errors and all functions continue working. 

6. Check the TLS/SSL connections logged in the proxy.
    - This test __fails__ if the connections are fully established, and data is being sent.
    - Otherwise, this test passes.

## Resources

- [Burp Suite](https://portswigger.net/burp/)
- [Charles](https://www.charlesproxy.com/documentation/)

## Success Criteria

- The requirement "Test that the client validates digital certificates" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
