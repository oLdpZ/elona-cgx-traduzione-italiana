# -*- coding: utf-8 -*-
"""107a - Le descrizioni di `db_item.hsp` contro i pannelli che le disegnano.

⚠️ **I quattro indici NON sono la stessa cosa e non hanno lo stesso vincolo.**
E' la cosa che il conteggio «5.284 descrizioni» nascondeva, ed e' il motivo per
cui questo file e' un fronte e non un lotto. (E delle 5.284 righe, **2.452 sono
la stringa vuota**: le vive sono 2.832.)

    description(0..2)   il CORPO del pannello «Conoscenza dell'oggetto».
                        `command.hsp:16746` fa `repeat 3`, salta le vuote,
                        passa da `trimdesc(desc, 2)` (via i `\t` e TUTTI i `#`),
                        spezza sui `\n` con `notesel`/`noteget`, e **solo** le
                        righe piu' lunghe di 66 caratteri (`:16758`) finiscono
                        nell'impaginatore ANNA CUSTOM di `:16802`-`:16829`.
                        Le altre si stampano intere.

    description(3)      il **rapporto di identificazione**, e passa da tutt'altra
                        parte: `:16275`, `cnven(trimdesc(description(3), 1))`.
                        `trimdesc` con 1 **tronca al primo `#`** e toglie il
                        primo `\n`. ⚠️⚠️ E poi finisce in `listn` **senza
                        nessun impaginatore**: non va a capo, non si taglia,
                        **sfora e basta**. E' l'unica delle quattro con un tetto
                        secco, ed e' la piu' numerosa (1.319 vive).

⚠️ **E il tetto dell'indice 3 e' gia' rotto da monte su 110 voci** (massimo 73
caratteri contro 69 di budget). Quindi il numero che deve restare a zero **non
e' la seconda colonna**: e' la **terza**, quelle che introduce l'italiano dove
l'inglese stava dentro. Un cancello sulla seconda boccerebbe lavoro giusto.

⚠️ **L'italiano si misura DEGRADATO.** CP932 non ha le accentate e `degrada()`
le allunga: «perche'» sta in 7 caratteri dove «perché» ne occupa 6. Su un tetto
secco di 69 caratteri e' la differenza fra dentro e fuori, e misurare la forma
accentata darebbe un verde falso.

L'impaginatore, il rinculo e i tre guasti che ne nascono stanno gia' descritti
in `_102-carta-conoscenza.py`, e da li' si **importano** invece di riscriverli:
e' lo stesso ramo di codice, `command.hsp:16802`, e due copie divergerebbero.
La scansione e' quella di `estrai.siti()` — dalla 107a le descrizioni sono un
tipo di sito — e non un automa locale: era proprio un automa locale a far
contare a `perimetro.py` 5.284 descrizioni invece di 2.832.

    python scratchpad/_107-descrizioni-item.py            # il referto
    python scratchpad/_107-descrizioni-item.py --peggiori 15
    python scratchpad/_107-descrizioni-item.py --prova    # la prova al contrario
"""
import argparse
import collections
import importlib.util
import io
import json
import re
from pathlib import Path

from strumenti.accenti import degrada
from strumenti.estrai import estrai_da_testo, spezza_righe
from strumenti.percorsi import DIZIONARIO, SORGENTE_HSP

# il fratello ha un trattino nel nome e non si importa con `import`
_spec = importlib.util.spec_from_file_location(
    '_102_carta_conoscenza', Path(__file__).with_name('_102-carta-conoscenza.py'))
_102 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_102)
BUDGET, impagina, spezza_parola = _102.BUDGET, _102.impagina, _102.spezza_parola

# ⚠️⚠️ **IL RIQUADRO HA DUE BUDGET PERCHE' HA DUE CORPI**, e i due indici stanno
# da parti diverse. Le righe **impaginate** del corpo (indici 0-2) le disegna
# `command.hsp:16897` a font **11**: budget 77. Il rapporto d'identificazione
# (indice 3) entra in `listn` con `list = 7` (`:16278`) e **non** passa da
# quel ritocco: resta al font **12** di `:16875`, dove il budget e' **69**.
# ⚠️ Il 2026-08-27 il budget del font 11 e' stato corretto da 69 a 77 e per un
# momento questa riga non c'era: il cancello dell'indice 3 — CHIUSO su 1.319
# rese — e' passato da «110 inglesi fuori» a «0» senza che nulla fosse
# cambiato a schermo. Un cancello che si allenta in silenzio e' peggio di uno
# rosso.
BUDGET_INTERO = _102.BUDGET_INTERO

FILE = 'db_item.hsp'

# `command.hsp:16758`: sotto questa soglia la riga si stampa intera
SOGLIA_IMPAGINA = 66

# ⚠️ Nel SORGENTE `\n` sono DUE caratteri (barra rovescia + n): e' HSP a
# tradurlo in un a capo a tempo di esecuzione. Chi cerca un `'\n'` vero qui
# non trova niente e conta zero senza dirlo.
ACAPO = chr(92) + 'n'
TABULA = chr(92) + 't'

_INDICE = re.compile(r'^\s*description\((\d+)\)\s*=')


def carica():
    """(riga, indice, en, it_o_None) per ogni descrizione viva di `db_item.hsp`.

    La scansione e' quella del progetto: `estrai_da_testo` rende le voci con la
    firma, e le descrizioni sono quelle **senza** `array` — i nomi ce l'hanno,
    loro no, perche' non hanno plurale ne' articolo.
    """
    testo = (SORGENTE_HSP / FILE).read_text(encoding='cp932')
    righe, _, _ = spezza_righe(testo)
    reso = {}
    percorso = DIZIONARIO / (FILE + '.jsonl')
    if percorso.exists():
        with io.open(percorso, encoding='utf-8') as f:
            for linea in f:
                if not linea.strip():
                    continue
                voce = json.loads(linea)
                if voce.get('it'):
                    reso[voce['firma']] = voce['it']

    fuori = []
    for voce in estrai_da_testo(FILE, testo):
        if 'array' in voce:          # e' un nome, non una descrizione
            continue
        trovato = _INDICE.match(righe[voce['riga'] - 1])
        if trovato is None:          # non e' una `description()`: non e' roba nostra
            continue
        fuori.append((voce['riga'], int(trovato.group(1)),
                      voce['en'], reso.get(voce['firma'])))
    return fuori


def trimdesc(testo, modo):
    """`command.hsp:15947`, il ramo `en` (per noi `en = TRUE`, quindi niente virgole)."""
    q = testo.replace(TABULA, '')
    if modo == 1:
        q = q.replace(ACAPO, '', 1)
        taglio = q.find('#')
        if taglio != -1:
            q = q[:taglio]
    if modo == 2:
        q = q.replace('#', '')
    return q


def righe_a_schermo(testo):
    """Il corpo (indici 0-2): trimdesc 2, spezza sui `\n`, impagina solo se > 66.

    Rende (righe, perduti, spezzate).
    """
    q = trimdesc(testo, 2)
    fuori, perduti, spezzate = [], 0, 0
    for linea in q.split(ACAPO):
        if len(linea) > SOGLIA_IMPAGINA:
            pezzi, consumati = impagina(linea)
            fuori += pezzi
            perduti += len(linea) - consumati
            spezzate += spezza_parola(linea, pezzi)
        else:
            fuori.append(linea)
    return fuori, perduti, spezzate


def _misura_corpo(testo):
    righe, perduti, spezzate = righe_a_schermo(testo)
    larghe = sum(1 for r in righe if len(r.rstrip()) > BUDGET)
    return perduti, spezzate, larghe


def referto(voci):
    per_indice = collections.defaultdict(list)
    for riga, indice, en, it in voci:
        per_indice[indice].append((riga, en, it))

    rese = sum(1 for _, _, _, it in voci if it)
    print(f'{FILE}: {len(voci)} descrizioni vive, {rese} gia\' rese in italiano')
    print(f'budget del riquadro: {BUDGET} caratteri '
          f'(600 px meno l\'inset di 68, a 7,7 px/carattere)')
    print()
    print('  idx   vive   rese  distinti  mediana   max   >66  con \\n')
    print('  ' + '-' * 58)
    for indice in sorted(per_indice):
        gruppo = per_indice[indice]
        lung = sorted(len(en) for _, en, _ in gruppo)
        print(f'  {indice:>3} {len(gruppo):>6} {sum(1 for _, _, it in gruppo if it):>6}'
              f'  {len(set(en for _, en, _ in gruppo)):>8}'
              f'  {lung[len(lung) // 2]:>7}  {lung[-1]:>5}'
              f'  {sum(1 for _, en, _ in gruppo if len(en) > SOGLIA_IMPAGINA):>4}'
              f'  {sum(1 for _, en, _ in gruppo if ACAPO in en):>6}')

    peggiori = []

    # --- il corpo, indici 0-2 -------------------------------------------
    corpo = [v for i in (0, 1, 2) for v in per_indice.get(i, [])]
    c_en = c_it = s_en = s_it = l_en = l_it = 0
    solo_coda = solo_spezza = solo_largo = 0
    misurate = 0
    for riga, en, it in corpo:
        p_en, sp_en, la_en = _misura_corpo(en)
        c_en += p_en > 0
        s_en += sp_en
        l_en += la_en
        if not it:
            continue
        misurate += 1
        testo = degrada(it)
        p_it, sp_it, la_it = _misura_corpo(testo)
        c_it += p_it > 0
        s_it += sp_it
        l_it += la_it
        if p_it > 0 and p_en == 0:
            solo_coda += 1
            peggiori.append((riga, 'CODA PERSA', p_it, testo))
        if sp_it > sp_en:
            solo_spezza += 1
            peggiori.append((riga, 'PAROLA SPEZZATA', sp_it - sp_en, testo))
        if la_it > la_en:
            solo_largo += 1

    print()
    print(f'=== IL CORPO (indici 0-2): {len(corpo)} vive, {misurate} rese')
    print(f'                                inglese   italiano')
    print(f'  con la coda persa           : {c_en:7d}   {c_it:8d}')
    print(f'  righe spezzate a meta\'      : {s_en:7d}   {s_it:8d}')
    print(f'  righe oltre i {BUDGET} caratteri : {l_en:7d}   {l_it:8d}')
    print(f'  ⚠️ INTRODOTTE DALL\'ITALIANO — coda: {solo_coda}   '
          f'parole spezzate: {solo_spezza}   righe larghe: {solo_largo}   (atteso 0/0/0)')

    # --- l'indice 3, il tetto secco -------------------------------------
    tre = per_indice.get(3, [])
    fuori_en = fuori_it = solo_it = 0
    misurate3 = 0
    for riga, en, it in tre:
        lungo_en = len(trimdesc(en, 1))
        fuori_en += lungo_en > BUDGET_INTERO
        if not it:
            continue
        misurate3 += 1
        lungo_it = len(trimdesc(degrada(it), 1))
        fuori_it += lungo_it > BUDGET_INTERO
        if lungo_it > BUDGET_INTERO and lungo_en <= BUDGET_INTERO:
            solo_it += 1
            peggiori.append((riga, 'TETTO SECCO', lungo_it - BUDGET_INTERO, degrada(it)))

    lung3 = sorted(len(trimdesc(en, 1)) for _, en, _ in tre)
    print()
    print(f'=== L\'INDICE 3 (rapporto di identificazione), che NON si impagina')
    print(f'  vive {len(tre)}, rese {misurate3}; '
          f'inglese: mediana {lung3[len(lung3) // 2]}, massima {lung3[-1]}, '
          f'budget {BUDGET_INTERO} (font 12, non impaginato)')
    print(f'  oltre il tetto — inglese: {fuori_en}   italiano: {fuori_it}')
    print(f'  ⚠️ INTRODOTTE DALL\'ITALIANO: {solo_it}   (atteso 0 — questo e\' il cancello)')
    print(f'  ⓘ i {fuori_en} inglesi gia\' fuori sono un difetto di monte: '
          f'non si contano contro di noi, ma una resa piu\' corta li ripara gratis')

    return peggiori


def prova_al_contrario():
    print()
    print('PROVA AL CONTRARIO')
    print('  1. la coda che sparisce: i giri sono strlen/61+1 ma ogni riga ne')
    print('     consuma 57 se il confine cade in fondo al rinculo. Un testo con')
    print('     uno spazio al 57o carattere e nessun confine prima e\' il caso')
    print('     peggiore costruibile.')
    modello = 'x' * 56 + ' '
    acceso = None
    for ripetizioni in range(2, 40):
        finto = (modello * ripetizioni).rstrip()
        _, perduti, _ = righe_a_schermo(finto)
        if perduti:
            acceso = (len(finto), perduti)
            break
    print(f'     {"✅ ACCESA" if acceso else "⚠️⚠️ SPENTA"}: '
          + (f'a {acceso[0]} caratteri ne perde {acceso[1]}' if acceso
             else 'non vede il guasto per cui e\' nata'))
    print(f'     ⓘ l\'inglese piu\' lungo del file ne ha 716: sotto la soglia, ed e\'')
    print(f'       per questo che la colonna «coda persa» sta a zero. Non e\' merito')
    print(f'       di nessuno, e una resa molto piu\' lunga la riaprirebbe.')

    print('  2. il tetto secco dell\'indice 3:')
    corta = 'It is a rod.'
    lunga = 'x' * (BUDGET_INTERO + 1)
    print(f'     {"✅" if len(trimdesc(lunga, 1)) > BUDGET_INTERO else "⚠️"} accende su '
          f'{BUDGET_INTERO + 1} caratteri; '
          f'{"✅" if len(trimdesc(corta, 1)) <= BUDGET_INTERO else "⚠️"} muta su {len(corta)}')

    print('  3. il degrado degli accenti, che allunga:')
    accentata = 'perché è così'
    print(f'     «{accentata}» {len(accentata)} car. -> '
          f'«{degrada(accentata)}» {len(degrada(accentata))} car.  '
          f'{"✅ allunga" if len(degrada(accentata)) > len(accentata) else "⚠️ non allunga"}')

    falsi = 0
    for lunghezza in (10, 40, 66, 67, 120, 300):
        testo = ' '.join(['parola'] * (lunghezza // 7 + 1))[:lunghezza]
        _, p, _ = righe_a_schermo(testo)
        falsi += bool(p)
    print(f'  4. {"✅ muta" if not falsi else "⚠️ FALSI POSITIVI"} su sei testi '
          'innocui da 10 a 300 caratteri')


def previsione(voci):
    """Quanto e' stretto il tetto dell'indice 3 PRIMA di tradurre.

    ⚠️ **E' una previsione, non una misura**, e va marcata come tale: dice che
    cosa succede al rapporto di identificazione se l'italiano viene lungo
    quanto l'italiano viene di solito. Serve a scegliere il registro **prima**
    del primo lotto, invece di scoprirlo alla prima resa bocciata.

    Il fattore non e' inventato: si legge dal progetto stesso, confrontando le
    rese gia' fatte col loro inglese su tutto il dizionario.
    """
    print()
    print('=== PREVISIONE sul tetto dell\'indice 3 (NON e\' una misura)')
    fasce = _fattori_per_lunghezza()
    print('  il fattore italiano/inglese delle rese esistenti, per fascia:')
    for chiave in ('20-49', '50-99', '100-199', '200+'):
        if chiave in fasce:
            mediana, quante = fasce[chiave]
            print(f'    inglese {chiave:>8} caratteri: x{mediana:.3f}  '
                  f'({quante} rese)')
    print('  ⓘ Le fasce servivano a un sospetto che la misura SMENTISCE: si')
    print('    temeva che le corte fossero schiacciate dai tetti dei menu e che')
    print('    la prosa fosse piu\' lunga. Stanno tutte a ~1,0, e i 200+ — prosa')
    print('    vera, 1.482 rese — stanno a x1,000 esatto.')

    # l'indice 3 ha una mediana di 48 caratteri: la fascia sua e' la 20-49,
    # ma il contenuto e' prosa, quindi il fattore onesto sta fra le due
    tre = [(riga, trimdesc(en, 1)) for riga, indice, en, _ in voci if indice == 3]
    candidati = sorted({1.00, 1.05, 1.10, 1.15, 1.20, 1.25}
                       | {round(m, 3) for m, _ in fasce.values()})
    prosa = fasce.get('200+', (None, 0))[0]
    for prova in candidati:
        fuori = sum(1 for _, en in tre if len(en) * prova > BUDGET_INTERO)
        marca = '  <- la fascia della PROSA' if prosa and prova == round(prosa, 3) else ''
        print(f'  a x{prova:.3f}: {fuori:>5} su {len(tre)} sforerebbero '
              f'({100 * fuori / len(tre):.0f}%){marca}')
    print('  💡 Il tetto e\' STRETTO: non e\' un vincolo che si rispetta per caso.')
    print('     Il rapporto di identificazione va scritto CORTO per contratto,')
    print('     non accorciato dopo che la rete lo boccia.')


def _fattori_per_lunghezza():
    """La mediana di len(degrada(it))/len(en), per fascia di lunghezza inglese.

    Le fasce ci sono per un sospetto che la misura ha poi **smentito**, e vale
    la pena tenerne il conto perche' il sospetto era ragionevole: il corpus
    reso e' pieno di voci di MENU, che hanno tetti stretti (`larghezze.py`), e
    ci si aspettava che fossero corte per costrizione — quindi che un fattore
    unico sottostimasse la prosa. Non e' cosi': **tutte e quattro le fasce
    stanno intorno a 1,0**, e la fascia dei 200+ caratteri, che e' prosa vera e
    pesa 1.482 rese, sta a x1,000 esatto. L'italiano di questo progetto corre
    alla pari con l'inglese anche dove nessun tetto lo costringe.

    ⓘ Il che rende il numero **piu'** attendibile, non meno: la previsione
    sull'indice 3 non poggia su una fascia sola.
    """
    fasce = {'20-49': [], '50-99': [], '100-199': [], '200+': []}
    for percorso in sorted(DIZIONARIO.glob('*.jsonl')):
        with io.open(percorso, encoding='utf-8') as f:
            for linea in f:
                if not linea.strip():
                    continue
                voce = json.loads(linea)
                en, it = voce.get('en'), voce.get('it')
                if voce.get('tipo') != 'statica' or not en or not it:
                    continue
                n = len(en)
                if n < 20:            # le corte sono rumore di articolo
                    continue
                chiave = ('20-49' if n < 50 else '50-99' if n < 100
                          else '100-199' if n < 200 else '200+')
                fasce[chiave].append(len(degrada(it)) / n)
    fuori = {}
    for chiave, rapporti in fasce.items():
        if rapporti:
            rapporti.sort()
            fuori[chiave] = (rapporti[len(rapporti) // 2], len(rapporti))
    return fuori


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--peggiori', type=int, default=0)
    ap.add_argument('--prova', action='store_true')
    ap.add_argument('--previsione', action='store_true')
    a = ap.parse_args()

    voci = carica()
    peggiori = referto(voci)

    if a.previsione:
        previsione(voci)

    if a.peggiori and peggiori:
        print()
        print(f'Le {a.peggiori} peggiori introdotte dall\'italiano:')
        for riga, che, quanto, testo in sorted(
                peggiori, key=lambda x: -x[2])[:a.peggiori]:
            print(f'  :{riga}  {che} (+{quanto})  {testo[:90]}')
    elif a.peggiori:
        print()
        print('Nessun guasto introdotto dall\'italiano da mostrare.')

    if a.prova:
        prova_al_contrario()


if __name__ == '__main__':
    main()
