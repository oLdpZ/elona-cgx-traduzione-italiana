# -*- coding: utf-8 -*-
"""Lotto fase4-init-002: casa, negozio, comunita', gilda, e le cariche
cittadine (init.hsp, righe 359-390).

54 rese, ed e' il **secondo lotto piu' grosso del progetto** dopo le 68 del
`chara_func-003`. Chiude le quattro scale di rango che restavano e i due
elenchi piccoli che le seguono: i tre nomi di gilda che `guildname()` sceglie
(`:370`-`:381`) e le sei cariche di `popostname` (`:384`-`:390`).

⚠️⚠️ **L'inglese di monte ha sbagliato CONTINENTE, due volte.** `:359` gradino 0
e' 「イルヴァの楽園」 e `:360` gradino 0 e' 「イルヴァ最大の店」 — **Irva**, che e'
il mondo — e l'inglese scrive tutt'e due «Tyris», che e' **il continente** dove
sta il gioco. Non e' una semplificazione: e' un posto diverso, e il progetto ha
gia' i due nomi separati (`text.hsp:2917` «Irva Perduta», `proc.hsp:9996` «Tyris
del Nord»). ✅ Resi su Irva. Con questi la serie degli errori di monte passa da
quarantatre' a **quarantasei**: il terzo e' `:362` gradino 10, qui sotto.

⚠️⚠️ **E il terzo e' lo stesso errore del museo, ma peggio: l'inglese ha messo un
GRADINO dove andava il nome della categoria.** L'undicesima voce di ogni riga di
`rankn` non e' un rango, e' l'etichetta che `module.hsp:264` stampa in «Cambio di
rango (**Gilda** 5° → 4°)». Per le altre sette categorie l'inglese ci mette
l'etichetta giusta — `Arena`, `Pet Arena`, `Museum`, `Home`, `Shop`,
`Community` — e per la gilda ci mette **«Novice»**, che e' un grado. Il
giapponese dice 「ギルド」. ✅ «Gilda».

⚠️ **La scala della gilda e' l'unica dove l'inglese ha rifatto la classifica da
capo.** Il giapponese sale 見習い → メンバー候補 → 正式メンバー → ジャーニーマン →
エキスパート → アダプト → 重役候補 → 重役 → 右腕 → 次代マスター, cioe' una
carriera di bottega; l'inglese ci ha messo sopra `Master` e `Champion` sui due
gradini dei **重役**, che sono i dirigenti. ✅ Reso sul giapponese, con i termini
della bottega italiana: **apprendista → lavorante → maestro**, che e' la scala
vera dei mestieri. ⚠️ E `ranktitle(8)` finisce dentro una frase — `chat.hsp:5396`
fa 「ようこそ魔術士ギルドへ、」+ ranktitle(8) + 「の」+ nome — quindi ogni gradino
dev'essere un titolo che si puo' appiccicare a un nome: «Apprendista Tizio»
regge, «Della gilda» no.

💡 **I termini erano quasi tutti gia' fissati, e nessuno in una frase intera.**
ギルドマスター e' il «maestro della Gilda» (`db_creature.hsp:123766`), 見習い
l'«apprendista» (`db_creature.hsp:99431`), 乞食 l'«accattone»
(`db_creature.hsp:102544`), 徴税官 l'«esattore» (`db_item.hsp:144349`), マダム la
«dama» (`db_item.hsp:145456`), e i tre nomi di gilda stanno gia' per intero in
`db_creature.hsp:79873`-`:80071`. E' la sesta volta in due sessioni che il
lavoro sta nei **termini** e `dossier.py` non li vede.

⚠️ **Le sei cariche restano minuscole**, perche' minuscole sono in inglese
(`mayor`, `chief`, `priest`…) e perche' `podata` le stampa dentro una frase. Non
sono titoli come i ranghi.

💡 **Le quattro grida della rete 3 non sono divergenze.** Tre sono i nomi di
gilda, che in `db_creature.hsp:103737`-`:103915` compaiono dentro il nome di una
creatura — «il **membro della** Gilda dei Maghi» — mentre qui il nome della gilda
sta da solo: e' lo stesso termine in due cornici, non due decisioni. La quarta e'
「なし」, che a `text.hsp:49` e' il valore `none` di `CDATAN_NEWSEX` e **resta
inglese apposta** (vedi `invariati.md`, «Valori di dato»), mentre qui e' la
risposta di `guildname()` a chi non sta in nessuna gilda: due cose diverse con lo
stesso giapponese, e infatti hanno due inglesi diversi — `none` contro `None`.

💡 **Nessuna chiave ambigua in questa zona**: le quattro righe hanno undici
inglesi distinti ciascuna. La chiave lunga serviva solo al museo del lotto 001.
"""
