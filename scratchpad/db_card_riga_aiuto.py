# -*- coding: utf-8 -*-
"""La riga d'aiuto della carta: quanto e' lunga oggi, e quanto la allunga la resa.

`tcg.hsp:1492`-`:1509` compone la riga che il tavolo mostra in basso quando la
carta e' selezionata:

    rtvaln  = cardrefn
    rtvaln += "  No." + cardrefno
    rtvaln += " " ( + " " + cardrefsex se non e' "random" )
    rtvaln += " " + cardrefrace + " " + cardrefclass
    rtvaln += "  Rare:" + cnvrare(cardrefrare)

La disegna una `mes` sola (`tcg.hsp:3506`) a `basex + 120` su un tavolo largo
800 (`tcg_mod.hsp:3490`): **680 px**, font 10 — e **non c'e' `talk_conv`**,
quindi quel che sfonda esce dal tavolo invece di andare a capo.

⚠️ Il nome e' l'unico campo che la traduzione cambia. Quindi la domanda non e'
«quanto e' lunga la riga italiana» in assoluto: e' **quanto slack c'e' oggi** fra
la riga inglese piu' lunga e il bordo, e se i +12 caratteri del nome piu' lungo
ci stanno dentro.

⚠️ `cardrefrace` porta dentro `skillname(cardrefattack)`, che il sorgente non
risolve: il conto usa il piu' lungo nome di mossa che il dizionario abbia, cioe'
il caso peggiore vero.
"""
import glob
import io
import json
import re
from pathlib import Path

DB_CARD = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\db_card.hsp')
LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')

CAMPI = {
    'nome': re.compile(r'^\s*cardrefn\s*=\s*(.*)$'),
    'sex': re.compile(r'^\s*cardrefsex\s*=\s*"([^"]*)"'),
    'race': re.compile(r'^\s*cardrefrace\s*=\s*(.*)$'),
    'classe': re.compile(r'^\s*cardrefclass\s*=\s*(.*)$'),
}
BLOCCO = re.compile(r'^\s*if \(\s*dbid == (CREATURE_ID_[A-Z0-9_]+)\s*\)')
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')

# 680 px di tavolo, font 10: in questo font i caratteri a mezza larghezza stanno
# in 5 px. E' la stessa aritmetica di `larghezze.py` (che usa 6 px a font 12).
PX_PER_CAR = 5
TETTO_PX = 680


def piu_lunga_mossa() -> int:
    """⚠️ **Il tetto di una mossa e' quindici caratteri, e sta nel `sdim`**:
    `skill.hsp:3` dichiara `sdim skillname, 16, MAX_SKILL`, cioe' 16 byte per
    elemento. E' la stessa lezione del lotto `tcg_mod-001`, dove il tetto delle
    schede veniva da `sdim cfname@tcg, 16, 10`. Il primo conto di questo referto
    aveva preso il piu' lungo `it` di `dizionario/skill.hsp.jsonl` — **59
    caratteri** — che non e' un nome di mossa ma una descrizione: il file tiene
    tutt'e due, e il campo non dice quale sia quale. Un tetto letto dal `sdim`
    e' un dato del sorgente; un massimo letto da un file misto e' un caso."""
    return 15


def main() -> None:
    righe = io.open(DB_CARD, encoding='cp932').read().split('\n')
    mossa = piu_lunga_mossa() or 25
    carte = []
    corrente = None
    for riga in righe:
        m = BLOCCO.match(riga)
        if m:
            if corrente:
                carte.append(corrente)
            corrente = {'id': m.group(1), 'nome': '', 'sex': 'random', 'race': '', 'classe': ''}
            continue
        if corrente is None:
            continue
        for campo, rx in CAMPI.items():
            m = rx.match(riga)
            if not m:
                continue
            if campo == 'sex':
                corrente['sex'] = m.group(1)
            elif campo == 'nome':
                l = LANG.search(m.group(1))
                corrente['nome'] = l.group(2) if l else ''
            else:
                # i campi non passano da lang(): sono letterali piu' chiamate
                pezzi = LETTERALI.findall(m.group(1))
                lungo = sum(len(x) for x in pezzi)
                if 'skillname(' in m.group(1):
                    lungo += mossa
                corrente[campo] = 'x' * lungo
    if corrente:
        carte.append(corrente)

    def componi(c, nome=None) -> int:
        n = len(nome if nome is not None else c['nome'])
        l = n + len('  No.') + 4        # cardrefno: al massimo quattro cifre
        l += 1
        if c['sex'] != 'random':
            l += 1 + len(c['sex'])
        l += 1 + len(c['race']) + 1 + len(c['classe'])
        l += len('  Rare:') + len('Legendary')
        return l

    lunghe = sorted(carte, key=lambda c: -componi(c))
    print(f'{len(carte)} carte lette; la mossa piu\' lunga del dizionario: {mossa} car.')
    print(f'tetto: {TETTO_PX} px a {PX_PER_CAR} px per carattere = '
          f'{TETTO_PX // PX_PER_CAR} caratteri\n')
    print('=== le dieci righe d\'aiuto piu\' lunghe OGGI (inglese)')
    for c in lunghe[:10]:
        n = componi(c)
        print(f'  {n:4d} car. ({n * PX_PER_CAR:4d} px)  {c["nome"][:40]:40s} {c["id"]}')
    peggio = componi(lunghe[0])
    print(f'\nla piu\' lunga oggi: {peggio} car. = {peggio * PX_PER_CAR} px '
          f'su {TETTO_PX} → slack {TETTO_PX - peggio * PX_PER_CAR} px '
          f'= {(TETTO_PX - peggio * PX_PER_CAR) // PX_PER_CAR} caratteri')
    print(f'il nome italiano piu\' lungo supera il piu\' lungo inglese di 12 caratteri '
          f'= {12 * PX_PER_CAR} px')


if __name__ == '__main__':
    main()
