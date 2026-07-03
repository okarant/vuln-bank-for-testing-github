---
name: t66-prevent-web-pages-from-being-loaded-inside-iframe
description: Prevent web pages from being loaded inside iFrame
---

# T66: Prevent web pages from being loaded inside iFrame

**Category:** CODE_FIX
**SD Elements:** [T66](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T66/)
**Priority:** P7

**Code to Fix:**
```python
# transaction_graphql.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in transaction_graphql.py:
# Do not allow your application to be loaded in an `iframe` unless you need that functionality. Different strategies can be applied to deny framing. 1. Instruct the browser to prevent framing using HTTP response headers (`X-Frame-Options` and `Content Security Policy`). __This is a current best practi
```

**Success Criteria:**
- The control described by T66 is enforced in transaction_graphql.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
