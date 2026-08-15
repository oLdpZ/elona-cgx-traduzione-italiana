# -*- coding: utf-8 -*-
"""Lotto `command-031`: **i tre menu dell'aspetto** — il cambio di immagine
(`*com_shape_change`), l'editor del ritratto e del PCC (`*com_portrait_loop`) e
lo specchio che nasconde i pezzi d'armatura (`*com_mirror_loop`). Trentadue rese.

⚠️⚠️ **Il lotto non segue la zona: segue la FAMIGLIA, e la zona l'avrebbe
spezzata.** Le voci stanno in 11825-12297, cioè a cavallo del confine fra la
zona 11000-11999 e la 12000-12999. A tenerle insieme non è il gusto ma le
**firme condivise**: `lang("決定    ", "Done    ")` è ancorata a `:11825` e serve
tutt'e tre i menu (`:11825`, `:12034`, `:12276`); `lang("項目", "Category")` è
ancorata a `:11852` e la riusa `:12067`; la riga di aiuto
`"Right,left [Change]  Shift,Esc [Close]"` è ancorata a `:11849` e la riusano
`:12064` e `:12295`. Chi avesse aperto la sola zona 12000-12999 avrebbe reso
sette etichette di una colonna **lasciandone fuori la prima**, e la larghezza
della colonna si decide su tutte insieme.

⭐⭐⭐ **La scoperta del lotto: il carattere inglese è MONOSPAZIATO, quindi la
spaziatura di queste etichette non è decorativa — allinea davvero, e in un caso
è l'unico separatore.** `config.txt` dice `font2. "Courier New"`, cioè il
carattere che il ramo inglese usa a schermo. Per questo upstream scrive
`"Hair    "` e `"Body    "` imbottite a otto colonne: a `:12135`-`:12138` il
gioco fa `s = listn(0, p)` e poi `s += " " + rtval(2)`, e sono quelle spaziature
a incolonnare i numeri.
⚠️⚠️ **E nel menu dello specchio la spaziatura è LOAD-BEARING**: `:12333` e
`:12336` fanno `s += "On"` e `s += "Off"` **senza spazio davanti**. «Mantello» da
sola darebbe «MantelloOff». Per questo qui le etichette vanno a **nove** colonne
e non a otto: «Mantello» ne occupa già otto da sola.

⭐⭐ **Il tetto è 10, ed è misurato, non stimato.** Il testo esce a `wx + 64`
(`module.hsp:129`, `pos arg2 + 4 + arg5`) e la freccia destra è disegnata a
`wx + 175` (`:12153`, `:11900`, `:12340`, identiche in tutt'e tre i menu): sono
**111 px**. Courier a corpo 12 (`12 + sizefix - en * 2`) fa 7,2 px per carattere,
cioè **15,4 caratteri** per etichetta più valore.
⚠️ Il valore più lungo è quello del **ritratto**: `:12141`-`:12145` stampa
` N/A` se l'indice è −1 e ` u` + numero se è più negativo, quindi fino a **cinque**
caratteri. 10 + 5 = 15 → 108 px, dentro; 11 + 5 = 16 → 115 px, **fuori**. Le
righe di colore non arrivano mai a tanto (l'indice è una divisione, sempre ≥ 0),
ma la colonna è una sola e il tetto lo detta la riga peggiore.
✅ **E che 10 sia davvero permesso lo dimostra upstream**: `"Set Detail"` è di
dieci caratteri. Non è un caso che possa esserlo — `*portrait_item:11356` le dà
`rtval = -1`, e `:12136` appende il valore solo `if ( rtval >= 0 )`. Le righe
**senza valore** (`Done`, `Set Detail`, `Set Basic`, `Original`) non hanno tetto
stretto e non entrano nell'incolonnamento; le righe **con valore** vanno tutte
alla stessa larghezza. È la regola vera, e vale la pena scriverla: *l'imbottitura
serve alle righe che portano un numero, e solo a quelle.*

⭐⭐ **E `verifica` ha insegnato la regola giusta, che è più stretta della mia.**
`verifica.py:440` rifiuta una statica il cui inglese finisce con uno spazio e la
cui resa no, perché quello spazio è la **giuntura** col pezzo che segue. Aveva
ragione su due voci — «Conferma» e «Col.capel.», che riempivano tutte le colonne
senza lasciarne una vuota in fondo — e la ragione è più forte di come la guardia
la racconta: nel menu del ritratto lo spazio lo aggiunge il codice
(`s += " " + rtval(2)`), ma nello specchio **no** (`s += "Off"`). Una regola che
vale in un menu e non nell'altro è una regola che si dimentica.
✅ Quindi qui **ogni etichetta finisce con almeno uno spazio**, e la separazione
smette di dipendere da chi concatena. Il testo utile scende a nove colonne su
dieci, ed è per questo che 「髪の色」 è «Col.cap.» e non «Col.capel.».

⚠️⚠️ **La riga di aiuto è al tetto già in inglese, e nessuno strumento la
guarda.** `module.hsp:4344` la stampa a `wx + 58` con `mes`, senza taglio e senza
andare a capo; la riga «Page.» accanto (`:4349`) si tiene un margine di 40 px dal
bordo. Su una finestra da 380: 380 − 58 − 40 = **282 px = 39 caratteri**.
L'inglese ne usa **38**. Un carattere di margine.
✅ Per questo la resa **non** è «Destra,sinistra [Cambia]  Shift,Esc [Chiudi]»,
che ne farebbe 44 e uscirebbe dalla finestra, ma
«Dx,Sx [Cambia]  Shift,Esc [Chiudi]», che ne fa 34. ⚠️ `larghezze.py` non poteva
avvisare: guarda **solo `text.hsp`** e solo i menu che passano da `*prompt_key`,
e questa è la sottotitolatura di `display_window`.
💡 La forma della resa la detta `text.hsp:115`, che ha già `strhint3` =
«Shift,Esc [Chiudi]  »: il nome del tasto resta com'è, l'azione fra parentesi si
traduce.

⚠️ **Lo stesso giapponese sotto due inglesi diversi, e la rete 4 ha ragione a
pretenderne una resa sola.** 「項目」 è `"Category"` a `:11852` e `"Part"` a
`:12297`. La resa è **«Voce»** in tutt'e due, che è quel che 項目 vuol dire e che
regge sopra tutt'e due gli elenchi — le categorie dell'aspetto e i pezzi
d'armatura.

⭐ **E il rovescio: lo stesso inglese sotto TRE giapponesi diversi.**
`"Appearance"` sta per 「個別画像の変更」 (`:11849`, cambia lo sprite), per
「肖像の変更」 (`:12064`, cambia il ritratto) e per 「着替えさせる」 (`:6062`, già reso
«Cambia i vestiti» in una sessione passata). Tre schermate diverse, un inglese
solo: le rese sono «Cambia immagine», «Cambia aspetto» e quella già decisa. È la
famiglia della rete 13, e qui il referto avrà ragione a parlare.

⭐ Riscosso senza decidere: **«Ritratto»** era già la resa di `"Portrait"` in
`text.hsp:120` (`p [Ritratto]`), e i nomi delle parti del corpo di `text.hsp:136`
— Testa, Collo, Dorso, Torso, Mano, Anello, Arto, Vita, Gamba — fissano il
registro nominale asciutto che queste etichette seguono.

💡 **Due scelte di parola, per il tetto.** 「服」 è **«Veste»** e non «Vestito»
perché così «Col.veste» sta in nove colonne; 「アクセサリ1」 è **«Access. 1»** e non
«Etc1» perché l'inglese qui dice meno del giapponese e la voce è una statica,
senza contratto di funzioni da rispettare.
"""
