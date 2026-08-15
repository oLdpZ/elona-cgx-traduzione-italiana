# -*- coding: utf-8 -*-
"""Lotto `command-032`: **la scheda dell'equipaggiamento** — le righe d'attacco
di `*show_weaponStat`, i cinque avvisi sul peso dell'arma e l'intestazione della
finestra `*com_wear`. Sedici rese e **una rinviata**.

⭐⭐⭐ **La resa di quattro etichette non l'ho scelta io: l'aveva già scelta
`buff.hsp:679`, e in questa stessa opposizione.** Le righe d'attacco sono una
colonna di quattro voci — 「武器」, 「格闘」, 「射撃」, 「命中」 — e le prime tre la rete 3
le dava già rese altrove, ma **in un altro mestiere**: `text.hsp:59` ha 武器 come
**categoria d'inventario** al plurale («armi»), `skill.hsp:161` ha 格闘 come **nome
di abilità** («Arti marziali»), `skill.hsp:387` ha 射撃 come nome dell'abilità di
tiro («Mira»).
✅ **A sciogliere il nodo è stato `buff.hsp:679`**, dove 「射撃力上昇/命中率上昇」 è già
reso «Tiro e **mira**»: lì i due termini compaiono **affiancati**, ed è la stessa
opposizione di questa colonna. Quindi 射撃 è «Tiro» e 命中 è «Mira», e la «Mira» di
`skill.hsp:387` è il nome dell'**abilità** Mira, non di questa colonna.
`skill.hsp:1277` conferma dall'altro lato: 命中率上昇 è «+mira».
💡 **La lezione**: quando la rete 3 accusa, la domanda non è «chi ha ragione fra
me e lei» ma «in che mestiere stava la resa che cita». Tre delle quattro rese di
questa colonna divergono da lei, e tutt'e tre perché il sito citato è un nome di
abilità o una categoria, non un'etichetta di riga.

⚠️⚠️ **E la colonna è larga sei caratteri, il che è la ragione per cui le rese
lunghe non erano scrivibili comunque.** `*com_skill_calcAttack` stampa `s(1)` a
`wx + 422` (`:12429`) e i dadi del danno a `wx + 460 + en * 8`, cioè `wx + 468`
nel ramo italiano (`:12452`): sono **46 px**, cioè 6,4 caratteri in Courier a
corpo 12. «Arti marziali» ne avrebbe fatti tredici, novantaquattro pixel, sopra
la colonna dei dadi. ⚠️ E upstream ci sfora già: «Unarmed» è di sette.
⚠️ Più stretta ancora l'etichetta di 「命中」: sta a `wx + 590` e la percentuale a
`wx + 625 - en * 8` = `wx + 617` (`:12444`), cioè **27 px**. «Mira» ne occupa 29:
due pixel di sconfinamento, un quarto di carattere, meno di quello che upstream
si permette con «Unarmed».

⭐⭐ **L'inglese appiattisce due scene in una, e stavolta la rete 11 non c'entra:
sono dinamiche, ma le funzioni coincidono.** `:12488` e `:12495` hanno lo
**stesso** inglese — «is too heavy for two-wield fighting style.» — e due
giapponesi diversi, perché il sorgente li raggiunge da due rami opposti:
`:12485` è `if ( attacknum == 1 )`, cioè l'arma della **mano principale** che
pesa 4 kg o più (「利手で扱うにも重すぎる」, «troppo pesante perfino per la mano
dominante»); `:12492` è l'`else`, cioè l'arma **secondaria** sopra i 1500
(「片手で扱うには重すぎる」, «troppo pesante per una mano sola»). Tutt'e due portano
`itemname` e nient'altro in tutt'e due le lingue, quindi la rete 11 **autorizza**
e l'italiano può rimettere la distinzione che l'inglese aveva buttato. È la
famiglia di `:15636` della 46ª.

⚠️⚠️ **E i cinque avvisi sul peso hanno un nodo che l'inglese non ha: il
GENERE.** «is too light» non concorda con niente, «troppo leggera» concorda con
`itemname(cw)`, che può essere «la spada» o «il martello». Non si può sapere a
scrittura. ✅ La manovra è quella di sempre e qui rende tutte e cinque: si passa
al **verbo**, che al presente non ha genere — «pesa troppo», «pesa troppo poco»,
«si impugna bene» — e l'accordo sparisce dal problema. ⚠️ Anche «per usarla a
cavallo» sarebbe stato un accordo nascosto dentro un pronome: la resa è «per
l'uso a cavallo».

⚠️⚠️ **`:12636` è rinviata, ed è la prima volta che una riga risulta morta in
TUTTI E QUATTRO i siti in cui è scritta.** È l'intestazione delle resistenze,
「火 冷 雷 闇 幻 毒 獄 音 神 沌 魔」 / «Fi Co Li Da Mi Po Nt So Nr Ch Ma», e compare a
`:12636`, `:12645`, `:14127` e `:14136`. Le prime e le terze stanno nel blocco
`ORIGINAL` spento; **le seconde e le quarte stanno nel blocco `ANNA CUSTOM`, che
è spento anche lui.**
💡 **E questo si vede solo leggendo il delimitatore**: `:12639` è
`/********** ANNA CUSTOM - BEGINNING ********** // Show skills on 'z' toggle`,
**senza la barra finale**, e a chiuderlo è `********** ANNA CUSTOM - ENDING
**********/` a `:12670`. Dove invece il blocco è vivo la riga si scrive
`/********** X - ENDING **********/` con la barra da tutt'e due i lati, come
`:12673` e `:14118`. La barra è l'unica differenza fra un blocco acceso e uno
spento, e non la guarda nessuno se non `commenti-blocco.py`.
✅ **A disegnare davvero le resistenze è MMAH**: `:12672` è
`display_show_resist showresist, ...`, una riga viva fra due marcatori
autochiusi. Le due versioni di monte sono state sostituite, non spente per
sbaglio. ⭐ **Quindi la rete 6 corretta nella 45ª ha fatto esattamente il lavoro
per cui era stata corretta**: boccia solo se sono spente tutte le occorrenze, e
qui lo sono.

⭐ Riscosso senza decidere: **«Mano\\*»** viene da `bodyn` (`text.hsp:136`, «Mano»),
che è la colonna in cui 「利手」 si sostituisce; e sta nei 42 px fra `wx + 46` e la
lettera di scelta a `wx + 88` (`:12698`, `:12709`).

💡 **Una misura che è avanzata**: la riga del peso di `:12674` è **destra**
(`display_note`, `module.hsp:4360`, `wx + ww - strlen * 7 - 140`), quindi su una
finestra da 690 il tetto è di **75 caratteri** — e l'inglese, con
«(Medium)» e un DV/PV a tre cifre, ci arriva. La resa italiana con « Mira:» e
« Danno:» ne fa 62, e il margine serve: 「(重いです)」 di `screen.hsp` non è ancora
tradotto e crescerà.
"""
