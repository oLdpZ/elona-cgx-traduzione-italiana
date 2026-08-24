# -*- coding: utf-8 -*-
"""92a - SHURAIDA (`chat.hsp:13537`-`:13633`, 17 firme).

歴戦の傭兵『シュライダ』 = **«<Shuraida> il mercenario veterano»**
(`db_creature.hsp:65831`, `db_card.hsp:5054`). E' il capo della compagnia di
mercenari con cui il giocatore va ad abbattere il **demone della pestilenza**
a **Kikkasu**: l'incarico e' quello di `chat.hsp:2111` e la presentazione sta
in `:2141`, gia' resa, che fissa mezza scenografia di questo blocco.

⭐ IL BLOCCO E' UNA MISSIONE INTERA, letta dalla bandiera
`GDATA_FLAG_SUB_REGULUS_KIKKASU`: il briefing (`:13585`-`:13588`), la partenza
(`:13599`-`:13603`), l'arrivo in citta' (`:13573`-`:13576`), la vittoria
(`:13559`-`:13560`) e due battute fuori missione (`:13541`, `:13545`, nella
Culla del Caos; `:13553` a guerra finita).

LESSICO EREDITATO (non deciso qui):
  - キッカス          «Kikkasu»                    chat.hsp:2111, :2140
  - 疫病の悪魔        «il demone della pestilenza» chat.hsp:2111, :2140
  - ザナン            «Zanan»                      chat.hsp:1403, :2102
  - パルミア          «Palmia»
  - 傭兵部隊/傭兵団   «compagnia di mercenari»     chat.hsp:2141
  - 小型艇            «battello»                   chat.hsp:2141
  - アンデッド        «non morti»                  chat.hsp:2140, :14014
  - 消毒薬            «disinfettante»              blend.hsp:614

REGISTRO: e' un capitano di mercenari — 俺, 「お前」, frasi corte, tono da
rapporto. Italiano asciutto e militare, mai aulico.

⚠️⚠️ DEROGA 1 — 冒険者 NON E' «AVVENTURIERO», E QUI RICORRE TRE VOLTE.
`decisioni.md` (e `chat.hsp:1469`, `:1595`) fissa la forma senza genere, «tu
che vai all'avventura». Vale in `:13585` («Sei tu che vai all'avventura»),
`:13559` («qualcuno che va all'avventura») e `:13545`, dove 「よくここまで
来れたな」 diventa **«ce l'hai fatta ad arrivare fin qui»**: «sei arrivato»
darebbe un genere al giocatore.

⭐⭐ DEROGA 2 — `:13575`, L'INGLESE BUTTA VIA META' DELLA FRASE.
Il giapponese e' 「地の利だけじゃない。敵の物量・耐久性からも考えて持久戦は
不利だ。お前の制圧能力にもよるが、ある程度片づけたら切り込んだほうが得策
だろう。」: **il terreno**, il **numero e la resistenza** del nemico, e la
**capacita' di tenere il campo** del giocatore. L'inglese riassume in «Given
our enemy, a prolonged fight is not to our advantage. It all depends on you,
but putting the demon down quickly would be best in my opinion.», cioe' toglie
il terreno, i due parametri del nemico e la ragione per cui la scelta dipende
dal giocatore. E' un **consiglio tattico** in una missione dove il giocatore
decide davvero come muoversi: si rende il giapponese per intero.

⚠️ DEROGA 3 — `:13588`, LA ツアーコンダクター.
La parola compare **una volta sola in tutto il sorgente** (cercata in tutti i
file) e non e' il titolo di nessuno dei due personaggi del turismo, che sono
ガイドの『アルマ』 = «<Arma> la guida turistica» (`db_creature.hsp:90210`) e
プランナーの『フロン』 = «<Fron> l'organizzatrice di viaggi» (`:71217`).
Siccome il giapponese non dice **chi**, non lo dice neanche l'italiano: si
scrive **«la guida turistica»**, che e' il mestiere e non il nome, e che in
italiano e' un sostantivo femminile buono per chiunque lo faccia — quindi non
attribuisce la battuta ad Arma ne' le da' un genere.

⚠️ `:13590`-`:13592` (il menu «Aspetta» / «Andiamo») erano gia' resi: sono tre
delle venti firme del blocco.

PERIMETRO: 17 firme su 20 dentro il blocco, zero occorrenze fuori
(`python scratchpad/_85-blocco.py 13537`).

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    13541: "Scendere altri piani, francamente, è troppo. Esploriamo ancora un po' e poi ci ritiriamo.",
    13545: "Tu... ce l'hai fatta ad arrivare fin qui, eh. Noi abbiamo messo insieme gente in gamba, ma di potenza di fuoco non ne abbiamo abbastanza. E siamo volontari, senza compenso, quindi non abbiamo neanche i soldi.",
    13553: "I miei mercenari hanno deciso di non entrare in guerra. Ma tenere in piedi una compagnia costa il suo... ecco perché gli incarichi di caccia ai mostri sono il nostro guadagno.",
    13585: "Sei tu che vai all'avventura, ti manda Palmia. Giusto?",
    13586: "Il bersaglio è un demone che governa i batteri con la forza magica. Fuori dal suo raggio di controllo la tossicità cala parecchio, pare. Ma il contagio non è roba da sottovalutare.",
    13587: "Sul battello che useremo ci hanno montato un impianto di disinfezione: non è solo un mezzo per spostarsi, serve anche a impedire che il contagio si allarghi. Non possiamo accostare dritti al campo nemico e fare la fine dei topi.",
    13588: "Stando alle informazioni della guida turistica, qui vicino c'è una grotta calcarea che arriva al pozzo della città. Entriamo da lì e ci prendiamo il bersaglio: il piano è questo. I miei sono già tutti a bordo del battello ad aspettare. Si parte quando vuoi.",
    13599: "Dai rapporti c'è da aspettarsi veleno ed emorragie. Bevi questa: è la medicina che ci ha passato Zanan. Serve solo ad attenuare i sintomi, intendiamoci.",
    13603: "...Bene! Seguimi.",
    13625: "Sbrigati. Se il bersaglio si sposta, siamo in ritardo.",
    13573: "...Che disastro. Mi dicono che fosse una cittadina piccola ma viva, vicina alla capitale.",
    13574: "Dai rumori direi che in giro ci sono parecchi non morti. Occhio agli angoli bui. Quanto ai batteri... la medicina sembra funzionare. Per ora il sangue dalle mucose è ridotto al minimo, ma se i danni si accumulano non so dire che succede.",
    13575: "E non è solo il terreno. Anche per numero e resistenza del nemico, tirarla per le lunghe ci penalizza. Dipende da quanto sai tenere il campo, ma la mossa giusta è ripulire un po' e poi affondare il colpo.",
    13576: "Si va. Operazione avviata.",
    13566: "Se ogni singolo demone ha una forza del genere... mi preoccupa l'altra squadra. Speriamo che se la stiano cavando.",
    13559: "Ottimo lavoro, va detto. Aver chiesto qualcuno che va all'avventura è stata la scelta giusta: da soli non ci saremmo bastati.",
    13560: "Noi mercenari abbiamo il compito di finire i superstiti e disinfettare tutta la zona. Tu torna pure indietro a riscuotere il compenso.",
}
