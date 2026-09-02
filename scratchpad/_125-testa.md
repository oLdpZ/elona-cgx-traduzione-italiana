# Ripresa sessione

Aggiornato: 2026-09-02, fine della **centoventicinquesima** sessione (**167 rese
in tre file, il perimetro `lang()` chiuso al 100%, 17 toppe, e un test che ha
fermato un lotto per una cosa che non era ancora successa**).

⚠️⚠️⚠️ **L'ESEGUIBILE IN GIOCO E' QUELLO DELLE 08:40 DEL 02/09**, ricompilato e
ricopiato a mano dopo l'ultima resa. Se la data e' quella, non c'e' niente da
rifare. ⓘ Si legge con `ls -l C:\Games\Elona\elonaplus2.31\cgx-test.exe`.

⭐⭐⭐ **IL PERIMETRO `lang()` E' CHIUSO. 26.326 SU 26.326, ZERO DA FARE.**
Il conto **non si eredita da qui** — si rilancia:

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/perimetro.py

        firme rese                              26.326
        firme ancora da fare, contate                0
        --- fatto 26.326 su 26.326            = 100,0%

ⓘ I due file che restano nell'elenco, `custom_pet.hsp` e `custom_dmgpop.hsp`,
hanno **una firma sola ciascuno ed e' muta**: erano gia' finiti dalla 124a e non
si chiuderanno mai traducendoli.

⚠️⚠️⚠️ **E IL 100% NON E' LA FINE DEL PROGETTO. RESTANO DUE FRONTI VERI.**

  1. ⭐ **212 righe inglesi nude che sono TESTO** — `nudi_en.py` ne conta 400
     ancora intatte, e `triage_nudi.py` le spacca: **212 testo**, 87 sigle (i
     nomi delle tracce del jukebox), 93 `dbg` (la console da mago) e 22 spente
     dentro un commento. Le 212 non passano da nessuna `lang()`, non hanno
     firma, non hanno voce di dizionario e **nessun lotto puo' raggiungerle**:
     si toccano solo con una toppa. Stanno in **blocchi**, e un blocco e' una
     schermata sola:

        13  item_func.hsp   *skipName            13  proc.hsp   *jump_changeCreature
        11  item_func.hsp   *itemname             9  map_rand.hsp *map_randomDungeon
         9  system.hsp      *game_title           8  command.hsp *txttargetnpcextrainfo
         8  config.hsp      *com_config_loop_WHILE1

     💡 **Questo e' il fronte da aprire domani**, ed e' l'unico rimasto che sia
     lavoro di traduzione. Si comincia da `triage_nudi.py`, non da `nudi_en.py`.
  2. Il **debito di collaudo**, sotto.

⚠️⚠️⚠️ **IL DEBITO DI COLLAUDO E' 9.516 E NON E' MISURATO DA NIENTE.** E' un
numero tenuto **a mano** in questo documento, non c'e' nessuno strumento che lo
calcoli, e vale come ordine di grandezza e non come misura. ⓘ Nessuna delle 167
rese di oggi e' stata vista a schermo, e nemmeno le 17 toppe.

---

## I TRE FILE CHIUSI, E CHE COSA AVEVANO DENTRO

### `custom_itemenchantment.hsp` — 26 rese, 17 gia' decise altrove

Il giapponese di questo file e' **ricopiato identico** da `chat.hsp:11290`-
`:11661`: e' la copia che Custom-GX ha fatto del fabbro di monte.
`scratchpad/_125-sorelle-itemench.py` (la regola della 113a applicata al lotto
intero) trova **17 identiche, 4 somiglianti, 5 sole**.
⚠️ **Le due versioni sono tutt'e due vive** — `chat.hsp:23306` manda qui su
`chatval == 114514`, `chat.hsp:11287` tiene l'originale su `chatval == 1` — e
per questo le 17 si **copiano**, non si riscrivono.

### `net.hsp` — 24 rese, le funzioni in rete

L'urna del **voto per l'esecuzione** dei lupi mannari, quella del **voto per
l'epiteto** (il CGI di nifty.com, oggi fermo), la chat verso il server e le due
finestrelle del caricamento file e del browser.
⚠️ **`:375` e' un difetto di monte**: tre righe portano lo stesso inglese e i
giapponesi sono due, e il codice da' ragione al giapponese (`:373` guarda
`MDATA_WEREWOLF_STAGE == 0`, cioe' *nessuna votazione in corso*; `:563` e `:715`
guardano `GDATA_NEXT_VOTE`, cioe' *il tuo diritto di voto*).
⚠️ **Quattro voci restano identiche all'inglese** e sono dichiarate in
`invariati.md`: uno spazio e due parentesi, cioe' cornice.

### `txtadv.hsp` — 117 rese, l'esplorazione e il casino'

⚠️⚠️⚠️ **Le slot sono inglese scritto su giapponese ricopiato a caso**, e il
segnaposto non e' nemmeno la riga giusta: `:1183` porta la spiegazione del
blackjack sotto l'inglese delle slot, `:1253` porta «che faccio?» sotto «Wheel
of Fortune», `:799` porta «blackjack» sotto «I want to play Slots».
⭐⭐ **E tre punti dell'esplorazione sono lo stesso caso dentro il codice di
monte**, dove a smentire il giapponese sono le **abilita' controllate due righe
sopra**: `:507` CARPENTRY/WEIGHT_LIFTING e' un tronco, `:516` TACTICS/STEALTH
sono yeek kamikaze, `:525` LITERACY/MEMORIZATION sono iscrizioni magiche — e
tutte e tre hanno il giapponese di `:498`, «ho trovato dei resti».
⚠️ **`:665` stampa la parentesi due volte in giapponese** (`"叩き割る(筋力: "`
piu' il `"(" + skillname(...)` che la riga ci attacca): l'inglese ha buttato il
pezzo di troppo e l'italiano pure.

---

## LE DICIASSETTE TOPPE DELLA 125a

    custom_itemenchantment.hsp   3   l'etichetta del prezzo e due voci di menu
    txtadv.hsp                  12   gli esiti delle slot («3 putits!» e sorelle)
    net.hsp                      2   «[Chat Skipped]» e l'errore di connessione

⭐ **«Try to remove» era l'indebolimento.** `custom_itemenchantment.hsp:279`
sceglie fra le due voci con `p_rem == val(1)`, che e' **la stessa condizione**
con cui `:324` stampa «…removed!» contro «…**weakened**!». Il codice lo dice due
volte a due righe di distanza, e l'inglese e' vago dove il codice e' preciso.

⚠️⚠️ **`net.hsp:263` NON e' stata toppata apposta.** Assegna `"net"` alla
casella che finisce nella colonna di destra dell'urna: che cosa ci faccia li'
non si capisce dal sorgente, e a schermo ci si arriva solo con un server che
risponde. Resta nell'elenco di `nudi_en.py`: **misurata, non decisa**.

---

## IL TEST CHE HA FERMATO UN LOTTO, E LA GEOMETRIA CHE HA COSTRETTO A LEGGERE

⭐⭐⭐ Dopo il reimporta di `txtadv.hsp`, `pytest` e' passato da 794 verdi a **1
rosso**: `test_le_voci_tradotte_stanno_tutte_in_un_contenitore_misurabile`.
`menu_dialogo.py` elencava `com_txtadv_loop` fra i «non misurati» dalla 72a, e
nessuno ci aveva mai messo una resa dentro; con questo lotto ce ne sono finite
**quaranta** in un colpo.
**E' la prima volta che una rete del progetto ferma un lotto per una cosa che
non era ancora successa.** Non ha trovato un danno: ha impedito un permesso.

    txtadv.hsp:157-161   x = 170, 400 ; gcopy 2, x, y, x(1), y(1)
    txtadv.hsp:173       cs_list s, 170 + 30, …
    module.hsp:70        limit(strlen(…) * 7 + 32 + arg5, 10, 480)

⚠️⚠️ **Qui non c'e' un taglio: c'e' una SCIA.** Il ciclo ripulisce a ogni giro
la striscia 170..570 ricopiandola dal buffer pulito, e la barra evidenziata
parte da 200: quel che finisce oltre i 570 **non viene ripulito** e resta a
schermo. Tetto `(570 - 200 - 34) / 7 = 48`, entrato in `menu_dialogo.py` come
**quinto contenitore** (`SCHERMATA_TXTADV`). Le voci misurate salgono da 1.383 a
**1.423**.
⚠️ **E monte stesso puo' sforare**, su `:1256`: 25 caratteri fissi piu' un
`itemname()`, e oltre i 23 di nome la barra passa i 570 **anche in inglese**. Per
questo la resa italiana di quella riga e' piu' **corta** della parte fissa
inglese invece che piu' lunga.

⚠️⚠️ **Le altre due geometrie di quella schermata restano fuori dalle reti**, e
le misura `scratchpad/_125-larghezze-txtadv.py`: le righe di **messaggio**
(`pos 170`, font 14, metro = monte, **71 caratteri**) e il **pannello in alto**
(`screen.hsp:100`, font 11, tetto **51**, e il passo di 6,5 px lo dichiara il
gioco stesso). ⓘ Per il font 14 il passo **non e' misurato a schermo e non si
inventa**: la 118a ha gia' insegnato che prendere una costante da un'altra rete
dicendo «tanto e' lo stesso carattere» e' esattamente il difetto.

---

## IL REFERTO DEI PARTICIPI, E PERCHE' VA RILANCIATO IN CHIUSURA

⭐⭐ `scratchpad/referti.py` e' passato da **9 participi a 15** dopo il lotto di
`txtadv.hsp`, e tutte e sei le nuove erano rese di oggi che danno del
**maschile** al giocatore, che in Elona puo' essere donna:

    «Ti sei perso!»                   ->  «Hai perso la strada!»
    «Sei inciampato … e sei caduto!»  ->  «Inciampi in un sasso e cadi!»
    «Ti sei seduto e ti sei riposato» ->  «Ti siedi e riprendi fiato»
    «Ti sei stirato un muscolo»       ->  «Ti stiri un muscolo»
    «Ti sei fatto male nel farlo»     ->  «Ti fai male nel farlo»
    «Ti hanno beccato a barare»       ->  «Ti hanno visto barare»

⭐ **Il rimedio non e' una perifrasi faticosa: e' il presente.** Cinque su sei si
risolvono cambiando tempo, e il testo ci guadagna in immediatezza.
⚠️⚠️ **E il referto le ha viste solo perche' e' stato rilanciato in chiusura**
(regola della 120a). Rilanciato in apertura avrebbe detto 9, cioe' il numero di
ieri. I nove che restano vengono da `chat.hsp` e sono di sessioni vecchie.

---

## I VALORI DA ASPETTARSI IN APERTURA, DOPO LA 125a

    pytest                   794 passed, 6 skipped
                             ⓘ rilanciato DOPO aver scritto i documenti
    prova_identita           72/72 e 30.905, **invariato**
    applica                  **30.764** sostituzioni piu' **17 toppe**
                             (era 30.532: +30 itemench, +32 net, +170 txtadv)
    perimetro.py             **26.326 fatte, 0 da fare, 100,0%**
    _123-file-senza-dizionario  **2 firme in 2 file, 2 mute, 0 da fare**
    nudi_en                  struttura 1044, **ancora da fare 400** (era 417)
    triage_nudi              **testo 212**, sigla 87, dbg 93, spenta 22
                             ⭐ le 212 sono il fronte di domani
    toppe                    **1048**, e `_97-toppe-agganciate` **1048 su 1048**
    menu_dialogo             0 fuori misura su **1423** (erano 1383)
                             ⓘ il quinto contenitore e' `com_txtadv_loop`
    _125-larghezze-txtadv    messaggio/menu/pannello **0 fuori**, prova al
                             contrario accesa su **3 classi su 3**
    _125-larghezze-menu-incanti  rese 0 fuori, prova al contrario accesa su 2
    referti                  **participi 9, elisioni 0**
                             ⚠️ rilanciato DOPO l'ultima resa, non prima
    _108-accento-decomposto  **0 su 26.326**
    verifica --dizionario    **112 «non ancora tradotte» in 19 file**
                             ⚠️⚠️ NON «tutti 0 e 0»: `confronta_col_sorgente`
                             (`verifica.py:619`) **non toglie le rinviate**
    _97-quanto-resta         TOTALE **112 / 112 / 0**
    _125-non-tradotte        **112 non tradotte, 112 rinviate, 0 FUORI**
                             ⭐ e' la domanda giusta, e il numero e' l'ultimo

Tutto il resto e' **fermo dov'era**: `dati_applica --identita` 6 file e 3.767
righe, `rinviate.jsonl` 114 righe / 111 firme, `creature` 1131/2466/0/0,
`larghezze` 0, `diario` 0 su 205, `riquadri` 0 su 38 e 0 su 71, `linguette` 0 e
0, `battute --divergenti` 13, `dati_sorgente` 7/7 e gioco difforme su 0,
`gronde` 0 su 5, `maiuscole` 143/6/1/7/0, `bilingui` 0, `lang-nel-ramo-jp`
21 | 0, `_96-morte-nella-build` 0, e tutti i referti da `_107` a `_124`.

⚠️⚠️ **TUTTO E' COMMITTATO E SPINTO** su `origin/fase-0`, e l'albero e' pulito.
ⓘ La 125a e' stata chiusa dicendo **«riprendo in un altro terminale»**, come le
nove sessioni prima: la macchina e' la stessa, ma la sessione nuova non ha in
memoria niente di questa.

---

## LE COSE APERTE, CHE VANNO DECISE E NON EREDITATE

Le otto della 124a restano **tutte aperte**: il rango dei grimori; i 37 nomi di
grimorio discordi; i dodici nomi delle pietre dei mesi; «vento di etere» contro
«vento d'etere»; il genere di due divinita'; «stivali» contro «scarpe»; 機械弓
reso in due modi; i **ventuno nomi di mappa** che si tagliano al tetto di 12
caratteri. Se ne aggiungono tre, tutte **misurate e non decise**:

  9. ⭐ **異名 e' reso in due modi dentro la STESSA funzione**: «epiteto» in
     `action.hsp:2238`, `chara.hsp:3187` e `:3196`, «alias» in
     `command.hsp:4566` e `:10504`. In prosa e' «soprannome» otto volte su otto,
     e quello e' un caso diverso e va bene. ⚠️ `command.hsp:10504` e'
     l'etichetta della scheda e ha un budget di larghezza: il cambio va
     **misurato prima di farlo**, e «Epiteto» sono due caratteri piu' di
     «Alias». La 125a ha reso `net.hsp:604` con «epiteto», che e' la
     maggioranza e la parola delle sue sorelle nella stessa finestra;
 10. **カジノチップ e' reso in due modi**: «fiche da casinò» in
     `material_data.hsp:14` — che e' quello che `matname(1)` restituisce, cioe'
     quello che il gioco compone — e «chip da casinò» in altre due righe. Le
     rese di `txtadv.hsp` usano `matname(1)`, quindi dicono «fiche»;
 11. **`net.hsp:263`**, la parola `"net"` nella colonna dei voti (sopra).

⭐⭐⭐ **LA LISTA DI COLLAUDO CHE SERVE ADESSO, in ordine di costo.** Nessuna
delle 167 rese e' stata vista a schermo, e tre schermate nuove si guardano in
pochi minuti:

  1. **il menu del fabbro** — fusione (`chatval 114514`) e disincantazione
     (`69000`): le tre voci nuove («Potenziare?», «Indebolire?», «Cancellare?»),
     il prefisso del punteggio e l'etichetta del prezzo `[N oro]`;
  2. **la schermata testuale** — l'esplorazione di un sito casuale e il casino'
     (blackjack e slot): e' l'unico posto dove si vede se il tetto di 48
     caratteri e quello di 71 tengono davvero, perche' il passo del font 14
     **non e' mai stato misurato a schermo**;
  3. **i ventuno nomi di mappa** della 124a, che dipendono da
     `adata(ADATA_TYPE)` a tempo di esecuzione e che il codice non sa dare.

---
