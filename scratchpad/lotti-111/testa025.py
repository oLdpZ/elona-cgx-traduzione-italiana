# -*- coding: utf-8 -*-
"""111a - Lotto 025 di `db_item.hsp`: LA CODA, e l'indice 3 si chiude.

`description(3)`, tutto quel che resta: **25 righe del sorgente, 23 firme**,
sparse in nove categorie minuscole piu' una voce che categoria non ha.

⚠️ **Lo scheletro non l'ha fatto `_107-chiavi-item.py`**, che seleziona per
categoria: l'ha fatto `lotti-111/_coda.py`, che prende lo scheletro intero
dell'indice 3 dallo strumento di sempre — cosi' i filtri restano gli stessi — e
tiene solo le righe che nel dizionario non hanno ancora una resa.

💡 **E la prima versione di `_coda.py` diceva «l'indice 3 e' chiuso» quando
restavano venticinque righe**, perche' cercava nel dizionario le voci con
l'italiano **vuoto**: quelle righe nel dizionario non ci sono affatto, e il
conto giusto e' il **positivo** — le righe che una resa ce l'hanno gia'. Un
elenco vuoto non e' una risposta.

### ⭐ TRE FAMIGLIE, E SI SCRIVONO IN FILA

**Le munizioni**, 「〜と共に装備する武器だ」, quattro righe in tre firme:

    銃と共に装備する武器          -> insieme a un'arma da fuoco   (:96637, :126989)
    銃と共に装備する武器（拳銃専用）-> ... (solo pistole)          (:65950)
    弓と共に装備する武器          -> insieme a un arco            (:127065)
    機械弓と共に装備する武器      -> insieme a una balestra       (:98728)

**I resti di creatura**, 「生物の〜だ」, cinque righe: osso, cuore, occhio,
sangue, pelle — i **nomi** degli oggetti, gia' resi. ⓘ `:108708` e' 体液, un
umore del corpo, e l'oggetto si chiama gia' «sangue»: si segue il nome.

**L'acqua**, tre righe che il giapponese distingue e l'inglese no:

    水を使用する設備。何度か飲むことができる。 -> che usa l'acqua, più volte
    水を湛える設備。飲むことができる。         -> che raccoglie l'acqua
    聖なる水を湛えた井戸。飲むことができる。   -> un pozzo pieno d'acqua santa

⚠️ L'inglese scrive **«(Re-drinkable) facility that supplies water»** su tutt'e
tre, gabinetto compreso. Il giapponese dice 使用する (la usa) contro 湛える (la
raccoglie) e 何度か (qualche volta) contro il bere semplice. Si segue il
giapponese, e le tre righe restano tre.

### ⭐ 飲むことができる ERA GIA' «SI PUO' BERE»

Due volte nel dizionario. 食べることができる non c'era: prende la stessa forma,
«Si può mangiare». Come 読むことができる «Si legge» della 108a.

### ⚠️⚠️ `:131247` — LA VOCE CHE NON ESISTE

`ITEM_ID_DUMMY` (il lingotto d'oro) ha il **giapponese vuoto** e l'inglese dice
letteralmente «not used in the game». Non e' un'estrazione rotta: e' cosi' nel
sorgente. Resa **«Non è usato nel gioco.»**, cioe' l'inglese, perche' li'
l'inglese e' l'unica fonte che c'e' e quel che dice e' vero.

💡 E' la stessa voce che nella 110a aveva fatto sbagliare `_coerenza.py`: il
giapponese vuoto raggruppava trenta voci che di comune avevano solo il non
avere una fonte.
"""
