---
name: t186-use-recommended-settings-and-the-latest-patches-for-third-p
description: Use recommended settings and the latest patches for third party libraries and software
---

# T186: Use recommended settings and the latest patches for third party libraries and software

**Category:** CODE_FIX
**SD Elements:** [T186](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T186/)
**Priority:** P10

**Code to Fix:**
```text
# requirements.txt (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```text
# Apply the SD Elements guidance for this countermeasure in requirements.txt:
# Regularly reviewing and addressing the security vulnerabilities reported for third party software will decrease the risk of a compromise. For any third party libraries or software being used in the system: - Upgrade to the latest version, or apply the latest security patches. - Look for documentatio
```

**Success Criteria:**
- The control described by T186 is enforced in requirements.txt and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
