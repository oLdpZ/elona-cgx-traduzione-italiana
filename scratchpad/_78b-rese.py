# -*- coding: utf-8 -*-
# Lotto 78b: il sistema delle GILDE in chat.hsp.
# Tre maestri (Revlus/Fray/Sin), tre guardiani (Lexus/Abyss/Doria), tre
# investigatori di Tyris del Sud (Lenas/Naga/Ratin), piu' il menu di Miches
# che condivide la firma di «Let's Talk.».
# Glossario fissato altrove: Gilda dei Maghi/Guerrieri/Ladri (command.hsp),
# il maestro della gilda, il guardiano, punti gilda, obiettivo (= norma),
# grimorio, refurtiva, Nefia casuali, Tyris del Nord/Sud.
RESE = {
 # --- Miches, il bambino del gioco di carte -------------------------------
 1466: "Salutare",                       # firma condivisa coi tre maestri di gilda
 1467: "Accettare",
 1468: "Non ne ho voglia",
 1469: "Senti, tu che vai all'avventura! Ho appena comprato un mazzo di putit e yeek! Giochi con me? Ti prego!",

 # --- il menu comune dei tre maestri --------------------------------------
 4867: "<Addestramento del mese>",
 4869: '"Investire 50 (" + calcinvestvalueg() + strgold + ")"',
 4871: "Voglio lasciare la gilda...",
 4875: "Ci ripenso",
 4876: "<È deciso>",
 4905: '"Prossimo addestramento collettivo: dopo " + cnvdate(cdata(CDATA_ROLE_SHOP_LEVEL, tc), 1) + "."',
 4908: "Oh, siamo già a quel punto del mese? Cominciamo subito l'addestramento collettivo. Il potenziale si rimetterà in sesto secondo il rango della gilda.",

 # --- Revlus, maestro della Gilda dei Maghi (cortese) ---------------------
 4877: "...È successo qualcosa? Va bene, non chiedo i dettagli. Ma vuoi davvero buttare via tutta la fatica fatta finora? Ti prego, ripensaci.",
 4880: "Bene così. Agire d'impulso non porta mai niente di buono.",
 4884: "...Vedo che la tua volontà è ferma. Va bene: accolgo la tua richiesta di uscita.",
 4889: "Hai lasciato la Gilda dei Maghi...",
 4969: "Fra i nuovi arrivati, giusto? Buon lavoro.",
 4973: "Pare che ultimamente ti stia dando da fare. Conto molto sui tuoi progressi.",
 4977: "Un tempo le altre due gilde ci schiacciavano... ma da quando ci sei tu questa gilda ha ripreso vigore. ...Ti ringrazio.",
 4981: "Piegheremo la subdola Gilda dei Ladri e la barbara Gilda dei Guerrieri, e la nostra Gilda dei Maghi mostrerà al mondo la sua forza! Voglio che tu abbatta il maestro di una delle due. Dell'altro mi occupo io.",
 4987: "E adesso, quale gilda attacco io?",
 4991: "Meraviglioso! Sapevo che ce l'avresti fatta! Ecco una ricompensa speciale da parte mia. Accettala.",
 5006: '"Non c\'è nessun altro degno di fare il maestro della gilda. Non lo penso solo io: lo pensano tutti. " + cdatan(CDATAN_NAME, CHARA_PLAYER) + "... da oggi in poi ci affidiamo a te."',
 5013: "Qui non puoi stare: non sei dei nostri. Vattene, per favore.",

 # --- Fray, maestro della Gilda dei Guerrieri (donna, registro fermo) -----
 5033: "...Cosa!? È perché come maestro della gilda sono troppo debole? Uh... non importa. Non trattengo chi se ne va. Ma se cambi idea, torna pure: ricomincerai dal gradino più basso.",
 5036: "Tutti questi combattimenti stancano. Riposati un po'.",
 5040: "...Addio! Onore a chi combatte con noi. Grazie di tutto!",
 5045: "Hai lasciato la Gilda dei Guerrieri...",
 5125: "Una recluta nuova. Qui si va avanti con la disciplina.",
 5129: "Ultimamente ti stai facendo notare. Mi aspetto molto da te.",
 5133: "Anche gli altri si allenano per non restare indietro. È un'ottima cosa. Sono davvero contenta che tu abbia scelto la nostra gilda...",
 5137: "È venuto il momento di mostrare la forza di noi guerrieri! Abbatteremo i maestri di tutt'e due quelle gilde da vigliacchi! Tu occupati del più debole dei due, dell'altro mi occupo io.",
 5143: "Mm, avere un avversario vero mi fa ribollire il sangue!",
 5147: "Hai vinto! Sapevo che ce l'avresti fatta! Questa è una ricompensa speciale da parte mia. Accettala.",
 5162: '"Il prossimo maestro della gilda non può essere altri che te. Non lo penso solo io: lo pensano tutti. " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", continuiamo a lavorare insieme."',
 5169: "Vattene, prima che qualcuno se ne accorga.",

 # --- Sin, maestro della Gilda dei Ladri (sbrigativo) ---------------------
 5189: "...Vuoi chiudere con la gilda. E va bene, di te mi scordo. Tu scordati quello che hai visto qui. D'ora in poi vivi la tua vita e lascia stare il mondo di sotto.",
 5192: "Per poco non ci cascavo.",
 5196: "...Riguardati.",
 5201: "Hai lasciato la Gilda dei Ladri...",
 5281: "Sei una faccia nuova. Non fare casini.",
 5285: "Come lavori mi piace. Ma non ti mettere a dormire.",
 5289: "Con la fama che hai potevi andare in un'altra gilda qualunque. Scegliere la nostra è roba da tipi strani... Non che mi lamenti, eh.",
 5293: '"È arrivato un lavoro coi fiocchi. Facciamo fuori i maestri della Gilda dei Maghi e della Gilda dei Guerrieri. Roba grossa... " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", di uno dei due te ne occupi tu, dell\'altro io. Non fare casini."',
 5299: "Uno degli altri maestri lo stendi di sicuro. Heh, chi l'avrebbe detto che mi sarei fidato così di qualcuno. Sto rammollendo.",
 5303: "Ce ne hai messo, di tempo... Non che fossi in pensiero, eh. Questa è la tua parte. Tienila.",
 5318: '"Il prossimo maestro della gilda potresti essere tu, e per me va bene. " + cdatan(CDATAN_NAME, CHARA_PLAYER) + "... non tradirci."',
 5325: "Fuori di qui. Non hai niente da fare qui dentro.",

 # --- Lexus, guardiano della Gilda dei Maghi ------------------------------
 5331: "Che cos'è la Gilda dei Maghi?",
 5332: "Voglio entrare nella Gilda dei Maghi",
 5334: "Alt... oltre queste scale c'è la sede della Gilda dei Maghi. Chi non è della gilda non può entrare.",
 5337: "La Gilda dei Maghi riunisce esperti provati e riconosciuti nella loro arte. Offriamo diversi servizi: sconti sui grimori, prenotazione dei grimori, addestramento delle abilità collegate. Ma per entrare bisogna superare una prova difficile, che la maggior parte dei maghi non supera.",
 5342: "Vuoi entrare nella nostra gilda... Noi prendiamo solo maghi di prim'ordine. Vediamo se sei all'altezza dei nostri.",
 5343: "A Tyris del Nord sono sparsi libri antichi scritti in una lingua runica particolare. Se vuoi entrare nella gilda, decifrali e mettili nel baule delle consegne: in cambio avrai punti gilda.",
 5347: "Per entrare nella Gilda dei Maghi devi accumulare 15 punti gilda. Fino ad allora non abbiamo altro di cui parlare.",
 5351: "Per superare la prova devi accumulare 15 punti gilda.",
 5354: "Bene... a quanto pare hai portato a termine l'obiettivo.",
 5356: "Ma prima devi uscire ufficialmente dalla gilda in cui sei. Chi se ne va senza rispettare le procedure non dà garanzie a un'organizzazione. Ti pare ovvio, no?",
 5358: "Va detto al maestro della tua gilda che te ne vai.",
 5378: "Adesso fai parte della Gilda dei Maghi!",
 5379: "Congratulazioni... prova superata. Da oggi fai parte della Gilda dei Maghi. Puoi usare queste scale per entrare nella sede. Da qui in avanti rispetta le regole della gilda e porta a termine gli obiettivi.",
 5390: "Chiedere un obiettivo",
 5393: "Riferire sull'obiettivo",
 5396: '"Ti diamo il benvenuto nella Gilda dei Maghi, " + ranktitle(8) + " " + cdatan(CDATAN_NAME, CHARA_PLAYER) + "... Vieni all\'addestramento collettivo di ogni mese, quando puoi. Il maestro ha molto da fare e se ne dimentica: se lo incontri, ricordaglielo."',
 5402: '"Bene. Di lavoro ce n\'è in abbondanza. Per adesso raccogli i libri antichi e decifrali. Quando avrai messo insieme " + gdata(GDATA_FLAG_GUILD_MAGE_NORMA) + " punti gilda, penseremo alla tua promozione."',
 5407: "Che c'è? Hai ancora un obiettivo da portare a termine.",
 5423: "Obiettivo raggiunto, confermo. Convoco subito il consiglio e riferisco i tuoi meriti.",

 # --- Abyss, guardiano della Gilda dei Ladri ------------------------------
 5431: "Che cos'è la Gilda dei Ladri?",
 5432: "Voglio entrare nella Gilda dei Ladri",
 5434: "Alt... oltre queste scale c'è la sede della Gilda dei Ladri. Chi non è della gilda non può entrare.",
 5437: "La Gilda dei Ladri riunisce esperti provati e riconosciuti nelle arti dell'ombra. Offriamo diversi servizi: acquisto della refurtiva, sconti al mercato nero, addestramento delle abilità collegate. Ma per entrare bisogna superare una prova difficile, che la maggior parte dei ladri non supera.",
 5442: "Ti interessa la nostra gilda? Noi ci nascondiamo nell'ombra della società. Per entrare devi guadagnarti la nostra fiducia.",
 5445: "È una prova semplice. Devi portare il tuo karma a -100. Sappi che dal -31 in giù le guardie ti daranno la caccia. Se non te la senti, lascia perdere.",
 5449: "Te l'ho già detto, quello che devi fare. Porta il karma a -100.",
 5476: "Adesso fai parte della Gilda dei Ladri!",
 5477: "Congratulazioni... prova superata. Da oggi fai parte della Gilda dei Ladri. Puoi usare queste scale per entrare nella sede. Da qui in avanti rispetta le regole della gilda e porta a termine gli obiettivi.",
 5494: '"Ti diamo il benvenuto nella Gilda dei Ladri, " + ranktitle(8) + " " + cdatan(CDATAN_NAME, CHARA_PLAYER) + "... Vieni all\'addestramento collettivo di ogni mese, quando puoi. Il maestro ha molto da fare e se ne dimentica: se lo incontri, ricordaglielo."',
 5500: '"Bene. La Gilda dei Ladri vuole che tu rimetta in circolo la refurtiva. Ruba della roba e rivendila a un mercante qualunque. Quando il ricavato arriverà a " + gdata(GDATA_FLAG_GUILD_THIEF_NORMA) + " monete d\'oro, penseremo alla tua promozione."',

 # --- Doria, guardiano della Gilda dei Guerrieri --------------------------
 5529: "Che cos'è la Gilda dei Guerrieri?",
 5530: "Voglio entrare nella Gilda dei Guerrieri",
 5532: "Alt... oltre queste scale c'è la sede della Gilda dei Guerrieri. Chi non è della gilda non può entrare.",
 5535: "La Gilda dei Guerrieri riunisce esperti provati e riconosciuti nell'arte del combattimento. Offriamo diversi servizi: sconti su identificazione e ripristino, addestramento delle abilità collegate. Ma per entrare bisogna superare una prova difficile, che la maggior parte dei guerrieri non supera.",
 5540: "Per entrare nella Gilda dei Guerrieri devi prima superare una prova e guadagnarti la nostra fiducia. Ci servono cacciatori esperti, che rispettino le regole e non indietreggino in una battaglia disperata.",
 5546: '"L\'incarico è questo. Trova e conquista " + gdata(GDATA_FLAG_GUILD_FIGHTER_NORMA) + " Nefia casuali di tipo " + _nefiatype(gdata(GDATA_FLAG_FIGHTER_GUILD_NEFIA_TYPE)) + " di livello " + gdata(GDATA_FLAG_FIGHTER_GUILD_NEFIA_MIN_LEVEL) + " o più. Quando hai finito torna a parlarmi."',
 5550: '"Ti mancano ancora " + gdata(GDATA_FLAG_GUILD_FIGHTER_NORMA) + " Nefia casuali di tipo " + _nefiatype(gdata(GDATA_FLAG_FIGHTER_GUILD_NEFIA_TYPE)) + " di livello " + gdata(GDATA_FLAG_FIGHTER_GUILD_NEFIA_MIN_LEVEL) + " o più da conquistare."',
 5577: "Adesso fai parte della Gilda dei Guerrieri!",
 5578: "Congratulazioni... prova superata. Da oggi fai parte della Gilda dei Guerrieri. Puoi usare queste scale per entrare nella sede. Da qui in avanti rispetta le regole della gilda e porta a termine gli obiettivi.",
 5595: '"Ti diamo il benvenuto nella Gilda dei Guerrieri, " + ranktitle(8) + " " + cdatan(CDATAN_NAME, CHARA_PLAYER) + "... Vieni all\'addestramento collettivo di ogni mese, quando puoi. Il maestro ha molto da fare e se ne dimentica: se la incontri, ricordaglielo."',
 5603: '"C\'è un incarico per te. Trova e conquista " + gdata(GDATA_FLAG_GUILD_FIGHTER_NORMA) + " Nefia casuali di tipo " + _nefiatype(gdata(GDATA_FLAG_FIGHTER_GUILD_NEFIA_TYPE)) + " di livello " + gdata(GDATA_FLAG_FIGHTER_GUILD_NEFIA_MIN_LEVEL) + " o più. Poi penseremo alla tua promozione."',

 # --- i tre investigatori di Tyris del Sud --------------------------------
 9247: "Sono l'investigatrice della Gilda dei Maghi. Seguo i progressi dei nostri membri qui a Tyris del Sud.",
 9274: "Obiettivo raggiunto, confermo. Riferisco subito i tuoi meriti al consiglio.",
 9290: "Sono l'investigatrice della Gilda dei Ladri... Seguo i progressi dei nostri membri qui a Tyris del Sud...",
 9296: '"Bene. La Gilda dei Ladri vuole che tu rimetta in circolo la refurtiva. Ruba della roba e rivendila a un mercante qualunque. Quando il ricavato arriverà a " + gdata(GDATA_FLAG_GUILD_THIEF_NORMA) + " monete d\'oro, penseremo alla tua promozione."',
 9301: "Che c'è? Hai ancora un obiettivo da portare a termine.",
 9317: "Obiettivo raggiunto, confermo. Riferisco subito i tuoi meriti al consiglio.",
 9333: "Sono l'investigatore della Gilda dei Guerrieri. Seguo i progressi dei nostri membri qui a Tyris del Sud.",
 9341: '"C\'è un incarico per te. Trova e conquista " + gdata(GDATA_FLAG_GUILD_FIGHTER_NORMA) + " Nefia casuali di tipo " + _nefiatype(gdata(GDATA_FLAG_FIGHTER_GUILD_NEFIA_TYPE)) + " di livello " + gdata(GDATA_FLAG_FIGHTER_GUILD_NEFIA_MIN_LEVEL) + " o più. Poi valuteremo la tua promozione."',
 9346: "Che c'è? Hai ancora un obiettivo da portare a termine.",
}
