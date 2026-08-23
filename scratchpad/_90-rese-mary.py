# -*- coding: utf-8 -*-
"""90a - MARY l'entomologa (`chat.hsp:9854`-`:9982`, 31 firme).

「蟲使いのメアリー」, «<Mary> l'entomologa» (`db_creature.hsp:76576`): il genere
sta nel nome, come per Marka e Melget. Studia gli insetti, e per colpa dei suoi
esperimenti ha trasformato in un mostro <Alice> la formica gigante
(`db_creature.hsp:62712`), che e' la bestiola della **figlia**. La missione e'
rimetterla a posto prima che la figlia lo scopra.

Registro: donna adulta, chiacchierona, 〜わ / 〜のよ / 〜かしら, e un fondo di
imbarazzo — mezza missione e' lei che si copre le spalle.

LESSICO EREDITATO (non deciso qui):
  - «<Mary> l'entomologa»          db_creature.hsp:76576
  - «<Alice> la formica gigante»   db_creature.hsp:62712, db_card.hsp:6809
  - «[cura per la mutazione speciale]»  ⭐ text.hsp:11624, il **diario della
                                   missione**: la riga `:9958` che la consegna
                                   deve dire la stessa cosa, parola per parola
  - «bacchetta di mutamento di creatura»   chat.hsp:24337
  - «pozione di cura della mutazione»      db_item.hsp:146861-:146862
  - «libro di resurrezione»                db_item.hsp:142959-:142960
  - «Sigillo Eterno»                       chat.hsp:16200 e altri 46 siti
  - «Nefia»                                chat.hsp:2307

LESSICO DECISO QUI (va in glossario):
  - 館長 / «chief librarian» -> **il direttore della biblioteca**. Il progetto
    non ha ne' 館長 ne' «librarian» da nessuna parte.
  - ゴッドロイヤルゼリー / «godly royal jelly» -> **pappa reale divina**.
  - 森の王様 / «king of the forest» -> **il re della foresta**.

⭐⭐⭐ DEROGA 1 — IL BISTICCIO SULLA FORMICA, CHE L'INGLESE BUTTA VIA.
`:9942` in giapponese e' 「ありがとうねぇ、アリだけに。」: 「ありがとう」 contiene
「アリ」, la formica, e Mary lo fa notare — una battuta brutta apposta, detta
dalla donna che ha trasformato in mostro una formica. L'inglese la cancella e
scrive «Thank you so much!».

Non si cancella, si **rifa'**: il progetto ha gia' deciso che «si rende il
gioco, non le sillabe» (`decisioni.md`, le fusioni delle razze — ダゴンズイ e'
«il pesce gatto Dagon», エンタメイド・ザンコック e' «la spettacameriera
cuocrudele»), e li' il precedente e' dell'inglese stesso, che i giochi di
parole li ricostruisce invece di tradurli. Qui l'italiano ha la parola giusta
gia' in mano, perche' Alice **e'** «la formica gigante»:

    «Grazie mille, eh. E non e' una formicalita'.»

(formalita' -> formicalita'.) Stessa battuta, stesso posto, stessa qualita' di
barzelletta.

ALTRE DEROGHE DICHIARATE
2. `:9862` e `:9863` - L'INGLESE HA CAPITO MALE, due volte di fila. Il
   giapponese di `:9862` e' 「森の王様の力も借りてここまで来たけれど」 — *sono
   arrivata fin qui anche grazie alla forza del re della foresta* — e l'inglese
   lo mette al futuro con un ripensamento in mezzo («I'll borrow the power...
   hang on, ...oh no!»). Peggio `:9863`:
   「私たちは神の間を真面目に目指しているのよ」 e' *puntiamo sul serio al
   Sigillo Eterno*, e l'inglese scrive «we have the goal of making the
   relations between the gods grave», cioe' ha letto 神の間 come *i rapporti fra
   gli dei*. E' il nome di un posto, ed e' nel dizionario da 46 siti. Si segue
   il giapponese (57a).
3. `:9858` - Stessa famiglia. 「アリスは私が置いてきたわ」 e' *Alice l'ho
   lasciata indietro io*; l'inglese aggiunge un «I told her clearly» che il
   giapponese non ha, e attacca 「ついていけない」 (*non ce la faccio a stare
   dietro a questa Nefia*) alla formica invece che a lei. Il soggetto e' Mary:
   e' lei che fatica.
4. `:9882` - 「さん」 dopo il nome del giocatore non si rende: l'italiano non ha
   il suffisso di cortesia, e appiccicare «signore» darebbe un genere a chi non
   ce l'ha (75a). Resta il nome nudo, come fa l'inglese.
5. `:9931` e `:9932` - 「渡す」/「渡さない」 sono azioni fra parentesi anche
   nell'inglese («(Hand one over)»), non parlato: restano infinito e parentesi,
   e la fila si accorda al suo interno (49a).

PERIMETRO: 31 firme, zero occorrenze fuori dal blocco e zero in altri file.
Nessun contraccolpo.

MENU: due file, di 2 voci — il tetto delle due colonne non morde.

⚠️ Accenti veri; niente «dèi» e simili (lezione del lotto di MELGET).
"""

RESE = {

    # --- la Culla del Caos
    9858: 'Ah, Alice l\'ho lasciata indietro io. Diciamocelo: a questa Nefia '
          'non riesco a stare dietro...',
    9862: 'Sono arrivata fin qui grazie anche al re della foresta, ma si è '
          'fatta un po\'... anzi, parecchio dura. Tu invece sei in scioltezza... '
          'che roba.',
    9863: 'Restare senza i nostri studi sugli insetti sarebbe un guaio, quindi '
          'al Sigillo Eterno ci puntiamo sul serio. Nel nostro piccolo, eh.',

    # --- a missione finita
    9870: 'Acqua in bocca con mia figlia, mi raccomando.',

    # --- la cura, e la vera forma di Alice
    9874: 'Gliel\'hai data, la medicina! Bene, vediamo come sta Alice...',
    9877: 'M-morta stecchita...',
    9880: '?! Alice... quella forma...?',
    9881: 'Sei tornata come prima, tutta intera! Per un momento ho temuto il '
          'peggio. ...E a quanto pare parli di nuovo come le persone. Che '
          'sollievo.',
    9882: 'cdatan(CDATAN_NAME, CHARA_PLAYER) + ", grazie! Così mia figlia non '
          'mi odierà. Se venisse a sapere che gliel\'ho ridotta in quello stato '
          'mentre me la teneva in custodia... ohi ohi."',
    9883: 'Eh? Alice non è mia figlia. Non l\'ho mai detto, che io ricordi...? '
          'Alice si era persa nel bosco ed era una formica randagia, e mia '
          'figlia l\'ha raccolta. Adesso è la sua bestiola del cuore... o forse '
          'il suo braccio destro? E comunque, \\"tornata come prima\\" vuol dire '
          'che resta pur sempre una formica.',
    9884: 'Insomma, questo è il compenso più il prezzo del silenzio. Mi hai '
          'salvata davvero!',
    9902: 'Scusa, ma la medicina dalla tu ad Alice, fino in fondo.',

    # --- i tre oggetti da portare
    9907: 'Allora. Gli oggetti che mi servono sono diversi, quindi comincerei '
          'da quelli facili.',
    9911: 'Dunque. Stavolta voglio che mi porti una bacchetta di mutamento di '
          'creatura.',
    9914: 'Dunque. Stavolta voglio che mi porti un libro di resurrezione.',
    9917: 'Con questo siamo all\'ultimo! Voglio che mi porti una pozione di cura '
          'della mutazione.',
    9931: '(Consegnarne uno)',
    9932: '(Non consegnare niente)',
    9933: 'Ah? Che sia il caso di chiederti se ce l\'hai già addosso?',
    9936: 'Ah, no...? Se fai in fretta mi rendi un favore.',
    9942: 'Grazie mille, eh. E non è una formicalità.',
    9946: 'Ehm... Combino quel che mi hai portato nelle dosi che mi ha detto il '
          'direttore della biblioteca... e ci mescolo la pappa reale divina che '
          'mi sono procurata...',
    9956: 'Ecco, la cura per la mutazione speciale è pronta! Io riordino qui: '
          'ad Alice dalla tu, per favore.',
    9958: 'Hai ottenuto la [cura per la mutazione speciale].',
    9963: 'È per quella creaturina: sbrigati il più possibile.',

    # --- l'inizio della missione
    9967: 'È una tragedia! Una mattina mi sveglio e la nostra Alice si era '
          'trasformata in quel coso orribile! E non riesce più nemmeno a '
          'parlare come le persone...!',
    9968: 'Non è affar mio',
    9969: 'Ti do una mano',
    9970: 'Ne ho parlato con il direttore della biblioteca qui, e pare che per '
          'rimetterla com\'era servano diversi oggetti. Il compenso c\'è: non è '
          'che mi aiuteresti a raccoglierli?',
    9973: 'Grazie mille! Così posso dedicarmi anima e corpo allo studio degli '
          'insetti.',
    9978: 'Ma no! E adesso come la guardo in faccia, mia figlia...',
}
