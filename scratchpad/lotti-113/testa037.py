# -*- coding: utf-8 -*-
"""115a - Lotto 037 di `db_item.hsp`: GLI ATTREZZI, la coda. LA CATEGORIA SI CHIUDE.

`FILTER_ITEM_TOOL`, righe 90.000 in su: **25 righe** su 21 oggetti — 21
dell'indice 0, nessuna dell'indice 1 e 4 dell'indice 2. Con questo lotto
`FILTER_ITEM_TOOL` passa a **0 da fare su 204 vive**: e' la seconda categoria
chiusa del corpo dopo `FILTER_FURNITURE` (114a), e ci sono voluti cinque lotti,
dal 033 al 037.

⚠️ **La zona non e' un intervallo stretto**: le ultime 25 righe stanno sparse
fra `:90137` e `:122679`, e per prenderle tutte si passa `90000 200000`. Il
numero che `_corpo.py` stampa prima di scrivere e' l'unico modo di saperlo.

### ⭐⭐ TRE FAMIGLIE, E UNA E' UNA FRASE RIPETUTA QUATTRO VOLTE

  - **i quattro attrezzi di mestiere** (`:104791` gemme, `:120505`
    falegnameria, `:120571` cucito, `:122679` alchimia) hanno il giapponese
    identico a meno del mestiere, **seconda frase compresa**:
    当然ながら技術が無ければ扱うことはできない, «va da se' che senza l'abilita'
    non si puo' adoperare». Quattro rese uguali tranne il mestiere;
  - **le due coperte** (`:92934` gelo, `:92998` fuoco) sono la stessa frase con
    l'elemento cambiato, e la stessa chiusa «tutto ha un limite»;
  - **i due dischi** (`:92389` immagini, `:94601` musica) chiudono con la stessa
    frase sulla tecnica dimenticata.

⚠️ **E i due dischi non hanno la stessa spaziatura.** `:92389` mette lo spazio
prima del `\\n`, `:94601` no — due righe gemelle in tutto il resto. Il
preflight l'ha visto; leggendo il dossier non si vedeva.

### ⚠️⚠️ IL TITOLO-FONTE SBAGLIATO DELL'INGLESE ALZA IL CANCELLO A 5

`:102458` (il sacco a pelo) ha per fonte giapponese
～今日から君も冒険者・旅用マニュアル～, il manuale di viaggio. L'inglese ci
mette `~ Great Encyclopedia of North Tyris Furnitures~`, che e' la fonte di
`:88021` (il letto orientale, lotto 036) e di `:92252` (il salvadanaio, qui).

Il cancello «titoli resi in piu' modi» chiava sull'**inglese**, quindi dopo
questo lotto passa da **4 a 5**, e il quinto e'
`~ Great Encyclopedia of North Tyris Furnitures~` -> Enciclopedia dei Mobili /
Manuale di Viaggio. **Annunciato prima di misurarlo**, come il terzo nel 034 e
a differenza del quarto nel 035, che e' arrivato senza preavviso.

ⓘ I cinque sono adesso tutti e cinque appiattimenti o errori **dell'inglese**:
Gavela/Icolle, le Cianfrusaglie, Irva/Aimwell, Extra Issue, e questo. Nessuno e'
una nostra divergenza. Un **6** va guardato.

### ⓘ E l'inglese sbaglia ancora la fonte due volte, senza che nessun cancello lo veda

`:116603` (la corda robusta) porta ～巻かれる為の長いもの～ e l'inglese ci
mette di nuovo `~Battles, Dragons, Swords and Magic~`, come per la frusta e il
guinzaglio del 036. Tre righe, stesso errore di monte, stessa resa nostra:
il cancello non si accende perche' l'inglese e' lo stesso e la resa e' la
stessa. Si vede solo dal giapponese.

### ⭐ LA REGOLA DEL MESTIERE, dove il giapponese cambia parola e l'italiano deve seguirlo

Il giapponese dei quattro attrezzi non dice sempre «attrezzo»: dice ツール
(`:104791`), 道具 (`:120505`), セット (`:120571`), キット (`:122679`). Le rese
seguono — «l'attrezzo di base», «l'attrezzo di base», «il set di base», «il kit
di base» — perche' e' l'unica differenza che il giapponese si e' preso la briga
di fare in quattro righe altrimenti identiche.
"""
