# -*- coding: utf-8 -*-
"""91a - SSIL la strega del divieto infranto (`chat.hsp:14928`-`:15070`, 20 firme).

「破禁の魔女『シズル』」, «<Ssil> la strega del divieto infranto»
(`db_creature.hsp:63131`, `db_card.hsp:4586`). Vive nella **Dimora della
Strega** in fondo a un bosco, e' non-morta da secoli, e la sua missione e'
mostrarle un **mazzo** con sempre piu' **tipi di carte** (`text.hsp:11097`).
Ogni cinquanta tipi racconta un pezzo di mondo: dieci ricordi in fila, che sono
il vero contenuto del blocco.

⭐ IL BLOCCO E' UNA STORIA DEL MONDO RACCONTATA DA CHI C'ERA. Le dieci battute
`:14948`-`:14975` non sono chiacchiere: nominano <Quruiza>, la civilta'
biochimica, i negromanti della fine, Sierre Terre e Rehm-Ido — cioe' cose che
il gioco ha gia' detto altrove, con parole gia' decise. Il lavoro qui e' stato
per nove decimi **cercare**, non scrivere.

REGISTRO: vecchissima, cortese e insinuante — 〜ですじゃ / 〜のう / 〜ませぬ,
e la risata 「ひひひ」/「いひひ」. La risata ha gia' una forma italiana:
«Ihihi...» (`screen.hsp:1774`, «Ssil ridacchia: Ihihi... mi tocchera'
intervenire un pochino»). Si tiene il «tu» del resto del progetto, con la
cortesia antiquata nel giro di frase e non nel pronome.

LESSICO EREDITATO (non deciso qui):
  - «<Ssil> la strega del divieto infranto»  db_creature.hsp:63131
  - ⭐ «un mazzo», «tipi di carte», «la Dimora della Strega»
                                      text.hsp:11097, **il diario della
                                      missione**: «devo mostrare a <Ssil> un
                                      mazzo che contenga almeno N tipi di
                                      carte» — le due dinamiche `:15052` e
                                      `:15056` dicono la stessa cosa e usano le
                                      stesse parole
  - «Ihihi...»                        screen.hsp:1774
  - «<Quruiza> l'ingannatrice dall'occhio finto»   db_creature.hsp:100463,
                                      chat.hsp:2334, :24328
  - «la civilta' biochimica»          chat.hsp:14350, :24421
  - «Sierre Terre», «Rehm-Ido», «Eulderna»   chat.hsp:1251, :2377
  - «il mazzo» (デッキ)               action.hsp:19128, chat.hsp:1475

LESSICO DECISO QUI (va in glossario):
  - ネクロマンサー -> **il negromante**. Nel progetto non c'era: l'unica
    occorrenza e' `db_card.hsp:5035`, ancora da tradurre.
  - 超生命 -> **creature superiori**. Non c'era.
  - ⚠️ ブラッドランナー -> **Blood Runner**, non «Blade Runner». Vedi DEROGA 2.

⭐⭐⭐ DEROGA 1 — L'INGLESE BUTTA VIA IL NUMERO CHE IL GIOCATORE CERCA.
`:15056` in giapponese e' 「ところで、今デッキに入っているカードは" + syurui +
"種類のようですのう」: *le carte che hai adesso nel mazzo mi paiono N tipi*.
E' l'unico posto del gioco dove si legge **quanti tipi si hanno gia'**, ed e'
la ragione per cui si torna a parlarle.

L'inglese la sostituisce con «Ah, let me see your deck... Not bad, not bad.»,
e la variabile `syurui` **sparisce dall'espressione**. Chi traducesse
sull'inglese perderebbe il conto per sempre, e nessuna rete se ne
accorgerebbe: l'espressione inglese e' coerente con se stessa.

L'italiano rimette `syurui` dentro, che e' il gesto opposto a quello vietato —
non si inventa un pezzo, si ricuce un pezzo che il giapponese ha e l'inglese ha
lasciato cadere (57a).

⭐⭐ DEROGA 2 — ブラッドランナー E' «BLOOD RUNNER», E LO DICE IL GIOCO.
`:14954`: l'inglese scrive «a man named Blade Runner», che e' il titolo del
film. Ma il gioco ha una sua ortografia, e non e' un'opinione:

    ブラッド  ->  blood   (「リビングブラッド」 living blood, db_creature.hsp:53421;
                          「ブラッドゴーレム」 blood golem, :82222;
                          「デッドアイズ・ブラッドスカルドラゴン」, :79753)
    ブレード  ->  blade   (「ブレードボウ」 blade bow, db_item.hsp:136506)

Otto ブラッド in `db_creature.hsp`, tutti «blood»; zero ブレード. Il nome
resta **Blood Runner**.

⭐ DEROGA 3 — CHI TORNA BAMBINO, LA PRINCIPESSA O LA TARTARUGA.
`:14966` e' Urashima Tarō: si aiuta una tartarughina e si finisce dalla
principessa del mare. Poi 「数万年ごとに子供の姿へ戻ることを繰り返し、悠久の時
を生きてきたと言っておりました」 — il soggetto non e' scritto, ma l'ultima
persona nominata e' **la principessa**, e la battuta finale
(「まるでクラゲの一種」, la medusa che ringiovanisce) e' su di lei. L'inglese
sceglie la tartaruga e la fa maschio: «He said that he returned to the form of
a child». Si tiene l'italiano sul soggetto sottinteso — «Diceva che...» — che
resta attaccato alla principessa senza doverlo dichiarare.

ALTRE DEROGHE DICHIARATE
4. `:14963` - ⭐ **LA RIGA CHE SPIEGA IL SUO NOME.** 「他人の定めた倫理や禁忌
   など邪魔なだけ」: 禁忌 e' il **divieto**, e lei e' «la strega del **divieto
   infranto**». Si rende con «i divieti», non con «i tabu'», perche' l'eco col
   nome e' l'unica cosa che il giocatore puo' mettere insieme da solo.
5. `:14948` - l'inglese aggiunge un pezzo che il giapponese non ha («I made
   some sweets just recently, in fact - it couldn't have been more than 50
   years ago»). Il giapponese dice solo che in fondo alla credenza ci sono
   dolci di piu' di cinquant'anni fa. Si segue il giapponese.
6. `:14975` - ⚠️ 神によって: **niente «dèi»**. L'accento in mezzo alla parola
   degrada in apostrofo e a schermo esce `de'i` (lezione della 90a). Si scrive
   «gli dei», senza accento.
7. `:14960` - 「弟子」 e' un discepolo **maschio** (l'inglese lo conferma con
   «the boy»), ma non e' il giocatore: l'accordo si puo' fare e si fa.
8. `:15062` - 「アンデッド化しております」: lei parla di se', quindi «passata
   non morta» accorda con lei e non col giocatore.

9. ⭐ LE TRE RIGHE PIU' LUNGHE DELL'INGLESE, e nessuna delle tre e' mia.
   `chat-lotto-misura` ne ha segnalate **otto** al primo giro: cinque erano
   prolissita' mia e sono state accorciate. Le tre che restano (`:14951` 5
   contro 4, `:14969` 9 contro 8, `:15063` 7 contro 6; tetto di un `chatMore`:
   13, quindi non morde) sono esattamente le righe dove l'inglese ha buttato
   via un pezzo:
     `:14951`  「歳は大きく違えど」 e 「力を代償とする義眼」 — l'inglese perde
               la differenza d'eta' e trasforma il **prezzo** dell'occhio in
               «powerful magic rubies», cioe' in un vantaggio;
     `:14969`  「超生命となり」 — le razze non si sono solo adattate, sono
               diventate **altro**; l'inglese scrive solo «adapted»;
     `:15063`  「デッキに入れるもの」 e 「死んだように長く暮らして」 — sparisce
               sia il mazzo sia il vivere «come morta».
   Accorciarle vorrebbe dire ributtare via lo stesso pezzo una seconda volta
   (90a).

PERIMETRO: 20 firme su 20 nel blocco, zero occorrenze fuori dal blocco
(`python scratchpad/_85-blocco.py 14928`).

MENU: nessuno — il blocco non ha `chatList`.

⚠️ Accenti veri; niente virgolette tipografiche e niente caratteri a due byte.
"""

RESE = {
    # --- il seguito non c'e' ancora
    14931: 'Da qui in avanti è ancora tutto da preparare. Intanto mi farebbe '
           'piacere che me le raccogliessi.',
    14937: 'To\', pare che un mazzo non ce l\'hai.',

    # --- i dieci ricordi, uno ogni cinquanta tipi
    14948: 'Dieci anni, vent\'anni, passano in un soffio. Anche questa casa, '
           'quando mi ci ero appena trasferita, era una bottega. In fondo alla '
           'credenza ci saranno ancora dei dolci di più di cinquant\'anni fa.',
    14951: 'La strega dall\'occhio finto rosso la conosci? Di anni fra noi '
           'due ce ne passano, ma è una conoscente. Farsi mettere un occhio '
           'finto pagato con le proprie forze, e tutto per stare accanto al '
           'marito amato... Ah, la gioventù.',
    14954: 'A stare così mi torna in mente. Tanto tempo fa veniva spesso a '
           'trovarmi un certo Blood Runner. Diceva che sarebbe andato a '
           'servire al palazzo reale come apprendista cavaliere; poi come sia '
           'finita non lo so... Oh, ma quella era roba della civiltà di prima. '
           'Il tempo corre in fretta.',
    14957: 'Fino a poco fa vivevo in un paese che si chiama Eulderna. Avevo '
           'anche un discepolo, sì: un orfano trovato stremato nel bosco. Per '
           'la ricerca era negato, ma nella magia da combattimento un '
           'fenomeno.',
    14960: 'Quel mio discepolo, però, una volta cresciuto è entrato '
           'nell\'esercito. Ne hanno fatto uno strumento di guerra. A vederlo '
           'travolgere con la magia i soldati degli altri paesi, uno dopo '
           'l\'altro, e fare altri orfani come era stato lui, mi sono '
           'disillusa e ho lasciato il paese. Come sia finito non lo so. Se è '
           'vivo, ormai sarà un rudere come me.',
    14963: 'Io la ricerca non la faccio per delle guerre da nulla, e tanto '
           'meno per aiutare qualcuno. È tutto per inseguire il possibile. '
           'Ihihi... e per quello l\'etica e i divieti che hanno stabilito gli '
           'altri sono solo un intralcio. Non trovi?',
    14966: 'È di quando vivevo in riva al mare, tanto tempo fa. Per una serie '
           'di cose ho aiutato una tartarughina, e così mi sono trovata '
           'davanti la principessa del mare. Diceva che ogni qualche decina di '
           'migliaia di anni torna bambina, e che in questo modo vive da un '
           'tempo sterminato. Se è vero, è tale e quale a una certa medusa. '
           'Chissà se vive ancora in fondo al mare.',
    14969: 'Dopo la fine della civiltà biochimica è stata dura. Il mondo '
           'era pieno di mostri mutati, terra di nessuno. I pochi '
           'esseri normali rimasti non reggevano l\'ambiente contaminato e '
           'morivano uno dopo l\'altro. Ero certa che il mondo fosse finito '
           'lì. E invece, in tanti anni, razze diverse si sono adattate alla '
           'contaminazione, sono diventate creature superiori e hanno perfino '
           'costruito una civiltà nuova... roba da restare a bocca aperta.',
    14972: 'Anche i negromanti che si davano da fare ai tempi della fine '
           'adesso non si vedono più. Eppure un certo numero dovrebbe essere '
           'sopravvissuto. Anzi: i loro non morti da ricognizione venivano '
           'spesso a disturbarmi la ricerca, una bella seccatura.',
    14975: 'Sierre Terre è una civiltà curiosa, dove le tecniche del passato '
           'si sono date appuntamento. Per opera degli dei la magia si è di '
           'nuovo diffusa nel mondo e ha preso un ordine, l\'alchimia si è '
           'sviluppata, e dalle rovine si tirano fuori macchine a mucchi, che '
           'poi ripartono. E poi la tecnica biochimica portata da Rehm-Ido. Un '
           'disegno c\'è, si sente. Ihi... forse è il segno che sta per '
           'succedere qualcosa di grosso.',

    # --- la consegna
    14978: 'To\', mi hai portato delle carte? Che gentilezza, per una vecchia '
           'come me. Allora fammi dare un\'occhiata.',
    14987: 'Ihiii-ihihihi...! Questo è il ringraziamento. Prendilo pure.',
    15052: '"Ihihi... rifammele vedere quando arrivi a " + '
           'gdata(GDATA_FLAG_SUB_THE_LIFE_IN_THIS_WORLD) * 50 + " tipi."',
    15056: '"A proposito, nel mazzo mi pare che tu abbia " + syurui + '
           '" tipi. Ihi... rifammele vedere quando arrivi a " + '
           'gdata(GDATA_FLAG_SUB_THE_LIFE_IN_THIS_WORLD) * 50 + " tipi."',

    # --- il primo incontro
    15061: 'Oh, oh, un visitatore: cosa rara. Di solito la gente mi trova '
           'sinistra e non si avvicina.',
    15062: 'Ihi, su, mettiti pure comodo. Io sono passata non morta, ma i '
           'viandanti non me li mangio. Se mi si assale, magari qualche '
           'resistenza la faccio... ihihi.',
    15063: 'Ecco... Non è che faresti un favore a questa vecchia mezza morta? '
           'Le carte... esistono anche nel mondo di adesso, no? Sì, quelle '
           'con su le informazioni degli esseri viventi, quelle da mettere nel '
           'mazzo. Vedi, a stare tanto a lungo in fondo a un bosco come una '
           'morta, a un certo punto ti prende la curiosità di sapere che cosa '
           'vive oggigiorno.',
    15064: 'Ma no, non le userò per niente di male... Tanto per cominciare, '
           'mettine almeno cinquanta tipi in un mazzo e mostramelo: il '
           'ringraziamento ci sarà. Quando ti va, s\'intende. Ihihi... ho già '
           'una certa età. Il tempo mi corre via che è un piacere.',
}
