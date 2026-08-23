# -*- coding: utf-8 -*-
"""89a - DAIN l'anziano della collina (`chat.hsp:10982`-`:11085`, 38 firme).

Il nonno di Thalia, il capo del villaggio sulla collina: sprezzante, xenofobo,
convinto che il mestiere sia suo e di nessun altro. `CDATA_SEX = 0`
(`db_creature.hsp:74262`): maschio, e il suo parlato in prima persona si
accorda. Il registro sta gia' scritto nel suo repertorio
(`db_creature.hsp:74181`-`:74199`): «Ai giovani d'oggi manca la grinta.», «Non
vali niente: nessun talento.», «Con te non c'e' proprio da discutere.», «Non
l'accetto, non l'accettero' mai.»

LESSICO EREDITATO (non deciso qui):
  - «l'anziano della collina»    db_creature.hsp:74213 e il diario text.hsp:11455
  - «pugnale»                    text.hsp:11455, il diario della missione (88a)
  - «forno fusorio»              db_item.hsp:151275, il nome dell'oggetto
  - «giudizio / giudicare»       chat.hsp:11716 (Irma, 88a)
  - «rozzo», «impugnatura», «lama», «stravagante»   chat.hsp:11733-:11741 (88a)
  - «Hmpf»                       db_creature.hsp:93048
  - «Tsk»                        db_creature.hsp:90846
  - «Thalia», «Irma»             senza parentesi angolari, come nel lotto di Irma

LESSICO DECISO QUI (va in glossario):
  - 武具職人 / «arms craftsman»  ->  **armaiolo / armaiola**. «fabbro» il
    progetto l'ha gia' speso per 職人 (Garok e Miral, i fabbri leggendari,
    `db_creature.hsp:118328`), e il diario chiama il mestiere «forgiare le
    armi»: «armaiolo» e' la parola che nomina esattamente chi fa armi e
    armature. Serve anche al menu di Thalia a `:11187`.
  - 後継者 / «successor»  ->  **erede**, che in italiano non ha genere.
    Il giocatore lo dice di se' a `:11070` (divieto di genere, 75a) e Dain lo
    ripete di lui a `:11079`: «successore» non ha femminile, «erede» si'.

DEROGHE DICHIARATE
1. `:10990` - L'INGLESE SCAMBIA CHI VA RISPARMIATO. Il giapponese dice
   「サリムにはまだ利用価値があるから傷つけずに連れてこい」, cioe' *Thalia*
   serve ancora e va riportata indietro senza farle male; l'inglese fa dire a
   Dain di catturare *Irma* illesa «per fare pressione su Thalia». Non e' una
   sfumatura: a `:10986` Dain ha appena festeggiato che Irma se ne sia andata,
   e a `:11043` giura che non riconoscera' mai niente di suo. Il pronome
   inglese («her») e' ambiguo, il giapponese no, e il resto del blocco da'
   ragione al giapponese. Si segue il giapponese (57a, «l'inglese scambia»).
2. `:11031` - «the dagger(s)». Stessa parentesi di `:11756` (88a): il numero
   cambia col ramo di `GDATA_FLAG_SUB_IRMA_DAGGER` (1-3 e' uno, 4 sono tre) e
   l'italiano non ha quella forma. Si dice «il lavoro», che e' la parola con
   cui la 88a ha gia' reso `:11756`, e che vale per uno e per tre.
3. `:11028` - «The craftsman should be proud of THEIR practical pieces». Li'
   Dain non sa ancora di chi sia il pugnale (lo scopre a `:11030`), quindi
   l'italiano non puo' dargli un genere: si usa il relativo `chi`, che accorda
   al maschile singolare invariabile senza nominare nessuno (86a).
4. `:10999` - «as an adventurer that takes on requests for money». Il
   giapponese non dice 冒険者: dice 「金を貰って仕事を引き受ける以上」. Il
   bersaglio e' il giocatore, quindi niente «avventuriero» (84a) e niente
   accordo: «Chi si fa pagare per un incarico...».
5. `:11066` - «Welcome, traveler». Vocativo al giocatore (77a): «viandante» da
   solo non porta genere, ma «sei arrivato» si'. Girato in impersonale.
6. `:11045` e `:11046` - l'inglese NON traduce il giapponese
   (「言い方ってものがある」 = *c'e' un modo di dire le cose*, 「滅相もない」 =
   *ma no, si figuri*). Si traduce dall'inglese, che regge: `:11052` risponde
   «ho detto quello che pensavo» e chiude tutt'e due le letture.
7. `:11066` e `:11071` - l'inglese perde 丘の民 («gli oggetti fatti dalla gente
   della collina»). Non si rimette: il giocatore non ci fa niente, e il
   criterio non e' rendere il testo piu' ricco.

ECO (84a): `:11019`, `:11022`, `:11025` e `:11028` sono la valutazione dei tre
pugnali che Irma presenta a `:11733`, `:11737`, `:11741`, `:11745`, gia' resi
nella 88a. Le parole sono le stesse per costruzione — «Il disegno e' rozzo»,
«l'impugnatura», «la lama», «stravagante» — perche' il giocatore legge le due
scene a pochi minuti di distanza e la seconda deve riconoscere la prima.

FIRMA CONDIVISA: `:11069` (「残念だ」 / «That's too bad.») vive anche a
`:12526`, nel menu di Urcaguary. E' una VOCE DI MENU, quindi il contraccolpo e'
certo (85a) ed e' il motivo per cui il lotto di Urcaguary entra nella stessa
giornata. «Che peccato» regge in tutt'e due i siti: qui il villaggio non ha
piu' una bottega d'armi, la' i Cavalieri Dorati non accettano nuovi membri.
"""

RESE = {

    # --- missione finita (flag >= 8): Dain assolda il giocatore contro Irma
    10985: '"(" + cdatan(CDATAN_NAME, tc) + " sogghigna e ride...)"',
    10986: 'Finalmente quella ragazzina se n\'è andata. Rinunciare al proprio '
           '\\"sogno\\" dopo così poco: che miseria! Alla fine tanto valeva. '
           'Del resto l\'avevo capito subito, e ho fatto in modo che venisse '
           'fuori presto la sua vera natura. Che spreco. Dovrebbe '
           'restituirmelo, il tempo che mi ha portato via.',
    10987: 'Ci penso su',
    10988: 'Dammi un anticipo',
    10989: 'A finire a pezzi sarai tu',
    10990: 'Il guaio è che se n\'è andata anche Thalia, mia nipote. Di sicuro è '
           'stata quella ragazzina a girarle la testa e a portarsela via: scova '
           'il loro rifugio e mettilo a soqquadro. Ma sì, con lei fa\' quello '
           'che ti pare, è una rapitrice, la colpa è tutta sua. Ah: Thalia mi '
           'serve ancora, quindi riportamela senza torcerle un capello. Intesi?',
    10993: 'Ah. E io darei un anticipo a gente di fuori di cui non mi fido? '
           'Prova un po\' a ricordarti che posto occupi, qui.',
    10999: 'Chi si fa pagare per un incarico deve tenersi caro il proprio buon '
           'nome. E tu ti permetti di parlare così a un committente? Non hai '
           'nessun titolo per farti dare incarichi dalla gente.',
    11002: 'Scuse così non me le compro. Fammela vedere sul serio, la buona '
           'fede: fa\' quello che ti ho chiesto.',
    11005: 'Hmpf. Vedo che non hai niente da ribattere.',

    # --- dopo la valutazione (5 <= flag < 8)
    11012: 'Che c\'è? Hai altre armi da farmi \\"giudicare\\"? Mi rifiuto. Non '
           'ho nessuna voglia di prendermi altri dispiaceri!',

    # --- la scena della valutazione (flag == 4)
    11016: 'Ehi, aspetta un momento. Quel pugnale che hai con te... fammelo '
           'vedere bene.',
    11019: 'Oh, questo è fatto bene. L\'impugnatura tiene la mano ferma quando '
           'si colpisce, e pesa poco. Il disegno è rozzo, ma la lama è robusta: '
           'un pugnale fatto per l\'uso pratico.',
    11022: 'Questo è bello... Come arma non serve, ma questa fattura passerebbe '
           'per opera d\'arte. Le decorazioni sulla lama, e poi come brilla...',
    11025: 'Nuovo! A prima vista la forma sembra stravagante, ma è la lama a '
           'rendere il taglio molto più netto. Una linea inedita, evolutasi '
           'per conto suo...',
    11028: 'Che una persona sola abbia fatto pugnali così diversi fra loro è '
           'notevole. Se proprio devo sceglierne uno, dico che quello rozzo è '
           'il più riuscito. Forse chi l\'ha fatto dà il meglio nei pezzi '
           'pratici. Ma anche gli altri due sono fatti bene...',
    11030: 'Ma guarda...? Qui c\'è inciso in piccolo il nome di chi l\'ha '
           'fatto... Irma?',
    11031: '(Dain scaraventa il lavoro nel forno fusorio.)',
    11034: 'Di pugnali robusti che stanno bene in mano ne è pieno il mondo. Ha '
           'buttato via tutto il lato decorativo e non ha avuto nemmeno '
           'un\'idea nuova. Non c\'è altra parola: banale.',
    11037: 'Un pezzo che si aggiusta solo l\'apparenza, dentro non c\'è niente. '
           'Se le cose che vuol fare sono queste, tanto varrebbe lasciasse '
           'l\'armaiola e si mettesse a scolpire. Anche se, con decorazioni di '
           'questo livello, da scultrice non camperebbe lo stesso.',
    11040: 'Un aborto che serve solo a far vedere quanto è stravagante. Crede '
           'davvero di conoscere la forma giusta di un pugnale meglio di chi li '
           'fa da millenni? Che presunzione.',
    11043: 'Chi fa questo mestiere deve puntare su una cifra sola. Blandire il '
           'giudice mettendo le mani in altri stili è cosa da non farsi. Del '
           'resto, qualunque cosa tiri fuori quella ragazzina, io non '
           'l\'accetterò mai.',
    11045: 'Hai detto tutto il contrario',
    11046: 'Non sei ragionevole',
    11047: 'Ridammi il pugnale',
    11048: 'Che c\'è? Non avrai da ridire?',
    11052: 'Hmpf. Ho detto quello che pensavo, niente di più. I criteri e il '
           'metro li stabilisco io, che sono il giudice. Che altro c\'è da '
           'dire?',
    11055: 'E va bene, portatelo a casa. Se infili un braccio nel forno fusorio '
           'magari qualche resto lo trovi ancora. O forse, con quella qualità '
           'lì, si è già sciolto tutto? Uahahah.',
    11057: 'Tsk, a furia di parlare mi sono stancato. Che spreco di tempo. '
           'Sbrigati ad andartene.',

    # --- il primo incontro (flag < 4)
    11064: 'Comprare armi e armature',
    11065: 'Facciamo così',
    11066: 'Un viandante, eh? Non è da tutti arrivare fin quaggiù. Di botteghe '
           'ne abbiamo poche, ma quel che tengono è roba di prima qualità.',
    11069: 'Che peccato',
    11070: 'Voglio essere l\'erede',
    11071: 'Che peccato, davvero: in questo villaggio una bottega d\'armi non '
           'c\'è più. Da un pezzo hanno chiuso, per mancanza di eredi. Qualcuno '
           'che fa mobili e capanne è rimasto, ma di armaioli non ce n\'è più '
           'nessuno.',
    11074: 'Già. Mia nipote la stoffa per raccogliere la tecnica ce l\'avrebbe, '
           'ma non pare le interessi...',
    11078: 'Come...?',
    11079: 'Ehi, non prendere in giro la nostra antica tecnica!! Gente di fuori '
           'come erede? Prima tu, poi quella ragazzina dai capelli rossi... Ci '
           'stai scherzando? Eh? Basta. Fuori di qui. Subito.',
}
