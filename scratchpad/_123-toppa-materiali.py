# -*- coding: utf-8 -*-
"""123a - La toppa che toglie il suffisso inglese al plurale dei materiali.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_123-toppa-materiali.py
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_123-toppa-materiali.py --scrivi

⚠️⚠️⚠️ **PERCHE' SERVE, E PERCHE' NON E' RINVIABILE.** `material.hsp:120`
costruisce la frase cosi':

    locvar_matgetmain_s = "You get " + n + " " + matname(...) + material_plural + ". "

`material_plural` vale `""`, `"s"` o `"es"`, e lo sceglie uno `switch` scritto a
mano sull'identificativo del materiale (righe 63-118). Finche' `matname()`
restituisce l'inglese, il difetto non si vede. **Nel momento in cui
`material_data.hsp` prende un dizionario**, la stessa riga stampa

    You get 3 carbones.

cioe' un plurale inglese attaccato a una parola italiana. Il dizionario dei
materiali e questa toppa **vanno insieme in un commit solo**: metterne uno
senza l'altro introduce un difetto visibile.

⭐⭐ **E LA FORMA GIUSTA ERA GIA' DECISA.** `glossario.md`, in fondo alla tabella
dei ventisette materiali:

  «L'inglese scrive "You get 3 Pebble.", sgrammaticato anche in inglese;
   l'italiano non puo' scrivere "Ricevi 3 pietruzza" ne' indovinare il plurale
   di una variabile. Il giapponese ha gia' la soluzione — 石ころを3個受け取った,
   col contatore 個 che lascia il nome invariato — e in italiano il contatore e'
   la **parentesi**:  Materiale ricevuto: pietruzza (3).»

Quella forma e' **gia' in gioco** su ventisette righe di `command.hsp` e
ventisette di `chat.hsp`. Questa toppa la porta anche qui, e cosi' le due strade
per ottenere un materiale smettono di parlare due lingue diverse.

ⓘ **Perche' sono due strade.** `matgetmain` ritorna prima di stampare quando il
terzo argomento e' 6 (`material.hsp:49`), ed e' proprio quello che passano
`chat.hsp:21050` e seguenti: quei siti la frase se la scrivono da soli, e sono i
cinquantaquattro gia' resi. `material.hsp:120` serve **tutti gli altri modi** di
ottenere un materiale — la raccolta, lo smontaggio — e nessuno l'aveva toccato.

⚠️ La toppa **non tocca lo `switch`**: `material_plural` resta calcolato e non
viene piu' usato. Toccarlo vorrebbe dire un `cerca` di 56 righe per un guadagno
nullo, e una toppa lunga si sgancia al primo aggiornamento di monte.
"""
import argparse
import io
import json
import os
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
TOPPE = os.path.join(RADICE, 'toppe.jsonl')
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\material.hsp'

MOTIVO = (
    "material.hsp:120 costruisce il plurale col SUFFISSO inglese "
    "(material_plural vale \"\", \"s\" o \"es\", scelto da uno switch a mano sulle "
    "righe 63-118). Appena material_data.hsp prende un dizionario, la stessa "
    "riga stampa «You get 3 carbones»: un plurale inglese su una parola "
    "italiana. La forma giusta era gia' decisa in glossario.md e gia' in gioco "
    "su 27 righe di command.hsp e 27 di chat.hsp — il contatore e' la "
    "PARENTESI, «Materiale ricevuto: pietruzza (3)», come il 個 del giapponese "
    "che lascia il nome invariato. Sito fuori da lang(): il dizionario non lo "
    "raggiunge. Lo switch non si tocca: material_plural resta calcolato e non "
    "piu' usato, perche' un'ancora di 56 righe si sgancerebbe al primo "
    "aggiornamento di monte."
)

CERCA = [
    '\t\tlocvar_matgetmain_s = "You get " + locvar_matgetmain_n + " " '
    '+ matname(matgetmain_arg1) + material_plural + ". "',
]

# ⚠️⚠️ IL TESTO DELLA TOPPA DEVE SOPRAVVIVERE A CP932. La prima stesura aveva
# le virgolette basse e l'ideogramma del contatore dentro un COMMENTO, e
# `applica` e' morto con `UnicodeEncodeError: 'cp932' codec can't encode
# character '\xab'` a meta' lavoro — 842 toppe su 1028 agganciate, build a
# pezzi. Un commento non si vede in gioco, ma passa dallo stesso codificatore
# del codice: qui dentro si scrive ASCII.
SOSTITUISCI = [
    '\t\t; TOPPA IT: il contatore e\' la PARENTESI, non un suffisso.',
    '\t\t; Il nome resta invariato, come il contatore giapponese, e il',
    '\t\t; participio cade su "materiale", che un genere ce l\'ha suo.',
    '\t\t; Stessa forma delle 27 righe gia\' rese in command.hsp e chat.hsp.',
    '\t\tlocvar_matgetmain_s = "Materiale ricevuto: " '
    '+ matname(matgetmain_arg1) + " (" + locvar_matgetmain_n + "). "',
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scrivi', action='store_true')
    scelte = ap.parse_args()

    sorgente = io.open(SORGENTE, encoding='cp932', errors='replace').read()
    ago = '\n'.join(CERCA)

    quante = sorgente.count(ago)
    print()
    print('  ancora cercata in material.hsp : %d volte   (atteso 1)' % quante)

    # ⚠️ Prova al contrario: si CERCA il caso peggiore invece di ipotizzarlo.
    # La riga 55 e' la stessa frase SENZA `material_plural`, dentro un commento
    # `ORIGINAL`. Se l'ancora fosse scritta troppo larga aggancerebbe anche
    # quella, e la toppa cadrebbe sul pezzo commentato.
    quasi = '"You get " + locvar_matgetmain_n + " " + matname(matgetmain_arg1) + ". "'
    print('  la gemella COMMENTATA (:55)    : %d volte nel file' % sorgente.count(quasi))
    print('    e l\'ancora la %s'
          % ('TIENE FUORI, com\'e\' giusto' if quasi not in ago
             else '⚠️ PRENDEREBBE: e\' scritta troppo larga'))

    if quante != 1:
        print()
        print('  ⚠️ la toppa NON si scrive: un\'ancora che non aggancia una volta')
        print('     sola e\' un\'ancora sbagliata.')
        return 1

    toppa = {'file': 'material.hsp', 'motivo': MOTIVO,
             'cerca': CERCA, 'sostituisci': SOSTITUISCI}

    gia = [json.loads(l) for l in io.open(TOPPE, encoding='utf-8') if l.strip()]
    doppia = any(t.get('cerca') == CERCA for t in gia)
    print('  gia\' presente in toppe.jsonl   : %s' % ('SI' if doppia else 'no'))

    if not scelte.scrivi:
        print()
        print('  (prova a vuoto: rilancia con --scrivi per aggiungerla)')
        print()
        return 0

    if doppia:
        print('\n  niente da fare.\n')
        return 0

    with io.open(TOPPE, 'a', encoding='utf-8', newline='\n') as f:
        f.write(json.dumps(toppa, ensure_ascii=False) + '\n')
    print('\n  scritta. toppe: %d -> %d\n' % (len(gia), len(gia) + 1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
