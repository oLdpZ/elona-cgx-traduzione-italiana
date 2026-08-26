# -*- coding: utf-8 -*-
"""104a - `エルン` si scrive in un modo solo: **Eln**.

Secondo nome sdoppiato della giornata, e ha la forma esatta del primo (vedi
`scratchpad/correzione-kikkasu.py`): **la divergenza e' di monte**, e ogni lotto
ha seguito la riga che aveva davanti.

    chat.hsp:7676   EN «the fairies named Eln»    → IT «gli Eln»
    chat.hsp:9499   EN «a special race of fairy
                        known as Elun»            → IT «gli Elun»

Si tiene **Eln**, perche' `:7676` e' la riga che **definisce** i Norne nominando
tutt'e tre le stirpi insieme — `アールン` Ahlung fra i giganti, `エルン` fra le
fate, `ドヴァルン` Dovarn fra i nani — e una definizione batte una menzione. In
piu' l'eco che il giapponese vuole (`エルン` → elfo, detto apertamente a `:9499`)
in `Eln` si sente di piu' che in `Elun`.

⚠️ Serve **adesso** perche' `db_card.hsp:7011`, la carta di `<Norne> la guida`,
apre su 「エルンという種類の妖精」 — e li' il nome va scritto una volta sola.
ⓘ Le altre due occorrenze di `エルン` nel sorgente sono dentro `ザイエルン`, il
nome della banca: non c'entrano, e questa correzione non le tocca perche'
guarda la resa italiana, non il giapponese.

    python scratchpad/correzione-eln.py [--prova]
"""
import glob
import io
import json
import os
import re
import sys

ATTESE = 1
QUALE = re.compile(r'\bElun\b')


def main(prova: bool) -> None:
    toccate = 0
    for percorso in sorted(glob.glob('dizionario/*.jsonl')):
        righe = list(io.open(percorso, encoding='utf-8'))
        fuori = []
        cambiato = False
        for l in righe:
            if not l.strip():
                fuori.append(l)
                continue
            v = json.loads(l)
            it = v.get('it') or ''
            if QUALE.search(it):
                nuovo = QUALE.sub('Eln', it)
                print(f'{os.path.basename(percorso)}:{v["riga"]}')
                print(f'   {it[:120]!r}')
                print(f'-> {nuovo[:120]!r}')
                v['it'] = nuovo
                cambiato = True
                toccate += 1
                fuori.append(json.dumps(v, ensure_ascii=False) + '\n')
            else:
                fuori.append(l)
        if cambiato and not prova:
            with io.open(percorso, 'w', encoding='utf-8', newline='\n') as f:
                f.writelines(fuori)
    print(f'\nvoci cambiate: {toccate}   (atteso: {ATTESE})'
          + ('   [PROVA]' if prova else ''))
    if toccate != ATTESE:
        raise SystemExit("numero inatteso: il dizionario non e' quello che credevo")


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main('--prova' in sys.argv)
