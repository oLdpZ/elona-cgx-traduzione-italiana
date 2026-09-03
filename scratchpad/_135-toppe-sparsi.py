"""Le rese degli «sparsi» della 135a: il testo scoperto fuori dal gioco di carte.

Ogni toppa si costruisce leggendo la riga ESATTA dal sorgente e sostituendo
dentro di essa il solo letterale: cosi' l'indentazione non si indovina mai, e
se il monte muove una riga lo script si ferma invece di scrivere una toppa che
non aggancia.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from strumenti import percorsi

# (file, riga, [(inglese, italiano), ...], motivo)
RESE = [
    # ---------------------------------------------------------------- main
    ("main.hsp", 61, [
        ("Could not find an installation of Elona+. Please follow the install "
         "instructions to install Elona+ first before running this program.",
         "Impossibile trovare un'installazione di Elona+. Segui le istruzioni "
         "di installazione, installa prima Elona+, poi riavvia questo programma.")],
     "La finestra che si apre quando manca l'installazione di base. E' la prima "
     "cosa che vede chi ha sbagliato a installare, e in inglese non aiuta chi "
     "non lo legge. `dialog` e' una finestra di Windows: nessun vincolo di "
     "larghezza delle reti del progetto."),
    ("main.hsp", 66, [
        ("Could not find debug assets folder '",
         "Impossibile trovare la cartella delle risorse di debug '"),
        ("'. Please copy a full installation of Elona+ Custom-G to this folder first.",
         "'. Copia prima in questa cartella un'installazione completa di Elona+ Custom-G.")],
     "Stessa famiglia della :61: la finestra d'errore all'avvio quando manca la "
     "cartella delle risorse. Il messaggio e' spezzato in due letterali attorno "
     "al percorso, e l'italiano tiene lo stesso ordine."),
    ("main.hsp", 1987, [
        ("Character with invalid position taking a turn.\\nCharacter name: ",
         "Un personaggio con posizione non valida sta giocando il turno.\\nNome: "),
        ("\\nState:", "\\nStato:"),
        ("\\nHired:", "\\nAssunto:")],
     "La finestra che avvisa di uno stato incoerente durante il turno. Il "
     "giocatore la vede e la segnala, quindi va letta: i tre letterali sono "
     "l'intestazione e due etichette di campo."),
    ("main.hsp", 3176, [
        ("Perform a quickload? You are playing in a mode where no-save penalties apply.",
         "Vuoi caricare la partita? Stai giocando in una modalita' che penalizza "
         "chi non salva.")],
     "La conferma del caricamento rapido nella modalita' con penalita'. E' una "
     "delle finestre che un giocatore vede piu' spesso, e la sua gemella e' la "
     ":3178: le due rese devono somigliarsi, perche' compaiono nello stesso "
     "punto a seconda della modalita'."),
    ("main.hsp", 3178, [
        ("Perform a quickload?", "Vuoi caricare la partita?")],
     "La conferma del caricamento rapido fuori dalla modalita' con penalita'. "
     "Gemella della :3176."),

    # -------------------------------------------------------------- system
    ("system.hsp", 72, [
        ("Updating Tweak Data from pre-2.18 version. \\nTweak entry is expanded "
         "to 2500 entries. \\nCheck your tweak menu to see if your tweaks are correct.",
         "Aggiornamento dei dati Tweak da una versione precedente alla 2.18. "
         "\\nLe voci passano a 2500. \\nControlla il menu Tweak: verifica che le "
         "tue opzioni siano rimaste giuste.")],
     "L'avviso di migrazione dei dati delle opzioni, che compare una volta sola "
     "a chi viene da una versione vecchia — e chiede di andare a controllare, "
     "quindi va capito."),
    ("system.hsp", 1924, [
        ('The name contains an invalid word \\"_tmp_\\"',
         'Il nome contiene una parola non ammessa: \\"_tmp_\\"')],
     "Una delle tre regole sul nome di un oggetto o PNG personalizzato "
     "(:1924, :1930, :1934). ⚠️ `_tmp_` resta com'e': e' la parola che il gioco "
     "cerca davvero, non una parola italiana."),
    ("system.hsp", 1930, [
        ("The first letter of the name must be alphabetic.",
         "La prima lettera del nome dev'essere una lettera dell'alfabeto.")],
     "Seconda delle tre regole sul nome, vedi :1924."),
    ("system.hsp", 1934, [
        ("The name is too long.", "Il nome e' troppo lungo.")],
     "Terza delle tre regole sul nome, vedi :1924."),
    ("system.hsp", 1859, [("Custom Item Text", "Testo oggetto personalizzato")],
     "La descrizione del tipo di file nella finestra Apri/Salva di Windows. "
     "La legge chi crea un oggetto personalizzato. Gemelle: :1876 e :1962."),
    ("system.hsp", 1876, [("Bit Map File", "File Bitmap")],
     "Descrizione del tipo di file nella finestra Apri/Salva, vedi :1859."),
    ("system.hsp", 1962, [("Custom Npc Text", "Testo PNG personalizzato")],
     "Descrizione del tipo di file nella finestra Apri/Salva, vedi :1859. "
     "«PNG» e' la sigla che il progetto usa per «personaggio non giocante»."),
    ("system.hsp", 1999, [("BMP File|JPG File", "File BMP|File JPG")],
     "Il filtro a tendina della finestra Apri di Windows. ⚠️ La barra verticale "
     "separa le voci ed e' sintassi: resta. L'altro argomento della stessa "
     "riga, `\"bmp|jpg\"`, sono le ESTENSIONI e non si toccano."),
    ("system.hsp", 3521, [
        ("Contributor MSL / View the credits for more",
         "Contributi di MSL / Vedi i crediti")],
     "Una riga dei crediti sulla schermata del titolo. Le sue sei sorelle sono "
     "gia' rese da altrettante toppe (`mes \"Contributor f1r3fly, ...\"` -> "
     "«Contributi di f1r3fly, ... / Vedi i crediti»): questa era restata "
     "indietro, e la resa ne ricalca la forma parola per parola."),

    # -------------------------------------------------------------- screen
    ("screen.hsp", 22, [
        ("Invalid screen resolution detected. Custom-GX will attempt to reset "
         "to a sane default.",
         "Risoluzione dello schermo non valida. Custom-GX prova a tornare a un "
         "valore ragionevole.")],
     "La finestra che compare all'avvio quando la risoluzione salvata non e' "
     "valida — tipicamente dopo aver cambiato monitor. Il giocatore la vede "
     "prima di qualunque altra cosa del gioco."),

    # ------------------------------------------------------------ custom_ai
    ("custom_ai.hsp", 1663, [
        ("Re-Initialize this pet's spells and abilities?",
         "Vuoi reimpostare incantesimi e abilita' di questo famiglio?")],
     "La conferma nel menu dell'IA dei famigli. «famiglio» e' il termine del "
     "glossario per `pet`."),
    ("custom_ai.hsp", 3077, [("Throw Salt", "Lancia sale")],
     "Una delle quattro azioni che si leggono nella lista dell'IA di un "
     "famiglio (:3077-:3086). Sono voci di menu, non frasi: l'imperativo e' la "
     "forma che il progetto usa per i comandi."),
    ("custom_ai.hsp", 3080, [("Throw Greater Potion", "Lancia pozione maggiore")],
     "Azione dell'IA dei famigli. «greater» -> «maggiore» postposto, come dice "
     "il glossario; vedi :3077."),
    ("custom_ai.hsp", 3083, [("Throw Major Potion", "Lancia pozione potente")],
     "Azione dell'IA dei famigli. ⚠️ Qui l'inglese ha DUE gradi vicini, "
     "`Greater` (:3080) e `Major`: il glossario da' «maggiore» per `greater`, "
     "quindi `major` prende «potente» per non avere due voci identiche nella "
     "stessa lista. Vedi :3077."),
    ("custom_ai.hsp", 3086, [("Throw Potion", "Lancia pozione")],
     "Azione dell'IA dei famigli, il grado base dei tre. Vedi :3077."),
    ("custom_ai.hsp", 3214, [("Not Set", "Non impostato")],
     "Il valore che il menu dell'IA mostra quando una casella e' vuota. "
     "⚠️ Il `\"not set\"` minuscolo di :71 NON si tocca: quello sta in un `if`, "
     "e' l'operando del confronto."),
    ("custom_ai.hsp", 3483, [
        ("ElonaPlus CGX custom AI", "IA personalizzata ElonaPlus CGX")],
     "Descrizione del tipo di file nella finestra Salva quando si esporta l'IA "
     "di un famiglio."),

    # ------------------------------------------------------------- command
    ("command.hsp", 13240, [
        ("Invalid Item Id found. Item No:", "Trovato un Id oggetto non valido. Oggetto n.:"),
        (" has been removed from your inventory.", " e' stato tolto dal tuo inventario.")],
     "La finestra che avvisa di un oggetto corrotto tolto dall'inventario: "
     "riguarda la roba del giocatore, quindi va letta. Due letterali sulla "
     "stessa riga, attorno al numero e all'Id."),
    ("command.hsp", 16039, [
        ("It is a Custom Item from Omake branch!",
         "E' un oggetto personalizzato del ramo Omake!")],
     "La descrizione che si legge esaminando un oggetto che viene dal ramo "
     "Omake. «Omake» resta: e' il nome del ramo, non una parola comune."),
    ("command.hsp", 16041, [("(Omake CItem) ", "(Oggetto Omake) ")],
     "Il prefisso che marca lo stesso oggetto nella riga della descrizione "
     "(:16041, subito dopo :16039). `CItem` e' l'abbreviazione di «Custom "
     "Item», e in italiano si scioglie perche' non e' un identificatore."),
    ("command.hsp", 17555, [("ElonaPlus User Map", "Mappa utente ElonaPlus")],
     "Descrizione del tipo di file nella finestra Apri/Salva delle mappe "
     "utente."),
    ("command.hsp", 17600, [("ElonaPlus Extra Team", "Squadra extra ElonaPlus")],
     "Descrizione del tipo di file nella finestra Apri/Salva della squadra "
     "extra."),

    # --------------------------------------------------------------- trait
    ("trait.hsp", 1268, [
        ('This is an UNKNOWN_TRAIT["+tid+"], report it.',
         'Questo e\' un UNKNOWN_TRAIT["+tid+"], segnalalo.')],
     "Il messaggio che il giocatore legge nella lista dei tratti quando il "
     "gioco ne incontra uno che non conosce. Compare tre volte sulla stessa "
     "riga (le tre colonne della voce) e la toppa le prende tutte. "
     "⚠️ `UNKNOWN_TRAIT[<numero>]` resta in inglese di proposito: e' la "
     "stringa che chi riceve la segnalazione deve poter cercare."),

    # ---------------------------------------------------------------- text
    ("text.hsp", 9351, [("Unknown Code", "Codice sconosciuto")],
     "Il testo che compare al posto di un codice che il gioco non riconosce."),

    # ---------------------------------------------------------------- help
    ("help.hsp", 230, [("help index not found ", "indice della guida non trovato ")],
     "La finestra d'errore quando manca l'indice della guida."),

    # ---------------------------------------------------------------- proc
    ("proc.hsp", 16980, [("your friends", "i tuoi compagni")],
     "⚠️ RIPARA UN DIFETTO DI RESA, non solo una stringa scoperta. "
     "`proc.hsp:16991` e' `txt lang(jp, \"You started a reading party with \" + "
     "studybuddy + \".\")`, e `studybuddy` vale il NOME del compagno (:16977) "
     "oppure «your friends» (:16980) quando sono piu' d'uno. La resa nel "
     "dizionario aveva inghiottito la variabile — «Cominci un circolo di "
     "lettura con i tuoi compagni.» — cosi' nella build `studybuddy` risultava "
     "assegnato e mai letto, e leggendo con un compagno solo l'italiano diceva "
     "«i tuoi compagni» invece del suo nome. Il dizionario ora rimette "
     "`studybuddy` nella frase e questa toppa rende il suo altro valore."),
]

# La resa del dizionario che va rimessa insieme alla toppa qui sopra: senza
# questa, `studybuddy` resta assegnato e mai letto.
FIRMA_CIRCOLO = "ad9aaf3819d2028a5ef086820401316cbd097f0d"
IT_CIRCOLO = '"Cominci un circolo di lettura con " + studybuddy + "."'


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
                raise SystemExit(
                    f"{nome_file}:{numero}: non trovo {inglese[:60]!r} nella "
                    f"riga\n    {riga.strip()[:160]}")
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
    print(f"  toppe nuove: {len(da_scrivere)} (di {len(nuove)} rese)")

    # e la resa del dizionario che rimette `studybuddy` nella frase
    diz = percorsi.DIZIONARIO / "proc.hsp.jsonl"
    righe = diz.read_text(encoding="utf-8").splitlines()
    cambiata = False
    for i, r in enumerate(righe):
        if not r.strip():
            continue
        v = json.loads(r)
        if v.get("firma") == FIRMA_CIRCOLO and v.get("it") != IT_CIRCOLO:
            v["it"] = IT_CIRCOLO
            righe[i] = json.dumps(v, ensure_ascii=False)
            cambiata = True
    if cambiata:
        diz.write_text("\n".join(righe) + "\n", encoding="utf-8")
        print("  dizionario: rimessa `studybuddy` nel circolo di lettura")
    else:
        print("  dizionario: gia' a posto")


if __name__ == "__main__":
    main()
