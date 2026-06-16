---
name: t295-avoid-storing-unencrypted-confidential-data-without-access
description: Consider the following guidelines for saving confidential data on mobile/client devices or in shared locations on the server: - Generally there are two types of confidential data that you may identify: 1. Application's secrets such as keys,
---

# T295: Avoid storing unencrypted confidential data without access control mechanisms

**Category:** CODE_FIX  
**SD Elements:** [T295](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T295/)  
**Priority:** 7  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Consider the following guidelines for saving confidential data on mobile/client devices or in shared locations on the server:

- Generally there are two types of confidential data that you may identify:
    1. Application's secrets such as keys, proprietary data and other information that belongs to you (usually shared among all instances of the application)
    2. User-specific sensitive data

- Encrypt all these sensitive data before writing them into files on storage. Never use shared storage for storing unencrypted sensitive data that you don't want to be accessible by other processes.
    - You can implement wrappers for data storage and retrieval functions in order to make the encryption and decryption transparent. The major benefit of these wrappers is their ability to transparently encrypt/decrypt data. For example, your application can read or write a normal stream without knowing about the underlying cryptography. This can be most helpful when adding encryption into an existing application, as it would not require changes beyond wrapping the stream functions.

- Encrypt these sensitive data before writing storing them in the local databases.
    - For mobile devices, these platform databases could be accessible on rooted or jail-broken ROMs. Therefore your application's secrets may be accessed by a hacker that owns the device.

- Use a secure key storage mechanism (such as keystores or keychains) for storing keys, certificates, and/or passwords.

Examples of applications that need to store sensitive information are a browser that saves user passwords locally, or an offline password management solution.

### Serialized objects

Do not store serialized objects with fields that contain confidential data, in an unencrypted format. Data in serialized objects is easy to extract and read without additional protection such as encryption.

## Success Criteria

- The control "Avoid storing unencrypted confidential data without access control mechanisms" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
