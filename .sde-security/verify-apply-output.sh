#!/usr/bin/env bash
# Independent, disk-only verification for the apply-security-fixes run
# (scope=domain=authentication, project 31909). Counts via grep/python; never
# reads task/file bodies into the model context.
set -u
REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO" || exit 2
AGENTS="AGENTS.md"
AUDIT=".sde-security/apply/audit_records.json"
NOTES=".sde-security/apply/note_posted.tsv"
SCOPED_TOTAL=30
fail=0

echo "Repo: $REPO"

# 1) Ledger terminal-status rows for authentication
applied=$(grep -cE '^\| T[0-9]+ .*authentication/.*\| Applied \|' "$AGENTS")
documented=$(grep -cE '^\| T[0-9]+ .*authentication/.*\| Documented \|' "$AGENTS")
skipped=$(grep -cE '^\| T[0-9]+ .*authentication/.*\| Skipped \|' "$AGENTS")
pending=$(grep -cE '^\| T[0-9]+ .*authentication/.*\| Pending \|' "$AGENTS")
terminal=$((applied + documented + skipped))
echo "Ledger(auth): Applied=$applied Documented=$documented Skipped=$skipped Pending=$pending Terminal=$terminal"
if [ "$terminal" -ne "$SCOPED_TOTAL" ]; then echo "VERIFY FAIL: terminal-status shortfall ($terminal != $SCOPED_TOTAL)"; fail=1; fi
if [ "$pending" -ne 0 ]; then echo "VERIFY FAIL: $pending authentication CMs still Pending"; fail=1; fi

# 2) One ledger row per authentication SKILL.md file on disk
files_on_disk=$(find skills/authentication -mindepth 2 -name SKILL.md | wc -l | tr -d ' ')
ledger_rows=$(grep -cE '^\| T[0-9]+ .*authentication/.*SKILL.md' "$AGENTS")
echo "auth SKILL.md files on disk=$files_on_disk ; ledger rows=$ledger_rows"
if [ "$files_on_disk" -ne "$SCOPED_TOTAL" ] || [ "$ledger_rows" -ne "$SCOPED_TOTAL" ]; then
  echo "VERIFY FAIL: file/ledger count mismatch vs scoped_total=$SCOPED_TOTAL"; fail=1; fi

# 3) Per-scoped-CM checks via python (terminal ledger status, run-marker note, surviving source)
python3 - "$AUDIT" "$NOTES" "$AGENTS" <<'PY'
import json, os, re, sys
audit_path, notes_path, agents_path = sys.argv[1], sys.argv[2], sys.argv[3]
audit = json.load(open(audit_path))
agents = open(agents_path).read()
notes = {}
for line in open(notes_path):
    parts = line.rstrip("\n").split("\t")
    if len(parts) >= 3:
        notes[parts[0]] = (parts[1], parts[2])
bad = 0
ALT = re.compile(r'(_secure\.|_fixed\.|_safe\.|/batch_)')
for r in audit:
    cid, status, files = r["id"], r["status"], r["files_modified"]
    # terminal ledger status present for this CM in an authentication row
    rowpat = re.compile(r'^\| %s \|.*authentication/.*\| (Applied|Documented|Skipped) \|' % re.escape(cid), re.M)
    if not rowpat.search(agents):
        print(f"VERIFY FAIL: {cid} has no terminal authentication ledger row"); bad = 1
    # run-marker note recorded this run
    marker, result = notes.get(cid, (None, None))
    want = "[AI-Applied]" if status == "Applied" else "[AI-Documented]"
    if marker != want or result != "ADDED":
        print(f"VERIFY FAIL: {cid} missing run-marker note ({marker}/{result}, expected {want}/ADDED)"); bad = 1
    # surviving-source check for Applied CMs
    if status == "Applied":
        if not files:
            print(f"VERIFY FAIL: Applied {cid} has empty files_modified"); bad = 1
        for f in files:
            if f.startswith("security/") or f.startswith(".sde-security/") or ALT.search(f):
                print(f"VERIFY FAIL: Applied {cid} references non-surviving/alt file {f}"); bad = 1
            elif not os.path.exists(f):
                print(f"VERIFY FAIL: Applied {cid} file missing on disk: {f}"); bad = 1
print("PY_AUDIT_RESULT", "OK" if bad == 0 else "FAIL")
sys.exit(1 if bad else 0)
PY
pyrc=$?
if [ "$pyrc" -ne 0 ]; then fail=1; fi

if [ "$fail" -ne 0 ]; then echo "VERIFY FAIL"; exit 1; fi
echo "VERIFY PASS"
exit 0
