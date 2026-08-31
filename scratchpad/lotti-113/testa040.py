# -*- coding: utf-8 -*-
"""115a - Lotto 040 di `db_item.hsp`: GLI SCARTI, la coda. LA CATEGORIA SI CHIUDE.

`FILTER_JUNK`, righe 76.000 in su: **29 righe** su 27 oggetti — 26 dell'indice
0, nessuna dell'indice 1 e 3 dell'indice 2. Con questo lotto `FILTER_JUNK` passa
a **0 da fare su 124 vive**: e' la terza categoria chiusa del corpo dopo il
mobilio (114a) e gli attrezzi (115a), e ci sono voluti tre lotti, dal 038 al 040.

⚠️ Come per il 037, la coda di una categoria **non e' un intervallo stretto**:
le ultime 29 righe stanno sparse fra `:86735` e `:128235`.

### ⭐⭐ LE TRE OSSA SONO UNA FAMIGLIA, E IL GIAPPONESE LO DICE DUE VOLTE

`:116408` (animale), `:127669` (umane), `:127731` (di qualcosa) hanno la stessa
identica seconda frase — «di occasioni per usarle ce n'e' parecchie... ma ce
n'e' talmente tante che come valore non contano niente» — e cambia solo di chi
sono le ossa. Tre rese uguali tranne la prima riga.

ⓘ L'inglese qui e' fedele: traduce tre volte la stessa frase in tre modi
leggermente diversi, ma non aggiunge e non toglie niente.

### ⭐ IL NOME DELL'OGGETTO E' LUNGO 15 CARATTERI, E LO SI SCRIVE LO STESSO

`:91460` e' lo spaventapasseri di neve, e «spaventapasseri» misura **15**
caratteri: uno in piu' della finestra di rinculo. Il preflight lo segnala.

Si scrive lo stesso, per due ragioni misurabili: il contratto dei nomi (107a)
vuole che la prosa nomini l'oggetto col nome che il giocatore vede, e la parola
sta **all'inizio** della riga (caratteri 5-19), lontano dal confine dei 70 dove
l'impaginatore spezza. ⚠️ La prova non e' il ragionamento ma il cancello: se
`_107-descrizioni-item` avesse detto «parole spezzate introdotte: 1», la frase
andava riscritta. Ha detto 0.

ⓘ Nella riga gemella `:112817` (lo spaventapasseri normale) la parola **non
c'e'**, e non e' una svista: il giapponese li' dice 農地の守護者, «il guardiano
dei campi», e non usa il nome dell'oggetto. Si segue il giapponese.

### ⭐ LA QUINTA RIGA DEL CORPO SENZA GIAPPONESE

`:116915` — la battuta sul pezzo di minerale — ha il giapponese **vuoto** e un
inglese vero, come `:50410` (034), `:72552` (035), `:80994` e `:84969` (036).
Fanno **cinque su 694 rese del corpo**, e sono tutte e cinque righe di indice 2.

Il conto continua a comportarsi come previsto nel 036: cresce piano, una ogni
lotto o due, ed e' compatibile con l'ipotesi che siano aggiunte del CGX scritte
direttamente nel ramo inglese.

### ⓘ Il verso della battuta del cane

`:127733` e' 「う～、わんわん！わん！　…くぅん」, dove くぅん e' il guaito
sommesso del cane. L'italiano scrive «...mugolio» e non «...guaìto» per una
ragione di codifica, non di gusto: l'accento in mezzo alla parola `degrada()`
lo trasforma in apostrofo e la parola si spacca. E' la stessa lezione di «dei»
nel lotto 035, applicata **prima** invece che dopo il rifiuto.
"""
