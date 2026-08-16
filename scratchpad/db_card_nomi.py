# -*- coding: utf-8 -*-
"""Referto: `db_card.hsp`, il NONO punto cieco — i nomi che il giocatore legge
sulle carte non sono quelli di `db_creature.hsp`.

⭐⭐⭐ **Trovato nella 54ª, traducendo il negozio delle carte.** Le 26
descrizioni di `tcg_custom.hsp` elencano 141 nomi di carta, e il dizionario ne
rende gia' 131: sembrava lavoro fatto. Ma la carta non porta
`cdatan(CDATAN_NAME)`: `tcg_custom.hsp:4537` legge `cardrefn` da `dbs_card`,
che `:4514` ha riempito chiamando `db_card` — cioe' **`db_card.hsp`**, che di
quei nomi tiene una copia tutta sua, dentro `lang()`, **mai estratta**.

    db_card.hsp:23   cardrefn = lang("ビッグモスキート", "big mosquito")
    db_creature.hsp  la stessa creatura, gia' resa «la zanzara gigante»

Tradurre l'elenco del negozio senza toccare `db_card.hsp` darebbe la stessa
cosa che la 53ª ha trovato a schermo: **il negozio in italiano e la carta in
inglese**, nella stessa partita.

⚠️ **Il file non e' in nessun elenco di dizionario** — `dizionario/` non ha
`db_card.hsp.jsonl` — quindi `verifica --dizionario` non lo nomina e nessun
conteggio di «non tradotte» lo include. E' un punto cieco della stessa famiglia
del quarto e dell'ottavo: il testo c'e', la rete che dovrebbe vederlo guarda
altrove.

Questo referto misura **quanto costa chiuderlo**: quanti dei nomi hanno gia'
una resa nel dizionario e quanti no.

Uso:
    python scratchpad/db_card_nomi.py
    python scratchpad/db_card_nomi.py --senza-resa
"""
import argparse
import collections
import glob
import io
import json
import re
import sys
from pathlib import Path

DB_CARD = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\db_card.hsp')
LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
NOME = re.compile(r'^\s*cardrefn\s*=\s*(lang\(.*)$')
SKILL = re.compile(r'^\s*cardrefskill\s*=\s*(lang\(.*)$')


def campi() -> tuple:
    nomi, ambientazioni = [], []
    righe = io.open(DB_CARD, encoding='cp932').read().split('\n')
    for n, riga in enumerate(righe, 1):
        m = NOME.match(riga)
        if m:
            l = LANG.search(m.group(1))
            if l:
                nomi.append((n, l.group(2)))
            continue
        m = SKILL.match(riga)
        if m:
            l = LANG.search(m.group(1))
            if l:
                ambientazioni.append((n, l.group(2)))
    return nomi, ambientazioni


def dizionario() -> dict:
    indice = {}
    for p in sorted(glob.glob('dizionario/*.jsonl')):
        nome = Path(p).name
        for l in io.open(p, encoding='utf-8'):
            if not l.strip():
                continue
            d = json.loads(l)
            if d.get('it'):
                indice.setdefault(d['en'].strip().lower(), []).append((nome, d['riga'], d['it']))
    return indice


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--senza-resa', action='store_true')
    args = ap.parse_args()

    nomi, ambientazioni = campi()
    indice = dizionario()

    resi, mancanti, ambigui = [], [], []
    for n, en in nomi:
        rese = indice.get(en.strip().lower(), [])
        if not rese:
            mancanti.append((n, en))
            continue
        diverse = {r[2] for r in rese}
        (ambigui if len(diverse) > 1 else resi).append((n, en, sorted(diverse)))

    print(f'db_card.hsp — {len(nomi)} nomi di carta, {len(ambientazioni)} testi di ambientazione')
    print(f'  nomi con una resa gia\' nel dizionario : {len(resi)}')
    print(f'  nomi con PIU\' rese diverse            : {len(ambigui)}')
    print(f'  nomi senza nessuna resa               : {len(mancanti)}')
    lunghezze = [len(en) for _, en in ambientazioni]
    if lunghezze:
        print(f'  ambientazione: {sum(lunghezze)} caratteri in tutto, '
              f'la piu\' lunga {max(lunghezze)}, la media {sum(lunghezze)//len(lunghezze)}')

    if ambigui:
        print(f'\n=== i {len(ambigui)} nomi con piu\' di una resa (vanno scelti a mano)')
        for n, en, diverse in ambigui[:40]:
            print(f'  :{n:6d}  {en:44s} {diverse}')
        if len(ambigui) > 40:
            print(f'  … e altri {len(ambigui) - 40}')

    if args.senza_resa or mancanti:
        print(f'\n=== i {len(mancanti)} nomi senza resa')
        for n, en in mancanti[:60]:
            print(f'  :{n:6d}  {en}')
        if len(mancanti) > 60:
            print(f'  … e altri {len(mancanti) - 60}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
