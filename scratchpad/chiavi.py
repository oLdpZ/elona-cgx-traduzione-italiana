import io, json, sys

sorgente, da, a = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
voci = [json.loads(l) for l in io.open(sorgente, encoding='utf-8') if l.strip()]
z = sorted([v for v in voci if da <= v['riga'] <= a], key=lambda v: (v['riga'], v['en']))
for v in z:
    print(f"({v['riga']}, {v['en']!r}): [{v['tipo']}]")
