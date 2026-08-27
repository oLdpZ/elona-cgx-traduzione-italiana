# -*- coding: utf-8 -*-
"""Le rese del lotto 018 (gli AMULETI, `FILTER_ACCESSORY_AMULET`), per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 018 scratchpad/lotti-111

**13 righe del sorgente, 13 firme**, 13 giapponesi distinti. Nove righe su
tredici finiscono in 首輪だ.

### ⚠️⚠️ 首輪 E' «COLLANA» NELLE DESCRIZIONI E «AMULETO» NEI NOMI

Il dizionario ha **tutt'e due**, e non e' un'incoerenza da riparare:

    首輪         -> collana            (la voce generica)
    結婚首輪     -> amuleto nuziale    (i nomi degli oggetti)
    細工首輪     -> amuleto ingioiellato
    装飾首輪     -> amuleto decorativo
    《暴風の首輪》 -> <Collare della Tempesta>

I nomi sono stati decisi contro l'**inglese** («engagement amulet»), che li' e'
la fonte del nome; la descrizione invece dice la parola generica, e la parola
generica e' «collana». Le nove descrizioni prendono «collana».

⚠️ **L'eccezione e' `:76250`**, dove la descrizione **nomina l'oggetto che
l'artefatto diventa** e quell'oggetto ha un nome suo: «Collare della Tempesta».
Li' si scrive «collare», se no la riga contraddice il nome una riga sopra.

### ⭐⭐ TRE RITROVAMENTI, E DUE SONO RIGHE INTERE GIA' SCRITTE

- `:99451`, l'amuleto nuziale: 「人に渡すと友好度が上がるアイテムだ」 e' gia'
  in questo file, reso **«Dato a qualcuno, alza la simpatia.»**. La riga
  dell'amuleto e' la stessa cosa piu' 返ってくることはない, e diventa **«Data a
  qualcuno, alza la simpatia. Non torna indietro.»** — non una resa nuova, la
  stessa con la coda.
- `:82679` e `:82745`: 追加打撃 e 追加射撃 sono **potenziamenti** che il
  giocatore legge sull'equipaggiamento, gia' resi «Aumenta la probabilità di un
  attacco corpo a corpo extra» e «...di un attacco a distanza extra» (e come
  colonne, «Mischia+» e «Tiro+»). Le due collane li ripetono, in fila.
- 魔力 e' **«potere magico»**, quasi duecento volte.

### ⭐ DUE COPPIE CHE SI SCRIVONO INSIEME

    想いのこめられた首輪 -> in cui è racchiuso un sentimento     (:99594)
    魔力のこめられた首輪 -> in cui è racchiuso il potere magico  (:99738)

    追加打撃の機会を得られる -> la probabilità di un attacco extra in mischia
    追加射撃の機会を得られる -> la probabilità di un attacco extra a distanza

### ⚠️ 〜のついた, terza volta in tre lotti

宝石のついた首輪 (:99810) e 羽のついた帽子 (:100135, lotto 017) hanno la stessa
costruzione e prendono lo stesso «con»: «con una gemma», «con una piuma». Come
沢山のベルトがついた服 del lotto 015, «pieno di cinghie».
"""

IT = {
    # === il dono divino, quarto dei quattro (vedi il lotto 017)
    76250: "Se lo indossi, si trasforma in un collare.",

    # === le due collane dei potenziamenti, che si leggono in coppia
    82679: "Una collana che dà la probabilità di un attacco extra in mischia.",
    82745: "Una collana che dà la probabilità di un attacco extra a distanza.",

    # === le due collane della こめられた, che si leggono in coppia
    99594: "Una collana in cui è racchiuso un sentimento.",
    99738: "Una collana in cui è racchiuso il potere magico.",

    # === le altre collane
    # ⚠️ «degli dèi» e' stato BOCCIATO dalla rete dell'accento: la degradazione
    #    fa «de'i», che a schermo non si legge. Si cambia parola, non si toglie
    #    l'accento — e «parola divina» dice la stessa cosa di 神の発言.
    81539: "Una collana che fa sentire la parola divina.",
    83904: "Una collana che protegge dalle disgrazie.",
    99522: "Una collana ben lucidata.",
    99666: "Una collana per proteggersi.",
    99810: "Una collana con una gemma.",
    126650: "Una collana con delle decorazioni.",

    # === le due che non dicono «collana»
    99451: "Data a qualcuno, alza la simpatia. Non torna indietro.",
    62466: "Una sfera che rinforza lo spirito.",
}
