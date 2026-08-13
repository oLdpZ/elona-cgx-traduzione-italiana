import io, json, sys

quali = sys.argv[1:]
for l in io.open('lavoro/toppe-proc-en.jsonl', encoding='utf-8'):
    if not l.strip():
        continue
    t = json.loads(l)
    etichetta = t['motivo'].split('.')[0] + '.' + t['motivo'].split('.')[1]
    if quali and not any(q in etichetta for q in quali):
        continue
    print('===', etichetta)
    c = t['cerca'] if isinstance(t['cerca'], list) else [t['cerca']]
    s = t['sostituisci'] if isinstance(t['sostituisci'], list) else [t['sostituisci']]
    for r in c:
        print('  -', r.rstrip()[:200])
    for r in s:
        print('  +', r.rstrip()[:200])
