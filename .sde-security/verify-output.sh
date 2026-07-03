#!/usr/bin/env bash
set -u
EXP_FILES=83
EXP_FT=83
fail=""
cd "$(dirname "$0")/.."
n=$(find skills -name SKILL.md | wc -l); [ "$n" -eq "$EXP_FILES" ] || fail="$fail files($n!=$EXP_FILES)"
rows=$(grep -cE '^\| [A-Z]*T[0-9]' AGENTS.md); [ "$rows" -eq "$EXP_FILES" ] || fail="$fail rows($rows!=$EXP_FILES)"
uniq=$(find skills -name SKILL.md -path "*/*T[0-9]*-*/*" | sed -E 's|.*/([A-Z]*T[0-9]+)-.*|\1|' | sort -u | wc -l); [ "$uniq" -eq "$EXP_FT" ] || fail="$fail uniq($uniq!=$EXP_FT)"
ll=$(ls .sde-security/library-lookup/*.json | wc -l); [ "$ll" -eq "$EXP_FT" ] || fail="$fail lookup($ll!=$EXP_FT)"
cw=$(ls .sde-security/cm-work/*.json | wc -l); [ "$cw" -eq "$EXP_FILES" ] || fail="$fail cmwork($cw!=$EXP_FILES)"
aud=$(python3 -c "import json;print(len(json.load(open('.sde-handoff.json'))['library_lookup_audit']))")
[ "$aud" -eq "$EXP_FT" ] || fail="$fail audit($aud!=$EXP_FT)"
sf=$(python3 -c "import json;print(len(json.load(open('.sde-handoff.json'))['skill_files']))")
[ "$sf" -eq "$EXP_FILES" ] || fail="$fail skillfiles($sf!=$EXP_FILES)"
# library fidelity
fidfail=$(python3 -c "
import json,os
srcmap=json.load(open('/tmp/srcmap.json'))
bad=[p for p,sl in srcmap.items() if os.path.getsize(p) < sl]
print(','.join(bad))
")
[ -z "$fidfail" ] || fail="$fail fidelity($fidfail)"
# placeholder scan on TEMPLATE files only (exclude library files)
mapfile -t LIB < /tmp/libpaths.txt
is_lib(){ local f="$1"; for l in "${LIB[@]}"; do [ "$l" = "$f" ] && return 0; done; return 1; }
ph=""
while IFS= read -r f; do
  if is_lib "$f"; then continue; fi
  if grep -qE '\{ID\}|\{Title\}|\{file_path\}|\{current_code\}|\{secure_code_pattern\}|\{who/what|TODO:' "$f"; then ph="$ph $f"; fi
done < <(find skills -name SKILL.md)
[ -z "$ph" ] || fail="$fail placeholders($ph)"
if [ -z "$fail" ]; then echo "VERIFY PASS"; exit 0; else echo "VERIFY FAIL:$fail"; exit 1; fi
