# -*- coding: utf-8 -*-
"""52a, lotto `ai-menu`: le 28 righe che restano di custom_ai.hsp.

Il seguito di `toppa-ai-tabelle.py`: li' le sei tabelle e la schermata
principale, qui le cinque routine che restavano — il riquadro di stato
(`PrintAIInfo`), il menu d'insegnamento, quello di configurazione, quello della
singola tattica e le due domande delle altre impostazioni.

⭐ **E una correzione a una toppa di poche ore fa.** L'intestazione della prima
colonna era «Chi», che regge da sola ma non regge la voce di menu che ci si
appoggia: «Cambia chi.» non e' italiano. Diventa «Soggetto» — 8 caratteri in
100 px, ci sta comodo — e la voce diventa «Cambia il soggetto.». 💡 E' la stessa
regola delle «due letterali per riga» della 51a vista da un altro lato: due
righe diverse che parlano della stessa cosa vanno decise insieme, anche quando
stanno in routine diverse.

⚠️ `him(tc)` a `:1191` e' morfologia inglese a un argomento — restituisce «him»,
«her» o «it» nudi (`strumenti/funzioni.py`, e il punto 3 della ripresa della
51a). La resa italiana lo toglie dal sito: «Fai dimenticare una magia o
un'abilita'.» non ha bisogno del pronome.
"""
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SORGENTE = Path(r"C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\custom_ai.hsp")
FILE = "custom_ai.hsp"

TESTO = SORGENTE.read_bytes().decode("cp932").splitlines()

# La toppa gia' scritta da correggere: (cerca, nuova resa, nota da aggiungere)
CORREZIONE = (
    '\tdisplay_topic "Entity", wx + 28, wy + 30',
    '\tdisplay_topic "Soggetto", wx + 28, wy + 30',
    " ⚠️ CORRETTA poche ore dopo, nello stesso giorno: diceva «Chi», che regge da "
    "sola ma non regge la voce di menu che ci si appoggia — `:1692` dice «Cambia "
    "il soggetto.», e «Cambia chi.» non e' italiano. «Soggetto» fa 8 caratteri e "
    "la colonna e' 100 px: ci sta comodo, e l'inglese ne faceva 6.",
)

LOTTO = [
    # --- PrintAIInfo: il riquadro di stato, a wx + 400 su 680, cioe' ~240 px
    (1043, '\t\ts = "Ora usa l\'IA personalizzata."',
     "Il riquadro di stato in alto a destra, `pos wx + 400` su una finestra di "
     "680: restano ~240 px, cioe' una quarantina di caratteri a corpo 11. Questa "
     "ne fa 27. «IA personalizzata» e' deciso dalla 51a."),
    (1046, '\t\ts = "Ora usa l\'IA normale."',
     "Il ramo opposto. ⭐ «default» e' «normale» e non «predefinita»: e' l'IA che "
     "il gioco usa quando nessuno ha configurato niente, e «normale» e' la parola "
     "che il giocatore legge altrove per la stessa idea."),
    (1050, '\ts = "Posti disponibili: " + CAIAvailableSlots(tc)',
     "Quante tattiche si possono impostare: il numero di righe della tabella. "
     "⚠️ Il letterale sta accanto a una variabile che ci si concatena, quindi la "
     "toppa deve tenersi tutta la riga."),
    (1059, '\t\ts = "Sta imparando: niente"',
     "⭐ «N/A» diventa «niente» e non un trattino: la riga sopra e sotto sono "
     "frasi, e in mezzo a due frasi un «N/A» resta una sigla inglese."),
    (1062, '\t\ts = "Sta imparando: " + ActionName',
     "Il ramo con la magia o l'abilita' vera, che arriva da `GetActionName`."),
    (1067, '\t\ts = "Avanzamento: niente"',
     "Stessa coppia della riga sopra, stessa scelta per «N/A»."),
    (1070, '\t\ts = "Avanzamento: " + CAIActionLearnProgress(tc) + "%"',
     "Il ramo con la percentuale. Il «%» resta in coda, dove l'italiano lo vuole "
     "come l'inglese."),
    # --- AITeachConfigMenu
    (1189, '\tlistn(0, 0) = "Insegna una magia."', "Prima voce del menu d'insegnamento."),
    (1190, '\tlistn(0, 1) = "Insegna un\'abilita\'."', "Seconda voce."),
    (1191, '\tlistn(0, 2) = "Fai dimenticare una magia o un\'abilita\'."',
     "⚠️ Qui sparisce `him(tc)`, ed e' voluto: e' morfologia inglese a UN "
     "argomento, che restituisce «him»/«her»/«it» nudi — il ramo a due argomenti "
     "passa da `lang()`, questo no (`strumenti/funzioni.py`; punto 3 della "
     "ripresa della 51a). L'italiano non ha bisogno del pronome: «Fai dimenticare "
     "una magia» dice chi gia' dal contesto del menu, che parla di un alleato "
     "solo. ⭐ E «spell/ability» diventa «una magia o un'abilita'»: la barra "
     "inglese qui e' una disgiunzione, non una coppia."),
    (1192, '\tlistn(0, 3) = "Indietro"',
     "Come in tutto `custom_tweaks.hsp`, dove «Back» e' «Indietro»."),
    # --- AIConfigMenu
    (1544, '\tlistn(0, CAIAvailableSlots(tc)) = "Accendi o spegni l\'IA"',
     "⭐ «toggle» e' «accende e spegne» dalla 50a, che l'italiano non ha in una "
     "parola sola. Come voce di menu diventa imperativo: «Accendi o spegni»."),
    (1545, '\tlistn(0, CAIAvailableSlots(tc)+1) = "Azzera le azioni"',
     "«Re-Initialize» e' riportare le tattiche a come stavano all'inizio."),
    (1546, '\tlistn(0, CAIAvailableSlots(tc)+2) = "Comportamento da confuso"',
     "Apre la schermata delle due domande di `AIOtherSettingsMenu`, che chiede "
     "proprio «what to do when confused»."),
    (1547, '\tlistn(0, CAIAvailableSlots(tc)+3) = "Importa o esporta l\'IA"',
     "La barra inglese e' di nuovo una disgiunzione."),
    (1548, '\tlistn(0, CAIAvailableSlots(tc)+4) = "Indietro"', "Ultima voce."),
    # --- AITacticConfigMenu: le cinque voci col valore corrente in coda
    (1692, '\tlistn(0, 0) = "Cambia il soggetto. (Ora: " + AITextData(CAIEntity(CurrentTactic, tc) \\ 1000, 1) + ")"',
     "⭐ Il nome deve essere lo STESSO dell'intestazione della colonna che cambia "
     "(`:1090`), altrimenti il giocatore non collega la voce alla colonna: per "
     "questo «Chi» e' diventato «Soggetto». «(Current: X)» e' «(Ora: X)» dalla "
     "50a. ⚠️ Il valore in mezzo arriva dalla tabella 1, gia' resa."),
    (1693, '\tlistn(0, 1) = "Cambia la condizione. (Ora: " + AITextData(CAIComparator(CurrentTactic, tc), 2) + ")"',
     "Come sopra, e il nome combacia con l'intestazione «Condizione» di `:1091`."),
    (1694, '\tlistn(0, 2) = "Cambia il confronto. (Ora: " + AITextData(CAIComparatorFix(CurrentTactic, tc), 3) + ")"',
     "Combacia con «Confronto» di `:1092`."),
    (1697, '\tlistn(0, 3) = "Cambia il valore. (Ora: " + ValueName + ")"',
     "Combacia con «Valore» di `:1093`. Il valore arriva da `GetValueName`, che "
     "pesca da quattro tabelle diverse a seconda della condizione."),
    (1701, '\tlistn(0, 4) = "Cambia l\'azione. (Ora: " + ActionName + ")"',
     "Combacia con «Azione» di `:1094`."),
    (1703, '\t\tlistn(0, 5) = "Tieni il soggetto come bersaglio o il suo gruppo. (Ora: acceso)"',
     "⚠️ La riga piu' lunga del menu: 63 caratteri contro i 69 dell'inglese. Le "
     "voci partono da `wx + 64` in una finestra di 680, quindi ci sono ~550 px a "
     "corpo 12: ci sta. ⭐ La barra inglese e' l'unico posto di questa schermata "
     "dove NON e' una disgiunzione ma una coppia di effetti («preserve as target» "
     "e «keep target group» sono la stessa opzione vista sul singolo e sul "
     "gruppo), e l'italiano li lega con «o il suo gruppo» invece di ripetere il "
     "verbo. «On» e' «acceso» dalla 50a."),
    (1706, '\t\tlistn(0, 5) = "Tieni il soggetto come bersaglio o il suo gruppo. (Ora: spento)"',
     "Il ramo opposto, identico tranne lo stato."),
    (1708, '\tlistn(0, 6) = "Indietro"', "Ultima voce del menu della tattica."),
    # --- AIOtherSettingsMenu: le due domande, in un prompt da 280 px
    (3448, '\t\tpromptAdd "(Ora: dimmelo)", "a"',
     "La prima delle due domande: se l'alleato avvisa di quel che fa o sta zitto. "
     "⚠️ Sta in un `promptAdd` largo 280 px, il piu' stretto di questa schermata: "
     "13 caratteri contro i 19 dell'inglese."),
    (3450, '\t\tpromptAdd "(Ora: sto zitto)", "a"',
     "Il ramo opposto. ⭐ Prima persona come «dimmelo»: e' l'alleato che risponde, "
     "non un'etichetta di stato — l'inglese fa lo stesso con «Tell me» e «Be "
     "quiet», che sono quel che il giocatore ordina."),
    (3453, '\t\tpromptAdd "(Ora: sto fermo)", "b"',
     "La seconda domanda: cosa fa l'alleato quando e' confuso."),
    (3455, '\t\tpromptAdd "(Ora: faccio come voglio)", "b"',
     "Il ramo opposto, e la stessa idea che nella tabella delle azioni e' «Fa' "
     "come vuoi» (`:24`): li' e' un ordine del giocatore, qui e' l'alleato che "
     "dice cosa fara', quindi prima persona."),
]


def main() -> None:
    toppe, problemi = [], []

    for n, resa, motivo in LOTTO:
        cerca = TESTO[n - 1]
        quante = TESTO.count(cerca)
        if quante == 0:
            problemi.append(f":{n} non esiste nel sorgente")
            continue
        if cerca == resa:
            problemi.append(f":{n} la resa e' identica all'inglese")
        for c in resa:
            if ord(c) > 0x7F:
                problemi.append(f":{n} carattere fuori ASCII: {c!r}")
        toppa = {"file": FILE, "cerca": cerca, "sostituisci": resa, "motivo": motivo}
        if quante > 1:
            toppa["tutte"] = True
            toppa["motivo"] += (f" ⭐ `tutte`: la riga sta identica in {quante} punti del "
                                "pannello, e la resa e' la stessa in tutti.")
        toppe.append(toppa)

    if problemi:
        for p in problemi:
            print("⚠️ ", p)
        raise SystemExit("lotto non scritto")

    # la correzione alla toppa di poche ore fa
    vecchio, nuovo, nota = CORREZIONE
    percorso = REPO / "toppe.jsonl"
    fuori, corrette = [], 0
    for r in percorso.read_text(encoding="utf-8").splitlines():
        v = json.loads(r)
        if v.get("file") == FILE and v.get("cerca") == vecchio:
            v["sostituisci"] = nuovo
            v["motivo"] = v.get("motivo", "") + nota
            corrette += 1
        fuori.append(json.dumps(v, ensure_ascii=False))
    if corrette != 1:
        raise SystemExit(f"attesa 1 toppa da correggere, trovate {corrette}")
    percorso.write_bytes(("\n".join(fuori) + "\n").encode("utf-8"))
    print(f"corretta la toppa di :1090 («Chi» -> «Soggetto»)")

    uscita = REPO / "lavoro" / "_toppe-ai-menu.jsonl"
    dati = "".join(json.dumps(t, ensure_ascii=False) + "\n" for t in toppe).encode("utf-8")
    uscita.write_bytes(dati)
    print(f"{len(toppe)} toppe in {uscita.name}")

    esito = subprocess.run(
        [sys.executable, str(REPO / "scratchpad" / "aggiungi-toppe.py"), str(uscita)],
        cwd=REPO, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    print(esito.stdout.strip() or esito.stderr.strip())


if __name__ == "__main__":
    main()
