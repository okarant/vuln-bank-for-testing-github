#!/usr/bin/env bash
# Independent apply-output verification (disk-only, context-light).
# Scope for THIS run: domain=injection. Generated at runtime from this run's data.
set -u
cd "$(dirname "$0")/.."
AGENTS=AGENTS.md
FAIL=0

# --- Scope definition ---
SCOPED_CMS="CT435 T38 T1365 T279 T1144 T29 T36 T37 T42"
APPLIED_CMS="CT435 T38 T1365"     # files_modified surviving-source check
# scoped_file_total = number of skill FILES/ledger rows belonging to scoped CMs (injection = 9, all single-file)
SCOPED_FILE_TOTAL=9
SCOPED_TOTAL=9                    # unique scoped CMs

# --- Structural invariant: expected_total == ledger rows == SKILL.md files on disk ---
LEDGER_ROWS=$(grep -cE '^\| [A-Z]*T[0-9]' "$AGENTS")
SKILL_FILES=$(find skills -path 'skills/*/*/SKILL.md' | wc -l | tr -d ' ')
echo "expected_total: ledger rows [A-Z]*T grep = $LEDGER_ROWS | SKILL.md files on disk = $SKILL_FILES"
if [ "$LEDGER_ROWS" -ne "$SKILL_FILES" ]; then echo "VERIFY FAIL: ledger rows != SKILL.md files"; FAIL=1; fi
# regression (b): CT435 (custom CT#) must be counted by the [A-Z]*T grep
if ! grep -E '^\| [A-Z]*T[0-9]' "$AGENTS" | grep -q '^\| CT435 '; then echo "VERIFY FAIL: CT435 not counted by [A-Z]*T grep"; FAIL=1; fi

# --- Terminal-status ledger rows for the SCOPED CMs (regression a: anchor on scoped_file_total, NOT expected_total) ---
TERM_SCOPED=0
for cm in $SCOPED_CMS; do
  st=$(grep -E "^\| $cm " "$AGENTS" | awk -F'|' '{print $7}' | tr -d ' ')
  case "$st" in
    Applied|Documented|Skipped) TERM_SCOPED=$((TERM_SCOPED+1));;
    *) echo "VERIFY FAIL: scoped CM $cm not terminal (status=$st)"; FAIL=1;;
  esac
done
echo "terminal-status ledger rows for scoped CMs = $TERM_SCOPED (scoped_file_total = $SCOPED_FILE_TOTAL)"
if [ "$TERM_SCOPED" -ne "$SCOPED_FILE_TOTAL" ]; then echo "VERIFY FAIL: terminal-status shortfall (scoped)"; FAIL=1; fi
# NOTE: asserting against expected_total ($LEDGER_ROWS=83) here would FALSE-FAIL on this narrowed scope.

# --- SDE note coverage (scoped CMs only), proven via this-run markers recorded to disk ---
for cm in $SCOPED_CMS; do
  nc=$(awk -F'\t' -v c="$cm" '$1==c{print $2}' .sde-security/apply/note_counts_injection.tsv)
  mk=$(awk -F'\t' -v c="$cm" '$1==c{print $3}' .sde-security/apply/note_posted.tsv | tail -1)
  if [ -z "$nc" ] || [ "$nc" -lt 1 ] 2>/dev/null; then echo "VERIFY FAIL: $cm note_count<1"; FAIL=1; fi
  if [ -z "$mk" ]; then echo "VERIFY FAIL: $cm no this-run marker recorded"; FAIL=1; fi
done
echo "note coverage: all scoped CMs have note_count>=1 + this-run marker"

# --- Surviving-source check for Applied CMs ---
for f in app.py auth.py; do
  [ -f "$f" ] || { echo "VERIFY FAIL: applied source $f missing"; FAIL=1; }
  case "$f" in *_secure.*|*_fixed.*|*_safe.*|batch_*) echo "VERIFY FAIL: alt file $f"; FAIL=1;; esac
done
echo "surviving-source: Applied CM fix files (app.py, auth.py) exist and are real source"

if [ "$FAIL" -eq 0 ]; then echo "VERIFY PASS"; exit 0; else echo "VERIFY FAIL"; exit 1; fi
