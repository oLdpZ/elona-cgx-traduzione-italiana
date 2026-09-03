# Ripresa sessione

Aggiornato: 2026-09-03, fine della **centotrentatreesima** sessione (**il lotto
B e mezzo lotto C di `scene2.hsp`, e due nomi propri che l'italiano scriveva in
inglese**).

⭐ **L'ESEGUIBILE IN GIOCO E' FRESCO: 11:04 del 03/09**, e contiene tutte e 892
le rese delle scene. ⓘ Si legge con `ls -l C:\Games\Elona\elonaplus2.31\cgx-test.exe`.
I sei file dati non sono cambiati (solo `talk_it.txt` a meta' sessione, per le
due «Sierre»; gia' copiato).

⚠️⚠️ **L'ordine obbligato per portare le scene in gioco non cambia.**
`applica.py` rigenera l'albero di build da `sorgente/` e **cancella**
l'iniezione delle scene:

    python -m strumenti.applica            <- prima
    python -m strumenti.scene --applica    <- POI, mai prima
    python -m strumenti.compila --eseguibile
    cp .../build/2.05-custom-gx/elonapluscgx.exe .../elonaplus2.31/cgx-test.exe

⚠️ **`strumenti.installa` NON ESISTE**, e la testa di questo documento lo
scriveva lo stesso fino alla 132a, dieci righe sopra il paragrafo che lo nega.
L'ultimo passo e' una copia a mano.

---

## DOVE SIAMO: `scene2.hsp` a 892 su 1.701

    lotto A  scene 0-5      79 blocchi   ✅ CHIUSO (132a)
    lotto B  scene 7-30    239 voci      ✅ CHIUSO (133a)
    lotto C  scene 101-135 632 voci      ⏳ 558 fatte, **restano le scene
                                            132, 133, 134, 135** = 74 voci
    lotto D  scene 300-400 599 blocchi   ⬜ mai aperto

Il lotto C si riprende cosi', ed e' il primo comando della prossima sessione:

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python -m strumenti.scene --estrai 101-135
    python scratchpad/_133-mostra.py --lotto lavoro/scene2-101-135.jsonl --scene 132 133 134 135

⚠️ **`--estrai` rigenera il lotto con `it` VUOTO**: le 558 rese fatte stanno nel
**dizionario**, non nel file di lavoro, e non si perdono. Il giro e':
scrivere un `scratchpad/rese/C-132-135.json` (`{"scena.blocco": "resa"}`),
misurarlo con `_133-inserisci.py`, poi `--scrivi`, poi `scene --reimporta`.

---

## ⚠️⚠️⚠️ LA COSA CHE PESA DI PIU' DELLA 133a: UN NOME PROPRIO SI SBAGLIA COPIANDO

`Ylva` e' l'inglese. Il progetto scrive **`Irva`** in 1.058 rese (`db_item` 266,
`chat` 34, `db_card` 27...). Le **due sole** eccezioni in tutto il dizionario
erano le scene della 132a -- cioe' il lotto A, cioe' esattamente il lotto da cui
stavo per copiare la grafia, lotto dopo lotto, fino a fine fase.

**Perche' conta:** non l'ho trovato traducendo. L'ho trovato perche' stavo per
scrivere `Ylva` nel lotto C e sono andato a controllare come lo scriveva il
resto del gioco. Il modo in cui si sbaglia un nome proprio non e' inventarlo:
e' **guardare come l'ha reso chi ha tradotto prima**, che e' anche il modo in
cui un difetto di una sessione diventa una convenzione.

Tirando quel filo sono uscite altre tre grafie della stessa famiglia, e in
tutto **13 rese corrette in cinque dizionari**:

    Ylva         -> Irva            2 rese (scene2, la 132a)
    Sierre Terre -> Sierra Terre    10 rese. ⚠️⚠️ L'INGLESE SI CONTRADDICE DA
                                    SOLO: `scene2.hsp` scrive «Sierra» 8 volte,
                                    `chat.hsp` «Sierre» 7. Il giapponese
                                    (シエラ・テール) ne ha **una**
    Port Kapul   -> Porto Kapul     1 resa contro 24 gia' giuste
    Rosura       -> Lothria         un refuso di `scene2.hsp:1139`, e solo li':
                                    nello stesso file «Lothria» compare 29 volte

Ora e' un cancello: **`scene.GRAFIE`**, letto da `problemi()` per tutti e tre i
tipi di blocco, con accanto il conto che ha deciso ogni riga. ⭐ La prova al
contrario **non e' una riga inventata per far accendere il cancello**: e' la
resa del prologo com'era scritta nel dizionario fino a stamattina, parola per
parola (`test_la_grafia_inglese_di_un_nome_proprio_si_accende`).

💡 **Quello che resta aperto qui:** il cancello guarda **solo `scene2.hsp`**.
Le 11 rese sbagliate stavano negli altri dizionari, e li' una rete equivalente
non c'e'. Vedi le cose aperte.

---

## ⚠️⚠️ E `applica` GRIDAVA UN ALLARME CHE CRESCEVA

`dizionario/scene2.hsp.jsonl` sta nella cartella dei dizionari ma **non e' fatto
di firme `lang()`**: lo inietta `strumenti.scene --applica`, in un giro suo. Il
ciclo di `applica.py` lo trattava come tutti gli altri, faceva 0 sostituzioni e
contava **ogni resa nuova come «voce orfana»**.

    132a (95 rese)     ATTENZIONE: 86 voci orfane
    dopo il lotto B    ATTENZIONE: 258 voci orfane
    a fase finita      sarebbe arrivata a 1.701

**Perche' conta:** un allarme che suona sempre **e cresce** e' peggio di nessun
allarme, perche' seppellisce l'orfana VERA -- quella che dice che il monte si e'
mosso sotto una resa, che e' il motivo per cui quell'ATTENZIONE esiste. Ed e' la
stessa forma del guasto della 96a (uno strumento che segnala e va avanti), solo
piu' subdola: qui il numero **saliva**, e un numero che sale sembra informativo.

Ora `applica.py` salta quel file, con la ragione scritta accanto. Orfane: **0**.

---

## ⚠️⚠️ UN CARATTERE CHE CP932 NON SA SCRIVERE PASSAVA IL CANCELLO

Le caporali `«»` sono la punteggiatura che il progetto usa **nei documenti**, e
scriverle in una resa e' un gesto naturale: stavo per farlo nella scena 119.
`degrada()` toglie gli accenti, non le caporali; `problemi()` non guardava la
codifica; e la resa sarebbe morta molto piu' tardi, dentro `--applica`, a lotto
gia' reimportato.

    «quella cosa»   -> CP932 non lo scrive: UnicodeEncodeError
    perché          -> degrada -> "perche'" -> ok
    “virgolette”    -> CP932 LE SCRIVE, a doppia larghezza ⚠️

⭐ **Il cancello va dove si scrive la resa, non dove si costruisce l'albero.**
Ora `problemi()` prova la codifica e dice **quale** carattere non passa.
⚠️ Le virgolette curve `“”` restano un buco che il codice non puo' vedere: CP932
le scrive, ma a doppia larghezza, e la differenza si vede solo a schermo.

---

## ⭐ IL BLOCCO CHE IL PIANO TEMEVA NON HA CHIESTO NIENTE

La scena 11 blocco 8 e' il solo punto del file dove l'**inglese** sfora il
riquadro: 14 righe su un soffitto di 13. Il piano della Fase 4 prevedeva che,
non entrandoci l'italiano, si dovesse **spezzare il blocco in due `{chat_N}`** —
una decisione di struttura che il meccanismo attuale non sa nemmeno esprimere.

Non e' servito: la resa fa **11 righe**. E la ragione vale per tutta la fase:
**l'inglese di monte e' una traduzione lunga di un giapponese piu' asciutto**
(quel blocco: 690 caratteri inglesi contro 262 giapponesi), e traducendo dal
giapponese il margine si ricompra da solo. In tutto il lotto B **nessuna resa
e' fuori misura**, e il blocco a margine zero (scena 8 blocco 15, 13 righe su
13) l'ho accorciato apposta a 12 per non stare sul filo.

---

## ⭐ LO STRUMENTO CHE IL PIANO CHIEDEVA, E CHE ORA C'E'

`scratchpad/_133-attori.py <lotto>` dice, per ogni etichetta `{actor_N}`, come
il progetto ha gia' reso quel `<Nome>` **altrove nel gioco**. Sul lotto C:

    41 etichette distinte, 155 voci
    19 avevano gia' una resa decisa altrove -> si copia
    22 no -> si decide, e si scrive in scratchpad/rese/C-attori.json

E ha trovato il caso che il piano annunciava: **`<Conerly>` di `scene2.hsp` e'
il `<Conery>` di tutto il resto del gioco** (giapponese コネリー). Reso
`<Conery> il generale di Palmia`, come `db_creature` e `db_card`.

⚠️ La tabella si espande sul lotto con `_133-attori-applica.py`, che **rifiuta**
se il lotto ha un'etichetta che la tabella non copre e avvisa se la tabella ha
una riga che il lotto non usa. Le etichette non si scrivono a mano 155 volte.

---

## I COMANDI NUOVI DELLA 133a

    python scratchpad/_133-terreno.py <lotto>          conta il terreno di un lotto
    python scratchpad/_133-mostra.py --lotto L --scene 11 12   le voci in chiaro
    python scratchpad/_133-mostra.py --lotto L --attori        solo le etichette
    python scratchpad/_133-attori.py <lotto>           che cosa e' gia' deciso
    python scratchpad/_133-attori-applica.py <lotto> <tabella> <uscita>
    python scratchpad/_133-inserisci.py <lotto> <rese.json> [--scrivi]
    python scratchpad/_133-grafie.py [--scrivi]        le grafie inglesi nelle rese

---

## I VALORI DA ASPETTARSI IN APERTURA, DOPO LA 133a

    pytest                   **833 passed**, 6 skipped (erano 827: +6 sui
                             cancelli nuovi -- 4 grafie, 2 CP932)
    prova_identita           72/72 e 30.905, invariato
    scene --referto          2199 blocchi, 1701 con testo, **892 tradotte**,
                             4 righe morte, identita' OK, 0 fuori misura
    toppe                    1.182, e `applica` non stampa piu' ATTENZIONE
    perimetro (scratchpad/perimetro.py)   **27.219 fatte**, 0 da fare, 100,0%
    _97-quanto-resta         111 / 111 / 0
    verifica --dizionario    111 non tradotte, 0 da ritradurre

⚠️ **Nessuno di questi numeri si eredita da qui: si rilanciano.** E in chiusura
si rilancia tutto cio' che produce un numero atteso, **dopo** l'ultima modifica
ai documenti. ⓘ In questa sessione il primo giro di questa voce diceva «835» e
«26.900»: erano **previsioni**, non misure, e il controllo le ha smentite
tutt'e due. Un numero scritto senza averlo appena letto e' una bugia con l'aria
di un dato.

---

## Che cosa guardare adesso: le cose aperte

1. ⭐⭐⭐ **Le scene 132-135 del lotto C** (74 voci). Poi il lotto D
   (599 blocchi, scene 300-400), che e' il finale. Vedi
   `piani/2026-09-03-fase-4-scene2.md`.
2. ⭐⭐⭐ **La rete delle grafie vale solo per `scene2.hsp`.** Le 11 rese
   sbagliate che ho corretto stavano in `chat.hsp`, `db_item`, `db_race` e
   `dati/talk.txt`, dove un cancello equivalente **non c'e'**: se domani
   qualcuno riscrive «Sierre Terre» li', nessuno se ne accorge. La tabella
   `scene.GRAFIE` e' gia' pronta per essere letta da `verifica.py`.
   ⚠️ E la tabella e' **incompleta per costruzione**: ci sono cinque righe
   perche' cinque sono le grafie che mi sono capitate sotto. Un referto che
   *cerchi* le divergenze (nome inglese frequente + resa italiana diversa)
   non esiste.
3. ⭐⭐ **`Rehmido` e' ambiguo e per questo NON e' nella tabella.** L'inglese
   lo usa sia per レム・イド (la **civilta'**, → `Rehm-Ido`) sia per レミード
   (le **rovine**, → `Remido`): una sostituzione meccanica sbaglierebbe meta'
   dei casi. Serve un cancello che dica «questa parola in italiano non esiste,
   guarda il giapponese», senza proporre la sostituzione.
4. ⭐⭐ **Il debito di collaudo: ~10.542 rese mai viste a schermo**, e le 797
   di oggi non fanno eccezione. **Sono in gioco** (eseguibile delle 11:04), il
   che vuol dire che oggi basta una partita nuova per vedere il prologo e le
   scene 7-30.
5. ⭐⭐ **Il `keyrange` del riquadro di dialogo, che nessuno ha mai visto.**
   Il soffitto e' 13 con una voce di menu, 12 con due, e le due letture del
   progetto differiscono di una riga (vedi la 132a). ⚠️ **L'aperta della 132a
   si e' chiusa da sola e non nel modo giusto**: lo scatto proposto era il
   blocco inglese da 14 righe della scena 11, che ora e' italiano e ne fa 11.
   La domanda va posta altrove — un qualunque riquadro di dialogo, contando le
   voci del menu in fondo.
6. ⭐⭐ **Le quattro teste variabili senza articolo** (`JUICE`, `NECRO_PARTS`,
   `PRODUCED_BOOK`, `EVITEM`), dalla 131a. Invariata.
7. ⭐⭐ **Chi altro vive dentro l'uscita di un generatore?** Dalla 131a.
   Invariata.
8. ⭐⭐ **La rete che cerca l'operando di una SOSTITUZIONE** (`sreplace`,
   `instr`, `strmid` con un letterale). Invariata dalla 130a.
9. ⭐ **Le reti sulle toppe: ne restano fuori due** — le maiuscole del testo e
   le larghezze fuori dai menu. Invariata dalla 130a.
10. 💡 **La coda nuda di una `lang()` gia' resa** (`chat.hsp:17065`, 127a).

---

## La centotrentaduesima sessione (per storia)
