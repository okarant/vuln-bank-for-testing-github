---
name: t4746-ensure-container-images-are-secure
description: Securing container images is crucial as they form the foundation of your containers, containing the code, runtime, system libraries, and settings necessary for your application to function. Ensuring these images are secure helps prevent vul
---

# T4746: Ensure container images are secure

**Category:** CODE_FIX  
**SD Elements:** [T4746](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T4746/)  
**Priority:** 10  
**Domain:** container-security

## Affected Areas in This Repository

See repository source files relevant to this control.

## Required Fix

Apply the secure pattern described by SD Elements guidance below.

## Implementation Guidance (SD Elements)

Securing container images is crucial as they form the foundation of your containers, containing the code, runtime, system libraries, and settings necessary for your application to function. Ensuring these images are secure helps prevent vulnerabilities from being introduced into your containerized applications. 

1. Use images from trusted repositories or create your own to avoid vulnerabilities from untrusted sources. This ensures that the images you use have been vetted for security issues. 
2. Regularly update your images to incorporate the latest security patches and updates. This step is essential to protect against newly discovered vulnerabilities. 
3. Employ image scanning tools to detect and fix vulnerabilities in your container images. These tools can identify common security flaws, allowing you to take corrective measures before deploying your containers. 

After implementing this countermeasure, your container images will be more secure, reducing the risk of vulnerabilities being introduced into your containerized applications.

## Success Criteria

- The control "Ensure container images are secure" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Pending
