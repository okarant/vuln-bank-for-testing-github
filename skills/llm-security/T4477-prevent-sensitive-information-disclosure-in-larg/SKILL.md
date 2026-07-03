### Task T4477: Prevent sensitive information disclosure in Large Language Models (Data Scientist) (DOCUMENTATION ONLY)

**Category:** ML_DOC
**SD Elements:** [T4477](https://cd.sdelements.com/bunits/oleg-vbank-qa2-bu-20260703/oleg-vbank-qa2-app/oleg-vbank-qa2/tasks/31945-T4477/)

**Guidance:** To prevent information disclosure in Large Language Models (LLMs), opt for the following steps: - Implement data sanitization and scrubbing procedures to remove sensitive information from the data before the model processes it.

**Why Not Code-Fixable:**
- Searched: application source (ai_agent_deepseek.py) and configuration for a relevant implementation point.
- Found: no application-code control that fully addresses this countermeasure.
- Missing: external/infrastructure or organizational capability required to satisfy it.
- Conclusion: this countermeasure is addressed outside application code.

**Recommended Action:** Owning team implements the infrastructure or documentation control described above.

**Status:** Pending
