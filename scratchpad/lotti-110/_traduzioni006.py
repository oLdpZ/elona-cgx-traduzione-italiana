# -*- coding: utf-8 -*-
"""Le rese del lotto 006 (gli SCARTI, `FILTER_JUNK`), indicizzate per RIGA.

`lotti-109/_monta.py 006 scratchpad/lotti-110` prende questo file e
`chiavi006.txt` e ne fa `rese006.py`, copiando l'inglese verbatim dal template.

**97 righe del sorgente, 81 firme**: sedici righe portano una firma che un'altra
riga ha gia' — i tre materium doppi (superiore e normale hanno lo stesso
giapponese), i dodici materiali della sintesi, la spada del teschio e il cesto
vuoto. Una resa le copre tutte.

`FILTER_JUNK` non e' una categoria: e' il cassetto dove finisce quel che non sta
in nessun'altra. Dentro ci sono sei famiglie vere e una ventina di solitari.

Le formule ricorrenti, oltre alle code del lotto 004 e alla formula della 108a:

    〜の時に自動で使うアイテムだ。 -> Un oggetto che si usa da se' quando ...
                                     (nove strumenti degli dei, piu' due)
    投げてぶつけると〜を放つ〜だ。 -> Un ... che, lanciato, sprigiona ...
    投げてぶつけると〜爆発を起こす -> ... fa un'esplosione ...
    合成用のアイテムだ。           -> Un oggetto per la sintesi.  (12 firme)
    〜中間素材だ。                 -> Un materiale intermedio ...  (3 firme)
    所持していると〜勾玉だ。       -> Una perla ricurva: portandola, ...
    使用することはできない         -> Non si puo' usare.  (109a)

⚠️ Tre rese non seguono l'inglese, e la fonte che vince e' il giapponese:

  :48738  la cicala — il giapponese dice 「死にかけのセミだ。」, l'inglese
          racconta che spaventa chi colpisci. Il nome dell'oggetto e' gia'
          «cicala morente»;
  :116668 la ciotola — l'inglese cita Laozi («the empty space which makes the
          bowl useful»), il giapponese dice che dentro c'e' qualcosa;
  :46013  il fukagurumi — l'inglese aggiunge «Worth less than you think»,
          il giapponese ha solo la coda.

⚠️⚠️ Due rese sono state decise leggendo il CODICE, non il testo:

  :59793  l'ohuda cancella **un** potenziamento, non «i» potenziamenti: il
          giapponese non dice il numero e l'italiano lo deve dire.
          `action.hsp:752-766` fa `delbuff` e poi `break`;
  :63586  「態勢を崩す」 e' davvero la **rottura guardia** del gioco:
          `action.hsp:745` chiama `chara_guardbreak`. L'inglese dice
          «disorientates», che non e' un termine. La resa usa il termine, che
          il dizionario ha gia' («Rottura guardia», `command.hsp`).
"""

IT = {
    # --- i lanciabili: il giapponese dice sempre COSA succede all'urto
    42979: "Uno sterco che, lanciato, fa un'esplosione velenosa.",
    43177: "Una scatoletta immangiabile. Lanciata, fa un'esplosione neurale.",
    43305: "Un cristallo di neve che, lanciato, sprigiona gelo.",
    43367: "Un attrezzo che, lanciato, sprigiona oscurità.",
    43429: "Un lungo ago che, lanciato, sprigiona fulmini.",
    43491: "Una scatola piena di pestilenza. Meglio non aprirla.",
    55276: "Un barile che bruciando sputa fuoco. Lanciato, esplode in fiamme.",
    60128: "Una scatola che non si può aprire. Ma si può lanciare.",
    60851: "Un mozzicone di sigaretta. Lanciato, prende fuoco.",
    64872: "Un cristallo che, lanciato, esplode più volte.",
    64934: "Un cristallo che esplode all'urto.",
    63586: "Un oggetto che all'urto ferisce e rompe la guardia.",
    59793: "Un talismano che cancella un potenziamento. Si può lanciare.",

    # --- i nove strumenti degli dei, piu' i due che si usano da se'
    62868: "Un oggetto che si usa da sé quando ti alleni.",
    62932: "Un oggetto che scatta da sé quando ti ammali.",
    62996: "Un oggetto che si usa da sé quando addestri.",
    63060: "Un oggetto che si usa da sé quando dai ordini tattici.",
    63124: "Un oggetto che si usa da sé quando guardi una scheda.",
    63188: "Un oggetto che si usa da sé quando leggi un libro di studio.",
    63252: "Un oggetto che si usa da sé quando bevi una pozione.",
    63316: "Un oggetto che si usa da sé quando raccogli.",
    69391: "Si usa da sé, sempre, quando accarezzi il bestiame.",
    71646: "Un'esca automatica. Si usa da sé quando peschi.",
    86738: "Portato addosso, alza le probabilità di dominare i mostri.",

    # --- le tre perle ricurve
    52582: "Una perla ricurva: portandola, il gelo non spacca gli oggetti.",
    66012: "Una perla ricurva: portandola addosso, ci si bagna.",
    68048: "Una perla ricurva: portandola, il fuoco non provoca incendi.",

    # --- i materiali
    50881: "Un materiale per fare libri.",
    58027: "Un materiale intermedio affilato.",
    58151: "Un materiale intermedio duro.",
    58275: "Un materiale intermedio morbido.",
    66264: "Un oggetto per la sintesi.",
    66768: "Una grande pietra buona per scolpire.",
    68391: "Del legno lavorato per farne materiale.",
    112882: "Pezzi di legno tagliati per il focolare.",

    # --- le carte e i fogli
    42917: "Una carta che registra i dati di chi colpisci.",
    43770: "Paga l'addestramento di un compagno di LV non superiore al tuo.",
    57896: "Un foglio che sostituisce il platino quando impari un'abilità.",

    # --- i tappi, i cocci, gli avanzi
    43832: "Un tappo di pozione come tanti.",
    46278: "Il tappo di una bottiglia. Non serve ad altro.",
    46340: "Il tappo di una bottiglia di gazzosa. Non serve ad altro.",
    116543: "Un pesce secco. Non si può usare.",
    116854: "Bottiglie vuote e scheggiate, tutte insieme. Non si possono usare.",
    116916: "Un minerale fatto quasi tutto di roccia.",
    127796: "Una spada rotta che non serve a niente.",
    128044: "Un vaso rotto che non serve a niente.",
    128238: "Una scheggia di legno rotto.",
    127982: "Vestiti sporchi dentro un cesto.",
    92454: "Gli escrementi di un essere vivente.",
    48738: "Una cicala moribonda.",

    # --- le ossa
    116411: "Le ossa abbandonate di un animale.",
    127672: "Le ossa abbandonate di una persona.",
    127734: "Le ossa abbandonate di qualcosa.",

    # --- i cesti e i recipienti
    64618: "Un cesto di vimini senza niente dentro.",
    116792: "Un cesto di vimini.",
    116668: "Un recipiente con qualcosa dentro.",
    116730: "Un recipiente senza niente dentro.",

    # --- l'erba, i fiori, le piante
    46216: "Una pianta che, mangiata, cura un poco.",
    59731: "Un mazzo di fiori freschi. Si usa per dire quel che si prova.",
    111066: "Un mazzo di fiori freschi.",
    116473: "Erba secca legata in fascio.",
    128106: "Un fascio di erba secca.",
    61181: "Foglie di una pianta che dà dipendenza. Si usa (usa e getta).",

    # --- i minerali e i fossili
    55862: "La traccia di un essere vivente.",
    55924: "Della terra appiccicosa.",
    55986: "Un cristallo giallo.",

    # --- il resto, uno per uno
    43965: "Una catena gradita a chi ha un alto grado di sottomissione.",
    46013: "Si può usare sempre.",
    47152: "Un fischietto che abbassa la rottura guardia. Si usa sempre.",
    56536: "Un apparecchio che conserva la linea di chi lo porta.",
    61313: "Una moneta rossastra. Dà diritto a certi servizi.",
    62735: "Un bastone che alza il morale dei compagni e sceglie il bersaglio.",
    66326: "Il dono dei figli.",
    75378: "Un oggetto che si vende a un prezzo discreto.",
    89761: "Un'esca per la canna da pesca.",
    91463: "Uno spaventapasseri coperto di neve.",
    109211: "Quel che resta di un albero tagliato. Si può usare sempre.",
    112758: "Un attrezzo per pulire.",
    112820: "Uno scacciauccelli da mettere nel campo.",
    127858: "Un ornamento fatto di stoffa.",
    127920: "Una lampada semplice. Illumina sempre di luce viva.",
}
