import io, json, sys
p = sys.argv[1]
for v in (json.loads(l) for l in io.open(p, encoding='utf-8') if l.strip()):
    print(f'{v["riga"]:6d} [{v["tipo"][:3]}] jp={v["jp"]!r}')
    print(f'        en={v["en"]!r}')
