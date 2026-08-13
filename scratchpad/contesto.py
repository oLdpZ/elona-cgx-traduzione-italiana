import io, sys

P = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx\proc.hsp'
t = io.open(P, encoding='cp932').read().split('\n')
out = io.open('lavoro/_proc_contesto.txt', 'w', encoding='utf-8')
for arg in sys.argv[1:]:
    n = int(arg)
    out.write(f'=== {n}\n')
    for i in range(n - 7, n + 4):
        out.write(f'{i+1:6d} | {t[i].rstrip()[:150]}\n')
out.close()
print('scritto lavoro/_proc_contesto.txt')
