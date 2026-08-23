# -*- coding: utf-8 -*-
"""89c - URCAGUARY la gemma tenace (`chat.hsp:12332`-`:12559`, 32 firme).

Il capo dei Cavalieri Dorati, a Ol-dran: la missione dei calzini e, dietro la
toppa JAMES CUSTOM di `:12334`-`:12428`, la sua variante coi kit di
riparazione. `CDATA_SEX = 1` (`db_creature.hsp:71993`): donna, e il suo
parlato in prima persona si accorda.

IL REGISTRO STA NEL REPERTORIO (`db_creature.hsp:71913`-`:71931`), gia' reso:
«Guarda un po'! Fuahaha!», «Fatti sotto!», «Ma che faccia stanca e' quella!
Riposati!!», «Ehi ehi, non si muore per cosi' poco.», «Mangia piu' carne, piu'
carne!» — sanguigna, sbrigativa, affettuosa a modo suo, del tu con chiunque.

⭐ E da li' arriva anche la RISATA: フハハ e' **Fuahaha**, non «Fuhaha». E'
scritto in `db_creature.hsp:71913` e vale per `:12385`, `:12513`, `:12542`,
`:12552`.

LESSICO EREDITATO (non deciso qui):
  - «calzini»                      db_item.hsp:134939 e il diario text.hsp:11209
  - «kit di riparazione»           il diario text.hsp:11239
                                   (il nome pieno dell'oggetto e' «kit di
                                   riparazione di pregio», db_item.hsp:137649)
  - «kit di materiali»             db_item.hsp:144134
  - «kit di cioccolatini fatti in casa»   db_item.hsp:139834
  - «il ladro di calzini»          chat.hsp:12713, gia' reso (e' l'altra meta'
                                   di questa missione: il ladro in persona)
  - «campi di neve»                chat.hsp:12728, gia' reso, stessa missione
  - «punire»                       il diario text.hsp:11228
  - «Ol-dran»                      il diario text.hsp:11228

LESSICO DECISO QUI (va in glossario):
  - 黄金騎士団 / «the Golden Knights»  ->  **i Cavalieri Dorati**. Non e' una
    scelta: 黄金の騎士 / «golden knight» e' gia' **«il cavaliere dorato»** in
    `db_creature.hsp`, `db_card.hsp` e `action.hsp:16890` — la creatura di cui
    l'ordine e' fatto. L'ordine prende il nome dei suoi.
  - 備品調達係 / «Procurement Officer»  ->  **responsabile dei rifornimenti**.
    E' insieme un VOCATIVO al giocatore (`:12338`, `:12431`) e un titolo che
    gli viene dato (`:12473`), cioe' due bersagli del divieto di genere su tre
    siti: «addetto» si accorderebbe tutt'e tre le volte, «responsabile» e'
    invariabile. A `:12473`, dove ci vorrebbe l'articolo, la frase e' girata in
    «i rifornimenti dei Cavalieri Dorati li curi tu», che non nomina nessuno.

DEROGHE DICHIARATE
1. `:12394` e `:12473` - LO STESSO GIAPPONESE, DUE INGLESI DIVERSI, DUE FIRME.
   「根性あるじゃないか…アンタは立派な騎士団備品調達係さ！褒美をやるよ、取って
   おきな。」 a `:12394` diventa «Got some guts, don't you... Alright, here's
   your reward.» (l'inglese lascia cadere il titolo) e a `:12473` «...you're
   now in charge of equipment procurement for the Knights! Here's your
   reward.» E' la 84a al contrario — li' erano due giapponesi in un inglese,
   qui e' un giapponese in due inglesi — e la differenza la detta il sito:
   `:12473` e' la PRIMA volta che il titolo viene dato, `:12394` e' il giro
   successivo, dove il giocatore ce l'ha gia'. Due rese diverse.
2. `:12385` - l'inglese NON traduce il giapponese. 「フハハ！面白い冗談を言う
   じゃないか、照れちまうよ！」 e' la stessa battuta di `:12542` (il
   corteggiamento); l'inglese ci mette «We have no use for those. Maybe you
   should just use those for your loved ones.» Si traduce dall'inglese: sta in
   piedi da solo, e a febbraio quella e' la battuta giusta sui cioccolatini.
3. `:12545` e `:12548` - «child» / «a good child» rivolti al GIOCATORE.
   «bambino» e «bravo» si accorderebbero tutt'e due (77a, il vocativo). Si
   gira: `:12545` in terza persona generica («a quest'ora i bambini stanno a
   casa loro»), `:12548` sul nome comune femminile «creatura» (85a).
4. `:12552` - l'inglese accorcia. Il giapponese chiude con 「アタシにとっちゃ
   冗談の域を出てないのさ」 (*per me non va oltre lo scherzo*), che e' il no
   vero e proprio; l'inglese dice «That was just too much». Si segue l'inglese:
   la risata e' gia' il rifiuto, e il criterio non e' rendere il testo piu'
   ricco.
5. `:12543` - il giapponese 「おうちかえぅ」 e' storpiato apposta (il giocatore
   parla come un bambino, ed e' il gancio di 「お子ちゃま」 a `:12545`);
   l'inglese lo appiattisce in «(Leave)». Si segue l'inglese, che e' anche la
   forma con cui il progetto rende quella voce da sempre: le due battute dopo
   tengono in piedi la scena da sole.

CHIUDE LA FIRMA CONDIVISA della 89a: `:12526` (「残念だ」 / «That's too bad.»)
e' stata resa col lotto di DAIN, dove vive la sua prima occorrenza (`:11069`).
Da qui in poi `bilingui` deve tornare a zero.
"""

RESE = {

    # --- JAMES CUSTOM: la variante coi kit di riparazione (:12334-:12428)
    12337: "I miei Cavalieri Dorati si sono allenati duro. Anzi, un po' troppo: "
           "gli attrezzi li abbiamo rotti quasi tutti, e di kit di riparazione e "
           "kit di materiali ce ne servono ancora parecchi per rimettere in "
           "sesto il disastro.",
    12338: "Al lavoro, responsabile dei rifornimenti. Raccoglimene una trentina, "
           "di kit, che gli attrezzi vanno rimessi a posto: e un altro premio te "
           "lo do.",
    12344: "Aspetta ancora un po'",
    12345: "(Consegnare tutti i kit)",
    12346: "Allora? I kit di riparazione li hai portati?",
    12380: "Bene... ricevuti, questi kit.",
    12383: "Kit di cioccolatini? Aspetta il prossimo febbraio.",
    12385: "Kit di cioccolatini? Fuahaha, a noi non servono. Tienili per chi ti "
           "sta a cuore.",
    12390: "Datti una regolata. Di kit da darmi non ne hai nemmeno uno.",
    12394: "Fegato ne hai... Bene, ecco il tuo premio. Tienilo da conto.",

    # --- la missione dei calzini
    12430: "Strano... mi giro un attimo e i calzini sono spariti di nuovo, tutti "
           "quanti.",
    12431: "Al lavoro, responsabile dei rifornimenti. Altri trenta calzini, "
           "forza... E non fare quella faccia. Un altro premio te lo do.",
    12438: "(Consegnare tutti i calzini)",
    12439: "Allora? I calzini li hai portati?",
    12466: "Bene... ricevuti.",
    12469: "Datti una regolata. Di calzini da darmi non ne hai nemmeno uno.",
    12473: "Fegato ne hai... Bene: da oggi i rifornimenti dei Cavalieri Dorati li "
           "curi tu! Ecco il tuo premio, tienilo da conto.",
    12513: "Hai steso il ladro di calzini? Fuahahah! Ti guardo con altri occhi, "
           "adesso! E ora, come d'accordo, portami i calzini che ti ho chiesto.",

    # --- il primo incontro
    12520: "Entrare nei Cavalieri Dorati",
    12521: "Sono qui per corteggiarti",
    12522: "Niente di particolare",
    12523: "Oh, cercavi me per qualcosa?",
    12527: "Faccio qualunque cosa!",
    12528: "Ah, mi spiace. L'ultimo che l'ha detto poi si è rivelato un ladro. "
           "Quindi al momento non prendiamo nessuno che non conosciamo già.",
    12531: "Qualunque cosa? Uhm... Se la metti così, ti prendo in prova e vediamo "
           "come lavori.",
    12532: "Il ladro di cui ti dicevo è scappato verso i campi di neve a nordest. "
           "Può darsi che non li abbia passati: se lo vedi, puniscilo. Sono "
           "sicura che basta mostrargli un calzino e si tradisce da solo. Per il "
           "resto, procuraci trenta calzini in cambio di quelli che si è portato "
           "via.",

    # --- il corteggiamento
    12542: "Fuahaha! Che battuta! Mi fai arrossire!",
    12543: "(Andarsene)",
    12544: "Non sto scherzando",
    12545: "Su, a quest'ora i bambini stanno a casa loro. Fila.",
    12548: "Sì, sì. Che brava creatura.",
    12552: "Fuahahahaha! Fuahaha-! ...Ah, scusa. È stata troppo forte.",
}
