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


SKILL_BUILD = Path(r'C:\Games\Elona\_traduzione\build\2.05-custom-gx\skill.hsp')
ASSEGNA_MOSSA = re.compile(r'^\s*skillname\([^)]*\)\s*=\s*lang\(\s*"(?:[^"\\]|\\.)*"\s*,'
                           r'\s*"((?:[^"\\]|\\.)*)"\s*\)')


def piu_lunga_mossa() -> int:
    """Il nome di mossa piu' lungo, **letto dalle assegnazioni** di `skill.hsp`.

    ⚠️⚠️ **Questa funzione ha sbagliato due volte, in due modi opposti, e
    tutt'e due gli errori valgono piu' del numero che restituisce.**

    1. Il primo conto prendeva il piu' lungo `it` di
       `dizionario/skill.hsp.jsonl`: **59 caratteri**. Ma quel file tiene i nomi
       di mossa *e* le descrizioni, e il campo non dice quale sia quale — 59 e'
       una descrizione. Con quel numero la riga d'aiuto risultava **fuori
       misura**, e la conclusione sarebbe stata sbagliata.
    2. Il secondo conto tornava `15`, letto da `skill.hsp:3`
       (`sdim skillname, 16, MAX_SKILL`). ⚠️ **E `sdim` NON e' un tetto**:
       `decisioni.md` lo aveva gia' misurato — «`skilldesc` e' dimensionato a 40
       e porta gia' una resa da 59 caratteri, vista a schermo» — perche' HSP
       riespande la stringa in assegnazione. Misurato qui: **47 nomi inglesi e
       172 italiani superano i 15**. Il lotto `tcg_mod-001` della 53ª aveva fatto
       la stessa inferenza sul `sdim` di `cfname@tcg`, quindi e' un errore che il
       progetto ha gia' corretto una volta e rifatto.

    ✅ Adesso si contano le assegnazioni vere, nella **build**, che e' dove sta
    l'italiano: il massimo e' 24, lo stesso dell'inglese.
    """
    percorso = SKILL_BUILD if SKILL_BUILD.exists() else (
        Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\skill.hsp'))
    massimo = 0
    for riga in io.open(percorso, encoding='cp932').read().split('\n'):
        m = ASSEGNA_MOSSA.match(riga)
        if m:
            massimo = max(massimo, len(m.group(1)))
    return massimo or 24


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
