---
name: t129-test-for-reliance-on-file-name-or-extension-of-externally-s
description: Use the following guidelines to test if your application's upload feature relies on the name or extension of files acquired from external sources: 1. Inspect the application for file-upload functionality. 2. For every part of the site that 
---

# T129: Test for reliance on file name or extension of externally-supplied file

**Category:** CODE_FIX  
**SD Elements:** [T129](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T129/)  
**Priority:** 6  
**Domain:** file-handling

## Affected Areas in This Repository

app.py /upload_profile_picture and /upload_profile_picture_url (write to static/uploads)

## Required Fix

Validate file content/type (not just extension), store with randomized server-generated names outside the web root or with restricted execution, prevent path traversal/symlink following, and clean up temporary files.

## Implementation Guidance (SD Elements)

Use the following guidelines to test if your application's upload feature relies on the name or extension of files acquired from external sources:

1. Inspect the application for file-upload functionality.

2. For every part of the site that provides file upload, determine if there are restrictions on the file type. 

    If there are restrictions:

3. Save a file of one type with the extension of another type that can be uploaded to the application.
    - For example, if the application only allows users to upload JPEG images:
        - Create a new text file, but save the extension as ".jpg" rather than ".txt".
        
4. Upload the renamed file.

This test __fails__ if the application does not restrict the upload.

## Success Criteria

- The control "Test for reliance on file name or extension of externally-supplied file" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
