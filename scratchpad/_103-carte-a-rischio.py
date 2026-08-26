# -*- coding: utf-8 -*-
"""103a - Quali carte far vedere a schermo, scelte dai numeri e non a gusto.

`_102-carta-conoscenza.py` dice che l'italiano non spezza parole e non perde
code, ma lo dice **per deduzione**: rifa' a mano il taglio di
`command.hsp:16802`-`:16829` e conta. Quel taglio non e' mai stato visto a
schermo. Questa sceglie le carte da guardare puntando dove il margine e' piu'
sottile, cosi' lo screenshot vale come prova e non come conferma di comodo.

⚠️⚠️ **`impagina` e `degrada` si IMPORTANO dalla rete, non si riscrivono.**
La prima stesura di questo file rifaceva il taglio da capo e dava righe medie
intorno a **52** dove la rete dice **68,4**: la differenza era l'ultima riga,
che finisce dove finisce il testo ed e' corta per costruzione — la rete la
scarta (`piene = r[:-1]`), io no. Due misure della stessa cosa che non tornano
sono peggio di una misura sola: qui si usa quella che ha i numeri gia' creduti.

Due rischi, e sono opposti:

- **parola spezzata di netto**: il taglio torna indietro al massimo di 15
  caratteri per cercare uno spazio, una virgola o un punto. Una parola piu'
  lunga della finestra non lascia scampo. Si ordina per parola piu' lunga.
- **coda persa**: i giri sono `strlen/61 + 1`, ma ogni riga ne consuma quanti
  gliene concede il rinculo. Se la riga media sta **sotto** 61 i giri
  finiscono prima del testo. Si ordina per riga media piu' corta.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_103-carte-a-rischio.py
"""
import importlib.util
import io
import json
import re
import sys
from pathlib import Path

from strumenti.percorsi import DIZIONARIO

FILE = 'db_card.hsp'
LOTTI = {7: (3101, 3600), 8: (3601, 4100), 9: (4101, 4600), 10: (4601, 5100)}

_rete_percorso = Path(__file__).with_name('_102-carta-conoscenza.py')
_spec = importlib.util.spec_from_file_location('_carta_conoscenza', _rete_percorso)
rete = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(rete)


def nomi_per_riga() -> dict:
    """Il `cardrefn` gia' reso, per dare un nome leggibile a ogni prosa."""
    fuori = {}
    for l in io.open(DIZIONARIO / (FILE + '.jsonl'), encoding='utf-8'):
        if l.strip():
            v = json.loads(l)
            fuori[v['riga']] = v.get('it') or ''
    return fuori


def main() -> None:
    reso = nomi_per_riga()
    schede = []
    for lotto, (da, a) in sorted(LOTTI.items()):
        for riga, it in sorted(reso.items()):
            if not (da <= riga <= a) or not it:
                continue
            testo = rete.degrada(it)
            righe, consumati = rete.impagina(testo)
            if len(righe) < 2:
                continue                      # e' un nome, non una prosa
            piene = righe[:-1]                # come fa la rete: l'ultima e' corta
            media = sum(len(x) for x in piene) / len(piene)
            piu_lunga = max(re.findall(r'\S+', testo), key=len)
            nome = next((reso[r] for r in range(riga + 1, riga + 20)
                         if reso.get(r) and len(reso[r]) < 60), '')
            schede.append({'lotto': lotto, 'riga': riga, 'nome': nome,
                           'media': media, 'parola': piu_lunga,
                           'righe': len(righe), 'persi': len(testo) - consumati})

    print(f'prose misurate nei lotti {min(LOTTI)}-{max(LOTTI)}: {len(schede)}')
    print(f'⚠️ code perse davvero: {sum(1 for s in schede if s["persi"] > 0)}   '
          f'(la rete dice 0 su tutto il file: qui deve dire 0 anche lei)\n')

    print('=== la parola piu\' lunga: e\' li\' che il taglio puo\' spezzare ===')
    print(f'    (la finestra del rinculo e\' {rete.RINCULO} caratteri)')
    for s in sorted(schede, key=lambda s: -len(s['parola']))[:5]:
        print(f'  lotto {s["lotto"]:2d}  :{s["riga"]}  {s["parola"]} '
              f'({len(s["parola"])} caratteri)   {s["nome"]}')

    print(f'\n=== la riga media piu\' corta: sotto {rete.GIRI_SU} la coda si perde ===')
    for s in sorted(schede, key=lambda s: s['media'])[:5]:
        print(f'  lotto {s["lotto"]:2d}  :{s["riga"]}  riga media {s["media"]:.1f}  '
              f'{s["righe"]} righe   {s["nome"]}')

    print('\n=== la prosa piu\' lunga: e\' li\' che i giri finiscono ===')
    for s in sorted(schede, key=lambda s: -s['righe'])[:5]:
        print(f'  lotto {s["lotto"]:2d}  :{s["riga"]}  {s["righe"]} righe   {s["nome"]}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
