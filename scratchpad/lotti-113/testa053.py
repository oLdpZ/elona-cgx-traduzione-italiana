# -*- coding: utf-8 -*-
"""120a - Lotto 053 di `db_item.hsp`: LE ARMI A DISTANZA, prima meta'.

`FILTER_RANGE`, righe da `:43631` a `:88670`: **50 righe** — 46 dell'indice 0,
1 dell'indice 1, 3 dell'indice 2 — su 46 oggetti. La categoria e' la piu'
grossa che restasse (**60 su 60 da fare**) e con questo lotto scende a **10**:
la chiude il 054.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 053`: **+50** per 50 rese,
**nessuna gemella**: le 50 firme coprono 50 righe del sorgente e basta.
ⓘ `_gia-reso.py 053`: 0 su 50. `_code.py 053`: 0 righe senza resa in tabella.

⚠️ La zona non e' l'intera categoria per scelta: `0 200000` dava **60** righe,
sopra il tetto di 55 che la 115a dichiara sano. `0 90000` ne da' 50, e le 10
che restano stanno fra `:90000` e `:127280`.

### ⭐⭐⭐ LA SERIE DELLE TRE ARMI CHE NESSUN UOMO SOLLEVA

E' la cosa che vale oltre questo lotto, ed e' la lezione della 119a — cercare
per **struttura**, sull'originale — applicata **in avanti** invece che a
posteriori.

Tre righe chiudono con la stessa formula, parola per parola:

    人では扱えない程の重さだが、使いこなす者が現れた時
    この武器は使用者に ◯◯ を授けるだろう。それと少しばかりの気まぐれを。

    :75515  la moneta di pietra     魅力          -> carisma
    :77075  la balestra gigantesca  飛びぬけた器用さ -> destrezza fuori dal comune
    :77145  il cannone a gravita'   超感覚         -> percezione fuori dall'umano

⚠️⚠️ **Le tre parole sono TRE ATTRIBUTI DEL GIOCO**, non tre aggettivi: sono
CHR, DEX e PER, e il giocatore le legge nella propria scheda. Le rese vengono
dal dizionario e non dall'inglese — `_cerca.py` da' 「魅力の成長」 -> «Cresce
carisma» e 「器用の成長」 -> «Cresce destrezza». L'inglese scrive «a tremendous
charm»: chi rendesse da li' scriverebbe «fascino» su una statistica che a
schermo si chiama **carisma**, e il legame fra la descrizione e cio' che l'arma
fa davvero si spezzerebbe.

⭐ E la formula si ripete **identica** nelle tre rese, di proposito. La
tentazione di variare («dona», «concede», «regala») cancellerebbe la serie:
qui la ripetizione e' il testo, ed e' come il giocatore riconosce che la terza
arma e' parente delle prime due. Stessa forma della scala delle navi della
119a, al rovescio: la' l'inglese aveva appiattito quattro gradini in uno, qui
ci sono tre righe che devono restare **uguali** tranne una parola.

⚠️ Nessuna rete poteva vederle: firme diverse, tre oggetti di tre tipi
(moneta, balestra, cannone), e ognuna presa da sola e' a posto. Il dossier le
mostra a distanza di dodici voci l'una dall'altra.

### ⭐⭐ IL DOPPIO SENSO DELLA FOGLIA, CHE L'ITALIANO TIENE PER INTERO

`:43632`, le parole della volpe a nove code:「おぬしにハッパをかけてやろうぞ…
ドカーン！」. ハッパ e' insieme:

  - 葉っぱ, **la foglia** — che e' l'oggetto;
  - 発破, **la carica esplosiva** — che e' il nome dell'oggetto, 金毛発破;
  - e ハッパをかける, la locuzione, vuol dire **«dare la carica, incitare»**.

Tre sensi in una parola sola, e l'italiano ne ha una che ne tiene due: «ti do
io **la carica**» e' insieme l'incitamento e l'esplosivo, e il «BUM!» che segue
fa scattare il secondo. L'inglese («Lemme give you a little nudge...boom!»)
tiene solo l'incitamento.

### ⚠️⚠️ DUE RIGHE DOVE L'INGLESE HA RISCRITTO, E LA CODA LO DENUNCIA

  - `:52650`, il gambero fritto esplosivo. Il giapponese e' un **commesso
    confuso** che minaccia 「エビフライ５本くらいぶつけんぞ」, *guarda che te ne
    tiro addosso cinque*. L'inglese ci mette un **bandito eccentrico** con un
    gioco di parole tutto suo su shrimp/shrimping. ⭐ A dire quale delle due e'
    la fonte non e' stato il giudizio: e' `_code.py`, che assegna la coda
    passando dal **giapponese** e scrive «Parole di un Commesso Confuso».
    Rendere dall'inglese avrebbe messo la battuta del bandito sotto il titolo
    del commesso, **nello stesso pannello**;
  - `:52648`, la voce sopra, stesso oggetto. Il giapponese chiude con
    「悪魔の兵器」の別称でも知られている — *lo chiamano anche l'arma del
    diavolo*, che e' un fatto sull'oggetto. L'inglese lo butta e ci mette
    «shrimply devilish», un bisticcio. La resa tiene il fatto.

ⓘ Le due righe stanno **a due voci di distanza** nel dossier, ed e' lo stesso
oggetto: il pannello le disegna una sotto l'altra.

### ⓘ Tre termini presi dal dizionario e non dall'inglese

  - 光子銃 (`:65063`) e' **«pistola laser»**, non «cannone a fotoni»:
    `_cerca.py` da' 光子銃 | laser gun | pistola laser, ed e' il nome che il
    giocatore vede sull'oggetto. ⚠️ Il dizionario porta anche «cannone a
    fotoni» su un **altro** oggetto (la bazooka), e quella e' la resa di
    大口径化された光子銃: le due non si confondono;
  - 詠唱 (`:85997`) e' **«incantesimi»**, la voce della scheda
    (詠唱スキル上昇 -> «bonus in Incantesimi»), non «canto» ne' «recitazione»;
  - 冥界 (`:53561`) e' **«Oltretomba»** con la maiuscola, come nelle sei rese
    di `text.hsp` che il giocatore legge in combattimento.

### ⓘ 妖気 non e' nel dizionario, e non lo diventa qui

`:43631` dice 特殊な妖気が込められており — l'aura sinistra che emana uno
spirito. `_cerca.py` non la trova da nessuna parte, e l'inglese la lascia in
giapponese («special Yokai energy»). La resa la **descrive** («un'aura sinistra
fuori dal comune») invece di coniare un termine: coniarlo qui vorrebbe dire
decidere per tutte le volte che tornera', e questa riga non e' il posto.
"""
