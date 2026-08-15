# -*- coding: utf-8 -*-
"""Lotto fase4-command-003: la scheda del personaggio
(command.hsp, righe 10495-10948).

⭐⭐ **È la schermata che si guarda più di ogni altra dopo il log**, e i valori
dentro sono **già italiani** da tre sessioni — «Maschio», «Nessuna», «FOR COS DES
PER APP VOL MAG CAR», i nomi di razza e di classe. Mancava solo la cornice: 41
rese e 1 rinviata.

⚠️⚠️ **Nessuna guardia misura questa schermata, e i budget sono di trentotto
pixel.** `larghezze.py` conosce solo i menu che passano da `*prompt_key`
(il suo docstring lo dice: «solo le assegnazioni a `s(cnt)`» dentro quei
`#deffunc`); qui le etichette si disegnano con `mes` a `pos` fisse, e il metro
è la **distanza fra la posizione dell'etichetta e quella del valore**, che il
sorgente scrive due volte a poche righe di distanza:

| gruppo | etichetta | valore | budget | inglese più lungo |
|---|---|---|---|---|
| `:10495` | `wx+355` | `wx+410+5` | **60 px** | `Next Lv` (7) |
| `:10504` col. 1 | `wx+30` | `wx+68` | **38 px** | `Class` (5) |
| `:10504` col. 2 | `wx+220` | `wx+270` | **50 px** | `Height` (6) |
| `:10517` | `wx+255` | `wx+310` | **55 px** | `Rating` (6) |
| `:10526` | `wx+29` | `wx+86` | **57 px** | `Cargo Lmt` (9) |
| `:10730` | `wx+422` | `wx+468` | **46 px** | `Prot` (4) |
| `:10732` | `wx+574` | `wx+617` | **43 px** | `Evade` (5) |
| `:10734` | `wx+554` | `wx+617` | **63 px** | `SpellPow` (8) |
| `:10837` | `wx+30` | `wx+63` | **33 px** | `Desc:` (5) |

💡 Il carattere è `12 + sizefix - en * 2`, cioè **10 px in grassetto** nella
build inglese (9 px per `:10837`). Da `Cargo Lmt` — nove caratteri dentro 57
pixel — viene il metro usato qui: **~6,3 px per carattere**, e la regola pratica
è che l'italiano non superi l'inglese di più di un paio di caratteri.
⚠️ **Perciò upstream abbrevia, e l'italiano deve abbreviare uguale**: `Prot`,
`Evade`, `SpellPow`, `InSAN`, `Cargo Wt` sono già tutte sigle. Dove il progetto
ha una resa distesa e non ci sta, si abbrevia **quella**, non si allarga il
riquadro.

⚠️⚠️ **La scheda NON si chiude con questo lotto, e non è una dimenticanza.**
`Level` e `Name` non compaiono in questa zona perché `estrai --da-tradurre` dà
**una voce per firma**, e le loro prime occorrenze stanno a `:3556` e `:7623`.
Finché non si traducono quelle due righe, la scheda avrà due etichette inglesi
in cima. ⚠️ E i loro budget sono questi — 60 px per `Level`, 38 per `Name` —
non quelli dei siti dove le firme sono estratte: chi scriverà quel lotto guardi
qui prima di scegliere.

⚠️ **`Schiv.` contro la rete 3, ed è la larghezza a decidere.** `skill.hsp:307`
rende 「回避」 «Schivata», ed è la resa giusta per il **nome dell'abilità**; qui
l'etichetta ha **43 pixel** e «Schivata» ne vuole ~46. ✅ Abbreviata: non è una
resa nuova, è la stessa parola tagliata dove il riquadro taglia. Stesso motivo
per «Prot.» e «Pot. magia».
💡 Idem per `Sesso` contro `text.hsp:191`, che scrive «sesso» minuscolo: lì la
parola sta **dentro una frase**, qui è l'intestazione di una colonna. La
maiuscola la mette il sito, non una scelta diversa.

⚠️⚠️ **Un giapponese solo per due siti, e la rete 4 impone lo spazio.**
「ターン」 sta a `:10526` come **etichetta** di colonna (`Turns`) e a `:10754`
come **suffisso di un numero** (` Turns`, con lo spazio davanti): l'inglese
mette lo spazio dove serve e la rete 4 pretende una resa sola. ✅ « Turni» con
lo spazio in tutt'e due: il valore ne ha bisogno («12345 Turni») e l'etichetta
se lo assorbe come un rientro di tre pixel. È la lezione del brusio del
`map-005` — lo stesso giapponese, una resa sola, spazi compresi.

⭐ **Sei etichette non le ho decise io.** 「信仰」 è «Fede» (`skill.hsp:347`),
「生命力」 «Vita» (`:9`), 「マナ」 «Mana» (`:14`), 「速度」 «Velocità» (`:59`),
`Shoot` «Tiro» (`text.hsp:136`), e le tre gilde sono parola per parola quelle di
`init.hsp:373`-`:379`. ⚠️ Le gilde sono lunghe — «Gilda dei Guerrieri» sono
diciannove caratteri — ma quella è la **colonna dei valori**, che ha 186 pixel
fino al ritratto: il tetto stretto è delle etichette, non dei valori.

💡 **`INI` è `INIT`, e vuol dire i tiri iniziali**: `:10657` compone
`inipower = CDATA_INIT_LIFEMANA + CDATA_INIT_ATTR` e il valore accanto è
`inipower + "/" + CDATA_INIT_SPEED`. «Iniz.» in cinque caratteri.
💡 **`AP` e `HP/MP` sono due invariati nuovi**, dichiarati in `invariati.md`:
il giapponese scrive `HP/MP` identico e 「ＡＰ」 a larghezza intera, che CP932
vieta comunque. `Karma` e `Mana` erano **già** dichiarati dalle sessioni
passate — si guarda prima di aggiungere.

⚠️ **`:10825` è rinviata: sta dentro l'`ORIGINAL` che il mod ha spento**
(`:10817`-`:10827`). È la gemella di `:10837`, che è viva e resa: stesso
giapponese 「説明:」, due inglesi diversi (`Hint:` e `Desc:`). Senza il rinvio la
rete 4 avrebbe preteso una resa sola per tutt'e due, e sarebbe stato un vincolo
imposto da **testo morto**.

💡 **`:10948` è un prefisso che il giapponese mette in coda.**
`s = lang("", "Resist ") + cnven(s) + lang("耐性", "")`: l'inglese antepone
«Resist », il giapponese posticipa 「耐性」, e il ramo inglese della seconda
`lang()` è **vuoto**, quindi non c'è nessuna firma da tradurre lì. L'italiano
può solo anteporre: «Res. fuoco», nella colonna della lista abilità.
"""
