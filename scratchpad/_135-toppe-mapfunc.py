"""L'editor di mappe: i widget Win32 di `map_func.hsp`.

⚠️ Resta fuori di proposito il filtro delle 26 categorie di :2517
(«All items\\nFurniture\\nJunk\\n...»): quella lista fisserebbe i nomi italiani
delle categorie di oggetto, e il progetto non ce li ha ancora — `categorie.py`
legge la classe che il sorgente DICHIARA (`FILTER_ITEM_FOOD`...), non un nome
da mostrare. Inventarli qui vorrebbe dire deciderli in un attrezzo laterale e
poi trovarseli addosso nell'interfaccia del gioco.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from strumenti import percorsi

MOTIVO_MENU = (
    "Una voce del menu Win32 dell'editor di mappe (`AppendMenuA`, :1918-:1933). "
    "Sono widget del sistema operativo, non finestre di Elona: la larghezza la "
    "decide Windows, e le reti del progetto sulle larghezze non le riguardano. "
    "«PNG» e' la sigla che il progetto usa per «personaggio non giocante»."
)

RESE = [
    ("map_func.hsp", 1857, [
        ("Unsaved data will be lost. Create a new map?",
         "I dati non salvati andranno persi. Vuoi creare una mappa nuova?")],
     "La conferma prima di buttare via una mappa non salvata, nell'editor. "
     "⚠️ E' un `dialog` con secondo argomento 3, cioe' Si'/No: la resa dev'essere "
     "una domanda, o i due pulsanti non hanno senso."),
    ("map_func.hsp", 1896, [
        ("Shift + Left Click = Replace all the same tiles in the map with the "
         "tile currently selected.",
         "Maiusc + clic sinistro = sostituisce nella mappa tutte le caselle "
         "uguali con quella selezionata."),
        ("Coast Check Button = Check the box to automatically generate coast "
         "around tiles surrounded by sea(#264).",
         "La casella Costa automatica = spuntala per generare da sola la costa "
         "attorno alle caselle circondate dal mare (#264).")],
     "La guida della modalita' mappa, che si apre da «Guida alla modalita' "
     "mappa» (:1918). ⚠️ La seconda riga NOMINA la casella di spunta di :2513: "
     "le due rese devono usare la stessa parola, o la guida rimanda a un "
     "comando che a schermo si chiama in un altro modo. `#264` e' l'indice "
     "della casella di mare e resta un numero."),
    ("map_func.hsp", 1918, [("Map Mode Help", "Guida alla modalita' mappa")], MOTIVO_MENU),
    ("map_func.hsp", 1921, [("Map Mode", "Modalita' mappa")], MOTIVO_MENU),
    ("map_func.hsp", 1922, [("Item Mode", "Modalita' oggetti")], MOTIVO_MENU),
    ("map_func.hsp", 1923, [("NPC Mode", "Modalita' PNG")], MOTIVO_MENU),
    ("map_func.hsp", 1924, [("Object Mode", "Modalita' strutture")],
     MOTIVO_MENU + " ⚠️ «Object» non e' «Item»: nell'editor sono due modalita' "
     "diverse e vicine (:1922 e :1924), e in italiano devono restare "
     "distinguibili a colpo d'occhio. Gli `object` di Elona sono porte, "
     "altari, insegne — quel che sta FISSO sulla mappa — da cui «strutture»."),
    ("map_func.hsp", 1928, [("Save Map", "Salva mappa")], MOTIVO_MENU),
    ("map_func.hsp", 1929, [("Save Map as...", "Salva mappa con nome...")], MOTIVO_MENU),
    ("map_func.hsp", 1931, [("Load Map", "Carica mappa")], MOTIVO_MENU),
    ("map_func.hsp", 1933, [("New Map", "Nuova mappa")], MOTIVO_MENU),
    ("map_func.hsp", 2513, [("Auto Coast", "Costa automatica")],
     "L'etichetta della casella di spunta dell'editor (`chkbox`, :2513). "
     "⚠️ La guida di :1896 la nomina: le due rese vanno tenute insieme."),
]


def _riga(nome_file: str, numero: int) -> str:
    testo = (percorsi.SORGENTE_HSP / nome_file).read_bytes().decode("cp932")
    return testo.split("\n")[numero - 1].rstrip("\r")


def main() -> None:
    nuove = []
    for nome_file, numero, coppie, motivo in RESE:
        riga = _riga(nome_file, numero)
        nuova = riga
        for inglese, italiano in coppie:
            if inglese not in nuova:
                raise SystemExit(f"{nome_file}:{numero}: non trovo {inglese[:60]!r}")
            nuova = nuova.replace(inglese, italiano)
        if nuova == riga:
            raise SystemExit(f"{nome_file}:{numero}: la toppa non cambia niente")
        nuove.append({"file": nome_file, "cerca": riga,
                      "sostituisci": nuova, "motivo": motivo})

    percorso = percorsi.PROGETTO / "toppe.jsonl"
    testo = percorso.read_text(encoding="utf-8")
    gia = set()
    for r in testo.splitlines():
        if r.strip():
            c = json.loads(r)["cerca"]
            if isinstance(c, str):
                gia.add(c)
    da_scrivere = [t for t in nuove if t["cerca"] not in gia]
    if da_scrivere:
        if not testo.endswith("\n"):
            testo += "\n"
        testo += "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in da_scrivere)
        percorso.write_text(testo, encoding="utf-8")
    print(f"  toppe nuove: {len(da_scrivere)} (di {len(nuove)})")


if __name__ == "__main__":
    main()
