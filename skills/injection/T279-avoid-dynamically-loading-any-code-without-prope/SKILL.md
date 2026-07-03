---
name: t279-avoid-dynamically-loading-any-code-without-proper-security
description: Avoid dynamically loading any code without proper security considerations
---

# T279: Avoid dynamically loading any code without proper security considerations

**Category:** CODE_FIX
**SD Elements:** [T279](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T279/)
**Priority:** P8

**Code to Fix:**
```python
# database.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in database.py:
# While dynamic loading of code is possible in some programming languages and frameworks like Java and Android, it is recommended that you avoid this capability as it increases the code complexity and makes your application dependent on an external resource. However, If you have to load any module dyn
```

**Success Criteria:**
- The control described by T279 is enforced in database.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Documented
