---
name: t178-obtain-consent-from-users-prior-to-collecting-personal-info
description: Obtain consent from users prior to collecting personal information
---

# T178: Obtain consent from users prior to collecting personal information

**Category:** CODE_FIX
**SD Elements:** [T178](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T178/)
**Priority:** P10

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Implement a clear and transparent consent process to ensure compliance and build user trust. 1. **Review Privacy Impact Assessment (PIA):** Consult with your privacy officer to confirm that the information you are collecting requires consent. Update the PIA for future reference. 2. **Separate Consen
```

**Success Criteria:**
- The control described by T178 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
