# -*- coding: utf-8 -*-
"""125a - Le tre righe inglesi nude di `custom_itemenchantment.hsp`.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_125-toppa-itemench.py

⚠️⚠️⚠️ **PERCHE'.** Il lotto delle 26 firme chiude tutte le `lang()` del file,
ma `nudi_en.py` (quinto punto cieco, 49a) ne trova **tre** che non passano da
nessuna `lang()`: non hanno firma, non hanno voce di dizionario e nessun lotto
puo' raggiungerle. Tutt'e tre si leggono nel menu della disincantazione, cioe'
nella stessa schermata che il lotto rende italiana:

    :256   s = "[" + p_gold + " gold] " + s
    :278   s = "Try to remove the enchantment? (" + cnvitemname(p_item2) + ")"
    :280   s = "Remove the enchantment? (" + cnvitemname(p_item2) + ")"

`:278` e `:280` finiscono in `chatList 2, lang(s, s)` (`:282`): l'argomento
giapponese e quello inglese sono **la stessa variabile**, quindi la riga e' in
inglese per tutte e due le lingue e `estrai` non ha niente da estrarre.
Senza toppa il giocatore italiano legge «Remove the enchantment? (pozione di
evoluzione)» sotto a «Potenziare l'incanto? (pozione di mutazione)».

⭐⭐⭐ **`:280` e `:278` SONO LA STESSA VOCE IN DUE STATI, E L'INGLESE NE
NASCONDE UNO.** Li distingue `:279`, `p_rem == val(1)`, ed e' **la stessa
condizione** che a `:324` sceglie il messaggio finale: «...The enchantment is
removed!» contro «...The enchantment is weakened!». Quindi `:278` non e' un
tentativo incerto di cancellare — e' l'**indebolimento**, e il codice lo dice
due volte. L'inglese scrive «Try to remove», che e' vago dove il codice e'
preciso: la resa segue il codice, che e' la quinta fonte (110a).

    :278   p_rem != val(1)   ->  encremove parziale  ->  «indebolito» (:327)
    :280   p_rem == val(1)   ->  encremove totale    ->  «cancellato» (:325)

⚠️⚠️⚠️ **E LE TRE VOCI DI QUESTA FINESTRA NON CI STAVANO.** Il tetto della
pergamena e' **58 caratteri** (`strumenti/menu_dialogo.py`) e dentro la
parentesi ci va `cnvitemname()`, che per la **pergamena di acquisizione di
attributi** — `p_item2` quando l'incantamento e' Ragnarok o succhiasangue
(`:227`, `:232`) — vale **38 caratteri** contro i 24 di «scroll of gain
attribute». Le prime stesure sforavano di 4 e di 14 dove l'inglese ci sta:

    "Provare a cancellare l'incanto? (pergamena di ...)"   72   ✗
    "Cancellare l'incanto? (pergamena di ...)"             62   ✗
    "Potenziare l'incanto? (pergamena di ...)"             62   ✗

⭐ Restano **18 caratteri** per l'etichetta, e allora l'etichetta e' il verbo
solo. Le tre voci diventano simmetriche fra loro e con i tre messaggi finali
(«Potenziamento», «Indebolimento», «Cancellazione»), e il nome dell'incantamento
non serve ripeterlo: lo dice il testo della finestra due righe sopra (`:274`).

    "Potenziare? (" / "Indebolire? (" / "Cancellare? ("   52 nel caso peggiore

⚠️⚠️ **E QUESTO SFORO NESSUN CANCELLO LO VEDEVA, DUE VOLTE.**
`menu_dialogo` legge il **dizionario** (`voci_di_menu`, `:491`): una riga messa
da una toppa non ha voce di dizionario, quindi `:278` e `:280` non le misura
proprio. E `:276`, che nel dizionario c'e', lo misura **senza il nome
dell'oggetto**, perche' `reso()` scioglie i segnaposto e una chiamata di
funzione non porta caratteri. Il cancello diceva «0 su 1383» con tre voci fuori
misura dentro. Le misura `scratchpad/_125-larghezze-menu-incanti.py`.

⚠️ **`:256` non e' una frase, e' un'etichetta di prezzo** in testa a ogni voce
della lista degli incantamenti. «gold» diventa **«oro»** e non «monete d'oro»:
e' la forma corta gia' decisa nel glossario per `<N gp>` (`text.hsp:193`), ed e'
quella giusta qui perche' quella lista puo' passare le dieci voci e allora
`chat.hsp:25166` la tronca a **24 caratteri netti**.

⚠️ La toppa e' in **ASCII, commenti compresi** (123a).
"""
import io
import json
import os

QUI = os.path.dirname(os.path.abspath(__file__))
RADICE = os.path.dirname(QUI)
TOPPE = os.path.join(RADICE, 'toppe.jsonl')

MOTIVO_COMUNE = (
    "custom_itemenchantment.hsp, il menu della disincantazione "
    "(*extrachat_disenchantment). LETTERALE INGLESE NUDO: non passa da nessuna "
    "lang(), quindi non ha firma, non ha voce di dizionario e nessun lotto puo' "
    "raggiungerlo (quinto punto cieco, nudi_en.py, 49a). "
)


def main():
    toppe = [
        {
            'file': 'custom_itemenchantment.hsp',
            'motivo': MOTIVO_COMUNE + (
                "E' l'etichetta del prezzo in testa a ogni voce della lista "
                "degli incantamenti (:256). Forma corta 'oro' e non 'monete "
                "d'oro' perche' la lista puo' passare le dieci voci, e allora "
                "chat.hsp:25166 la tronca a 24 caratteri netti."),
            'cerca': ['            s = "[" + p_gold + " gold] " + s'],
            'sostituisci': [
                '            ; TOPPA IT: etichetta di prezzo, forma corta come'
                ' <N oro> di text.hsp:193.',
                '            s = "[" + p_gold + " oro] " + s',
            ],
        },
        {
            'file': 'custom_itemenchantment.hsp',
            'motivo': MOTIVO_COMUNE + (
                "E' la voce di menu :278, che finisce in chatList 2, "
                "lang(s, s) a :282: i due argomenti della lang() sono la "
                "stessa variabile, quindi la riga e' inglese anche in "
                "giapponese. ⭐ E' l'INDEBOLIMENTO, non un tentativo incerto: "
                ":279 sceglie questa quando p_rem != val(1), che e' la stessa "
                "condizione con cui :324 stampa «...The enchantment is "
                "weakened!». L'inglese scrive «Try to remove» ed e' vago dove "
                "il codice e' preciso. ⚠️ Etichetta col verbo solo perche' "
                "cnvitemname(p_item2) puo' essere «pergamena di acquisizione "
                "di attributi», 38 caratteri su un tetto di 58."),
            'cerca': ['        s = "Try to remove the enchantment? (" '
                      '+ cnvitemname(p_item2) + ")"'],
            'sostituisci': [
                '        ; TOPPA IT: voce di menu, letta da chatList 2 a :282.',
                '        ; Indebolire e non "provare a cancellare": :279 e :324',
                '        ; hanno la stessa condizione, e :324 dice "weakened".',
                '        s = "Indebolire? (" + cnvitemname(p_item2) + ")"',
            ],
        },
        {
            'file': 'custom_itemenchantment.hsp',
            'motivo': MOTIVO_COMUNE + (
                "E' la voce di menu :280, la gemella di :278 nello stato "
                "'si cancella per intero' (p_rem == val(1), :279, la stessa "
                "condizione che a :325 stampa «...The enchantment is "
                "removed!»). Stessa etichetta col verbo solo."),
            'cerca': ['            s = "Remove the enchantment? (" '
                      '+ cnvitemname(p_item2) + ")"'],
            'sostituisci': [
                '            ; TOPPA IT: voce di menu, la gemella di :278.',
                '            s = "Cancellare? (" + cnvitemname(p_item2) + ")"',
            ],
        },
    ]
    for t in toppe:
        testo = ''.join(t['cerca'] + t['sostituisci'])
        assert all(ord(c) < 128 for c in testo), 'la toppa non e\' ASCII'
    with io.open(TOPPE, 'a', encoding='utf-8', newline='\n') as f:
        for t in toppe:
            f.write(json.dumps(t, ensure_ascii=False) + '\n')
    print('%d toppe aggiunte a %s' % (len(toppe), TOPPE))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
