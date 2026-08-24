# -*- coding: utf-8 -*-
"""91a - REGULUS l'uomo modificato (`chat.hsp:12779`-`:12871`, 19 firme).

「改造人間『エユル』」, «<Regulus> l'uomo modificato» (`db_creature.hsp:71122`,
`db_card.hsp:5964`). ⚠️ In giapponese si chiama **エユル**, ma l'inglese e
l'italiano lo chiamano gia' **Regulus** dappertutto (`chat.hsp:2015`, `:2117`,
`screen.hsp:1750`, `text.hsp:9810`): il nome giapponese non entra qui, nemmeno
in `:12829` dove si presenta.

Cavia dell'istituto di Zanan, scappato dopo l'operazione che gli ha dato il
controllo del Meshera che ha in corpo; torna al campo di prova per la sorella
**<Renai>**, che era nella cella accanto alla sua. La storia finisce con i due
fusi in un corpo solo.

REGISTRO: 「オレ」/「あんた」, parlata larga e diretta da uomo pratico, e la
cosa che la rende quel che e' e' che le frasi piu' terribili le dice con lo
stesso tono di tutte le altre.

LESSICO EREDITATO (non deciso qui):
  - «Regulus», «<Regulus> l'uomo modificato»   db_creature.hsp:71122
  - «<Renai> la calamita' repressa»   db_creature.hsp:62040 — e nel dialogo il
                                      nome nudo, come in `screen.hsp:1750`
  - «il Meshera», «i Meshera»         chat.hsp:7652, :10237, action.hsp:17270 —
                                      ⚠️ **maschile e invariabile**: «il
                                      Meshera che ho in corpo», non «la»
  - «Zanan», «l'istituto», «le armi biologiche»   chat.hsp:2116, :2117
  - «gas nervino» (神経ガス)          map.hsp:14836, chat.hsp:24462, che e'
                                      **lo stesso impianto** visto dalla parte
                                      dell'informatore
  - «diario del ricercatore»          db_item.hsp:138165, l'oggetto che
                                      `:12788` consegna
  - «il valico» (関所)                text.hsp:9810

LESSICO DECISO QUI (va in glossario):
  - 独房 -> **cella**. Le due celle numerate (14 e 16) sono il cuore del
    blocco e vanno dette con la stessa parola tutte e tre le volte.
  - 素体 -> **materiale di partenza**. E' il termine da laboratorio con cui
    l'istituto chiama gli uomini che usa, e la riga vive di quel gelo.
  - 菌 (il Meshera visto da dentro) -> **il fungo**. L'inglese dice
    «bacteria», ma il Meshera nel gioco non e' un batterio.

⭐⭐⭐ DEROGA 1 — LA FRASE CHE L'INGLESE NON TRADUCE, ED E' QUELLA CHE DICE CHI E'.
`:12819` in giapponese finisce cosi':

    「もし適合できずに苦しんでいたのなら…その時は、楽にしてやりたい。」

*e se invece non si fossero adattati e stessero soffrendo... allora vorrei
dar loro pace*. Sta parlando degli altri prigionieri **e di sua sorella**, e
sta dicendo che se la trovera' in quello stato la uccidera' lui.

L'inglese si ferma una frase prima: «There's a chance she may have been able
to adapt, just like me.» Butta la coda, e con la coda butta il motivo per cui
questo blocco esiste — Regulus non sta andando a salvare qualcuno, sta andando
preparato a non poterlo fare. Si segue il giapponese (57a).

⭐⭐ DEROGA 2 — 「二人で」, I DUE CHE ADESSO SONO UNO.
`:12782` e' dopo la fusione: 「このまま二人で冒険者としてやっていこうと思って
いるんだ」. L'inglese scrive «we will be able to continue working together as
adventurers», che si legge come *io e te, giocatore*. Non e': i due sono
**Regulus e Renai**, dentro lo stesso corpo — lo dice `screen.hsp:1750`, gia'
reso, «Qui accanto a me anche Renai fa il tifo per te». Si scrive «noi due»
con Renai nominata subito prima nel blocco, e la riga resta sua.

⭐ DEROGA 3 — IL NOME DELLA SORELLA ARRIVA DUE VOLTE.
`:12786` in giapponese e' 「レナイが！ついにオレの妹が見つかったんだ！」: due
esclamazioni, prima il nome e poi il grado di parentela, come parla uno che ha
appena finito di cercare per mesi. L'inglese le fonde in una («At last, I've
found my sister, Renai!»). Si tengono separate.

ALTRE DEROGHE DICHIARATE
4. `:12788` - 手帳 e' un *taccuino*, ma l'oggetto che il gioco consegna nella
   riga dopo si chiama «diario del ricercatore» (`db_item.hsp:138165`). Si
   dice **«il diario»**, perche' il giocatore deve riconoscere nell'inventario
   la cosa di cui gli si sta parlando. Il giapponese e' gia' incoerente per
   conto suo (手帳 qui, 《研究員の閻魔帳》 sull'oggetto).
5. `:12816` - 「殺人的な加速」: l'accelerazione «da ammazzare» non e' un modo di
   dire, e la riga dopo lo conferma («un cittadino qualunque ci lascerebbe la
   pelle»). Si tiene letterale.
6. `:12832` NON E' IN QUESTO LOTTO. La firma di 「ちょっと待って」 vale anche per
   `:10398`, nel blocco della Nave Magica, e `--da-tradurre` la assegna alla
   prima occorrenza: si rendera' li'. E' l'unica firma del blocco con
   occorrenze fuori (`_85-blocco.py 12779` -> «con occorrenze FUORI: 1»), e
   siccome e' una voce di menu generica non c'e' contraccolpo da temere.

7. LE QUATTRO RIGHE PIU' LUNGHE DELL'INGLESE, divise in due mucchi.
   (tetto di un `chatMore`: 13 righe, quindi non morde in nessun caso)
     `:12819`  5 contro **3**: e' la riga della DEROGA 1, dove l'inglese
               taglia una frase intera. La riga in piu' e' sua.
     `:12817`  5 contro 4: l'inglese scrive «Meshera» dove il giapponese dice
               「旧型メシェーラ」, il Meshera **di vecchio tipo**. Anche qui il
               pezzo e' loro.
     `:12809` e `:12816`  4 contro 3: qui no, e' italiano piu' lungo e basta.
               Accorciate una volta, restano una riga sopra e si dichiarano.

PERIMETRO: 19 firme (20 nel blocco, meno `:12832` che appartiene a un altro
lotto), zero contraccolpo.

MENU: uno solo, di 2 voci — il tetto delle due colonne non morde.

⚠️ Accenti veri; niente virgolette tipografiche e niente caratteri a due byte.
"""

RESE = {
    # --- >= 1003: dopo la fusione
    12782: 'Con un corpo così a casa non ci torno più. Per fortuna il fisico '
           'è migliorato, così ho pensato che continueremo a fare gli '
           'avventurieri noi due.',

    # --- 1002: il ritrovamento
    12786: '"Oh, " + cdatan(CDATAN_NAME, CHARA_PLAYER) + "! Renai! Alla fine '
           'mia sorella l\'ho trovata! Quanta fatica, davvero... Quando l\'ho '
           'trovata il corpo le si era già deformato, di coscienza non ne '
           'aveva quasi più e mi è saltata addosso."',
    12787: 'Per farla breve: mi sono fatto assimilare fin quasi in fondo, così '
           'ho collegato i nervi e ho strappato il controllo al fungo, e in '
           'qualche modo l\'ho riportata indietro. Non c\'era nessuna garanzia '
           'di riuscire a controllarne due insieme, quindi era proprio un '
           'tutto o niente.',
    12788: 'Ah, e se riesco a controllare il Meshera pare sia perché il '
           'sistema nervoso me l\'hanno rinforzato con farmaci e modifiche al '
           'corpo. Stava scritto nel diario che ho trovato quando sono andato '
           'all\'istituto con te... Ecco, giusto: il diario tienilo tu. '
           'L\'avevo tenuto perché poteva servire da traccia, ma ormai non mi '
           'serve più. Brucialo, vendilo o usalo per ricattare i militari di '
           'Zanan: fanne quello che vuoi.',

    # --- >= 1000: la ricerca
    12797: 'Da allora sono andato in giro per un po\' di posti a chiedere, ma '
           'per ora non è saltato fuori niente. ...Devo trovarla in fretta. '
           'Lei la solitudine non l\'ha mai retta.',

    # --- 100: la cella vuota
    12803: 'Nella cella numero 16 c\'erano i segni di uno sfondamento '
           'dall\'interno. Renai è viva da qualche parte, di sicuro. Una '
           'speranza c\'è ancora...',

    # --- 4: la cella accanto
    12809: 'Io ero rinchiuso nella cella numero 14, accanto a quella di mia '
           'sorella. Ce l\'avevo a un muro di distanza, e potevo darle solo '
           'parole di incoraggiamento senza niente dietro...',

    # --- 3: l'arrivo al campo di prova
    12816: 'Che roba... un\'accelerazione da ammazzare... Si capisce perché lo '
           'fanno usare solo agli avventurieri: un cittadino qualunque ci '
           'lascerebbe la pelle.',
    12817: '...Comunque al campo di prova ci siamo arrivati. Qui sviluppavano '
           'e provavano armi basate sul potenziamento biologico del Meshera '
           'di vecchio tipo. E come materiale di partenza usavano uomini... '
           'io sono uno di quelli.',
    12818: 'Io me la sono svignata appena ho visto uno spiraglio, finita '
           'l\'operazione per controllare il Meshera che ho in corpo; ma in '
           'fondo, nella cella numero 16, mia sorella, \\"Renai\\", dovrebbe '
           'essere ancora prigioniera. ...Ero così preso dalla fuga che a '
           'venirla a prendere ci ho messo tutto questo tempo.',
    12819: 'Con una situazione da cui perfino l\'esercito si è tirato indietro '
           'le speranze sono poche, ma... può darsi che si sia adattata come '
           'me. Vale anche per gli altri. E se invece non si fossero adattati '
           'e stessero soffrendo... allora voglio dar loro pace.',
    12820: 'Quando ripiegare lo decidi tu. Toccherà rimontare su quel coso, ma '
           'pazienza. Poi... eh?',
    12821: '...Brutta faccenda. Pare che abbiano sparso un gas nervino potente '
           'per bloccare i soggetti. Probabile che i ricercatori l\'abbiano '
           'diffuso nel settore di detenzione, ma che sia arrivato fin qui '
           'all\'ingresso... Meglio stare attenti.',

    # --- <= 2: il primo incontro al valico
    12829: '"Tu sei " + cdatan(CDATAN_AKA, CHARA_PLAYER) + " " + '
           'cdatan(CDATAN_NAME, CHARA_PLAYER) + ", giusto. Io sono Regulus. '
           'Piacere."',
    12830: 'Ho letto i documenti che mi hanno dato: pare che ci muoveremo con '
           'un veicolo supersonico a propulsione nucleare preso in prestito '
           'dagli dei, e che saremo a destinazione in un attimo. Sembra una '
           'cosa grossa.',
    12833: 'Partiamo',
    12835: 'Che ne dici, partiamo?',
    12838: 'Dobbiamo risalire su quel coso...',
    12866: 'Va bene. Io aspetto qui.',
}
