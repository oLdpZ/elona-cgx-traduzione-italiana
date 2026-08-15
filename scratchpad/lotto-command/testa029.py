# -*- coding: utf-8 -*-
"""Lotto `command-029`: **cambiare classe, razza, sesso, e le monete che piovono**.
Diciassette rese e una rinviata.

⚠️⚠️ **La stessa `lang()` è insieme l'etichetta di un menu e il valore che
finisce nel salvataggio, e il progetto ha già deciso che in quel caso vince il
salvataggio.** `:4655` è `promptAdd cnven(lang("両性具有", "hermaphrodite"))`, cioè
la quinta voce del menu del sesso; trentun righe più sotto, `:4686`, la **stessa**
`lang()` scrive `locvar_newsex`, che a `:4707` diventa
`cdatan(CDATAN_NEWSEX, CHARA_PLAYER)`. `invariati.md` tiene `hermaphrodite` fra i
«valori di dato, non testo — tradurli rompe i salvataggi», e ha ragione: una resa
qui scriverebbe «ermafrodito» dentro il personaggio salvato.
✅ La voce è **rinviata**, e a schermo ci arriva per **toppa** — che è la strada
già battuta: `toppe.jsonl` ha sei toppe su `text.hsp` che fanno esattamente
questo per «maschio», «femmina», «maschio?», «femmina?». Qui la toppa prende le
**tre righe `promptAdd`** (`:4653`-`:4655`), che sono solo etichette, e lascia
intatti gli assegnamenti di `:4678`, `:4682` e `:4686`.
⚠️ **E senza, il menu era metà in italiano**: `strmale` e `strfemale` arrivano già
toppati da `text.hsp` («maschio», «femmina»), 「性別不明」 è tradotto «sconosciuto»,
e in mezzo restavano «male?», «female?» e «hermaphrodite» in inglese. Le due di
mezzo non ha mai potuto prenderle nessuno, perché la loro firma è **ancorata in
`text.hsp`** e `applica.py:618` applica ogni dizionario al suo file soltanto.
💡 **La regola che ne esce**: quando una `lang()` serve **due volte con due
mestieri diversi** — etichetta e dato — il dizionario deve seguire il mestiere
più severo, e l'altro si sistema con una toppa sul solo sito di visualizzazione.

⚠️⚠️ **E il difetto di monte è più grosso di come lo raccontava `invariati.md`:
non sono due grafie, sono TRE.** Lo stesso giapponese 「両性具有」 in inglese è

    command.hsp:4686   locvar_newsex = lang("両性具有", "hermaphrodite")   <- SCRIVE
    command.hsp:3639   if ( cdatan(CDATAN_NEWSEX, i) == lang("両性具有", "bisexual") )
    text.hsp:359       s = lang("両性具有", "hermaphorodite")

cioè il valore si salva con una grafia e si confronta con **altre due**, diverse
fra loro e diverse da quella salvata. In giapponese sono tutte e tre 「両性具有」 e
tutto funziona; in inglese **nessuno dei due confronti scatta mai**, e chi sceglie
l'ermafrodito si vede stampata la stringa grezza sulla scheda del personaggio.
⚠️ `invariati.md` conosceva solo il refuso di `text.hsp` dal 2026-08-07: la terza
grafia, `bisexual`, non l'aveva mai vista nessuno.
⭐ **Non lo tocco**, e non per pigrizia: una toppa qui **rende vivo un ramo che
oggi non gira**, e questo è un cambio di comportamento che vuole un collaudo a
schermo, non una riga scritta di notte. ⚠️ E i due siti di confronto stanno in
**3000-3999**, cioè in una zona ancora da fare: chi la apre se li trova davanti
insieme, che è il posto giusto per decidere.
💡 La lezione: **il valore che un programma salva e il valore con cui lo
confronta sono due stringhe diverse finché qualcuno non prova che coincidono.**
Qui non coincidono da anni, in due punti su tre.

⚠️ **`:4709` dice più dell'inglese, e può.** Il giapponese chiude con
「…もう後戻りはできないわよ。」 — «e adesso non si torna indietro» — che l'inglese non
ha. Le funzioni di contenuto sono `name` e `gendername` in tutt'e due, quindi la
rete 11 lascia passare: è lo stesso permesso di `:15645` nel lotto 026.
⚠️ E «è diventato» non si può scrivere, perché accorderebbe col giocatore: la
resa gira sul presente, «adesso è».

⚠️ **Un legame da ricordare**: la toppa su `:4653`-`:4655` riscrive anche la riga
di 「自称男性」/«male?», la cui **firma è ancorata a `:3651`** e non è ancora
tradotta. Finché quella firma resta l'invariato «male?» che `invariati.md`
prescrive, la sostituzione del dizionario non cambia la riga e la toppa continua
ad agganciarsi. ⚠️ Se un lotto futuro le desse una resa diversa, `applica` si
fermerebbe con «la riga della toppa non esiste piu'» — che è il modo giusto di
accorgersene, ma va saputo prima.

⭐ Riscosso senza decidere: «Hai cambiato idea.» (`action.hsp:9206`, stesso
giapponese), «monete d'oro» (`action.hsp:1245`), «monete di platino»
(`action.hsp:931`), «Medagliette» (`command.hsp:14105`) e «Classe»
(`command.hsp:17663`).
"""
