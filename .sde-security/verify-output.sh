#!/bin/bash
set -euo pipefail

REPO_ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$REPO_ROOT"

echo "=== SDE Security Plan Verification ==="
echo ""

PASS=0
FAIL=0

check() {
    if [ "$1" = "true" ]; then
        echo "  [PASS] $2"
        PASS=$((PASS + 1))
    else
        echo "  [FAIL] $2"
        FAIL=$((FAIL + 1))
    fi
}

echo "1. File Structure Checks"
check "$([ -f AGENTS.md ] && echo true || echo false)" "AGENTS.md exists"
check "$([ -f .sde-security/.sde-handoff.json ] && echo true || echo false)" ".sde-handoff.json exists"
check "$([ -f .sde-security/survey-evidence.md ] && echo true || echo false)" "survey-evidence.md exists"
check "$([ -f .sde-security/cm-work/classifications.json ] && echo true || echo false)" "classifications.json exists"
check "$([ -f .sde-security/cm-work/code-mappings.json ] && echo true || echo false)" "code-mappings.json exists"
check "$([ -d .sde-security/skills ] && echo true || echo false)" "skills directory exists"

echo ""
echo "2. Count Checks"
SKILL_COUNT=$(find .sde-security/skills -name "SKILL.md" | wc -l)
check "$([ "$SKILL_COUNT" -eq 69 ] && echo true || echo false)" "Skill file count = 69 (got: $SKILL_COUNT)"

DOMAIN_COUNT=$(find .sde-security/skills -maxdepth 1 -type d | wc -l)
DOMAIN_COUNT=$((DOMAIN_COUNT - 1))
check "$([ "$DOMAIN_COUNT" -eq 14 ] && echo true || echo false)" "Domain directory count = 14 (got: $DOMAIN_COUNT)"

echo ""
echo "3. Content Checks"
check "$(grep -q 'SDE-SECURITY-HARDENING:BEGIN' AGENTS.md && echo true || echo false)" "AGENTS.md has BEGIN marker"
check "$(grep -q 'SDE-SECURITY-HARDENING:END' AGENTS.md && echo true || echo false)" "AGENTS.md has END marker"

LEDGER_COUNT=$(grep -c '| pending |' AGENTS.md || true)
check "$([ "$LEDGER_COUNT" -eq 69 ] && echo true || echo false)" "Ledger entries = 69 (got: $LEDGER_COUNT)"

echo ""
echo "4. Handoff JSON Validation"
HANDOFF=".sde-security/.sde-handoff.json"
check "$(python3 -c "import json; json.load(open('$HANDOFF'))" 2>/dev/null && echo true || echo false)" "Handoff JSON is valid"
check "$(python3 -c "import json; d=json.load(open('$HANDOFF')); assert d['countermeasures']['total']==100" 2>/dev/null && echo true || echo false)" "Total CMs = 100"
check "$(python3 -c "import json; d=json.load(open('$HANDOFF')); assert d['verification']['count_match']==True" 2>/dev/null && echo true || echo false)" "Verification flags all True"

echo ""
echo "=== Results: $PASS passed, $FAIL failed ==="
if [ "$FAIL" -eq 0 ]; then
    echo "ALL CHECKS PASSED"
    exit 0
else
    echo "SOME CHECKS FAILED"
    exit 1
fi
