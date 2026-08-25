# -*- coding: utf-8 -*-
"""95a - La Gabbia di Amur: cinque parlanti, un posto solo (14 rese).

`ALFRED` (`:13924`-`:13949`, 5), `ETHER_GENERATOR` (`:8795`-`:8811`, 3),
`HELLABYRINTH_RULER` (`:10521`-`:10550`, 3), `GILPHEM` (`:15123`-`:15131`, 2)
e `ENTHUMESIS` (`:15093`-`:15100`, 1).

⭐⭐ IL RAGGRUPPAMENTO L'HA DATO `map.hsp`, COME NEL PRIMO GIRO. Cinque blocchi
sparsi su settemila righe di `chat.hsp` che non hanno **niente** in comune a
guardare il file, e che stanno tutti in `AREA_AMUR_CAGE`: `:6089` (il
generatore), `:6313` (Alfred), `:6361` (Enthumesis), `:6379` (Gilphem),
`:6546`-`:6999` (il demone, sette piani). AMURDAD e MANYTIA, gia' resi nella
92a, sono la' dentro anche loro. Il criterio non e' il numero di firme: e' il
posto in cui il giocatore le legge di seguito.

⭐⭐⭐ E DI NUOVO IL REGISTRO ERA GIA' SCRITTO, PERSINO LA CORTESIA.
  - **ALFRED** — `db_creature.hsp:55746`, gia' reso: «**Le** mostro la forza di
    un ex comandante dei cavalieri.», «Il vento che sollevo non è gentile, **sa**.»
    Da' al giocatore del **LEI**, come RYUTYE stamattina, e per la stessa
    ragione: e' scritto nella sua voce. ⚠️ Ma al suo signore da' del **voi**:
    `:55752`, «**Signor Barius, vi** chiedo perdono...». Le due cortesie
    convivono perche' i destinatari sono due.
  - **GILPHEM** — parla in **katakana**, e il progetto ha gia' deciso come si
    rende: `db_creature.hsp:52721` e `:52727`, gia' rese **TUTTE MAIUSCOLE**
    («CHIEDO PERDONO...», «ERO DI GUARDIA.»). Non c'era niente da inventare.

⭐⭐⭐ LA COSA PIU' IMPORTANTE DEL LOTTO E' CHE DUE RIGHE DEVONO ESSERE UGUALI.
`:10539` e `:10530` sono **la stessa frase due volte**: 「早く！こっちよ！」 in
kana e poi 「早ク！コッチヨ！…」 in katakana. Il demone del palazzo infero
imita la **voce della madre** per tirare dentro l'anima del bambino — che a
`:10596`, gia' reso, piange «Mamma... dove sei... Ho paura...!» — e a `:10541`
il bambino risponde «Mam... ma?». Poi la maschera cade: stessa frase,
**maiuscola e sfigurata**, e la risata.
⚠️ Se le due rese non usano **le stesse identiche parole** lo scherzo non si
sente, e nessuna rete se ne accorgerebbe: sono due firme diverse, con
giapponese diverso, in due rami diversi dello stesso blocco.
💡 La maiuscola del katakana, decisa per Gilphem in un altro file, qui fa
esattamente il lavoro che serve.

LESSICO EREDITATO (non deciso qui):
  - エーテル        «etere»                     `text.hsp:46` e ottanta siti
  - 生命体          «forma di vita»             `chat.hsp:24423`, che parla
                                                proprio di questo generatore
  - ヴァリウス様    «il signor Barius»          `db_creature.hsp:55752`
  - ランカータ      «Lankata»                   `db_card.hsp:3689`
  - 混沌の神        «il dio del caos»           `chat.hsp:10210` e trenta siti
  - ゼーム様        «il signor Zeome»           `chat.hsp:2263`, `text.hsp:669`
  - 冥宮            «il Palazzo Infero»         `map.hsp:6524`-`:7011`
  - お父さん (di Enthumesis) «Padre»            `chat.hsp:18083`, gia' reso

⚠️ DEROGA 1 — `:13931`, L'INGLESE NON TRADUCE: DICE UN'ALTRA COSA.
Il giapponese e' 「は見えない誰かに話しかけている…」 — *sta parlando con
qualcuno che non si vede* — e l'inglese e' « is stunned. », che non ha niente a
che fare. E' la famiglia trovata dalla rete della 94a
(`_94-jp-dinamico-en-statico.py`), stavolta senza concatenazione: si segue il
giapponese, e la riga serve, perche' e' **l'unica cosa che spiega `:13933`** —
Alfred non sta parlando al giocatore, sta chiedendo scusa a qualcuno che il
giocatore non vede.

⚠️ DEROGA 2 — `:13927` E' ALFRED CHE PARLA DI SE', NON DEL GIOCATORE.
「任務に失敗したうえ、後続隊を犠牲にしてまで生き延びてしまいましたか…」 non ha
soggetto, e la frase dopo — 「合わせる顔がありませんね」 — e' senza dubbio sua.
L'inglese apre con «**You** failed in your mission» e chiude con «**I** will be
ashamed»: due soggetti in due frasi che ne hanno uno solo. Si segue il
giapponese (57a).

⚠️ DEROGA 3 — `:13938`, L'INGLESE AGGIUNGE IL SIGILLO ETERNO.
「もし、辿り着いても」 non dice **dove**; l'inglese scrive «even if you manage to
reach **the Eternal Seal**». Il Sigillo Eterno e' un posto preciso, con un nome
gia' in uso in trenta rese: metterlo qui vorrebbe dire scrivere
un'informazione che il giapponese non da'. Resta «anche se ci dovesse
arrivare».

⚠️ DEROGA 4 — `:8803`, IL GIAPPONESE SPACCA E L'INGLESE CI PROVA.
「叩き割った」 e' fatto; l'inglese dice «**attempt** to break it off». Che sia
fatto lo conferma la riga subito dopo, `:8805`, gia' resa: «Metti il blocco di
etere purissimo nella capsula di recupero.» ⚠️ E si scrive al **presente**,
come quella e come tutta la colonna: un participio passato qui prenderebbe il
genere del giocatore.

⭐ DEROGA 5 — 嬉シイ NON DIVENTA «CONTENTO».
Gilphem e' 番兵 e in italiano si chiama «la sentinella d'acciaio magico»: un
aggettivo su di se' gli chiederebbe un genere che il gioco non gli da'. 嬉シイ
diventa **«CHE GIOIA.»**, che vale per chiunque, e 作ラレタガーディアン diventa
«UN GUARDIANO, OPERA DEL SIGNOR ZEOME» invece di «COSTRUITO DA», per la stessa
ragione.

PERIMETRO: 14 firme su 14 dentro i cinque blocchi, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 13924 15123 8795 10521 15093`), zero gia'
rese altrove.

MENU: nessuno. Tutte `chatMore` o `txt`, tranne `:13931` che e' un
**frammento** concatenato dopo `name(tc)` e comincia percio' con uno spazio.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- ETHER GENERATOR: la descrizione che si legge esaminandolo
    8801: '(È una forma di vita che genera etere e lo spande su tutta la zona '
          'qui intorno. Una parte dell\'etere che ha emesso si è '
          'cristallizzata e gli copre la superficie.)',
    8798: '(Non sembra più che stia spandendo etere, ma l\'etere che si è '
          'cristallizzato fin qui gli copre la superficie come prima.)',
    8803: '(Prendi di mira un cristallo a portata di mano e lo spacchi via.)',

    # --- IL DEMONE DEL PALAZZO INFERO: la voce della madre, e poi la maschera
    10539: 'Presto! Di qua!',
    10541: 'Mam... ma?',
    10530: 'PRESTO! DI QUA! PRESTO... DI QUA... PRESTO PRESTO! PRESTO DI '
           'QUA... AHAHAHAHAHAHAH!!!!',

    # --- ALFRED al Santuario del Guardiano
    13927: 'Ho fallito la missione, e per giunta sono sopravvissuto '
           'sacrificando il reparto che veniva dietro... Non ho più faccia da '
           'mostrare al signor Barius...',

    # --- ALFRED nella Gabbia di Amur: parla con qualcuno che non si vede
    13931: ' sta parlando con qualcuno che non si vede...',
    13933: 'Mi perdoni. Se non l\'avessi trascinata dentro io, Lankata non '
           'sarebbe ancora venuta qui. Mi dispiace davvero. La prego, non me '
           'ne voglia.',

    # --- ALFRED nella Culla del Caos: l'ultima cosa che dice
    13938: 'Uuurgh! Mi ascolti... anche se ci dovesse arrivare... il dio del '
           'caos, ancora, non lo abbatta...! Quello serve a... tenere unito '
           'il mondo...!',
    13939: 'Ah... agh...',

    # --- ENTHUMESIS
    15095: 'Padre... padre...',

    # --- GILPHEM: katakana, quindi maiuscolo
    15126: 'INSIEME AL SIGNOR ZEOME. CHE GIOIA. IL SIGNOR ZEOME SEMBRA '
           'DIVERTIRSI. CHE GIOIA.',
    15129: 'IO SONO UN GUARDIANO, OPERA DEL SIGNOR ZEOME. CHI INTRALCIA IL '
           'SIGNOR ZEOME VA ELIMINATO.',
}
