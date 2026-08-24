# -*- coding: utf-8 -*-
"""92a - MANYTIA (`chat.hsp:13634`-`:13833`, 15 firme).

冒険商人『メニティア』 = **«<Manytia> la mercante avventuriera»**
(`db_creature.hsp:58081`, `db_card.hsp:3728`). Vende alle spalle del fronte, a
centomila pezzi l'uno, e ha in tasca la chiave che sbarra la strada: se non hai
centomila monete non ti parla nemmeno (`:13636`).

⭐ META' DEL BLOCCO E' UNA LEGGENDA, non chiacchiere da bottega: `:13642`-`:13645`
sono quattro battute fra virgolette — il racconto degli **abitanti della
collina** che lasciarono il continente prima che diventasse **Irva Perduta**.
Registro da fiaba recitata, staccato dal resto.

LESSICO EREDITATO (non deciso qui):
  - «<Manytia> la mercante avventuriera»  db_creature.hsp:58081
  - ロストイルヴァ «Irva Perduta»          chat.hsp:10227, :2094, :2141
  - 丘の民        «gli abitanti della collina»  db_card.hsp:6471
  - 結界          «barriera»               event.hsp:3620, db_creature.hsp:84804
  - ネフィア      «Nefia» · イルヴァ «Irva»
  - 靴下          «calzini»                chat.hsp:12431 e la catena del ladro
  - i nove dei con l'epiteto: `:13651`-`:13658`, gia' resi
  - e con lei si usa il **tu**: `:13715` «Ti serve altro?», gia' resa

⭐⭐⭐ DEROGA 1 — `:13646`, L'INGLESE DICE IL CONTRARIO E SI SMENTISCE DA SOLO.
Il giapponese e' 「…伝説どおりだったとは思いませんでしたぁ。ロストイルヴァは
本当にあったんだ！」: *non avrei mai creduto che fosse davvero come nella
leggenda* — cioe' lo stupore di chi scopre che **era vero**. L'inglese scrive «I
don't think it actually happened in exactly the way the legend recounts», cioe'
*non e' andata proprio cosi'*, e poi nella stessa battuta esclama «There really
was a Lost Irva!». ⚠️ Le due frasi inglesi si contraddicono a due parole di
distanza: arbitra il giapponese (57a).

⭐⭐ DEROGA 2 — `:13707`, L'INGLESE TAGLIA LA BATTUTA E IL SUO AGGANCIO.
Il giapponese dice che il cliente di prima si e' portato via una dozzina di
pezzi **a condizione che, oltre alla chiave, lei ci mettesse anche i propri
calzini**, e chiude con 「こんなに捌けるなんて大誤算ですよぉ」 — *non pensavo di
smaltirne cosi' tanti, che errore di calcolo*. L'inglese tiene solo «since the
previous customers bought one dozen, I'm no longer in stock».
⚠️ Non e' colore che si puo' buttare: i **calzini** sono una catena di battute
che il progetto ha gia' resa per intero — il responsabile dei rifornimenti che
ne chiede trenta (`:12431`), il ladro di calzini (`:12513`, `:12713`-`:12738`),
il collezionista di `:13170`. Tolti i calzini, questa riga diventa una nota di
magazzino; con i calzini e' la stessa barzelletta che attraversa il gioco.

⚠️ DEROGA 3 — `:13662`, NIENTE AGGETTIVO SUL GIOCATORE.
「そんなつれないこと言っちゃってぇ」 e' *che risposta scortese*. «Non fare il
difficile» darebbe un genere: si sposta l'accordo sulla **risposta**, che e'
roba mia.

💡 `:13698` — l'inglese comprime 「お客さんもお目が高いですねぇ。うへへ…毎度
ありですぅ。」 in «Thank you for your purchase!», buttando via il complimento
interessato e la risatina. Restano tutt'e due: e' il suo modo di parlare.

⭐ UNA RIPARAZIONE SU UNA RIGA GIA' RESA: `:13714` diceva «Comprare anche
l'altro **(99999gp)**», mentre le due voci gemelle dello stesso personaggio
(`:13773`, `:13774`) dicono **«(99999 oro)»** e la convenzione del progetto
rende `gp` con «oro» (`chat.hsp:8825`, `:8832`, `:8835`). Tre voci di menu della
stessa creatura, due unita' di misura diverse. Allineata.

PERIMETRO: 15 firme su 30 dentro il blocco, zero occorrenze fuori
(`python scratchpad/_85-blocco.py 13634`). Le altre quindici erano gia' rese.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    13637: "Non hai neanche uno straccio di centomila...? Allora non ho niente da dirti.",
    13642: "\\\"Tanto tempo fa, molto prima che nascessero le Nefia. Gli dei decisero che il continente dove la guerra aveva sconvolto il mana era troppo pericoloso, e lo separarono da Irva chiudendolo dentro una barriera.\\\"",
    13643: "\\\"Gli dei consigliarono a chi viveva sul continente di trasferirsi, e quasi tutti obbedirono. Ma gli abitanti della collina no: si divisero fra chi voleva restare a ogni costo sulla collina a cui teneva e chi, pur a malincuore, se ne sarebbe andato.\\\"",
    13644: "\\\"Dopo liti e ripensamenti, i nostri antenati scelsero di passare su un altro continente, in cerca di tecniche nuove e materiali nuovi. E quando, arrivati di là, si voltarono indietro, il continente si stava avvolgendo di luce e saliva verso il cielo.\\\"",
    13645: "\\\"Se alzi gli occhi al cielo, ricordati: da qualche parte lassù c'è la collina delle origini, Lustor, e forse gli abitanti della collina ci vivono ancora.\\\"",
    13646: "...Non avrei mai creduto che fosse tutto vero come nella leggenda. Irva Perduta esisteva davvero! Chissà se Lustor c'è ancora...",
    13659: "Un articolo dedicato agli dei, che ne dici? Centomila tondi tondi l'uno! Un affare.",
    13662: "Ma dai... che risposta scortese. I soldi ti avanzano, no? I soldi.",
    13698: "Che occhio fino, cliente. Uhehe... grazie e torna presto.",
    13767: "Cliente, vuoi andare avanti? Da qui in poi è pericoloso, e ho fatto sbarrare il passaggio. Se compri qualcosa da me, la chiave te la posso anche dare. Non mi pare un cattivo affare.",
    13776: "Su, se vuoi la chiave non ti resta che comprare qualcosa.",
    13779: "Anche se mi ammazzi, la chiave non cade: ce l'ho ben chiusa nella tasca quadridimensionale.",
    13757: "Ehehe... grazie e torna presto. Il cliente se la passa bene, eh.",
    13824: "Ecco fatto, grazie e torna presto! E allora ti do anche la chiave.",
    13707: "A dire il vero volevo venderne ancora... Ma il cliente di prima se n'è portati via una dozzina per tipo, a condizione che oltre alla chiave ci mettessi anche i miei calzini. Adesso sono senza scorte. Non avrei mai creduto di smaltirne così tanti: un bell'errore di calcolo, eh.",
}
