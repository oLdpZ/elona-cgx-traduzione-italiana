# -*- coding: utf-8 -*-
"""94a - MANSON l'avventuriero prudente (`chat.hsp:15378`-`:15397`, 7 su 7).

周到な冒険家『マンソン』 / `<Manson> the careful adventurer`, reso **«<Manson>
l'avventuriero prudente»** (`db_card.hsp:1999`, `db_creature.hsp:48003`).
E' il compagno di <Cray> — la sua carta lo dice: «si prende cura
dell'equipaggiamento e delle provviste, e si preoccupa per Cray che si butta
nell'avventura» (`db_card.hsp:1993`) — e i due stanno **fianco a fianco** sulla
mappa, `characreate` a `map.hsp:4977` e `:4980`, alle caselle 23,25 e 25,25.

⭐⭐ IL REGISTRO NON SI DECIDE, SI TROVA — E QUI LO DECIDE UNA REGOLA GIA'
SCRITTA. Manson da' del **あなた** al giocatore in 敬語 (お見受けします, お気を
つけて, 〜ですかな), con la coda pomposa 〜ぞ del vecchio signore. La decisione
dell'88a (Maile) dice che in questo caso la resa e' il **voi di cortesia**, che
oltre a suonare giusto e' **l'unica seconda persona italiana che non chiede un
genere**. Sta in `decisioni.md`.

⭐⭐⭐ IL LESSICO E' TUTTO NEL VICINATO, E IL VICINATO E' A VENTI RIGHE.
La donna all'imbocco della valle (`chat.hsp:15438`-`:15442`, resa nella 91a)
racconta **la stessa scena dall'altra parte**, ed e' li' che il lessico e' gia'
fissato:
  - 谷            «la valle», «l'imbocco della valle»   `:15438`, `:15439`
  - 谷の奥        «il fondo della valle»                 `:15440`
  - 黒い獣        «le bestie nere»                       `:15439`
  - 空間が閉じて  «lo spazio si e' richiuso»             `:15440`
  - 謎の声        la voce che tutti hanno sentito        `:15438`
  - 旅糧          «cibo da viaggio»                      `db_item.hsp:148280`

⚠️ DEROGA 1 — `:15391`, «avventuriero» PORTA UN GENERE E QUI NON PUO'.
並の冒険家ではない e' detto **al giocatore**, quindi «non siete un avventuriero
qualunque» sbaglia meta' delle partite. Si gira su **«persona»**, che in
italiano vale per chiunque: «non siete persona comune». Stessa ragione a
`:15390`, dove この世界の人間 diventa «una persona di questo mondo».

⚠️ DEROGA 2 — `:15385`, IL SENSO DEL TEMPO E' IL SUO, NON QUELLO DEL GIOCATORE.
L'inglese scrive «**your** sense of time gets out of whack», ma il giapponese
non ha soggetto e la frase dopo e' 「もうここに10年以上いる気がしてなりませんぞ」,
cioe' **lui** che si sente qui da dieci anni. E' un sintomo che riferisce di se
stesso, come tutto il resto del suo referto sulla valle.

⭐ DEROGA 3 — `:15386`, 空間の隔離 NON SONO «RIFTS».
L'inglese dice «Those rifts in continuous space», che sono squarci; il
giapponese dice **isolamento** dello spazio, e la donna a `:15440` conferma:
«lo spazio si e' richiuso, e ne e' rimasta solo una fessura piccolissima». Non
si apre niente: si chiude.

PERIMETRO: 7 firme su 7 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 15378`), zero gia' rese altrove.

MENU: uno, da 2 voci (`:15380`-`:15381`). `:15382` e' un **buff**, cioe' il
corpo grande in mezzo allo schermo.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- il buff: il referto sulla valle
    15382: 'In questo momento il fondo della valle è in preda a un fenomeno '
           'soprannaturale a cui nessun essere umano può porre rimedio... Me '
           'lo dice il fiuto che mi sono fatto in tanti anni d\'avventura.',

    # --- il menu
    15380: 'Che cosa sta succedendo?',
    15381: 'Vado a dare un\'occhiata',

    # --- «Che cosa sta succedendo?»
    15385: 'Tanto per cominciare, il senso del tempo si è sballato. Dalla '
           'comparsa delle bestie non dovrebbe essere passato molto, eppure '
           'non riesco a togliermi la sensazione di essere qui da più di '
           'dieci anni.',
    15386: 'E poi quella voce misteriosa che dicono di aver sentito tutti '
           'quelli che erano nella valle. E lo spazio che si richiude, pezzo '
           'dopo pezzo. Non c\'è dubbio: c\'è una mano che sta piegando lo '
           'spazio e il tempo.',

    # --- «Vado a dare un'occhiata»
    15390: 'Voi? Uhm... Sento addosso a voi un\'aria che non so spiegarmi. '
           'Come se... ecco. Come se non foste una persona di questo mondo.',
    15391: 'Perdonatemi. Comunque sia, vedo bene che non siete persona comune. '
           'Se anche così avete deciso di andare verso la valle, abbiate '
           'riguardo. Avete con voi del cibo da viaggio? Sarà una strada '
           'lunga e aspra, statene certi.',
}
