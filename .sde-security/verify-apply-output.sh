#!/usr/bin/env bash
# Independent, context-light apply verification (disk + tsv only; no file bodies).
set -u
fail=0
AGENTS=AGENTS.md
expected_total=$(find skills -path 'skills/*/*/SKILL.md' -type f | wc -l | tr -d ' ')
ledger_rows=$(grep -cE '^\| [A-Z]*T[0-9]' "$AGENTS")
terminal_rows=$(grep -E '^\| [A-Z]*T[0-9]' "$AGENTS" | grep -cE '\| (Applied|Documented|Skipped) \|')
# unique scoped CMs with terminal status
unique_terminal=$(grep -E '^\| [A-Z]*T[0-9]' "$AGENTS" | grep -E '\| (Applied|Documented|Skipped) \|' | awk -F'|' '{gsub(/ /,"",$2); print $2}' | sort -u | wc -l | tr -d ' ')
echo "expected_total(skill files)=$expected_total | ledger_rows=$ledger_rows | terminal_rows=$terminal_rows | unique_terminal_CMs=$unique_terminal"
[ "$ledger_rows" = "$expected_total" ] || { echo "VERIFY FAIL: ledger_rows != expected_total"; fail=1; }
[ "$terminal_rows" = "$expected_total" ] || { echo "VERIFY FAIL: terminal-status shortfall ($terminal_rows/$expected_total)"; fail=1; }
[ "$unique_terminal" = "8" ] || { echo "VERIFY FAIL: unique terminal CMs != 8"; fail=1; }
# Note run-marker coverage (file-tracked Applied/Documented CMs), from disk-recorded post-time markers
echo "--- note run-marker coverage (from note_posted.tsv) ---"
for cm in $(grep -E '^\| [A-Z]*T[0-9]' "$AGENTS" | grep -E '\| (Applied|Documented) \|' | awk -F'|' '{gsub(/ /,"",$2); print $2}'); do
  if grep -qE "^${cm}\b" .sde-security/apply/note_posted.tsv; then
    marker=$(grep -E "^${cm}\b" .sde-security/apply/note_posted.tsv | awk -F'\t' '{print $3}')
    echo "  $cm note-marker=$marker OK"
  else
    echo "  VERIFY FAIL: $cm Applied/Documented but no run-marker note recorded"; fail=1
  fi
done
# Surviving-source check for Applied CMs (from handoff)
echo "--- surviving-source check (Applied CMs) ---"
python3 - <<'PY'
import json,os,sys
h=json.load(open(".sde-apply-handoff.json")); bad=0
for c in h["countermeasures"]:
    if c["status"]!="Applied": continue
    if not c["files_modified"]:
        print(f"  VERIFY FAIL: Applied {c['id']} has no files_modified"); bad=1; continue
    for p in c["files_modified"]:
        if not os.path.exists(p): print(f"  VERIFY FAIL: {c['id']} file missing {p}"); bad=1
        elif p.startswith(("security/",".sde-security/")) or any(x in p for x in ("_secure.","_fixed.","_safe.","batch_")):
            print(f"  VERIFY FAIL: {c['id']} alt/scratch file {p}"); bad=1
        else: print(f"  {c['id']}: {p} OK")
sys.exit(1 if bad else 0)
PY
[ $? -eq 0 ] || fail=1
if [ "$fail" = "0" ]; then echo "VERIFY PASS"; else echo "VERIFY FAIL"; fi
exit $fail
