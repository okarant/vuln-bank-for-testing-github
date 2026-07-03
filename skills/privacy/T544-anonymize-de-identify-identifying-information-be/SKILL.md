---
name: t544-anonymize-de-identify-identifying-information-before-using
description: Anonymize (de-identify) identifying information before using it for a secondary purpose
---

# T544: Anonymize (de-identify) identifying information before using it for a secondary purpose

**Category:** CODE_FIX
**SD Elements:** [T544](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T544/)
**Priority:** P8

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Anonymize personally identifiable information that can be linked to an individual when the information is intended to be used for secondary purposes. If you are a [controller](/library/glossary/G33/) delegating this job to [processors](/library/glossary/G34/), provide them with written anonymization
```

**Success Criteria:**
- The control described by T544 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
