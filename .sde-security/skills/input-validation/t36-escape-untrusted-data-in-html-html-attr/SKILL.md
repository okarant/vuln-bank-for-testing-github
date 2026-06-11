# Escape untrusted data in HTML, HTML attributes, CSS, and JavaScript

**CM ID:** T31905-T36
**Classification:** CODE_FIX
**Domain:** input-validation
**Priority:** 8

## Objective

Fix the existing security vulnerability: Escape untrusted data in HTML, HTML attributes, CSS, and JavaScript.

## Affected Files

- `app.py` (lines: render_template calls): User input in templates without proper escaping

## Implementation Steps

1. Enable Jinja2 autoescape globally for all templates
2. Audit all render_template calls for unescaped variables
3. Use markupsafe.escape() for any dynamic content in responses
4. Add Content-Security-Policy header to restrict inline scripts
5. Test with XSS payloads in all user input fields

## Verification

After implementing the fix:

1. Run the application test suite
2. Verify the specific vulnerability is addressed
3. Update the countermeasure status in SD Elements (Project 31905, T36)

## References

- SD Elements Project: 31905
- Countermeasure: T31905-T36
- Classification: CODE_FIX