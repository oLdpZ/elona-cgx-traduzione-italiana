# -*- coding: utf-8 -*-
"""Le tre colonne della finestra dei talenti, e quanto ci sta in ognuna.

`command.hsp:2596` apre una finestra da **730 px** con tre intestazioni — Name,
Level, Detail — e la riempie in due modi diversi (`:2680`-`:2691`):

- un **talento vero** (`list(1, p) < 10000`) scrive il nome a `wx + 84` con
  `cs_list`, e l'effetto a `wx + 270` con un `mes`;
- una **mutazione, un tratto di razza, un bit o l'etere** scrive tutto su una
  riga sola a `wx + 70`, preceduto da `[Feat]`, `[Mutation]`, `[Race]` o
  `[Ether]`.

Il carattere e' Courier New a corpo 12 (`command.hsp:2643`, `14 - en * 2`),
cioe' **7 px per carattere** — lo stesso passo misurato al pixel sul pannello
degli dei nella 62a. I bordi:

    nome     wx +  84 .. wx + 270   186 px    26 caratteri
    effetto  wx + 270 .. wx + 674   404 px    57 caratteri
    riga sola wx + 70 .. wx + 674   604 px    86 caratteri

Il margine destro e' `wx + ww - 56` (`:2607`), dove comincia la decorazione.

⚠️ **Il nome porta anche un suffisso che non e' nel dizionario**: `(MAX)` quando
il talento e' al massimo e `(requirement)` quando manca il requisito
(`command.hsp:2128`-`:2135`). Il secondo costa 13 caratteri e in inglese sfonda
gia' da solo: il nome vero ha 26 - 13 = **13 caratteri** se lo si vuole leggere
insieme al requisito. Qui il tetto e' misurato **senza** suffisso, com'e' il
caso normale, e i suffissi sono contati a parte.

## Come si sa in che colonna finisce una stringa

Lo dice la forma dell'assegnazione dentro `trait.hsp`:

    traitrefn2 = lang(..), lang(..), ..     -> i NOMI di livello (colonna 1)
    traitrefn(2) = lang(..), lang(..), ..   -> il primo e' l'EFFETTO (colonna 3),
                                               gli altri sono le descrizioni per
                                               livello, che vanno sulla riga sola

⚠️ E' la stessa lezione della 61a: il metro va preso sulla **stringa che finisce
in quella colonna**, non su tutte le stringhe del file.
"""
import io
import os
import re
import sys

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'

PASSO = 7
TETTO_NOME = (270 - 84) // PASSO          # 26
TETTO_EFFETTO = (730 - 270) // PASSO      # 65
# ⚠️ La decorazione di `wx + ww - 56` sta in BASSO (`wy + wh - 198`), quindi
#    non stringe la colonna: il confine e' il bordo destro della finestra.
#    Anche cosi' l'inglese di monte ne sfora **11 su 63**, fino a 69: `mes`
#    non taglia e il testo esce dalla finestra. Il metro operativo resta
#    «non sforare dove l'inglese ci stava».
TETTO_RIGA = (674 - 70) // PASSO          # 86

SUFFISSI = {'(MAX)': 5, '(requirement)': 13}

_LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
_NOMI = re.compile(r'^\s*traitrefn2\s*=')
_DESCR = re.compile(r'^\s*traitrefn\(\s*2\s*\)\s*=')


def leggi(percorso):
    with io.open(percorso, encoding='cp932', errors='replace') as f:
        return f.read().split('\n')


def _elementi(coda):
    """Gli elementi dell'assegnazione HSP `a = x, y, z`, in ordine.

    ⚠️ Non si puo' spezzare sulle virgole nude: `lang("a, b", "c")` ne porta
    dentro. Si conta la profondita' delle parentesi e si sta fuori dalle
    virgolette.
    """
    fuori, corrente, prof, dentro = [], '', 0, False
    for c in coda:
        if c == '"':
            dentro = not dentro
        if not dentro:
            if c == '(':
                prof += 1
            elif c == ')':
                prof -= 1
            elif c == ',' and prof == 0:
                fuori.append(corrente)
                corrente = ''
                continue
        corrente += c
    fuori.append(corrente)
    return fuori


def raccogli(radice):
    """[(riga, colonna, giapponese, testo)] per ogni stringa della finestra.

    ⚠️ **L'indice non e' la posizione della `lang()`**: per le mutazioni e per
    l'etere l'assegnazione comincia con un elemento vuoto —
    `traitrefn(2) = "", lang(..), lang(..)` — quindi la prima `lang()` sta
    all'indice **3**, cioe' va sulla riga larga e non nella colonna stretta.
    Contarle a partire da zero diceva che diciassette effetti inglesi
    sforavano: sforavano solo nel referto.
    """
    fuori = []
    for n, riga in enumerate(leggi(os.path.join(radice, 'trait.hsp')), 1):
        if _NOMI.match(riga):
            base = 0
            colonna_di = lambda i: 'nome'
        elif _DESCR.match(riga):
            base = 2
            colonna_di = lambda i: 'effetto' if i == 2 else 'riga'
        else:
            continue
        coda = riga.split('=', 1)[1]
        for salto, elemento in enumerate(_elementi(coda)):
            for jp, testo in _LANG.findall(elemento):
                fuori.append((n, colonna_di(base + salto), jp, testo))
    return fuori


TETTI = {'nome': TETTO_NOME, 'effetto': TETTO_EFFETTO, 'riga': TETTO_RIGA}


def referto(etichetta, voci):
    print(f'--- {etichetta}')
    for colonna in ('nome', 'effetto', 'riga'):
        gruppo = [v for v in voci if v[1] == colonna]
        if not gruppo:
            continue
        tetto = TETTI[colonna]
        fuori = [v for v in gruppo if len(v[3]) > tetto]
        piu_lungo = max(len(v[3]) for v in gruppo)
        print(f'    {colonna:<8} tetto {tetto:>3}   {len(gruppo):>4} voci   '
              f'fuori {len(fuori):>3}   il piu lungo {piu_lungo}')
    return {(v[0], v[2]): v for v in voci}


def main(argv):
    sorgente = raccogli(SORGENTE)
    build = raccogli(BUILD)
    print('LA FINESTRA DEI TALENTI (command.hsp:2596)')
    print(f'Courier New a corpo 12, {PASSO} px per carattere')
    print()
    m_en = referto("l'inglese di monte", sorgente)
    m_it = referto('la build italiana', build)
    print()

    nostre = []
    for chiave, v in m_it.items():
        en = m_en.get(chiave)
        if not en:
            continue
        tetto = TETTI[v[1]]
        if len(en[3]) <= tetto < len(v[3]):
            nostre.append((len(v[3]) - tetto, v, en))
    print(f"=== DOVE L'INGLESE CI STA E NOI NO: {len(nostre)} ===")
    for _, v, en in sorted(nostre, reverse=True):
        print(f'  [{v[1]}] {len(v[3]):3d}/{TETTI[v[1]]}  trait.hsp:{v[0]}')
        print(f'      it  {v[3]}')
        print(f'      en  {en[3]}')

    if '--suffissi' in argv:
        print()
        print('=== i nomi che col suffisso sfondano ===')
        for v in [x for x in build if x[1] == 'nome']:
            for suff, costo in SUFFISSI.items():
                if len(v[3]) + costo > TETTO_NOME:
                    print(f'  {len(v[3]) + costo:3d}  {v[3]}{suff}')


if __name__ == '__main__':
    main(sys.argv[1:])
