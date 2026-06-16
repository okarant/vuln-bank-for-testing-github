---
name: t595-test-that-your-application-checks-for-symlinks-before-openi
description: Use the following guidelines to test that your application checks for symlinks: - Find scenarios in which your application opens a file for reading or writing data. - Create a symlink at the expected location with the expected name, and lin
---

# T595: Test that your application checks for symlinks before opening files

**Category:** CODE_FIX  
**SD Elements:** [T595](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T595/)  
**Priority:** 6  
**Domain:** file-handling

## Affected Areas in This Repository

app.py /upload_profile_picture and /upload_profile_picture_url (write to static/uploads)

## Required Fix

Validate file content/type (not just extension), store with randomized server-generated names outside the web root or with restricted execution, prevent path traversal/symlink following, and clean up temporary files.

## Implementation Guidance (SD Elements)

Use the following guidelines to test that your application checks for symlinks:

- Find scenarios in which your application opens a file for reading or writing data.
- Create a symlink at the expected location with the expected name, and link it to a file outside the application realm.
- Test that your application detects the symlink and rejects opening it.
    - This test __fails__ if your application does not detect the symlink.

## Success Criteria

- The control "Test that your application checks for symlinks before opening files" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
