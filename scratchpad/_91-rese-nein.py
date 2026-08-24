# -*- coding: utf-8 -*-
"""91a - NEIN la strega volante (`chat.hsp:10442`-`:10520`, 24 firme).

「空を翔ける『ネイン』」, «<Nein> la strega volante» (`db_creature.hsp:75902`,
`db_card.hsp:6705`). Ragazzina prodigio di una casata di maghi di Eulderna,
saltata avanti di un anno e prima della classe; sta sulla **Nave Magica**
(`text.hsp:11149`) e la missione e' quella del **monolito di mana** da
catturarle e portarle davanti.

REGISTRO: letto nel repertorio (`db_creature.hsp:75870`-`:75888`) — «Certo, e'
normale essere gelosi del mio talento!», «Chi non ha talento si scalda subito,
eh?», «Che pena enorme.» Boria da secchiona, 「あたし」/「あんた」, e sotto
un'insicurezza che esplode appena il libro non si lascia leggere. Il «tu» e'
sprezzante, mai confidenziale.

LESSICO EREDITATO (non deciso qui):
  - «<Nein> la strega volante»        db_creature.hsp:75902, db_card.hsp:6705
  - «il monolito di mana»             db_creature.hsp:65463, db_card.hsp:4989
  - ⭐ «forma di vita artificiale con circuiti magici incisi addosso»
                                      text.hsp:11157, **il diario della
                                      missione**: le righe :10505 e :10506 che
                                      la descrivono devono dire le stesse
                                      parole, perche' il giocatore le legge
                                      appaiate
  - «la Nave Magica (Eulderna)»       text.hsp:11149, :11157
  - «l'incantatore di corte» (王宮魔導士)   db_creature.hsp:67065, db_card.hsp:5262
  - «Lettura» (読書, l'abilita')      skill.hsp:192
  - «cerchio magico» (魔法陣)         chat.hsp:8941, db_item.hsp:151038
  - «artefatto» (アーティファクト)    chat.hsp:8433, :10159, :11367 e altri
  - «grimorio» (魔法書/魔術書)        chat.hsp:14356
  - «Eulderna», elitaria per definizione: 「エリート主義のエウダーナ」,
                                      chat.hsp:2132

LESSICO DECISO QUI (va in glossario):
  - ベルム家 / «Bellum family» -> **casa Bellum**. ⚠️ Il nome NON e' inventato
    e non viene dalla riga :10477: l'inglese di monte lo scrive per esteso in
    `scene2.hsp:3204` («I'm from House Bellum in Eulderna») e in
    `db_item.hsp:51432` («the Belm family»). Si sceglie la forma di `scene2`,
    che e' quella di un dialogo scritto per esteso.
  - 魔力電池 / «mana battery» -> **batteria di mana**. Non c'era da nessuna
    parte; regge il confronto con «monolito di mana», che e' la stessa cosa
    vista dall'altra parte.
  - 魔術研 / «magicians of the Imperial Court» -> **l'istituto di magia**.
    Abbreviazione di 魔術研究所; l'inglese la fonde col palazzo e perde il
    secondo ente.
  - 王宮魔導士長 -> **capo degli incantatori di corte**, costruito sul nome di
    creatura gia' deciso.
  - 転写魔法 -> **magia di trascrizione**.

⭐⭐⭐ DEROGA 1 — LA SORELLA SPARITA, E DOVE L'INGLESE LA FA SPARIRE.
`:10445` in giapponese e' 「行方不明のミネア姉さま」 e basta: *mia sorella
Minea, che e' scomparsa*. L'inglese aggiunge **dove**: «that went missing
within the ruins of Nefia».

Non e' un abbellimento innocuo, e' **smentito dal gioco stesso**. Minea
esiste: e' `<Minea> The Puppeteer` di `scene2.hsp:2581` e seguenti, e li'
racconta lei la sua storia — ha inventato una magia per manovrare gli uomini,
l'esaminatore l'ha bocciata come volgare magia di dominio, e «soon people began
to call me the shame of House Bellum»: i genitori hanno tagliato i ponti e lei
se n'e' andata a fare l'avventuriera (`scene2.hsp:3213`, `:3219`). Non e'
sparita in una Nefia: e' stata **cacciata di casa**, la casa che Nein vuole far
tornare grande. Nella stessa scena parla della propria sorella minore, e la
sorella minore e' Nein.

Si segue il giapponese e si tace il dove (57a: quando l'inglese aggiunge un
fatto che il resto del gioco smentisce, il fatto non si eredita).

⚠️ Minea **non ha ancora un nome italiano**: `scene2.hsp` non e' nel
dizionario. Chi lo tradurra' trovera' qui che il suo epiteto e' *The
Puppeteer* e che e' la sorella maggiore di Nein.

⭐⭐ DEROGA 2 — «QUESTO L'ABBIAMO FATTO AL CORSO», CHE L'INGLESE CANCELLA.
`:10473` in giapponese e' 「あ、ここは施術ゼミでやったところだわ」: *ah, questo
pezzo l'abbiamo fatto al corso di incantesimi*. L'inglese lo butta e scrive «Ah,
this spot looks a bit more interesting».

E' esattamente la battuta degli allievi del seminario,
「これゼミでやったところだ！」, resa **«Questo l'abbiamo appena fatto al
corso!»** (`db_creature.hsp:54616`). Con quelle parole la riga dice due cose in
una: che Nein e' ancora una studentessa, e che sta per sbattere contro
qualcosa che al corso non c'era. Si conserva, e si conserva **con le stesse
parole**, perche' l'eco vale solo se si sente.

⭐⭐ DEROGA 3 — L'INGLESE ROVESCIA CHI HA L'OCCHIO BUONO.
`:10513` chiude con 「パッとしない感じだけど、人を見る目はあるみたいじゃない」:
*hai un'aria dimessa, ma a giudicare la gente ci sai fare* — cioe' il merito e'
del giocatore, che ha notato lei. L'inglese sposta il soggetto su Nein e
ribalta il senso: «Nah. I've got a pretty good eye for people, and you don't
seem like a scout or someone with magical talent», che oltretutto contraddice
le due righe prima, dove Nein da' per **certo** che il giocatore l'abbia
notata. Si segue il giapponese.

ALTRE DEROGHE DICHIARATE
4. `:10488` - 「未来の王宮魔導士…いえ、魔導士長も夢じゃない」 parla di **lei**,
   non del giocatore: lo dice la coda, 「そんなあたしに認められるのだから光栄に
   思いなさい」. L'inglese lascia la frase senza soggetto e in inglese si legge
   come una promessa al giocatore. Si scioglie sul giapponese.
5. `:10488` - IL GENERE DEL GIOCATORE, preso da `referti.py` e non da me. La
   prima resa diceva «con che mezzi ci sei **riuscito**»: un participio
   riferito al giocatore, cioe' esattamente la cosa che la guida di stile
   vieta. Non l'ha vista ne' `verifica`, che guarda le firme, ne'
   `chat-lotto-misura`, che guarda le righe: l'ha vista `referti.py`, salendo
   da **8** a **9** participi. Risolto con «ce l'hai fatta», che non ha
   genere. 💡 Ecco a che serve rilanciarlo **dentro** il lotto e non solo in
   chiusura: la differenza fra 8 e 9 e' leggibile solo se il numero prima lo
   si conosce.
6. `:10504` e `:10513` - IL GENERE DEL GIOCATORE, gli altri due casi.
   「本当に来たの？」 non puo' diventare «sei venuto/a»: si gira in «ma sei
   davvero qui?». Stessa cosa per
   「凡人のくせに」 -> «un comune mortale», che e' un sostantivo (90a, la regola
   del bersaglio spostato).
7. `:10462` - 「身の程知らずってレベルじゃ…え？」 e' una frase **rotta a meta'**
   dallo stupore: la rottura si conserva («il senso della misu... eh?»), come
   l'inglese fa a modo suo.
8. `:10487` - L'UNICA RIGA PIU' LUNGA DELL'INGLESE, e la riga in piu' non e'
   mia. `chat-lotto-misura` da' 7 righe contro 6 (tetto di un `chatMore`: 13,
   quindi non morde). Le venti parole di scarto stanno tutte nella coda
   giapponese 「…と教わったのだけれど」 — *cosi' mi hanno insegnato, pero'* —
   che e' il punto della battuta: il pregiudizio su cui e' cresciuta le si sta
   sgretolando in mano. L'inglese la coda la butta e scrive una massima
   generica sugli avventurieri. Accorciare qui vorrebbe dire ributtare via lo
   stesso pezzo una seconda volta (90a). Le altre quattro righe segnalate al
   primo giro erano prolissita' mia e sono state accorciate tutte.
9. `:10505` - le due virgolette 「偶然」 e 「調査依頼」 sono l'ironia della
   riga: restano, come virgolette protette (mai le tipografiche, guida di
   stile).

PERIMETRO: 24 firme su 27 nel blocco (`:10456` e `:10475` erano gia' rese),
zero occorrenze fuori dal blocco (`python scratchpad/_85-blocco.py 10442`).

MENU: uno solo, di 2 voci — il tetto delle due colonne non morde
(`SOGLIA_DUE_COLONNE` = 10).

⚠️ Accenti veri; niente virgolette tipografiche e niente caratteri a due byte.
"""

RESE = {
    # --- 1002: dopo aver letto il libro, in ginocchio e non doma
    10445: '...Non mi arrendo. Io diventerò capo degli incantatori di corte, '
           'farò tornare grande casa Bellum e mi riprenderò anche mia sorella '
           'Minea, che è scomparsa! Non è certo qui che mi lascio abbattere!',

    # --- 1001: il libro non si lascia decifrare, e il giocatore ci prova
    10449: 'Non riuscire a decifrarlo nemmeno con il grimorio sotto gli '
           'occhi... Ma che cervelli ce l\'hanno, gli esperti del palazzo e '
           'dell\'istituto di magia...',
    10450: 'Me ne vado',
    10451: 'Provo a leggere (serve Lettura 130)',
    10452: 'Che hai da guardare?! Sparisci!',
    10458: '(Nein è allibita come non mai.)',
    10462: 'Ah? Ma tu non hai proprio il senso della misu... eh?',
    10463: 'A-aspetta, non ci credo!? Stai sparando a caso, vero...?',
    10464: 'Stop! Non dire altro! Ho detto basta! Guarda che meno!',

    # --- 1000: la decifrazione, e il muro
    10472: 'Bene, cominciamo subito a decifrare. ...Che hai da guardare, non '
           'hai niente da fare?',
    10473: 'Mh-mh, la formula di base è quasi quella delle batterie di mana '
           'in uso. Ah, questo l\'abbiamo fatto al corso di incantesimi. Ma '
           'va\', è più semplice del previsto. Vediamo la struttura magica '
           'principale...',
    10476: 'M-ma cos\'è questa roba... È diversa da quello che esiste già a '
           'partire dall\'idea. E non somiglia nemmeno alle cose uscite in '
           'questi anni. M-montarla è fuori discussione, ma almeno '
           'leggerla... vediamo, questa formula si aggancia qui e... ah, '
           'uuh...',
    10477: 'I-io sono! il prodigio di casa Bellum! Ho saltato un anno! Sono la '
           'prima della classe!? U-una cosa così... urgh!!',
    10478: 'C-che hai da guardare?! Sparisci!',

    # --- 2: la caccia al monolito di mana
    10484: 'E adesso che vuoi? Sbrigati a cercarlo, va\'. Anche se dubito che '
           'ci riuscirai.',
    10487: 'Q-quello!? Non ci posso credere, ma questo schema di sigilli nei '
           'circuiti magici non lascia dubbi: è roba dell\'esercito! Non '
           'pensavo lo portassi davvero. Un colpo di fortuna... no, con la '
           'sola fortuna non si arriva a... A me hanno insegnato che gli '
           'avventurieri sono fuorilegge che fanno il comodo loro e la magia '
           'non la sanno nemmeno usare.',
    10488: '...E va bene. Con che mezzi ce l\'hai fatta non lo so. Ma visto '
           'che ce l\'ho qui davanti, te lo riconosco. Io sarò incantatrice '
           'di corte... anzi, capo degli incantatori, e non è un sogno. Sono '
           'io a riconoscertelo: fattene un onore. Questo è il compenso.',
    10500: 'Ho preso appunti con una magia di trascrizione, quindi il mostro '
           'te lo restituisco. Se me lo tengo troppo a lungo sono guai.',

    # --- 1: la prova, e l'incarico
    10504: '...Eh? Ma sei davvero qui? Un comune mortale che non prova un '
           'briciolo di soggezione? Pazienza... e allora vediamolo, questo '
           'tuo valore. Ti metto alla prova: voglio vedere se meriti il mio '
           'tempo prezioso.',
    10505: 'Da qualche anno le forze armate della nostra Eulderna stanno '
           'sviluppando una forma di vita artificiale che immagazzina mana. È '
           'materiale riservato, quindi le specifiche non si sanno, ma di come '
           'è fatta mi importa troppo. Perciò catturamene una e portamela '
           'davanti. Che la catturi io di persona, con la posizione che ho, è '
           'un problema... ma un avventuriero che ne prende una \\"per caso\\" '
           'e poi chiede a me, che sono un genio, di \\"esaminarla\\": non c\'è '
           'niente di strano, no?',
    10506: 'Quella forma di vita, mi dicono, la stanno provando all\'aperto. '
           'Vista la resa di mana che deve dare, i circuiti magici li avrà '
           'incisi addosso in bella vista. Chi non ha studiato li scambierà '
           'per un cerchio magico storto. Il nome non si sa: notizie in giro '
           'non ce ne sono.',
    10507: 'Non è che mi aspetti chissà che, ma se la cosa riesce un compenso '
           'te lo do. Vediamo... i miei compagni di corso... anche se non '
           'voglio essere messa sullo stesso piano di quei mediocri. Vabbè, '
           'ci aggiungo pure un artefatto di mia fattura che nemmeno a loro '
           'ho ancora fatto vedere. Sempre che la cosa riesca, eh?',

    # --- 0: il primo incontro
    10513: 'E tu chi saresti. ...Ah-ah. Scommetto che hai messo gli occhi sul '
           'mio talento magico! Che vuoi, reclutarmi? O metterti a bottega da '
           'me? Fufu. Hai un\'aria dimessa, ma a giudicare la gente ci sai '
           'fare, eh.',
    10514: 'A dirla tutta non ho né il dovere né il tempo di badare ai '
           'comuni mortali... ma va bene: sono di animo grande, la '
           'possibilità la do anche a te. Fatti rivedere.',
}
