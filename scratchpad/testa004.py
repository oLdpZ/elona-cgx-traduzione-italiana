# -*- coding: utf-8 -*-
"""Il resto di `map_user.hsp`: i codici dell'allevamento, il negozio, i ranghi.

`map_user.hsp:1025`-`:2775`, cinquantadue voci, e con queste **il file e'
chiuso** per il referto del dizionario: 204 `lang()`, 203 rese e una rinviata
con toppa (`:730`, lotto 003).

## ⚠️ Due volte l'inglese di monte non regge, e decide il sito

1. **`:1510` sbaglia la reazione.** `shopval == 0` vuol dire che il giocatore ha
   **annullato** il menu dei talenti del negoziante. Il giapponese gli fa fare
   una ずっこけ — la caduta comica della delusione — e l'inglese scrive
   «smiled». Dopo un annullamento un sorriso non vuol dire niente: la resa
   segue il giapponese, «ci resta male».
2. **`:1164` ha il giapponese di un'altra riga.** 「護衛対象は放せない」 e'
   identico a `:937`, che sta all'**allevamento** e parla di lasciar libero un
   compagno; qui si e' nel **campo di prigionia** e si rinchiude. L'inglese
   distingue («release» contro «contain»), il giapponese no: e' il caso
   dell'inglese che **sa di piu'**, e si segue lui. ⚠️ La rete 3 lo segnala, ed
   e' giusto che lo segnali.

## Il vocabolario, e da dove viene

    YacaPoint          invariato, da action.hsp:1277 e db_item.hsp:135931
    punti fama         名声値, da action.hsp:1207 — stessa riga, si copia
    chip da casino'    カジノチップ, da text.hsp:2197
    monete di bronzo   ブロンズ硬貨, dal lotto 001
    Energia da Lavoro  労働エナジー, da map.hsp:12281
    accresce il potenziale   潜在能力を伸ばす, da ai.hsp:1893
    vendite            営業実績, il contatore reso «[Vendite: N]» a :407
    Arredi / Cimeli    家具 / 家宝, dalla finestra del valore (lotto 003)
    map0..map3         nomi di file, non parole: restano

💡 **`:1611` e' l'unica volta che l'inglese e' piu' oscuro del giapponese senza
sbagliare**: 片開き e' la porta a **un battente solo**, e l'inglese scrive «EW
type», che non dice niente a nessuno. La resa segue il giapponese.

## ⚠️ Tre righe sono pezzi di un'altra riga

`:2308` e `:2310` non sono frasi: sono i due addendi con cui `:2308`-`:2311`
compone `s`, che poi entra dentro `:2315`. Lo spazio in testa e' quel che li
attacca al numero che li precede, e va tenuto.

## ⚠️ E il riquadro dei talenti del negoziante e' uno dei larghi

`:1501` dichiara `val = promptx, prompty, 280 + (en * 140), 0`, cioe' **420 px
in inglese** contro 280 in giapponese: e' uno dei cinque riquadri che la lingua
**allarga** invece di stringere, e la rete 5 lo sa leggere solo dalla 60a.
"""
