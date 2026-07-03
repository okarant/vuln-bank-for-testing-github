---
name: t754-enable-the-restriction-of-processing-personal-information-o
description: Enable the restriction of processing personal information of an individual for a specific purpose
---

# T754: Enable the restriction of processing personal information of an individual for a specific purpose

**Category:** CODE_FIX
**SD Elements:** [T754](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T754/)
**Priority:** P8

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# When [controllers](/library/glossary/G33/) delegate user-response responsibilities to [processors](/library/glossary/G34/), they must provide clear written instructions. Processors taking on this role must ensure that any functionality used to restrict personal data processing fully complies with th
```

**Success Criteria:**
- The control described by T754 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
