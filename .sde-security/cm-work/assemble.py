import json, glob, re, os

root = '/root/dev-work-sde-mcp/vuln-bank-for-testing-github'
cms = {c['task_id']: c for c in json.load(open(f'{root}/.sde-security/cm-list/cms.json'))}
cls = json.load(open(f'{root}/.sde-security/cm-list/classification.json'))
dom = json.load(open(f'{root}/.sde-security/cm-list/domains.json'))
slugs = json.load(open(f'{root}/.sde-security/cm-list/slugs.json'))
meta = json.load(open(f'{root}/.sde-security/cm-work/domain_meta.json'))
PID = 31909
BASE = "https://cd.sdelements.com/bunits/oleg-skill-test/vuln-bank-for-testing-github-app-20260616-1404/vuln-bank-for-testing-github-20260616-1404"

ft = sorted([t for t in cls if cls[t] != 'PROCESS'])

def fm_name(tid):
    n = f"{tid.lower()}-{slugs[tid]}"
    return n[:64].strip('-')

def cm_link(tid):
    return f"{BASE}/tasks/{PID}-{tid}/"

written = 0
fidelity = []
for tid in ft:
    cwpath = f'{root}/.sde-security/cm-work/{tid}.json'
    d = dom[tid]
    path = f"{root}/skills/{d}/{tid}-{slugs[tid]}/SKILL.md"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    cw = json.load(open(cwpath)) if os.path.exists(cwpath) else None
    if cw and cw.get('library_sourced'):
        content = cw['content']
        open(path, 'w').write(content)
        back = open(path).read()
        fidelity.append((tid, cw['source_len'], len(back), len(back) >= cw['source_len']))
        written += 1
        continue
    # template
    cat = cls[tid]
    title = cms[tid]['title']
    pri = cms[tid]['priority']
    desc = (cms[tid].get('desc') or '').strip()
    m = meta.get(d, {})
    affected = m.get('affected', 'See repository source files relevant to this control.')
    approach = m.get('approach', 'Apply the secure pattern described by SD Elements guidance below.')
    code_applicable = cat in ('CODE_FIX', 'ML_CODE')
    desc_short = re.sub(r'\s+', ' ', (desc or title))[:240]
    out = []
    out.append('---')
    out.append(f'name: {fm_name(tid)}')
    out.append(f'description: {desc_short}')
    out.append('---')
    out.append('')
    out.append(f'# {tid}: {title}')
    out.append('')
    out.append(f'**Category:** {cat}  ')
    out.append(f'**SD Elements:** [{tid}]({cm_link(tid)})  ')
    out.append(f'**Priority:** {pri}  ')
    out.append(f'**Domain:** {d}')
    out.append('')
    out.append('## Affected Areas in This Repository')
    out.append('')
    out.append(affected)
    out.append('')
    if code_applicable:
        out.append('## Required Fix')
        out.append('')
        out.append(approach)
    else:
        out.append('## Why Not Directly Code-Fixable in This Repository')
        out.append('')
        out.append(approach)
        out.append('')
        out.append('**Recommended Action:** Track and implement this control at the infrastructure/operations or governance level; document the responsible owner.')
    out.append('')
    if desc:
        out.append('## Implementation Guidance (SD Elements)')
        out.append('')
        out.append(desc)
        out.append('')
    out.append('## Success Criteria')
    out.append('')
    if code_applicable:
        out.append(f'- The control "{title}" is implemented in the affected source files listed above.')
        out.append('- The fix is applied in-place to the original files (no `*_secure.*` copies).')
        out.append('- A test or manual check confirms the vulnerability is no longer exploitable.')
    else:
        out.append(f'- The requirement "{title}" is documented with an owner and an infrastructure/process plan.')
    out.append('')
    out.append('**Status:** Pending')
    out.append('')
    open(path, 'w').write('\n'.join(out))
    written += 1

print('SKILL.md written:', written)
print('expected file_tracked:', len(ft))
print('--- FIDELITY (library-sourced) ---')
bad = [f for f in fidelity if not f[3]]
print('library files checked:', len(fidelity), '| fidelity FAIL:', len(bad))
for f in fidelity:
    print(f"[FIDELITY] {f[0]}: source={f[1]}ch written={f[2]}ch {'PASS' if f[3] else 'FAIL'}")
