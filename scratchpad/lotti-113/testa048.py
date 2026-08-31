# -*- coding: utf-8 -*-
"""118a - Lotto 048 di `db_item.hsp`: I GRIMORI, il CORPO, e la categoria CHIUDE.

`FILTER_ITEM_SPELLBOOK`, righe da `:102037` a `:129870`: **48 righe** su 42
oggetti — 42 dell'indice 0, **4 dell'indice 1** e 2 dell'indice 2. Con questo
lotto `FILTER_ITEM_SPELLBOOK` va a **0 da fare su 92 vive**: e' la **sesta**
categoria del corpo che si chiude, dopo mobilio, attrezzi, cibi, scarti e armi.

⚠️⚠️ Previsione di `applica`: **+48** per 48 rese, nessuna gemella.

### ⭐⭐⭐ L'INDICE 1 DEI GRIMORI: IL GIAPPONESE E L'INGLESE DICONO DUE COSE

Quattro righe di questo lotto — `:113099`, `:113172`, `:113245`, `:113460` —
non sono la stessa frase in due lingue. Sono **due contenuti diversi nello
stesso posto**:

    JP  <ランク6魔法>
    EN  \\"Ouch! Hot!\\" \\n# a Eulderna Researcher handling this tome

Il giapponese ci mette il **tassello del rango**; l'inglese lo butta e ci mette
una battuta. Non e' un appiattimento e non e' una perdita: e' l'unico posto del
file dove le due lingue riempiono lo slot con roba diversa.

**La decisione**: la build e' il ramo `en`, e la stringa che il giocatore legge
e' quella inglese. Si rende **quella**. Il rango resta non scritto, che e'
esattamente la decisione della 110a, e la battuta che il giocatore vede oggi non
sparisce.

### ⚠️⚠️⚠️ E LA DOMANDA «QUANTE CE NE SONO» HA SMENTITO LA 110a

Chiesto al sorgente — 「ランク…魔法」 su ogni `description()` di `db_item.hsp` —
il tassello del rango non e' su quattro righe: e' su **80**, una per **ogni**
grimorio, sempre in `description(1)` del ramo `if ( jp )`. Le quattro di questo
lotto sono le uniche **vive**, perche' per le altre 76 l'inglese lascia
`description(1) = ""` e una riga con l'inglese vuoto non arriva
nell'estrazione.

⚠️ Questo **smentisce l'argomento** su cui la 110a ha deciso di non scrivere il
rango. Il glossario dice, degli 82 inglesi dell'indice 3: «il giapponese non lo
dice mai — non su una sola riga [...] Il rango si sa dire; qui l'autore ha
scelto di non dirlo». L'autore lo dice, su tutti e 80 gli oggetti, **un indice
piu' su**. Il rango non e' un'aggiunta dell'inglese: e' una cosa che le due
lingue mettono in due posti diversi.

    JP   description(1)   <ランク6魔法>            80 righe su 80
    EN   description(3)   Book of Rank 6 Magic.   82 righe su 82
    IT   da nessuna parte                          (la decisione della 110a)

Oggi il giocatore italiano e' **l'unico dei tre** che il rango non lo legge. La
decisione va riaperta, e non la riapre questo lotto: le 80 righe dell'indice 3
sono gia' rese e chiuse (1.319 su 1.319), il loro tetto e' **secco a 69** e il
glossario stesso nota che ci stanno dentro proprio perche' non portano parole in
piu'. Rimetterci il rango e' un lavoro suo, da misurare prima di cominciarlo.

ⓘ La lezione e' quella della 117a, la `?` dell'uovo: la domanda giusta non e'
«come rendo questa riga», e' «quante ce ne sono». Stavolta la risposta non ha
confermato un numero — ne ha rovesciato uno scritto nel glossario da otto
sessioni.

### ⭐⭐⭐ IL NOME DEL LIBRO NON E' IL NOME DELL'INCANTESIMO: 37 SU 80, E SONO NOSTRE

La 047 aveva trovato la cosa su tre righe. Misurata invece di stimata —
`scratchpad/_118-nomi-vs-incantesimi.py`, nato qui — e' su **37 grimori su 80**,
e la misura separa due cose che sembravano una:

    il GIAPPONESE  nome del libro contro skillname   divergenti  2 su 80
    l'ITALIANO     nome dell'oggetto contro skillname divergenti 37 su 80

Le due di monte sono `:91976` (「扉生成」 contro ドア生成) e `:102031`
(「自己変容」 contro 自己の変容). **Le altre 35 le abbiamo fatte noi**: i nomi
degli oggetti e i nomi degli incantesimi sono stati resi in sessioni diverse, da
chi non aveva sott'occhio l'altra tabella, e nessuno strumento del progetto le
confronta. In giapponese il giocatore legge la stessa parola in testa al
pannello e dentro la descrizione; in italiano, 37 volte su 80, ne legge due.

⚠️ **Nel corpo si e' scritto il nome dell'INCANTESIMO**, perche' quella riga
serve a cercare la magia nella lista: col nome del libro non la si trova. Ma la
divergenza adesso si vede **nello stesso pannello**, e il rimedio vero e'
allineare i 37 nomi di oggetto allo `skillname`. E' un lavoro suo, e non lo fa
questo lotto.

ⓘ Dal solo lotto 048, tredici delle 37:

    :104519  «conoscenza»            -> **Saggezza divina**
    :105228  «pioggia sacra»         -> **Scaccia i malocchi**
    :105742  «debolezza»             -> **Nebbia di fragilità**
    :106398  «resistenza»            -> **Scudo elementale**
    :106686  «silenzio»              -> **Nebbia di silenzio**
    :112952  «vortice caotico»       -> **Vortice del caos**
    :113025  «onda di boato»         -> **Onda fragorosa**
    :113459  «ago neurale»           -> **Ago dei nervi**
    :113532  «occhio caotico»        -> **Occhio del caos**
    :113605  «sospiro infernale»     -> **Sospiro d'oltretomba**
    :114013  «freccia magica»        -> **Dardo magico**
    :114788  «cartografia magica»    -> **Mappa magica**
    :123492  «teletrasporto minore»  -> **Teletrasporto breve**

⚠️ Nessuna rete lo vede: il nome del libro e' li' nel dossier, due righe sopra
la prosa, e sarebbe bastato copiarlo per sbagliare. Il referto che le conta
tutte e 37 e' `scratchpad/_118-nomi-vs-incantesimi.py`, e va riletto quando
qualcuno decidera' di allineare i nomi.

### ⭐⭐ IL DESIDERIO E' L'UNICO 珍しい魔法書, E L'INGLESE LO PERDE

`:111850` apre con 「〜という呪文について学ぶことができる**珍しい**魔法書。」 —
un grimorio **raro**. E' l'unico degli 80 che porti l'aggettivo, ed e' il libro
del Desiderio, che nel gioco e' il piu' raro che ci sia (rango 50). L'inglese
scrive il solito «A spellbook to help you learn...» e la parola cade.

### ⚠️ UN ROVESCIAMENTO E DUE PAROLE LETTE MALE

  - ⚠️⚠️ `:129870` (il teletrasporto) — 今すぐ旅に出たいあなたに e' «per te che
    vuoi partire subito». L'inglese scrive «For those who hates traveling»: il
    **rovescio** della dedica;
  - `:128941` — 寒がり e' «chi sente il freddo». L'inglese legge «For those who
    catches the cold», il raffreddore;
  - `:106181` — 足を引っ張る e' «trattenere, ostacolare», ed e' il senso che il
    rallentamento chiede. L'inglese scrive «pull people's legs», prendere in
    giro;
  - `:113532` — 流し眼 e' l'occhiata di sottecchi, quella che si lancia di lato.
    L'inglese ne fa «people with a lot of eye problems»;
  - `:105301` — 体調の優れぬ e' «non essere in forma». L'inglese scrive «For the
    hardcore exorcists», che nel giapponese non c'e' in nessuna forma.

### ⓘ E quattro volte l'inglese butta la dedica e ne scrive una sua

`:105886` («Strangely reading this book gives you a slight adrenalin rush»),
`:114013` («Designed for beginners»), `:128868` («This tome let's off a static
discharge») e `:113459` («It makes people's eye twitch»). In tutt'e quattro il
giapponese dice 「〜なあなたに」 e parla a chi legge; l'inglese parla del libro.

### ⚠️⚠️ `_coerenza` SI ACCENDE, ED E' ATTESO

`scratchpad/lotti-109/_coerenza.py lavoro/fase5-db_item-048.jsonl` esce con **1**
e stampa:

    lo stesso GIAPPONESE, rese diverse: 1
        <ランク6魔法>
            \\"Ahi! Scotta!\\" ...
            \\"Iiih! Gela!\\" ...
            \\"Mi fanno male gli occhi, e la testa ancora di più...\\" ...

E' il caso per cui la rete esiste, girato: tre righe con lo **stesso** giapponese
e **tre inglesi diversi**, perche' il giapponese non e' una frase — e' il
tassello del rango, uguale per tutti i grimori di rango 6. Renderle uguali
cancellerebbe tre battute distinte.

ⓘ E' la forma gemella della «stesso inglese, rese diverse: 1» che la 116a aveva
gia' dichiarato attesa. Chi rilancia questa rete su questo lotto **non ripari
niente**.

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le code del lotto sono **cinque**, tutte gia' in tabella con una sola resa
italiana: `~Il Libro dei Libri: i Grimori~` (42 righe), `#un ricercatore
Eulderna che maneggia questo tomo` (3), e una a testa per `#un ricercatore
Eulderna che tiene in mano questo tomo`, `#un ricercatore Eulderna ripudiato` e
`#un incendiario in arresto`. Il cancello «titoli resi in PIU' modi» resta a
**7**.

⚠️ La forma: **6** righe su 48 hanno lo spazio prima del `\\n` — le quattro
dell'indice 1 e le due dell'indice 2 — e **nessuna** delle 48 code ha lo spazio
dopo il `#`, nemmeno le cinque il cui inglese ce l'ha. La coda italiana la
decide la tabella dei titoli, non la forma dell'inglese.
"""
