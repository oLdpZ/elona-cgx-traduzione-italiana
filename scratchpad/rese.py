import io, json, sys

f = sys.argv[1]
filtro = sys.argv[2] if len(sys.argv) > 2 else 'name('
v = [json.loads(l) for l in io.open(f, encoding='utf-8') if l.strip()]
v = [x for x in v if x.get('it') and filtro in (x.get('it') or '')]
for x in sorted(v, key=lambda x: x['riga']):
    print(f"{x['riga']:6d}  {x['it']}")
print('---', len(v), 'voci rese che contengono', repr(filtro))
