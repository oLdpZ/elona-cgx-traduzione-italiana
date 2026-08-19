# -*- coding: utf-8 -*-
"""Compone lavoro/correzione-his-possessivo.jsonl: `his(x, 1)` per il GIOCATORE.

`init.hsp:1959` rende `lang("あなたの", "your")`, cioe' il possessivo che
`his(x, 1)` restituisce quando il possessore e' il giocatore. Il dizionario ci
aveva scritto **«il tuo»**, ma `name(CHARA_PLAYER)` rende **«il viandante»**
(terza persona, `init.hsp:1704`, decisione della 4a sessione): nelle frasi che
portano tutt'e due — e sono la maggioranza dei siti di `his(x, 1)` — a schermo
esce

    il viandante si sorprende e interrompe il tuo daffare.

cioe' terza e seconda persona nella stessa riga. La resa che si accorda col
registro del progetto e' **«il suo»**, che e' anche quel che il ramo dei PNG
(`:1965`, `:1971`, `:1974`) gia' dice: dopo questa correzione la funzione
restituisce la stessa forma per chiunque, ed e' giusto, perche' in italiano il
possessivo di terza persona non distingue il genere del possessore.

⚠️ Il sito che paga il prezzo e' `command.hsp:2543`, l'intestazione della pagina
dei talenti: `cnven(his(tc, 1)) + " equipment "` diventa «Il suo equipaggiamento:»
anche quando la pagina e' la tua. E' la lezione della 63a — il difetto stava
nella FAMIGLIA, non nel sito — al rovescio: qui la famiglia si accorda al
registro e un sito solo perde un po' di calore. Se un collaudo dice che quella
riga stona, si ripara li' con una toppa, non rimettendo «il tuo» a tutti.

I quattro siti che ne guadagnano subito, tutti col `name()` accanto:

    proc.hsp:8849   «... succhi il suo sangue.»
    proc.hsp:9605   «... interrompe il suo daffare.»
    proc.hsp:9631   idem
    item.hsp:3377   :3389  :3393  :3397   il lotto di oggi
"""
import io
import json
import pathlib

RIGA = 1959
NUOVA = "il suo"

radice = pathlib.Path(__file__).resolve().parent.parent
voci = []
with io.open(radice / "dizionario" / "init.hsp.jsonl", encoding="utf-8") as f:
    for riga in f:
        d = json.loads(riga)
        if d["riga"] == RIGA and d["en"] == "your":
            print("   vecchia: %r" % d["it"])
            d["it"] = NUOVA
            voci.append(d)

if len(voci) != 1:
    raise SystemExit("attesa una voce, trovate %d" % len(voci))

uscita = radice / "lavoro" / "correzione-his-possessivo.jsonl"
dati = "".join(json.dumps(d, ensure_ascii=False) + "\n" for d in voci).encode("utf-8")
with io.open(uscita, "wb") as f:
    f.write(dati)
print("   nuova  : %r" % NUOVA)
print("1 voce scritta in %s" % uscita)
