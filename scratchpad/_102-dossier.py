# -*- coding: utf-8 -*-
"""102a - Il dossier di una zona di `db_card.hsp`: la prosa col nome gia' reso.

⚠️ **La descrizione non si traduce da sola.** Ogni `cardrefskill` sta nel blocco
di una creatura, e poche righe sotto c'e' il `cardrefn` con il **nome della
carta**, che il progetto ha gia' reso (1.141 nomi, dalla 54a in poi). Se la
prosa nomina la creatura, deve nominarla **con quel nome**: e' l'unico posto in
cui il giocatore vede le due cose vicine.

💡 E il blocco porta anche `cardrefrace`, che dice l'identificativo della
creatura di monte: serve per andare a cercare la stessa creatura in
`db_creature.hsp`, dove il nome e la razza sono anch'essi gia' resi.

    python scratchpad/_102-dossier.py 1 800
"""
import io
import json
import re
import sys

from strumenti.percorsi import DIZIONARIO, SORGENTE_HSP

FILE = 'db_card.hsp'
_SKILL = re.compile(r'^\s*cardrefskill\s*=\s*lang\(')
_NOME = re.compile(r'^\s*cardrefn\s*=\s*lang\(')
_RACE = re.compile(r'^\s*cardrefrace\s*=\s*"(\d+)')
_ID = re.compile(r'^\s*if\s*\(\s*dbid\s*==\s*(\w+)\s*\)')
_PEZZI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def rese_per_riga():
    percorso = DIZIONARIO / (FILE + '.jsonl')
    fuori = {}
    with io.open(percorso, encoding='utf-8') as f:
        for l in f:
            if l.strip():
                v = json.loads(l)
                fuori[v['riga']] = v
    return fuori


def main():
    da, a = int(sys.argv[1]), int(sys.argv[2])
    righe = (SORGENTE_HSP / FILE).read_bytes().decode('cp932', 'replace').split('\n')
    reso = rese_per_riga()

    dbid = None
    quante = 0
    for i, testo in enumerate(righe, 1):
        m = _ID.match(testo)
        if m:
            dbid = m.group(1)
        if not (_SKILL.match(testo) and da <= i <= a):
            continue
        if testo.lstrip().startswith(';'):
            continue
        pezzi = _PEZZI.findall(testo)
        jp, en = (pezzi[0], pezzi[-1]) if len(pezzi) >= 2 else ('', '')

        # il nome della carta e la razza: si cercano nelle venti righe sotto
        nome_riga = nome_en = nome_jp = None
        razza = None
        for j in range(i, min(i + 20, len(righe))):
            if _NOME.match(righe[j]) and not righe[j].lstrip().startswith(';'):
                p = _PEZZI.findall(righe[j])
                if len(p) >= 2:
                    nome_riga, nome_jp, nome_en = j + 1, p[0], p[-1]
            r = _RACE.match(righe[j])
            if r:
                razza = r.group(1)
            if righe[j].strip() == 'return 1':
                break

        nome_it = (reso.get(nome_riga) or {}).get('it') if nome_riga else None
        quante += 1
        print(f'--- {FILE}:{i}   {dbid}   creatura {razza}')
        print(f'    NOME  jp {nome_jp}')
        print(f'          en {nome_en}')
        print(f'          IT {nome_it}')
        print(f'    JP    {jp}')
        print(f'    EN    {en}')
        print()
    print(f'== {quante} carte fra la riga {da} e la {a}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
