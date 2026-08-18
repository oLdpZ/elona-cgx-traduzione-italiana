# -*- coding: utf-8 -*-
"""Gli atti di proprieta', il pannello della struttura e la scala dei potenziali.

`map_user.hsp:39`-`:431`, cinquantacinque voci: leggere un atto e costruire
(`:39`-`:227`), e poi il pannello che il gioco stampa **prima** del menu di casa
del lotto 001 — quanti oggetti ci sono, che negozio e', chi ci lavora e quanto
vale (`:286`-`:431`).

## ⭐ La scala dei potenziali non esisteva, e adesso c'e'

Sedici voci su cinquantacinque sono la stessa scala scritta due volte, per la
trattativa (`:365`-`:383`) e per il carisma (`:387`-`:405`). ⚠️ **Nessuna delle
sette parole era mai stata resa nel progetto**: `Supreme`, `Amazing`, `Superb`,
`Great`, `Good`, `Bad`, `Hopeless` non compaiono in nessun dizionario, e il
giapponese le tiene **in inglese** dentro le quadre.

    Supreme -> Supremo    Great -> Notevole    Hopeless -> Nullo
    Amazing -> Enorme     Good  -> Buono
    Superb  -> Ottimo     Bad   -> Scarso

⭐ Le prime tre le detta `text.hsp:107`, la scala delle **resistenze**, gia' resa
«Suprema / Enorme / Ottima»: sono le stesse parole al maschile, perche' qui
concordano con «potenziale». Le altre quattro sono nuove, e stanno sotto.

## ⚠️ Il giapponese conta i prigionieri, l'inglese no

`:321` interpola **tre** valori in giapponese — 収容者 (quanti), 労働強度,
労働エナジー — e solo **due** in inglese: il conto dei prigionieri sparisce.
Non e' una scelta: le venti righe sopra (`:310`-`:320`) esistono **solo** per
calcolare `pet`, e senza quella riga il ciclo non serve a niente. Si segue il
giapponese, cioe' il codice.
💡 `pet` e' una variabile, non una funzione: la rete 11 confronta le funzioni di
contenuto e non se ne accorge. E' la stessa famiglia dell'«inglese che sa di
meno» della 57a, con la differenza che qui la prova sta nel ciclo di sopra.

## ⚠️ L'articolo lo porta il nome, e otto nomi lo portano

`:227` e' «あなたは + s + を建設した！», dove `s` e' uno degli otto edifici di
`:178`-`:223`. In italiano la frase vuole un articolo, e `contratto-nomi.md` §4
dice che **lo porta il nome**: `s` diventa «un museo», «un campo di prigionia»,
«un sotterraneo». Scrivere «Hai costruito un " + s + "!» funzionerebbe **oggi**,
perche' tutt'e otto sono maschili e cominciano per consonante, e si romperebbe
il giorno che CGX aggiunge un atto per una fattoria.

⚠️ **Non sono i nomi di `text.hsp:2806`**, che pure hanno lo stesso giapponese:
li' sono i **nomi propri** della proprieta' sulla mappa («Museo», «Campo di
prigionia»), qui sono nomi comuni dentro una frase. L'inglese di monte lo dice
scrivendoli in due modi, «My Museum» contro «museum».

## Quel che si e' copiato invece di scriverlo

    :54   ha lo stesso inglese di action.hsp:14742, gia' reso
    :91   e' la nona copia di «Hai imparato una nuova capacita': ...»
    :178-:216  gli edifici, dal contesto gia' reso di text.hsp:2806-:2821
    :325-:343  i tipi di negozio, dagli epiteti di text.hsp:424-:460 —
               «bazar», «drogheria», «bottega magica», «armeria», «locanda»
    :431  «Che cosa vuoi fare?», da command.hsp:17531

Restano nuovi solo 装飾家具店 e ジャンク屋, che nessun epiteto nomina.
"""
