# Prevent prompt injection in Large Language Models (MLOps Engineer)

**CM ID:** T31905-T4456
**Classification:** CODE_FIX
**Domain:** ai-ml
**Priority:** 7

## Objective

Fix the existing security vulnerability: Prevent prompt injection in Large Language Models (MLOps Engineer).

## Affected Files

- `ai_agent_deepseek.py` (lines: 15-30): System prompt explicitly allows instruction override
- `ai_agent_deepseek.py` (lines: 47-60): User input passed directly to LLM without sanitization

## Implementation Steps

1. Remove instruction-override allowances from system prompt
2. Implement input sanitization for user messages before LLM processing
3. Add system prompt integrity checks
4. Implement output validation to detect injection artifacts
5. Add guardrails to prevent role/behavior changes via user input
6. Test with known prompt injection payloads

## Verification

After implementing the fix:

1. Run the application test suite
2. Verify the specific vulnerability is addressed
3. Update the countermeasure status in SD Elements (Project 31905, T4456)

## References

- SD Elements Project: 31905
- Countermeasure: T31905-T4456
- Classification: CODE_FIX