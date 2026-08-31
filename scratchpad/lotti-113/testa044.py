# -*- coding: utf-8 -*-
"""116a - Lotto 044 di `db_item.hsp`: I CIBI, il primo lotto della categoria.

`FILTER_ITEM_FOOD`, righe da `:68650` a `:88275`: **39 righe** su 34 oggetti —
34 dell'indice 0, nessuna dell'indice 1 e 5 dell'indice 2. Restano **59 righe**
per due lotti.

⚠️ Previsione di `applica`: **+39**, fatta contando il giapponese nel sorgente
(la lezione del 042). Zero righe gemelle in questo lotto.

### ⭐⭐⭐ `_corpo.py` NON FILTRA LE RIGHE GIA' RESE, E QUI SI E' VISTO

`python _corpo.py 044 FILTER_ITEM_FOOD 0 200000` ha detto **148 righe**, ma
`_114-corpo-da-fare` dice **98 da fare su 148 vive**. Le altre 50 sono gia'
rese: `_107-chiavi-item.py` filtra per categoria, indice e intervallo, e
**basta** — «gia' tradotta» non e' fra i suoi filtri.

⚠️⚠️ Non era mai emerso perche' nelle quattro categorie chiuse finora tutto era
da fare, e i due numeri coincidevano. Su una categoria **cominciata a meta'** un
lotto costruito a occhio dall'uscita di `_corpo.py` riscriverebbe da capo 50
rese gia' in gioco, e **niente lo fermerebbe**: il preflight controlla che le
chiavi siano quelle di `righeNNN.py`, non che siano da fare.

⭐ **Come si e' evitato:** contando prima di scegliere l'intervallo. Le 50 gia'
rese sono un prefisso pulito, `:42782`-`:67985`, e le 98 da fare cominciano a
`:68650`: per questo il lotto parte da 68000. Su un'altra categoria potrebbero
essere sparse, e allora l'intervallo non basterebbe.

### ⭐⭐⭐ UNA RIGA HA IL GIAPPONESE E L'INGLESE CHE PARLANO DI DUE COSE DIVERSE

`:70398` e' l'indice 2 della castagna. Il giapponese e' una battuta:

    「う、うにを粗末にするとバチが当たるんですよ！」
    #～怯える錬金術士の『ナプラス』の言葉～

L'inglese, nella stessa posizione, e' il **testo generico** del rapporto di
identificazione: «A type of nut that restores satiety, it's used to make
candies.» con la coda `~Identification Report: <Food> Category~`.

⚠️ Non e' uno slittamento: si e' guardato il sorgente riga per riga
(`:70392` contro `:70398`), e le posizioni corrispondono. E' una **sostituzione**
fatta a monte, nel ramo inglese.

⚠️⚠️ **E il cancello non se ne accorgeva, per come e' fatto.** `_code.py` cerca
prima la coda giapponese in tabella; ～怯える錬金術士の『ナプラス』の言葉～
non c'era, quindi **ripiegava sull'inglese**, trovava il rapporto di
identificazione e assegnava quel titolo. Il referto «righe senza resa in
tabella: 0» restava verde su una riga sbagliata.

⭐ **Quanto e' grande la famiglia**: `scratchpad/_116-code-discordi.py`, nuovo,
guarda tutte le righe che hanno **tutt'e due** le code e chiede se indicano lo
stesso libro. Su **1.411** righe, le discordi sono **1**: questa. Un difetto
puntuale di monte, non un difetto della nostra estrazione.

**La decisione (dell'utente):** si rende il **giapponese**. Il titolo mancante
e' stato aggiunto alla tabella e al glossario come
`~Parole di <Naplus> l'alchimista spaventata~` — ナプラス e' donna, lo dice
`chat.hsp` («mi ha chiesto di portarle»), e `錬金術士の『ナプラス』` e' gia'
reso «<Naplus> l'alchimista».

⚠️⚠️⚠️ **IL CANCELLO «TITOLI RESI IN PIU' MODI» PASSA DA 6 A 7, ED E' QUESTA
RIGA.** Il settimo e' l'inglese `~Identification Report: <Food> Category~`, che
adesso copre due italiani: il rapporto di identificazione (nelle venti righe di
indice 2 dei cibi, dove il giapponese e' **vuoto**) e le parole di <Naplus>
(qui, dove il giapponese c'e' e dice un'altra cosa). **Il valore atteso in
apertura non e' piu' 6: e' 7.** Un **8** sarebbe un difetto nuovo.

⭐ E la battuta si regge da sola, perche' il dizionario la spiegava gia':
`chat.hsp` dice che «quelli che si dicono alchimisti, quando tirano una
castagna, insistono» che sia un riccio di mare, e 「うにーっ！」 e' reso
«Ricciooo!». Naplus e' una di quelli.

### ⭐⭐ IL LOTTO E' IL PRIMO DISOMOGENEO, E DI MOLTO

    24 righe su 39 hanno lo spazio prima del `\\n`, 15 no
    30 code su 39 sono `#~` senza spazio, 9 sono `# ~` con lo spazio
     1 riga (`:78596`) ha un `\\n` in PIU' in fondo, dopo la coda

Nel 041 le eccezioni erano tre, nel 042 e nel 043 zero. Qui non c'e' una regola
da ricordare: c'e' una tabella da leggere.

⭐ Per questo e' nato `scratchpad/lotti-113/_forma.py NNN`, che mette insieme
in una riga sola quel che prima stava in due strumenti — lo spazio prima del
`\\n` (da `_scheda034.py`) e la coda italiana esatta (da `_code.py`). Il
preflight ha poi trovato l'unica cosa che era sfuggita, il `\\n` in piu' di
`:78596`.

### ⚠️ L'INGLESE LASCIA CADERE TRE FRASI, E UNA CAMBIA IL SENSO

  - `:69598` (il mais): ちなみにヒゲのような部分には利尿作用がある — la barba
    del mais fa venire da urinare. Sparita;
  - `:69669` (la patata): イーモとほぼ同種だが、大きくてやや不格好 — che e'
    quasi la stessa specie dell'**imo**, ma piu' grande e sgraziata. E' la
    **prima** frase, e l'inglese attacca dalla seconda;
  - `:70671` (il granchio del cocco): 弱りはするが — «si indebolisce, si', ma»
    bollirlo non basta a ucciderlo. L'inglese scrive «Although they are boiled
    this way, they are still alive», che perde la concessione e dice una cosa
    piu' forte di quella scritta.

### ⭐ LO ZUCCHERO E IL SALE SONO SPECULARI, E L'INGLESE ROMPE LO SPECCHIO

`:78529` e `:78596` sono in giapponese **la stessa frase** con dolce e salato
scambiati: «aggiunge dolcezza / aggiunge sapore salato... tira fuori il sapore
pieno e il salato / il dolce». L'inglese riscrive la seconda da capo, piu'
lunga e con altre parole. L'italiano tiene lo specchio.

ⓘ Ed e' la riga con il `\\n` in piu': la stessa voce che l'inglese ha riscritto
e' anche l'unica del lotto con la struttura diversa. Le due cose vanno insieme —
qualcuno ha rimesso mano a quella riga sola.
"""
