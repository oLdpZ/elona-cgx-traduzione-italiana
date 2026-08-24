# -*- coding: utf-8 -*-
"""91a - ALLEN il ricercatore (`chat.hsp:15145`-`:15199`, 23 firme).

「調査隊員の『アレン』」, «<Allen> il ricercatore» (`db_creature.hsp:51025`,
`db_card.hsp:2545`). Sta a **Zaile** e appartiene al gruppo di ricerca andato
nella **valle di Raskilis** a studiare gli effetti del vento d'etere; la
missione e' 「調査隊壊滅の危機」, «[Lv. 180] Il gruppo di ricerca in pericolo»
(`text.hsp:11544`).

⭐ IL BLOCCO E' UN PERSONAGGIO CHE SI CANCELLA MENTRE PARLA. Nel ramo `>= 900`
Allen ha gia' perso i compagni — non morti: **dimenticati**, mangiati dalla
bestia che divora i ricordi. Il giapponese lo mette in scena con le frasi che
si accorciano fino a spegnersi: 「それから…。」「調査隊？は…。」「ええと…。」
Sono tre righe da tre parole, e vanno rese **corte allo stesso modo**: se
l'italiano le riempie, il personaggio smette di dimenticare.

REGISTRO: uomo adulto, 「俺」, parlata sbrigativa e un po' rude
(「クソ」, 「駄目だ！」), ma cortese col giocatore (「君」). Nel ramo 900 la
rudezza resta e sotto c'e' il panico.

LESSICO EREDITATO (non deciso qui):
  - «<Allen> il ricercatore»          db_creature.hsp:51025, db_card.hsp:2545
  - ⭐ «il gruppo (di ricerca)» (調査隊)   text.hsp:11554, **il diario della
                                      missione**: «<Allen>, a Zaile, mi ha
                                      chiesto di riportare da Raskilis i
                                      compagni del gruppo» — e' la riga che il
                                      giocatore ha in mano mentre parla con lui
  - «Il gruppo di ricerca in pericolo»    text.hsp:11544, il titolo
  - «le bestie nere» (黒い獣)         chat.hsp:15440, la donna all'imbocco
                                      della valle, **nella stessa missione**
  - «Raskilis», «Valle di Raskilis»   chat.hsp:15470, text.hsp:2908, :2911
  - «il vento d'etere»                chat.hsp:7682, :9500, main.hsp:1229 e altri
  - «il bar»                          chat.hsp:1549

LESSICO DECISO QUI (va in glossario):
  - 生態系 -> **ecosistema**. Non c'era da nessuna parte. La parola dotta ci
    sta: la riga e' la sola in cui Allen parla da ricercatore, ed e' quello che
    lo distingue dagli altri sfollati di Raskilis.
  - ラエス / «Laes» -> **Laes**. ⚠️ Compare **una volta sola in tutto il
    sorgente** (`chat.hsp:15190`): non e' una creatura, non ha un blocco, non
    ha un epiteto. Chi lo cercasse in `db_creature.hsp` non lo troverebbe.
  - 調査隊長 -> **il capo del gruppo**, costruito su «il gruppo» del diario.

⭐⭐⭐ DEROGA 1 — LE TRE RIGHE CHE SI SPENGONO, E L'INGLESE CHE NE RIEMPIE UNA.
`:15159` in giapponese e' 「調査隊？は…。」: quattro caratteri e due segni
d'interpunzione, in cui **la parola gli si sfalda in bocca** — dice «gruppo di
ricerca», ci mette un punto interrogativo sopra come se non fosse sicuro di
averla detta bene, e poi si perde. L'inglese la spiega: «The research team - if
it could be called that - they were...», che e' una glossa da traduttore, non
una frase di un uomo che sta dimenticando.

Si tiene la forma corta, con l'esitazione dentro la parola e non in un inciso:
«Il gruppo di... ricerca? loro...». ⚠️ Le tre righe `:15158`, `:15159` e
`:15160` vanno lette **insieme**: sono una scala che scende, e la misura conta
piu' del contenuto.

⭐⭐ DEROGA 2 — 「調査隊なのになんで俺一人なんだ」 E' UN GIOCO SULLA PAROLA.
`:15153`: 隊 e' il *gruppo*, e la battuta e' che di gruppo e' rimasto uno solo.
L'inglese lo risolve con le virgolette: «why would you call it a research
\"team\" if I'm the only person in it?!». In italiano le virgolette non
servono, perche' «gruppo» porta il numero addosso: «si chiama gruppo di
ricerca, e allora perche' sono da solo?». La parola e' quella del diario, e va
tenuta identica proprio perche' e' su di lei che la battuta gira.

⭐ DEROGA 3 — 「もっと綺麗に忘れているはずなのに」.
`:15155`: 綺麗に忘れる non e' *dimenticare completamente* (l'inglese scrive
«forget them completely») ma *dimenticare pulito*, senza lasciare i bordi.
E' l'immagine che regge tutto il blocco — quel che lo tormenta non e' il vuoto,
sono i residui — e in italiano si dice tale e quale: «li avrei dimenticati
puliti». Si conserva.

ALTRE DEROGHE DICHIARATE
4. `:15190` - IL GENERE DEL GIOCATORE. 「君は強そうだけど」 non puo' diventare
   «sembri uno forte»: «forte» da solo non ha genere e basta («Sembri forte,
   ma...»).
5. `:15154` - 「隊長はなんか紫っぽい格好をしていた気がするな」: il viola del
   capo e' l'unico dettaglio che gli resta, e resta **incerto** (なんか, っぽい,
   気がする — tre attenuazioni in fila). Si tengono tutte e tre: «il capo mi
   pare avesse addosso qualcosa sul viola».
6. `:15157` - 「アイツが…誰だっけ？」: la persona che gli aveva dato l'allarme
   e' gia' stata mangiata, e la riga lo mostra perdendola a meta' frase. Non si
   riscrive in una frase intera.
7. `:15179` - 「バーの酒で一杯やりたい」: 酒 e' generico, non sake. Si dice «un
   bicchiere al bar» (`chat.hsp:1549` per il bar).

PERIMETRO: 23 firme su 25 nel blocco (`:15185` «Fammici pensare» e `:15186`
«D'accordo» erano gia' rese altrove), zero occorrenze fuori dal blocco
(`python scratchpad/_85-blocco.py 15145`).

MENU: due, da 2 voci l'uno — il tetto delle due colonne non morde.

⚠️ Accenti veri; niente virgolette tipografiche e niente caratteri a due byte.
"""

RESE = {
    # --- >= 900: i compagni sono stati dimenticati
    15148: 'Il gruppo di ricerca?',
    15149: 'Sarà una tua impressione',
    15150: 'Mi sa che... ti avevo chiesto qualcosa, ma non me lo ricordo...',
    15153: 'Adesso che ci penso... si chiama gruppo di ricerca, e allora '
           'perché sono da solo?! Non torna. Dei compagni li avevo di '
           'sicuro...',
    15154: 'Niente da fare! Che c\'erano me lo ricordo, ma come in una nebbia: '
           'né i nomi né quanti fossero! Erano tutti vestiti uguale... no, il '
           'capo mi pare avesse addosso qualcosa sul viola...',
    15155: 'Merda, perché li dimentico così a metà?? Se quella bestia se li '
           'fosse solo mangiati, li avrei dimenticati puliti.',
    15156: 'Ricorda... ecco. Noi eravamo venuti qui per studiare che effetti '
           'avesse il vento d\'etere sull\'ecosistema della valle. Poi da un '
           'certo giorno in poi ho cominciato a non ricordarmi più il mio '
           'paese.',
    15157: 'Quello lì diceva che non era una cosa normale... come si chiamava? '
           'Insomma, è nato un putiferio. E intanto arriva la voce che nella '
           'valle era comparsa una bestia che mangia i ricordi. E ho '
           'cominciato a non ricordarmi nemmeno la gente di questa città...',
    15158: 'E poi...',
    15159: 'Il gruppo di... ricerca? loro...',
    15160: 'Ecco...',
    15161: 'Che brividi',
    15162: 'Non è niente di che',
    15163: 'Scusa. Di che stavamo parlando?',
    15166: 'Magari fosse così...',
    15169: '???',
    15174: 'Dici? Eppure mi pareva una cosa importante...',

    # --- 1: l'incarico accettato
    15179: 'Quando saranno tornati tutti sani e salvi mi voglio fare un '
           'bicchiere al bar. La paura si dimentica solo bevendo qualcosa di '
           'buono.',

    # --- 0: il primo incontro
    15183: 'Oh, un viandante? ...Senti, posso chiederti un favore?',
    15184: 'Mi sono ferito, e i compagni mi hanno lasciato qui e sono tornati '
           'a Raskilis per un\'altra ricerca. Quel posto è pericoloso. '
           'Dicevano di cercare un appiglio per rimettere le cose a posto, ma '
           'lo so che non è più roba che possiamo sbrogliare da soli.',
    15187: 'Il capo si sta agitando per questa storia. Convincilo in qualche '
           'modo e riportali tutti indietro...!',
    15190: 'Il capo del gruppo si chiama Laes. Sembri forte, ma con le bestie '
           'nere sta\' attento davvero.',
    15195: 'Ti prego... Qualcuno è un po\' esaltato, ma sono tutta brava '
           'gente.',
}
