"""La toppa della giuntura del nome composto, nel fumetto del danno.

`custom_dmgpop.hsp` spezza il nome di un PNG su due righe per mostrarlo sopra
la testa: sopra l'epiteto, sotto il nome proprio. In inglese la giuntura e'
` the ` («Arnord the mercenary»); in italiano **non c'e' piu' nessun ` the `,
perche' il contratto dei nomi (§4) dice che l'articolo lo porta il nome, e la
composizione e' `randomname() + " " + cdatan(CDATAN_NAME)` — «Arnord il
mercenario», in 152 siti di `db_creature.hsp`.

Percio' oggi il fumetto non spezza niente e scrive tutto su una riga sola.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from strumenti import percorsi

TOPPE = percorsi.PROGETTO / "toppe.jsonl"
FILE = "custom_dmgpop.hsp"
PRIMA, ULTIMA = 230, 234

NUOVE_RIGHE = [
    "    // In italiano la giuntura e' l'ARTICOLO, che il nome si porta dietro",
    "    // (\"Arnord il mercenario\"): contratto-nomi.md par. 4. Si prende quello",
    "    // che viene PRIMA nella stringa, non il primo dell'elenco.",
    "    if ( instr(s@DP, 0, \" the \") == (-1) ) {",
    "        sdim articoliIT@DP, 8, 7",
    "        articoliIT@DP = \" gli \", \" il \", \" lo \", \" la \", \" le \", \" l'\", \" i \"",
    "        giunturaIT@DP = \"\"",
    "        posIT@DP = -1",
    "        repeat 7",
    "            pIT@DP = instr(s@DP, 0, articoliIT@DP(cnt))",
    "            if ( pIT@DP != (-1) ) {",
    "                if ( posIT@DP == (-1) | pIT@DP < posIT@DP ) {",
    "                    posIT@DP = pIT@DP",
    "                    giunturaIT@DP = articoliIT@DP(cnt)",
    "                }",
    "            }",
    "        loop",
    "        if ( giunturaIT@DP != \"\" ) {",
    "            split s@DP, giunturaIT@DP, names@DP",
    "            // l'articolo resta attaccato all'epiteto: \"il mercenario\" e'",
    "            // italiano giusto, mentre l'inglese butta via il suo \"the\"",
    "            // perche' \"the mercenary\" da solo non si scrive",
    "            s@DP = names@DP(0), strmid(giunturaIT@DP, 1, strlen(giunturaIT@DP) - 1) + names@DP(1)",
    "        }",
    "    }",
]

MOTIVO = (
    "LA GIUNTURA DEL NOME COMPOSTO NEL FUMETTO DEL DANNO "
    "(custom_dmgpop.hsp:230-234). `DamagePopupNPCNameSplit` scrive il nome di "
    "un PNG su due righe sopra la testa — sopra l'epiteto, sotto il nome "
    "proprio — e per spezzarlo cerca ` the ` («Arnord the mercenary»). "
    "⭐⭐ MISURATO sulla build: nella build non esiste piu' nessun ` the ` di "
    "giuntura, perche' il contratto dei nomi §4 dice che l'articolo lo porta "
    "il nome, e la composizione italiana e' `randomname() + \" \" + "
    "cdatan(CDATAN_NAME, rc)` in 152 siti di db_creature.hsp: «Arnord il "
    "mercenario». Quindi oggi il fumetto non spezza niente e stampa tutto su "
    "una riga. ⭐ La giuntura italiana e' l'ARTICOLO, e si sceglie quello che "
    "viene prima nella stringa, non il primo dell'elenco: un nome puo' "
    "portarne piu' d'uno («Arnord il cavaliere de le rose») e la giuntura e' "
    "sempre la prima. ⚠️ L'articolo resta attaccato all'epiteto — «il "
    "mercenario» — mentre l'inglese butta via il suo «the»: «the mercenary» "
    "da solo non si scrive, «il mercenario» si'. ⚠️ Il ramo inglese resta "
    "intero e viene provato per primo: chi gioca di monte non perde niente. "
    "⚠️ Quel che questa toppa NON fa: il nome proprio senza articolo dietro "
    "(un PNG il cui nome e' un nome proprio e basta) non si spezza, come non "
    "si spezzava prima. ⓘ Fronte trovato da strumenti/operandi.py: era "
    "l'ultimo dei quattro."
)


def main():
    percorso = percorsi.SORGENTE_HSP / FILE
    righe = percorso.read_bytes().decode("cp932").split("\n")
    cerca = [r.rstrip("\r") for r in righe[PRIMA - 1:ULTIMA]]

    atteso_primo = "// If not unique, split with"
    if atteso_primo not in cerca[0]:
        raise SystemExit("l'aggancio non e' dove lo credevo: %r" % cerca[0])
    if cerca[-1].strip() != "}":
        raise SystemExit("il blocco non chiude: %r" % cerca[-1])

    toppa = {
        "file": FILE,
        "cerca": cerca,
        "sostituisci": cerca + NUOVE_RIGHE,
        "motivo": MOTIVO,
    }

    for riga in toppa["sostituisci"]:
        print(riga)

    if "--scrivi" in sys.argv:
        esistenti = TOPPE.read_text(encoding="utf-8").splitlines()
        with TOPPE.open("a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(toppa, ensure_ascii=False) + "\n")
        print()
        print("scritta: le toppe sono %d" % (len(esistenti) + 1))


if __name__ == "__main__":
    main()
