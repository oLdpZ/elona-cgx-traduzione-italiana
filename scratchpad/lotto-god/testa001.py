# -*- coding: utf-8 -*-
"""`god.hsp` si apre e si chiude: le 95 firme del sistema divino.

I nove nomi degli dei, le nove schede del pannello di scelta, le preghiere, le
conversioni, i doni e la disputa dei mattoni. `god.hsp` non aveva dizionario:
114 `lang()` che nessun conteggio guardava, ed e' la regola della 54a.

## ⚠️ Tradurre `godname()` ripara TRENTATRE' siti, non nove

`god.hsp:81`-`:89` riempie l'array `godname`, e trentatre' righe in nove file lo
interpolano. Finche' non era tradotto, `proc.hsp:11749` diceva a schermo «Senti
su di te lo sguardo benevolo di **Lulwy of Wind**»: italiano intorno a un nome
inglese. La 37a lo aveva gia' scritto («`his2` della 36a ha un fratello»), e
questa e' la riparazione.

## Il tetto dei nomi e' 20 caratteri, e lo detta la scheda del personaggio

`command.hsp:17662` scrive `fixtxt("Fede      : " + godname(...), 32)`, e
`fixtxt` (`module.hsp:5041`-`:5054`) **taglia**: `strmid(m, 0, 32)`. L'etichetta
italiana e' lunga 12 — non si accorcia, perche' «Uccisioni : » nella stessa
colonna ne vuole 12 — quindi al nome ne restano **20**.

    Kumiromi della Messe    20   il piu' lungo, ed e' esatto
    Yacatect del Tesoro     19
    Mani della Macchina     19
    Ehekatl della Sorte     19

⚠️ La 37a diceva «`sdim godname, 20, 9` da' 20 byte»: e' una coincidenza, non la
causa. `sdim` non e' un tetto in scrittura — lo dice la 28a e lo riconferma la
33a. Il tetto vero e' `fixtxt`, ed e' un taglio vero.

⚠️ **«Itzpalt Elementale» e' l'unico nome senza genitivo**, e non e' un
capriccio: «Itzpalt degli Elementi» ne ha 22 e verrebbe tagliato a «Itzpalt
degli Element». L'epiteto aggettivale e' una forma italiana buona quanto il
genitivo — «Giove Tonante», «Apollo Delfico» — e qui e' l'unica che ci sta.

## Le schede: `gmes` va a capo da solo, e il pannello e' pieno

`god.hsp:448`-`:454` disegna la scheda con `gmes`, non con `mes`. Il compositore
sta in `module.hsp:4918`-`:5018` e detta tutto:

    7 px per lettera        `gmesx += size / 2`, con size = 14 (:5014)
    va a capo a 84 caratteri  `if gmesx >= gmesx + gmesw`, gmesw = 590 (:5001)
    <br> = 16 px, <p> = 24 px                            (:4979, :4975)

⚠️ **`gmes` ignora il `font` del chiamante**: `god.hsp:419` chiede corpo 13, e
`gmes` lo riscrive a 14. Il passo e' 7, non 6.
⚠️ **Va a capo a meta' parola**: il controllo e' su un carattere, non su una
parola. I `<br>` di upstream stanno li' apposta.

Il corpo comincia a `wy + 70` e il menu a `wy + 212` (`:462`, con `dy = 270` e
`listmax = 2`): **142 px**, cioe' otto righe scarse. `scratchpad/misura-god.py`
le conta, e sull'inglese di monte dice che **due schede su nove finiscono sotto
il menu** — Ehekatl e Opatos, che hanno un `<p>` in piu' e un potere su due
righe. Le rese italiane stanno tutte a `wy+174` o meno: nessuna sfora, e quelle
due sono riparate.

## ⚠️ Sei volte l'inglese di monte perde qualcosa che il giapponese dice

1. `:35` **dice tutt'altro.** La condizione e' `faith * 100 < piety`, cioe' la
   pieta' ha superato quel che l'abilita' Fede regge. Il giapponese lo dice
   («la tua fede e' gia' salita al limite»); l'inglese scrive «Your god becomes
   indifferent to your gift», che parla del dono e non della fede.
2. `:270` e `:300` **perdono il numero.** 無畏無頼 dice `+40%`, オパートスの甲殻
   dice `-10%`; l'inglese scrive «Increase all damage» e «Reduce any damage».
   Un giocatore che sceglie un dio sta confrontando numeri.
3. `:315` **e' un mozzicone.** Il giapponese descrive Yacatect in una frase
   intera — chi la venera impara a trattare e accumula ricchezze enormi —
   e l'inglese scrive «Yacatect is a god of wealth.» e basta. Ed e' l'unica
   scheda in cui l'inglese lascia mezzo pannello vuoto.
4. `:309` e `:285` **accorciano.** Kumiromi «insegna anche a lavorare» quel che
   raccoglie, Itzpalt protegge **e** insegna ad assorbire: l'inglese tiene una
   meta' per ciascuno.
5. `:316` **generalizza**: 首飾り / 指輪 sono collane e anelli, «Accessories» e'
   la categoria.
6. `:616` e `:903` **perdono la battuta.** Il giapponese dice che il senza-dio
   «ci prova lo stesso» a pregare e a offrire; l'inglese scrive due volte «You
   don't believe in the gods.» ⚠️ La resa non puo' portare `name()`, che il
   giapponese ha e l'inglese no: la rete 11 pretende le funzioni dell'inglese.

## ⚠️⚠️ E tre abilita' sono nominate con un nome che il gioco non usa piu'

`:317` scrive 自然鑑定 / «Sense Quality», ma quell'abilita' nel gioco si chiama
分析 / «Analysis» (`skill.hsp:252`). Stessa cosa a `:275`: 銃 e 大工, mentre
`skill.hsp:181` e `:322` dicono 銃器 e 工作. **Sbagliano tutt'e due le lingue di
monte**, ed e' un nome vecchio rimasto in un file che nessuno rilegge. Le rese
usano i nomi che il giocatore trova nell'elenco delle abilita' — «Analisi»,
«Arma da fuoco», «Falegnameria» — perche' una lista di bonus serve a **cercare**
quelle voci, e un nome che li' non esiste non serve a niente.

## Il vocabolario, e da dove viene

    Possessione di Lulwy    ルルウィの憑依, da buff.hsp:63
    Assorbi magia           魔力の吸収, da skill.hsp:952
    Preghiera di Jure       ジュアの祈り, da skill.hsp:948
    Imposizione delle mani  レイハンド, da chara_func.hsp:6258
    Analisi                 分析, da skill.hsp:252 — vedi sopra
    dio / dea / divinita'   神, gia' 37 volte nel dizionario
    Fede                    信仰, l'abilita' di skill.hsp:347
    i ventisei nomi di abilita' dei «Bonus» vengono tutti da skill.hsp
"""
