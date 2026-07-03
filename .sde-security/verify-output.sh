#!/usr/bin/env bash
# Independent, disk-only verification for generate-security-skill-files output.
set -u
cd "$(dirname "$0")/.." || exit 2
EXPECTED_SKILL_FILES=8
EXPECTED_FILE_TRACKED=8
FAIL=""

files=$(find skills -name SKILL.md | wc -l | tr -d ' ')
[ "$files" = "$EXPECTED_SKILL_FILES" ] || FAIL="$FAIL skill_files($files!=$EXPECTED_SKILL_FILES)"

rows=$(grep -cE '^\| P?T[0-9]' AGENTS.md)
[ "$rows" = "$EXPECTED_SKILL_FILES" ] || FAIL="$FAIL ledger_rows($rows!=$EXPECTED_SKILL_FILES)"

uniq=$(find skills -name SKILL.md -path "*/*T[0-9]*-*/*" | sed -E 's|.*/(P?T[0-9]+)-.*|\1|' | sort -u | wc -l | tr -d ' ')
[ "$uniq" = "$EXPECTED_FILE_TRACKED" ] || FAIL="$FAIL unique_cm_ids($uniq!=$EXPECTED_FILE_TRACKED)"

lookups=$(ls .sde-security/library-lookup/*.json 2>/dev/null | wc -l | tr -d ' ')
[ "$lookups" = "$EXPECTED_FILE_TRACKED" ] || FAIL="$FAIL library_lookups($lookups!=$EXPECTED_FILE_TRACKED)"

cmwork=$(ls .sde-security/cm-work/*.json 2>/dev/null | wc -l | tr -d ' ')
[ "$cmwork" = "$EXPECTED_SKILL_FILES" ] || FAIL="$FAIL cm_work($cmwork!=$EXPECTED_SKILL_FILES)"

audit=$(python3 -c "import json;print(len(json.load(open('.sde-handoff.json'))['library_lookup_audit']))")
[ "$audit" = "$EXPECTED_FILE_TRACKED" ] || FAIL="$FAIL audit_len($audit!=$EXPECTED_FILE_TRACKED)"

sf=$(python3 -c "import json;print(len(json.load(open('.sde-handoff.json'))['skill_files']))")
[ "$sf" = "$EXPECTED_SKILL_FILES" ] || FAIL="$FAIL handoff_skill_files($sf!=$EXPECTED_SKILL_FILES)"

# library file fidelity: written char-count >= source amendment char-count
check_fidelity () { # $1 path  $2 source_len
  local n; n=$(wc -m < "$1" | tr -d ' ')
  [ "$n" -ge "$2" ] || FAIL="$FAIL fidelity($1:$n<$2)"
}
check_fidelity skills/xss/T36-javascript/SKILL.md 3673
check_fidelity skills/secrets/T76-python/SKILL.md 3112
check_fidelity skills/llm-security/T4457-python/SKILL.md 5530
check_fidelity skills/transport-security/T21-python/SKILL.md 4390

# placeholder scan on TEMPLATE files only (exclude LIBRARY: files per AGENTS.md stamps)
LIBFILES=$(grep -oE 'skills/[^ |]+/SKILL.md' AGENTS.md | while read p; do grep -qF "| $p |" AGENTS.md && grep -F "$p" AGENTS.md | grep -q 'LIBRARY:' && echo "$p"; done)
for f in $(find skills -name SKILL.md); do
  echo "$LIBFILES" | grep -qxF "$f" && continue
  if grep -qE '\{ID\}|\{Title\}|\{file_path\}|\{current_code\}|\{secure_code_pattern\}|\{who/what|TODO:' "$f"; then
    FAIL="$FAIL placeholder($f)"
  fi
done

if [ -n "$FAIL" ]; then
  echo "VERIFY FAIL:$FAIL"
  exit 1
fi
echo "VERIFY PASS"
exit 0
