# Ripresa sessione

Aggiornato: 2026-09-02, fine della **centoventottesima** sessione (**l'ultimo
fronte aperto della 127a si chiude con due toppe, e la misura che lo diceva
grande era sbagliata: le «cinque code» stavano in codice irraggiungibile**).

⚠️⚠️⚠️ **L'ESEGUIBILE IN GIOCO E' QUELLO DELLE 17:36 DEL 02/09**, ricompilato e
ricopiato dopo le due toppe di `chara_func.hsp`. Se la data e' quella, non c'e'
niente da rifare. ⓘ Si legge con `ls -l C:\Games\Elona\elonaplus2.31\cgx-test.exe`.

⭐⭐⭐ **IL PERIMETRO `lang()` RESTA CHIUSO AL 100%.** Il conto **non si eredita
da qui** — si rilancia:

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/perimetro.py

        firme rese                              26.326
        firme ancora da fare, contate                0
        --- fatto 26.326 su 26.326            = 100,0%

---

## ⚠️⚠️⚠️ LA LEZIONE DELLA 128a: UNA PREMESSA EREDITATA VA RIMISURATA COME UN NUMERO

La 127a lasciava **una sola cosa aperta e misurata**, gli AP di
`chara_func.hsp`, e la descriveva **negli stessi termini in tre documenti** —
questa ripresa, `decisioni.md`, `invariati.md`:

> «`gain_ap_source` e' operando e testo insieme; la frase si compone **per
> ricorsione** con quattro frammenti inglesi, uno dei quali porta `his()` a un
> argomento, che e' morfologia; la strada e' una tabella al sito di stampa,
> **tre basi per cinque code**; e' una toppa a blocco di una certa dimensione e
> **vuole una sessione sua**.»

⚠️⚠️⚠️ **Le cinque code non escono mai a schermo, e il fronte erano due
toppe.** Le otto chiamate che le compongono (`:8533` `:8536` `:8540` `:8546`
`:8548` `:8553` `:8556` `:8560`) stanno **tutte dentro `gain_ap_old`**, che ha
**un chiamante solo in tutto il sorgente** — `action.hsp:8992`, con
`"destone"` — e stanno dentro `if ( gain_ap_source == "talk" )` (`:8530`) e
`if ( gain_ap_source == "kill" )` (`:8543`): li' dentro quella variabile vale
sempre `"destone"` e non e' mai riassegnata. **Codice irraggiungibile.**

⭐ **La prova stava scritta in inglese tre righe sopra la funzione viva**
(`chara_func.hsp:8342`): «*Ano made ap gain functions a lot simpler in 2.29,
but he didn't change the destone formula*». Chi ha misurato il fronte ha letto
le righe delle code e **non ha guardato chi chiama la funzione che le
contiene**.

💡 **La regola, e costa un comando.** Prima di scrivere che un fronte e' grande
si contano i **chiamanti** delle funzioni in cui vive, non le sue righe:

    grep -nE '(^|[^A-Za-z0-9_])gain_ap(_old)?\s*("|\(|\s+[A-Za-z0-9_"(])' *.hsp

Tredici righe, dodici dentro `chara_func.hsp` stesso; le tre che contano si
vedono in un colpo d'occhio. ⚠️ **Una riga si legge nel blocco; un frammento di
frase si legge nella catena di chiamata.**

---

## LE DUE TOPPE DELLA 128a, E LE TRE PAROLE CHE NON SI SONO SCELTE

I valori vivi sono **tre e fissi**:

    :8430   gain_ap      chiamata da chara_func.hsp:3991 e :4135
                         gain_ap_source vale "talk" oppure "kill"
    :8522   gain_ap_old  chiamata da action.hsp:8992
                         gain_ap_source vale sempre "destone"

| operando | prima | adesso | riscossa da |
|---|---|---|---|
| `"talk"` | «from the talk.» | «AP dalla **trattativa**» | `skill.hsp:222` (`Negotiation` -> «Trattativa»), `action.hsp:15250` e `proc.hsp:26922` («switched to talking mode!» -> «passa in assetto di trattativa!») |
| `"kill"` | «from the kill.» | «AP dall'**uccisione**» | — |
| `"destone"` | «from the destone.» | «AP dalla **pietra del risveglio**» | `db_item.hsp:134581`, 覚醒の閃石 / «awakening stone» |

⭐ **«talk» non e' il chiacchierare: e' la sconfitta per PERSUASIONE.**
`proc.hsp:2338` sfonda gli SP con `dmgtalk` e `:2340` da' esperienza in
`SKILL_NORMAL_NEGOTIATION`. «Conversazione» sarebbe stato un errore di gioco,
non di lingua.

⚠️⚠️ **E «destone» non era inglese: era un IDENTIFICATORE DI CODICE finito
dentro una frase.** `ITEM_ID_AWAKE_DESTONE` / `EFFECT_AWAKE_DESTONE`. Il
giocatore inglese legge «X obtained 3 AP from the destone.» e non ha modo di
capire che si parla della pietra che ha appena usato. Qui la traduzione non
traduce: **ripara**.

⚠️ La toppa di `:8430` e' **a blocco** perche' deve esserlo — «from the » +
operando + «.» non si rende senza spaccare le due vie, e l'operando deve
restare inglese (sette confronti lo leggono). La forma dell'`if` e' **copiata
da `:8415`-`:8419`, dentro la stessa funzione**: stesso confronto, stesso
`} else {`.

### ⚠️⚠️ UN COLLAUDO CHE SAREBBE MUTO, SCRITTO QUI PERCHE' NESSUNO LO RIPROVI

`spawn_item 1274` (la pietra del risveglio) **non fa vedere la terza riga**. La
pietra porta le statistiche della creatura da cui e' caduta in
`INV_ITEM_PARAM2`/`PARAM3`/`AMUR_CAGE` (`chat.hsp:20263`-`:20265`), e una pietra
generata dalla console li ha a zero: `gain_ap_old` esce alla soglia `>= 1000` di
`:8465` e il gioco stampa invece la riga gia' italiana di `action.hsp:8995`,
«non sembra servirgli a niente».

ⓘ **Le due righe vive** (`"talk"` e `"kill"`) si vedono invece in gioco normale,
e la condizione e' scritta a `:8393`-`:8394`: il **nemico** deve avere somma
degli otto attributi piu' vita/mana **>= 1000**, ed essere piu' veloce di chi
riceve gli AP. Un compagno debole in squadra (`add_ally 3`, il putit, livello 1)
rende la seconda condizione banale; resta da uccidere qualcosa di grosso.
⚠️ La prima condizione non si calcola dal sorgente — gli attributi si scalano
col livello a tempo di creazione — quindi uno schermo muto qui vuol dire
«nemico troppo debole», non «resa non arrivata».

---

## I VALORI DA ASPETTARSI IN APERTURA, DOPO LA 128a

    pytest                   796 passed, 6 skipped, **invariato**
    prova_identita           72/72 e 30.905, **invariato**
    applica                  30.764 sostituzioni, **invariato**
                             ⓘ chara_func.hsp: 8 -> **10** toppe
    perimetro.py             26.326 fatte, 0 da fare, 100,0%, **invariato**
    triage_nudi              **testo 60** (era 62), sigla 87, dbg 93, spenta 22
    _126-nudi-nel-ramo-jp    **57 vive**, 3 nel ramo jp
    _126-spente-da-una-costante  14 morte, e **43 VIVE DAVVERO** (erano 45)
                             ⭐ e le due che NON erano dichiarate — gli AP —
                                sono quelle chiuse oggi
    toppe                    **1.168**, e `_97-toppe-agganciate` **1.168 su 1.168**
    _126-referti-toppe       **participi 0, elisioni 0** su **907** toppe con testo
    referti                  participi 9, elisioni 0 (il dizionario, invariato)
    maiuscole                143/6/1/7/0, **invariato**

⚠️ **Nessuno di questi numeri si eredita da qui**: si rilanciano. E in chiusura
si rilancia **tutto cio' che produce un numero atteso**, dopo l'ultima modifica
ai documenti — non solo `pytest` (lezione della 112a e della 120a).

Tutto il resto e' **fermo dov'era** e vale l'elenco della 125a piu' sotto:
`_123-file-senza-dizionario` 2 firme mute, `menu_dialogo` 0 su 1.423,
`_108-accento-decomposto` 0 su 26.326, `verifica --dizionario` 112 in 19 file,
`_97-quanto-resta` 112/112/0, `_125-non-tradotte` 112/112/0, `creature`
1131/2466/0/0, `larghezze` 0, `diario` 0 su 205, `riquadri` 0 su 38 e 0 su 71,
`linguette` 0 e 0, `battute --divergenti` 13, `dati_sorgente` 7/7, `gronde` 0 su
5, `bilingui` 0, `lang-nel-ramo-jp` 21 | 0, `_96-morte-nella-build` 0, e tutti i
referti da `_107` a `_126`.

---

## ⚠️⚠️⚠️ IL FRONTE DELLE RIGHE NUDE E' FINITO: NE RESTANO 43, E SONO DICHIARATE

Il conto si rilancia in due comandi, e **non si eredita da qui**. ⚠️ **Le due
sottrazioni non si sommano a mano: la seconda parte dalla prima**, e la seconda
guarda **anche la build**, non solo il sorgente.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_126-nudi-nel-ramo-jp.py
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_126-spente-da-una-costante.py

        testo, dal triage                            60
        dentro un `if ( jp )`                         3
        dentro un `if ( FALSE )`                     14
        --- VIVE DAVVERO                             43

Le 43 sono **dichiarate in `invariati.md`** — sigle di colonne, falsi positivi
del triage, roba da modo mago, `helloworld.hsp` che non fa parte della build.
Restano nel conto solo perche' `nudi_en` e `triage_nudi` contano i letterali
**intatti**, e una riga che deve restare intatta e' indistinguibile da una che
nessuno ha guardato. ⭐ **Le uniche due che non erano dichiarate — gli AP di
`chara_func.hsp` — sono quelle chiuse oggi**, ed erano la voce «misurata e non
chiusa» che la 127a lasciava.

💡 **Chi riapre questo documento e vede «43» non ha davanti un lotto.** Ha
davanti le tre voci qui sotto.

---

## Che cosa guardare adesso: le tre cose aperte

1. ⭐⭐⭐ **Il debito di collaudo.** ~9.650 rese mai viste a schermo, e nessuno
   strumento che le conti. E' il fronte piu' grande del progetto e l'unico che
   non si chiude scrivendo codice. ⓘ Le due toppe della 128a **non sono state
   viste a schermo**, ne' le 78 della 127a, ne' le 40 della 126a.
2. ⭐⭐ **Le reti sulle toppe.** Le toppe hanno tre referti — participi,
   elisioni, caratteri a doppia larghezza — e **nessuno** che guardi il
   **glossario**, le **larghezze** o le **maiuscole**. Sono 907 toppe con testo
   dentro.
3. ⭐ **La coda nuda di una `lang()` gia' resa** (il caso `chat.hsp:17065` della
   127a): un referto che nessuno ha scritto, e che avrebbe trovato quella frase
   mozzata senza bisogno che qualcuno leggesse il blocco. ⓘ Gemello: **la resa
   che cita per nome un'etichetta che vive in una toppa**.

💡 **E una quarta, nata oggi:** nessun referto guarda se un frammento inglese
nudo stia in **codice irraggiungibile per flusso** — non `if ( FALSE )`, ma «la
funzione che lo contiene non e' mai chiamata con quel valore». Le otto code di
`gain_ap_old` sono esattamente questo, e il triage non le vede perche' non sono
`txt`/`mes`. Chi lo scrivesse toglierebbe dal conto lavoro che non esiste,
com'e' successo oggi a mano.
