# -*- coding: utf-8 -*-
"""92a - ALICE la formica gigante (`chat.hsp:9794`-`:9853`, 17 firme).

<Alice> la formica gigante (`db_creature.hsp:62712`, `db_card.hsp:6809`) e' la
bestiola della figlia di **<Mary> l'entomologa**, che un esperimento ha
trasformato in mostro: la missione e' rimetterla a posto, ed e' quella resa
nella 90a (`chat.hsp:9854`-`:9982`). Questo blocco e' **l'altra meta'**: qui si
usa la cura, e qui Alice parla.

⭐ ALICE PARLA IN KATAKANA, e il progetto ha gia' la sua regola: **il maiuscolo
lo porta il katakana** (`decisioni.md`, 31a). Sono sessanta le rese cosi' nel
dizionario — `command.hsp:1750` 命令ヲ実行スル «ESEGUO L'ORDINE»,
`db_creature.hsp:52727` 「番ヲシテイマシタ」 «ERO DI GUARDIA.». Le sue battute
vanno in maiuscolo, e non e' una scelta di questo lotto.

LESSICO EREDITATO (non deciso qui):
  - «<Alice> la formica gigante»     db_creature.hsp:62712
  - «<Mary> l'entomologa»            db_creature.hsp:76576
  - 「ギャオオオオオ」 «GRAAAOOO»    db_creature.hsp:68892

⭐⭐⭐ DEROGA 1 — 「アリーヴェデルチ！」 E' UNA BATTUTA DOPPIA, E LA META' CHE
SOPRAVVIVE IN ITALIANO E' QUELLA SBAGLIATA. Alice saluta con *Arrivederci*
scritto in katakana: per un lettore giapponese e' (a) una parola **straniera**,
detta da chi ha appena riavuto la voce, e (b) una parola che comincia per
**アリ**, cioe' *formica* — la stessa sillaba del suo nome, アリッス. Tradotta
«Arrivederci!» in italiano non resta ne' l'una ne' l'altra: diventa un saluto
qualunque.

⭐ Il precedente e' della 90a, sullo **stesso personaggio**: 「ありがとうねぇ、
アリだけに。」 di Mary non e' stato cancellato ma **rifatto** sul canale che
l'italiano ha — la formica — e ne e' uscito «E non e' una formicalita'».
Stessa mossa qui, sullo stesso animale e a nove righe di distanza:

    ARRIFORMICARCI!

Saluto e formica in una parola sola, come nell'originale; e il maiuscolo del
katakana lo rende chiaramente una parola coniata, non un refuso.

⭐⭐ DEROGA 2 — 「サンキューベリマッチ！！」 RESTA IN INGLESE, E LO SUGGERISCE
L'INGLESE STESSO. In giapponese e' *thank you very much* scritto in katakana:
il punto non e' il ringraziamento, e' che lo dice in una **lingua straniera**.
Upstream l'ha capito e ha fatto la mossa simmetrica: la versione inglese non
scrive «Thank you very much», scrive **«Arigatou gozaimashita!»**, cioe'
sostituisce la lingua straniera con un'altra lingua straniera per chi legge.
Per un lettore italiano la lingua straniera del caso e' l'inglese, e la riga
resta **«THANK YOU VERY MUCH!!»**.
⚠️ Non e' una riga «non tradotta»: e' tradotta scegliendo la lingua, come in
`invariati.md` per lo Spazzino di sotterranei (27a).

⚠️ DEROGA 3 — `:9823`, L'ACCORDO SPOSTATO SU UN SOSTANTIVO MIO.
La dinamica dice 「不思議そうにこちらを見ている」. «incuriosita» concorderebbe
con la creatura: qui il sesso e' noto (Alice e' femmina, ed e' «la formica»),
ma la forma che non chiede di saperlo e' **«con aria incuriosita»**, dove
l'accordo si appoggia ad «aria». E' la regola della 91a, applicata dove costa
zero.

⚠️ Le sette voci del menu (`:9816`-`:9822`) sono **azioni**, non parlato: restano
all'infinito, come 「渡す」/「渡さない」 della 90a. E l'ordine dei `chatList` non
e' quello delle righe — 6, 5, 4, 3, 2, 1, 0 — ma il menu li mostra dal piu'
gentile al piu' brutale al contrario: la voce 0, «tenere la medicina in alto»,
e' lo scherzo, e porta a `:9827`.

PERIMETRO: 17 firme su 18 dentro il blocco, zero occorrenze fuori
(`python scratchpad/_85-blocco.py 9794`). La diciottesima e' `:9841`, gia' resa.

MENU: uno, 7 voci — una colonna sola, tetto 58.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte
(la tilde di 「上にあげたー」 passa nei puntini, lezione della 89a).
"""

RESE = {
    # --- il congedo, dopo la guarigione
    9797: "ARRIFORMICARCI!",

    # --- il ringraziamento
    9801: "ANCHE IO VOGLIO RINGRAZIARTI.",
    9802: "PER AVERMI RIDATO IL MIO ASPETTO...",
    9803: "DAVVERO, DAVVERO...",
    9804: "THANK YOU VERY MUCH!!",

    # --- mostro, ma gia' curata: dice solo il suo nome
    9810: "ALICE.",

    # --- mostro: il ruggito e il menu della cura
    9814: "GRAAAOOO!",
    9823: '"(" + cdatan(CDATAN_NAME, tc) + " guarda da questa parte con aria incuriosita.)"',
    9816: "Colpirla con la medicina",
    9817: "Versarle addosso la medicina",
    9818: "Spalmarle la medicina",
    9819: "Iniettarle la medicina",
    9820: "Farle bere la medicina",
    9821: "Darle la medicina",
    9822: "Tenere la medicina in alto, fuori portata",
    9827: "Ecco fatto, tenuta su bene in alto...",
    9829: "...???",
}
