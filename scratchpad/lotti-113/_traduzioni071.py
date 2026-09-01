# -*- coding: utf-8 -*-
"""Le rese del lotto 071 — LE ALGHE: `FILTER_ENVIRONMENT_SEABED` si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 071 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa071.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️⚠️ Forma, da `_forma.py 071`: **0 righe su 6** con lo spazio prima del `\\n`,
**0 su 6** con lo spazio dopo il `#`. Tutte e sei senza, nessuna eccezione.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 071`: **+6** per 6 rese,
nessuna gemella.

⚠️⚠️⚠️ **TRE RIGHE SU SEI HANNO IL GIAPPONESE VUOTO.** Sono le `description(2)`
— `:44865`, `:44928`, `:44991` — e l'inglese un testo ce l'ha. E' il caso di
`:89358` e non quello di `:129299`: la domanda non e' «manca il giapponese?» ma
«esiste una fonte?». Si rendono.

⚠️⚠️⚠️ **E PER QUESTO L'AVVISO DI `_120-serie-bacchette` E' FALSO.** La rete
dice che `:44928` e `:44991` devono avere rese **identiche** «perche' il
giapponese e' lo stesso». Il giapponese e' lo stesso perche' e' **vuoto** in
tutt'e due, e due stringhe vuote sono uguali a ogni rete che le confronti.
L'inglese li distingue («Giant» contro «Huge») e il giapponese della
`description(3)` **degli stessi oggetti** li distingue davvero:

    :44929  巨大な海藻だ  ->  «Un'alga gigantesca»   (kombu)
    :44992  大きな海藻だ  ->  «Un'alga grande»       (wakame)

Quelle due rese sono gia' nel dizionario, e sono l'arbitro. Le tre rese
dell'indice 2 aprono con la stessa parola dell'indice 3 dello stesso oggetto.

ⓘ `_gia-reso 071`: 0 su 6. `_119-togli-rinviate 071`: nessuna rinviata.
"""

IT = {
    # =====================================================================
    # L'INDICE 0 — DAL GIAPPONESE
    # =====================================================================
    # ⓘ 海藻 -> «alga» (glossario). `mozuku`, `kombu` e `wakame` sono NOMI
    #   invariati (invariati.md, tre voci): non compaiono nel corpo, che
    #   parla sempre di «un'alga».

    # 喉越し e' «come scende in gola», e l'italiano ce l'ha di suo: di una
    # bevanda o di un cibo si dice che «scende bene». 酢漬け -> «sott'aceto».
    44863: "Un'alga dal corpo lungo, sottile e ramificato, che a volte passa il metro. La consistenza è ottima e scende bene in gola, ma la si mette quasi sempre sott'aceto, e per questo non piace a molti.\\n#~Alghe e Piante Marine: la Differenza~",

    # ダシ non e' nel dizionario, ma «brodo» ci sta gia' due volte, nelle due
    # righe del mochi. コツがいる -> «richiede il suo mestiere».
    44926: "Un'alga che diventa lunghissima. Ha molta acqua dentro, e perciò pesa parecchio. Farla seccare richiede il suo mestiere, ma da secca se ne ricava un buon brodo.\\n#~Alghe e Piante Marine: la Differenza~",

    # 具材 -> «ingrediente» (dizionario, le due righe del mochi).
    # 重宝されてきた e' «e' stata tenuta cara»: il giapponese guarda al passato
    # che dura, e l'inglese lo dice con «has long been valued».
    44989: "Un'alga di taglia grande. Assorbe il nutrimento del mare e si moltiplica in fretta. In certe regioni, fin da tempi antichi, è tenuta cara come ingrediente di piatti d'ogni sorta.\\n#~Alghe e Piante Marine: la Differenza~",

    # =====================================================================
    # L'INDICE 2 — GIAPPONESE VUOTO, SI RENDE DALL'INGLESE
    # =====================================================================
    # ⭐⭐⭐ E le tre NON sono uguali: l'arbitro e' l'indice 3 degli stessi
    #    tre oggetti, che il dizionario ha gia' reso dal giapponese.
    #    «You can eat it I guess» ha l'esitazione dentro, e l'indice 3 dice
    #    «Si può mangiare»: la resa tiene quella e ci aggiunge il «credo».

    44865: "Un'alga. Si può mangiare, credo.\\n#~Rapporto di Identificazione: categoria <Alghe>~",

    # ⚠️ «Giant» -> gigantesca, come :44929 (巨大な). NON uguale alla riga sotto.
    44928: "Un'alga gigantesca. Si può mangiare, credo.\\n#~Rapporto di Identificazione: categoria <Alghe>~",

    # ⚠️ «Huge» -> grande, come :44992 (大きな). NON uguale alla riga sopra.
    44991: "Un'alga grande. Si può mangiare, credo.\\n#~Rapporto di Identificazione: categoria <Alghe>~",
}
