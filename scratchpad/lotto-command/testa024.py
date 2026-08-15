# -*- coding: utf-8 -*-
"""Lotto `command-024`: **dare un oggetto a un alleato**, e il bestiame che mangia.
Apre la zona 15000-15999, la piu' densa rimasta di `command.hsp` (79 firme).

⭐⭐ **Qui parla sempre qualcun altro, e non si sa mai chi**: ventisei rese su
trentasei sono battute di `tc` — l'alleato, il bestiame, il figlio — passate da
`cnvtalk`. Il genere del parlante non e' noto a chi scrive, quindi **nessuna
resa puo' contenere un participio o un aggettivo riferito a chi parla**. Le
manovre sono quelle di sempre: il nome al posto dell'aggettivo («Ho la pancia
piena!» e non «Sono pieno»), l'accordo spostato sulla cosa («Ma quanto e'
secco!», che concorda col mangime), il verbo al posto dello stato («Non ho piu'
fame!»).

⭐⭐ **E un errore di monte con la forma piu' pulita che si sia vista finora:
l'inglese di `:15188` e' l'array di `:15196` copiato addosso, senza guardare il
giapponese.** I quattro slot di `:15188` sono i quattro esiti della **borraccia
filtrante** (`:15169`-`:15186`) e il giapponese li dice tutti: `f = 2` e' la
borraccia vuota (`PARAM2 == 0`) e dice 「からっぽ！」, `f = 4` e' l'alleato che
**beve davvero** (`PARAM2 > 0`, `SOUNDLIST_DRINK1`, `THIRST += 2000`) e dice
「ありがとう！」, cioe' «grazie». L'inglese ci mette «No way.» e **«Never!»**,
che sono lo slot 2 e lo slot 4 dell'array del **rifiuto** otto righe piu' sotto.
In inglese, l'alleato beve e ti risponde «mai».
✅ La resa non deve scegliere: **la rete 3 decide da sola**, perche' 「ありがとう！」
e' gia' reso in `text.hsp:1994` come «Grazie!». Il giapponese e' l'identita'
della voce, e quando l'inglese sbaglia e' il giapponese a vincere.
💡 La lezione e' il gemello del punto 4 della 45a — «un referto puo' avere un
punto cieco suo» — dall'altro lato: qui a sbagliare non e' uno strumento, e'
**l'inglese di monte**, e a prenderlo e' stata una rete che guarda il
giapponese. Nessun conteggio di «non tradotte» lo avrebbe mai segnalato.

⚠️ **La rete 4 lega due righe che l'inglese distingue**: 「いらん」 sta in
`:15188` come «I don't want it.» e in `:15196` come «I don't need it.», stesso
giapponese e nessuna funzione di contenuto, quindi **una resa sola per tutt'e
due** — «Non mi serve!», che regge sia sull'alleato non assetato (`:15176`,
`THIRST > 10000`) sia sull'oggetto da buttare (`:15165`, `FILTER_JUNK`).
Stessa cosa per `:15101` e `:15115`, che hanno il **giapponese identico**
(name(tc) + 「に家畜の餌を食べさせた。」) e un inglese che a `:15101` dice «food for
livestock» e a `:15115` solo «food»: la resa e' una, e dice «mangime» — che vale
per tutt'e due, perche' **tutt'e due i rami pretendono `CHARA_BIT_LIVESTOCK`**.

⚠️ **Due dinamiche hanno dovuto girare la frase per la rete 8.** «You hand X to
Y» in italiano vuole «a » davanti a `name`, che si fonde con l'articolo: e'
diventata `name(tc) + " riceve " + itemname(ci, 1)`, cioe' il ricevente in testa.
Lo stesso per `:15101`, dove «dare da mangiare **a**» e' diventato «**nutrire**»,
che regge l'oggetto diretto. 💡 La rete 8 non chiede di accorciare: chiede di
scegliere un verbo che non abbia bisogno di quella preposizione.

⚠️ **`:15264` nomina un oggetto che l'inglese non nomina.** Il giapponese e'
`name(tc) + "は激怒して" + itemname(ci, 1) + "を叩き割った。"`, l'inglese
«throws it on the ground angrily» — un `itemname` in meno. La rete 11 pretende
l'insieme dell'**inglese**, quindi la resa non puo' nominare la pozione: dice
«il regalo», che e' un nome fisso e maschile e non ha bisogno di sapere che
oggetto sia.

⭐ Copiate senza decidere, tre su trentasei: «Non mi va.» (`action.hsp:9799`),
«Grazie!» (`text.hsp:1994`) e `name(tc) + " arrossisce."` (`action.hsp:10757`).
E due termini gia' fissati altrove: «pane soffice» (`db_item.hsp:141763`) e
«mangime per il bestiame» (`db_item.hsp:137486`).

💡 **Un invariato solo, ed e' un lamento**: «Nooooo!» per 「イヤぁぁあ！」. Le altre
tre del gruppo si scostano dall'inglese — «Nooo!», «No e no!», «Nooo!!!!!!» —
questa no, e in italiano si scrive identica. Va in `invariati.md`.
"""
