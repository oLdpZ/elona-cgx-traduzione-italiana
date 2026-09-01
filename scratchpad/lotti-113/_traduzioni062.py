# -*- coding: utf-8 -*-
"""Le rese del lotto 062 — GLI ALBERI: `FILTER_ENVIRONMENT` si apre e si chiude.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 062 scratchpad/lotti-113

Il ragionamento sta per esteso in `testa062.py`. Vale tutto quel che dice
`_traduzioni026.py`: la coda `\\n#<titolo>` la assegna `lotti-113/_code.py`
passando dal giapponese, lo spazio dopo il `#` si conserva com'e' nella tabella,
e gli **accenti si scrivono veri**.

⚠️ Forma, da `_forma.py 062`: **13 righe su 13** con lo spazio prima del `\\n`,
13 su 13 con lo spazio dopo il `#`.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 062`: **+13** per 13 rese,
nessuna gemella. ⓘ `_gia-reso.py 062`: 0 su 13.

⚠️⚠️⚠️ **`:95858` — L'INGLESE E' QUELLO DELL'ABETE, E LO DICE UNO STRUMENTO
NUOVO.** Il cedro (スギ) porta **parola per parola** l'inglese dell'abete
(`:91522`): «festivals are held in Noyel to celebrate the Saint by decorating
these trees». Il giapponese del cedro parla di tutt'altro — il **polline**, che
fa credere di avere qualcuno che intralcia gli incantesimi. Una resa presa
dall'inglese avrebbe messo la festa di Noyel sull'albero sbagliato, e nessun
cancello se ne sarebbe accorto.
⭐ L'ha trovato `scratchpad/_122-inglese-doppio-item.py`, scritto un'ora fa
dopo lo stesso difetto nel lotto 061 (`:56267`). **Queste due righe non erano
ancora tradotte**: e' la prima volta che la rete arriva prima del danno invece
che dopo.
"""

IT = {
    # =====================================================================
    # LA SERIE: 実を落とさない + 常緑樹 / 落葉樹, cinque alberi
    # =====================================================================
    # ⭐ 常緑樹 -> «sempreverde» e 落葉樹 -> «albero che perde le foglie»
    #   sono gia' in gioco sull'indice 3 di questi stessi oggetti. Le rese
    #   ripetono la formula del giapponese, che la ripete apposta.

    # ⚠️ L'abete: qui la festa di Noyel c'e' davvero, e' il suo giapponese.
    #   ノイエル -> «Noyel» (dizionario). さる聖人 e' «un certo santo»:
    #   il giapponese non lo nomina, e nemmeno noi.
    91522: "Un sempreverde che non lascia cadere frutti. Pare che nella stagione fredda, a Noyel, questi alberi li carichino di addobbi d'ogni sorta e si faccia una festa per un certo santo. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ⚠️⚠️ Il cedro: RESA DAL GIAPPONESE, perche' il suo inglese e' quello
    #   dell'abete qui sopra (vedi la testa). 詠唱を妨害する -> «intralciare
    #   gli incantesimi», che e' la forma gia' in gioco sulla veste dei
    #   monaci (`:130714`, lotto 060).
    95858: "Un sempreverde che non lascia cadere frutti. Succede spesso di credere che qualcuno stia intralciando i propri incantesimi e scoprire poi che era il polline di questo albero. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ⭐⭐ LA COPPIA CHE CAMBIA UNA PAROLA SOLA: il frassino e' 非常に硬く
    #   (durissimo), la zelkova 非常に良質で (di ottima qualita'). Tutto il
    #   resto della frase e' identico nel giapponese, e lo e' nelle rese.
    #   Appiattirle sarebbe la 119a: qui l'inglese le distingue e saremmo
    #   noi a perderle.
    95484: "Un albero che perde le foglie e non lascia cadere frutti. È durissimo, e si lavora soprattutto come legname per mobili d'ogni sorta. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    95608: "Un albero che perde le foglie e non lascia cadere frutti. È di ottima qualità, e si lavora soprattutto come legname per mobili d'ogni sorta. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # 水薬 -> «pozione» (dizionario), 魔術士ギルド -> «Gilda dei Maghi».
    95920: "Un albero che perde le foglie e non lascia cadere frutti. Di recente si è scoperto che, crescendo, dalle radici emette tossine che fanno seccare gli alberi intorno, e la Gilda dei Maghi sta studiando se se ne possa ricavare una pozione. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # =====================================================================
    # GLI ALTRI ALBERI
    # =====================================================================
    # ⭐ 常世桜 e' il ciliegio del mondo dei morti. 狂い咲き e' il fiorire
    #   fuori stagione, e la riga ci gioca: 儚さを通り越して狂気 — oltre la
    #   caducita' c'e' la follia. Le due parole si tengono tutt'e due.
    68450: "Un ciliegio misterioso che nel mondo dei morti fiorisce e sfiorisce, fiorisce e sfiorisce, per sempre. I petali che toccano terra svaniscono piano, come un'illusione. In quel fiorire fuori stagione si va oltre la caducità: quello che si sente è follia. \\n# ~Speciale: sulle Tracce delle Piante Leggendarie~",

    # モミの木 -> «abete» e 飾り -> «addobbi», come nel lotto 061 (:91026,
    # l'albero di Natale da commercio: «un abete abbattuto e carico di
    # addobbi»). Sono lo stesso oggetto visto da due parti.
    90894: "Un abete a cui hanno attaccato addobbi a non finire. Gli ornamenti sgargianti illuminano tutt'intorno, come se l'albero splendesse di luce propria. \\n# ~Viaggio in Tyris del Nord: Inverno~",

    91584: "Un albero a cui sono cadute tutte le foglie. Sembra infreddolito, ma è il suo modo di passare l'inverno. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # ノースティリス -> «Tyris del Nord» (dizionario). 砲丸 e' la palla di
    # cannone, come dice anche l'inglese.
    95546: "Un albero che viene dai paesi caldi. Dicono che il suo frutto sia duro e grosso come una palla di cannone, ma a Tyris del Nord questi alberi pare non ne portino. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    95670: "Un albero vecchio, seccato del tutto. Prende fuoco con niente: meglio non giocare con le fiamme lì vicino. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    95734: "Un albero che, a dargli una spallata, lascia cadere i frutti. Ma se ci si prende gusto e si insiste, per un po' di frutti non se ne avranno più: occhio. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    95796: "Un albero che, per quanto lo si aspetti, non ha nessuna intenzione di dare frutti. Meglio rassegnarsi e cercarne uno che i frutti li abbia. \\n# ~Atlante Illustrato del Giardinaggio di Tyris~",

    # =====================================================================
    # LA BATTUTA DI <BARIUS>, che e' un indice 2 e non un indice 0
    # =====================================================================
    # ⓘ 映写機 non e' nel dizionario da nessuna parte: e' il proiettore, e
    #   l'inglese dice «projector». La battuta gioca su due sguardi sulla
    #   stessa cosa — un legno marcito, oppure noi, oppure un bosco — e la
    #   domanda finale resta aperta come nel giapponese.

    95672: "\\\"Fa pensare a molte cose. Questo di sicuro è solo un legno marcito, ma basta cambiare sguardo e diventa noi, o quel bosco. Col tempo che passa, chissà quale delle due cose finirà per riprendere, questo proiettore.\\\" \\n# ~Parole di <Barius> dai capelli blu~",
}
