---
name: t1144-prevent-server-side-template-injection-ssti
description: Prevent Server-Side Template Injection (SSTI)
---

# T1144: Prevent Server-Side Template Injection (SSTI)

**Category:** CODE_FIX
**SD Elements:** [T1144](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T1144/)
**Priority:** P8

**Code to Fix:**
```python
# database.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in database.py:
# Prevent SSTI using the following techniques: - Use a safe Template engine that only allows white-list functions and are syntax safe. - Use the validation functions of the Template engine if it provides them. - Sandbox your Template engine inside a locked down container so that arbitrary code execute
```

**Success Criteria:**
- The control described by T1144 is enforced in database.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Documented
