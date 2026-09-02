# Ripresa sessione

Aggiornato: 2026-09-02, fine della **centoventinovesima** sessione (**la
condizione di un rinvio smette di stare in prosa e diventa un campo che
qualcuno misura; al primo giro trova cinque cose, e una l'avevo appena
sbagliata io**).

⚠️⚠️⚠️ **L'ESEGUIBILE IN GIOCO E' QUELLO DELLE 21:23 DEL 02/09**, ricompilato e
ricopiato dopo la resa di `command.hsp:10710`. Se la data e' quella, non c'e'
niente da rifare. ⓘ Si legge con `ls -l C:\Games\Elona\elonaplus2.31\cgx-test.exe`.

---

## ⚠️⚠️⚠️ LA COSA PIU' GROSSA DELLA 129a: `condizione` E' UN CAMPO, NON UNA FRASE

La 128a lasciava **una domanda sola, marcata ⭐⭐⭐**: quanti altri rinvii hanno
una condizione che nessuno valuta? E proponeva di cercarli con un `grep` sulla
prosa.

⚠️⚠️ **Quel `grep` non funziona, ed e' la prima cosa che ho misurato.**
`INSIEME|non prima|ASSEGNA|CONFRONT` sulle 114 voci vere ne pesca **piu' di
sessanta**: «se » compare in quasi ogni `motivo`, e i termini specifici stanno
nella prosa che *spiega* il rinvio quanto in quella che lo *condiziona*.

> Un filtro che lascia passare meta' dell'insieme non e' un filtro: e' l'elenco
> completo con un passaggio in piu'. E un elenco completo di 114 voci e'
> esattamente la cosa che nessuno rilegge, cioe' il problema di partenza.

Adesso ogni voce di `rinviate.jsonl` porta
`condizione: {tipo, siti?, nota?}`, con **sette tipi**, e il tipo dice *che cosa
andare a misurare*:

    riga_morta        spenta nel sorgente: `;`, `//`, `/* */`, `if ( jp )`,
                      `if ( FALSE )`, guardia composta `& jp`
    morta_per_flusso  la riga e' VIVA, e' morto **chi la stampa**
    risolta_da_toppa  la build la cambia gia'   -> ROTTA se smette
    attende_toppa     la build la lascia intatta -> MATURA se comincia
    attende_resa      un ALTRO sito e' ancora inglese  <- la famiglia dei
                      quattro rami morti della 128a
    attende_monte     un sito e' ancora spento nel sorgente pinnato
    mai               niente puo' maturare, e pretende una `nota` che lo dica

⭐⭐ **Il vocabolario sta in `strumenti/estrai.py` (`TIPI_CONDIZIONE`) e a
pretenderlo e' `carica_rinviate`, cioe' OGNI ESTRAZIONE** — non il referto che
lo valuta. Un rinvio senza `condizione`, o con un `tipo` inventato, fa fallire
l'estrazione con un `ValueError`, come gia' il `motivo`. Una disciplina che
vive solo dentro uno script di `scratchpad/` chiede a qualcuno di ricordarsi di
lanciarlo.

⭐ **E una classificazione sbagliata si accende da sola.** Marcare `riga_morta`
una riga che e' viva non produce silenzio: produce «MATURATA», col numero di
riga. Il campo non e' una dichiarazione da credere, e' **un'ipotesi da
falsificare** — ed e' cosi' che sono usciti quattro dei cinque difetti qui
sotto, sbagliando io la prima classificazione e lasciando che fosse il referto
a dirlo.

---

## LE CINQUE COSE CHE IL PRIMO GIRO HA TROVATO

### 1. ⚠️⚠️ Un frammento inglese che il giocatore leggeva: `command.hsp:10710`

`lang("階相当", " level")` era rinviata perche' la sua **gemella** a `:2956` sta
nel ramo `if ( jp )`. Ma **il dizionario e' indicizzato per firma**, e l'altra
occorrenza vive nella scheda del personaggio — quella con «Vita, Mana, Follia,
Velocita', Fama, Karma, **Potenza**» — dove accanto a etichette tutte italiane
il gioco scriveva «0 level».

Resa **« liv.»**, come `" Lv"` -> `" liv."` di `:17435` e come dice il glossario
(`Level` -> `Livello`, abbreviato `Lv.`). ✅ **Vista a schermo** (vedi sotto).

⭐ E' la stessa forma del guasto della 128a da un altro lato: **una firma
rinviata guardando un sito solo**. Il rinvio non era sbagliato dove guardava:
era incompleto.

### 2-3. ⭐⭐ Due rinvii aspettavano una toppa CHE C'ERA GIA'

`item_func.hsp:974` (« grown ») aspettava il lotto dei modificatori di qualita'
di `contratto-nomi.md` §6: quel lotto e' stato fatto (commit «Fase 1: la taglia
e la qualita' del manoscritto») e la toppa rende « di taglia ».

`item_func.hsp:1386` (il materiale del kit) aspettava «la toppa che sposta la
concatenazione»: c'e' (commit «Il giunto del materiale non e' uno solo: sette
elidono») e nella build passa per `mtcomplemento`.

⚠️⚠️ **La ripresa della 128a dava il secondo per «ancora vero»**, avendolo
cercato a mano fra le 114 voci. Era gia' chiuso. Cercare a mano in un registro
grande da' risposte sbagliate **con la stessa faccia** di quelle giuste.

### 4. ⚠️⚠️⚠️ Una l'ho sbagliata io, nella stessa ora, nel modo che stavo correggendo

Avevo riclassificato ` Plat` come `attende_toppa` — «il ramo `else` del diario
e' inglese nudo, aspetta la toppa che lo rende» — **ricopiando la premessa dal
motivo vecchio invece di misurarla**. Il referto ha risposto MATURATA al primo
giro: quella toppa c'e' da un pezzo, tutto `command.hsp:3040`-`:3069` nella
build e' italiano («Il tuo cammino finora:», «Platino raccolto:», «Vittorie
all'Arena delle Bestie:») e la stessa toppa ha cambiato la `lang()` in « pz.».

Il motivo vecchio era falso **due volte**: diceva che la `lang()` «non viene
valutata mai» (`:3067` la valuta) e che il ramo `else` e' inglese nudo (non lo
e' piu'). ⭐ La rete ha corretto chi la stava costruendo, mezz'ora dopo che era
nata.

### 5. ⭐⭐ La SETTIMA famiglia di riga morta: la guardia composta `& jp`

`lang-nel-ramo-jp.py` riconosce solo `^if ( jp ) {`, e **lo dichiara nella
propria intestazione**: «restano fuori due guardie composte». Le nove parti del
corpo di `item_func.hsp:1034`
(`if ( inv(...) == ITEM_ID_NECRO_PARTS & jp ) {`) stanno esattamente li' sotto,
ed erano dichiarate morte nel registro **senza che niente potesse
confermarlo**.

> Una limitazione scritta in un docstring non e' una limitazione nota: e'
> visibile a chi apre quel file, cioe' a chi gia' la sa. Chi ne ha bisogno e'
> chi si fida del **risultato**, tre file piu' in la'.

Adesso il referto la riconosce, contando le graffe **fuori dalle stringhe**.
Vedi `wiki/concepts/una-limitazione-scritta-in-un-docstring-non-e-nota.md`.

---

## ⭐ IL PRIMO MODO DI MISURARE `risolta_da_toppa` ERA SBAGLIATO, E L'HA DETTO IL NUMERO

Cercavo la riga dentro il `cerca` di una toppa. Sbagliava su **sei rinvii su
ventiquattro**: una toppa puo' cercare un **frammento** invece della riga
intera, o riscrivere il blocco intorno.

La domanda vera non e' «esiste una toppa che parla di questa riga», e'
**«quel che il giocatore riceve e' ancora l'inglese del sorgente?»** — e si
risponde confrontando le **occorrenze del testo esatto** fra sorgente e build.

⚠️ **Non si confrontano i numeri di riga**: le toppe aggiungono righe, e
`map.hsp` nella build ne ha **cinque piu'** del sorgente. Si contano le
occorrenze, cosi' una riga ripetuta e cambiata in un punto solo si vede lo
stesso.

Si misura l'esito, non l'intenzione — la stessa lezione della 128a, dall'altro
lato.

---

## I DUE COMANDI, E LA PROVA AL CONTRARIO

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_129-condizioni-dei-rinvii.py
    ... --elenco     tutte le voci, tipo per tipo
    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_129-prova-al-contrario-condizioni.py

La prova al contrario prende le voci **vere** e sposta di un passo la cosa che
le tiene chiuse — il sito di una riga, la riga di un commento, il tipo di una
condizione — e pretende che il cancello si accenda. Stampa **dove** si e'
acceso, non un ✅: un esito booleano non distingue «ho trovato il guasto» da
«non l'ho cercato abbastanza» (lezione della 107a, dove la prova al contrario
c'era **ed era spenta**).

⭐ E il referto stampa **perche' lo zero e' zero**, che senza non si legge:
27 chiuse da toppa, 19 nel ramo jp, 14 morte per flusso, 11 col `;`, 11 nel
blocco `/* */`, 9 sotto `& jp`, 8 in attesa di toppa, 6 in attesa di monte,
1 `if ( FALSE )`, 1 `mai`.

---

## ⭐⭐ IL COLLAUDO: LA SCHEDA PERSONAGGIO, MAI VISTA PRIMA

Passi (verificati sul `config.txt` dell'utente, `key_charainfo. "c"`): avvia
`cgx-test.exe`, carica una partita, premi **`c`**, prima pagina.

Risultato: **«Potenza   0 liv.»**, in misura. E lo sfondo valeva piu' della
riga — quel pannello non era **mai** stato guardato a schermo, e ci sono dentro
una trentina di rese: gli otto valori in colonna, le cinque righe in basso
(Carico, Limite, Peso eq., Turni, Tempo), le tre linguette, gli otto attributi
coi loro giudizi (Enorme/Ottimo/Notevole), il profilo in quattro righe, il
riquadro «Modificatori», la barra dei tasti. **Tutte italiane, tutte in
misura.**

⚠️ **Due sospetti misurati e assolti, scritti qui perche' nessuno li rifaccia:**

- **«Turni   915 Turni»** non e' una resa doppia. Sono due siti distinti —
  l'etichetta `lang("ターン", "Turns")` a `command.hsp:10526` e il valore
  `gdata(GDATA_TURN) + lang("ターン", " Turns")` a `:10754` — e la ridondanza
  c'e' identica **in inglese e in giapponese**. Toglierla vorrebbe dire una
  resa vuota, cioe' una toppa, per un difetto di monte;
- **«Info:Adesso non ha…»** attaccati vengono dal **pannello**, non dalla resa:
  l'etichetta sta a `pos wx + 30` e il testo a `wx + 63`, trentatre' pixel, e
  l'inglese li' diceva «Desc:», **piu' largo** del nostro «Info:».

L'unica parola inglese nel riquadro e' **«Essential»** in «Modalita'
Essential», ed e' il nome proprio della modalita': lo e' anche in giapponese
(`lang("Essentialモード", …)`).

---

## I VALORI DA ASPETTARSI IN APERTURA, DOPO LA 129a

    pytest                   **798 passed**, 6 skipped (erano 796: due test nuovi)
    prova_identita           72/72 e 30.905, **invariato**
    applica                  **30.766** sostituzioni (erano 30.764: +2, le due
                             occorrenze della firma resa)
    perimetro.py             26.326 fatte, 0 da fare, 100,0%, **invariato**
    triage_nudi              testo 60, sigla 87, dbg 93, spenta 22, **invariato**
    _126-nudi-nel-ramo-jp    57 vive, 3 nel ramo jp, **invariato**
    _126-spente-da-una-costante  14 morte, **43 vive davvero**, **invariato**
    toppe                    **1.172**, e `_97-toppe-agganciate` 1.172 su 1.172
    _126-referti-toppe       participi 0, elisioni 0 su **910** toppe con testo
                             ⚠️ la 128a scriveva 911 qui e 907 nella sua bozza:
                                erano tre misure della stessa cosa prese in tre
                                momenti diversi. **910 e' il valore misurato
                                dopo l'ultima modifica.**
    _128-confronti-contro-un-nome-assegnato
                             di monte 3, aggiunti dalla traduzione 0
    _129-condizioni-dei-rinvii
                             **MATURATE 0, ROTTE 0, SENZA CONDIZIONE 0** su
                             **113** voci (erano 114: una e' diventata lavoro)
    _129-prova-al-contrario-condizioni
                             **8 famiglie su 8 si accendono**
    gemelle                  9 / 0 / 9, **invariato**
    larghezze                0 fuori misura, **invariato**
    referti                  participi 9, elisioni 0 (il dizionario, invariato)
    maiuscole                143/6/1/7/0, **invariato**
    verifica --dizionario    command.hsp **26** non tradotte (erano 27)

⚠️ **Nessuno di questi numeri si eredita da qui**: si rilanciano. E in chiusura
si rilancia **tutto cio' che produce un numero atteso**, dopo l'ultima modifica
ai documenti — non solo `pytest` (lezione della 112a e della 120a).

⚠️ **E tre contatori sono scesi di uno, perche' una rinviata e' diventata una
resa**: `verifica --dizionario` **111** in 19 file (erano 112),
`_97-quanto-resta` **111/111/0** e `_125-non-tradotte` **111/111/0** (erano
112). Lo zero che conta — «fuori dalle rinviate» — resta zero.

Tutto il resto e' **fermo dov'era** e vale l'elenco della 125a piu' sotto:
`_123-file-senza-dizionario` 2 firme mute, `menu_dialogo` 0 su 1.423,
`_108-accento-decomposto` 0 su 26.326, `creature` 1131/2466/0/0, `diario` 0 su
205, `riquadri` 0 su 38 e 0 su 71, `linguette` 0 e 0, `battute --divergenti` 13,
`dati_sorgente` 7/7, `gronde` 0 su 5, `bilingui` 0, `lang-nel-ramo-jp` 21 | 0,
`_96-morte-nella-build` 0, e tutti i referti da `_107` a `_126`.

---

## Che cosa guardare adesso: le cose aperte

1. ⭐⭐⭐ **Il debito di collaudo.** ~9.650 rese mai viste a schermo, e nessuno
   strumento che le conti. E' il fronte piu' grande del progetto e l'unico che
   non si chiude scrivendo codice. ⓘ Oggi ne e' stato pagato un pezzo — la
   scheda personaggio — ma le due toppe della 128a, le 78 della 127a e le 40
   della 126a **non sono state viste a schermo**.
2. ⭐⭐ **Le reti sulle toppe.** Le toppe hanno tre referti — participi,
   elisioni, caratteri a doppia larghezza — e **nessuno** che guardi il
   **glossario**, le **larghezze** o le **maiuscole**. Sono **910** toppe con
   testo dentro.
3. ⭐ **La coda nuda di una `lang()` gia' resa** (il caso `chat.hsp:17065` della
   127a): un referto che nessuno ha scritto, e che avrebbe trovato quella frase
   mozzata senza bisogno che qualcuno leggesse il blocco. ⓘ Gemello: **la resa
   che cita per nome un'etichetta che vive in una toppa**.
4. 💡 **Il frammento inglese in codice irraggiungibile per flusso ha una casa,
   non una rete.** Il tipo `morta_per_flusso` copre le **14 voci dichiarate**
   (le sigle di `item_func.hsp:2474`, che si compongono davvero mentre il
   `mes s(cnt)` che le stamperebbe e' commentato a `:2485`-`:2491`), ma nessuno
   **cerca** quella famiglia. Le otto code di `gain_ap_old` della 128a erano
   esattamente questo, e il triage non le vede perche' non sono `txt`/`mes`.
   ⭐ Adesso pero' c'e' un appiglio che prima non c'era: le 14 dichiarate dicono
   **che forma ha** il difetto da cercare.
5. 💡 **Nato oggi: la gemella viva di una firma rinviata.** Il difetto n. 1 —
   una firma morta in un sito e viva in un altro — l'ha trovato il referto
   **per caso**, perche' pretende che *tutte* le occorrenze siano spente. Un
   referto che lo cercasse di proposito guarderebbe tutte le 113 voci e non
   solo quelle marcate `riga_morta`: le altre sei famiglie non contano le
   occorrenze, e una gemella viva li' dentro non si vedrebbe.
