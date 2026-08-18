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
(`command.hsp:2131`-`:2135`). Il tetto qui sotto e' misurato **senza** suffisso,
com'e' il caso normale, e i suffissi si contano a parte con `--suffissi`.

⚠️⚠️ **E il suffisso non e' lo stesso nelle due lingue**: `(MAX)` e' un letterale
nudo e vale 5 in tutt'e due, ma il secondo e' una `lang()` — `(requirement)` 13
in inglese, `(requisiti)` **11** in italiano. Fino alla 63a questo referto
applicava il costo inglese anche alla build e non confrontava con l'inglese:
gridava 45 nomi sfondati, contandoli 2 caratteri piu' lunghi del vero e senza
dire che l'inglese sfonda negli stessi posti. E' di nuovo la lezione della 61a —
misurare una cosa *vicina* invece della cosa. Adesso i suffissi si leggono da
`command.hsp` **dell'albero che si sta misurando**, e il metro e' quello di
sempre: **sforare dove l'inglese ci stava**.

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

_LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
# ⚠️ `.*` avido e non `[^)]*`: l'argomento e' `traitref(2) - 1`, che una
#    parentesi ce l'ha dentro, e la classe negata si fermava li'.
_MAX = re.compile(r'traitrefn2\(.*\)\s*\+\s*"([^"]*)"')
_RQ = re.compile(r'^\s*s\s*\+=\s*(lang\(.*\))\s*$')
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


def suffissi(radice):
    """I due suffissi del nome, letti da `command.hsp` di QUESTO albero.

    ⚠️ Non si scrivono a mano: `(MAX)` e' un letterale nudo e resta uguale, ma
    l'altro e' una `lang()` e la build lo traduce. Si parte dalla riga del
    `(MAX)` e si guarda poco sotto, perche' `s += lang(..)` da solo non e'
    abbastanza raro da agganciarlo in tutto il file.
    """
    righe = leggi(os.path.join(radice, 'command.hsp'))
    fuori = {}
    for n, riga in enumerate(righe):
        m = _MAX.search(riga)
        if not m:
            continue
        fuori[m.group(1)] = len(m.group(1))
        for seguito in righe[n + 1:n + 8]:
            r = _RQ.match(seguito)
            if r:
                for _, testo in _LANG.findall(r.group(1)):
                    fuori[testo] = len(testo)
                break
        break
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
        s_en, s_it = suffissi(SORGENTE), suffissi(BUILD)
        print()
        print('=== IL NOME COL SUFFISSO ===')
        for etichetta, s in (("l'inglese di monte", s_en), ('la build', s_it)):
            print(f'    {etichetta}: ' + ', '.join(
                f'{k} = {v}' for k, v in s.items()))
        for etichetta, voci, s in (("l'inglese di monte", sorgente, s_en),
                                   ('la build italiana', build, s_it)):
            print(f'--- {etichetta}')
            for suff, costo in s.items():
                nomi = [x for x in voci if x[1] == 'nome']
                fuori = [x for x in nomi if len(x[3]) + costo > TETTO_NOME]
                print(f'    {suff:<14} costo {costo:>2}   '
                      f'sfondano {len(fuori):>3} nomi su {len(nomi)}')
        print()

        # ⚠️ Il metro resta quello di sempre: non «sforare», ma «sforare dove
        #    l'inglese ci stava». Le chiavi sono (riga, giapponese) come sopra.
        nostre = []
        for chiave, v in m_it.items():
            en = m_en.get(chiave)
            if not en or v[1] != 'nome':
                continue
            for (suff_it, c_it), (suff_en, c_en) in zip(s_it.items(),
                                                        s_en.items()):
                if len(en[3]) + c_en <= TETTO_NOME < len(v[3]) + c_it:
                    nostre.append((len(v[3]) + c_it, v, suff_it, en, suff_en))
        print(f"=== COL SUFFISSO, DOVE L'INGLESE CI STA E NOI NO: "
              f'{len(nostre)} ===')
        for lungo, v, suff_it, en, suff_en in sorted(nostre, reverse=True):
            print(f'  {lungo:3d}/{TETTO_NOME}  trait.hsp:{v[0]}')
            print(f'      it  {v[3]}{suff_it}')
            print(f'      en  {en[3]}{suff_en}')


if __name__ == '__main__':
    main(sys.argv[1:])
