# -*- coding: utf-8 -*-
"""95a - HALION, FRON e RENAI: tre voci sole in tre posti diversi (11 rese).

`HALION` (`:13517`-`:13536`, 5), `FRON` (`:12758`-`:12762`, 1) e `RENAI`
(`:12763`-`:12778`, 5).

⚠️ QUI IL RAGGRUPPAMENTO PER MAPPA FINISCE, E VA DETTO.
I due lotti prima li ha messi insieme `map.hsp`. Questi no: HALION sta in
`AREA_RUOZA` (`:7979`), RENAI in `AREA_NT_SOUTH_BORDER` (`:1803`) e FRON non ha
nemmeno un `characreate` — la si incontra dove capita, e `chat.hsp:13176` lo
dice per esteso: «Pare che stia sempre in movimento a preparare il viaggio
dopo, quindi con un po' di fortuna la incontri anche tu.» Quel che li tiene
insieme e' solo il file: FRON e RENAI sono blocchi **attaccati** (`:12758` e
`:12763`). Il criterio buono e' finito, e si dichiara invece di fingerlo.

⭐⭐⭐ MA IL LESSICO DI DUE DEI TRE ERA GIA' SCRITTO PER INTERO.
  - **RENAI** — `db_creature.hsp:62008`, gia' resa: «Mio fratello, sempre cosi'
    **apprensivo**.» (過保護), «Se abbasso la guardia mi spuntano i
    **tentacoli**, che orrore.» (触手), «**Fratello**... scusami...» (兄さん).
    Tutte e tre le parole difficili del suo blocco sono gia' decise, e la sua
    voce — わたし, timida, che si scusa — pure.
  - **FRON** — `:12760` e' la **gemella** di `chat.hsp:7774`, gia' resa: la
    stessa forma di discorso («per fare il mestiere X bisogna...») in bocca ad
    ARMA, che di FRON e' la cugina (`:7763`). E il mestiere ha gia' un nome
    italiano in `:13176`: **«organizzatrice di viaggi»**, tenuto distinto da
    **«guida turistica»** (ツアーガイド), che e' quello di Arma. Le due rese si
    accostano apposta.

LESSICO EREDITATO (non deciso qui):
  - 護衛        «scorta»              `chat.hsp:6735` e otto siti
  - ツアーガイド «guida turistica»      `chat.hsp:7774`, `db_card.hsp:9045`
  - ツアープランナー «organizzatrice di viaggi»  `chat.hsp:13176`
  - エレア      «gli Elea»            `db_race.hsp:1764` e cinquanta siti
  - エーテルの風 «il vento d'etere»     `text.hsp:46`
  - ルオザ      «Ruoza»               `text.hsp:2985`
  - メシェーラ  «il Meshera»          `chat.hsp:10237` e sessanta siti
  - ガード      «le guardie»          `chat.hsp:726`, `event.hsp:3127` e altri
  - 兄さん      «mio fratello»        `db_creature.hsp:62008`, di RENAI stessa

⚠️⚠️ DEROGA 1 — RENAI PRENDE IL **LEI**, ED E' LA TERZA VOLTA OGGI.
Renai non ha nessuna riga con una seconda persona gia' resa, quindi il registro
qui va **deciso**, non trovato. Prende il **lei** e non il voi dell'88a per due
ragioni che si sommano: il suo arco e' quello **moderno** di Zanan — istituti,
farmaci, armi biologiche — dove il voi di cortesia (che il progetto usa per
Maile, Manson e Bonyac, tutti di un mondo cortese e antico) suonerebbe di
un'altra epoca; e il fratello REGULUS, che il giocatore conosce gia', gli da'
del **tu** (`:12788`, `:12817`), quindi una seconda persona **piu' distante** di
quella del fratello e' esattamente il rapporto che c'e'.
💡 Con RYUTYE e ALFRED, oggi il lei viene fuori **tre volte**. Nei loro due casi
era scritto in `db_creature.hsp`; qui no, e la scelta va messa in
`decisioni.md` con il criterio: **voi** per il registro cortese e antico, **lei**
per quello deferente e moderno — e quando il personaggio ha gia' delle battute
rese, decidono quelle e basta.
⚠️ Il vincolo di genere regge lo stesso: nessuna resa mette un aggettivo o un
participio addosso al giocatore.

⚠️ DEROGA 2 — `:12770`, LA さん DOPO IL NOME DEL GIOCATORE SI BUTTA.
Come per RYUTYE (`:12898`): il progetto rende 〜さん con «il signor 〜», e un
titolo davanti al nome del giocatore chiederebbe un genere. La cortesia la
porta il lei. ⚠️ La voce e' `dinamica` da tutt'e due i lati.

⚠️ DEROGA 3 — `:13527`, L'INGLESE DICE IL CONTRARIO.
Il giapponese e' 「何も考えずに受け入れるというのも考え物だな」 — accogliere
senza pensarci **e' una cosa su cui riflettere**, cioe' un problema. L'inglese
scrive «it is also said that it's **important** to accept people without
thinking», che capovolge la frase e toglie il senso al resto della battuta, che
parla appunto di un'organizzazione cresciuta troppo. Si segue il giapponese
(57a).

⭐ DEROGA 4 — `:13521`, LA BATTUTA E' UNA BATTUTA E VA LASCIATA CADERE.
「全然許されなかったんだが。」 chiude l'aneddoto con l'ovvio detto piatto: il
predicatore del perdono non lo ha perdonato. L'inglese la gira in un sarcasmo
esplicito («Some forgiveness he had.»). In italiano il piatto funziona meglio
del sarcasmo, e Halion e' uno che racconta con rancore, non uno che fa lo
spiritoso: resta «Perdonato non mi ha perdonato per niente.»

PERIMETRO: 11 firme su 11 dentro i tre blocchi, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 13517 12758 12763`), zero gia' rese altrove.

MENU: nessuno. Tutte `chatMore`.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
⚠️ Le virgolette dentro `:13521` e `:13527` si scrivono protette (`\\"`).
"""

RESE = {
    # --- HALION: cinque battute a caso, una per volta
    13521: 'Durante il viaggio mi è capitato un brav\'uomo che non la finiva '
           'più di predicare: \\"per spezzare la catena dell\'odio, qualunque '
           'cosa ti facciano non rendere il colpo, perdona\\". Mi sono '
           'innervosito e gli ho tirato un sassolino: mi ha coperto di '
           'insulti per un pezzo e alla fine ha chiamato le guardie. Ma come '
           'funziona, di grazia? Perdonato non mi ha perdonato per niente.',
    13524: 'A dire la verità, all\'inizio ci credevo anch\'io alla storia che '
           'la foresta fosse la radice della sciagura. Che il vento d\'etere '
           'portasse malattia era vero, del resto. E allora ho pensato che '
           'fosse inevitabile che noi che vivevamo nella foresta venissimo '
           'perseguitati, e ho sopportato anche le angherie più insensate. A '
           'lungo, a lungo. Proprio per questo, quando ho saputo come '
           'stavano davvero le cose... quando ho saputo che era una diceria '
           'messa in giro per fare degli Elea i cattivi, mi sentivo bollire '
           'le viscere...!',
    13527: 'Si dice \\"chi viene non si respinge\\", ma accogliere senza '
           'starci a pensare è una cosa su cui ci sarebbe da riflettere... Il '
           'giro si è fatto troppo grande, e chi siano davvero i nostri, uno '
           'per uno, non c\'è più modo di saperlo.',
    13530: 'Quando abbiamo cominciato a muoverci ce n\'erano parecchi che si '
           'offrivano di darci una mano, per senso di colpa o per pietà. In '
           'giro erano in tanti a fare finta di niente, ma sapere che un '
           'certo numero di sostenitori c\'era mi aveva commosso! Be\'... poi '
           'è andato tutto a monte.',
    13533: 'Questa Ruoza pare sia una terra che una guerra ha dato alle '
           'fiamme e distrutto. Non dico di non sentirmela vicina, ma gli '
           'Elea con Zanan una guerra non l\'avevano mica... Fra farsi male '
           'picchiandosi e farsi male mentre ti picchiano e basta c\'è una '
           'certa differenza.',

    # --- FRON: che cosa vuol dire fare il suo mestiere
    12760: 'Per mettere insieme un viaggio migliore bisogna sapere sempre '
           'come stanno le cose in ogni posto. Anche se quel posto è dentro '
           'il fuoco, dentro l\'acqua, dentro l\'erba, dentro il bosco, '
           'sottoterra o dentro le nuvole. Chi organizza viaggi ha meno peso '
           'addosso di una guida turistica, perché non deve fare da scorta ai '
           'clienti; però deve esplorare zone dove non è mai andato nessuno e '
           'trattare a muso duro, e per questo gli si chiede di saper '
           'combattere, e bene.',

    # --- RENAI: quando non si sa ancora chi è
    12776: '...Sarebbe meglio che non mi venisse vicino.',

    # --- RENAI: dopo la storia di Regulus
    12770: '"Ehm... " + cdatan(CDATAN_NAME, CHARA_PLAYER) + "? Allora '
           'conosceva mio fratello. Mi scusi se a suo tempo le ha dato dei '
           'fastidi..."',
    12771: 'Adesso come adesso la forma umana riesco a tenerla, ma non è che '
           'l\'erosione del Meshera sia finita: i tentacoli mi escono da '
           'soli, le braccia mi si gonfiano all\'improvviso, e se mi '
           'indebolisco il corpo se lo prende lui. Mio fratello tutte le sere '
           'mi collega i nervi e mi regola...',
    12772: 'Collegarmi a mio fratello tutte le sere... c-che roba un po\' '
           'oscena, a dirla così.',

    # --- RENAI: tutte le volte dopo
    12766: 'Mio fratello è sempre stato apprensivo... per me ha fatto un '
           'sacco di pazzie. Da un po\' mi viene da pensare che la mia '
           'esistenza gli sia diventata una palla al piede.',
}
