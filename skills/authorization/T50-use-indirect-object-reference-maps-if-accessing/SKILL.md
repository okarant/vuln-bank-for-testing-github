---
name: t50-use-indirect-object-reference-maps-if-accessing-files
description: Use indirect object reference maps if accessing files
---

# T50: Use indirect object reference maps if accessing files

**Category:** CODE_FIX
**SD Elements:** [T50](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T50/)
**Priority:** P8

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Always use indirect references for accessing a specific object, such as a database record or a file. This practice prevents IDOR (Insecure Direct Object Reference) attacks. Direct object references use a direct ID such as an actual file name like `"file=statement1.pdf"` in the URL parameters. Altern
```

**Success Criteria:**
- The control described by T50 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
