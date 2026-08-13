# -*- coding: utf-8 -*-
"""Ogni blocco `if ( en )` con letterali nudi, accoppiato col suo `if ( jp )`."""
import io, re

P = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx\proc.hsp'
t = io.open(P, encoding='cp932').read().split('\n')
_LET = re.compile(r'"[^"]*[A-Za-z][^"]*"')

# righe dentro if ( en ) con letterali nudi
bersagli = []
dentro = False
for i, riga in enumerate(t):
    s = riga.strip()
    if re.match(r'^if\s*\(\s*en\s*\)\s*\{?\s*$', s):
        dentro = True
        continue
    if dentro:
        if 'lang(' not in riga and _LET.search(riga):
            bersagli.append(i)
        if s.startswith('}'):
            dentro = False

out = io.open('lavoro/_proc_blocchi.txt', 'w', encoding='utf-8')
for i in bersagli:
    # il ramo giapponese: il piu' vicino `if ( jp )` sopra, entro 12 righe
    jp_riga = None
    for j in range(i - 1, max(-1, i - 12), -1):
        if re.match(r'^if\s*\(\s*jp\s*\)\s*\{?\s*$', t[j].strip()):
            for k in range(j + 1, i):
                if t[k].strip().startswith('txt ') or t[k].strip().startswith('txtef'):
                    if t[k].strip().startswith('txt '):
                        jp_riga = k
                        break
            break
    out.write(f'=== en riga {i+1}\n')
    if jp_riga is not None:
        out.write(f'  jp {jp_riga+1}: {t[jp_riga].strip()}\n')
    else:
        out.write('  jp: NESSUN RAMO jp TROVATO\n')
    out.write(f'  en {i+1}: {t[i].strip()}\n')
out.close()
print(f'{len(bersagli)} blocchi -> lavoro/_proc_blocchi.txt')
