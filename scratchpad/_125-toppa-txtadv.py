# -*- coding: utf-8 -*-
"""125a - Le dodici righe inglesi nude delle slot di `txtadv.hsp`.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_125-toppa-txtadv.py

⚠️⚠️⚠️ **PERCHE'.** Il lotto delle 117 firme chiude tutte le `lang()` del file,
ma `nudi_en.py` (quinto punto cieco, 49a) ne trova **dodici** che non passano da
nessuna `lang()`: `noteadd "3 putits!"` e le sue sorelle. Non hanno firma, non
hanno voce di dizionario e nessun lotto puo' raggiungerle. Sono l'**esito** di
ogni tirata di slot, cioe' la riga che dice al giocatore che cosa ha vinto:
senza toppa, la schermata italiana annuncia i premi in inglese.

⭐ **Sono i simboli dei rulli**, e il progetto ha gia' deciso come si chiamano
tutti e otto. Non si inventa niente:

    putit        `action.hsp:16907`   «il putit», prestito invariabile
    dog          `db_creature.hsp`    «cane»
    bread        `db_item.hsp`        «pane»
    cat          `db_creature.hsp`    «gatto»
    bethel       `db_card.hsp:4612`   «Bethel», nome proprio (il falco bianco)
    larnneire    `db_card.hsp:10566`  «Larnneire», nome proprio
    ehekatl      `chat.hsp:13654`     «Ehekatl», nome proprio
    crimberry    `db_item.hsp:139482` «crimberry», prestito invariabile

⚠️ **Il plurale segue l'italiano, non l'inglese.** «cani», «pani», «gatti» si
flettono; «putit» e «crimberry» sono prestiti invariabili — `db_item.hsp` scrive
gia' «crimberry» al singolare e al plurale — e i tre nomi propri non si
flettono affatto. L'inglese mette la -s a tutti e otto, compresi i nomi delle
persone («3 larnneires!»), e quello e' il suo modo, non il nostro.

⚠️ La toppa e' in **ASCII, commenti compresi** (123a), e i tre nomi propri lo
sono gia'.

ⓘ Larghezza: sono righe di **messaggio**, tetto di monte 71 caratteri
(`_125-larghezze-txtadv.py`). La piu' lunga qui e' «3 crimberry!», 12.
"""
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
TOPPE = os.path.join(RADICE, 'toppe.jsonl')

# riga: (inglese, italiano). L'ordine e' quello del sorgente.
VOCI = [
    (1359, '3 putits!', '3 putit!'),
    (1373, '3 dogs!', '3 cani!'),
    (1389, '3 breads!', '3 pani!'),
    (1405, '3 cats!', '3 gatti!'),
    (1413, '3 bethels!', '3 Bethel!'),
    (1421, '3 larnneires!', '3 Larnneire!'),
    (1429, '3 ehekatls!', '3 Ehekatl!'),
    (1462, '3 crimberries!', '3 crimberry!'),
    (1469, '2 breads!', '2 pani!'),
    (1485, '2 larnneires!', '2 Larnneire!'),
    (1501, '2 bethels!', '2 Bethel!'),
    (1518, '2 crimberries!', '2 crimberry!'),
]

MOTIVO = (
    "txtadv.hsp, l'esito di una tirata di slot (*adv_casinoSlots_WHILE_END). "
    "LETTERALE INGLESE NUDO: `noteadd \"%s\"` non passa da nessuna lang(), "
    "quindi non ha firma, non ha voce di dizionario e nessun lotto puo' "
    "raggiungerlo (quinto punto cieco, nudi_en.py, 49a). E' la riga che dice al "
    "giocatore che combinazione ha fatto, e senza toppa resta inglese in mezzo "
    "a una schermata tradotta. Il nome del simbolo viene dal dizionario, non "
    "inventato; il plurale segue l'italiano, che sui prestiti (putit, "
    "crimberry) e sui nomi propri (Bethel, Larnneire, Ehekatl) non flette."
)


def main():
    toppe = []
    for riga, inglese, italiano in VOCI:
        cerca = '\t\t\tnoteadd "%s"' % inglese
        sostituisci = '\t\t\tnoteadd "%s"' % italiano
        assert all(ord(c) < 128 for c in cerca + sostituisci), (riga, italiano)
        toppe.append({
            'file': 'txtadv.hsp',
            'motivo': MOTIVO % inglese,
            'cerca': [cerca],
            'sostituisci': [sostituisci],
        })
    with io.open(TOPPE, 'a', encoding='utf-8', newline='\n') as f:
        for t in toppe:
            f.write(json.dumps(t, ensure_ascii=False) + '\n')
    print('%d toppe aggiunte a %s' % (len(toppe), TOPPE))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
