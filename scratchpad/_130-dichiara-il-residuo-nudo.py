# -*- coding: utf-8 -*-
"""Aggiunge a `invariati.md` la sezione che dichiara le ultime 18 righe nude.

Il testo si scrive da qui e non a mano perche' e' lungo e pieno di caratteri
che una shell rovinerebbe. Idempotente: se il titolo c'e' gia', non riscrive.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_130-dichiara-il-residuo-nudo.py
"""
import io
import sys

from strumenti import percorsi

TITOLO = "## Le ultime diciotto righe nude, e la parola che non si tocca — 130ª"

SEZIONE = """

""" + TITOLO + """

Chiudendo le quattro righe vive che restavano (`init.hsp:537`, `quest.hsp:782`,
`text.hsp:11912` e `:12104`), il fronte delle righe nude di classe `testo`
scende a **56**, e quel che resta **non è lavoro rimandato**. Sono diciotto, in
cinque classi, e nessuna è una frase che il giocatore legga in inglese.

⚠️⚠️ **Il conto non scenderà mai a zero, ed è per costruzione:** `triage_nudi` e
`nudi_en` contano i letterali **intatti**, e una riga che deve restare intatta è
indistinguibile da una che nessuno ha guardato. È la stessa ragione già scritta
per `net.hsp:263` e per le diciotto della 127ª. Il numero che si legge è il
**residuo** di `scratchpad/_130-residuo-delle-righe-nude.py`, che incrocia le
righe coi siti nominati qui, in `decisioni.md` e in `rinviate.jsonl`.

### ⚠️⚠️⚠️ `init.hsp:536`, `return "user"` — un OPERANDO, non una parola

**Non si traduce, e tradurla non darebbe nessun errore.** Quella stringa è quel
che due `sreplace` **cercano**: `item_func.hsp:967` e `:1073` prendono il nome
composto dell'oggetto — carte, statuette, parti di creatura — e vi sostituiscono
la parola «user» col nome del PNG personalizzato, che arriva da
`getcnpcnamebychecksum`. Renderla «utente» spegnerebbe tutt'e due i siti **in
silenzio**: il giocatore leggerebbe per sempre il segnaposto invece del nome.

⭐ È la famiglia della 128ª — un ramo ucciso dalla traduzione perché è cambiata
la stringa **confrontata** e non quella **assegnata** — vista da un lato che
nessuna rete guarda: `_128-confronti-contro-un-nome-assegnato.py` cerca
`X == lang(J, E)`, e un `sreplace` non è un confronto.

⚠️ **Misurato il 2026-09-03, e oggi i due rami sono vivi:** nella build
`db_creature.hsp:97539` torna ancora `lang("user", "user")`, cioè il nome della
creatura `CREATURE_ID_USER` non è tradotto. Il giorno in cui un lotto di
`db_creature.hsp` lo renderà, i due `sreplace` moriranno **senza che niente lo
dica**. ⓘ Il rimedio, quando quel lotto arriverà, è la forma già usata per «Your
Home» (42ª) e per i quattro rami della 128ª: si allarga il sito che cerca, non
si tocca il nome.

ⓘ `init.hsp:537` è invece **testo**, ed è stata resa: «utente sconosciuto». Le
due righe adiacenti stanno nella stessa funzione e vogliono trattamenti opposti
— è esattamente la distinzione fra sigla e parola, portata sul confine più
sottile che il progetto abbia incontrato.

### Cinque righe di un pluralizzatore già spento

**`item_func.hsp:1894`, `:1905`, `:1915`, `:1918`, `:1921`** — `"es"`, `"ves"`,
`"ies"`, `"coffins"`: il pluralizzatore inglese dei nomi di oggetto
(`BLOODYSHADE CUSTOM`, 91 righe e 47 `case ITEM_ID`). ⚠️ **È già codice morto**:
una toppa cambia la sua guardia in `if ( 0 )`, e il plurale italiano arriva da
`ioriginalnamerefplur`, dove il nome si concatena — `contratto-nomi.md` §4-bis.
Le righe restano nel conto perché la toppa ha cambiato **la guardia**, non loro.

### Otto nomi di campo di un file, non di una schermata

**`map_rand.hsp:692`-`:699`** — `area[…];`, `Rdtype[…];`, `mobdensity[…];` e
compagnia, scritti con `noteadd` dentro `mapinfo_%06d.txt` e salvati su disco
(`notesave`, `:700`). Stessa classe del TSV di `custom_itemlist.hsp:49`
dichiarato nella 127ª: sono **nomi di campo**, e chi apre quel file lo apre per
leggere i parametri di generazione di una mappa, non una frase.

### Due righe nel ramo `if ( jp )`

**`system.hsp:3521`** (`Contributor MSL / View the credits for more`) e
**`system.hsp:3537`** (le voci del menu iniziale, alternate al giapponese) —
stanno tutt'e due dentro `if ( jp )`. I gemelli vivi sono `:3524` e `:3540`, e
sono **già italiani**. Lo stesso vale per **`item_func.hsp:1020`** (`"No."`),
dentro l'`if ( jp )` di `*itemNameSub`.

### Tre righe di servizio

**`item_data.hsp:339`, `s = "error:" + val + "/" + val(1)`** — il valore di
ripiego di `*item_encdetail`, sovrascritto poche righe sotto quando
l'incantamento si riconosce. Se il giocatore lo vede, sta guardando un difetto:
tradurlo ne nasconderebbe la natura a chi lo segnala. È la stessa scelta dei
messaggi di `dbg_*`.

**`main.hsp:3258`, `txt "lv:" + gdata(GDATA_LEVEL)`** — dentro il tasto **F7**
del modo mago (`// Wizard F7 reload/regen map`), che rigenera la mappa. Testo
che esiste solo per chi sviluppa, come `screen.hsp:1125` e `system.hsp:4400`.

**`map_rand.hsp:691`** — la nona riga dello stesso dump, già nominata altrove.
"""


def main() -> int:
    percorso = percorsi.PROGETTO / "invariati.md"
    testo = io.open(percorso, encoding="utf-8").read()
    if TITOLO in testo:
        print("la sezione c'e' gia': non riscrivo")
        return 0
    io.open(percorso, "w", encoding="utf-8", newline="\n").write(
        testo.rstrip("\n") + "\n" + SEZIONE.lstrip("\n"))
    print("sezione aggiunta a invariati.md (%d caratteri)" % len(SEZIONE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
