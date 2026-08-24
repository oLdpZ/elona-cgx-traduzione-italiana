# -*- coding: utf-8 -*-
"""92a - MIKRAANESIS (`chat.hsp:9367`-`:9430`, 18 firme).

ミクラアネーシス = **Mikraanesis** (`chat.hsp:268`), il dio nato dalla fusione
di ventotto divinita' (`:9460`: «ventotto fra i fratelli e le sorelle di
Sophia, fusi in uno solo»). Parla al **plurale** — 私達, «noi» — e da' del tu
al giocatore: l'asimmetria e' voluta e sta gia' nelle righe rese
(`:268`, `:269`, `:9423`).

LESSICO EREDITATO (non deciso qui):
  - ミクラアネーシス  «Mikraanesis»                 chat.hsp:268
  - ソピアー          «Sophia», 《叡智のソピアー》 «<Sophia> la Saggia»
                                                    db_creature.hsp:76380
  - エンテュメイシス  «Enthumesis»                  chat.hsp:10210
  - 《深淵のプロパトル》 «<Propator dell'Abisso>»    chat.hsp:9423
  - 混沌の巨城        «la Culla del Caos»           chat.hsp:7913, :7917
  - ラスキリスの谷間  «Valle di Raskilis»           text.hsp:2908, :2911
  - 常闇の杖          «il bastone delle tenebre eterne»  chat.hsp:10242
  - 分身体            «questo corpo staccato da noi»     chat.hsp:269
  - 手合わせ          «misurarsi»                   db_creature.hsp:96788
  - 叡智              «sapienza»                    chat.hsp:9460, :10328

⭐⭐⭐ DEROGA 1 — I VENTOTTO NOMI SONO GLI EONI GNOSTICI, E L'INGLESE LI
STORPIA. `:9409`-`:9412` sono un elenco di ventotto katakana. Non sono inventati:
sono i nomi greci degli **eoni valentiniani**, e il gioco ne usa gia' quattro
nella trama principale — **Sophia**, il padre inconoscibile **Propator/Bythos**
(`:9423`), e **Enthumesis**, che nel mito e' proprio la passione di Sophia
staccata da lei (`:10213`: «quel desiderio impazzito genero' Enthumesis dentro
di me»). Cioe' la storia di Sophia in Elona+ **e' il mito valentiniano**, e
questo elenco e' il suo pleroma.

L'inglese traslittera a orecchio dal giapponese e sbaglia quasi tutto:

    アウトピュエース  Outpuece   -> Autophyes    アキネートス  Aquinatos -> Akinetos
    ヘードネー        Hedonay    -> Hedone       メートリコス  Maitrikos -> Metrikos
    ビュテイオス      Buteios    -> Bythios      アエイヌース  Aeneus    -> Aeinous
    アレーテイア      Areteia    -> Aletheia     マカリア      Macalia   -> Macaria
    ヌース            Nuus       -> Nous         ゾーエー      Zoea      -> Zoe

⚠️ E su uno **cambia il significato**: 独り子のモノゲーネス e' *l'Unigenito*
(独り子 = figlio unico), l'inglese scrive «Monogenes of **Solitude**». Se si
traduce l'inglese, il nome che nel mito indica il Figlio unigenito diventa il
dio della solitudine.
💡 Si scrivono i nomi nella forma **greca**, che in italiano e' anche quella
degli studi gnostici, e i domini si traducono: «Ennoia del Pensiero», «Logos
della Parola». Sono 3 + 7 + 8 + 10 = **28**, e il conto torna.

⚠️ DEROGA 2 — `:9405`, NIENTE AGGETTIVO SUL GIOCATORE.
黙っておけば e' «se stai zitto», che darebbe un genere. Si gira in **«se non
fiati»**, che non lo da' a nessuno.

⭐ DUE RIPARAZIONI SU RIGHE GIA' RESE, trovate leggendo questo blocco (e sono
il caso d'uso della «rete che manca» n. 4 della ripresa):

1. **`chat.hsp:269`** diceva «Norne, hai fatto bene a guidare **la tua amica**
   fin qui»: il giapponese non ha oggetto (「よくここまでガイドしてくれたね」)
   e l'italiano ce ne aveva messo uno **femminile**, che a schermo da' un genere
   al giocatore in una delle prime battute della storia. Rifatta: «Norne, hai
   fatto bene a farle da guida fin qui» -> no, anche quello lo da': si scrive
   **«a fare da guida fin qui»**.
2. **`chat.hsp:10211`** chiamava lo stesso 《深淵のプロパトル》
   **«<Prophatorl dell'abisso>»**, ricopiando il refuso inglese, mentre
   `:9423` — resa dopo — dice **«<Propator dell'Abisso>»**. Una sola entita',
   due nomi diversi a schermo, e nessuna rete lo vede: le due firme sono frasi
   diverse, quindi `battute --divergenti` non le confronta. Allineata su
   `:9423`.

PERIMETRO: 18 firme su 20 dentro il blocco, zero occorrenze fuori
(`python scratchpad/_85-blocco.py 9367`). Le altre due erano gia' rese.

⚠️ `:9399`-`:9403` NON sono nel lotto e non sono `lang()`: sono il ramo
`if ( jp )` con i letterali nudi, e l'inglese li' e' **due** `chatMore` dove il
giapponese ne ha uno. Restano da toppare, non da tradurre qui.

MENU: uno, 6 voci — una colonna sola, tetto 58.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    9370: "Questo corpo staccato ha finito il suo compito. Se ti va, puoi anche misurarti con lui.",
    9371: "Per provare le tue forze è quel che ci vuole, non credi? Del resto noi, così come ci vedi adesso, siamo appena un po' più forti di Sophia.",
    9381: "Se vuoi uscire dalla Valle di Raskilis possiamo farti volare noi oltre i suoi bordi. Oppure puoi andartene guardandoti il paesaggio, lungo la strada dei viandanti di un tempo.",
    9375: "C'è ancora qualcosa che non ho visto",
    9376: "Fammi uscire",
    9377: "Che ne pensi di Sophia?",
    9378: "Del padre di Sophia",
    9379: "Voglio sapere di te",
    9380: "Non ho ascoltato e non so che devo fare",
    9389: "Addio. Noi non ti dimenticheremo.",
    9405: "Be', che la sorellina sciocca sia adorabile è l'opinione di tutti noi. Ah, e quello che ti abbiamo raccontato non dirlo a Sophia, che si mette di malumore. Tanto siamo in un altro mondo: se non fiati, non lo scopre nemmeno il bastone delle tenebre eterne.",
    9409: "Noi siamo un dio solo, nato dalla fusione di ventotto divinità. Al centro ne stanno tre: Mixis dell'Unione, Syncrasis della Mescolanza e Synesis dell'Integrazione.",
    9410: "Le altre sono Ennoia del Pensiero, Nous della Ragione, Aletheia della Verità, Logos della Parola, Zoe della Vita, Anthropos dell'Uomo, Ecclesia della Chiesa.",
    9411: "Bythios della Profondità, Ageratos dell'Indistruttibile, Henosis della Premura, Autophyes della Crescita, Hedone del Piacere, Akinetos dell'Immobilità, Monogenes dell'Unigenito, Macaria della Beatitudine.",
    9412: "Parakletos della Mediazione, Pistis della Fede, Patrikos della Paternità, Elpis della Speranza, Metrikos della Maternità, Agape dell'Amore, Aeinous dell'Eternità, Ecclesiasticus della Predicazione, Makariotes della Felicità, Theletos della Volontà.",
    9413: "Non serve che li impari a memoria. Sono lunghi, sono tanti e si somigliano tutti: una faticaccia.",
    9418: "Perché questo mondo non venga dimenticato, abbiamo fatto in modo di condividere i ricordi.",
    9419: "Nel punto più profondo della Culla del Caos c'è qualcuno che devi affrontare. Intesi?",
}
