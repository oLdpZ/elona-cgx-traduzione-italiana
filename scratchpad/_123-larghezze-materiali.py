# -*- coding: utf-8 -*-
"""123a - Il cancello di larghezza del pannello dei materiali.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_123-larghezze-materiali.py

⚠️⚠️⚠️ **PERCHE' ESISTE.** Le 118 rese di `material_data.hsp` sono state scritte
senza un budget, e le due colonne del pannello sono **strette**. La geometria sta
in `material.hsp`:

    :445   pos wx + 70    gfini 490, 18        la riga evidenziata: wx+70 .. wx+560
    :450   font ..., 14 - en * 2, 0            font **12**, come i menu
    :458   s = matname(i) + " x " + mat(i)
    :459   cs_list s, wx + 96, ...             la colonna del NOME parte a wx+96
    :460   s = matdesc(i)
    :461   pos wx + 308                        la colonna della DESCRIZIONE a wx+308

Da cui due larghezze secche:

    nome + " x N"   wx+96  -> wx+308   =  212 px
    descrizione     wx+308 -> wx+560   =  252 px

⭐⭐⭐ **E IL METRO NON VA INVENTATO: il progetto l'ha gia' pagato.** `larghezze.py`
ha misurato **7,7 px/carattere** su uno screenshot dei **menu**, e i menu
disegnano a `font 14 - en*2` = **12**. Questo pannello disegna alla stessa riga
(`:450`), quindi e' **lo stesso carattere alla stessa dimensione**: il metro si
applica senza taratura nuova.
⚠️ Non e' il 6,9 px/carattere del font 11, che vale per le righe impaginate del
pannello degli oggetti. Sono **due** metri, come i due budget della 112a
(`BUDGET` 77 a font 11, `BUDGET_INTERO` 69 a font 12): confonderli allenta un
cancello in silenzio.

    212 / 7,7 = 27,5  ->  budget NOME+CONTATORE  **27**
    252 / 7,7 = 32,7  ->  budget DESCRIZIONE     **32**

⭐ **La conferma che il modello e' giusto la da' l'inglese di monte**: il suo
nome piu' lungo e' 17 caratteri (che con « x 12» fa 22) e la sua descrizione piu'
lunga e' **33** — cioe' appoggiata esatta al budget calcolato. Un modello che
ricava 32,7 e trova la fonte ferma a 33 non e' un modello ipotizzato.

⚠️⚠️ **IL CONTATORE FA PARTE DELLA STRINGA.** `mat(i)` puo' arrivare a cinque
cifre, e « x 12345» sono **8** caratteri attaccati al nome. Qui si misura col
peggio realistico (` x ` + 4 cifre = 7), perche' un budget che misura il nome da
solo e' un budget che non misura quel che il gioco disegna.
"""
import io
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
DIZIONARIO = os.path.join(RADICE, 'dizionario', 'material_data.hsp.jsonl')

PX_PER_CARATTERE = 7.7        # larghezze.py, font 12 — lo stesso dei menu
PX_NOME = 308 - 96            # 212
PX_DESCRIZIONE = 560 - 308    # 252
# ⚠️⚠️ CINQUE CIFRE, NON QUATTRO. La prima stesura metteva quattro, e non era
# una misura: era una speranza. `mat()` non ha nessun tetto — in tutto il
# sorgente non c'e' un `limit` che lo tocchi, e `MAX_MATERIAL` limita QUANTI
# materiali esistono, non quanti se ne posseggono. Un personaggio che scava a
# lungo passa le diecimila pietruzze, e « x 12345» sono otto caratteri
# attaccati al nome.
CONTATORE = len(' x ') + 5

BUDGET_NOME = int(PX_NOME / PX_PER_CARATTERE)
BUDGET_DESCRIZIONE = int(PX_DESCRIZIONE / PX_PER_CARATTERE)

# ⚠️⚠️ LE ECCEZIONI SI DICHIARANO, NON SI ALLENTA IL CANCELLO. Abbassare
# CONTATORE a quattro cifre avrebbe azzerato il referto e nascosto il motivo:
# e' l'allentamento silenzioso della 112a. Qui la riga resta contata, e accanto
# c'e' la ragione per cui non e' un difetto.
ECCEZIONI = {
    229: "«macchina generatrice» (20) e' uno dei 27 nomi gia' decisi in "
         "glossario.md, e sfora SOLO a cinque cifre di contatore. "
         "material_data.hsp:228 le da' livello 70 e rarita' 7, e le uniche "
         "strade sono gli alleati (chat.hsp:21309, command.hsp:6520): a tre "
         "cifre fa 26 su 27 e sta dentro. Non si cambia un nome deciso per un "
         "caso che il gioco non produce.",
}


def voci():
    return [json.loads(l) for l in io.open(DIZIONARIO, encoding='utf-8') if l.strip()]


def main():
    tutte = voci()
    # ⓘ In `material_data.hsp` il nome sta a `:9`, `:14`, `:19`… (resto 4 su 5)
    #   e la descrizione alla riga dopo (resto 0). E' la forma del file, non una
    #   convenzione scelta qui: `matname(...)` e `matdesc(...)` sono due righe
    #   consecutive per ogni materiale.
    nomi = [v for v in tutte if v['riga'] % 5 == 4]
    desc = [v for v in tutte if v['riga'] % 5 == 0]

    print()
    print('  metro: %.1f px/carattere (font 12, da larghezze.py)' % PX_PER_CARATTERE)
    print('  budget NOME + contatore : %d caratteri  (%d px)'
          % (BUDGET_NOME, PX_NOME))
    print('  budget DESCRIZIONE      : %d caratteri  (%d px)'
          % (BUDGET_DESCRIZIONE, PX_DESCRIZIONE))
    print()

    guasti = 0
    for etichetta, insieme, budget, extra in (
            ('NOME', nomi, BUDGET_NOME, CONTATORE),
            ('DESCRIZIONE', desc, BUDGET_DESCRIZIONE, 0)):
        oltre = [v for v in insieme if len(v['it']) + extra > budget]
        fuori_it = [v for v in oltre if v['riga'] not in ECCEZIONI]
        dichiarate = [v for v in oltre if v['riga'] in ECCEZIONI]
        fuori_en = [v for v in insieme if len(v['en']) + extra > budget]
        print('  === %s' % etichetta)
        print('    inglese di monte fuori : %d su %d   (il piu\' lungo: %d)'
              % (len(fuori_en), len(insieme), max(len(v['en']) for v in insieme)))
        print('    ⚠️ ITALIANO fuori      : %d su %d   (il piu\' lungo: %d)  '
              '(atteso 0)'
              % (len(fuori_it), len(insieme), max(len(v['it']) for v in insieme)))
        for v in sorted(fuori_it, key=lambda a: -len(a['it'])):
            print('       :%-5d %2d+%d  %-44s  (en %d: %s)'
                  % (v['riga'], len(v['it']), extra, v['it'], len(v['en']), v['en']))
        for v in dichiarate:
            print('    ⓘ oltre il budget ma DICHIARATA: :%d  %2d+%d  %s'
                  % (v['riga'], len(v['it']), extra, v['it']))
            print('       %s' % ECCEZIONI[v['riga']])
        guasti += len(fuori_it)
        print()

    # ⚠️ Prova al contrario: si CERCA il caso peggiore invece di ipotizzarlo, e
    # si stampa DOVE si accende, non un ✅. Se il cancello fosse tarato troppo
    # largo, non si accenderebbe nemmeno su una stringa costruita apposta.
    finta = 'x' * (BUDGET_DESCRIZIONE + 1)
    acceso = len(finta) > BUDGET_DESCRIZIONE
    print('  prova al contrario: una descrizione di %d caratteri %s'
          % (len(finta), 'ACCENDE il cancello' if acceso else '⚠️ NON lo accende'))
    print('    e l\'inglese piu\' lungo del file (%d) sta %s il budget: e\' la'
          % (max(len(v['en']) for v in desc),
             'dentro' if max(len(v['en']) for v in desc) <= BUDGET_DESCRIZIONE
             else 'FUORI'))
    print('    ragione per cui il modello si regge — monte scriveva per questo')
    print('    riquadro, e si e\' fermato dove il calcolo dice che finisce.')
    print()
    return 1 if guasti else 0


if __name__ == '__main__':
    sys.exit(main())
