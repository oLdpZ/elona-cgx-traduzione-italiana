# -*- coding: utf-8 -*-
"""94a - AIKAGE il ninja dalla maschera demoniaca (`chat.hsp:15071`-`:15092`, 8 su 8).

鬼面の忍者『藍影』 / `<Aikage> the shinobi mask`, reso **«<Aikage> il ninja dalla
maschera demoniaca»** (`db_card.hsp:6263`, `db_creature.hsp:73166`). ⚠️ Il nome
italiano viene dal giapponese 鬼面 e non dall'inglese `shinobi mask`: e' gia'
deciso e non si tocca.

⭐ IL REGISTRO E' GIA' FISSATO dalle sue **battute di combattimento**
(`db_creature.hsp:73140`-`:73152`, rese in un lotto precedente): parla per
**massime militari** — «Senza saper adattarsi non c'e' vittoria.», «E' nella
mischia che si mettono alla prova attenzione e discernimento.» ⚠️ Usa 俺 e
お前: da' del **tu** al giocatore, secco, da soldato. Niente keigo.

LESSICO EREDITATO (non deciso qui):
  - アンデッド兵器  «armi non morte»       chat.hsp:10239, :13890, :24505
  - 露払い          «ripulire la strada»   chat.hsp:18160
  - 分身            «sdoppiarsi»           chat.hsp:24445 (il bollettino SU DI LUI)
  - 身代わりの術    «tecnica della sostituzione»  db_creature.hsp:73146, :87632
  - 混沌            «caos»                 ovunque
  - 層              «piano»                chat.hsp:24443
  - 「いいところに来てくれた」 «Capiti proprio a proposito»  chat.hsp:1502, :8734

⚠️⚠️ DEROGA 1 — `:15078`, 露払い NON SONO GUARDIE DEL CORPO.
L'inglese scrive «he was forcing us to act as his personal bodyguards», ma
露払い e' **chi va avanti a sgombrare la strada**, cioe' l'esatto contrario di
chi sta a fianco a proteggere. Il progetto l'ha gia' reso una volta, in bocca a
un altro personaggio e nello stesso senso: «se non aveste **ripulito la
strada**, non sarei arrivata in tempo» (`chat.hsp:18160`). Si tiene quello.
💡 E la lettura giusta cambia la scena: Aikage e i suoi erano l'**avanguardia**
mandata avanti, non la scorta di nessuno.

⭐ DEROGA 2 — `:15087`, 分身の術 E' LO SDOPPIAMENTO, NON UN'OMBRA.
L'inglese dice «That was just my shadow decoy», che in italiano suonerebbe come
un'illusione. Ma il **bollettino su Aikage** (`chat.hsp:24445`, gia' reso) dice
«Se lo colpisci a meta' **si sdoppia**», e la sua carta (`db_card.hsp:6257`)
mette 分身 e 身代わり come due cose distinte. Quindi «la tecnica dello
sdoppiamento», che sta accanto alla «tecnica della sostituzione» gia' resa in
`db_creature.hsp:73146` senza confondersi con lei.

⚠️ DEROGA 3 — `:15074` e `:15077`, IL GIOCATORE NON HA GENERE.
「冒険者か…！」 non puo' diventare «Un avventuriero!». Formula del progetto:
**«chi va all'avventura»** (`chat.hsp:257`, `:1595`, `:7843`, e la NORNE della
93a). E a `:15077` il participio resta invariabile perche' l'oggetto e' un
clitico di seconda persona: «ti ho steso» non concorda.

PERIMETRO: 8 firme su 8 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 15071`), zero gia' rese altrove.

MENU: uno, da 3 voci (`:15075`-`:15077`).

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- l'incontro: le armi non morte si sono scatenate
    15074: 'Chi va all\'avventura...! Capiti proprio a proposito.',
    15078: 'Noi eravamo manovrati con la magia da uno del caos, e ci faceva '
           'ripulire la strada davanti a lui... Ora che chi lanciava '
           'l\'incantesimo è morto, le armi non morte, manovrate anche loro, '
           'hanno cominciato a scatenarsi. Dammi una mano a fermarle!',

    # --- il menu
    15075: 'Se mi va',
    15076: 'E scappare, no?',
    15077: 'Ti ho steso al settimo piano',

    15081: 'Conto su di te!',
    15084: 'Mentre ero manovrato me li sono visti accanto, e ho capito: questi '
           'sono pericolosi. Voglio toglierli di mezzo anche per quelli che '
           'verranno dopo di noi.',
    15087: 'Peccato per te: era la tecnica dello sdoppiamento.',
}
