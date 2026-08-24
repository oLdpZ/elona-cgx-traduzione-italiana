# -*- coding: utf-8 -*-
"""95a - CARTER, NANCY e TONI: Raskilis Sud, una mappa intera in un lotto.

Tre blocchi, 14 rese: `chat.hsp:15331`-`:15346` (CARTER, 5 su 5),
`:15347`-`:15361` (NANCY, 4 su 4) e `:15362`-`:15377` (TONI, 5 su 5).

⭐⭐ LA MAPPA E' IL RAGGRUPPAMENTO. `map.hsp:5087`-`:5100` mette **TONI**
(`:5093`), **NANCY** (`:5096`) e **CARTER** (`:5099`) nella stessa area,
`AREA_SOUTH_RASKILIS` / `ras_south`, e non ce n'e' un quarto che parli: dopo
questo lotto la mappa e' **finita**. E' l'accampamento dove sono scesi i
profughi della valle, tre caselle di distanza l'uno dall'altro.

⭐⭐⭐ E I TRE RACCONTANO LA STESSA COSA DA TRE POSTI DIVERSI NEL TEMPO.
Carter e' li' da prima («Raskilis e' da sempre una via di passaggio»), Nancy ci
e' arrivata da **Zaile** dopo l'Etherwind (`db_card.hsp:2110`) e sta gia'
cercando dove andare dopo, Toni pesca come se non fosse successo niente. Le
rese vanno lette insieme: e' un accampamento, non tre passanti.

⭐⭐⭐ LA PERDITA DI MEMORIA E' LA TERZA VOLTA OGGI, ED E' UN TRATTO DEL POSTO.
`:15355` — 「何が消えたのかすらもう思い出せない」 — dice che Nancy non ricorda
**che cosa** le sia stato portato via. Nello stesso giorno CRAY non ricorda chi
si sia buttato nella fenditura (`:15407`) e MANSON ha perso il senso del tempo
(`:15385`, 94a). Due mappe piu' in la' ci sono **RYUTYE e NERES, i due
smemorati** (`:12872`-`:12906`, ancora da fare). Non si alleggerisce nessuna
delle tre: e' la stessa cosa detta da tre bocche.

LESSICO EREDITATO (non deciso qui):
  - ザイール    «Zaile»                       `text.hsp:2902`, `chat.hsp:9462`
  - 谷の奥      «il fondo della valle»        `:15382`, `:15439`
  - 旅人        «il viandante»                `chat.hsp:11066`, `:15183` e altri
  - 未開        «terra selvaggia»             `chat.hsp:2334`
  - 釣り        «pesca»                       `text.hsp:137`
  - ラスキリス  «Raskilis»                    `:15470` e altri

LESSICO DECISO QUI (va in glossario):
  - 悪魔の獣 -> **«bestie diaboliche»**. ⚠️ NON «demoniache»: in questo progetto
    「悪魔」 e' **il demone**, quello della trama principale — i tre di Mayroon,
    Eulderna e Kikkasu (`chat.hsp:24298`-`:24304`, `text.hsp:9819`-`:9840`) —
    e Nancy non sta parlando di quelli. Sta dando un nome suo, da profuga, alle
    stesse creature che tutti gli altri chiamano 黒い獣 «le bestie nere». Le due
    parole restano distinte perche' lo sono nel giapponese.
  - ウキ -> **«galleggiante»**, il termine di pesca.
  - キャンプ地 -> **«il campo»**. ⚠️ Non «campo profughi», che e' gia' preso da
    `text.hsp:2985` per un altro posto (la terra di Ruoza): qui il giapponese
    dice solo キャンプ地, e chi ci vive non lo chiama cosi'.

⚠️ DEROGA 1 — `:15366`, L'INGLESE BUTTA VIA L'UNICA COSA UTILE DELLA RIGA.
Il giapponese dice 「魚の釣れる場所には目印にウキを浮かべているよ」: dove si
pescano i pesci Toni ha messo **un galleggiante a fare da segnale**. L'inglese
scrive «I'm floating over a place where you can fish», che perde sia il
galleggiante sia il fatto che sia un segnale — e resta una frase che non dice
niente. E' un'**istruzione di gioco**: quei segnali sull'acqua si vedono sulla
mappa, e la riga serve a spiegare che cosa sono. Si segue il giapponese (57a).

⚠️ DEROGA 2 — `:15342`, 冒険者 AL PLURALE E' DI ALTRI, NON DEL GIOCATORE.
La regola dell'88a vieta «avventuriero» **riferito al giocatore**, perche' porta
un genere. Qui Carter parla di gente che e' entrata nella valle e non e'
tornata: il plurale generico italiano regge, e non c'e' niente da girare.

⭐ DEROGA 3 — `:15335` e `:15338`, IL VECCHIO PARLA DA VECCHIO.
Carter usa 〜じゃ e 〜おる, la coda del vecchio signore, e la sua carta lo dice
veterano ritirato in campagna (`db_card.hsp:2123`). In italiano non c'e' una
desinenza che lo faccia: si tiene con **l'ordine delle parole e il lessico**
(«sul ciglio della strada», «mi servo di», «non e' male») e non con un accento
finto. Da' del **tu** al giocatore, come gli altri due.

PERIMETRO: 14 firme su 14 dentro i tre blocchi, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 15331 15347 15362`), zero gia' rese altrove.

MENU: due, da 2 voci ciascuno (`:15333`-`:15334`, `:15364`-`:15365`), piu' due
`buff` (`:15335`, `:15366`), cioe' il corpo grande in mezzo allo schermo.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- CARTER: il corpo e il menu
    15335: 'Raskilis è da sempre una via di passaggio per i viandanti. Prima '
           'che succedesse tutto questo, sul ciglio della strada c\'era anche '
           'qualche mercante, qua e là.',
    15333: 'Vivi qui?',
    15334: 'Che cosa c\'è in fondo alla valle?',
    15338: 'Ah. Mi servo di un campo che qualcuno aveva cominciato a mettere '
           'su e non ha finito. Vivere di quel che ci si procura da sé non è '
           'male.',
    15342: 'Il fondo, fuori dalla strada, è ancora terra selvaggia. Gli '
           'avventurieri che ci sono entrati a cuor leggero non sono quasi '
           'mai tornati indietro.',

    # --- NANCY: la prima volta
    15354: 'Bestie diaboliche, che ci portano via tutto quello che abbiamo di '
           'caro...',
    15355: 'Anche se, a dirla tutta, non riesco più nemmeno a ricordarmi che '
           'cosa sia sparito.',
    15356: 'Anche Zaile, a ovest, è stata colpita e come città non funziona '
           'più, così non mi è rimasto altro da fare che trasferirmi qui.',

    # --- NANCY: quando la si risente
    15350: 'A dire il vero sto già cercando dove trasferirmi la prossima '
           'volta. Anche qui, chi lo sa per quanto si starà al sicuro?',

    # --- TONI: il corpo e il menu
    15366: 'Dove i pesci abboccano ho messo un galleggiante a fare da '
           'segnale. Regolati su quelli.',
    15364: 'Come va?',
    15365: 'Non si pesca in qualsiasi specchio d\'acqua?',
    15369: 'Come sempre. Il mondo cambia, ma i pesci che si pescano restano '
           'gli stessi. È una bella cosa.',
    15373: 'Ah ah, questa è buona. Tu vieni da un mondo dove si pesca in '
           'qualunque specchio d\'acqua?',
}
