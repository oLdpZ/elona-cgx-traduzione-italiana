## Una famiglia toppata a metà l'avevo lasciata io — 2026-09-02, centoventisettesima

Il fronte delle righe nude è sceso da 141 a 45 con 78 toppe, e **quattro volte
su nove lotti** quel che ho trovato non era una riga da tradurre: era una
famiglia di cui **una metà era già resa e l'altra no**.

| famiglia | la metà fatta | la metà rimasta |
|---|---|---|
| la scala del potenziale | i sette gradini della scheda (`command.hsp:10677`-`:10700`), toppati da sessioni | i cinque minuscoli di `*dump_chara` |
| le suppliche di chi muore | `proc.hsp:20596`/`:20677`/`:20756`, rese nella 126ª | `ai.hsp:805`/`:813`/`:821`, **giapponese identico parola per parola** |
| «YOU COMMITED TAX EVASION.» | `command.hsp:15556` | `event.hsp:4560` |
| la spiegazione del potenziale | le etichette (toppe) | la `lang()` che le **nomina** (`chat.hsp:14246`) |

⭐⭐⭐ **La terza riga di quella tabella è l'unica che insegni qualcosa di
nuovo, ed è la peggiore: la metà mancante l'ho lasciata IO**, la mattina della
stessa sessione, tre ore prima, col contesto tutto in testa. Le prime due sono
debiti di sessioni vecchie e si spiegano con la memoria; questa no.

> Non è un problema di memoria: è la forma di lavoro. Chi topa una riga guarda
> il **blocco** in cui sta, e il blocco è esattamente l'unità dentro cui una
> gemella non si vede.

**La regola, e costa dieci secondi:** prima di chiudere una toppa si cerca la
stringa **in tutto il sorgente pinnato**, non nel file che si sta guardando.

```
grep -n 'YOU COMMITED TAX EVASION' *.hsp
```

⚠️ **E non basta cercare l'inglese.** Per `ai.hsp` l'inglese delle due gemelle
era **diverso** («my every penny» qui, «all I have» là): a essere identico era
il **giapponese**. La ricerca che paga è quella sull'originale, ed è la regola
della 113ª — *questa stringa è già stata resa altrove?* — applicata dentro le
nostre toppe invece che nel dizionario.

### E la quarta dice l'altra metà: una toppa può far scadere una resa

`chat.hsp:14246` è la lezione dell'istruttore sul potenziale, e diceva «Supreme
è il massimo, Hopeless è il minimo». Era **giusta quando è stata scritta**: a
schermo la scala era inglese. Poi sette toppe l'hanno resa italiana, e da quel
giorno la lezione manda il giocatore a cercare due parole che non esistono più.

⚠️⚠️ **Nessuna rete poteva vederlo.** La spiegazione è dizionario, le etichette
sono toppe, e **nessun referto del progetto mette a confronto i due mondi**. È
la scoperta della 126ª — «le toppe erano l'unico italiano che nessuna rete
avesse mai letto» — vista dal lato opposto: non l'italiano delle toppe che
nessuno legge, ma l'italiano del **dizionario** che una toppa ha reso falso.

💡 Il caso ha una forma riconoscibile: **una voce di dizionario che cita per
nome un'etichetta che vive in una toppa**. Un referto che cerchi le rese
contenenti una parola inglese *che una toppa ha tradotto altrove* le troverebbe
tutte. Non è stato scritto.

---

## La rete che guarda i byte invece di un elenco — 2026-09-02, centoventisettesima

Cinque toppe della 126ª scrivevano nell'italiano `…` (U+2026). CP932 quel
carattere **ce l'ha** — è 0x81 0x63 — quindi
`test_nessuna_toppa_porta_testo_che_cp932_non_sa_scrivere` restava verde: chiede
che il carattere sia **scrivibile**, non che sia **leggibile**. Ma è a doppia
larghezza, e il ramo che la build italiana esegue disegna col carattere latino
di `config.txt`: i due byte diventano due glifi a caso.

La prima stesura della rete nuova copiava l'elenco `PROIBITI` di `guardie.py`
(`…“”～«»`). **La versione buona non ha elenco**: chiede quanti byte CP932 spende
per il carattere, e un carattere che non ci sta in un byte è sbagliato per
costruzione in una riga latina.

> Un elenco enumera i casi che qualcuno ha già visto. Una misura chiude la
> famiglia, compresi i casi che nessuno ha ancora scritto.

E la differenza non è teorica: l'elenco avrebbe lasciato passare `—`, `–`, `’`,
`※`, tutti a due byte come `…` — e **il trattino lungo stavo per scriverlo
davvero**, mezz'ora dopo, traducendo il racconto di Mikraanesis.

⚠️ **La rete è stata esercitata, non solo scritta**: rimettendo il
`toppe.jsonl` di ieri diventa rossa e nomina la riga; con quello di oggi è
verde. Più una seconda prova su righe inventate nei due versi — l'italiano col
`…` accusa, il ramo giapponese con lo stesso `…` no. È la lezione già scritta
nel vault: *una rete mai esercitata non è una rete*, e un cancello booleano non
dice il margine.

ⓘ La deroga è `♪`, ed è vecchia: quel glifo il gioco lo disegna davvero, e le
onomatopee di `proc.hsp` ci contano.

---

## «English», in questa build, vuol dire italiano — 2026-09-02, centoventisettesima

`config.hsp:950`, la scelta della lingua, è `s = "Japanese", "English"`. La resa
è **«Giapponese», «Italiano»**.

Non è una svista e non è una libertà: in questa build il ramo `en` **è** la
traduzione italiana. È lì che vivono le 26.326 firme del dizionario, le 1.166
toppe e i file dati `_it.txt`. Chi sceglie quella voce ottiene l'italiano, e
chiamarla «Inglese» direbbe al giocatore una cosa falsa su quel che sta per
succedere.

ⓘ Il valore scritto in `config.txt` è l'**indice** (`cfg_language`), non la
stringa: l'etichetta non tocca né il salvataggio né la rilettura.

⚠️ **È l'unica resa della 127ª che non sia riscossa da nessuna parte**, ed è
segnata qui apposta. Se un giorno sembrerà sbagliata, si cambia con una riga:
è una toppa sola.

---

## «Master» diceva padrone anche a una giocatrice — 2026-09-02, centoventisettesima

`text.hsp:7051` e `:12081` sciolgono il segnaposto `{syujin}` dei file di
dialogo. Il giapponese sceglie fra 「ご主人様」 e 「お嬢様」 **guardando il sesso
del giocatore** (`:7043`-`:7046`); l'inglese dice «master» in tutt'e due i casi.

⭐⭐ **Qui il sesso del giocatore si conosce, ed è l'eccezione che la guida di
stile prevede.** La regola vieta il participio *quando il genere è ignoto*; qui
il codice lo porta scritto in fronte, dentro un
`if ( cdata(CDATA_SEX, CHARA_PLAYER) == 0 )`. In italiano «padrone» detto a una
giocatrice non è un'approssimazione: è un errore.

La via giusta non si scrive senza rimettere l'`if`, quindi è una **toppa a
blocco** — e la forma non è inventata, è **copiata dal ramo giapponese tre
righe sopra**: stesso `cdata`, stesso ordine, stesso `break`.

> Quando l'inglese collassa due vie che il giapponese tiene distinte, la forma
> da copiare c'è già ed è quella giapponese. Non si progetta: si ricalca.

ⓘ E `{onii}` è 「お兄」/「お姉」, cioè il **vocativo** e non il sostantivo — il
template lo usa come 「{onii}ちゃん」, e la tenerezza sta nel suffisso. La resa è
«fratellone»/«sorellona»: «fratello» renderebbe 兄 e perderebbe il registro,
che è l'unica cosa per cui quel segnaposto esiste.

---

## Tre parole della stessa specie, e una che era già presa — 2026-09-02, centoventisettesima

`economy.hsp:249`-`:255`, l'allineamento della città che si governa: tre parole
in fila, stampate in coda alla riga «Sicurezza (N) …».

- **«Legge», «Neutralità», «Caos»** — tre **sostantivi**, per la regola della
  guida di stile sulle etichette di stato. «Neutrale» sarebbe stato un aggettivo
  in fila con due nomi: le tre parole devono essere della stessa specie, o la
  riga suona rotta senza che nessuna rete lo dica.
- ⚠️ **«Legge» e non «Leggi»**, che in `economy.hsp:468` e `module.hsp:5163` è
  **già preso** e vuol dire un'altra cosa: le ordinanze che il sindaco
  promulga. È il caso della rete 3 — *guarda in che mestiere stava la resa che
  cita* — trovato prima che la rete lo dicesse.

E lo stesso ragionamento su `chara.hsp:4034`, il bollino di un attributo
bloccato: **«Blocco!» e non «Bloccato!»**, perché il bollino sta sopra una
colonna di **nove attributi di genere misto** (Forza e Volontà femminili,
Apprendimento e Carisma maschili) e il participio avrebbe sbagliato l'accordo in
metà delle righe. La parola era già decisa venti righe sopra, dove `:4014` dice
«Blocchi rimasti: ».

---

## ⓘ Aperte alla fine della 127ª

1. **Gli AP di `chara_func.hsp:8430`/`:8522`** — misurata e non chiusa.
   `gain_ap_source` è **operando e testo insieme** (sette confronti lo leggono
   per decidere il ramo) e la frase si compone **per ricorsione** con quattro
   frammenti inglesi, uno dei quali porta `his()` a un argomento, che è
   morfologia. La strada è separare l'operando dalla resa con una tabella al
   sito di stampa: tre basi per cinque code. Il dettaglio è in `invariati.md`.
2. **Un referto per la coda nuda di una `lang()` già resa.** `chat.hsp:17065`
   era la sesta riga di una frase le cui prime cinque erano italiane: a schermo
   si leggeva «…Uscire senza salva ed esci *option from the ESC menu will result
   in a penalty at load time*.» Nessun conteggio poteva distinguerla, perché per
   `nudi_en` è un letterale intatto come gli altri. Il progetto ha
   `code-virgolette.py` per il caso opposto; questo non ce l'ha.
3. **Un referto per la resa che cita un'etichetta toppata** — vedi la prima
   sezione qui sopra.
4. **Le reti sulle toppe**: dopo la 126ª e la 127ª sono tre (participi,
   elisioni, caratteri a doppia larghezza) e **nessuna** guarda il glossario, le
   larghezze o le maiuscole. Sono 905 toppe con testo dentro.

---
