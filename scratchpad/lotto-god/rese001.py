import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :9 e :35 la pieta' che sale, e il tetto che la ferma.
    # ⚠️ Lo spazio davanti c'e' anche nell'inglese: la riga segue una battuta
    #    del dio (txtgod) sulla stessa riga di registro.
    (9, ' Now prayer to God may bring something special!'):
        ' Ora una preghiera al tuo dio potrebbe portare qualcosa di speciale!',
    # ⚠️ L'inglese parla del dono, il giapponese della fede — e la condizione
    #    (`faith * 100 < piety`, :33) da' ragione al giapponese.
    (35, 'Your god becomes indifferent to your gift.'):
        'La tua fede è già salita al limite.',

    # --- :81-:89 i nove nomi. Tetto 20 caratteri: fixtxt taglia a 32 e
    #     l'etichetta «Fede      : » ne occupa 12 (command.hsp:17662).
    (81, 'Eyth of Infidel'): 'Eyth del Nulla',
    (82, 'Mani of Machine'): 'Mani della Macchina',
    (83, 'Lulwy of Wind'): 'Lulwy del Vento',
    (84, 'Itzpalt of Element'): 'Itzpalt Elementale',
    (85, 'Ehekatl of Luck'): 'Ehekatl della Sorte',
    (86, 'Opatos of Earth'): 'Opatos della Terra',
    (87, 'Jure of Healing'): 'Jure della Cura',
    (88, 'Kumiromi of Harvest'): 'Kumiromi della Messe',
    (89, 'Yacatect of Wealth'): 'Yacatect del Tesoro',

    # --- :270 la scheda del senza-dio. Il giapponese porta il numero.
    (270, 'Atheism (Passive: Increase all damage you<br>give to gods.)<p>'):
        'Miscredenza (automatico: +40% a ogni danno inflitto a un dio)<p>',

    # --- :273-:276 Mani. Due righe di descrizione invece di tre: il «Bonus»
    #     italiano ne vuole due, e il pannello regge otto righe in tutto.
    (273, 'Mani is a clockwork god of machinery. Those faithful to Mani<br>'
          'receive immense knowledge of machines and learn a way to use them<br>'
          'effectively.<p>'):
        "Mani è il dio meccanico delle macchine. Chi lo venera riceve una<br>"
        "conoscenza immensa dei congegni e, coi sensi affinati, colpisce con "
        "precisione.<p>",
    (274, 'Offering: Corpses/Guns/Machinery<p>'):
        'Offerte: cadaveri/armi da fuoco/macchinari<p>',
    # ⚠️ 銃 e 大工 sono nomi vecchi: l'elenco delle abilita' dice 銃器 e 工作,
    #    cioe' «Arma da fuoco» e «Falegnameria». La resa usa quelli.
    (275, 'Bonus   : DEX/PER/Firearms/Healing/Detection/Jeweler/Lockpick/Carpentry<p>'):
        'Bonus  : DES/PER/Arma da fuoco/Guarigione/Individuazione/<br>'
        '         Oreficeria/Scasso/Falegnameria<p>',
    (276, 'Ability : Precise Strikes (Physical Damage +20%)<p>'):
        'Potere : Attacco preciso (automatico: +20% ai danni fisici)<p>',

    # --- :279-:282 Lulwy.
    (279, 'Lulwy is a goddess of wind. Those faithful to Lulwy receive<br>'
          'the blessing of wind and can move swiftly.<p>'):
        'Lulwy è la dea che governa il vento. Chi la venera riceve il<br>'
        'favore del vento e si muove con rapidità.<p>',
    (280, 'Offering: Corpses/Bows/Arrows<p>'):
        'Offerte: cadaveri/archi/frecce<p>',
    (281, 'Bonus   : PER/SPD/Bow/Crossbow/Stealth/Magic Device<p>'):
        'Bonus  : PER/Velocità/Arco/Balestra/Furtività/Dispositivi magici<p>',
    (282, "Ability : Lulwy's trick (Boosts your speed for a short time.)<p>"):
        'Potere : Possessione di Lulwy (abilità: per un attimo diventi<br>'
        '         velocissimo)<p>',

    # --- :285-:288 Itzpalt.
    (285, 'Itzpalt is a god of elements. Those faithful to Itzpalt are<br>'
          'protected from elemental damage and learn to absorb mana from<br>'
          'their surroundings.<p>'):
        'Itzpalt è il dio che governa gli elementi. Chi lo venera assorbe<br>'
        "il potere magico dall'aria e riceve protezione dagli elementi.<p>",
    (286, 'Offering: Corpses/Rods<p>'):
        'Offerte: cadaveri/bacchette<p>',
    (287, 'Bonus   : MAG/Meditation/RES Fire/RES Cold/RES Lightning<p>'):
        'Bonus  : MAG/Meditazione/Res. fuoco/Res. gelo/Res. fulmine<p>',
    (288, 'Ability : Absorb magic power (Absorbs mana from the air.)<p>'):
        "Potere : Assorbi magia (abilità: succhia il mana dall'aria intorno)<p>",

    # --- :291-:294 Ehekatl. ⚠️ Upstream qui sfora: due <p> di fila piu' un
    #     potere su due righe portano l'ultima riga a wy+198, e il menu comincia
    #     a wy+212. La resa ne usa uno solo e il potere sta su una riga.
    (291, 'Ehekatl is a goddess of luck. Those faithful to Ehekatl are<br>'
          'really lucky.<p><p>'):
        'Ehekatl è la dea della fortuna. Chi la venera si tira la sorte<br>'
        'dalla propria parte.<p>',
    (292, 'Offering: Corpses/Fish<p>'):
        'Offerte: cadaveri/pesci<p>',
    (293, 'Bonus   : CHR/LUCK/Evasion/Magic Capacity/Fishing/Lockpick<p>'):
        'Bonus  : CAR/Fortuna/Schivata/Capacità magica/Pesca/Scasso<p>',
    (294, 'Ability : Ehekatl school of magic (Passive: randomize casting mana<br>cost.)<p>'):
        'Potere : Scuola di Ehekatl (automatico: il mana speso diventa<br>'
        '         casuale)<p>',

    # --- :297-:300 Opatos. ⚠️ L'altra scheda che upstream fa sforare.
    #     E il giapponese porta il numero che l'inglese lascia cadere.
    (297, 'Opatos is a god of earth. Those faithful to Opatos have massive<br>'
          'strength and defense.<p><p>'):
        'Opatos è il dio della terra. Chi lo venera acquista una difesa e<br>'
        'una potenza enormi.<p>',
    (298, 'Offering: Corpses/Ores<p>'):
        'Offerte: cadaveri/minerali<p>',
    (299, 'Bonus   : STR/CON/Shield/Weight Lifting/Mining/Magic Device<p>'):
        'Bonus  : FOR/COS/Scudo/Sollevamento pesi/Scavo/Dispositivi magici<p>',
    (300, "Ability : Opatos' shell (Passive: Reduce any damage you<br>receive.)<p>"):
        'Potere : Corazza di Opatos (automatico: -10% a ogni danno subito)<p>',

    # --- :303-:306 Jure.
    (303, 'Jure is a god of healing. Those faithful to Jure can heal wounds.<p><p>'):
        'Jure è la dea della guarigione. Chi la venera sa risanare le<br>'
        'ferite del corpo.<p>',
    (304, 'Offering: Corpses/Flowers<p>'):
        'Offerte: cadaveri/fiori<p>',
    (305, 'Bonus   : WIL/Healing/Meditation/Anatomy/Cooking/Magic Device/Magic Capacity<p>'):
        'Bonus  : VOL/Guarigione/Meditazione/Anatomia/Cucina/<br>'
        '         Dispositivi magici/Capacità magica<p>',
    (306, 'Ability : Prayer of Jure (Heal yourself.)<p>'):
        'Potere : Preghiera di Jure (abilità: recupera i punti vita persi)<p>',

    # --- :309-:312 Kumiromi. Il giapponese dice anche «e sa lavorarli».
    (309, 'Kumiromi is a god of harvest. Those faithful to Kumiromi receive<br>'
          'the blessings of nature.<p><p>'):
        'Kumiromi è il dio del raccolto. Chi lo venera miete i frutti della<br>'
        'terra e ne conosce la lavorazione.<p>',
    (310, 'Offering: Corpses/Vegetables<p>'):
        'Offerte: cadaveri/verdure<p>',
    (311, 'Bonus   : PER/DEX/LER/Gardening/Alchemy/Tailoring/Literacy<p>'):
        'Bonus  : PER/DES/APP/Giardinaggio/Alchimia/Sartoria/Lettura<p>',
    (312, 'Ability : Boundless vigor (Passive: Heal stamina turn by turn.)<p>'):
        'Potere : Vigore inesauribile (automatico: la vigoria si ricarica<br>'
        '         da sola)<p>',

    # --- :315-:318 Yacatect. ⚠️ L'inglese e' un mozzicone di una riga: la resa
    #     segue il giapponese, che descrive la dea per intero.
    (315, 'Yacatect is a god of wealth.<p><p>'):
        'Yacatect è la dea della ricchezza. Chi la venera impara a<br>'
        'trattare e mette insieme ricchezze immense.<p>',
    # 首飾り / 指輪 sono collane e anelli: «Accessories» e' la categoria.
    (316, 'Offering: Corpses/Accessories<p>'):
        'Offerte: cadaveri/amuleti/anelli<p>',
    # ⚠️ 自然鑑定 e' il nome vecchio di 分析: nell'elenco delle abilita' si
    #    chiama «Analisi» (skill.hsp:252), e li' il giocatore la va a cercare.
    (317, 'Bonus   : PER/CON/Negotiation/Sense Quality/Traveling/Alchemy/Investing<p>'):
        'Bonus  : PER/COS/Trattativa/Analisi/Viaggio/Alchimia/Investimento<p>',
    (318, 'Ability : All collection (Passive: Increase chances of get loot.)<p>'):
        'Potere : Raccolta totale (automatico: più probabilità di bottino)<p>',

    # --- :325 e :392 il pannello di scelta.
    (325, 'It seems that it will not reach the god from here...'):
        'Da qui non si arriva a nessun dio...',
    (392, '< '): '< ',
    (392, ' >'): ' >',

    # --- :340-:350 le tre voci del menu.
    (340, 'Abandon God'): 'Abbandona il dio',
    (343, 'Convert to '):
        '"Convertiti a " + godname(inv(INV_ITEM_GOD, ci))',
    (348, 'Believe in '):
        '"Segui " + godname(inv(INV_ITEM_GOD, ci))',
    # «Annulla» e non «Lascia stare»: 「やめる」 e' gia' reso cosi' in
    # text.hsp:1467, ed e' la voce di uscita di ogni menu del gioco.
    (350, 'Cancel'): 'Annulla',

    # --- :424-:445 le otto battute, una per dio, sopra la scheda.
    (424, '--- Are you... interested in machines? ---'):
        '--- ...Ti interessano le macchine? ---',
    (427, '--- Ahaha! Looks like you finally realized that slow is going to die! ---'):
        '--- Finalmente hai capito che i lenti muoiono, eh? ---',
    (430, '--- Elements will be your great power ---'):
        '--- Studia. Gli elementi ti daranno un grande potere. ---',
    (433, '--- Mewmewmew! Coconut crab! ---'):
        '--- Granchio! Granchio reale!!! ---',
    (436, '--- Muwahaha! A well-trained body will be your friend until the end! ---'):
        '--- Muahahah! Un corpo allenato ti resta amico fino in fondo! ---',
    (439, '--- I-I say that I will heal your wounds... ---'):
        '--- T-ti sto dicendo che ti curo le ferite... ---',
    (442, '--- I give...vitality... ---'):
        '--- Io... do... vigore... ---',
    (445, "--- Yeah~! No matter what you do, it's better to have property, right? ---"):
        '--- Qualunque cosa tu faccia, meglio avere di che spendere, no? ---',

    # --- :560-:641 la conversione, la preghiera e i rifiuti.
    # ⚠️ La rete 3 segnala che 「は激怒した。」 e' gia' reso «va su tutte le
    #    furie» in chara_func.hsp:2047, dove pero' il soggetto e' un PNG che
    #    diventa ostile. Qui e' un dio tradito, e la resa resta divisa apposta.
    (560, ' is enraged.'):
        'godname(cdata(CDATA_GOD, CHARA_PLAYER)) + " si adira."',
    (590, 'You are an unbeliever now.'): 'Ora non credi in nessun dio.',
    (598, 'You become a follower of !'):
        '"Ora sei un fedele di " + godname(cdata(CDATA_GOD, CHARA_PLAYER)) + "!"',
    # ⚠️ Il giapponese qui nomina il giocatore e dice che «ci prova lo stesso»;
    #    l'inglese non ha nessuna funzione, e la rete 11 pretende le sue.
    #    La resa tiene la battuta e lascia cadere il nome.
    (616, "You don't believe in the gods."):
        'Non credi in nessun dio, ma provi a pregare lo stesso.',
    (620, 'Really pray to your god?'): 'Vuoi pregare il tuo dio?',
    (626, 'You pray to .'):
        '"Preghi " + godname(cdata(CDATA_GOD, CHARA_PLAYER)) + "."',
    (629, ' is indifferent to you.'):
        'godname(cdata(CDATA_GOD, CHARA_PLAYER)) + " non ti degna di attenzione."',
    (636, "'s help does not seem to reach here..."):
        '"" + godname(cdata(CDATA_GOD, CHARA_PLAYER)) + ": nemmeno il suo aiuto arriva fin qui..."',
    (641, 'It seems that not even  can afford to help you right now...'):
        '"Nemmeno " + godname(cdata(CDATA_GOD, CHARA_PLAYER)) + " ha modo di aiutarti, adesso..."',

    # --- :673-:728 i doni: gli otto servitori divini.
    (673, 'With your current faith skill, you are unable to befriend any more god pets.'):
        'Con la Fede che hai non puoi accogliere altri servitori divini.',
    (682, 'Your party is full. The gift is reserved.'):
        'La squadra è al completo: il dono resta in serbo.',
    (687, 'Do you want to decline this gift?'): 'Vuoi rinunciare a questo dono?',
    (700, 'This android appears to be incredibly durable.'):
        'Questo androide sembra straordinariamente robusto.',
    (704, 'This black angel shows enormous strength when boosting.'):
        'Questo angelo nero sprigiona una forza enorme quando si potenzia.',
    (708, 'This exile can cast several spells in a raw.'):
        'Questo esiliato sa lanciare più incantesimi di fila.',
    (712, 'Weapons and armor licked by this cat receive a blessing of Ehekatl '
          'which adds an extra enchantment.'):
        'Le armi e le armature leccate da questo gatto ricevono la benedizione '
        'di Ehekatl, che vi aggiunge un incantamento.',
    (716, 'This knight can hold really heavy stuff for you.'):
        'Questo cavaliere porta pesi notevoli senza lamentarsi.',
    (720, 'This defender can use Lay on hand to heal a deadly wounded ally. '
          'The ability becomes re-useable after sleeping.'):
        "Questo difensore usa l'imposizione delle mani per curare un alleato "
        'ferito a morte. Torna disponibile a ogni dormita.',
    (724, 'This fairy generates a seed after eating. '
          'The ability becomes re-useable after sleeping.'):
        'Questa fata sputa un seme dopo aver mangiato. '
        'Torna a farlo solo dopo una dormita.',
    (728, 'This goose lay platinum after eating. '
          'The ability becomes re-useable after sleeping.'):
        'Questa oca depone un uovo di platino se mangia a sazietà. '
        'Torna a farlo solo dopo una dormita.',

    # --- :852-:908 il richiamo e l'offerta.
    (852, 'Your prayers have summoned your god.'):
        'La tua preghiera ha richiamato il tuo dio!',
    (899, 'It seems that it will not reach your god from here...'):
        'Da qui non si arriva al tuo dio...',
    (903, "You don't believe in the gods."):
        'Non credi in nessun dio, ma provi a offrire lo stesso.',
    (908, 'You put  on the altar and mutter the name of .'):
        '"Deponi " + itemname(ci) + " sull\'altare e mormori il nome di " '
        '+ godname(cdata(CDATA_GOD, CHARA_PLAYER)) + "."',

    # --- :939-:966 la disputa dell'altare.
    (939, ' claims the empty altar.'):
        'godname(cdata(CDATA_GOD, CHARA_PLAYER)) + " ha rivendicato l\'altare vuoto in un altro mondo."',
    (942, 'Strange fogs surround all over the place. You see shadows of  and  make a fierce dance.'):
        '"Si leva una nebbia strana: le ombre di " '
        '+ godname(cdata(CDATA_GOD, CHARA_PLAYER)) + " e di " '
        '+ godname(inv(INV_ITEM_GOD, ti)) + " si contendono il posto."',
    (958, 'The shadow of your god slowly gets bolder.'):
        "L'ombra del tuo dio si fa via via più netta.",
    # ⚠️ Il giapponese nomina l'altare con `itemname(ti)`, l'inglese no: la
    #    rete 11 pretende le funzioni dell'inglese, e la rete 8 rifiuterebbe
    #    comunque «di » davanti a un nome (di + l'altare -> dell'altare).
    (961, ' takes over the altar.'):
        "godname(cdata(CDATA_GOD, CHARA_PLAYER)) + \" ha preso il controllo dell'altare.\"",
    (966, ' keeps the altar.'):
        'godname(inv(INV_ITEM_GOD, ti)) + " ha difeso l\'altare."',

    # --- :976-:1002 che cosa succede all'offerta. ⚠️ `_s2` e' morfologia
    #     inglese e non si porta dietro: in italiano il verbo non cambia.
    (976, ' shine brightly and disappear. A four-leaved clover falls onto the altar.'):
        'itemname(ci) + " brilla di luce accecante e sparisce: '
        'sull\'altare cade un quadrifoglio."',
    (978, 'Coconut crab?.. Coconut crab!!!!'):
        'Granchio?... Granchio reale!!!!!',
    (984, "I'm glad....j-just a little!!"):
        'Che bello... N-ne sono contenta, un pochino!',
    (989, ' shine brightly and disappear.'):
        'itemname(ci) + " brilla di luce accecante e sparisce."',
    (994, ' shine for a moment and disappear. A three-leaved clover falls from the altar.'):
        'itemname(ci) + " brilla e sparisce: dall\'altare cade un trifoglio."',
    (998, ' shine for a moment and disappear.'):
        'itemname(ci) + " brilla un istante e sparisce."',
    (1002, ' disappear.'):
        'itemname(ci) + " sparisce."',
}
