---
name: t300-test-that-temporary-files-are-cleaned-up-after-the-resource
description: Test that the application cleans up temporary files by inspecting temporary directories belonging to the application or shared temporary folders used by the application: - Log in as various users. - Use the application. - Log out and check 
---

# T300: Test that temporary files are cleaned up after the resource is used

**Category:** CODE_FIX  
**SD Elements:** [T300](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T300/)  
**Priority:** 6  
**Domain:** file-handling

## Affected Areas in This Repository

app.py /upload_profile_picture and /upload_profile_picture_url (write to static/uploads)

## Required Fix

Validate file content/type (not just extension), store with randomized server-generated names outside the web root or with restricted execution, prevent path traversal/symlink following, and clean up temporary files.

## Implementation Guidance (SD Elements)

Test that the application cleans up temporary files by inspecting temporary directories belonging to the application or shared temporary folders used by the application:

- Log in as various users.
    - Use the application.
    - Log out and check if the temporary files are removed.

- Test if the expiry dates of temporary files are enforced by checking the time and date of the temporary files.
   
__Note__: A particular process may _create a large number of temporary files and create an opportunity to threaten the availability of the system_. It is helpful to identify those processes and concentrate the effort on testing them further.

## Success Criteria

- The control "Test that temporary files are cleaned up after the resource is used" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
