---
name: t60-use-correct-and-approved-cryptographic-algorithms-parameters
description: Use correct and approved cryptographic algorithms, parameters, and key lengths
---

# T60: Use correct and approved cryptographic algorithms, parameters, and key lengths

**Category:** CODE_FIX
**SD Elements:** [T60](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T60/)
**Priority:** P8

**Code to Fix:**
```python
# app.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in app.py:
# Strengthen cryptographic security by following these practices: 1. **Use well-tested and industry-accepted cryptographic algorithms**: Always choose algorithms that are recognized and validated by industry standards, such as those listed in the [FIPS 140-3 validation list](https://csrc.nist.gov/proj
```

**Success Criteria:**
- The control described by T60 is enforced in app.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
