"""Aggiunge in coda a `toppe.jsonl` le toppe della 135a.

Passa da uno script e non dalla shell perche' il testo non deve MAI attraversare
un terminale: `\\b` diventerebbe un carattere di controllo, gli apostrofi
sparirebbero e i backtick si espanderebbero.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from strumenti import percorsi

NUOVE = [
    {
        "file": "custom_lib.hsp",
        "cerca": '\t\tdialog "The file " + exedir + FilePath + " does not exist."',
        "sostituisci": '\t\tdialog "Il file " + exedir + FilePath + " non esiste."',
        "motivo": (
            "custom_lib.hsp:4, dentro `GetTabbedParameter`: la finestra di "
            "errore quando manca un file di configurazione del mod. Sito fuori "
            "da lang() in un file che non ha dizionario — il dizionario non lo "
            "raggiunge, e fino alla 135a non lo raggiungeva nessuno "
            "(`strumenti.copertura`). Il messaggio e' spezzato in due letterali "
            "che si concatenano attorno al percorso, e l'italiano tiene lo "
            "stesso ordine dell'inglese: una sola toppa sulla riga li prende "
            "tutt'e due. `dialog` e' una finestra di Windows, quindi non ha "
            "vincoli di larghezza delle reti del progetto."
        ),
    },
    {
        "file": "custom_itemlist.hsp",
        "cerca": '\t\tdialog "The Item List file does not exist. Preferences will not be loaded."',
        "sostituisci": '\t\tdialog "Il file della lista oggetti non esiste. Le preferenze non verranno caricate."',
        "motivo": (
            "custom_itemlist.hsp:10: la finestra di errore quando manca "
            "`ItemList.txt`, il file che dice quali oggetti evidenziare. Sito "
            "fuori da lang() in un file senza dizionario, trovato dalla 135a "
            "con `strumenti.copertura`. ⚠️ L'ALTRA stringa del file, "
            "`\"ID\\tType\\tJName\\tEName\\tValue\"` (:49), NON si tocca: e' "
            "l'intestazione del TSV che questo stesso file scrive e poi "
            "rilegge, e tradurla romperebbe il formato. `dialog` e' una "
            "finestra di Windows, senza vincoli di larghezza."
        ),
    },
]


def main() -> None:
    percorso = percorsi.PROGETTO / "toppe.jsonl"
    testo = percorso.read_text(encoding="utf-8")
    gia = {json.loads(r)["cerca"] if isinstance(json.loads(r)["cerca"], str) else None
           for r in testo.splitlines() if r.strip()}

    da_scrivere = [t for t in NUOVE if t["cerca"] not in gia]
    if not da_scrivere:
        print("  nessuna toppa nuova: ci sono gia' tutte")
        return

    if not testo.endswith("\n"):
        testo += "\n"
    testo += "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in da_scrivere)
    percorso.write_text(testo, encoding="utf-8")
    print(f"  aggiunte {len(da_scrivere)} toppe; ora sono "
          f"{len([r for r in testo.splitlines() if r.strip()])}")


if __name__ == "__main__":
    main()
