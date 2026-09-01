# -*- coding: utf-8 -*-
"""119a - Lotto 049 di `db_item.hsp`: LE POZIONI, il CORPO, prima meta'.

`FILTER_ITEM_POTION`, righe da `:43900` a `:89561`: **41 righe** su 37 oggetti —
37 dell'indice 0 e **4 dell'indice 2**. La categoria era intatta (82 da fare su
82 vive): dopo questo lotto ne restano **41**, tutte oltre la riga 90.000, ed e'
da li' che parte il 050.

⚠️⚠️ Previsione di `applica`: **+41** per 41 rese. `_previsione.py 049` non trova
gemelle — 41 righe, 41 firme distinte — e `_gia-reso.py 049` dice **0 su 41**:
nessuna di queste prose e' gia' resa altrove nel dizionario.

### ⭐⭐⭐ LA COLA: L'INGLESE SPOSTA DUE FRASI DA UN INDICE ALL'ALTRO

`:55344` e `:55346` sono lo stesso oggetto, e i due testi non si corrispondono
riga per riga:

    JP  description(0)  ...炭酸飲料...飲んだらゲップが出るのは確実。
                        ルートもわからん状態で山に登れば遭難するっていうくらい確実。
        description(2)  (VUOTO)

    EN  description(0)  ...Carbonated beverage... (le due frasi NON ci sono)
        description(2)  \\"If you drink a cola, you'll burp!! Like how you climb
                        a mountain without where the summit is...\\"

Il giapponese mette il rutto e la montagna **in fondo alla descrizione**;
l'inglese le toglie da li' e le rimette **nell'indice 2**, virgolettate, in bocca
a «some weird old guy». Non e' una perdita e non e' un'aggiunta: e' la stessa
battuta spostata di slot.

**La decisione**: si rende la disposizione che il giocatore ha davanti. Il
pannello disegna i tre indici uno sotto l'altro, quindi renderle in tutt'e due i
posti — il giapponese nell'indice 0 e l'inglese nell'indice 2 — le farebbe
leggere **due volte nella stessa schermata**. La battuta resta una sola volta,
nell'indice 2, dov'e' oggi. Il giapponese non perde niente: perde solo il
doppione.

⚠️ E' un caso che nessuna rete puo' vedere. Le due righe hanno firme diverse,
stanno in due indici diversi, e ognuna delle due presa da sola e' a posto: il
doppione nasce **dal pannello**, che le mette insieme.

### ⭐⭐ DUE VOLTE IL NOME ITALIANO ROVESCIA LA FRASE CHE LO SPIEGA

`:61652` e `:61723` aprono tutt'e due dicendo «lo chiamano anche X», e in
tutt'e due X **e' il nome che il giocatore italiano ha sotto gli occhi**:

    riga     nome JP    la frase dice          nome IT            regge?
    :61652   揮発油     «detto anche gasolina»  benzina           NO
    :61723   精油       «detto anche essential oil» olio essenziale  NO

In giapponese la frase informa: l'oggetto si chiama *olio volatile* e c'e' anche
questo altro nome, *gasolina*. In italiano il nome dell'oggetto e' gia'
«benzina», e la frase spiegherebbe il nome col nome — «la benzina, detta anche
benzina».

**La decisione**: si **gira** l'informazione invece di buttarla. «Detta anche
olio volatile», «lo chiamano anche essenza». Il fatto che il giapponese porta —
questa cosa ha due nomi — resta intero, e la frase e' vera davanti al nome che
il giocatore legge. E' la regola della 117a (i pesci che spiegano il proprio
nome): il metro non e' la fedelta' alla parola, e' la verita' a schermo.

### ⚠️⚠️ IL TE' NERO: L'INGLESE HA RICOPIATO LA FRASE DEL TE' VERDE

`:59385` (te' verde) e `:59456` (te' nero) sono due righe consecutive con la
stessa struttura, e il giapponese le oppone su una parola sola:

    :59385   茶葉を極力発酵させないようにして作られる   fermentare il MENO possibile
    :59456   茶葉を完全発酵させて作られる               fermentare DEL TUTTO

L'inglese scrive «made by minimizing the fermentation of tea leaves» **su tutt'e
due**. Sul te' nero e' falso, e non e' un'aggiunta o un appiattimento: e' la
frase dell'altra riga ricopiata dentro questa. La resa italiana segue il
giapponese, come e' regola dalla 26a.

ⓘ Il resto della riga dipende da quella parola: e' la fermentazione completa che
trasforma il mana rimasto nelle foglie, ed e' per questo che il te' nero ridA'
MP mentre il verde no.

### ⚠️ IL CARTELLO E LO STREGONE: `:56473`

L'indice 2 dell'urina porta due testi che non c'entrano niente l'uno con
l'altro. Il giapponese e' un **cartello**: 「ここにおしっこをさせないでください」,
*non fate pipi' qui*, firmato ～根元の濡れた標識～ (il cartello bagnato alla
base). L'inglese scrive «Dare you enter my magical realm?» firmato «the
Whizzard» — un gioco di parole su *wizard* e *whizz*.

**La coda italiana viene dal giapponese** (la tabella della 112a e' indicizzata
per giapponese: `~Il Cartello Bagnato alla Base~`), quindi il corpo deve venire
di li' pure: una firma che dice «cartello» sotto una battuta da stregone sarebbe
un pannello che si contraddice da solo.

### ⓘ Le altre cose che il lotto ha deciso

  - **`gli dei` senza accento.** Il preflight ha respinto `dèi` su `:71997` e
    `:72070`: `reimporta` non accetta l'accento **dentro** la parola, perche' la
    degradazione ad apostrofo esiste solo in coda. Il progetto scrive «degli
    dei» dappertutto in `chat.hsp`, quindi non c'era niente da inventare;
  - **`il te di ieri`, due volte.** 過去のあなた torna su `:83835` (la pozione
    del declino, che abbassa il livello) e su `:89149` (il sangue di Ermes, che
    alza la velocita' per sempre): due effetti opposti, la stessa immagine. Le
    due rese la dicono nello stesso modo, e la forma non chiede il genere del
    giocatore (`guida-stile.md`);
  - **`bannou mugi`** su `:55415`: il dizionario l'ha gia' traslitterato, ed e'
    la regola della 111a — un termine coniato che l'inglese traslittera resta
    traslitterato;
  - **`pericolosissima` sciolta prima di reimportare.** Il preflight l'ha data
    a 15 caratteri, dentro la finestra di rinculo dell'impaginatore. Il numero
    che decide e' quello di `_107-descrizioni-item`, ma scioglierla costava una
    parola: `:83835` dice «molto pericolosa».

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le code del lotto sono **nove**, tutte gia' in tabella con una sola resa
italiana (`_code.py 049`: righe senza resa in tabella **0**). Il cancello
«titoli resi in PIU' modi» resta a **7**.

⚠️ La forma, da `_forma.py 049`: **21** righe su 41 hanno lo spazio prima del
`\\n` e 20 no; **18** code hanno lo spazio dopo il `#` e 23 no. Le due cose non
vanno insieme — `:81811` ha lo spazio prima del `\\n` e non dopo il `#`,
`:65671` il contrario — e si copiano riga per riga.

⚠️ `:89149` e' l'unica delle 41 il cui inglese chiude con un `\\n` **dopo** la
coda. Il preflight se n'e' accorto contando i segmenti.
"""
