---
name: t4472-protect-large-language-models-against-supply-chain-vulnera
description: Protect Large Language Models against supply chain vulnerabilities (AI/ML Developer)
---

# T4472: Protect Large Language Models against supply chain vulnerabilities (AI/ML Developer)

**Category:** ML_CODE
**SD Elements:** [T4472](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T4472/)
**Priority:** P8

**Code to Fix:**
```python
# ai_agent_deepseek.py (review the handlers relevant to this control)
# The current implementation does not enforce the control described below.
```

**Required Fix:**
```python
# Apply the SD Elements guidance for this countermeasure in ai_agent_deepseek.py:
# To protect Large Language Models (LLMs) against supply chain vulnerabilities, ensure the following: - Use model and code signing to ensure authenticity when using external models and suppliers. - Update and patch all components regularly, including APIs and the underlying models.
```

**Success Criteria:**
- The control described by T4472 is enforced in ai_agent_deepseek.py and covered by a test.
- Manual review confirms the insecure pattern is no longer reachable.

**Status:** Pending
