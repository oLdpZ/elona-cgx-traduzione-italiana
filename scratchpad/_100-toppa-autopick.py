"""La toppa che fa copiare autopick_it.txt, con il ripiego su autopick.txt.

La quarta della famiglia, dopo board.txt (init.hsp), talk.txt (text.hsp) ed
exhelp.txt (help.hsp) — ma il sito e' di un'altra specie, e vale la pena dirlo.

⚠️⚠️ **Qui il file non si LEGGE: si COPIA nel salvataggio.**
`custom_autopick.hsp:39`-`:44` e' `AutoPickWriteDefaultSettingsFile`, che fa
`noteload` del modello di `data\\` e subito `notesave` in
`save\\<id>\\autopick.txt`. Quel che il gioco legge dopo e' **la copia**, e la
copia nessuna build la riscrive (`:26` la fa solo se non c'e'). ⚠️ La
conseguenza sta nelle note di rilascio, non nel codice: chi ha gia' giocato ha
gia' la sua copia inglese, e per lui il modello nuovo non cambia niente — deve
cancellarla, o riscriverla a mano. Piu' tardi si fa, piu' copie vecchie ci sono.

⚠️ Il ramo `exist` non e' prudenza generica: `noteload` su un file assente e' un
errore di esecuzione, e qui morirebbe alla **creazione del personaggio**, cioe'
nel punto peggiore possibile.
"""
import json
from pathlib import Path

from strumenti import percorsi

FILE = "custom_autopick.hsp"
RIGA = '\tnoteload exedir + "data\\\\autopick.txt"'

NUOVE = [
    '\texist exedir + "data\\\\autopick_it.txt"',
    '\tif ( strsize != (-1) ) {',
    '\t\tnoteload exedir + "data\\\\autopick_it.txt"',
    '\t}',
    '\telse {',
    '\t\tnoteload exedir + "data\\\\autopick.txt"',
    '\t}',
]

MOTIVO = (
    "Il nome del file dati e' un letterale nudo, fuori da ogni lang(): il dizionario "
    "non lo raggiunge. La toppa fa copiare autopick_it.txt, che dati_applica costruisce "
    "in build\\dati\\ dal dizionario dei file dati (dizionario/dati/autopick.txt.jsonl). "
    "E' la quarta della famiglia, dopo board.txt (init.hsp:2574), talk.txt (text.hsp) "
    "ed exhelp.txt (help.hsp:227), e come loro posa il file italiano ACCANTO a quello "
    "di monte invece che al posto suo. "
    "MA IL SITO E' DI UN'ALTRA SPECIE: qui il modello non si legge, si COPIA nel "
    "salvataggio (AutoPickWriteDefaultSettingsFile, :39-:44), e quel che il gioco legge "
    "poi e' la copia in save\\<id>\\autopick.txt, che nessuna build riscrive (:26 la fa "
    "solo se non c'e'). Quindi la toppa aggiusta i personaggi NUOVI; per quelli vecchi "
    "serve una riga nelle note di rilascio. "
    "E la toppa senza la traduzione delle 78 chiavi di questo stesso file non servirebbe "
    "a niente, ne' il contrario: vedi decisioni.md 98a, il guasto peggiore sta a meta'. "
    "Il ramo `exist` porta il ripiego, non il nome: noteload su un file assente e' un "
    "errore di esecuzione, e questo gira alla creazione del personaggio."
)


def main() -> None:
    sorgente = (percorsi.SORGENTE_HSP / FILE).read_bytes().decode("cp932").splitlines()
    quante = sorgente.count(RIGA)
    print("la riga cercata:", repr(RIGA))
    print("aggancia il sorgente pinnato:", quante, "volte")
    if quante != 1:
        raise SystemExit("la toppa deve agganciare esattamente una riga")

    percorso = Path("toppe.jsonl")
    esistenti = [json.loads(r) for r in
                 percorso.read_text(encoding="utf-8").splitlines() if r.strip()]

    toppa = {"file": FILE, "cerca": RIGA, "sostituisci": NUOVE, "motivo": MOTIVO}
    rimpiazzate = 0
    tenute = []
    for vecchia in esistenti:
        if vecchia["file"] == FILE and vecchia["cerca"] == RIGA:
            rimpiazzate += 1
            continue
        tenute.append(vecchia)
    tenute.append(toppa)

    percorso.write_text(
        "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in tenute),
        encoding="utf-8", newline="\n")
    print(f"toppe: {len(tenute)} (rimpiazzate {rimpiazzate})")


if __name__ == "__main__":
    main()
