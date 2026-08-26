# -*- coding: utf-8 -*-
"""103a - `カブ` non e' un cucciolo: e' una motoretta.

Trovato traducendo `:3423` di `db_card.hsp` (la moto grossa), che in giapponese
si presenta come 「カブの仲間だが、大型でかなりの速度を出せる」 — *e' della
famiglia del Cub, ma e' grossa e fa una velocita' notevole*. La carta di `カブ`
stessa (`db_card.hsp:13955`) lo dice senza margini:

    頑丈で燃費が良いだけでなく、高い生命力と速度を持つ機械の馬。

«un cavallo meccanico robusto, che consuma poco». E' la Honda Super Cub, ed e'
la sorella minore de «la moto grossa». Il nome era stato reso «il cucciolo»
nella fase dei nomi, prendendo alla lettera l'inglese `cub`: nessuna decisione
scritta a monte, solo l'inglese seguito senza aprire il blocco.

⚠️ Gli altri «cuccioli» del dizionario **non** si toccano: `火炎竜の幼体`,
`仔グリフォン`, `パピー`, `子犬の洞窟` e gli orsi sono cuccioli davvero. Qui si
cambia solo il giapponese `カブ` e il suo composto `カブ=トライズ`.

    python scratchpad/correzione-cub.py [--prova]
"""
import glob
import io
import json
import os
import sys

CAMBI = {
    'カブ': ('il cucciolo', 'il Cub'),
    'カブ=トライズ': ('il cucciolo Toraizu', 'il Cub Toraizu'),
}


def main(prova: bool) -> None:
    toccati = 0
    for percorso in sorted(glob.glob('dizionario/*.jsonl')):
        righe = [l for l in io.open(percorso, encoding='utf-8')]
        fuori = []
        cambiato = False
        for l in righe:
            if not l.strip():
                fuori.append(l)
                continue
            v = json.loads(l)
            atteso = CAMBI.get(v['jp'])
            if atteso and v.get('it') == atteso[0]:
                v['it'] = atteso[1]
                cambiato = True
                toccati += 1
                print(f'{os.path.basename(percorso)}:{v["riga"]}  '
                      f'{atteso[0]!r} -> {atteso[1]!r}')
                fuori.append(json.dumps(v, ensure_ascii=False) + '\n')
            else:
                fuori.append(l)
        if cambiato and not prova:
            with io.open(percorso, 'w', encoding='utf-8', newline='\n') as f:
                f.writelines(fuori)
    print(f'\nvoci cambiate: {toccati}   (atteso: 6)' + ('   [PROVA]' if prova else ''))
    if toccati != 6:
        raise SystemExit('numero inatteso: il dizionario non e\' quello che credevo')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main('--prova' in sys.argv)
