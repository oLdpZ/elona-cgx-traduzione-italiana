# -*- coding: utf-8 -*-
"""Lotto fase4-ai-002: chi tira i sassi, il gioielliere che contratta, la
tag-team a tavola, i figli che crescono (ai.hsp, righe 1525-4525).

42 rese, e la **percentuale di copie piu' alta mai vista in un lotto di questo
progetto: dodici su quarantadue**, tutte pescate da `dossier.py` per **giapponese
intero**. Batte le dodici su trentaquattro del `proc-026` e le nove su
quarantadue del `proc-018`, e stavolta non e' un menu ristampato da due punti: e'
il **blocco della tag-team a tavola** (`:2087`-`:2132`), che `action.hsp`
(`:1860`-`:2023`) ha gia' parola per parola in tre varianti — chi ti cavalca, il
bersaglio, il compagno — e che `ai.hsp` ripete in due.

⭐ **Le quattro grida della trasformazione erano gia' tutte e quattro decise.**
`action.hsp:11442` ha lo stesso `txt` con gli stessi quattro giapponesi:
「変身！」 «Trasformazione!», 「フォームアップ！」 «Cambio forma!»,
「ドレスアップ！」 «Cambio d'abito!», 「トランスフォーム！」 «Metamorfosi!». ⚠️ **Non
stanno in questo lotto**: vedi la nota sulla rete 0 qui sotto.

⚠️⚠️ **La rete 0 ha fermato una zona, ed e' la prima volta.** A `:4576` due
`lang()` diverse hanno lo **stesso inglese** — 「変身！」 e 「トランスフォーム！」
sono tutt'e due `cnvtalk("Transform!")` — quindi la chiave `(riga, en)` su cui e'
costruito ogni lotto **identifica due voci, non una**, e il modello si ferma
prima di scrivere. Non e' un difetto della rete: e' il limite della chiave.
✅ La zona di questo lotto arriva a `4560`, e le quattro grida vanno in un lotto
`003` scritto a mano e indicizzato per **`firma`**, che e' l'unica chiave davvero
univoca. 💡 Il dizionario la collisione la regge gia' — `action.hsp:11442` porta
«Trasformazione!» e «Metamorfosi!» sulla stessa riga con lo stesso inglese — ed
e' solo lo **script di lotto** a non poterla esprimere.

⭐ **Le preposizioni che non si fondono hanno salvato la resa gia' decisa, e
stavolta e' «verso».** 「睨み付けた」 e' «lanciare un'occhiataccia» da
`action.hsp:1854`-`:2011`, ma li' il bersaglio e' sempre **«ti»**, un clitico; qui
sono due nomi, e «un'occhiataccia **a** name(cc)» e' chiusa in partenza dalla
rete 8. ✅ «lancia un'occhiataccia **verso** X»: «verso» non si fonde con
l'articolo, quindi la frase gia' decisa si tiene tale e quale invece di essere
girata. E' la scorciatoia della 40a — «con», «contro», «per», «sotto», «sopra» —
con una preposizione in piu' all'elenco.

⚠️ **Un genitivo di monte girato col verbo.** `:1755` dice «X seems to be aiming
at Y», e «mira **a** Y» ricadrebbe nella rete 8 come sopra. ✅ «X **punta** Y»,
che in italiano regge il complemento oggetto diretto e non vuole nessuna
preposizione.

⚠️ **Tre aggettivi appesi a un nome di genere fisso.** I cinque versi dei figli
che crescono (`:2317`-`:2341`) sono tutti participi o aggettivi in inglese —
«`is looking away with interest`», «`is thinking with a serious face`» — e in
italiano concorderebbero col figlio, che puo' essere maschio o femmina. ✅ «con
**aria** curiosa», «con **aria** seria»: l'accordo cade su «aria», che e'
femminile per sempre. E' la strada dei ventidue di resistenza della 40a («si
sente la **pelle**…») applicata a un complemento di modo.

⚠️ **` *BAN* ` resta invariato**, e va dichiarato in `invariati.md`: `:2308` e'
`lang(" *BAN* ", " *BAN* ")` — **il giapponese e' inglese anche lui**, come
`HAPPY END!!` e `Destroy! Dynamite!`. E' il ghepardo che bara (`WALL_HACK_CHEATAH`
… `SPEED_HACK_CHEATAH`) che si prende il ban e muore sul colpo: la parola e'
gergo di rete, identica nelle tre lingue.

💡 **Un giapponese solo per TRE inglesi, e la resa e' una sola: cambia solo lo
spazio.**  *クスクス*  e' `*chuckle*` ad `action.hsp:250`, ` *Snicker* ` a
`db_creature.hsp:95622` e ` *grin* ` qui: l'italiano dice «*risatina*» in tutt'e
tre, e gli spazi attorno li mette **il sito**, copiando il suo inglese. La rete 3
grida perche' confronta i letterali e lo spazio conta, ma non e' una divergenza —
e' la stessa resa in tre vestiti. E' il rovescio della rete 13: li' un inglese
per due giapponesi, qui tre inglesi per un giapponese.

💡 **I termini gia' decisi che il dossier non vede, perche' sono termini e non
frasi:** 店主 e' «il negoziante» (`db_creature.hsp:74301`), 訓練券 e' il
«biglietto d'addestramento» (`db_item.hsp:134224`), e `gold pieces` sono le
«monete d'oro» di `proc.hsp:7056` e `:9488`. ⚠️ `:1939` scrive `hiyou + "gp"`
attaccato: la resa scioglie l'abbreviazione, come ha gia' fatto
`text.hsp:10817` con «2,000,000gp».
"""
