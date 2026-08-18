# -*- coding: utf-8 -*-
"""Il raccolto, le piastrelle, il valore della casa, e chi sta dove.

`map_user.hsp:604`-`:985`, trentaquattro voci: quel che succede **dopo** aver
scelto una voce del menu del lotto 001. Tre gruppi — l'editor delle piastrelle
e il raccolto, la finestra del valore della casa, e lo spostamento di compagni,
ospiti e bestiame.

## ⚠️⚠️ `:730` — l'inglese ha la riga giusta dell'evento sbagliato, ed e' RINVIATA

    :718  txt lang(mdatan(MDATAN_NAME) + "を何と呼ぶ？ ",
                   "What do you want to call " + mdatan(MDATAN_NAME) + "? ")
    :729  mdatan(MDATAN_NAME) = "" + inputlog
    :730  txt lang("" + mdatan(MDATAN_NAME) + "という名前で呼ぶことにした。",
                   "You named " + him(tc) + " " + cdatan(CDATAN_NAME, tc) + ".")

La riga sopra chiede il nome della **proprieta'**, la riga in mezzo lo scrive in
`mdatan(MDATAN_NAME)`, e la conferma inglese nomina un **personaggio** con
`cdatan(CDATAN_NAME, tc)`. E' la riga della finestra che da' il nome a un
compagno, copiata qui: a schermo, in inglese, esce il nome di chi capita in `tc`.
E' la famiglia della 58a (`main.hsp:5684`), e la prova sta nelle due righe
intorno, non nella lingua.

⚠️ **Non e' toppabile dal dizionario**: la rete 11 pretende che le funzioni di
contenuto della resa siano quelle dell'inglese, e l'inglese ha `cdatan`, non
`mdatan`. Scrivere `mdatan` sarebbe **aggiungere** una funzione che l'inglese
non ha, che e' proprio quel che la rete esiste per impedire; scrivere `cdatan`
sarebbe copiare il difetto. Si fa come `action.hsp:9631`: **rinvio piu' toppa**.

## ⚠️ La finestra del valore della casa ha una geometria stretta

`:762` disegna quattro etichette e poi le stelle:

    map_user.hsp:766   font ..., 12 + sizefix - en * 2      il carattere e' 10
    map_user.hsp:769   pos x, y                             l'etichetta
    map_user.hsp:773   pos x + 35 + cnt * 13 + en * 8       la prima stella

cioe' **43 px** fra l'inizio dell'etichetta e la prima stella (il `cnt` del `pos`
delle stelle e' quello del ciclo **interno**, non delle etichette: le stelle
stanno in fila a 13 px l'una dall'altra). Con un carattere da 10 px ci stanno
sei o sette lettere: «Base», «Arredi», «Cimeli», «Totale» ne usano al massimo
sei. ⚠️ Il passo di quel carattere **non e' misurato** — le reti conoscono il 13
di `*prompt_key` e il 12 della pergamena — e sei lettere sono una stima prudente,
non un tetto provato. Va guardato a schermo.

## Quel che si e' copiato invece di scriverlo

    :672  stesso giapponese di main.hsp:8475, la domanda che questa voce apre
    :687  stesso giapponese di main.hsp:8493
    :724  stesso giapponese di command.hsp:7466
    :878  stesso giapponese di proc.hsp:10793
    :953  stesso giapponese di command.hsp:7098, su un'altra variabile
    :776  «★» resta «*», come main.hsp:980 e text.hsp:12: e' un segno, non testo

## ⚠️ E cinque righe portano un helper inglese che se ne va

`is(tc)` (`:863`, `:890`), `his(c)` a **un** argomento (`:895`) e `_s(c)`
(`:903`, `:907`, `:949`) sono morfologia inglese: `funzioni.py` li toglie, e in
italiano non lasciano buchi perche' il verbo si accorda da solo.
"""
