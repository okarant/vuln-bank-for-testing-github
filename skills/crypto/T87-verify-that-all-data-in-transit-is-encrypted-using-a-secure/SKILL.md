---
name: t87-verify-that-all-data-in-transit-is-encrypted-using-a-secure
description: Use a network monitoring tool to ensure that data in transit is sent over a secure TLS channel: - Use a tool such as Wireshark or Ethereal. Focus on testing the authentication and post-authenticated processes. This test __fails__ if any of 
---

# T87: Verify that all data in transit is encrypted using a secure TLS channel

**Category:** INFRA  
**SD Elements:** [T87](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T87/)  
**Priority:** 8  
**Domain:** crypto

## Affected Areas in This Repository

auth.py (HS256 with weak hardcoded secret), merchant_payments.py (`hashlib.sha256` over a 4-digit code for API keys), app.py (`random.randint` reset PIN)

## Why Not Directly Code-Fixable in This Repository

Use approved algorithms and key lengths, generate all tokens/PINs/keys with the `secrets` module, never use fast hashes for secrets, and protect data in transit with TLS.

**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.

## Implementation Guidance (SD Elements)

Use a network monitoring tool to ensure that data in transit is sent over a secure TLS channel:

- Use a tool such as Wireshark or Ethereal. Focus on testing the authentication and post-authenticated processes. This test __fails__ if any of the network traffic transmits clear text data.

Attempt to connect to all SSL/TLS enabled interfaces (all available IP/Port). For each connection:

- This test __fails__ if SSLv1, SSLv2, or SSLv3 are offered as negotiable protocols.

- List all available ciphers:
    - If any NULL, or EXT (Export) ciphers are available, then the test __fails__.
    - The server must explicitly disallow EXPORT ciphers (which are weak ciphers) even if the client does not request it.

- This test __fails__ if any DES ciphers are offered.

- This test __fails__ if TLS Compression is enabled/offered.
    - This is due to the CRIME side channel attack vulnerability (compression ratio info-leak made easy, see [CRIME Attack Vector](/library/glossary/G10/)).

- Offer multiple ciphers to a server and check if it picks the more secure ciphers over less secure ones.
    - Specifically, verify that the server uses __SHA384/SHA256 instead of SHA1__, and __SHA2 family of ciphers instead of MD5-based ciphers__.

- Require WSS for WebSocket and HTTPS for SSE channels, with mixed-content rejection and modern TLS/certificate validation.

## Success Criteria

- The requirement "Verify that all data in transit is encrypted using a secure TLS channel" is documented with an owner and an infrastructure/process plan.

**Status:** Pending
