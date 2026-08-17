# -*- coding: utf-8 -*-
"""Lotto fase4-main-006: gli altri due finali e la morte del giocatore
(main.hsp, righe 4128-4409).

Ventun rese: la vittoria su Tyris del Sud (le Rovine di Remido) e quella sul
Sigillo Eterno, poi tutto il rito della morte — le ultime parole, la lapide, il
menu che decide se si ricomincia.

⚠️⚠️⚠️ **Questo lotto ha corretto la RETE 4, ed e' la QUINTA rete che si
corregge** dopo la 8, la 4 (una prima volta), la 9 e la 6. `:4151` e `:4232`
hanno **lo stesso giapponese** — 「あなたは「」とコメントした。」, «hai commentato
"X"» — e lo stesso `cnvtalk`, ma l'inglese di monte ci mette il nome del boss:
«Upon killing Meshera Alpha» e «Upon killing Enthumesis». Sono i due finali, e
le rese devono differire. La rete raggruppava per `(giapponese, funzioni)` e
bocciava il lotto.

La chiave le mancava per una ragione storica: la 37ª le aveva insegnato che la
**rete 11** pretende le funzioni dell'inglese, quindi due giapponesi uguali con
un numero diverso di `name()` non possono coincidere. Ma upstream distingue
anche con le **parole**, e quelle non erano nella chiave.
✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`, in
`scratchpad/modello-rete4.py`.

⭐⭐ **E la correzione e' stata misurata prima di usarla**, con
`scratchpad/misura-rete4.py`, che passa la rete 4 all'indietro su tutto il
dizionario — come `rete8_dizionario.py` fa con la rete 8. Su **11.982 gruppi**,
467 sono resi in piu' di un modo:

    con inglese diverso   458   <- la rete vecchia li bocciava a torto
    con lo stesso inglese   9   <- la famiglia per cui la rete e' nata

La rete nuova prende ancora tutti e nove, e i due Yerleswood del lotto 039 —
stesso giapponese **e** stesso inglese — restano bocciati. Non perde niente.
⚠️ E i nove sono un referto da leggere: uno e' un difetto vero, «Tiro oltre il
limite» (`buff.hsp:263`) contro «Lancio oltre il limite» (`skill.hsp:1240`), che
sono la **stessa mossa** vista dal potenziamento e dall'elenco.

⚠️ **`:4282` e' la prima chiave lunga di `main.hsp`.** Le due `lang()` sulla riga
sono `lang("「", "\\"")` e `lang("」", "\\"")` — le virgolette che aprono e chiudono
le ultime parole — e hanno **lo stesso inglese**, quindi la chiave corta
`(riga, en)` ne identifica due. Si danno con `(riga, en, jp)`, come la 41ª ha
insegnato su `init.hsp:2225`. Tutt'e due restano `\\"`: e' punteggiatura, ed e'
gia' dichiarata in `invariati.md` per `proc.hsp:3376`.

⭐ **`:4296` non usa nessuna preposizione, e non e' pignoleria.** L'inglese e'
`cnven(ndeathcause) + " in " + mdatan(MDATAN_NAME) + "."`, ma i nomi di mappa
italiani non stanno tutti dietro la stessa preposizione: «a Vernis» ma «nelle
Rovine di Remido», «al Sigillo Eterno» ma «in Prigione». La riga e' la **seconda
del referto della lapide** (`noteadd s, 2`), cioe' una voce di registro, e si
scrive come tale: «Prigione - Morì di fame.» ⚠️ `ndeathcause` arriva gia' reso da
`chara_func.hsp:6850`-`:7039` come un verbo alla **terza persona del passato
remoto senza soggetto** («morì di fame», «si impiccò», «perse la vita contro il
putit»), e `cnven` gli alza la prima lettera: la resa deve incastrarcisi, non
riscriverlo.

⚠️ **Le quattro voci del menu della morte sono `promptAdd` con
`val = promptx, 100, 400, 1`**, cioe' **400 px = (400 − 46) / 7,7 = 45
caratteri**. La piu' lunga, «Ricarica l'ultimo salvataggio», ne fa 28.
⚠️⚠️ **Ma nessuna rete lo misura**: `larghezze.py` guarda i menu di `*prompt_key`
**solo in `text.hsp`** (`FILE = "text.hsp"` a `larghezze.py`). I `promptAdd` di
`main.hsp`, `command.hsp` e degli altri file sono fuori da ogni referto — e' un
punto cieco di geometria, misurato qui a mano.
💡 Le quattro rese sono tutte all'imperativo — «Rialzati», «Lasciati
seppellire» — anche perche' e' l'unica forma che non porta genere: «Resta
disteso» sarebbe stato un aggettivo riferito al giocatore.

⭐ **I nomi propri erano gia' decisi:** 「災厄」 e' **«la calamità»**
(`text.hsp:9692` «Parte seconda - L'ombra della calamità», `db_card.hsp:9227`
«il semenzaio della calamità»), 「混沌の神」 e' **«il dio del caos»**
(`text.hsp:9852`), il Sigillo Eterno e le Rovine di Remido vengono dal lotto 005.

💡 **`:4293` tiene l'ordine anno/mese/giorno dell'inglese**, che non e' quello
italiano, perche' e' l'ordine con cui `init.hsp:2225` compone **tutte** le date
del gioco — e li' il dizionario non puo' cambiarlo, perche' l'ordine sta nel
codice e non nelle `lang()`. Due formati di data nello stesso gioco sarebbero
peggio di uno straniero. La voce va quindi in `invariati.md` con l'espressione
intera, come la 56ª ha imparato su `Karma()`.
"""
