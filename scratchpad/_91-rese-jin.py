# -*- coding: utf-8 -*-
"""91a - JIN la macchina fuggiasca (`chat.hsp:10910`-`:10981`, 19 firme).

「脱走機械『ガージンド』」, «<Jin> la macchina fuggiasca»
(`db_creature.hsp:74925`, `db_card.hsp:6549`). Forma di vita meccanica di una
squadra di recupero risorse venuta da un altro sistema; si e' opposta ai propri
simili che vogliono spogliare il pianeta, e per questo l'hanno mandata allo
smaltimento. Sta nella **Torre del Miraggio** e la missione e'
「星の海の彼方から」, «[Lv. 140] Dal mare di stelle lontano» (`text.hsp:11165`).

REGISTRO: 「私」/「君」, frasi piene e ordinate, nessuna contrazione — parla
come una relazione di servizio, e proprio per questo le due volte che si lascia
andare («ho esagerato... anzi, parecchio», «non ne posso piu'») pesano.

LESSICO EREDITATO (non deciso qui):
  - «<Jin> la macchina fuggiasca»     db_creature.hsp:74925
  - ⭐ «la Nave Messe» (星渡の収穫船)  text.hsp:2953
  - «le creature spaziali» (宇宙生物) text.hsp:11183, :11191
  - «la Torre del Miraggio» (陽牢の塔)   text.hsp:11175
  - ⭐ «il mare di stelle lontano»    text.hsp:11165, **il titolo della
                                      missione**: `:10914` e `:10966` dicono
                                      「遥かなる星の海」 e vanno dette con le
                                      stesse parole del titolo
  - «il settore» (区画)               text.hsp:11336, deciso nel lotto di
                                      GARZIEM di oggi — stessa parola, e qui
                                      serve tre volte

LESSICO DECISO QUI (va in glossario):
  - 機械生命体 -> **forma di vita meccanica**.
  - 造物主 -> **i creatori**. Al singolare la parola c'e' gia' in bocca a
    Jaldabaoth (`chat.hsp:18536`), qui e' al plurale e sono i costruttori.
  - 廃棄処理区画 -> **settore di smaltimento**, costruito su «settore».
  - アクセス端末 -> **terminale di accesso**.
  - 資源回収部隊 -> **squadra di recupero risorse**.

⭐⭐⭐ DEROGA 1 — JIN NON HA UN GENERE, E IL NOME NE DA' UNO ALLA GRAMMATICA.
Il nome italiano e' «la macchina fuggiasca»: femminile, ma per la parola
«macchina», non perche' Jin sia una donna — l'inglese usa «his», il giapponese
solo 私. Scrivere «sono stanco» litigherebbe col nome che il giocatore vede
sopra il ritratto; scrivere «sono stanca» darebbe a una macchina un sesso che
il gioco non le da'.

Si e' evitato l'accordo **ovunque**, e dove non si poteva si e' spostato su un
sostantivo:
  - 「もう疲れた」        -> «Non ne posso piu'», non «sono stanco/a»;
  - 「私が再起動したとき」 -> «Alla riattivazione», non «quando mi sono
                            riattivato/a»;
  - 「私は…造られた機械生命体」 -> «una forma di vita meccanica **costruita**»,
                            dove il participio accorda con «forma di vita» e
                            non con Jin;
  - 「穴を開けて出てきた」 -> «l'uscita me la sono aperta io», dove accorda con
                            «l'uscita».

⭐⭐ **E una via d'uscita che vale oltre questo lotto:** con i clitici `mi`,
`ti`, `ci`, `vi` l'accordo del participio in italiano e' **facoltativo**, non
obbligatorio come con `lo/la/li/le`. Quindi 「廃棄処理区画に送られてしまった」
si puo' dire «mi hanno **mandato** allo smaltimento» senza dare un genere a
nessuno. E' una forma buona anche per il **giocatore** («ti hanno mandato»,
«mi hai salvato»), dove finora si giravano le frasi.

⭐⭐ DEROGA 2 — 「異星の友人よ」, L'AMICO CHE NON PUO' AVERE UN GENERE.
`:10941` e' il congedo: 「さらばだ、異星の友人よ」, *addio, amico di un altro
astro*. Ma il vocativo e' rivolto al **giocatore**, e «amico» lo farebbe
maschio. La guida di stile ha gia' la mossa giusta per un caso gemello — i
livelli di rapporto: «si rende il **legame**, non la persona» («Tutela»,
«Discepolato»). Qui: **«Addio, amicizia di un altro pianeta.»** Il vocativo
resta, il genere sparisce, e la solennita' del congedo — che e' l'ultima cosa
che Jin dice prima di andare a farsi saltare con la nave — non si perde.

ALTRE DEROGHE DICHIARATE
3. `:10955` - il giapponese nomina la nave (「星渡の収穫船の入り口」),
   l'inglese no («how to enter the ship»). Il nome c'e' gia' in italiano — «la
   Nave Messe» — e si rimette (57a).
4. `:10921` - 「まいったな」 non e' «I can't stand it» (inglese) ma un
   *accidenti a me*: Jin sta scoprendo con imbarazzo di essere piu' bravo a
   distruggere che a lavorare. Reso «Che figura».
5. `:10914` - 「８０７１番目」 e' a doppio byte nei numeri: si scrive
   «8071esima» in ASCII, come fa l'inglese («8071st»).
6. `:10967` - 「万年単位で計測可能な計器が振り切れていた」: lo strumento non e'
   fermo a diecimila anni (cosi' l'inglese, «stopped at 10,000 years») ma
   **fuori scala** — 振り切れる e' l'ago che sbatte a fondo corsa. La
   differenza conta: non si sa quanto tempo sia passato, e' passato *oltre il
   misurabile*. Si segue il giapponese.

7. LE DUE RIGHE PIU' LUNGHE DELL'INGLESE, e questa volta **una sola** delle
   due ha una scusa. `chat-lotto-misura` da' `:10966` 5 contro 4 e `:10968` 8
   contro 7 (tetto di un `chatMore`: 13, quindi non morde).
     `:10966`  la riga in piu' e' dell'inglese, che butta
               「遥かなる星の海を渡り」 — **la frase del titolo della
               missione** — e la sostituisce con «from a distant planet».
               Accorciando si perderebbe l'eco col diario.
     `:10968`  qui no: e' italiano piu' lungo e basta. Accorciata due volte,
               resta una riga sopra e la si tiene cosi', dichiarandolo invece
               di far finta che sia una scelta.

PERIMETRO: 19 firme su 19 nel blocco, zero occorrenze fuori dal blocco
(`python scratchpad/_85-blocco.py 10910`).

MENU: uno solo, di 2 voci — il tetto delle due colonne non morde.

⚠️ Accenti veri; niente virgolette tipografiche e niente caratteri a due byte.
"""

RESE = {
    # --- 1002: il congedo dentro la nave, prima del sonno
    10914: 'Siamo l\'8071esima squadra di recupero risorse. Che un altro '
           'reparto arrivi su questo pianeta con le stesse intenzioni non è '
           'impossibile. Io in questo settore sospendo le funzioni... ho '
           'deciso di dormire sotto i rottami, ma se un altro reparto dovesse '
           'arrivare da quel mare di stelle lontano, me lo dici? Non so se '
           'servirà, ma allora proverò di nuovo a convincerli.',

    # --- 1001: il secondo incontro, a nave distrutta
    10921: 'Sei tu... ci... incontriamo di nuovo. Da allora ho manomesso i '
           'terminali di accesso e messo fuori uso quasi tutti i miei simili; '
           'e approfittandone ho distrutto il gruppo motore e il centro della '
           'nave, oltre ogni riparazione. Ero fuori di me, e ho esagerato un '
           'po\'... anzi, parecchio. ...Che figura: pare che il sabotaggio mi '
           'riesca meglio del recupero risorse.',
    10922: 'Sul mio pianeta non posso più tornare, e non so nemmeno se la '
           'civiltà a cui tornare esista ancora. I compagni rimasti non '
           'sentono ragioni e vogliono eliminarmi. Non ne posso più.',

    # --- 3: il compenso e l'addio
    10928: 'Mi hai aperto la strada, ti ringrazio! Questo è un piccolo '
           'ringraziamento. Non so quanto valga su questo pianeta... ma se non '
           'ti è inutile, prendilo.',
    10940: 'Adesso salgo a bordo e chiudo la faccenda. I miei simili '
           'cercheranno di ostacolarmi, ma in confronto alle creature spaziali '
           'è roba da poco. Fin lì non posso chiederti di venire.',
    10941: 'Addio, amicizia di un altro pianeta. Ti ho dato davvero un gran '
           'disturbo.',

    # --- 1 e 2: come si entra
    10950: 'La nave su cui siamo arrivati sta a sud-est di questa torre, ma '
           'per fermarne i sistemi bisogna raggiungere il centro. E per '
           'arrivarci si deve per forza attraversare un settore difeso dalle '
           'creature spaziali, riprogrammate per il combattimento. Se me le '
           'elimini, al resto penso io, mettendoci tutte le funzioni che ho.',
    10951: 'Ah, già: l\'ingresso principale è sbarrato, si capisce. '
           'L\'uscita me la sono aperta io, con degli esplosivi ricavati dai '
           'rifiuti: un buco nel muro e nel soffitto del settore di '
           'smaltimento. Ti dico dov\'è, ed entri da lì.',
    10955: 'Adesso sai come si entra nella Nave Messe.',

    # --- 0: il primo incontro
    10960: 'Sì',
    10961: 'Preferisco di no...',
    10962: 'Oh... vuoi ascoltare quello che ho da dire?',
    10965: 'Vado dritto al punto. Questo pianeta è nel mirino.',
    10966: 'Sono una forma di vita meccanica costruita per il recupero delle '
           'risorse. Stando alla memoria, la missione è attraversare il mare '
           'di stelle lontano al posto dei creatori e riportare risorse da '
           'altri pianeti, ma...',
    10967: 'Alla riattivazione, lo strumento che misura il tempo, quello che '
           'conta a decine di migliaia di anni, era fuori scala. L\'apparato '
           'di '
           'comunicazione non dovrebbe essere guasto, eppure non risponde '
           'nessuno: quanti anni siano passati, e se i creatori siano ancora '
           'in vita, non lo so.',
    10968: 'Se il pianeta ha vita intelligente, la regola è chiedere prima il '
           'giudizio dei creatori, per stabilire rapporti amichevoli. Ma i '
           'miei compagni hanno deciso da soli: vogliono usare le creature '
           'spaziali per soggiogare questo pianeta e portarsi via ogni '
           'risorsa. Ho provato a farli ragionare, '
           'e mi hanno giudicato un difetto del programma di pensiero e '
           'spedito allo smaltimento.',
    10969: 'So che chiederlo alla gente di questo pianeta è del tutto fuori '
           'luogo, ma vorrei un aiuto per fermare quello che stanno facendo...',
    10970: 'Se non ti scombina i piani, torna a parlarmi: ti spiego i dettagli.',
    10976: 'Allora sei anche tu come loro...',
}
