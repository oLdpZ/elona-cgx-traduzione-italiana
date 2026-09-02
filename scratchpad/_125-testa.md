# Ripresa sessione

Aggiornato: 2026-09-02, fine della **centoventicinquesima** sessione (**26 rese
che chiudono `custom_itemenchantment.hsp`, tre righe inglesi nude, e due valori
attesi del referto d'apertura che erano falsi**).

⚠️⚠️⚠️ **L'ESEGUIBILE IN GIOCO E' QUELLO DELLE 03:13 DEL 02/09**, ricompilato e
ricopiato a mano dopo il lotto. Se la data e' quella, non c'e' niente da rifare.
ⓘ La data esatta si legge con `ls -l C:\Games\Elona\elonaplus2.31\cgx-test.exe`.

⭐⭐⭐ **QUANTO MANCA: 141 FIRME IN DUE FILE.** E' l'unico fronte di traduzione
aperto, e il conto **non si eredita da qui** — si rilancia:

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/perimetro.py

        firme rese                              26.185
        firme ancora da fare, contate              141
        --- fatto 26.185 su 26.326             = 99,5%

        txtadv.hsp                117
        net.hsp                    24

ⓘ Gli altri due file senza dizionario, `custom_pet.hsp` e `custom_dmgpop.hsp`,
hanno **una firma sola ciascuno ed e' muta**: non si chiuderanno mai
traducendoli, sono gia' finiti (124a).
⚠️ **`txtadv.hsp` ha anche dodici righe inglesi nude** (`noteadd "3 putits!"` e
le altre), che il lotto non raggiunge: chi lo apre le guardi subito con
`nudi_en.py`, perche' sono meta' del lavoro vero di quel file.

⚠️⚠️⚠️ **E IL 99,5% E' IL PERIMETRO, NON IL PROGETTO.** Il debito di collaudo
sale da 9.349 a **9.375**: **nessuna delle 26 rese di oggi e' stata vista a
schermo**, e nemmeno le tre toppe.

---

## `custom_itemenchantment.hsp` SI CHIUDE, E DICIASSETTE RESE ERANO GIA' DECISE

⭐⭐⭐ **IL GIAPPONESE DI QUESTO FILE E' RICOPIATO IDENTICO DA `chat.hsp`.**
`scratchpad/_125-sorelle-itemench.py` ha cercato per somiglianza su tutto il
dizionario e ha trovato **17 identiche, 4 somiglianti, 5 sole**: il file e' la
copia che Custom-GX ha fatto del fabbro di monte (`chat.hsp:11290`-`:11661`).

⚠️⚠️ **E le due versioni sono tutt'e due vive**, non e' codice morto sostituito:
`chat.hsp:23306` manda qui su `chatval == 114514` e `chat.hsp:11287` tiene la
fusione originale su `chatval == 1`. Stesso fabbro, due voci di menu vicine. Le
diciassette si **copiano**, non si riscrivono.

⚠️⚠️⚠️ **IN QUESTO FILE LA FONTE SCRITTA E' L'INGLESE, NON IL GIAPPONESE**, ed
e' la prima volta che la regola della 109a («si guarda quale fonte e' stata
copiata e quale e' stata scritta») viene usata **al rovescio**. Ne seguono due
trattamenti:

  - giapponese = frase di monte, inglese riscritto → vale la resa gia' decisa;
  - giapponese = **moncone** (むむむ。, すまんのう。, どうだろう), inglese col
    contenuto vero del mod → si rende **dall'inglese**. Sono `:115`, `:267`,
    `:274`, `:276`: senza, il giocatore italiano leggerebbe «Mmm.» dove
    l'inglese gli dice **quanto oro costa** e **quale pozione serve**.

⭐ **Il prefisso del punteggio si tiene** (`:67`, `:108`, `:267`): «Sulla scala
di Thalia quest'oggetto sta a *p* su *p(1)*…». E' il numero concreto della scala
di cui `:58` parla in astratto, ed e' l'unico posto dove il giocatore lo legge.
ⓘ La prova che e' voluto sta dentro il file: `:290` ha lo **stesso giapponese**
di `:67` e l'inglese **senza** prefisso, perche' li' e' gia' stato mostrato a
`:267`. Due firme, due rese.

⚠️ **`:88` era gia' deciso e non e' colpa di Custom-GX**: la voce di menu dice
«Sorry.» dove il giapponese dice エンチャントひとつ消去 — ma anche
`chat.hsp:11347` di monte dice «Sorry.», ed e' gia' resa «Cancellare un
incanto». Cercare la sorella ha evitato di ridecidere una cosa decisa.

---

## LE TRE TOPPE DELLA 125a, E IL CANCELLO CHE NON LE VEDEVA

`nudi_en.py` trovava **tre righe inglesi nude** in questo file, tutte lette a
schermo nel menu della disincantazione:

    :256   s = "[" + p_gold + " gold] " + s          -> "[N oro] "
    :278   s = "Try to remove the enchantment? (…)"  -> "Indebolire? (…)"
    :280   s = "Remove the enchantment? (…)"         -> "Cancellare? (…)"

⭐⭐⭐ **«Try to remove» ERA L'INDEBOLIMENTO.** `:279` sceglie fra le due con
`p_rem == val(1)`, che e' **la stessa condizione** con cui `:324` stampa
«…removed!» contro «…**weakened**!». Il codice lo dice due volte a due righe di
distanza, e l'inglese e' vago dove il codice e' preciso. Vince il codice — la
quinta fonte della 110a — **contro la fonte scritta, nello stesso file in cui la
fonte scritta e' l'inglese**.

⚠️⚠️⚠️ **E LE TRE VOCI DI MENU NON CI STAVANO, SOTTO UN CANCELLO VERDE.**
`menu_dialogo` ha detto «0 su 1383» con tre voci fuori misura dentro, e non e'
rotto: guarda un insieme che non le contiene.

  1. legge il **dizionario**, e una riga di toppa voce di dizionario non ce l'ha:
     `:278` e `:280` non sono nemmeno nel **denominatore**;
  2. `:276` nel dizionario c'e', ma `reso()` conta una **chiamata di funzione
     come lunga zero**: `cnvitemname()` a schermo sono fino a 38 caratteri.

⚠️ **Il caso peggiore non e' quello che viene in mente**: «pergamena di
acquisizione di attributi» sono **38** caratteri contro i 24 di «scroll of gain
attribute», su un tetto di 58. Restano 18 per l'etichetta, e allora l'etichetta
e' il **verbo solo**. Il cancello e'
`scratchpad/_125-larghezze-menu-incanti.py`, e la sua prova al contrario non e'
una stringa finta: sono le **tre stesure vere scartate**, e si accende su due.

⭐ **Regola:** quando una toppa mette **testo che si legge a schermo** dentro un
contenitore misurato, il cancello di quel contenitore va guardato in faccia —
non basta che sia verde, bisogna sapere se quella riga sta nel suo denominatore.
ⓘ La forma generale manca: `nudi_en.py` sa **quali** righe sono di toppa e
`menu_dialogo.py` sa **come** si misura una voce; nessuno dei due sa dell'altro.
Un cancello che leggesse la **build** invece del dizionario li unirebbe, ed e' il
candidato piu' ovvio per la prossima sessione che voglia costruire.

---

## I VALORI DA ASPETTARSI IN APERTURA, DOPO LA 125a

    pytest                   794 passed, 6 skipped
    prova_identita           72/72 e 30.905, **invariato**
    applica                  **30.562** sostituzioni piu' **3 toppe**
                             (era 30.532: +30, previsione esatta)
                             ⓘ le toppe si contano a parte, riga per file
    perimetro.py             **26.185 fatte, 141 da fare, 99,5%**
    _125-previsione          30 righe di sorgente per 26 voci: quattro firme
                             hanno una **gemella** (:85/:247, :86/:283,
                             :115/:119, :301/:317)
    _123-file-senza-dizionario  **147 firme in 4 file**, 6 mute, **141 da fare**
                             ⚠️ referto: il valore atteso NON e' zero
    _125-larghezze-menu-incanti  rese **0 fuori misura**, monte 0,
                             prova al contrario accesa su **2**
    toppe                    **1034**, e `_97-toppe-agganciate` **1034 su 1034**
    nudi_en                  struttura 1044, **ancora da fare 414** (era 417);
                             `custom_itemenchantment.hsp` **0 intatte**
    referti                  **participi 9, elisioni 0**
                             ⓘ rilanciato in chiusura DOPO l'ultima resa
    _108-accento-decomposto  **0 su 26.185**

⚠️⚠️⚠️ **DUE VALORI ATTESI DELLA 124a ERANO FALSI, E SONO STATI CORRETTI QUI.**
Non erano regressioni, ed e' la **quarta** volta che questo referto porta un
numero scritto a mano che non torna:

    verifica --dizionario    **112 «non ancora tradotte» in 19 file**
                             ⚠️⚠️ NON «tutti 0 e 0»: `confronta_col_sorgente`
                             (`verifica.py:619`) fa `nel_sorgente - tradotte` e
                             **non toglie le rinviate**. Il valore atteso non
                             poteva essere zero nemmeno il giorno che fu scritto
    _97-quanto-resta         TOTALE **112 / 112 / 0**
                             ⚠️ la 124a scriveva 111, e il numero era gia' 112
                             al suo commit: `git status --short` dice che
                             nessuno dei 19 dizionari e' stato toccato oggi
    _125-non-tradotte        **112 non tradotte, 112 rinviate, 0 FUORI**
                             ⭐ e' la domanda giusta — *di chi sono quelle
                             righe?* — e il numero che conta e' l'ultimo

⭐ **Regola:** un valore atteso che il referto non sa rigenerare da solo non si
scrive come **numero**, si scrive come **comando**; e dove il comando non c'e',
la riga dice **da che cosa** viene il numero, cosi' chi lo trova diverso sa dove
guardare invece di chiedersi se ha rotto qualcosa.

Tutto il resto e' **fermo dov'era**: `dati_applica --identita` 6 file e 3.767
righe, `rinviate.jsonl` **114 righe / 111 firme distinte**, `creature`
1131/2466/0/0, `larghezze` 0 fuori misura, `menu_dialogo` 0 su **1383**,
`diario` 0 su 205, `riquadri` 0 su 38 e 0 su 71, `linguette` 0 e 0,
`battute --divergenti` 13, `dati_sorgente` 7/7 e gioco difforme su 0, `gronde`
0 su 5, `maiuscole` 143/6/1/7/0, `bilingui` 0, `lang-nel-ramo-jp` 21 | 0,
`_96-morte-nella-build` 0, `_107-descrizioni-item`, `_114-corpo-da-fare`,
`_112-corpo-descrizioni` 7, `_113-fonti-gia-rese` 46 su 202,
`_115-fonti-storpiate` 7 su 2.542, `_116-code-discordi` 1 su 1.411,
`_118-nomi-vs-incantesimi` 2 e 37 su 80, `_122-inglese-doppio-item` 10 e 27,
`_123-larghezze-materiali` 0 e 0, `_124-larghezze-produzione` tutti 0,
`_124-nomi-mappa` 0 e **21**, `intestazioni_larghezze` perimetro 0.

⚠️⚠️ **TUTTO E' COMMITTATO** e l'albero e' pulito.

⚠️⚠️⚠️ **LE OTTO COSE APERTE DELLA 124a RESTANO TUTTE APERTE**, e vanno decise,
non ereditate: il rango dei grimori; i 37 nomi di grimorio discordi; i dodici
nomi delle pietre dei mesi; «vento di etere» contro «vento d'etere»; il genere
di due divinita'; «stivali» contro «scarpe»; 機械弓 reso in due modi; e i
**ventuno nomi di mappa** che si tagliano al tetto stretto di 12 caratteri.
⭐ **La lista di collaudo che serve adesso e' ancora quella**: i ventuno nomi di
mappa, che si guardano entrando in quelle mappe e leggendo la barra in alto. E'
l'unica prova che il codice non sa dare, perche' dipende da `adata(ADATA_TYPE)`
a tempo di esecuzione. ⓘ E da oggi c'e' una seconda lista corta: **il menu del
fabbro** — la fusione (`chatval 114514`) e la disincantazione (`69000`), dove le
tre voci nuove e il prefisso del punteggio si leggono in due minuti.

---
