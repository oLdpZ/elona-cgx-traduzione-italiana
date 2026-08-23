# -*- coding: utf-8 -*-
"""90a - MARKA l'orsa d'argento (`chat.hsp:11771`-`:11892`, 32 firme).

「メイルーンの銀熊『マルカ』」, «<Marka> l'orsa d'argento di Mayroon»
(`db_creature.hsp:73827`). Avventuriera di Mayroon, il paese dove nevica tutto
l'anno: grossa, fortissima, sbrigativa, e **permalosa su una parola sola**.

⭐⭐ IL REGISTRO E IL SUO TASTO DOLENTE ERANO GIA' SCRITTI. Il repertorio
(`db_creature.hsp:73795`-`:73813`) porta «Orsa a chi!» (「誰が熊だっ！」),
«Scusa tanto se ho la forza di un toro...», «Io a casa ci torno viva!» — cioe'
il tic, la voce e perfino la trama. Qui 熊呼ばわり torna **due volte**
(`:11775`, `:11795`) ed e' la stessa parola: «dare dell'orsa». Non si e'
deciso niente, si e' riletto.

LESSICO EREDITATO (non deciso qui):
  - «l'orsa d'argento», «Marka»   db_creature.hsp:73827, e chat.hsp:2125 la
                                  nomina in coppia con Noyel e Mayroon
  - «Mayroon», «Noyel»            chat.hsp:2125 e :2212
  - «Rocca Ghiacciata»            map.hsp:3181, 氷の城
  - «Nefia»                       chat.hsp:2307 e altri 49 siti
  - «il dio del caos»             chat.hsp:2083 e la Culla del Caos
  - «Melugast»                    action.hsp:17242, chat.hsp:7913
  - «campi di neve»               chat.hsp:12728 — la stessa distesa della
                                  missione di Irma (88a)
  - «(Allontanarsi)», «Non voglio andarci», «Va bene»   ⭐ **tutte e tre le
                                  voci del menu di `:11829` erano gia' rese**, e
                                  la terza (「わかった」) non da un'altra riga di
                                  Marka ma da `chat.hsp:1712`, dall'altra parte
                                  del file: la firma e' la coppia (jp, en), e il
                                  lotto se le e' tolte da solo. Percio' il
                                  perimetro qui e' 32 su 35.

LESSICO DECISO QUI (va in glossario):
  - 犬ぞり -> **slitta trainata dai cani**; クレバス -> **crepaccio**;
    カマクラ -> **capanne di neve**. Tre parole di neve che il progetto non
    aveva perche' Mayroon non era ancora stata scritta.
  - 雑魚 -> **pesci piccoli**, che sta accanto al «pesciolino» gia' usato per
    la stessa idea (`db_creature.hsp:71000`).

DEROGHE DICHIARATE
1. `:11886` - 「冒険者」 e' **lei**, e in italiano prende il genere che il suo
   nome dichiara: «l'avventuriera». L'inglese puo' permettersi «the
   adventurer» perche' non accorda; l'italiano deve scegliere, e la scelta e'
   gia' fatta in `db_creature.hsp:73827`.
2. `:11810`, `:11827`, `:11838`, `:11872` - QUATTRO RIGHE CHE PARLANO AL
   GIOCATORE E CHIEDEREBBERO UN PARTICIPIO. «stai tremando tutto», «tranquillo»,
   «impalato», «non ti sei fatto male» accorderebbero al maschile chi non ha
   genere (75a). Girate: «stai tremando come una foglia», «niente paura», «che
   fai li' a bocca aperta», «tutto a posto? Niente di rotto?».
3. `:11811` - 「最奥に陣取ってる悪魔の首」. 首 e' il **capo**, non la testa
   mozzata: l'inglese sfuma in «the demon that's in the castle» e perde sia il
   grado sia il fatto che sia acquartierato in fondo. Si segue il giapponese —
   e serve, perche' la riga dopo distingue lui dai «pesci piccoli».
4. `:11821` - 「君どこかで会ったっけ？」 non diventa «ci siamo gia' visti», che
   accorda anche il giocatore: «ma noi ci conosciamo?».
5. `:11882` - 「メルガストのことを教える」 e' scritto come un'azione mentre le
   altre due voci della fila sono parlato («Ti stavo cercando», «Ascoltami»).
   L'inglese uniforma la fila e ha ragione: una fila di menu si accorda al suo
   interno (49a). «Ti parlo del Melugast».

PERIMETRO: 32 firme da fare su 35 nel blocco (due voci di menu e una terza
erano gia' rese), zero occorrenze fuori dal blocco e zero in altri file.
Nessun contraccolpo.

MENU: tre file da tre voci — **sotto** la soglia delle dieci: il tetto delle
due colonne non morde, vale quello dei 58 caratteri di `*chat_select`.

⚠️ Gli accenti si scrivono VERI, e «dèi» e i suoi simili no: la degradazione
CP932 metterebbe l'apostrofo dentro la parola (lezione del lotto di MELGET).
"""

RESE = {

    # --- la Culla del Caos
    11775: 'Solo perché sono un po\' grossa, forte e pelosa mi danno tutti '
           'dell\'orsa. Siete cattivi. Ci resto male, sai...',
    11781: 'In fondo a questa Nefia dorme qualcosa di simile al dio del caos, '
           'ed è quello la causa degli sconvolgimenti!',
    11782: '...Così dice il mio fiuto da avventuriera, ed è per quello che sono '
           'qui. Pare che anche parecchi altri avventurieri stiano scendendo '
           'verso il fondo. Mah. Fiuto ne hanno tutti, eh.',

    # --- dopo Mayroon
    11789: 'Anche qui nevica tutto l\'anno, ma in confronto a Mayroon fa un '
           'caldo che non ti dico. Con questa roba qui posso correre in giro '
           'nuda senza problemi.',
    11795: 'Grazie dell\'aiuto, mi hai salvata. Il resto della pulizia lo faccio '
           'da sola... anzi, lasciamelo fare. Devo far vedere quanto valgo a '
           'quelli che mi prendevano in giro dandomi dell\'orsa. ...Scherzo, eh.',
    11796: 'Per un lavorone così lo Stato un compenso lo darebbe. Vabbè, '
           'l\'abbiamo fatto di testa nostra.',

    # --- dentro la Rocca Ghiacciata
    11802: 'Non lo sa quasi nessuno, ma questo posto è un\'attrazione '
           'turistica: come castello non lo usa più nessuno. Tanti turisti '
           'restano di sasso a sentirlo... ma che gli prende? Credono che a '
           'Mayroon si viva in case di ghiaccio e capanne di neve?',
    11803: 'Be\'... nemmeno io posso fare la maestra: finché non sono uscita da '
           'Mayroon, degli altri paesi mi ero fatta idee tutte mie.',
    11810: 'Uff, correvano a una velocità tale in mezzo alla bufera che credevo '
           'di volare giù. ...Senti, stai tremando come una foglia: tutto bene?',
    11811: 'Comunque: questa è la Rocca Ghiacciata di Mayroon. La volta scorsa i '
           'paesi li avevo liberati, ma il castello era difeso troppo bene. '
           'Stavolta puntiamo al capo dei demoni, acquartierato in fondo. Fatto '
           'fuori lui, i pesci piccoli me li tolgo di mezzo da sola.',
    11812: '...Però che disastro: è ridotta peggio di quando ci sono venuta '
           'l\'ultima volta. Buchi enormi nel pavimento e nel tetto... ci '
           'arriveremo, in fondo?',

    # --- la partenza per Mayroon
    11821: 'Eh? Ma noi ci conosciamo? Vabbè. Tu hai l\'aria di essere forte: '
           'vorrei che venissi con me.',
    11824: 'Sono tornata di corsa al mio paese per abbattere il mostro, ma i '
           'nemici erano molti più del previsto e a un passo dalla fine ho '
           'dovuto ritirarmi. Che rabbia, davvero: e pensare che i campi di '
           'neve e il ghiacciaio me li ero fatti a piedi.',
    11827: 'Ma no, niente paura. Non so chi ce l\'abbia messa, ma poco fa ho '
           'trovato una slitta trainata dai cani: usiamo quella. Non c\'è '
           'bisogno di andarci a piedi. Sono cani enormi, in un crepaccio non ci '
           'cascano di sicuro.',
    11832: 'Non possiamo prepararci all\'infinito. Su, partiamo?',
    11838: 'Che fai lì a bocca aperta? Su, si va.',
    11859: 'Ehi! Ascoltami quando ti parlo!',

    # --- il primo incontro, nella Nefia
    11868: 'Uaah?!',
    11869: 'Sto bene',
    11870: 'Mi si è rotto un osso',
    11871: 'Sei tu l\'orsa d\'argento?',
    11872: 'S-scusa. Tutto a posto? Niente di rotto?',
    11874: 'Ma lascia stare quello: c\'è un guaio grosso! Al piano di sotto ho '
           'visto tre tizi strani. Mi sono insospettita e li ho spiati da dietro '
           'un riparo. E a un certo punto uno dei tre... come dire, ha storto lo '
           'spazio e l\'ha attaccato a un altro spazio... Comunque sia, io non '
           'posso essermi sbagliata: là dall\'altra parte c\'era il paesaggio '
           'del mio paese, di sicuro.',
    11875: 'Che cose terribili?',
    11876: 'Non m\'importa',
    11877: 'Questo lo so già',
    11878: 'E quelli, dopo aver spedito un mostro enorme nel mio paese, sono '
           'scesi giù parlando di cose terribili...',
    11880: 'Ti stavo cercando',
    11881: 'Ascoltami',
    11882: 'Ti parlo del Melugast',
    11883: 'Be\', io sono in pensiero per il mio paese, quindi vado. In '
           'superficie ci torno a ogni costo!',
    11886: 'Senza starti ad ascoltare, l\'avventuriera è corsa su per le '
           'scale...',
}
