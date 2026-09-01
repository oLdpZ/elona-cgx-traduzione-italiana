# -*- coding: utf-8 -*-
"""121a - Lotto 058 di `db_item.hsp`: GLI SCUDI, e la categoria CHIUDE.

`FILTER_SHIELD`, righe da `:42852` a `:127204`: **24 righe** — 23 dell'indice 0
e 1 dell'indice 2 — su 23 oggetti. Con questo lotto `FILTER_SHIELD` va a **0 da
fare su 24 vive**, ed e' la **tredicesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 058`: **+24** per 24 rese,
nessuna gemella. ⓘ `_gia-reso.py 058`: 0 su 24. `_code.py 058`: 0 righe senza
resa in tabella — e le ventiquattro code sono state **copiate** dalla sua
uscita, non ricostruite (la lezione del lotto 057, otto su otto sbagliate).

### ⭐⭐⭐ UNA SERIE DI CINQUE, E QUESTA VOLTA L'HA TROVATA LO STRUMENTO

`_120-serie-bacchette.py 058` — nato nella 120a, al suo secondo lotto — ha
stampato in un secondo quel che le tre sessioni prima cercavano a mano:

    5 x  攻防一体の装備。

Sono i cinque tonfa **ST-01 SACRIFICE, ST-02 SHIELD, ST-03 SMASH, ST-04 SABER
e ST-05 SONIC**, che stanno nel dossier a righe lontane (`:71233`-`:71509`) ma
che il giocatore incontra come una famiglia: cinque numeri di serie in fila.

⭐ La formula si ripete **identica** in tutte e cinque le rese — «Un
equipaggiamento che unisce attacco e difesa.» — e cambia solo quel che viene
dopo. E' la stessa decisione delle tre armi della 120a: variare i verbi per non
ripetersi avrebbe cancellato la serie, che e' il modo in cui il giocatore
riconosce l'ST-01 come parente dell'ST-05.

ⓘ **Il valore atteso dello strumento resta «nessuna serie»**: in cinque lotti
su sei non ne ha trovate. Qui ne ha trovata una da cinque, e l'ha trovata
prima che scrivessi la prima resa.

### ⭐⭐⭐ 神の間 NON E' «TRA GLI DEI»: E' UN LUOGO, E IL GIOCATORE LO CONOSCE

`:57962`, le manette del 《神々の枷鎖》, dice 神の間での使用を想定し.

Letto come lingua, 神の間 e' «fra gli dei», e la frase suona benissimo: manette
pensate per essere usate fra dei. **E' sbagliato.** 神の間 e' il **Sigillo
Eterno**, il luogo dell'atto finale del gioco — inglese `Eternal Seal` — e sta
in una quarantina di battute gia' rese: «Al Sigillo Eterno non ci andare», «il
Sigillo Eterno e' in mano a qualcuno che non si sa chi sia».

⚠️ **Nessuna rete poteva vederlo.** La riga e' pulita in ogni senso: il
giapponese c'e', l'inglese c'e' («Intended for the gods» — anche lui l'ha letto
come lingua e non come nome), la forma e' a posto. Il difetto sarebbe esistito
solo nella testa del giocatore, che quel nome lo ha letto quaranta volte.
A trovarlo e' stata la quinta fonte della 110a — *il codice e il resto del
gioco* — interrogata con `_cerca.py` su una parola che sembrava non averne
bisogno.
💡 La regola che ne esce: **una parola composta di kanji comuni puo' essere un
nome proprio**, e il modo di scoprirlo e' cercarla, non guardarla.

### ⭐⭐ IL TONFA CHE IL GIAPPONESE NON DESCRIVE, E L'INGLESE TAGLIA A META'

`:71509`, l'ST-01 SACRIFICE, in giapponese dice **soltanto** la formula della
serie: 攻防一体の装備。 e basta. L'inglese ci aggiunge una frase, e quella
frase e' **troncata a meta' di parola**:

    Offensive-and-defensive equipment. It allows it's user to sac

Chi rende dall'inglese qui deve inventare la fine («...to sacrifice its own
durability»?). La resa viene dal giapponese e finisce dove finisce lui.

⭐ **E la riga gemella lo aveva gia' deciso**: l'indice 3 dello stesso oggetto,
reso in una sessione passata, sta davanti allo stesso troncamento
(`It is a tonfa that suc`) e ha scritto «Un tonfa.». Le due meta' del pannello
fanno la stessa cosa perche' una delle due l'aveva gia' fatta.

### ⭐ IL BOLLINO DEL BRAVO, CHE IN ITALIANO E' ANCHE UNO SCUDO

`:59592`, il 《クラウンポイント》, racconta che l'oggetto si dava agli allievi
del **Seminario d'Avventura** che superavano la prova del **maestro Spada
Rossa** (due nomi gia' resi, presi dal dizionario e non reinventati), e che
allora si chiamava がんばりシールド, «con motivi anche diversi dalla corona».

がんばりシールド e' un bisticcio: がんばりシール e' il **bollino** che in
Giappone il maestro attacca sul quaderno a chi ha fatto bene — e con un ド in
fondo diventa シールド, lo scudo. L'inglese lo traslittera («Ganbari Shield») e
non tiene niente.

⭐ L'italiano ha una parola che tiene tutt'e due i sensi: **scudetto** e'
insieme lo scudo piccolo e il bollino che si dava a scuola. La resa e'
«Scudetto Bravo», e la frase dopo — i motivi diversi dalla corona — conferma da
sola che si parla di bollini e non di armi.

### ⓘ Tre punti dove l'inglese e il giapponese non dicono la stessa cosa

  - `:100717`, lo scudo a torre. Il giapponese dice 重量は半端なものではなく,
    «il peso non e' cosa da mezza misura», cioe' **e' enorme**; l'inglese scrive
    «it is not half as heavy as it should be», che dice il **contrario**. La
    resa segue il giapponese, e l'indice 3 gia' reso («Uno scudo pesantissimo»)
    conferma da che parte sta il gioco;
  - `:71511`, l'appunto degli autori dentro l'ST-01: 第三部用, «per la parte
    terza». L'inglese scrive «Reserved for ACT III», ma in italiano gli atti si
    chiamano **parti** — la missione e' `@QM[第三部 永遠の盟約]` ->
    «Parte terza - Il patto eterno». Chi legge «ATTO III» non lo ritrova da
    nessuna parte;
  - `:81328`, l'asse di 《カルネアデスの板》. クイーン・セドナ号 non e' una nave
    qualunque: e' la **<Regina Sedona>**, che il giocatore conosce anche come
    persona («<Regina Sedona> la fanciulla delle vele») e la cui carta racconta
    lo stesso naufragio, «per il vento d'etere durante il viaggio inaugurale
    verso Porto Kapul». La resa la nomina come la nomina il resto del gioco.

### ⚠️ Le parole lunghe: sette a quindici caratteri, e sei sono la stessa

`_preflight034.py 058` segnala **7** parole nella finestra di rinculo, contro le
2 del 057 e le 2 del 055 (che ne aveva anche una da **18**, ed e' passata).
Sei delle sette sono «equipaggiamento», cioe' la **prima parola della formula
dei cinque tonfa**: se l'impaginatore la spezza, la spezza cinque volte.

⚠️ Il preflight e' un referto, non un cancello: il cancello vero e'
`_107-descrizioni-item`, «parole spezzate introdotte dall'italiano: 0», e si
misura **dopo** il reimporta. Se quello si accende, si cambia la formula — non
prima, perche' «equipaggiamento» e' la resa di 装備 gia' usata nella stessa
categoria (`:68250`, gli artigli).

### ⓘ Un difetto NON di questo lotto, visto passando

Il **nome** di 《カルネアデスの板》 sta nel dizionario spezzato in due voci —
「Carneades」 -> «Carneade» e 「plank」 -> «asse» — e a schermo si legge
**«Carneade asse»**. In italiano l'oggetto ha un nome suo, ed e' famoso: la
**tavola di Carneade**, il dilemma del naufrago che ne salva uno solo — che e'
esattamente quel che la descrizione dice («al massimo tiene a galla una persona
sola che stia annegando»). ⚠️ E' una riga di **nomi**, non di corpo: non la
tocca questo lotto, e va decisa a parte.
"""
