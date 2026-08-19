# -*- coding: utf-8 -*-
"""Lotto `scheda-inglesi`: i sei inglesi che restavano sulla scheda del personaggio.

Trovati dal collaudo della 68a sfogliando le quattro pagine della scheda. Sono
tutte `lang()` vere — nessuna toppa — e stanno in due file:

    command.hsp:10215  Weapon Proficiencies        l'intestazione di pagina 3
    command.hsp:10239  Resistances                 l'intestazione di pagina 3
    command.hsp:10250  Spells                      l'intestazione di pagina 4
    command.hsp:11006  ( % Damage Taken)           su OGNI riga di resistenza
    command.hsp:11010  ( Less than 1% Damage Taken)
    command.hsp:2956   " level"                    la riga «Potenza 0 level»
    screen.hsp:6631/35/38   (Heavy) (Medium) (Light)   il «Peso eq.»

⚠️ Il quarto e' il piu' visibile di tutti: «(133% Damage Taken)» compare in coda
a **ognuna** delle undici righe di resistenza, quindi undici volte in una
schermata sola.

## ⭐ Le due che si misurano da se'

`:11006` e `:11010` stanno in coda a una riga gia' lunga, e non c'e' modo di
sapere dove finisce la finestra senza aprirla. La resa italiana e' lunga
**esattamente quanto l'inglese** in tutt'e due i casi — 19 e 28 caratteri —
quindi la riga piu' lunga della schermata («Resiste a oltretomba/perdita MP.»)
resta lunga uguale, e quel che si vedeva prima e' quel che si vedra' dopo.

## ⚠️ E una che era stata rinviata «a mai» per sbaglio

`" level"` era in `rinviate.jsonl` con la motivazione «sta nel ramo `if ( jp )`,
non gira mai in italiano»: vero per l'occorrenza `:2956`, falso per `:10710`,
che e' la scheda del personaggio. Vedi `scratchpad/sblocca-livello-scheda.py`.

La resa e' **« liv.»**: la potenza di combattimento espressa come il livello di
sotterraneo a cui equivale, che e' quel che 戦力評価 misura, nel registro
compatto della colonna («45/11», «100(100)», «0%»).

## ⚠️⚠️ E il grado `°` e' un carattere a DUE BYTE

La prima resa era «° piano», per accordarsi al «pari al piano N» che il progetto
usa gia' in `text.hsp`. **`verifica` l'ha bocciata**: `°` e' U+00B0, e CP932 lo
scrive su due byte — la build inglese ne disegna uno per byte e a schermo
sarebbero uscite due lettere latine a caso.

💡 **E il controllo che questo lotto si portava dentro non l'aveva visto**: era
scritto `ord(c) > 0x2000`, una soglia inventata pensando ai trattini lunghi e
alle virgolette tipografiche, e il grado sta a 0x00B0, molto piu' in basso. La
riga qui sotto adesso chiama `doppi_byte_cp932(degrada(...))`, cioe' **la stessa
funzione che usa `verifica`**, invece di una regola somigliante. Un controllo che
somiglia a quello buono e' peggio di nessun controllo: da' la stessa quiete e non
la stessa garanzia — la lezione della 61a, *misurare la cosa e non una cosa
vicina*, applicata a un controllo invece che a una misura.

⚠️ Gli accenti si scrivono veri: e' `applica` a degradarli.
⚠️ Si compone in memoria e si scrive solo alla fine (regola della 39a).
"""
import io
import json
import os
import sys

sys.path.insert(0, os.getcwd())
from strumenti.accenti import degrada          # noqa: E402
from strumenti.verifica import doppi_byte_cp932  # noqa: E402

LOTTI = {
    "lavoro/_cmd.jsonl": {
        "Weapon Proficiencies": "Maestria nelle armi",
        "Resistances": "Resistenze",
        "Spells": "Incantesimi",
        " level": " liv.",
        " (% Damage Taken)": '" (danno subito " + keigen2 + "%)"',
        " (Less than 1% Damage Taken)": " (danno subito meno dell'1%)",
    },
    "lavoro/_scr.jsonl": {
        "(Heavy)": "(pesante)",
        "(Medium)": "(medio)",
        "(Light)": "(leggero)",
    },
}

# ⚠️ Le due code di riga devono restare lunghe quanto l'inglese: stanno in fondo
# a una riga la cui larghezza non e' misurata da nessuna rete.
PARI_A_MONTE = {" (% Damage Taken)", " (Less than 1% Damage Taken)"}

tenute = []
for percorso, rese in LOTTI.items():
    righe, fatte = [], {}
    with io.open(percorso, encoding="utf-8") as f:
        for l in f:
            if not l.strip():
                continue
            d = json.loads(l)
            if d["en"] in rese and not d["it"]:
                d["it"] = rese[d["en"]]
                fatte[d["en"]] = d
            righe.append(d)
    mancanti = set(rese) - set(fatte)
    if mancanti:
        raise SystemExit(f"{percorso}: non trovate {sorted(mancanti)}")
    tenute.extend(fatte.values())

for en in PARI_A_MONTE:
    it = next(v["it"] for v in tenute if v["en"] == en)
    # per la dinamica si confronta il testo a schermo, non l'espressione HSP
    reso = it.replace('" + keigen2 + "', "").strip('"') if it.startswith('"') else it
    if len(reso) != len(en):
        raise SystemExit(f"{reso!r} fa {len(reso)}, l'inglese {len(en)}: non pari")

USCITA = "lavoro/scheda-inglesi.jsonl"
io.open(USCITA, "w", encoding="utf-8", newline="").write(
    "\n".join(json.dumps(v, ensure_ascii=False) for v in tenute) + "\n")

doppi = sorted({c for v in tenute for c in doppi_byte_cp932(degrada(v["it"]))})
print(f"{len(tenute)} voci in {USCITA}")
print(f"caratteri a due byte: {doppi if doppi else 'nessuno'}")
for v in tenute:
    print(f"   {v['file']}:{v['riga']:<6} {v['en']!r} -> {v['it']!r}")
