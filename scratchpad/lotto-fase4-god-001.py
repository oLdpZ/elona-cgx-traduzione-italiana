# -*- coding: utf-8 -*-
"""`god.hsp` si apre e si chiude: le 95 firme del sistema divino.

I nove nomi degli dei, le nove schede del pannello di scelta, le preghiere, le
conversioni, i doni e la disputa dei mattoni. `god.hsp` non aveva dizionario:
114 `lang()` che nessun conteggio guardava, ed e' la regola della 54a.

## ⚠️ Tradurre `godname()` ripara TRENTATRE' siti, non nove

`god.hsp:81`-`:89` riempie l'array `godname`, e trentatre' righe in nove file lo
interpolano. Finche' non era tradotto, `proc.hsp:11749` diceva a schermo «Senti
su di te lo sguardo benevolo di **Lulwy of Wind**»: italiano intorno a un nome
inglese. La 37a lo aveva gia' scritto («`his2` della 36a ha un fratello»), e
questa e' la riparazione.

## Il tetto dei nomi e' 20 caratteri, e lo detta la scheda del personaggio

`command.hsp:17662` scrive `fixtxt("Fede      : " + godname(...), 32)`, e
`fixtxt` (`module.hsp:5041`-`:5054`) **taglia**: `strmid(m, 0, 32)`. L'etichetta
italiana e' lunga 12 — non si accorcia, perche' «Uccisioni : » nella stessa
colonna ne vuole 12 — quindi al nome ne restano **20**.

    Kumiromi della Messe    20   il piu' lungo, ed e' esatto
    Yacatect del Tesoro     19
    Mani della Macchina     19
    Ehekatl della Sorte     19

⚠️ La 37a diceva «`sdim godname, 20, 9` da' 20 byte»: e' una coincidenza, non la
causa. `sdim` non e' un tetto in scrittura — lo dice la 28a e lo riconferma la
33a. Il tetto vero e' `fixtxt`, ed e' un taglio vero.

⚠️ **«Itzpalt Elementale» e' l'unico nome senza genitivo**, e non e' un
capriccio: «Itzpalt degli Elementi» ne ha 22 e verrebbe tagliato a «Itzpalt
degli Element». L'epiteto aggettivale e' una forma italiana buona quanto il
genitivo — «Giove Tonante», «Apollo Delfico» — e qui e' l'unica che ci sta.

## Le schede: `gmes` va a capo da solo, e il pannello e' pieno

`god.hsp:448`-`:454` disegna la scheda con `gmes`, non con `mes`. Il compositore
sta in `module.hsp:4918`-`:5018` e detta tutto:

    7 px per lettera        `gmesx += size / 2`, con size = 14 (:5014)
    va a capo a 84 caratteri  `if gmesx >= gmesx + gmesw`, gmesw = 590 (:5001)
    <br> = 16 px, <p> = 24 px                            (:4979, :4975)

⚠️ **`gmes` ignora il `font` del chiamante**: `god.hsp:419` chiede corpo 13, e
`gmes` lo riscrive a 14. Il passo e' 7, non 6.
⚠️ **Va a capo a meta' parola**: il controllo e' su un carattere, non su una
parola. I `<br>` di upstream stanno li' apposta.

Il corpo comincia a `wy + 70` e il menu a `wy + 212` (`:462`, con `dy = 270` e
`listmax = 2`): **142 px**, cioe' otto righe scarse. `scratchpad/misura-god.py`
le conta, e sull'inglese di monte dice che **due schede su nove finiscono sotto
il menu** — Ehekatl e Opatos, che hanno un `<p>` in piu' e un potere su due
righe. Le rese italiane stanno tutte a `wy+174` o meno: nessuna sfora, e quelle
due sono riparate.

## ⚠️ Sei volte l'inglese di monte perde qualcosa che il giapponese dice

1. `:35` **dice tutt'altro.** La condizione e' `faith * 100 < piety`, cioe' la
   pieta' ha superato quel che l'abilita' Fede regge. Il giapponese lo dice
   («la tua fede e' gia' salita al limite»); l'inglese scrive «Your god becomes
   indifferent to your gift», che parla del dono e non della fede.
2. `:270` e `:300` **perdono il numero.** 無畏無頼 dice `+40%`, オパートスの甲殻
   dice `-10%`; l'inglese scrive «Increase all damage» e «Reduce any damage».
   Un giocatore che sceglie un dio sta confrontando numeri.
3. `:315` **e' un mozzicone.** Il giapponese descrive Yacatect in una frase
   intera — chi la venera impara a trattare e accumula ricchezze enormi —
   e l'inglese scrive «Yacatect is a god of wealth.» e basta. Ed e' l'unica
   scheda in cui l'inglese lascia mezzo pannello vuoto.
4. `:309` e `:285` **accorciano.** Kumiromi «insegna anche a lavorare» quel che
   raccoglie, Itzpalt protegge **e** insegna ad assorbire: l'inglese tiene una
   meta' per ciascuno.
5. `:316` **generalizza**: 首飾り / 指輪 sono collane e anelli, «Accessories» e'
   la categoria.
6. `:616` e `:903` **perdono la battuta.** Il giapponese dice che il senza-dio
   «ci prova lo stesso» a pregare e a offrire; l'inglese scrive due volte «You
   don't believe in the gods.» ⚠️ La resa non puo' portare `name()`, che il
   giapponese ha e l'inglese no: la rete 11 pretende le funzioni dell'inglese.

## ⚠️⚠️ E tre abilita' sono nominate con un nome che il gioco non usa piu'

`:317` scrive 自然鑑定 / «Sense Quality», ma quell'abilita' nel gioco si chiama
分析 / «Analysis» (`skill.hsp:252`). Stessa cosa a `:275`: 銃 e 大工, mentre
`skill.hsp:181` e `:322` dicono 銃器 e 工作. **Sbagliano tutt'e due le lingue di
monte**, ed e' un nome vecchio rimasto in un file che nessuno rilegge. Le rese
usano i nomi che il giocatore trova nell'elenco delle abilita' — «Analisi»,
«Arma da fuoco», «Falegnameria» — perche' una lista di bonus serve a **cercare**
quelle voci, e un nome che li' non esiste non serve a niente.

## Il vocabolario, e da dove viene

    Possessione di Lulwy    ルルウィの憑依, da buff.hsp:63
    Assorbi magia           魔力の吸収, da skill.hsp:952
    Preghiera di Jure       ジュアの祈り, da skill.hsp:948
    Imposizione delle mani  レイハンド, da chara_func.hsp:6258
    Analisi                 分析, da skill.hsp:252 — vedi sopra
    dio / dea / divinita'   神, gia' 37 volte nel dizionario
    Fede                    信仰, l'abilita' di skill.hsp:347
    i ventisei nomi di abilita' dei «Bonus» vengono tutti da skill.hsp
"""
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
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-god-001.jsonl'
DA, A = 0, 99999
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\god.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_god.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]

# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006) o dentro un blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `event.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    return sorgente[riga - 1].lstrip().startswith(';') or riga in SPENTE


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _come = ("e' commentata nel sorgente"
                 if sorgente[_righe[0] - 1].lstrip().startswith(';')
                 else 'sta dentro un commento di BLOCCO')
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `event.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[chiave(v)]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
