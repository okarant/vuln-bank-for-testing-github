---
name: t338-control-access-to-resources-through-user-authentication-and
description: Use the following guidelines for controlling access to resources with user authentication and authorization: - Implement a user authentication/authorization system that enforces access control policies. - Users include human, software proce
---

# T338: Control access to resources through user authentication and authorization

**Category:** CODE_FIX  
**SD Elements:** [T338](https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404/tasks/31909-T338/)  
**Priority:** 7  
**Domain:** authentication

## Affected Areas in This Repository

auth.py (hardcoded JWT_SECRET='secret123', ALGORITHMS includes 'none', verify_token falls back to verify_signature:false), app.py (forgot/reset use random.randint for the reset PIN, default admin/admin123 seeded in database.py), merchant_payments.py (predictable 4-digit-derived API key)

## Required Fix

Load the JWT secret from a secret store/env var, restrict algorithms to a single strong symmetric/asymmetric alg (remove 'none' and the no-verify fallback), generate reset PINs/API keys with `secrets`, enforce account lockout/throttling, and remove all default/seeded credentials.

## Implementation Guidance (SD Elements)

Use the following guidelines for controlling access to resources with user authentication and authorization:

- Implement a user authentication/authorization system that enforces access control policies.
    - Users include human, software process, or device.
    - A typical authentication/authorization system identifies and authenticates users, and assigns roles to them.
    - It also checks user permissions when a request is made to access a resource, such as a piece of information, service, or page.

- Require additional levels of authentication (e.g., enable multi-factor authentication) when performing critical requests that involve [sensitive/personal information](/library/glossary/G8/).

-  Make sure that interfaces and pages that require authentication have easy access to logout functionality.
-  Make sure unique identification and authentication of each service, program, or system attempting to access critical assets is required, where interfaces, such as APIs, allow for automated access to critical assets.
-  Protect the authentication mechanisms, where identification is supplied across a non-console interface.

- While there are many access control models, Role Based Access Control (RBAC) is one of the most common models for typical applications.
    - For more information on access control models, especially RBAC, see this [FAQ from NIST](http://csrc.nist.gov/groups/SNS/rbac/faq.html).
- Restrict by default all access to critical assets to only those accounts and services that require access.

**Note:** Authorize a user or process acting on behalf of the user to publish **publicly accessible content**. Ensure information available to the general public, without identification and authentication, does not contain nonpublic content.

### Prevent untrusted parties from accessing admin interfaces in applications

Use the following guidelines for preventing untrusted parties from accessing administrative interfaces:

-Restrict non-admin users from accessing information or features they do not need.

-Use secure interface elements for making certain features or information visible or invisible and editable or uneditable for non-admin users based on their needs. 

-Restrict admin areas from being accessible from a single IP. Consider keeping the admin interface on a private subnet and off the public internet.

-Use second level authentication and consider using client SSL certificates for accessing admin areas. 

-Only allow access from trusted domains and IPs. This can be done by adding a check to a basic HTTP pipeline or by blocking untrusted IPs in access configuration files.

-Reissue the session ticket when moving between admin and normal users.

### Authorization, MDS2-2013

The answers to these questions are directly affected by the characteristics of the chosen authorization/authentication system:

- 3-1 Can the device prevent access to unauthorized users through user login requirements or other mechanism?

     - Other mechanisms may include use of smart cards, password-generating-tokens, device-specific certificates (e.g. PKI authentication of users/devices), etc. Note that in order to effectively prevent unauthorized access to resources you should complete the authentication/authorization related security tasks that are linked to this section in the compliance regulation report.
 
- 3-2	Can users be assigned different privilege levels within an application based on 'roles' (e.g., guests, regular users, power users, administrators, etc.)?

     - This is affected by the authorization model that is adopted. If you are using an RBAC model, the answer is yes.

## Success Criteria

- The control "Control access to resources through user authentication and authorization" is implemented in the affected source files listed above.
- The fix is applied in-place to the original files (no `*_secure.*` copies).
- A test or manual check confirms the vulnerability is no longer exploitable.

**Status:** Applied
