# strumenti/commenti.py
"""Le righe di un `.hsp` spente da un commento di blocco `/* ... */`.

⚠️ Nata nella 37a in `scratchpad/commenti-blocco.py`: `proc.hsp:11796` sta
dentro un blocco
`/********** ORIGINAL - BEGINNING **********  ...  ********** ORIGINAL - ENDING **********/`
— codice di monte spento dal mod BLOODYSHADE — e la **rete 6 non lo vedeva**,
perche' guarda solo le righe che cominciano per `;`. Una voce dentro un blocco
spento e' testo che il giocatore non leggera' mai.

⚠️ **Passata in `strumenti/` nella 60a**, quando a servirsene e' diventata una
rete: `larghezze.py` cammina all'indietro dal `gosub *prompt_key` per trovare il
`val =` che dichiara il riquadro, e in `map_user.hsp` ne trova **tre**, di cui
uno e' la riga di upstream tenuta in commento (`:522`). Una rete non puo'
dipendere da uno script di scratch senza test.

⚠️⚠️ **E nella 100a si e' scoperto che mancava il commento di riga `//`.** HSP3
accetta **due** commenti di riga, `;` e `//`, e il progetto ne ha sempre
guardato uno solo: `custom_autopick.hsp:200`-`:217` tiene spenti cosi' due
selettori interi, e `estrai` li estraeva come se fossero vivi. E' la **quinta
famiglia di riga morta** dopo il `;`, il blocco `/* */`, il ramo `if ( jp )` e
l'`if ( 0 )`. Misurata: 9 righe con una `lang()` in tutto il sorgente, di cui
**una gia' tradotta** (`command.hsp:17515`), cioe' lavoro speso su testo che il
giocatore non legge.
"""
from pathlib import Path


def righe_in_commento(percorso: Path | str) -> set[int]:
    """I numeri di riga (1-based) coperti da un commento di blocco.

    ⚠️ I delimitatori si cercano fuori dalle stringhe e fuori dai commenti di
    riga (`;`), se no un `/*` scritto dentro un letterale spegnerebbe meta' file.
    """
    testo = Path(percorso).read_bytes().decode("cp932", "replace").split("\n")
    dentro = False
    fuori: set[int] = set()
    for n, riga in enumerate(testo, 1):
        i = 0
        in_stringa = False
        apre_qui = False
        while i < len(riga):
            due = riga[i:i + 2]
            if dentro:
                if due == "*/":
                    dentro = False
                    i += 2
                    continue
                i += 1
                continue
            if riga[i] == '"':
                in_stringa = not in_stringa
            elif not in_stringa and riga[i] == ";":
                break
            elif not in_stringa and due == "/*":
                dentro = True
                apre_qui = True
                i += 2
                continue
            i += 1
        if dentro or apre_qui:
            fuori.add(n)
    return fuori


def colonna_commento_riga(riga: str) -> int | None:
    """La colonna del `//` che spegne il resto della riga, o `None`.

    ⚠️ Non basta cercare `//`: `"http://elona.fandom.com"` sta **dentro una
    stringa** e non spegne niente, e un `//` che viene **dopo** un `;` e' gia'
    dentro il commento di riga che il progetto guardava da sempre.

    Torna una colonna e non un booleano perche' quel che conta e' se il testo
    che interessa sta **dopo** le due barre: `x = 1 // nota` e' una riga viva
    con un commento in coda, non una riga morta.
    """
    dentro_stringa = False
    i = 0
    while i < len(riga):
        carattere = riga[i]
        if carattere == '"':
            dentro_stringa = not dentro_stringa
        elif not dentro_stringa:
            if carattere == ";":
                return None
            if riga[i:i + 2] == "//":
                return i
        i += 1
    return None


def lang_spenta_da_barre(riga: str) -> bool:
    """Vero se la riga porta una `lang()` che sta **dopo** un `//`."""
    colonna = colonna_commento_riga(riga)
    return colonna is not None and "lang(" in riga[colonna:]
