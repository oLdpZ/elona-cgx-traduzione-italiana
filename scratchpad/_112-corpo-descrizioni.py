# -*- coding: utf-8 -*-
"""112a - Il CORPO di `db_item.hsp` (indici 0-2): l'anatomia vera, e la
famiglia chiusa che va decisa PRIMA di aprire un lotto.

⚠️⚠️⚠️ **IL CORPO NON E' PROSA LIBERA: E' PROSA PIU' UNA RIGA-FONTE.**
1.509 descrizioni su 1.513 finiscono con una riga marcata da `#`, che il
pannello disegna in un modo tutto suo — a **destra**, in **corsivo grassetto**,
con un **trattino** davanti. E' il titolo del libro da cui la notizia viene:

    A fashionable scarecrow with a white hat on his head. It is said that
    this is the figure of a scarecrow that got tired of guarding the
    farmland and made a bold debut in the city.
                        -~Totally Made-up Stories that are Mistaken for Lies~

    `db_item.hsp:91460`, ITEM_ID_SNOW_SCARECROW

⚠️ **E i titoli distinti sono 225 su 1.512 righe**: i venti piu' frequenti ne
coprono il 74%. E' una **famiglia chiusa**, esattamente come gli otto doni
divini della 111a — solo che qui e' grande settanta volte tanto, e sta sparsa
su tutte le categorie, quindi su tutti i lotti futuri. Deciderla dopo vuol dire
disfare lotti.

IL PERCORSO NEL SORGENTE, verificato riga per riga:

    command.hsp:15991  *com_identify        <- il tasto `x` sull'inventario
                :15994  il messaggio d'errore dice «調査(xキー)»: e' quello
                :16000  pagesize = 15       <- ⚠️ 15, non 16
                :16398  if KNOWN >= ITEM_KNOWN_FULL {   <- ⚠️⚠️ IL CANCELLO
                :16423    if PARAM4 != 0 { ... plan<N>.txt ... }
                :16745    else {
                :16746      repeat 3        <- IL CORPO, description(0..2)
                :16747        salta le vuote
                :16751        una riga VUOTA prima di ogni indice
                :16753        buf = trimdesc(description(cnt), 2)   <- toglie \\t e TUTTI i #
                :16755        repeat noteinfo(0)      <- spezza sui \\n
                :16758          if strlen(q) > 66 -> impaginatore ANNA CUSTOM (:16804)
                :16833          else -> riga intera; e se e' l'ULTIMA:
                :16837            list = -2  ->  a destra, corsivo, col trattino

⚠️⚠️ **IL CORPO SI VEDE SOLO A OGGETTO IDENTIFICATO A FONDO** (`:16398`), come
il rapporto d'identificazione. Un oggetto non identificato mostra solo «You
have to identify the item to gain knowledge.» (`:16395`). Una lista di collaudo
che lo dimentica produce uno schermo muto e la conclusione «non tradotto».

LE QUATTRO GEOMETRIE, e sono quattro perche' il font cambia:

    riga <= 66 non ultima   intera, a sinistra, font 12   budget 69 caratteri
    riga <= 66 ULTIMA       a destra, corsivo, font 11, col trattino
    riga  > 66              impaginata a 70 con rinculo 15, a sinistra, font 11
    (in mezzo)              una riga vuota per ogni indice (:16751)

⚠️ **Il font non e' lo stesso**: `:16875` mette `14 - en*2` = **12**, e `:16897`
lo riporta a `13 - en*2` = **11** per le righe impaginate e per la fonte. Il
`BUDGET = 69` di `_102-carta-conoscenza.py` e' tarato su **7,7 px/carattere**,
che `larghezze.py` ha misurato sui menu — e i menu usano `14 - en*2`, cioe' il
font **12**. ⓘ Sulle righe a font 11 quel budget e' pessimistico di qualche
carattere, e nessuno l'ha ancora misurato a schermo: e' il motivo per cui i
«611 inglesi oltre i 69» di `_107-descrizioni-item.py` NON sono un difetto
dimostrato. **Da guardare in uno screenshot**, non da dedurre.

⚠️⚠️ **LA FONTE HA UN TETTO CHE NESSUNA RETE GUARDA, ED E' 66.** Non e' un
tetto di larghezza: e' la soglia che decide **di che tipo** e' la riga. A 67
caratteri la fonte smette di essere una fonte — cade nell'impaginatore e viene
disegnata a sinistra come testo normale. Il difetto non si vede in un conteggio
e non rompe niente: cambia solo l'aspetto, in silenzio. Il titolo inglese piu'
lungo ne misura **62**, cioe' ha **4 caratteri di margine**.

⚠️ **E il posizionamento della fonte conta 6 px/carattere** (`:16901`,
`pos wx + ww - strlen * 6 - 80`) mentre il carattere ne misura 7 — la stessa
asimmetria di `linguette.py`. Il testo si allunga verso destra piu' di quanto
il gioco creda, quindi un titolo lungo esce dal bordo. Dove esattamente dipende
dal margine vero della finestra, che si misura solo a schermo.

⚠️ **IL TRATTINO ORFANO.** Un `\\n` in coda alla descrizione lascia un ultimo
segmento **vuoto**, e il gioco gli mette il trattino lo stesso: a schermo esce
una riga con un solo `-`. Succede gia' in inglese su **11** descrizioni. Chi
traduce non deve aggiungerne.

⚠️ **`db_item.hsp:60514` scrive il titolo con la tilde LARGA** (`～`), che sta
fra i caratteri proibiti di `guardie.py`. Copiare quel titolo verbatim fa
bocciare il lotto. Il titolo giusto e' quello con la tilde ASCII.

    python scratchpad/_112-corpo-descrizioni.py             # il referto
    python scratchpad/_112-corpo-descrizioni.py --titoli    # la famiglia, tutta
    python scratchpad/_112-corpo-descrizioni.py --prova     # le prove al contrario
"""
import argparse
import collections
import importlib.util
import sys
from pathlib import Path

from strumenti.accenti import degrada

_qui = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location(
    '_107_descrizioni_item', _qui / '_107-descrizioni-item.py')
_107 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_107)
_102 = _107._102

ACAPO = _107.ACAPO
SOGLIA = _107.SOGLIA_IMPAGINA        # 66: sopra, si impagina
CANCELLO = '#'                       # il marcatore della riga-fonte
TABULA = _107.TABULA
TILDE_LARGA = chr(0xFF5E)


def anatomia(en):
    """(prosa, fonte_o_None, segmenti) di una descrizione del corpo.

    La fonte e' l'ultimo segmento se e' corto: e' la regola di `:16836`, che
    guarda **la posizione**, non il `#`. Il `#` e' gia' stato tolto da
    `trimdesc`, e serve solo a dire che chi ha scritto la riga la voleva fonte.
    """
    segmenti = _107.trimdesc(en, 2).split(ACAPO)
    if len(segmenti) >= 2 and len(segmenti[-1]) <= SOGLIA:
        return segmenti[:-1], segmenti[-1], segmenti
    return segmenti, None, segmenti


def voluta_fonte(en):
    """Il segmento che chi ha scritto la riga VOLEVA fonte: quello col `#`.

    ⚠️ Non e' sempre quello che il gioco disegna come fonte. Il `#` dichiara
    l'intenzione, `:16836` guarda la **posizione**: quando la descrizione
    finisce con un `\\n` di troppo, l'ultimo segmento e' vuoto e si prende lui
    il trattino, mentre il titolo scivola indietro e viene disegnato come prosa
    normale. Sono **due** difetti in uno, e si vedono solo confrontando le due
    letture.
    """
    grezzo = en.replace(TABULA, '')
    for pezzo in grezzo.split(ACAPO):
        if pezzo.startswith(CANCELLO):
            return pezzo[1:]
    return None


def righe_disegnate(en):
    """Le righe come il pannello le mette in `listn`, col loro tipo."""
    prosa, fonte, segmenti = anatomia(en)
    fuori = [('vuota', '')]                       # `:16751`
    for s in segmenti:
        ultimo = s is segmenti[-1]
        if len(s) > SOGLIA:
            for pezzo in _102.impagina(s)[0]:
                fuori.append(('impaginata', pezzo))
        elif ultimo and fonte is not None:
            fuori.append(('fonte', s))
        else:
            fuori.append(('intera', s))
    return fuori


def carica_corpo():
    return [(riga, idx, en, it) for riga, idx, en, it in _107.carica()
            if idx in (0, 1, 2)]


# ---------------------------------------------------------------- il referto
def referto(voci, mostra_titoli=False):
    print(f'db_item.hsp, il CORPO (indici 0-2): {len(voci)} descrizioni vive, '
          f'{sum(1 for *_, it in voci if it)} gia\' rese')
    print()

    titoli = collections.Counter()
    senza_fonte = []
    orfani = []
    senza_cancelletto = []
    righe_per_voce = []
    for riga, idx, en, it in voci:
        prosa, fonte, _ = anatomia(en)
        voluta = voluta_fonte(en)
        righe_per_voce.append(len(righe_disegnate(en)))
        if voluta is None:
            senza_cancelletto.append((riga, idx))
        else:
            titoli[voluta.strip()] += 1
        if fonte is None:
            senza_fonte.append((riga, idx))
        elif fonte.strip() == '':
            orfani.append((riga, idx, (voluta or '').strip()))

    print('=== L\'ANATOMIA')
    print(f'  che DICHIARANO una fonte col `#`: {sum(titoli.values())}')
    print(f'  senza il marcatore `#`          : {len(senza_cancelletto)}')
    print(f'  senza ultima riga corta         : {len(senza_fonte)}')
    print(f'  ⚠️ TRATTINO ORFANO: {len(orfani)}   — un `{ACAPO}` di troppo in coda.')
    print(f'     Sono DUE difetti: a schermo esce un trattino solo su una riga,')
    print(f'     e il titolo scivola indietro e viene disegnato come prosa,')
    print(f'     a sinistra e senza corsivo. Gia\' cosi\' in inglese.')
    for riga, idx, titolo in orfani[:4]:
        print(f'       db_item.hsp:{riga} idx{idx}  {titolo}')
    n = sorted(righe_per_voce)
    print(f'  righe disegnate per voce        : mediana {n[len(n)//2]}, '
          f'massima {n[-1]}   (pagesize 15: oltre, si sfoglia — non si taglia)')
    print()

    print('=== LA FAMIGLIA DELLE FONTI — da decidere PRIMA di aprire un lotto')
    print(f'  righe-fonte dichiarate: {sum(titoli.values())}   '
          f'titoli DISTINTI: {len(titoli)}')
    coperte = sum(n for _, n in titoli.most_common(20))
    print(f'  i 20 piu\' frequenti coprono {coperte} righe '
          f'({100 * coperte / max(1, sum(titoli.values())):.0f}%)')
    lung = sorted(len(t) for t in titoli)
    print(f'  lunghezza dei titoli: mediana {lung[len(lung)//2]}, '
          f'massima {lung[-1]}   (il tetto e\' {SOGLIA})')
    stretti = [t for t in titoli if len(t) > SOGLIA - 15]
    print(f'  ⚠️ titoli con meno di 15 caratteri di margine: {len(stretti)}')
    for t in sorted(stretti, key=len, reverse=True):
        print(f'       margine {SOGLIA - len(t):>2}  ({titoli[t]:>3}x)  {t}')
    sporchi = [t for t in titoli if TILDE_LARGA in t]
    if sporchi:
        print(f'  ⚠️ titoli scritti con la tilde LARGA (carattere proibito): {len(sporchi)}')
        for t in sporchi:
            print(f'       ({titoli[t]}x)  {t}')
    print()

    if mostra_titoli:
        print('=== TUTTI I TITOLI, per frequenza')
        for t, quante in titoli.most_common():
            print(f'  {quante:>4}x  L={len(t):>2}  margine {SOGLIA - len(t):>3}  {t}')
        print()

    # ---- il cancello sull'italiano, quando ci sara' --------------------
    rese = [(riga, idx, en, it) for riga, idx, en, it in voci if it]
    print(f'=== IL CANCELLO SULL\'ITALIANO ({len(rese)} rese)')
    if not rese:
        print('  ⓘ nessuna resa: il cancello e\' verde perche\' e\' VUOTO, non')
        print('    perche\' e\' stato superato. Vedi `--prova`, che lo accende.')
        return

    mappa = collections.defaultdict(set)
    fuori_tetto = incoerenti = cancelletto_perso = orfani_nuovi = 0
    coda_persa = spezzate = 0
    for riga, idx, en, it in rese:
        testo = degrada(it)
        if en.count(CANCELLO) != testo.count(CANCELLO):
            cancelletto_perso += 1
        p_en, f_en, _ = anatomia(en)
        p_it, f_it, _ = anatomia(testo)
        if f_en is not None:
            if f_it is None:
                fuori_tetto += 1
            else:
                if f_it.strip() == '' and f_en.strip() != '':
                    orfani_nuovi += 1
                mappa[f_en.strip()].add(f_it.strip())
        per_en = _107._misura_corpo(en)
        per_it = _107._misura_corpo(testo)
        coda_persa += per_it[0] > 0 and per_en[0] == 0
        spezzate += per_it[1] > per_en[1]
    incoerenti = sum(1 for v in mappa.values() if len(v) > 1)

    print(f'  `#` perso o aggiunto            : {cancelletto_perso}   (atteso 0)')
    print(f'  fonte oltre i {SOGLIA} (non e\' piu\' fonte): {fuori_tetto}   (atteso 0)')
    print(f'  trattini orfani introdotti      : {orfani_nuovi}   (atteso 0)')
    print(f'  ⭐ titoli resi in PIU\' modi       : {incoerenti}   (atteso 0)')
    print(f'  code perse introdotte           : {coda_persa}   (atteso 0)')
    print(f'  parole spezzate introdotte      : {spezzate}   (atteso 0)')
    for en_t, its in sorted(mappa.items()):
        if len(its) > 1:
            print(f'     ⚠️ {en_t}')
            for i in sorted(its):
                print(f'          -> {i}')


# ------------------------------------------------------- le prove al contrario
def prova(voci):
    """Ogni prova CERCA il caso peggiore e dice DOVE si accende.

    ⚠️ Una prova che passa in silenzio e' un test che non fallisce mai: qui
    ognuna stampa il punto esatto, non un ✅. E dopo il punto viene la ragione
    per cui l'italiano vero ci arriva o non ci arriva — uno zero senza la
    ragione dello zero non e' un risultato.
    """
    print('=== 1. LA FONTE CHE SMETTE DI ESSERLO (il tetto a 66)')
    base = '~Enciclopedia Fantastica di Irva~'
    for aggiunti in range(0, 80):
        finto = f'Prosa.{ACAPO}#{base[:-1]}{"o" * aggiunti}~'
        _, fonte, _ = anatomia(finto)
        if fonte is None:
            print(f'   -> si accende a {len(base) + aggiunti} caratteri di titolo: '
                  f'la riga cade nell\'impaginatore e va a sinistra')
            break
    else:
        print('   -> NON si accende: la prova non prova niente')

    print()
    print('=== 2. IL TRATTINO ORFANO')
    finto = f'Prosa.{ACAPO}#~Titolo~{ACAPO}'
    _, fonte, _ = anatomia(finto)
    if fonte is not None and fonte.strip() == '':
        print(f'   -> si accende con un {ACAPO!r} in coda: '
              f'l\'ultimo segmento e\' vuoto e a schermo esce un trattino solo')
    else:
        print('   -> NON si accende: la prova non prova niente')

    print()
    print('=== 3. LA CODA PERSA (il difetto dell\'impaginatore)')
    print('   i giri sono strlen/61+1 ma ogni pezzo ne consuma fino a 71:')
    print('   per perdere la coda i pezzi devono venire CORTI, e vengono corti')
    print('   solo se il rinculo trova un confine al 56o carattere e non prima.')
    parola = 'x' * 56
    for quante in range(2, 60):
        q = ' '.join([parola] * quante)
        _, consumati = _102.impagina(q)
        if consumati < len(q):
            print(f'   -> si accende a {len(q)} caratteri: ne perde '
                  f'{len(q) - consumati}, con parole da 56 caratteri')
            break
    else:
        print('   -> NON si accende: la prova non prova niente')
    medie = []
    for riga, idx, en, it in voci:
        for s in _107.trimdesc(en, 2).split(ACAPO):
            parole = [p for p in s.split(' ') if p]
            if len(s) > SOGLIA and parole:
                medie.append(sum(len(p) for p in parole) / len(parole))
    medie.sort()
    print(f'   ⓘ LA RAGIONE DELLO ZERO: la parola media dei segmenti impaginati '
          f'e\' {medie[len(medie)//2]:.1f} caratteri.')
    print(f'      Con parole cosi\' il rinculo trova un confine subito sotto il 70o,')
    print(f'      i pezzi vengono lunghi e i giri avanzano. Per perderla servono')
    print(f'      parole da 56: dodici volte tanto. L\'italiano non ci arriva.')

    print()
    print('=== 4. LA PAROLA SPEZZATA (l\'unica raggiungibile dall\'italiano)')
    for lung in range(2, 40):
        q = ('ab ' * 20)[:54] + 'y' * lung + ' e poi la coda che segue ancora'
        pezzi, _ = _102.impagina(q)
        if _102.spezza_parola(q, pezzi) > 0:
            print(f'   -> si accende con una parola di {lung} caratteri '
                  f'(la finestra di rinculo e\' {_102.RINCULO})')
            break
    else:
        print('   -> NON si accende: la prova non prova niente')
    print(f'   ⚠️ NON C\'E\' UNA RAGIONE DELLO ZERO, qui: «dell\'equipaggiamento» '
          f'ne misura 20,')
    print(f'      «immediatamente» 14, «sopravvivenza» 13. L\'italiano ci arriva,')
    print(f'      e ci arriva piu\' dell\'inglese. E\' il numero da guardare.')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--titoli', action='store_true', help='tutti i titoli distinti')
    ap.add_argument('--prova', action='store_true', help='le prove al contrario')
    args = ap.parse_args()
    voci = carica_corpo()
    if args.prova:
        prova(voci)
    else:
        referto(voci, mostra_titoli=args.titoli)


if __name__ == '__main__':
    main()
