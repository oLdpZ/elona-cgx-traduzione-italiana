import io, glob, os
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
ago = '\u968e\u76f8\u5f53'   # 階相当
for p in sorted(glob.glob(os.path.join(SORGENTE, '*.hsp'))):
    for n, r in enumerate(io.open(p, encoding='cp932', errors='replace').read().splitlines(), 1):
        if ago in r:
            print(os.path.basename(p), n, r.strip()[:110])
