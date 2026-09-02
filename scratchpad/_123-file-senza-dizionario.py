# -*- coding: utf-8 -*-
"""123a - Quali file hanno `lang()` nel sorgente e NON hanno un dizionario.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_123-file-senza-dizionario.py

⚠️⚠️⚠️ **PERCHE' ESISTE.** Dalla 123a **ogni file con un dizionario dice
`⭐ CHIUSO`**: `_97-quanto-resta` legge «TOTALE da fare 0» e `verifica
--dizionario` legge zero da ritradurre dappertutto. Ma `perimetro.py` dice
**90%**, e i due numeri non si contraddicono: `_97-quanto-resta` guarda **solo i
file che HANNO un dizionario**, e i file che non ce l'hanno non compaiono
nemmeno come riga.

⭐ E' la forma peggiore di zero: non «zero perche' e' finito», ma **zero perche'
non e' stato chiesto**. Questo strumento fa la domanda al posto giusto — quali
file portano `lang()` e nessuno ha mai estratto — e stampa **quante** stringhe
ci sono dentro, cosi' lo zero di `_97-quanto-resta` si legge accanto al numero
che gli manca.

⚠️⚠️ **LE FIRME DISTINTE E LE OCCORRENZE SONO DUE NUMERI DIVERSI**, e la prima
stesura di questo strumento contava le seconde: diceva **447** dove
`perimetro.py` dice **355**, e i due referti non si potevano confrontare.
`perimetro.firme_lang()` raccoglie gli argomenti inglesi in un **insieme**,
quindi due `lang()` con lo stesso inglese sono **una** firma — ed e' giusto
cosi', perche' una resa le copre tutt'e due. Qui si riusa quella funzione
invece di riscriverla: la colonna «firme» deve sommare **esattamente** al «di
cui in file mai estratti» del perimetro, e la colonna «lang()» sta accanto solo
per far vedere quante ripetizioni ci sono.
"""
import glob
import io
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
DIZIONARIO = os.path.join(RADICE, 'dizionario')
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'

sys.path.insert(0, QUI)
import perimetro  # noqa: E402  — per `firme_lang`, che e' la definizione buona
from strumenti.estrai import estrai_da_testo  # noqa: E402  — il conto VERO

LANG = re.compile(r'\blang\s*\(')


def main():
    con_dizionario = {os.path.basename(p).replace('.jsonl', '')
                      for p in glob.glob(os.path.join(DIZIONARIO, '*.jsonl'))}

    senza, con = [], []
    for percorso in sorted(glob.glob(os.path.join(SORGENTE, '*.hsp'))):
        nome = os.path.basename(percorso)
        testo = io.open(percorso, encoding='cp932', errors='replace').read()
        tutte = perimetro.firme_lang(testo)
        firme = len(tutte)
        if firme == 0:
            continue
        # ⚠️⚠️ 124a: NON OGNI FIRMA E' LAVORO. `perimetro.firme_lang()` raccoglie
        # l'argomento inglese di ogni `lang()`, e alcune non portano **nessun
        # letterale**: `font lang(cfg_font1, cfg_font2)` sceglie il carattere,
        # `lang(cnvrank(p), ...)` passa un valore gia' reso altrove. Sono 45 in
        # tutto il sorgente, di cui 26 sono `cfg_font2`. Il perimetro le conta e
        # va bene — e' un denominatore, non una lista di compiti — ma in QUESTO
        # referto, che dice «ecco il lavoro che nessuno ha chiesto», una riga
        # che non si puo' tradurre gonfia il numero. `material.hsp` diceva 18 e
        # il lavoro vero era 17: la diciottesima era il carattere.
        muti = len([x for x in tutte if '"' not in x])
        # ⚠️⚠️ 124a, seconda correzione: «da fare» NON e' `firme - muti`. Sono
        # due riconoscitori diversi — `firme_lang()` approssima con un
        # analizzatore di parentesi e sbaglia per difetto del 2-4% (le righe con
        # piu' `lang()`, le forme annidate) — e la sottrazione fra i due dava
        # **166** dove `estrai` ne trova **167**: uno in `net.hsp`. Il numero che
        # conta e' quello di `estrai`, perche' e' lo stesso codice che poi scrive
        # il lotto: «da fare» deve essere il numero di righe che si aprono
        # domani, non una stima.
        da_fare = len({v['firma'] for v in estrai_da_testo(nome, testo)}) \
            if nome not in con_dizionario else 0
        (con if nome in con_dizionario else senza).append(
            (firme, len(LANG.findall(testo)), muti, da_fare, nome))

    senza.sort(reverse=True)
    print()
    print('  I FILE CON `lang()` E SENZA DIZIONARIO')
    print()
    print('   firme   lang()     muti   da fare   file')
    print('  ' + '-' * 58)
    for firme, occorrenze, muti, da_fare, nome in senza:
        print('  %6d   %6d   %6d   %7d   %s'
              % (firme, occorrenze, muti, da_fare, nome))
    print('  ' + '-' * 58)
    print('  %6d   %6d   %6d   %7d   TOTALE in %d file'
          % (sum(f for f, _, _, _, _ in senza),
             sum(o for _, o, _, _, _ in senza),
             sum(m for _, _, m, _, _ in senza),
             sum(d for _, _, _, d, _ in senza), len(senza)))
    print()
    print('  ⚠️ «firme» e «da fare» vengono da DUE riconoscitori: il primo e\' la')
    print('    stima del perimetro, il secondo e\' `estrai`, cioe\' il codice che')
    print('    scrive davvero il lotto. Non tornano per sottrazione, e il numero')
    print('    su cui si lavora e\' il secondo.')
    print()
    print('  ⓘ referto, non cancello. Il valore atteso NON e\' zero: e\' il')
    print('    numero che `_97-quanto-resta` non puo\' vedere, e la colonna')
    print('    «firme» deve fare il «di cui in file mai estratti» del perimetro.')
    print()

    # ⚠️ Prova al contrario: si CERCA il caso peggiore invece di ipotizzarlo.
    # Se la rete confondesse i due insiemi, il file con dizionario piu' carico
    # comparirebbe nell'elenco qui sopra. Si stampa quale e' e quanto pesa, non
    # un ✅: un esito booleano nasconde la differenza fra «ho cercato il caso
    # peggiore» e «non l'ho cercato abbastanza».
    if con:
        peggiore = max(con)
        nomi_senza = [n for _, _, _, _, n in senza]
        print('  prova al contrario: il file CON dizionario piu\' carico e\' %s'
              % peggiore[4])
        print('    (%d firme, %d lang()), e la rete %s'
              % (peggiore[0], peggiore[1],
                 'lo TACE, com\'e\' giusto'
                 if peggiore[4] not in nomi_senza else '⚠️ LO STAMPA: e\' rotta'))
    # ⓘ 124a: e due file dell'elenco sono INTERAMENTE muti — `custom_pet.hsp` e
    #   `custom_dmgpop.hsp` hanno una firma sola ciascuno, ed e' `cfg_font2`.
    #   Non si chiuderanno mai «traducendoli»: sono gia' finiti.
    muti_interi = [n for f, _, m, d, n in senza if d == 0]
    if muti_interi:
        print()
        print('  ⓘ file senza NIENTE da tradurre (ogni firma e\' muta): %s'
              % ', '.join(muti_interi))
    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
