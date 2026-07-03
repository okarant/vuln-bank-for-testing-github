---
name: encrypt-data-in-transit-tls
description: Ensure all sensitive data in transit uses a secure, modern TLS channel; use when fixing cleartext or weakly protected network communication (CWE-319 / P216).
---

# Ensure all data in transit is encrypted using a secure TLS channel

## What This Skill Does
This skill detects and replaces cleartext or weakly protected data-in-transit paths with secure, modern TLS usage. It helps enforce HTTPS/TLS for authentication and sensitive endpoints, harden TLS protocol and cipher settings, reject plaintext authentication, avoid protocol downgrades, and disable HTTP/TLS compression where secrets are present, reducing the risk of credential theft and traffic tampering.

## Decision Table
| Situation | Action |
|-----------|--------|
| Code sends credentials, tokens, or personal data over `http://`, raw `socket`/`net`/`socket.sendall` with no TLS | Replace with HTTPS/TLS client or wrap socket using a secure TLS context that enforces certificate validation |
| Server exposes login, token, or account endpoints over HTTP or accepts auth on non-secure requests | Enforce HTTPS-only for these routes and reject/redirect plaintext authentication attempts |
| TLS contexts or servers rely on default protocol versions (or allow SSLv3/TLS1.0/1.1) | Explicitly set minimum TLS version (e.g., TLS 1.2+) and restrict maximum to a modern version (e.g., TLS 1.3) |
| TLS configuration uses broad/legacy cipher lists or defaults with no ordering | Configure a curated modern cipher suite set, enable server cipher preference, and disable TLS compression |
| Dynamic responses include tokens/session IDs and are served with HTTP compression (gzip/br) | Disable HTTP compression (or skip compression middleware) for these responses and set headers to discourage intermediary compression |
| Code already uses HTTPS/TLS with modern versions, strong ciphers, cert validation, and no compression on secret-bearing responses | No action needed |

## Boundaries

### Can Do
- Identify and replace cleartext network calls (HTTP, raw sockets) carrying sensitive data with secure TLS-based equivalents.
- Configure TLS client/server contexts to enforce modern protocol versions, strong cipher suites, and disabled TLS-level compression.
- Add application-level checks to reject plaintext authentication and to avoid HTTP compression on secret-bearing responses.
- Use framework or language-standard libraries (e.g., Node.js `https`/`tls`, Python `ssl`) to apply these patterns consistently.

### Cannot Do
- Generate or manage real production certificates, private keys, or PKI infrastructure (can only reference paths or placeholders).
- Reconfigure external infrastructure (load balancers, CDNs, API gateways, service meshes) that is not represented in the codebase.
- Guarantee regulatory or compliance adherence (PCI, HIPAA, etc.); only improve technical transport security.
- Fix unrelated issues like password storage, authorization logic, or input validation (beyond transport concerns).

## Gotchas
- Assuming `https://` is enough: Failing to set `rejectUnauthorized` / certificate verification (or disabling it) leaves you open to MITM even over TLS.
- Leaving legacy protocols enabled: Not explicitly setting `minVersion` / `minimum_version` can allow SSLv3/TLS1.0/1.1 if platform defaults are weak.
- Compressing secrets: Keeping HTTP compression on for responses that include tokens, cookies, or other secrets can enable compression side-channel attacks.
- Trusting all proxy headers: Using `x-forwarded-proto` without restricting it to trusted proxies can let attackers spoof “https” and bypass plaintext-auth checks.

## Quick Verification
```bash
# 1) Confirm no cleartext credential paths
grep -RIn --exclude-dir=.git -E "http://|socket\.socket\(|net\.Socket\(" .

# 2) Scan TLS protocol and cipher support (replace host/port)
nmap --script ssl-enum-ciphers -p 443 your-app.example.com

# 3) Check that old TLS versions are rejected
openssl s_client -connect your-app.example.com:443 -tls1
openssl s_client -connect your-app.example.com:443 -tls1_1

# 4) Verify HTTPS-only auth (replace URL)
curl -v http://your-app.example.com/login -d 'u=a&p=b'
curl -v https://your-app.example.com/login -d 'u=a&p=b'

# 5) Verify no compression on secret-bearing responses
curl -v -H 'Accept-Encoding: gzip,br' https://your-app.example.com/secret-endpoint
```