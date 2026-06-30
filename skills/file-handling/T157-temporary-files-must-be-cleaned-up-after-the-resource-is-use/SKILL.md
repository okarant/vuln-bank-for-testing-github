---
name: t157-temporary-files-must-be-cleaned-up-after-the-resource-is-us
description: Use a process, such as the one described below, to remove all temporary files that may contain confidential or integral data after use: * Group session files, or user specific files together. * Put user specific files in a folder whose name
---

# T157: Temporary files must be cleaned up after the resource is used

**Category:** CODE_FIX  
**SD Elements:** [T157](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T157/)  
**Priority:** 6  
**Domain:** file-handling

## Affected Areas in This Repository

app.py /upload_profile_picture and /upload_profile_picture_url (write to static/uploads)

## Required Fix

Validate file content/type (not just extension), store with randomized server-generated names outside the web root or with restricted execution, prevent path traversal/symlink following, and clean up temporary files.

## Implementation Guidance (SD Elements)

Use a process, such as the one described below, to remove all temporary files that may contain confidential or integral data after use:

* Group session files, or user specific files together.
    * Put user specific files in a folder whose name contains the session ID, or username/userID if session IDs are not being used. 
    * For example, `tmp/<appname>/sess_<session_id>/\*`.
 
* When a user logs out, remove the files grouped for that session/user.
    * Initiate the removal process immediately.
    * Do not rely on a server to respond to the logout request.

* Prepare a policy/convention that assigns an expiry period to each type of temporary file. 
    * One approach is to use the name and path to determine the expiry time.
    * For example, all files in `tmp/<appname>/sess_\*/\*` have a 10 minute expiry period, and files in `tmp/<appname>/media_cache/*` have a 12 hour expiry period.

* Provide an explicit check to ensure that the application is actually removing temporary files according to policy.
    * For example, implement a temporary file watchdog thread that iterates all temporary files and checks them every 10 minutes.
    * The file watchdog will then remove files whose last access timestamp has expired according to the expiration policy.

## Success Criteria

- The control "Temporary files must be cleaned up after the resource is used" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
