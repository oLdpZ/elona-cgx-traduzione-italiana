# -*- coding: utf-8 -*-
"""Le due domande da sciogliere prima di generare il lotto dei nomi di carta:
**l'articolo** e **la larghezza**.

1. **L'articolo.** Il dizionario rende i nomi di creatura *con* l'articolo — «la
   zanzara gigante» — perche' il contratto dei nomi dice che l'articolo lo porta
   il nome (`contratto-nomi.md` §4). Ma sulla carta il nome e' un'**etichetta**,
   e sta in testa a una riga di dati:

       big mosquito  No.1142   1142 effect:Mosquito Bite   Rare:Common

   Questo conta quanti dei nomi porterebbero un articolo in testa, e quanti sono
   nomi propri fra `<>` dove l'articolo non sta all'inizio e non va toccato.

2. **La larghezza.** Il nome finisce in `carddetailn@tcg` (`tcg.hsp:1647`) e lo
   disegna una `mes` sola a `basex + 120` (`tcg.hsp:3506`), su un tavolo largo
   `basew@tcg = 800` (`tcg_mod.hsp:3490`): **680 px**, font 10 o 12. Non c'e'
   `talk_conv`, quindi non va a capo: quel che sfonda esce dal tavolo.
   Il confronto giusto e' fra l'inglese di oggi e la resa italiana, non contro un
   numero assoluto — se l'italiano non e' piu' lungo del piu' lungo inglese, il
   tavolo regge quel che reggeva prima.
"""
import glob
import io
import json
import re
from pathlib import Path

DB_CARD = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\db_card.hsp')
LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
NOME = re.compile(r'^\s*cardrefn\s*=\s*(lang\(.*)$')

ARTICOLI = ('il ', 'lo ', 'la ', 'i ', 'gli ', 'le ', "l'", "gl'")


def senza_articolo(resa: str) -> str:
    for a in ARTICOLI:
        if resa.lower().startswith(a):
            return resa[len(a):]
    return resa


def main() -> None:
    righe = io.open(DB_CARD, encoding='cp932').read().split('\n')
    nomi = []
    for n, riga in enumerate(righe, 1):
        m = NOME.match(riga)
        if m:
            l = LANG.search(m.group(1))
            if l:
                nomi.append((n, l.group(2)))

    indice = {}
    for p in sorted(glob.glob('dizionario/*.jsonl')):
        for l in io.open(p, encoding='utf-8'):
            if not l.strip():
                continue
            d = json.loads(l)
            if d.get('it'):
                indice.setdefault(d['en'].strip().lower(), set()).add(d['it'])

    con_articolo = senza = propri = 0
    coppie = []
    for n, en in nomi:
        rese = indice.get(en.strip().lower(), set())
        if len(rese) != 1:
            continue
        it = next(iter(rese))
        nudo = senza_articolo(it)
        if nudo != it:
            con_articolo += 1
        else:
            senza += 1
            if it.startswith('<'):
                propri += 1
        coppie.append((n, en, it, nudo))

    print(f'nomi con resa unica: {len(coppie)}')
    print(f'  la resa comincia con un articolo : {con_articolo}')
    print(f'  la resa non ha articolo in testa : {senza} (di cui {propri} propri fra <>)')

    max_en = max(coppie, key=lambda c: len(c[1]))
    max_it = max(coppie, key=lambda c: len(c[2]))
    max_nudo = max(coppie, key=lambda c: len(c[3]))
    print(f'\nil piu\' lungo INGLESE      : {len(max_en[1]):3d}  :{max_en[0]}  {max_en[1]!r}')
    print(f'la piu\' lunga RESA         : {len(max_it[2]):3d}  :{max_it[0]}  {max_it[2]!r}')
    print(f'la piu\' lunga SENZA ARTICOLO: {len(max_nudo[3]):3d}  :{max_nudo[0]}  {max_nudo[3]!r}')

    piu_lunghe = [c for c in coppie if len(c[3]) > len(max_en[1])]
    print(f'\nrese (senza articolo) piu\' lunghe del piu\' lungo inglese ({len(max_en[1])}): '
          f'{len(piu_lunghe)}')
    for n, en, it, nudo in sorted(piu_lunghe, key=lambda c: -len(c[3]))[:20]:
        print(f'  :{n:6d}  {len(nudo):3d}  {en:40s} → {nudo}')

    media_en = sum(len(c[1]) for c in coppie) / len(coppie)
    media_it = sum(len(c[3]) for c in coppie) / len(coppie)
    print(f'\nmedia inglese {media_en:.1f} car., media resa senza articolo {media_it:.1f} car. '
          f'({(media_it/media_en - 1) * 100:+.1f}%)')

    print('\n=== un campione, per vedere che faccia fa la riga')
    for n, en, it, nudo in coppie[:12]:
        print(f'  {en:38s} → {nudo}')


if __name__ == '__main__':
    main()
