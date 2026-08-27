# -*- coding: utf-8 -*-
"""111a - Lotto 018 di `db_item.hsp`: il rapporto degli AMULETI.

`FILTER_ACCESSORY_AMULET`, `description(3)`: **13 righe del sorgente, 13
firme**, 13 giapponesi distinti. Nove righe su tredici finiscono in 首輪だ.

### ⚠️⚠️ 首輪 E' «COLLANA» NELLE DESCRIZIONI E «AMULETO» NEI NOMI

Il dizionario ha **tutt'e due**, e non e' un'incoerenza da riparare:

    首輪          -> collana              (la voce generica)
    結婚首輪      -> amuleto nuziale      (i nomi degli oggetti)
    細工首輪      -> amuleto ingioiellato
    装飾首輪      -> amuleto decorativo
    《暴風の首輪》 -> <Collare della Tempesta>

I nomi sono stati decisi contro l'**inglese** («engagement amulet»), che li' e'
la fonte del nome; la descrizione invece dice la parola generica, e la parola
generica e' «collana». Le nove descrizioni prendono «collana».

⚠️ **L'eccezione e' `:76250`**, dove la descrizione **nomina l'oggetto che
l'artefatto diventa**, e quell'oggetto ha un nome suo: «Collare della
Tempesta». Li' si scrive «collare», se no la riga contraddice il nome che sta
una riga sopra nella stessa scheda.

### ⭐⭐ TRE RITROVAMENTI, E DUE SONO RIGHE INTERE GIA' SCRITTE

- `:99451`, l'amuleto nuziale: 「人に渡すと友好度が上がるアイテムだ」 e' gia'
  in questo file, reso **«Dato a qualcuno, alza la simpatia.»**. La riga
  dell'amuleto e' la stessa cosa piu' 返ってくることはない, e diventa **«Data a
  qualcuno, alza la simpatia. Non torna indietro.»** — non una resa nuova: la
  stessa, con la coda.
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

### ⚠️ 〜のついた, TERZA VOLTA IN TRE LOTTI

宝石のついた首輪 (:99810) e 羽のついた帽子 (:100135, lotto 017) hanno la stessa
costruzione e prendono lo stesso «con»: «con una gemma», «con una piuma». Come
沢山のベルトがついた服 del lotto 015, «pieno di cinghie».

ⓘ Il dono divino `:76250` e' il **quarto** della famiglia 身に着けると変形して:
l'elenco completo sta nella testa del lotto 017.
"""
