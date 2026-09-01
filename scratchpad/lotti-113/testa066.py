# -*- coding: utf-8 -*-
"""122a - Lotto 066 di `db_item.hsp`: I GUANTI, e la categoria CHIUDE.

`FILTER_GLOVES`, righe da `:62801` a `:130649`: **10 righe**, tutte dell'indice
0, su 10 oggetti. Con questo lotto `FILTER_GLOVES` va a **0 da fare su 10
vive**, ed e' la **ventunesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 066`: **+10** per 10 rese,
nessuna gemella. ⓘ `_gia-reso.py 066`: 0 su 10. `_code.py 066`: 0 righe senza
resa in tabella. `_forma.py 066`: 10 su 10 con lo spazio prima del `\\n`.

### ⭐⭐⭐ IL PRIMO LOTTO CON LA RETE DELLE SORELLE, E HA CAMBIATO DUE RESE

`scratchpad/_122-sorelle-per-frase.py` e' stato scritto un'ora fa, dopo che
questa sessione aveva incontrato **tre volte** una riga sorella in un altro
lotto e l'aveva trovata ogni volta a mano. Sul 066 ha risposto in due secondi e
mezzo con **sette frasi**, cinque delle quali gia' rese.

**La famiglia dei materiali speciali ha SEI membri, non tre.** Prima di oggi se
ne conoscevano due (`:100849` e `:101769`, la 121a), stamattina e' diventata
tre col lotto 063, e adesso si vede tutta:

    :100849 (058)  盾 lo scudo        reso
    :101769 (060)  鎧 la corazza      reso
    :99872  (063)  兜 l'elmo          reso
    :101114 (066)  篭手 i guanti      <- questo lotto
    :100392 (---)  腰当 la cintura    DA FARE, FILTER_GIRDLE
    :130450 (---)  靴 gli stivali     DA FARE, FILTER_BOOTS

⭐ **Le ultime due righe sono il vero risultato**: non sono un difetto trovato,
sono due lotti futuri che adesso sanno gia' con che frase devono aprire. Finora
questa cosa si scopriva **dopo**, e nella 121a il lotto 014 aveva reso una riga
in un modo che il lotto 024 aveva dovuto disfare.

**E la famiglia di 〜を守る為に作られた ha QUATTRO membri:**

    :99937  (063)  頭部を守る為に作られた防具      la testa
    :99663  (064)  首を守る為に作られた装身具      il collo
    :130582 (066)  手首から先を守る為に作られた防具  dal polso in avanti

⚠️ Questa la rete l'ha trovata solo dopo aver abbassato la soglia della frase
minima da 14 a 12 caratteri: 頭部を守る為に作られた防具 e' lungo **13**, e sotto
i 14 non entrava nemmeno nell'indice. Il conto e' stato fatto, non ipotizzato —
a 12 le frasi trovate passano da 5 a 7 e le due nuove sono tutt'e due vere,
zero rumore.

### ⭐ DUE PAROLE CHE IL GIOCATORE HA TUTT'E DUE IN INVENTARIO

篭手 e 小手 sono i **guanti d'arme**, 手袋 sono i **guanti** e basta: la
categoria contiene sia gli uni sia gli altri, e gli indici 3 gia' in gioco li
distinguono («Dei guanti d'arme duri», «Dei guanti sottili»). Le rese lunghe
tengono la stessa distinzione.
ⓘ E i guanti d'arme sono **plurali** in italiano: l'apertura della famiglia dei
materiali diventa «Dei guanti d'arme che… **hanno** ottenuto», dove lo scudo e
l'elmo dicono «ha ottenuto». Cambia l'accordo, non la frase.

### ⓘ Le decisioni minori, e da dove vengono

  - 富の神 (`:75647`) -> «la dea della ricchezza», gia' in gioco sulla statua
    che la raffigura; e' Yacatect, che nel gioco parla al femminile;
  - 火炎竜 (`:107527`) -> «il drago di fuoco», dal dizionario delle creature
    («il drago di fuoco adulto», «il cucciolo di drago di fuoco»);
  - 甲冑 (`:101114`) -> «l'armatura di piastre», la parola del lotto 060
    (`:101899`, «sovrappone le piastre alla cotta di maglia»);
  - 隕鉄 (`:62801`) non e' nel dizionario da nessuna parte: e' il **ferro
    meteorico**, e l'inglese lo dice pure. Il nome dell'oggetto — «Cesto delle
    Meteore» — e il suo indice 3, che parla gia' di uno sciame di meteore, ci
    vanno d'accordo;
  - 武骨 -> «rozzo», terza occorrenza dopo la gorgiera (064) e l'anello del
    drago d'acciaio (065);
  - `:101247` chiude con やや重いがそれでも尚余りある, che e' l'eco di
    `:100849`, lo scudo dello stesso libro: la resa riprende «rendono molto più
    di quel poco che pesano in più».

### ⓘ Il preflight ha segnalato una parola lunga, e non e' un difetto

`dall'avambraccio` (16). Vale la misura del lotto 063: il tetto vero e' il
budget da 77 del corpo impaginato, e il cancello di `_107-descrizioni-item`
legge 0 parole spezzate.
"""
