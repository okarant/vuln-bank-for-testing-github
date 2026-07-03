---
name: t42-avoid-relying-on-untrusted-data-for-server-side-selection
description: Avoid relying on untrusted data for server-side selection
---

# T42: Avoid relying on untrusted data for server-side selection

**Category:** CODE_FIX
**SD Elements:** [T42](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T42/)
**Priority:** P10

**Code to Fix:**
```python
# database.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in database.py:
# Do not use untrusted data such as user-supplied settings for the selection of a page, view, or template on the server side. These settings may allow the user to run code on the server side, or access server-side files. Validate all input using a strict whitelist that only allows certain input, such 
```

**Success Criteria:**
- The control described by T42 is enforced in database.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Documented
