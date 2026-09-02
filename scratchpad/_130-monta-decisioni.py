# -*- coding: utf-8 -*-
"""Infila in testa a `decisioni.md` le decisioni della 130a.

Le sessioni recenti **antepongono**: la sezione nuova va subito dopo il `---`
della testa, prima di quella della 129a. Idempotente sul titolo.

⚠️ Si compone e si valida PRIMA di scrivere (regola della 39a).
"""
import io
import sys

from strumenti import percorsi

ANCORA = "## La condizione di un rinvio è un campo, e il campo è obbligatorio"

TITOLO = ("## Una parola sola per la barra, e due eccezioni che il glossario "
          "si tiene — 2026-09-03, centotrentesima")

SEZIONE = TITOLO + """

La rete nuova sul glossario ha segnalato una toppa che scrive «Forza liberata»
dove `glossario.md` dice **Barra**. Tirando il filo, la divergenza non era della
toppa: era del progetto, su sei siti — `barra` in una dozzina di posti, `forza`
in tre, `carica` in due.

⚠️⚠️⚠️ **La prova che chiude la questione sta su due righe adiacenti.** Il nome
di una mossa speciale e la sua descrizione si leggono sulla **stessa riga**
dell'elenco:

    skill.hsp:1528          «<Serba/libera la forza>»
    skill.hsp:1529          «Attiva o disattiva la barra»

e lo stesso pannello d'aiuto diceva «la barra», «Forza liberata» e «la barra»
dentro un paragrafo solo. Non serviva riaprire il term base: serviva applicarlo.

### Perché «barra» e non «forza», che pure è più fedele al giapponese

Il giapponese è `【力の解放】`, «liberazione della **forza**». «Forza liberata»
rendeva la fonte; `<Gauge Release>` è già una scelta del **localizzatore
inglese**, che ha battezzato la mossa col nome dello strumento invece che della
risorsa.

Si è scelto lo stesso l'inglese, e la ragione non è di fedeltà ma di
**riconoscibilità**. La 5ª aveva deciso `Gauge` → «Barra» *misurando*: 60
occorrenze su 75 sono le etichette di costo dell'elenco delle mosse,
`[50% Gauge] Party Shooting` → `[Barra 50%]`, ed è lì che il giocatore incontra
la meccanica. Una mossa che si chiama «Forza» e costa «Barra» chiede di tenere
in testa due nomi per una cosa sola.

⭐ **La regola generale, che vale oltre questo caso:** quando la fonte e la
lingua ponte danno due parole per la stessa cosa, si sceglie quella che tiene
insieme il **maggior numero di punti di contatto col giocatore**, non quella più
vicina alla fonte. La fedeltà si spende dove il giocatore non deve riconoscere
niente.

⚠️ «Carica» non era una resa alternativa: era una **deroga**, e in `custom_ai`
la stessa risorsa si chiamava già «Barra» — l'elenco con cui il giocatore
configura l'IA era l'unico posto in regola.

### Le due eccezioni, e perché stanno nel glossario e non nei siti

`glossario.md` si apre dicendo «un termine tradotto qui si riusa ovunque; se una
resa non funziona in un contesto, si cambia **qui** e si ritraduce — non si
deroga nel lotto». Applicato in tutt'e due i versi: una divergenza chiusa
allineando, due tenute e **scritte**.

- **`bread` → «Pagnotte mangiate:» resta** (`command.hsp:3079`). Non è gusto:
  quella riga sta in una colonna di contabili al plurale — «Mutandine
  mangiate», «Umani mangiati», «Oggetti rubati», «Sorelline» — e si legge come
  un insieme. «Pane mangiato» spezzerebbe il verso della colonna per far
  combaciare un termine che lì nessuno può confondere. Il **nome dell'oggetto**
  resta «pane» dappertutto: l'eccezione è del contatore, non del termine.
- **`detail` → «Nome Livello Effetto» non è una divergenza** (`command.hsp:941`).
  Il giapponese dice `特徴の効果`, «l'effetto del tratto», e la colonna di
  «Talenti e tratti» mostra l'effetto. `Detail` era la scelta larga dell'inglese;
  «Effetto» è la fonte. ⭐ Qui il giapponese decide, e nel caso di `Gauge` no:
  la differenza è che lì c'erano sessanta etichette da tenere insieme, qui una
  colonna sola.

### E l'elenco delle dichiarate non è un cancello abbassato

Le cinque divergenze lette stanno in un `GIUDICATI` col motivo, come fa
`strumenti/maiuscole.py`: **il referto non chiede zero divergenze, chiede che
quell'elenco non si allunghi da solo.** Una divergenza nuova è una riga da
leggere, non per forza un difetto — è la forma già decisa alla 123ª
(«un'eccezione si dichiara, non si abbassa il cancello»).

---

## Il termine si riconosce dalla maiuscola, non dalla lunghezza — 2026-09-03, centotrentesima

La prima stesura della rete sul glossario bocciava **87 voci su 163**: più della
metà, cioè l'elenco completo con un passaggio in più. La tentazione era
restringere per **lunghezza** — «guardo solo le etichette corte» — e sarebbe
stato il ritaglio sbagliato.

Contando i termini che bocciavano, la causa era una sola: `will` **trentacinque
volte**, ed era il futuro inglese. Poi `change`, `attack`, `bow` («**Bow** down
before me»), `body` («wash your **body**»). Sono parole comuni che il glossario
nomina perché **altrove** sono etichette.

⭐ **La discriminante è la maiuscola in mezzo alla frase.** Un termine di
glossario è un termine d'interfaccia; quando l'inglese lo scrive maiuscolo
dentro una frase lo sta usando come termine, non come parola. A inizio frase non
vale: lì la maiuscola è della punteggiatura.

    restrizione                     contenevano  giudicate  divergenze
    nessuna                                 163        163          87
    solo inglese ≤ 40 caratteri              68         68          15
    solo termine maiuscolo                  163         46           6   ← questa
    maiuscolo + inglese ≤ 40                 68         33           5

⚠️ **Si sceglie la terza e non la quarta, anche se boccia una voce di più:** la
quarta lascia fuori metà delle toppe **prima di guardarle**, per un criterio —
la lunghezza — che col glossario non c'entra niente. Un filtro si sceglie sul
**rapporto**, non sul totale, e una restrizione che riduce il numeratore
riducendo il denominatore non è un filtro: è un'astensione.

⚠️⚠️ **E la taratura non si trasporta.** La stessa rete sul dizionario dà
1.239 giudicate e **458 divergenze**, il 37%. Non è un difetto: le toppe sono
quasi tutte **etichette**, le rese quasi tutte **prosa**, e in prosa `Darkness`
→ «buio» è giusto anche dove il glossario dice «oscurità». Un criterio tarato su
un insieme va rimisurato sull'altro prima di chiamarlo cancello.

---

## Un conto di cose intatte non è un conto di lavoro — 2026-09-03, centotrentesima

La ripresa della 129ª dava il fronte della traduzione in **60 righe nude di
classe «testo»**. Misurate: 38 erano **già decise e scritte**, 22 il residuo,
e di quelle **4 vive**. Il fronte era il 7% del numero che lo annunciava.

⚠️⚠️ E il progetto lo sapeva: `invariati.md` scrive dalla 127ª che «quei referti
contano i letterali **intatti**, e una riga che deve restare intatta è
indistinguibile da una che nessuno ha guardato». La nota stava nel documento
delle **decisioni**; il numero sbagliato stava nel documento che si legge in
**apertura**. Sapere non basta: conta dove è scritto.

⭐ **La cura non è cambiare il contatore.** Deve continuare a contare anche il
deciso, altrimenti una decisione sbagliata diventa invisibile. Si aggiunge un
**secondo numero** — il residuo, cioè quel che nessun documento nomina — e si
porta a zero quello.

⚠️ L'incrocio si fa sui **siti** (`file:riga`), non sulle parole. E un intervallo
scritto `:692`-`:699` l'incrocio lo trova due volte su otto: gli intervalli si
scrivono **esplosi**, o il residuo mente al ribasso. Successo e corretto lo
stesso giorno.

Concetto: `wiki/concepts/un-conto-di-cose-intatte-non-e-un-conto-di-lavoro.md`.

---

## Due righe adiacenti, trattamenti opposti: `init.hsp:536` e `:537` — 2026-09-03, centotrentesima

    536   if ( … ) { return "user" }         ⚠️ NON si tocca: è una chiave
    537   locvar_getunid_s = "unknown user"  ✅ resa: «utente sconosciuto»

`"user"` è **l'operando che due `sreplace` cercano** (`item_func.hsp:967` e
`:1073`) per mettere il nome del PNG personalizzato dentro il nome di carte,
statuette e parti di creatura. Tradurlo spegnerebbe tutt'e due i siti **in
silenzio**: nessun errore, e il giocatore leggerebbe il segnaposto per sempre.

⭐ È la famiglia della 128ª — un ramo ucciso dalla traduzione — da un lato che
**nessuna rete guarda**: `_128-confronti-contro-un-nome-assegnato.py` cerca
`X == lang(J, E)`, e un `sreplace` non è un confronto. Il verbo cambia,
il difetto no: `sreplace`, `instr`, `strmid` con un letterale, uno `split` su un
separatore.

⚠️ **Misurato, e oggi i rami sono vivi**: nella build `db_creature.hsp:97539`
torna ancora `lang("user", "user")`. È un difetto con una **data di nascita
futura** — nascerà da solo il giorno in cui un lotto renderà quel nome, e
nessuno lo sta aspettando. Il rimedio, quel giorno, è la forma di «Your Home»
(42ª): si allarga il sito che cerca, non si tocca il nome.

---

## Una prova al contrario deve saper dire anche «qui deve restare spento» — 2026-09-03, centotrentesima

La rete nuova sulle larghezze ha trovato due cose al primo giro, e **una era un
difetto della misura**: `larghezze.reso` sbaglia quando il valore dinamico sta
**in testa** all'espressione, perché la sua regola cerca un valore *fra due
letterali*. `mapname(i) + " " + cnvrank(…)` risultava lungo 92 caratteri — il
codice, non la frase.

Corretto il difetto, la prova al contrario ha guadagnato una prova che **non**
chiede al cancello di accendersi: gli chiede di **restare spento** su quella
forma. Senza, una correzione esagerata — misurare l'espressione invece del testo
— passerebbe verde: tutte le prove si accendono, e il cancello grida su ogni
voce dinamica.

⭐ Una prova al contrario fatta solo di casi che devono accendersi misura la
**sensibilità** e non dice niente sulla **specificità**. Le due si guardano
insieme, o si scambia il rumore per copertura.
"""


def main() -> int:
    percorso = percorsi.PROGETTO / "decisioni.md"
    testo = io.open(percorso, encoding="utf-8").read()
    if TITOLO in testo:
        print("la sezione c'e' gia': non riscrivo")
        return 0
    if ANCORA not in testo:
        print("⚠️ ancora non trovata: non scrivo niente")
        return 1
    nuovo = testo.replace(ANCORA, SEZIONE.rstrip("\n") + "\n\n---\n\n" + ANCORA, 1)
    io.open(percorso, "w", encoding="utf-8", newline="\n").write(nuovo)
    print("decisioni.md: sezione della 130a anteposta (%d caratteri)" % len(SEZIONE))
    return 0


if __name__ == "__main__":
    sys.exit(main())
