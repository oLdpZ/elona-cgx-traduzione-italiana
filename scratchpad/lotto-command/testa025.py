# -*- coding: utf-8 -*-
"""Lotto `command-025`: **identificare, scambiare, consegnare**.
Dodici rese e una rinviata, la seconda fetta della zona 15000-15999.

⭐⭐ **Un letterale inglese nudo attaccato in coda a una `lang()`, e nessuno dei
cinque punti ciechi lo vede.** `:15489` e'

    txt lang(itemname(ci) + "を納入した", "You deliver " + itemname(ci) + ". ")
        + "(" + (inv(INV_ITEM_PARAM1, ci) + 5) * inv(INV_ITEM_NUM, ci) + " Guild Point)"

cioe' la `lang()` finisce, e **fuori** dalla parentesi c'e' « Guild Point)» in
inglese, sempre, in tutt'e due le lingue. La resa italiana non lo puo'
raggiungere: e' fuori dal perimetro della voce. ⚠️ E i referti non lo prendono
per un motivo preciso ciascuno — `blocchi_en.py` cerca `if ( en )`, `else_jp.py`
cerca il ramo `else`, `variabili_en.py` cerca l'**assegnamento** di una
variabile, e qui non c'e' ne' un ramo ne' una variabile: c'e' una concatenazione.
✅ Sta a `toppe.jsonl`, e la voce e' **rinviata**: vedi
`scratchpad/toppa-command-15489.py`.
💡 **E il termine era gia' deciso**: `:14115` e' `lang("ギルドポイント", "Guild Point")`
resa «Punti gilda» in un lotto passato. Lo stesso testo, quaranta righe piu' su,
dentro una `lang()` vera. La differenza non e' il testo: e' dove sta.

⚠️⚠️ **E la prima toppa che ho scritto era della specie sbagliata, per una
ragione che vale per tutte.** `applica.py` fa girare le toppe **dopo** il
dizionario (`applica.py:530`), quindi agganciare `cerca` alla riga gia' tradotta
funziona in build — e infatti funzionava. Ma `strumenti/tests/test_toppe.py:104`
pretende che **ogni toppa si applichi al SORGENTE pinnato**, ed e' quella prova a
diventare rossa il giorno in cui upstream riscrive la riga: una toppa agganciata
al testo italiano non ha piu' nessun rapporto col sorgente, e quella prova non
varrebbe piu' niente. Ha parlato la catena, non io.
✅ La forma giusta e' **rinvio + toppa insieme**, gia' in tabella in `LEGGIMI.md`
(`toppa-action-15221.py`, `toppa-proc-24107.py`, `toppa-chara_func-3037.py`).
💡 **La regola generale, che nessuno aveva ancora scritta**: una toppa e una resa
non possono stare sulla stessa riga. O la riga la sistema il dizionario, o la
sistema la toppa — e chi sceglie la toppa deve rinviare la voce.

⚠️ **«Quota» qui non e' una quantita', e' l'incarico della gilda.** L'inglese
usa la stessa parola per la riga di stato (`:15499`, «Quota (40.0s)») e per il
messaggio di compimento (`:15493`, «You fulfill the quota!»), e il progetto l'ha
gia' resa **«Obiettivo»** tre volte — `chara_func.hsp:7247`, `proc.hsp:241` e
`command.hsp:13895` («Al momento non hai nessun obiettivo per la Gilda dei
Maghi»). Si riscuote, non si ridecide.

💡 **Le due righe dell'identificazione prendono la stessa forma, e non per
simmetria estetica.** L'inglese dice «The item is half-identified as X» e «is
fully identified as X»: un participio, che in italiano si accorderebbe col
genere dell'oggetto — e `itemname()` restituisce tanto «la spada» quanto «lo
scudo». ✅ Il nome astratto toglie l'accordo di mezzo: «È X: identificazione
incompleta.» e «È X: identificazione completa.» Stessa manovra del lotto 024,
applicata a una cosa invece che a una persona.

⚠️ **`:15309` e `:15312` nominano gli spazi dell'equipaggiamento, e i nomi
esistono**: `text.hsp:136` fissa 「遠隔」/`Shoot` = «Tiro» e 「手」/`Hand` = «Mano».
Sono le etichette che il giocatore ha davanti mentre legge la domanda, quindi la
resa le scrive maiuscole come le legge sullo schermo, non come parole comuni.

⭐ Copiate senza decidere: «identificazione superiore» (`db_item.hsp:147871`),
«Punti gilda» (`command.hsp:14115`, che serve alla toppa e non alla resa), e
«Obiettivo » per `Quota ` (`chara_func.hsp:7247`, `proc.hsp:241`).
"""
