### Task T4458: Prevent prompt injection in Large Language Models (Data Scientist) (DOCUMENTATION ONLY)

**Category:** ML_DOC
**SD Elements:** [T4458](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T4458/)

**Guidance:** To protect your Large Language Models (LLM) against prompt injection attacks, use the following strategy: - Avoid insecure functions that could be exploited through the LLM and use secure alternatives wherever possible.

**Why Not Code-Fixable:**
- Searched: application source (ai_agent_deepseek.py) and configuration for a relevant implementation point.
- Found: no application-code control that fully addresses this countermeasure.
- Missing: external/infrastructure or organizational capability required to satisfy it.
- Conclusion: this countermeasure is addressed outside application code.

**Recommended Action:** Owning team implements the infrastructure or documentation control described above.

**Status:** Pending
