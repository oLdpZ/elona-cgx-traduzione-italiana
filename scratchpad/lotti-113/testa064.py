# -*- coding: utf-8 -*-
"""122a - Lotto 064 di `db_item.hsp`: LE COLLANE, e la categoria CHIUDE.

`FILTER_ACCESSORY_AMULET`, righe da `:62463` a `:126647`: **14 righe** — 13
dell'indice 0 e **una dell'indice 2** (`:99809`, la battuta di <Rianna>) — su 13
oggetti. Con questo lotto `FILTER_ACCESSORY_AMULET` va a **0 da fare su 14
vive**, ed e' la **diciannovesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 064`: **+14** per 14 rese,
nessuna gemella. ⓘ `_gia-reso.py 064`: 0 su 14. `_code.py 064`: 0 righe senza
resa in tabella. `_forma.py 064`: 14 su 14 con lo spazio prima del `\\n`.

### ⭐⭐⭐ L'INGLESE FONDE DUE POPOLI IN UNO, E IL TERZO NON C'ENTRA NIENTE

`:62463`, la sfera di Yekub. Il giapponese nomina **due** specie aliene:

    シャンの催眠術        l'ipnosi degli Shan
    サキュバロリンの思念吸収  l'assorbimento del pensiero dei Sakyubalorin

L'inglese scrive «Sunbararian's hypnotism and mind absorption»: **un popolo
solo**, e per giunta un **terzo** — gli abitanti di Sunbararia, quelli del lotto
063, che nella riga giapponese non compaiono affatto.

⚠️ **I due nomi giapponesi stanno in TUTTO il sorgente solo qui.** Cercati:
due occorrenze, che sono le due lingue di questa stessa riga. Quindi non sono
nomi di creature che il giocatore incontra, e il lettore giapponese e' opaco
esattamente quanto quello italiano — il che rende la trascrizione la scelta
giusta, non un ripiego. ⓘ Non e' un errore di monte come `:56267`: e' una
**semplificazione** dell'intermedio, la stessa forma di 神の間 della 121a.

### ⭐⭐ UNA PAROLA NUOVA, E IL DIZIONARIO NE AVEVA UNA SOLA

Il glossario ha 首輪 -> «collana», e l'indice 3 di questa categoria lo ripete su
tredici oggetti. Ma il **corpo** usa 装身具 — l'ornamento che si porta addosso —
e in `:99519` le due parole diverse stanno nella stessa frase:

    表面を磨き上げた**装身具**。どちらかといえば**宝飾品**というべきもの…

Le rese tengono tre parole distinte: 首輪 «collana», 装身具 «ornamento»,
宝飾品 «gioiello». ⓘ 装身具 non era nel dizionario da nessuna parte —
`_cerca.py` dice «niente» — ed e' una parola nuova di questo lotto.
⚠️ **E in `:76247` 首輪 non e' una collana ma un collare**, perche' l'oggetto si
chiama 《暴風の首輪》 -> «Collare della Tempesta» ed e' quello che il giocatore
legge in cima al pannello. La parola segue il nome, non il glossario.

### ⭐ LA TERZA RIGA DELLA FAMIGLIA 〜を守る為に作られた

    :99937 (063)  頭部を守る為に作られた防具    Un'armatura fatta per proteggere la testa.
    :99663 (064)  首を守る為に作られた装身具    Un ornamento fatto per proteggere il collo.

Trovata con `_cerca.py` **prima** di scrivere, come le due famiglie del lotto
063. E' la terza sessione di fila in cui la ricerca a mano trova quel che
nessuno strumento cerca: la richiesta della 121a — la riga sorella **per
frase** su tutto `db_item.hsp` — resta la cosa piu' utile da costruire.

### ⓘ Le decisioni minori, e da dove vengono

  - 風の神 «la dea del vento», gia' in gioco sull'arco lungo che quella dea
    dona; 御利益 e' il beneficio che viene dal divino, non un effetto qualunque;
  - ミカ (`:81536`) e' la **mica**, il minerale che si sfoglia: da li' viene la
    spirale della conchiglia. L'inglese la tiene, ed e' giusta;
  - 装着する / 装備する (`:99663`) sono due verbi che il gioco distingue
    davvero — indossare ed equipaggiare — e la riga ci gioca sopra;
  - 〜のこめられた -> «racchiuso», che e' la parola dei due indici 3 gia' in
    gioco («Una collana in cui è racchiuso un sentimento», «…il potere magico»);
  - le due collane del combattimento (`:82676`, `:82742`) si leggono in coppia,
    e i loro indici 3 dicono gia' «un attacco extra in mischia» e «…a
    distanza»: le rese ci vanno d'accordo senza ripetere le stesse parole;
  - 下賤な者達 (`:83901`) e' la gente di bassa condizione, e 札 la targhetta:
    la riga dice che il ciondolo e' un **segno di riconoscimento**, non un
    ornamento — ed e' il contrario di quel che sembra.
"""
