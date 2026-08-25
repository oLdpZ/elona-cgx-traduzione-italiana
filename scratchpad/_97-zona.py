import io, os, sys
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
f, da, a = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
righe = io.open(os.path.join(SORGENTE, f), encoding='cp932', errors='replace').read().splitlines()
for n in range(da, min(a, len(righe)) + 1):
    print(f'{n:6d} {righe[n-1]}')
