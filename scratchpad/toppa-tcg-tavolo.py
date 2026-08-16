# -*- coding: utf-8 -*-
"""52a, lotto `tcg-tavolo`: l'interfaccia del gioco di carte, e gli esiti.

Il seguito di `toppa-tcg-carte.py`: li' le parole chiave sulle carte, qui il
pannello del tavolo (turno, vita, mana, mazzo, dominio), l'editor del mazzo, i
cinque esiti della partita e il menu d'importazione.

⚠️ **Due parole chiave erano sfuggite alla toppa `tutte` del lotto prima**, e il
motivo e' l'indentazione: `:887` sta dentro tre `if` annidati e `:1010` dentro
quattro, quindi la riga NON e' identica e `applica` — giustamente — non l'ha
toccata. 💡 «Identica» vuol dire identica coi tab davanti: il conteggio delle
occorrenze va letto sulla riga intera, non sul letterale.

⚠️ **«Mana» non ha una toppa**, come «Immune» nel lotto prima: in italiano si
scrive uguale. Il conteggio dei nudi continuera' a contarla fra le «da fare».

⭐ Il vocabolario del tavolo e' quello dei giochi di carte in italiano — mazzo,
cimitero, dominio — e «Page» e' «Pag.» come l'ha deciso la 50a (`text.hsp:114`).
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\tcg.hsp")
FILE = "tcg.hsp"
TESTO = SORGENTE.read_bytes().decode("cp932").splitlines()

# (riga, vecchio letterale, nuovo letterale, motivo)
LOTTO = [
    (1010, "Silenced", "Silenzio",
     "La seconda occorrenza, sfuggita alla toppa `tutte` del lotto prima perche' "
     "sta a quattro tab invece che a tre. Stessa resa, per forza."),
    (1026, "Confused", "Confusione",
     "Come sopra, e la resa e' quella delle piastrelle dell'HUD "
     "(`text.hsp:99`)."),
    (2563, "Miches from Vernis loves to play all sorts of boardgames, maybe I should ask her about this,",
     "A Miches di Vernis piacciono tutti i giochi da tavolo, forse dovrei chiedere a lei.",
     "Il suggerimento che compare quando non si hanno carte. ⚠️ L'inglese "
     "finisce con una VIRGOLA e non ci si concatena piu' niente (`:2565` apre "
     "una `chatList`): e' un refuso di monte, e l'italiano mette il punto. "
     "⚠️ Si aggiunge in coda a `:2560`, che e' una `lang()` ancora inglese "
     "perche' `tcg.hsp` non ha un file di dizionario: finche' quella non si "
     "traduce, la frase resta mista. Non e' un motivo per non fare questa — "
     "e' testo che il giocatore legge, e la coda non dipende dalla testa."),
    (2771, "Draw!", "Pareggio!",
     "⚠️ In un gioco di carte «draw» e' anche «pesca una carta», ma qui no: e' "
     "il ramo di `gameresult@tcg == 0`, cioe' la partita finita pari. Il sito "
     "lo dice, la parola da sola no."),
    (2774, "Surrendered!", "Resa!", "`gameresult@tcg == -1`."),
    (2779, "Escaped!", "Fuggito!", "`gameresult@tcg == -2`: si scappa dal duello."),
    (2784, "You Win!", "Hai vinto!", "L'esito buono."),
    (2789, "You Lose!", "Hai perso!", "L'esito cattivo."),
    (2803, "Unexpected outcome, report to developer.",
     "Esito imprevisto, da segnalare a chi ha scritto il gioco.",
     "⭐ Si traduce anche se e' un messaggio d'errore che nessuno dovrebbe "
     "vedere: sta accanto a sei righe di esito normale ed e' scritto per il "
     "giocatore, non per la console — «report to developer» e' una richiesta a "
     "lui. Diverso dal ramo di guasto di `GetTStatus`, che e' una sigla."),
    (3368, "Page ", "Pag. ",
     "Come l'ha deciso la 50a: `text.hsp:114` rende gia' «[Page]» con "
     "«[Pagina]», e nella riga di stato ci sta solo l'abbreviazione."),
    (3387, "Turn ", "Turno ",
     "Il contatore dei turni, dentro il riquadro da 88x84 px in cima al tavolo."),
    (3390, "Turn ", "Turno ", "La copia chiara sotto l'ombra nera di `:3387`."),
    (3441, "Player", "Tu",
     "⭐ «Tu» e non «Giocatore»: e' la resa che il progetto da' gia' a «Player» "
     "(`text.hsp:1932`), sta in un riquadro da 106x18 px accanto a "
     "«Avversario», e le due etichette dicono di chi e' il turno."),
    (3445, "Opponent", "Avversario", "Il gemello, dieci caratteri su 106 px."),
    (3457, "Deck\\n Editor", "Modifica\\n mazzo",
     "Il titolo dell'editor, su DUE righe (la `\\n` sta dentro il letterale) in "
     "un riquadro da 88x84. ⚠️ L'ordine si rovescia: in inglese la testa e' "
     "«Deck», in italiano il verbo — e la seconda riga tiene lo spazio davanti, "
     "che e' il rientro con cui l'originale la centra."),
    (3460, "Deck\\n Editor", "Modifica\\n mazzo", "La copia chiara sotto l'ombra."),
    (3464, "Deck ", "Mazzo ", "Le carte nel mazzo, sotto il minimo consentito."),
    (3469, "Deck ", "Mazzo ", "Sopra il massimo."),
    (3473, "Deck ", "Mazzo ", "Nella misura giusta."),
    (3478, "Life ", "Vita ", "I punti vita nell'editor."),
    (3482, "Card ", "Carte ",
     "⭐ Plurale: e' il numero di carte con cui si parte, e l'italiano non usa "
     "il singolare collettivo che l'inglese ammette."),
    (3484, "Domain * ", "Dominio * ",
     "Il dominio, che nei giochi di carte e' la terra o il colore. L'asterisco "
     "e' dell'originale e resta."),
    (4542, "Export Deck", "Esporta il mazzo", "Il menu d'importazione ed esportazione."),
    (4543, "Import Deck", "Importa il mazzo", "Il gemello."),
    (4544, "Reset Current Deck", "Azzera il mazzo di adesso",
     "⭐ «di adesso» come in `custom_ai.hsp:3475`, deciso oggi: «corrente» e' un "
     "calco, e «Current» qui vuol dire quello caricato ora."),
    (4546, "Export Card List", "Esporta l'elenco carte",
     "Non il mazzo ma tutte le carte possedute."),
]


def main() -> None:
    toppe, problemi = [], []
    # ⚠️ Certe etichette del tavolo sono disegnate DUE volte, una in nero un px
    # piu' in basso per fare l'ombra e una in bianco sopra (`:3387`/`:3390`,
    # `:3457`/`:3460`): le due righe sono identiche, quindi sono UNA toppa con
    # `tutte`, non due. Due toppe con lo stesso `cerca` si escluderebbero a
    # vicenda e `aggiungi-toppe.py` si ferma, giustamente.
    viste = {}
    for n, vecchio, nuovo, motivo in LOTTO:
        cerca = TESTO[n - 1]
        if vecchio not in cerca:
            problemi.append(f":{n} non contiene {vecchio!r}: {cerca.strip()[:70]!r}")
            continue
        resa = cerca.replace(vecchio, nuovo, 1)
        if cerca in viste:
            if viste[cerca] != resa:
                problemi.append(f":{n} stessa riga di prima ma resa diversa: "
                                f"{viste[cerca]!r} contro {resa!r}")
            continue
        viste[cerca] = resa
        quante = TESTO.count(cerca)
        for c in resa:
            if ord(c) > 0x7F:
                problemi.append(f":{n} carattere fuori ASCII: {c!r}")
        toppa = {"file": FILE, "cerca": cerca, "sostituisci": resa, "motivo": motivo}
        if quante > 1:
            toppa["tutte"] = True
            toppa["motivo"] += f" ⭐ `tutte`: la riga sta identica in {quante} punti."
        toppe.append(toppa)

    if problemi:
        for p in problemi:
            print("⚠️ ", p)
        raise SystemExit("lotto non scritto")

    print(f"{len(toppe)} toppe")
    uscita = REPO / "lavoro" / "_toppe-tcg-tavolo.jsonl"
    dati = "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in toppe).encode("utf-8")
    uscita.write_bytes(dati)

    esito = subprocess.run(
        [sys.executable, str(REPO / "scratchpad" / "aggiungi-toppe.py"), str(uscita)],
        cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    print(esito.stdout.strip() or esito.stderr.strip())


if __name__ == "__main__":
    main()
