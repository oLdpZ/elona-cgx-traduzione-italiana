# -*- coding: utf-8 -*-
"""Lotto fase4-chara_func-003: il danno, le urla e le ventitre' morti
(chara_func.hsp 6000-6999).

68 rese, ed e' **il lotto piu' grosso mai fatto** — batte le 59 del `proc-021`.
Chiude la zona piu' densa di `chara_func.hsp`. La regge un blocco solo: dal
`:6850` in giu' ci sono **tutte le cause di morte del gioco**, e vengono a
coppie.

⭐⭐ **La scoperta del lotto e' che ogni morte si scrive DUE VOLTE, e le due
meta' hanno vincoli opposti.** Per ogni causa il sorgente scrive:

  - una **riga di log**, dinamica, che nomina chi muore — «`name + は餓死した。`»;
  - un **frammento di epigrafe**, statico, assegnato a `ndeathcause` — 「飢え死
    にした。」 — che **non nomina nessuno**.

Il frammento non e' una frase: e' un pezzo che `main.hsp:4409` incolla dentro
«`cdatan(AKA) + cdatan(NAME) + <frammento> + " in " + mdatan(NAME)`», cioe' la
riga che il gioco manda in rete e scrive sulla lapide.
⚠️⚠️ **E questo decide la lingua del frammento.** Il pezzo segue il nome del
morto e ne e' il predicato: in italiano «e' morto di fame» **concorderebbe col
personaggio**, e meta' dei personaggi di Elona sono femmine. L'inglese non ha il
problema (`was starved to death`), il giapponese nemmeno (「飢え死にした」).
✅ La strada e' il **passato remoto**, che in italiano non ha genere: «mori' di
fame», «cadde dalle scale e mori'», «si tolse la vita», «si prosciugo' nel
deserto». Ventitre' frammenti, ventitre' verbi senza participio. E' la strada
del participio della 37ª applicata a un tempo verbale invece che a una
struttura, ed e' l'unica volta che il progetto ha potuto usarla: **serve una
frase intera**, e i frammenti lo sono.
💡 **Le righe di log invece non hanno il vincolo** — nominano chi muore, quindi
la sostanza puo' fare da soggetto: «Il veleno consuma X fino alla morte», «La
ghigliottina decapita X», «I residui degli elementi inghiottono X».

⚠️⚠️ **E c'e' una dipendenza da dichiarare: la cornice e' in `main.hsp`, che non
ha dizionario.** Finche' `main.hsp:4409` resta inglese, l'epigrafe si leggera'
«`<Il viandante> Sinaha mori' di fame in Vernis`» — meta' italiano e meta'
inglese, con la preposizione sbagliata. Non e' un difetto delle rese, e' la
dipendenza nota di `godname()` della 37ª in forma nuova. ⚠️ E quando si
tradurra' la cornice va ricordato che **il giapponese mette il luogo PRIMA del
frammento** e l'inglese dopo: l'italiano vuole «… mori' di fame **a** Vernis».

⚠️⚠️ **Il QUARTO punto cieco, e la battuta che era gia' morta.** `:6852` e
`:6853` fanno `cnv_str ndeathcause, "was killed by motuhegui", "was mauled to
death by a bear"`: il mod riscrive la stringa **gia' composta**, e la chiave e'
l'**inglese di monte**. Nessuno dei tre referti la vede — `blocchi_en.py` guarda
dentro `if ( en )`, `else_jp.py` dentro `if ( jp ) ... else`, `variabili_en.py`
gli assegnamenti — perche' qui non c'e' nessun letterale inglese da tradurre:
c'e' una **chiave** che deve continuare a combaciare.
✅ Misurato con **`scratchpad/cnv_str_en.py`**: 41 chiamate, **17 con la chiave
in inglese**. ⚠️⚠️ **E questa era gia' rotta**: `db_creature.hsp:37656` rende
モツヘグイ «lo sbudellatore», quindi `cdatan(CDATAN_NAME, cc)` restituisce «lo
sbudellatore» e la chiave `"was killed by motuhegui"` **non aggancia da mesi**.
La battuta dell'orso e' morta quando si e' tradotto il bestiario, e nessuna
verifica l'ha detto. 💡 Le altre 15 stanno in `module.hsp` (il parser dei
desideri, che smonta «card of …» da quel che il giocatore scrive) e in
`help.hsp`: sono **input**, non uscita, e vanno guardate quando si aprira'
`module.hsp`.

⚠️ **`:6196` e `:6200` sono lo stesso inglese per due giapponesi, ed e' un
errore di monte scoperto dalla rete 13**: 「＜中破＞」 e 「＜大破＞」 sono il
danno **medio** e il danno **grave** dello scafo, e l'inglese scrive
«`<Medium damaged>`» tutt'e due le volte. Il ramo lo conferma: `:6194` guarda
`HP > MAX/4`, `:6198` guarda `HP <= MAX/4`. ✅ «Danno medio» e «Danno grave».

⚠️ **E la rete 13 in questo lotto grida QUATTRO volte, che e' il record.**
Oltre a `<Medium damaged>`: «`melt down`» sta per il cioccolato bollente
(`:6917`) **e** per l'acido (`:6959`), «`melted down`» per gli stessi due nei
frammenti (`:6919`/`:6961`), e «`is healed`» per 「再生した」 (`:6212`, il Figlio
del Caos che si rimette in piedi da solo) **e** per 「回復した」 (`:6260`, la cura
di Imposizione delle mani). Tutt'e quattro le distinzioni le fa il giapponese e
le conferma il ramo del codice; l'inglese le ha appiattite.

💡 **Cinque rese su 68 sono copie**, e le ha pescate tutte `dossier.py`: «ha
ripreso l'aspetto di prima» (`action.hsp:9265`), «si riprende»
(`proc.hsp:8199`), «freme di rabbia!» (`action.hsp:263`, `proc.hsp:20851`), «va
in pezzi» (`action.hsp:3102`) e «si contorce dal dolore» (`action.hsp:8778`).

💡 **E i tre gradini del dolore vanno rimessi in ordine sul giapponese.** `:6351`,
`:6358` e `:6365` sono i tre livelli di danno crescente, e il giapponese sale —
痛手を負った, 苦痛にもだえた, 悲痛な叫び声をあげた — mentre l'inglese mette
«`scream`» al **primo** gradino e «`is severely hurt`» al terzo. Reso sul
giapponese: «incassa un colpo doloroso», «si contorce dal dolore», «lancia un
urlo straziante».
"""
