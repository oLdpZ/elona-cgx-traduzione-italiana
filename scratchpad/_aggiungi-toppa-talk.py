"""Le toppe che fanno leggere talk_it.txt, col ripiego su talk.txt.

`talk.txt` si carica in tre siti di `text.hsp`: uno dentro un `if` (due
tabulazioni, `*convert_talk`) e due al primo livello (`*spec_talk` e
`*random_talk`). I due al primo livello sono la **stessa riga identica**, quindi
vogliono `"tutte": true` — la deroga che `applica_toppe` chiede di dichiarare
quando chi scrive la toppa ha guardato tutte le occorrenze e ha deciso che
vogliono la stessa resa. Qui le ho guardate: caricano lo stesso file per lo
stesso scopo.
"""
import json
from pathlib import Path

from strumenti import percorsi

MOTIVO = (
    "Il nome del file dati e' un letterale nudo, fuori da ogni lang(): il dizionario "
    "non lo raggiunge. La toppa fa leggere talk_it.txt, che applica costruisce in "
    "build\\dati\\ dal dizionario dei file dati (dizionario/dati/talk.txt.jsonl). "
    "Il file italiano si posa ACCANTO a quello di monte invece che al posto suo, "
    "come cgx-test.exe accanto a elonapluscgx.exe. "
    "Il ramo `exist` non e' prudenza generica: la riga di monte fa noteload senza "
    "guardia, e un noteload su un file assente e' un errore di esecuzione. Senza "
    "ripiego, chi copiasse l'eseguibile senza il file dati non sentirebbe i PNG "
    "parlare inglese: vedrebbe il gioco morire. Vedi "
    "piani/2026-08-20-fase-3-file-dati.md."
)


def toppa(tab: str, tutte: bool) -> dict:
    riga = f'{tab}noteload exedir + "data\\\\talk.txt"'
    nuove = [
        f'{tab}exist exedir + "data\\\\talk_it.txt"',
        f'{tab}if ( strsize != (-1) ) {{',
        f'{tab}\tnoteload exedir + "data\\\\talk_it.txt"',
        f'{tab}}}',
        f'{tab}else {{',
        f'{tab}\tnoteload exedir + "data\\\\talk.txt"',
        f'{tab}}}',
    ]
    voce = {"file": "text.hsp", "cerca": riga, "sostituisci": nuove, "motivo": MOTIVO}
    if tutte:
        voce["tutte"] = True
    return voce


def main() -> None:
    sorgente = (percorsi.SORGENTE_HSP / "text.hsp").read_bytes().decode("cp932").splitlines()

    nuove = [toppa("\t\t", tutte=False), toppa("\t", tutte=True)]
    for t in nuove:
        quante = sorgente.count(t["cerca"])
        print(f"{t['cerca']!r} aggancia {quante} righe"
              + ("  (tutte)" if t.get("tutte") else ""))
        if quante == 0 or (quante > 1 and not t.get("tutte")):
            raise SystemExit("aggancio inatteso: la toppa non si scrive")

    percorso = Path("toppe.jsonl")
    esistenti = [json.loads(r) for r in
                 percorso.read_text(encoding="utf-8").splitlines() if r.strip()]
    cerche = {t["cerca"] for t in nuove}
    tenute = [t for t in esistenti
              if not (t["file"] == "text.hsp" and t["cerca"] in cerche)]
    rimpiazzate = len(esistenti) - len(tenute)
    tenute.extend(nuove)

    percorso.write_text(
        "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in tenute),
        encoding="utf-8", newline="\n")
    print(f"toppe: {len(tenute)} (rimpiazzate {rimpiazzate})")


if __name__ == "__main__":
    main()
