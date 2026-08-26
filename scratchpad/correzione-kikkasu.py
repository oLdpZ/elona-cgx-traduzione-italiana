# -*- coding: utf-8 -*-
"""104a - `キッカス` si scrive in un modo solo: **Kikkasu**.

Il paese di `キッカス` era reso in **due** modi, e la spaccatura seguiva il file:

    Kikkasu   7 occorrenze   chat.hsp:2063, :2111, :2140, :24304
                             text.hsp:9828, :9831
    Kikkas    3 occorrenze   db_card.hsp:3722, :5431   db_creature.hsp:67983

Non e' una divergenza nostra: e' l'inglese di monte che scrive `Kikkasu` nella
catena della missione e `Kikkas` nelle carte, e ogni lotto ha seguito il file
che aveva davanti. Il giapponese pero' e' **uno**, e il giocatore incontra il
paese prima nella missione del demone della pestilenza e poi sulle carte.

Si tiene **Kikkasu**, per tre ragioni e in quest'ordine:

- e' la forma che il giocatore legge di piu' (7 contro 3) e nei punti che
  contano — il diario delle missioni (`text.hsp`) e i dialoghi di Erystia;
- traslittera per intero il katakana, e in italiano una parola che finisce in
  `-su` si legge e si declina, mentre `Kikkas` chiude su un nesso che
  l'italiano non ha;
- il nome del pitone e' **derivato** dal paese, non viceversa: e' il derivato
  che si adegua.

⚠️ Tocca anche un **nome di creatura**, `il pitone di Kikkas`, che vive con la
stessa firma in due dizionari (`db_card.hsp:5431` e `db_creature.hsp:67983`) e
va cambiato in tutti e due, se no la stessa firma porta due rese.

    python scratchpad/correzione-kikkasu.py [--prova]
"""
import glob
import io
import json
import os
import sys

ATTESE = 3


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
            # solo chi dice `Kikkas` senza gia' dire `Kikkasu`
            if 'Kikkas' in it and 'Kikkasu' not in it:
                nuovo = it.replace('Kikkas', 'Kikkasu')
                print(f'{os.path.basename(percorso)}:{v["riga"]}  {it!r}')
                print(f'{" " * (len(os.path.basename(percorso)) + 1 + len(str(v["riga"])))}   -> {nuovo!r}')
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
