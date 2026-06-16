---
name: t50-use-indirect-object-reference-maps-if-accessing-files
description: Always use indirect references for accessing a specific object, such as a database record or a file. This practice prevents IDOR (Insecure Direct Object Reference) attacks. Direct object references use a direct ID such as an actual file nam
---

# T50: Use indirect object reference maps if accessing files

**Category:** CODE_FIX  
**SD Elements:** [T50](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T50/)  
**Priority:** 8  
**Domain:** authorization

## Affected Areas in This Repository

app.py (IDOR: /check_balance, /transfer, /api/virtual-cards/<id>/*, /api/bill-payments accept account/card/user identifiers without verifying ownership), transaction_graphql.py (_resolve_scope), auth.py (token_required)

## Required Fix

Enforce server-side, deny-by-default authorization on every object access: verify the authenticated principal owns or is permitted the requested resource before acting. Centralize authorization checks and apply least privilege.

## Implementation Guidance (SD Elements)

Always use indirect references for accessing a specific object, such as a database record or a file. This practice prevents IDOR (Insecure Direct Object Reference) attacks.

Direct object references use a direct ID such as an actual file name like `"file=statement1.pdf"` in the URL parameters. Alternatively, indirect object references provide a separate identifier that the application later translates into an actual ID, such as `"file=a"`, where `'a'` is later translated to `'statement1.pdf'`.

Direct object references introduce a weakness that allows attackers to change the URL and access objects that should be off limits, such as `"file=../config.xml"`. An indirect object reference makes this attack impossible because the application can only provide access to a certain set of objects, such as all files in a particular directory or a predefined list of individual database records.

This control applies specifically to resources that require access control. Publicly accessible static content that is normally stored on web servers does not necessarily need this protection.

If direct object references must be facilitated, such as a filename, restrict the path to a single directory and ensure that users cannot escape out of that directory. Use a combination of allowlist validation on the filename and operating system access controls to enforce this. For example, a user should not be able to access: `"../../sensitive_folder/sensitive.file"`.

As an additional layer of defense, the object ID values should be random and unguessable. For example, UUID. This makes it harder for potential attackers to exploit any exposed instances of this vulnerability.

## Success Criteria

- The control "Use indirect object reference maps if accessing files" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
