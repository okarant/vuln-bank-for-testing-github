---
name: t20-generate-unique-session-ids-and-reset-old-ids-after-authenti
description: Generate unique session IDs and reset old IDs after authentication
---

# T20: Generate unique session IDs and reset old IDs after authentication

**Category:** CODE_FIX
**SD Elements:** [T20](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T20/)
**Priority:** P9

**Code to Fix:**
```python
# auth.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in auth.py:
# Protect against session-fixation attacks by using the following guidelines: - Generate a unique and random session identifier for each session. - Recognize only system-generated session IDs. - Regenerate the session ID after a user is successfully authenticated. - Regenerate the session ID after any
```

**Success Criteria:**
- The control described by T20 is enforced in auth.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
