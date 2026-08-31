# -*- coding: utf-8 -*-
"""113a - Lotto 026 di `db_item.hsp`: IL PRIMO LOTTO DI PROSA DEL CORPO.

`FILTER_ITEM_FOOD`, righe 42.700-68.000, **indici 0, 1 e 2**: 50 righe su 41
oggetti. E' il primo lotto che non tocca il rapporto di identificazione (indice
3, chiuso nella 111a su 1.319 rese) ma il **corpo** della descrizione — la prosa
lunga che il gioco impagina, piu' la riga-fonte in coda.

⚠️⚠️ **LA ZONA E' L'UNIONE DEI TRE INDICI, NON L'INDICE 0.** I tre segmenti di
un oggetto il gioco li disegna **nello stesso pannello**, uno sotto l'altro:
rendere l'indice 0 e lasciare l'1 e il 2 in inglese produce un pannello meta'
italiano. `_107-chiavi-item.py` prende un indice per volta, quindi lo scheletro
lo fa `lotti-113/_corpo.py`, che chiede tre volte allo strumento di sempre e ne
incolla i blocchi. Qui: 41 righe dell'indice 0, 1 dell'indice 1, 8 dell'indice 2.

### ⭐⭐ LA CODA NON SI SCEGLIE A MANO

Ogni riga finisce con `\\n#<titolo>`: la **riga-fonte**, il libro da cui la
notizia viene, che `command.hsp:16901` disegna a destra in corsivo col trattino
davanti. La famiglia e' decisa dalla 112a (`lotti-112/titoli_fonte.py`) e la
assegna `lotti-113/_code.py`, che passa dal **giapponese** — l'inglese
appiattisce. Le code di questo lotto sono otto:

    #~Il Cibo Mutevole di Tyris~                        38 righe
    #~Rapporto di Identificazione: categoria <Cibo>~     5   (righe MUTE)
    # ~Bevande da Bere e Bevande da Non Bere~            2
    # ~Vivere Insieme al Bestiame~                       1
    # ~Il Gemito dello Sconfitto~                        1
    # ~Parole del Calamaro Provocatore ...~              1
    # ~Le Parole nel Sonno di una Bambina~               1
    # ~Alle Radici degli Antichi Riti~                   1
    # ~Erbe che si Mangiano ed Erbe che Non si Mangiano~ 1
    # ~Parole di <Lomias> il messaggero di Vindale~      1

⚠️ **`:60514` (la salsa di soia) scrive la fonte con la TILDE LARGA** `～`, che
sta fra i caratteri proibiti di `guardie.py`. Copiata verbatim farebbe bocciare
il lotto: la resa usa la tilde normale.

### ⭐⭐⭐ DIECI TITOLI DELLA 112a CONTRADDICEVANO UN NOME GIA' A SCHERMO

Cercando a mano i termini di questo lotto e' saltato fuori che
`～異形の森の使者『ロミアス』の言葉～` — la fonte di `:67794` — era reso «messo
della **foresta deforme**», mentre lo **stesso identico giapponese**
`異形の森の使者『ロミアス』` sta gia' nel dizionario due volte
(`db_card.hsp:10579`, `db_creature.hsp:100005`) reso **«<Lomias> il messaggero
di Vindale»**. Una terza forma, che nel dizionario non esiste.

Da li' e' nata `scratchpad/_113-fonti-gia-rese.py`: **45 titoli su 200** hanno il
giapponese gia' reso altrove, e **dieci** divergevano. Corretti tutti sulla forma
che il giocatore vede gia' — Balzak («netturbino» -> **custode**), Gwen
(«bambina innocente» -> **l'innocente**), Milis («capo» -> **la comandante**),
Poppy («cucciolo» -> **cagnolino**), Erystia, Loyter, Sin e Abyss (**Gilda dei
Ladri** maiuscola), il sunbararian. ⓘ `<Sophia>` resta nudo: li' l'inglese del
titolo e' `~words of <Sophia>~`, come per le altre quindici divinita'.

### ⭐⭐ L'INGLESE SBAGLIA TRE VOLTE, E TRE VOLTE SI SEGUE IL GIAPPONESE

1. **`:56997`, l'ozouni.** L'inglese ha copiato di peso il testo dell'osiruko —
   «A sweet dish... put in azuki bean soup». Il giapponese dice che e' una
   **zuppa** (スープ料理), che il brodo non e' di azuki, e che il nome viene da un
   piatto ritrovato in testi antichi. Le due righe sono gemelle e vanno lette
   insieme: e' la stessa storia (smaltire i kagami mochi induriti) che finisce
   in due piatti diversi.
2. **`:67983`, la ghianda.** L'inglese dice «They taste good when eaten raw»; il
   giapponese dice **そのままだと渋みが強い**, cruda e' molto allappante. E'
   l'opposto, e la riga dopo («cucinata pare venga discreta») da' ragione al
   giapponese.
3. **`:55607`, la gomma.** L'inglese scrive «Some **gorillas** use gum»: e'
   ごろつき, i **teppisti**. Un katakana letto per un'altra parola.

⚠️ E `:55011` chiama la cicoria «just like **fern**»: e' フェーン, la **fane**,
l'erba della riga `:54948`. Le due righe sono gemelle e la seconda nomina la
prima — un caso che nessuna rete vede, perche' gli inglesi sono diversi.

### ⭐ I TERMINI CERCATI A MANO, che nessuna rete legge

    バーベキューセット  -> set da barbecue        (`db_item.hsp:144489`)
    サンドイッチ       -> panino imbottito
    エーテル抗体       -> cura della corruzione   (`db_item.hsp:145141`)
    黄衣の王          -> il Re in Giallo
    鬼               -> demone                  (鬼熊 «orso demoniaco»)
    幸運の女神 / 収穫の神 -> la dea della fortuna / il dio del raccolto
    もち / 鏡もち / 納豆 / とうふ  -> invariati, gia' in `invariati.md`

💡 **`ぜんざい` e' una parola nuova**: dolce giapponese senza nome italiano,
citato dentro la riga dell'osiruko. Va in `invariati.md` accanto a `osiruko`.

### ⚠️ IL VINCOLO CHE MORDE NON E' LA LARGHEZZA

La 112a l'ha misurato: la coda persa vuole parole da 56 caratteri, il taglio a
70 sta dentro un budget di 77 e il pannello **sfoglia** invece di tagliare. Le
due cose vere sono il **tetto dei 66** sulla riga-fonte (la piu' lunga di questo
lotto ne misura 52) e la **parola spezzata a 17**, che l'italiano raggiunge.
"""
