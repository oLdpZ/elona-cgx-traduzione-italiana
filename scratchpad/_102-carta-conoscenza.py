# -*- coding: utf-8 -*-
"""102a - L'impaginazione delle carte nel pannello «Conoscenza dell'oggetto».

Le 1.146 prose di `db_card.hsp` (`cardrefskill`) non finiscono nella carta del
gioco di carte: finiscono in `description(0)` del pannello che si apre con `x`
su un **cadavere**, una **carta** o una **figurina** (`command.hsp:16019`-`:16027`).
E li' l'impaginazione **non e' una `gmes`**: e' un taglio a conteggio di
caratteri scritto a mano, `command.hsp:16802`-`:16829`, il ramo ANNA CUSTOM.

IL MECCANISMO, RIGA PER RIGA (`en = 1`, quindi il ramo inglese):

    p(1) = 61, 0                          <- p(1)=61 e p(2)=0
    repeat strlen(q) / p(1) + 1           <- ⚠️ il NUMERO DI GIRI si fissa QUI, con 61
        p(1) = 70                         <- ma ogni riga si taglia a 70
        repeat 15                         <- e si torna indietro fino a 15 caratteri
            if strmid(q, p(2)+p(1)-cnt, 1) == " " | "," | "."
                p(1) = p(1)-cnt+1 : break
        loop
        listn(0, p) = strmid(q, p(2), p(1))
        p(2) += p(1)
    loop

Da cui **tre** guasti possibili, e sono tre domande diverse:

1. ⚠️⚠️ **LA CODA CHE SPARISCE.** I giri sono `strlen/61 + 1`, ma ogni riga
   consuma fra 57 e 70 caratteri. Se le righe vengono corte, i giri finiscono
   prima del testo e **l'ultimo pezzo non viene mai scritto**: non si vede
   niente, non c'e' un «...», la frase smette. E' il guasto peggiore perche'
   e' invisibile a chi non conosce l'originale.

2. ⚠️ **IL TAGLIO A META' PAROLA.** Se fra il 56o e il 70o carattere della riga
   non c'e' ne' uno spazio ne' una virgola ne' un punto, `p(1)` resta 70 e la
   parola si spezza senza trattino. L'italiano ci arriva piu' spesso
   dell'inglese: parole piu' lunghe, quindi finestre di 15 caratteri piu'
   facilmente senza confini.

3. ⓘ **LA LARGHEZZA.** Il riquadro e' largo 600 px, il testo comincia a
   `wx + 68` (`command.hsp:16877`): restano 532 px.

   ⚠️⚠️ **PER UN GIORNO QUI C'E' STATO SCRITTO 7,7 px/carattere, E IL BUDGET
   USCIVA 69.** Era il metro sbagliato: 7,7 e' misurato sui **menu**
   (`larghezze.py`), e i menu disegnano a `font 14 - en*2`, cioe' **12**. Le
   righe impaginate di questo riquadro le disegna `command.hsp:16897` a
   `font 13 - en*2`, cioe' **11**: un carattere piu' stretto.

   ⭐ **Misurato a schermo il 2026-08-27** (112a), sullo spaventapasseri di
   neve, con due ancore indipendenti nello stesso screenshot:

     - la riga-fonte comincia a `wx + 600 - 6*L - 80` (`:16901`), che per i
       suoi 64 caratteri fa **136 px esatti**: e' l'ancora che fissa la scala
       dello screenshot, perche' non dipende dal carattere ma solo dal codice;
     - con quella scala, i 69 caratteri della prima riga del corpo occupano
       **477 px**, e la riga-fonte ne occupa **441**.

   Da cui **6,9 px/carattere**, e un budget di **77**. Il taglio a 70 (71 col
   rinculo) sta dentro con sei caratteri di margine: ⚠️ **non sfora, e non ha
   mai sforato.** I «606 inglesi e 712 italiani oltre i 69» che questa rete
   contava erano un difetto del metro, non del testo.

   ⓘ E il 7,7 di `larghezze.py` **resta giusto**: e' un altro carattere, come
   gia' aveva scoperto `menu_dialogo.py` il 2026-08-18 trovandone un terzo a
   7,0. Il progetto ha tre metri perche' il gioco ha tre corpi.

⚠️ Il numero che deve restare a zero e' la **terza colonna**: i guasti che
l'italiano introduce dove l'inglese non ce li aveva.

    python scratchpad/_102-carta-conoscenza.py              # italiano contro inglese
    python scratchpad/_102-carta-conoscenza.py --en         # il solo inglese di monte
    python scratchpad/_102-carta-conoscenza.py --mostra 5   # le prime 5 impaginate
    python scratchpad/_102-carta-conoscenza.py --prova      # la prova al contrario
"""
import argparse
import io
import json
import re
import sys

from strumenti.accenti import degrada
from strumenti.percorsi import DIZIONARIO, SORGENTE_HSP

FILE = 'db_card.hsp'

# `command.hsp:16804` e `:16808`
GIRI_SU = 61
TAGLIO = 70
RINCULO = 15
CONFINI = (' ', ',', '.')

# `command.hsp:16868` e `:16877`
LARGHEZZA_RIQUADRO = 600
INSET_SINISTRO = 68
# ⚠️ corretto il 2026-08-27 da 7,7 a 6,9: vedi il docstring, punto 3. Il 7,7
# era il carattere dei MENU (font 12); qui il riquadro disegna a font 11.
# Misurato a schermo, con la riga-fonte come ancora di scala.
PIXEL_PER_CARATTERE = 6.9
BUDGET = int((LARGHEZZA_RIQUADRO - INSET_SINISTRO) / PIXEL_PER_CARATTERE)

# ⚠️⚠️ **LO STESSO RIQUADRO HA DUE BUDGET, PERCHE' HA DUE CORPI.** Il ciclo di
# disegno mette `font 14 - en*2` = **12** a ogni riga (`command.hsp:16875`) e
# poi lo riporta a `13 - en*2` = **11** SOLO per le righe impaginate
# (`list == -1`) e per la riga-fonte (`list == -2`), a `:16897` e `:16900`.
# Tutte le altre — il prezzo stimato, il rapporto d'identificazione
# (`list == 7`), le righe corte stampate intere — restano a **font 12**, dove
# il carattere misura 7,7 e il budget e' **69**.
# ⚠️ Il 2026-08-27, correggendo il budget delle righe impaginate, per un
# momento questa distinzione non c'era e il cancello dell'indice 3 e' passato
# da «110 inglesi fuori» a «0» senza che nulla fosse cambiato a schermo: un
# cancello CHIUSO su 1.319 rese si era allentato in silenzio. Un metro che
# serve due caratteri e' un metro sbagliato per uno dei due.
PIXEL_PER_CARATTERE_INTERO = 7.7
BUDGET_INTERO = int((LARGHEZZA_RIQUADRO - INSET_SINISTRO) / PIXEL_PER_CARATTERE_INTERO)

# `command.hsp:16901`: la riga-fonte si posiziona contando 6 px/carattere
# mentre il carattere ne misura 6,9 — la stessa asimmetria di `linguette.py`.
# Il testo finisce percio' a `520 + L` px invece che a `520`, e tocca il bordo
# destro del riquadro a L = 80. ⭐ Il titolo piu' lungo del gioco ne misura 64
# (63 piu' il trattino): **sedici caratteri di margine**, verificato a schermo.
PIXEL_SUPPOSTI_FONTE = 6
FONTE_TOCCA_IL_BORDO = LARGHEZZA_RIQUADRO - 80

_CARDREFSKILL = re.compile(r'^\s*cardrefskill\s*=\s*lang\(')


def impagina(q):
    """Riproduce `command.hsp:16802`-`:16829` carattere per carattere.

    Restituisce (righe, consumati). `len(q) - consumati` e' la coda perduta.
    """
    giri = len(q) // GIRI_SU + 1
    righe = []
    p2 = 0
    consumati = 0
    for _ in range(giri):
        p1 = TAGLIO
        for cnt in range(RINCULO):
            i = p2 + p1 - cnt
            # in HSP `strmid` oltre la fine rende "", che non e' un confine
            if i < len(q) and q[i] in CONFINI:
                p1 = p1 - cnt + 1
                break
        pezzo = q[p2:p2 + p1]
        if pezzo == '':
            break
        righe.append(pezzo)
        # ⚠️ `p(2) += p(1)` avanza di p(1) anche se il pezzo e' piu' corto:
        # i caratteri **visti** sono quelli del pezzo, non il salto.
        consumati += len(pezzo)
        p2 += p1
    return righe, consumati


def spezza_parola(q, righe):
    """Quante righe finiscono in mezzo a una parola.

    Una riga tagliata di netto e' lunga esattamente `TAGLIO` e non finisce con
    un confine; e non conta l'ultima, che finisce dove finisce il testo.
    """
    rotte = 0
    fine = 0
    for r in righe:
        fine += len(r)
        if len(r) != TAGLIO:
            continue
        if fine >= len(q):
            continue
        if r[-1] in CONFINI:
            continue
        rotte += 1
    return rotte


def margine(q):
    """Quanti caratteri si possono ancora aggiungere prima di perdere la coda.

    ⚠️ Non e' una sottrazione: il numero di giri cresce a scatti di 61 e la
    lunghezza delle righe dipende da **dove cadono** gli spazi. Si misura
    allungando il testo con una parola tipica e guardando quando la coda
    comincia a sparire — che e' il modo in cui l'italiano ci arrivera' davvero.

    Rende `None` se il testo perde gia' la coda cosi' com'e'.
    """
    _, consumati = impagina(q)
    if consumati < len(q):
        return None
    # una coda plausibile: parole italiane di lunghezza media con spazi
    coda = ' parola'
    for aggiunti in range(1, 400):
        prova = q + (coda * (aggiunti // len(coda) + 1))[:aggiunti]
        _, c = impagina(prova)
        if c < len(prova):
            return aggiunti - 1
    return 400


def _lang_argomenti(riga_testo, righe, i):
    """Il secondo argomento della `lang()` che comincia alla riga `i`.

    La `lang()` di `cardrefskill` sta su una riga sola in tutto il file: si
    prendono i due letterali fra virgolette con lo stesso metro di `estrai`.
    """
    pezzi = re.findall(r'"((?:[^"\\]|\\.)*)"', riga_testo)
    return pezzi[-1] if pezzi else None


def carica_sorgente():
    """(riga, en) per ogni `cardrefskill` di `db_card.hsp`."""
    grezzo = (SORGENTE_HSP / FILE).read_bytes().decode('cp932', errors='replace')
    righe = grezzo.split('\n')
    fuori = []
    for i, testo in enumerate(righe, 1):
        if not _CARDREFSKILL.match(testo):
            continue
        en = _lang_argomenti(testo, righe, i)
        if en:
            fuori.append((i, en))
    return fuori


def carica_dizionario():
    """riga -> `it`, per le sole voci gia' rese."""
    percorso = DIZIONARIO / (FILE + '.jsonl')
    if not percorso.exists():
        return {}
    reso = {}
    with io.open(percorso, encoding='utf-8') as f:
        for l in f:
            if not l.strip():
                continue
            v = json.loads(l)
            if v.get('it'):
                reso[v['riga']] = v['it']
    return reso


def referto(voci, etichetta):
    """voci: lista di (riga, testo_en, testo_it_o_None)."""
    coda_en = coda_it = rotte_en = rotte_it = largo_en = largo_it = 0
    solo_it_coda = solo_it_rotte = 0
    misurate = 0
    peggiori = []
    for riga, en, it in voci:
        r_en, c_en = impagina(en)
        perde_en = len(en) - c_en
        spezza_en = spezza_parola(en, r_en)
        oltre_en = sum(1 for r in r_en if len(r.rstrip()) > BUDGET)
        if perde_en > 0:
            coda_en += 1
        rotte_en += spezza_en
        largo_en += oltre_en
        if it is None:
            continue
        misurate += 1
        testo = degrada(it)
        r_it, c_it = impagina(testo)
        perde_it = len(testo) - c_it
        spezza_it = spezza_parola(testo, r_it)
        oltre_it = sum(1 for r in r_it if len(r.rstrip()) > BUDGET)
        if perde_it > 0:
            coda_it += 1
            if perde_en == 0:
                solo_it_coda += 1
                peggiori.append((riga, 'CODA PERSA', perde_it, testo))
        rotte_it += spezza_it
        largo_it += oltre_it
        if spezza_it > spezza_en:
            solo_it_rotte += 1
            peggiori.append((riga, 'PAROLA SPEZZATA', spezza_it - spezza_en, testo))

    print()
    print(f'=== {etichetta}')
    print(f'carte nel file           : {len(voci)}')
    print(f'gia\' rese in italiano    : {misurate}')
    print()
    print(f'                            inglese   italiano')
    print(f'carte con la coda persa  : {coda_en:7d}   {coda_it:8d}')
    print(f'righe spezzate a meta\'   : {rotte_en:7d}   {rotte_it:8d}')
    print(f'righe oltre i {BUDGET} caratteri: {largo_en:7d}   {largo_it:8d}')
    print()
    print(f'⚠️ introdotte dall\'italiano — coda persa: {solo_it_coda}   '
          f'parole spezzate: {solo_it_rotte}   (atteso: 0 e 0)')

    # ⭐ IL NUMERO CHE SPIEGA PERCHE' LA CODA NON SI PERDE MAI.
    # I giri sono contati su 61 caratteri per riga, ma ogni riga ne consuma
    # quanti gliene concede il rinculo: se la **media** sta sopra 61 il testo
    # finisce prima dei giri e non si perde niente. Il margine non e' una
    # costante da ricordare, e' questa disuguaglianza.
    medie = []
    for _, en, it in voci:
        testo = degrada(it) if it else en
        r, _ = impagina(testo)
        piene = r[:-1] if len(r) > 1 else r      # l'ultima riga finisce col testo
        if piene:
            medie.append(sum(len(x) for x in piene) / len(piene))
    medie.sort()
    sotto = sum(1 for m in medie if m < GIRI_SU)
    print()
    print(f'--- la riga media contro i {GIRI_SU} caratteri su cui sono contati i giri')
    print(f'    minimo {medie[0]:.1f}   primo centile {medie[len(medie)//100]:.1f}   '
          f'mediana {medie[len(medie)//2]:.1f}   massimo {medie[-1]:.1f}')
    print(f'    carte con la riga media sotto {GIRI_SU}: {sotto} su {len(medie)}   '
          f'(sono quelle che perderebbero la coda)')
    lunghezze = sorted(len(degrada(it) if it else en) for _, en, it in voci)
    print(f'    lunghezza del testo: mediana {lunghezze[len(lunghezze)//2]}, '
          f'massimo {lunghezze[-1]}')
    return peggiori


def mostra(voci, quante):
    for riga, en, it in voci[:quante]:
        testo = degrada(it) if it else en
        quale = 'IT' if it else 'EN'
        r, c = impagina(testo)
        print(f'--- {FILE}:{riga}  ({quale}, {len(testo)} caratteri, '
              f'{len(testo) // GIRI_SU + 1} giri, {len(r)} righe)')
        for x in r:
            print(f'    |{x}|')
        if c < len(testo):
            print(f'    ⚠️ CODA PERSA ({len(testo) - c} caratteri): {testo[c:]!r}')
        print()


def prova_al_contrario():
    """La rete puntata dove il difetto c'e' di sicuro: deve accendersi."""
    print('=== PROVA AL CONTRARIO — ogni riga qui sotto deve accendere la rete')
    print()

    # 1. la coda persa: righe che si tagliano corte fanno finire i giri prima
    #    del testo. Con confini fitti ogni riga consuma ~57 caratteri contro i
    #    61 su cui sono contati i giri.
    # ogni riga si chiude a 57 caratteri (confine all'estremo del rinculo),
    # cioe' sotto i 61 su cui sono contati i giri: il divario si accumula.
    corto = ('x' * 56 + ' ') * 20
    righe, consumati = impagina(corto)
    print(f'1. coda persa      : {len(corto)} caratteri, {len(corto)//GIRI_SU+1} giri, '
          f'{consumati} consumati -> perduti {len(corto)-consumati}')
    assert consumati < len(corto), 'la rete NON vede la coda persa'

    # 2. la parola spezzata: una parola lunga oltre il rinculo non offre confini
    lungo = 'a' * 40 + ' ' + 'b' * 90
    righe, _ = impagina(lungo)
    print(f'2. parola spezzata : {spezza_parola(lungo, righe)} righe tagliate di netto')
    assert spezza_parola(lungo, righe) > 0, 'la rete NON vede il taglio a meta\' parola'

    # 3. il testo sano non deve accendere niente
    sano = ('Una descrizione italiana con virgole, punti. E parole normali '
            'che offrono confini a sufficienza, sempre, ovunque. Fine.')
    righe, consumati = impagina(sano)
    print(f'3. testo sano      : perduti {len(sano)-consumati}, '
          f'spezzate {spezza_parola(sano, righe)}   (atteso 0 e 0)')
    assert consumati >= len(sano) and spezza_parola(sano, righe) == 0
    print()
    print('⭐ la rete si accende dove il difetto c\'e\' e tace dove non c\'e\'.')


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--en', action='store_true',
                    help='misura il solo inglese di monte (taratura)')
    ap.add_argument('--mostra', type=int, default=0,
                    help='stampa impaginate le prime N carte')
    ap.add_argument('--prova', action='store_true',
                    help='la prova al contrario della rete')
    ap.add_argument('--elenco', type=int, default=12,
                    help='quante voci peggiorate elencare')
    args = ap.parse_args()

    if args.prova:
        prova_al_contrario()
        return

    sorgente = carica_sorgente()
    reso = {} if args.en else carica_dizionario()
    voci = [(riga, en, reso.get(riga)) for riga, en in sorgente]

    if args.mostra:
        mostra(voci, args.mostra)
        return

    etichetta = ('l\'inglese di monte' if args.en
                 else 'l\'italiano contro l\'inglese')
    peggiori = referto(voci, etichetta)
    if peggiori:
        print()
        print(f'--- le prime {min(args.elenco, len(peggiori))} peggiorate')
        for riga, che, quanto, testo in peggiori[:args.elenco]:
            print(f'  {FILE}:{riga}  {che} ({quanto})  {testo[:90]!r}')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
