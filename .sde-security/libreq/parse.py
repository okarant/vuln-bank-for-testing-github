import json, re, sys, datetime

resp_file = sys.argv[1]
batch_no = int(sys.argv[2])

root = '/root/dev-work-sde-mcp/vuln-bank-for-testing-github'
batches = json.load(open(f'{root}/.sde-security/libreq/batch_index.json'))
batch_ids = batches[batch_no-1]
pool = json.load(open(f'{root}/.sde-security/cm-list/tech_pool.json'))

def norm(s):
    return re.sub(r'\s+', ' ', (s or '').strip().lower())

# alias groups: members are normalized equivalents
ALIAS = [
    {'python', 'python/django', 'python/flask'},
    {'node', 'node.js', 'express', 'node.js (server-side javascript)'},
    {'javascript'},
    {'sqlite', 'sqlite local data storage'},
    {'linux', 'linux/unix', 'unix'},
    {'postgresql', 'postgres'},
    {'github'},
    {'docker'},
    {'graphql'},
    {'html5', 'html5 web storage'},
    {'cors'},
    {'json'},
]
pool_norm = set(norm(p) for p in pool)

def suffix_matches(suffix):
    s = norm(suffix)
    if s in pool_norm:
        return suffix
    for grp in ALIAS:
        if s in grp and (grp & pool_norm):
            return suffix
    return None

d = json.load(open(resp_file))
cr = d['composite_response']
by_ref = {r['reference_id']: r for r in cr}

now = datetime.datetime.now().isoformat()
results = []
for cid in batch_ids:
    r = by_ref.get(cid)
    art = {'cm_id': cid, 'endpoint': f'library/tasks/{cid}/amendments/',
           'http_status': None, 'result': None, 'amendment_id': None,
           'matched_tech': None, 'queried_at': now}
    if r is None:
        art['http_status'] = 0; art['result'] = 'TEMPLATE_API_ERROR'
    else:
        sc = r.get('http_status_code'); art['http_status'] = sc
        body = r.get('body') or {}
        if sc == 200:
            amds = (body.get('results') if isinstance(body, dict) else None) or []
            match = None
            for a in amds:
                t = a.get('title') or ''
                m = re.match(rf'^{re.escape(cid)} - SKILL\.md - (.+)$', t)
                if m and suffix_matches(m.group(1)):
                    match = (a, m.group(1)); break
            if match:
                art['result'] = 'LIBRARY_SOURCED'
                art['amendment_id'] = match[0].get('id')
                art['matched_tech'] = match[1]
            else:
                art['result'] = 'TEMPLATE_NO_MATCH'
        elif sc == 404:
            art['result'] = 'TEMPLATE_404'
        else:
            art['result'] = 'TEMPLATE_API_ERROR'
    json.dump(art, open(f'{root}/.sde-security/library-lookup/{cid}.json', 'w'))
    results.append(art)

import glob
done_total = len(glob.glob(f'{root}/.sde-security/library-lookup/*.json'))
ft_total = 309
start = done_total - len(results)
for i, art in enumerate(results):
    rr = art['result']
    if rr == 'LIBRARY_SOURCED':
        tag = f"LIBRARY_SOURCED (amd {art['amendment_id']}, tech {art['matched_tech']})"
    elif rr == 'TEMPLATE_NO_MATCH':
        tag = 'TEMPLATE (no matching amendment)'
    else:
        tag = f'TEMPLATE ({rr})'
    print(f"[PROGRESS] Library lookup {start+i+1}/{ft_total} | {art['cm_id']}: {tag}")

print(f"--- BATCH {batch_no} parsed: {len(results)} CMs | artifacts on disk: {done_total} ---")
src = [a['cm_id'] for a in results if a['result']=='LIBRARY_SOURCED']
print('LIBRARY_SOURCED in batch:', src if src else 'none')
