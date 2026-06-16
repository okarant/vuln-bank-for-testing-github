---
name: t2167-secure-file-storage
description: Before storing a file uploaded by a user, perform the following checks: - Check for the validity of a file name with a set of accepted characters. - Do not put files in "DocumentRoot". For example, If your Apache DocumentRoot points to Rail
---

# T2167: Secure file storage

**Category:** CODE_FIX  
**SD Elements:** [T2167](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T2167/)  
**Priority:** 6  
**Domain:** file-handling

## Affected Areas in This Repository

app.py /upload_profile_picture and /upload_profile_picture_url (write to static/uploads)

## Required Fix

Validate file content/type (not just extension), store with randomized server-generated names outside the web root or with restricted execution, prevent path traversal/symlink following, and clean up temporary files.

## Implementation Guidance (SD Elements)

Before storing a file uploaded by a user, perform the following checks:

- Check for the validity of a file name with a set of accepted characters.

- Do not put files in "DocumentRoot". For example, If your Apache DocumentRoot points to Rails' `/public` directory, do not put file uploads in it, and store files at least one level above it.

## Success Criteria

- The control "Secure file storage" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
