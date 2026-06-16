#!/usr/bin/env bash
# Independent, disk-only verification for the setup-security-plan-from-repo run.
# Re-derives every count from disk; never reads file bodies into the model context.
set -u
cd "$(dirname "$0")/.." || exit 2
EXPECTED=309            # SDE anchor: project_countermeasures count(368) - PROCESS(59)
fail=0
reasons=""

note() { reasons="$reasons\n - $1"; fail=1; }

files=$(find skills -name "SKILL.md" | wc -l | tr -d ' ')
[ "$files" = "$EXPECTED" ] || note "skills SKILL.md count $files != $EXPECTED"

rows=$(grep -cE "^\| C?T[0-9]" AGENTS.md)
[ "$rows" = "$EXPECTED" ] || note "AGENTS.md ledger rows $rows != $EXPECTED"

lookup=$(ls .sde-security/library-lookup/*.json 2>/dev/null | wc -l | tr -d ' ')
[ "$lookup" = "$EXPECTED" ] || note "library-lookup artifacts $lookup != $EXPECTED"

cmwork=$(ls .sde-security/cm-work/T*.json .sde-security/cm-work/CT*.json 2>/dev/null | wc -l | tr -d ' ')
# cm-work only holds library-sourced CMs (47) in this run's offload design
audit=$(python3 -c "import json;print(len(json.load(open('.sde-handoff.json'))['library_lookup_audit']))" 2>/dev/null)
[ "$audit" = "$EXPECTED" ] || note "handoff library_lookup_audit length $audit != $EXPECTED"

# Library-sourced CM IDs from AGENTS.md Source stamps (excluded from tell-scan)
libids=$(grep -oE "^\| (C?T[0-9]+) .*LIBRARY:" AGENTS.md | grep -oE "C?T[0-9]+" | sort -u)
libcount=$(echo "$libids" | grep -c . )

# Fidelity: each library-sourced file >= its source amendment length
python3 - "$libcount" <<'PY'
import json, glob, sys, os, re
root='.'
lib={json.load(open(f))['cm_id']:json.load(open(f)) for f in glob.glob('.sde-security/library-lookup/*.json')}
cw={}
for f in glob.glob('.sde-security/cm-work/*.json'):
    try:
        d=json.load(open(f))
        if isinstance(d,dict) and d.get('library_sourced'): cw[d['cm_id']]=d
    except Exception: pass
bad=0
for cid,d in cw.items():
    hits=glob.glob(f'skills/*/{cid}-*/SKILL.md')
    if not hits: print('FIDELITY MISSING FILE', cid); bad+=1; continue
    if os.path.getsize(hits[0]) < d['source_len']*0.9: print('FIDELITY SHORT', cid); bad+=1
sys.exit(1 if bad else 0)
PY
[ $? -eq 0 ] || note "library fidelity check failed"

# Placeholder/sampling tells in TEMPLATE files only (exclude library-sourced)
tellhits=0
while IFS= read -r f; do
  cid=$(echo "$f" | grep -oE "/(C?T[0-9]+)-" | grep -oE "C?T[0-9]+")
  echo "$libids" | grep -qx "$cid" && continue
  if grep -qE "\{CM_ID\}|\bTODO\b|\.\.\. and [0-9]+ more|representative sample" "$f"; then
    echo "TELL in $f"; tellhits=$((tellhits+1))
  fi
done < <(find skills -name "SKILL.md")
[ "$tellhits" = "0" ] || note "placeholder/sampling tells in $tellhits template files"

echo "files=$files rows=$rows lookup=$lookup audit=$audit library=$libcount tells=$tellhits"
if [ "$fail" = "0" ]; then
  echo "VERIFY PASS"
  exit 0
else
  echo -e "VERIFY FAIL:$reasons"
  exit 1
fi
