# -*- coding: utf-8 -*-
"""Scrive la voce di `log.md` e la riga di `index.md` per la 130a.

Il vault sta fuori dal repo del progetto: i percorsi sono assoluti, come per le
sessioni precedenti. Idempotente su tutt'e due i file.

⚠️ Si compone e si valida PRIMA di scrivere (regola della 39a).
"""
import io
import sys
from pathlib import Path

VAULT = Path(r"C:\Users\old_p\Documents\progetto second brain")

TITOLO_LOG = ("## [2026-09-03] work | Elona ITA — le toppe entrano in due reti, "
              "e il fronte che il conto dava di sessanta righe era di quattro")

VOCE_LOG = TITOLO_LOG + """

- **⭐⭐⭐ Il lavoro della sessione: un conto di cose intatte non è un conto di lavoro.** La ripresa della 129ª dava il fronte della traduzione in **60 righe nude di classe «testo»**, «il lavoro vero». Incrociandole coi siti nominati in `invariati.md`, `decisioni.md` e `rinviate.jsonl`: **38 erano già decise** — sigle che inglese e giapponese scrivono identiche, chiavi di `config.txt` che tradurre romperebbe, il TSV dell'autopick, `helloworld.hsp` che non sta nemmeno nella build. Delle 22 rimaste, guardate una per una, **4 erano vive**. Il fronte era il **7%** del numero che lo annunciava. ⚠️⚠️ E il progetto lo sapeva: `invariati.md` scrive dalla 127ª che «quei referti contano i letterali **intatti**, e una riga che deve restare intatta è indistinguibile da una che nessuno ha guardato» — ma la nota stava nel documento delle **decisioni** e il numero sbagliato in quello che si legge in **apertura**.
- **La cura non è cambiare il contatore: è aggiungere il secondo numero.** Il totale deve continuare a contare anche il deciso, altrimenti una decisione sbagliata diventa invisibile. `_130-residuo-delle-righe-nude.py` stampa **contate / nominate / residuo**, e si porta a zero il residuo: **56 / 56 / 0**. ⚠️ L'incrocio si fa sui **siti** (`file:riga`), non sulle parole; e un intervallo scritto `:692`-`:699` l'incrocio lo trova due volte su otto — gli intervalli si scrivono **esplosi**, o il residuo mente al ribasso.
- **Le quattro rese vive.** `init.hsp:537` «unknown user» → «utente sconosciuto»; `quest.hsp:782` → «Voto del raccolto: … (…s)!»; `text.hsp:11912` → «Punteggio dell'esibizione: … punti!»; `text.hsp:12104` «[News] » → **«[Notizie] »**. ⭐ L'ultima non era una scelta di parola: il diario intitola già la sezione `" - Notizie - "`, dice «Nessuna notizia» quando è vuota e le testate sono italiane da sessioni — quel prefisso era l'unico pezzo inglese di un sistema tutto tradotto. E «Esibizione» viene dal glossario (`skill.hsp:357`), non dall'orecchio. ⚠️ La `s` di `(3s)` si è **ricopiata**: `seedp` non è il numero dei semi e il sorgente non dice che unità sia — un'unità opaca non si inventa.
- **⚠️⚠️⚠️ E la riga sopra, `init.hsp:536`, torna `"user"` e NON si tocca.** È l'**operando che due `sreplace` cercano** (`item_func.hsp:967` e `:1073`) per mettere il nome del PNG personalizzato dentro il nome di carte, statuette e parti. Tradurla spegnerebbe tutt'e due i siti **in silenzio**. È la famiglia della 128ª da un lato che nessuna rete guarda: il cancello di allora cerca `X == lang(J, E)`, e un `sreplace` non è un confronto. **Misurato**: nella build `db_creature.hsp:97539` torna ancora `lang("user", "user")`, quindi oggi i rami sono vivi — è un difetto con una **data di nascita futura**, che nascerà da solo quando un lotto renderà quel nome.
- **⭐⭐ Due reti nuove sulle toppe, e la premessa della 129ª era falsa in due punti su tre.** `maiuscole` **legge già la build**, quindi le toppe le vede per costruzione — ma di toppe con `cnven(` ce ne sono **sei**: non una rete assente, una rete quasi muta. `larghezze` non può vederle **in nessun caso**: scorre il dizionario e cerca `(file, riga)`, e una toppa non ha nemmeno il campo `riga`. Il glossario non lo legge nessuno. ⚠️⚠️ E il mio primo tentativo di misurare la seconda rispondeva **0** perché il ciclo saltava tutte e 1.172 le voci sul campo che non esiste: lo zero era la spia rotta, non il dato — lezione della 109ª, incassata il giorno dopo averla riscritta.
- **`_130-larghezze-sulla-build.py`: il metro sull'esito.** Gira la macchina di `strumenti/larghezze.py` sull'**albero della build**, dove dizionario e toppe sono già dentro: un metro solo per le due strade, e nessun numero di riga da far combaciare fra alberi di lunghezza diversa. **714 voci misurate, 86 scritte da una toppa, 0 fuori misura.** ⭐ Ha trovato due cose al primo giro, e una era della mia misura: `larghezze.reso` sbaglia quando il valore dinamico sta **in testa**, perché cerca un valore *fra due letterali* — `mapname(i) + " " + cnvrank(…)` risultava lungo **92 caratteri**, il codice invece della frase. Non si era mai visto perché nella rete del sorgente il testo arriva dal campo `it`, che è sempre un letterale.
- **La resa che quella rete ha trovato: `command.hsp:7770`.** «Evoca come amichevole. (350 pp)» sono **31 caratteri** in un riquadro da 280px, tetto 30, e il riquadro **taglia**. L'inglese ci stava (28): non un tetto ereditato da monte, un difetto **aggiunto dalla traduzione**. ⚠️⚠️ E il `motivo` della toppa **dichiarava la larghezza** — «ⓘ Il prompt è largo 280 (:7774)»: il dato era in mano, la misura no, perché niente la faceva. Cade il punto prima della parentesi, non la parola.
- **⭐ `_130-glossario-nelle-toppe.py`, e la maiuscola che lo rende un filtro.** La prima stesura bocciava **87 voci su 163** — più della metà, cioè l'elenco completo con un passaggio in più. La causa stava nel conto: `will` **trentacinque volte**, ed era il futuro inglese; poi `change`, `attack`, `bow` («Bow down before me»), `body` («wash your body»). La discriminante non è la lunghezza, è la **maiuscola in mezzo alla frase**: un termine di glossario è un termine d'interfaccia, e l'inglese lo scrive come tale. **163 → 46 giudicate, 6 divergenze.** ⚠️ Si è scelta questa e non «maiuscolo + testo ≤ 40» (33 giudicate, 5 divergenze): la seconda compra il numero piccolo **smettendo di guardare**. Un filtro si sceglie sul rapporto, non sul totale.
- **⭐⭐ E ha trovato che `Gauge` aveva tre rese, dove il glossario ne aveva decisa una nella 5ª.** Non era della toppa: era del progetto, su sei siti — `barra` in una dozzina di posti, `forza` in tre, `carica` in due. ⚠️⚠️⚠️ **La prova sta su due righe adiacenti**: `skill.hsp:1528` chiamava la mossa «<Serba/libera la forza>» e `:1529`, la sua descrizione *sulla stessa riga dell'elenco*, diceva «Attiva o disattiva la barra»; e un pannello d'aiuto diceva «la barra», «Forza liberata» e «la barra» dentro un paragrafo solo. ⚠️ Il giapponese è `【力の解放】` e «Forza» era la resa **più fedele** — `<Gauge Release>` è già una scelta del localizzatore inglese — ma si sceglie l'inglese per **riconoscibilità**: la 5ª aveva deciso «Barra» *misurando* (60 occorrenze su 75 sono le etichette di costo `[Barra 50%]`), e una mossa che si chiama «Forza» e costa «Barra» chiede due nomi per una cosa sola.
- **Due eccezioni tenute e **scritte nel glossario**, non lasciate nei siti.** «Pagnotte mangiate:» resta: quella riga sta in una colonna di contabili al plurale — «Mutandine mangiate», «Umani mangiati», «Oggetti rubati» — e «Pane mangiato» spezzerebbe il verso della colonna per un termine che lì nessuno confonde; il **nome dell'oggetto** resta «pane» dappertutto. E «Nome Livello Effetto» non è una divergenza: il giapponese dice `特徴の効果`, «l'effetto del tratto», e la colonna mostra l'effetto — `Detail` era la scelta larga dell'inglese. Le cinque lette stanno in un `GIUDICATI` col motivo, come in `strumenti/maiuscole.py`: **il referto non chiede zero, chiede che l'elenco non si allunghi da solo.**
- **✅ Prova al contrario: 9 su 9, e una pretende che il cancello resti SPENTO.** Prende i dati **veri** e sposta di un passo la cosa che tiene chiuso il cancello — allunga una voce di menu, le toglie la `lang()`, stringe il riquadro a testo fermo, guasta una resa buona, alza a maiuscolo un termine minuscolo — e stampa **dove** si è acceso. ⭐ La nona chiede il contrario: sulla dinamica in testa il cancello **non deve** accendersi. Una prova al contrario fatta solo di casi che devono accendersi misura la sensibilità e tace sulla specificità, e una correzione esagerata passerebbe verde.
- **⚠️ Il contratto delle toppe ha respinto il mio primo giro, nel verso giusto.** Spezzando il sorgente **CRLF** su `"\\n"`, ogni `cerca` si portava dietro un `\\r` e non combaciava con niente: quattro toppe mute fermate prima della build.
- **⚠️ Un numero della 129ª non reggeva, e non l'ha mosso questa sessione.** `perimetro` dà **26.327** dove la ripresa attendeva 26.326 «invariato». Verificato contando le voci con `it` a `HEAD` e dopo il lotto: **26.320 in tutt'e due**, quindi il numeratore non l'ho toccato. Il +1 è della 129ª — ha reso `command.hsp:10710`, che è una resa in più, e ha registrato il +2 di `applica` e il −1 dei tre contatori ma per `perimetro` ha scritto «invariato» invece di rilanciarlo. La sua stessa lezione, applicata a lei.

**File toccati**
- Repo `Elona+ CGX - Traduzione Italiana`: `toppe.jsonl` (1.172 → **1.176**: 4 rese nuove, 3 allineate a «barra», 2 accorciate), `dizionario/skill.hsp.jsonl`, `dizionario/custom_tweaks.hsp.jsonl`, `dizionario/command.hsp.jsonl` (4 rese allineate), `glossario.md` (la riga di `Gauge` e l'eccezione di `bread`), `invariati.md` (la sezione delle ultime 18 righe nude), `RIPRESA-sessione.md`, `decisioni.md`, e dieci `scratchpad/_130-*.py`.
- Fuori dal repo: albero di build rifatto e `elonaplus2.31/cgx-test.exe` ricompilato (**22:56 del 02/09**). I sei file dati non sono cambiati.
- Vault: `wiki/concepts/un-conto-di-cose-intatte-non-e-un-conto-di-lavoro.md` (nuovo), `wiki/concepts/stringhe-che-sono-dati.md` (la terza forma: l'operando di una **sostituzione**), `index.md`, `log.md`.

**Numeri, rilanciati dopo l'ultima modifica ai documenti**
- `pytest` **798 passed / 6 skipped**; `prova_identita` 72/72 e 30.905; `applica` **30.766**; toppe **1.176 agganciate su 1.176**; perimetro `lang()` **26.327 su 26.327 = 100%**; `triage_nudi` testo **56** (erano 60) e `_130-residuo-delle-righe-nude` **56 / 56 / RESIDUO 0**; `_126-nudi-nel-ramo-jp` **53 vive** (erano 57); `_126-spente-da-una-costante` **39 vive davvero** (erano 43); `_126-referti-toppe` participi 0, elisioni 0 su **914** toppe con testo; `_130-larghezze-sulla-build` **714 / 86 / 0 fuori misura**; `_130-glossario-nelle-toppe` **46 giudicate, 5 dichiarate, 0 nuove**; `_130-prova-al-contrario-reti-toppe` **9 su 9**; `_129-condizioni` 0/0/0 su 113; `_129-prova-al-contrario` 8 su 8; `_128-confronti` di monte 3, aggiunti 0; `_97-quanto-resta` e `_125-non-tradotte` **111 / 111 / 0 FUORI**; `larghezze` 0 fuori misura; `maiuscole` 143/6/1/7/**0 da guardare**; `riquadri` 0 su 38 e 0 su 71; `linguette` 0 e 0; `gemelle` 9; `creature` 0 e 0; `diario` 0 su 205; `gronde` 0 su 5; `bilingui` 0; `menu_dialogo` 0 peggiorate; `dati_sorgente` 7/7.

**Da fare alla prossima sessione**
- **⭐⭐⭐ Il debito di collaudo, e ormai è l'unico fronte grosso.** ~9.650 rese mai viste a schermo, e nessuno strumento che le conti. Il perimetro `lang()` è chiuso al 100%, le righe nude hanno **residuo 0**, le 111 non tradotte sono tutte rinviate decise: **da tradurre non resta niente che qualcuno abbia chiesto.** Quel che resta è guardare. ⓘ Le quattro rese di oggi non sono state viste a schermo.
- **⭐⭐ La rete che cerca l'operando di una SOSTITUZIONE.** `init.hsp:536` l'ha trovata un umano leggendo; il cancello della 128ª cerca `X == lang(J, E)` e non la vedrebbe mai. Il verbo cambia — `sreplace`, `instr`, `strmid` con un letterale, uno `split` — il difetto no.
- **⭐⭐ Alle toppe restano fuori due reti**: le **maiuscole del testo** (non `cnven`, che è un'altra cosa) e le **larghezze fuori dai menu** — `riquadri`, `linguette` e `gronde` girano tutte sul dizionario.
- **⭐ Due referti che nessuno ha scritto**: la coda nuda di una `lang()` già resa (`chat.hsp:17065`, 127ª) e la resa che cita per nome un'etichetta che vive in una toppa.
- **💡 E due famiglie che hanno una casa ma non una rete**: il frammento morto **per flusso**, e la **gemella viva di una firma rinviata**.
"""

RIGA_INDEX = ("- [Un conto di cose intatte non è un conto di lavoro]"
              "(wiki/concepts/un-conto-di-cose-intatte-non-e-un-conto-di-lavoro.md)"
              " — un contatore costruito su «gli elementi che nessuno ha ancora"
              " toccato» non distingue ciò che nessuno ha guardato da ciò che"
              " qualcuno ha guardato e ha deciso di **lasciare com'è**: la"
              " decisione non tocca l'oggetto, quindi il numero non si muove. È"
              " monotòno in un verso solo, e allora conviene toccare anche ciò"
              " che andrebbe lasciato, perché è l'unica azione che il cruscotto"
              " premia. Su Elona ITA il fronte annunciato in **60 righe** era di"
              " **4**: 38 erano decisioni già scritte, e il progetto lo sapeva —"
              " la nota stava nel documento delle decisioni, il numero sbagliato"
              " in quello che si legge in apertura. ⭐ La cura non è cambiare il"
              " contatore (deve contare anche il deciso, o una decisione"
              " sbagliata diventa invisibile) ma **aggiungere il residuo**: gli"
              " elementi che nessun documento nomina, e si porta a zero quello."
              " ⚠️ L'incrocio si fa sui **siti**, non sulle parole, e gli"
              " intervalli si scrivono esplosi o il residuo mente al ribasso.")

ANCORA_INDEX = "- [Una limitazione scritta in un docstring non è nota]"


def main() -> int:
    # ---------------------------------------------------------------- log
    percorso = VAULT / "log.md"
    testo = io.open(percorso, encoding="utf-8").read()
    if TITOLO_LOG in testo:
        print("log.md: la voce c'e' gia'")
    else:
        io.open(percorso, "w", encoding="utf-8", newline="\n").write(
            testo.rstrip("\n") + "\n\n" + VOCE_LOG.rstrip("\n") + "\n")
        print("log.md: voce della 130a aggiunta")

    # -------------------------------------------------------------- index
    percorso = VAULT / "index.md"
    testo = io.open(percorso, encoding="utf-8").read()
    if "un-conto-di-cose-intatte-non-e-un-conto-di-lavoro" in testo:
        print("index.md: la riga c'e' gia'")
        return 0
    if ANCORA_INDEX not in testo:
        print("⚠️ index.md: ancora non trovata, non scrivo")
        return 1
    io.open(percorso, "w", encoding="utf-8", newline="\n").write(
        testo.replace(ANCORA_INDEX, RIGA_INDEX + "\n" + ANCORA_INDEX, 1))
    print("index.md: riga del concetto nuovo aggiunta")
    return 0


if __name__ == "__main__":
    sys.exit(main())
