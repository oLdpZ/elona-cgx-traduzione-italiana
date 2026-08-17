# -*- coding: utf-8 -*-
"""Lotto fase4-main-002: il rientro, la navigazione e il carretto
(main.hsp, righe 1702-1937).

Quattordici rese, e sono il seguito naturale del lotto 001: lo stesso `txt` del
registro, ma il tratto che governa il **Ritorno** e l'**imbarco**. Undici delle
quattordici escono solo quando il giocatore lancia Ritorno o sale su una nave —
cioe' a ogni viaggio, per tutta la partita.

⭐ **Il tratto e' costruito a coppie, e le coppie vanno rese a coppia.** Il
sorgente distingue sempre gli stessi due casi con la stessa variabile,
`gdata(GDATA_FLAG_SHIP_LAST_PORT)`: se vale 0 il giocatore sta **rientrando**,
se non vale 0 sta **salpando**. Le coppie sono quattro — `:1867`/`:1871`,
`:1889`/`:1893`, `:1915`/`:1919`, `:1928`/`:1932` — e in italiano si distinguono
con le stesse due parole ogni volta: «rientro» e «salpare». Renderle una per una
avrebbe prodotto otto frasi che non si assomigliano fra loro dove il codice le
tiene appaiate.

⭐ **Tre nomi propri erano gia' decisi, e con le parentesi angolari.**
`<Arasiel>`, `<Garziem>` e `<Amurdad>` stanno cosi' in `db_card.hsp` e in
`text.hsp` (gli incarichi di livello 150), e le parentesi non sono decorazione:
`init.hsp:1713` riconosce un nome proprio **dalla prima lettera**, e `<` e' quella
che glielo dice. Si ricopiano identici.
💡 `:1738` e' il caso in cui giapponese e inglese nominano **due persone
diverse**: 「ネヘルタード」 e `<Amurdad>`. Vince l'inglese, che e' il ramo da cui
la build parte e l'unico nome che il resto del gioco usa (venti rese in
`map.hsp` e `chara_func.hsp`).

⭐ **Due etichette dell'interfaccia hanno deciso due parole.**

  - `text.hsp:66` e' la barra di stato, e `Overweight` vi si chiama
    **«Sovraccarico»**. `:1898` e' la voce che annuncia proprio quello stato,
    e ripete la parola invece di inventarne una seconda.
  - `command.hsp:14176` e `action.hsp:1906` chiamano il carro del giocatore
    **«carretto»**, ed e' la parola di `:1928` e `:1932`. ⚠️ `map.hsp:1069` dice
    «carro» ed e' l'unica: due siti su tre dicono carretto, e la barra
    dell'inventario e' quella che si legge piu' spesso.

⚠️ **`:1915` ha lo stesso inglese di `calculation.hsp:1556`, e la resa e'
diversa apposta.** Li' l'inglese `"A dimensional door opens in front of you."`
sta per 「不思議な力が空間を歪めた！」 (*una forza strana ha distorto lo spazio*) ed
e' reso «Una forza strana distorce lo spazio!»; qui sta per 「あなたは次元の扉を
開けた。」 (*hai aperto la porta dimensionale*), ed e' l'arrivo del Ritorno, col
suono `SOUNDLIST_TELEPORT1`. I due giapponesi sono diversi, quindi le firme sono
diverse e la rete 3 non ha niente da dire: e' upstream che ha riciclato la
frase inglese su due eventi che non sono lo stesso.

💡 **Le virgolette di `:1898` si scrivono `\\"`**, come fa l'inglese di monte e
come fanno le altre 84 rese statiche che ne portano una. Le tipografiche `“ ”`
sono vietate: CP932 le codifica su due byte e la build inglese disegna un glifo
per byte.

⭐ **「時の管理者」 non era mai stato nominato**, e `:1937` e' il messaggio con cui
il Ritorno ti scarica in prigione invece che a casa (`gdata(GDATA_TELEPORT_AREA)
== AREA_JAIL`). «Custode del tempo» tiene insieme le due cose che 管理者 dice —
chi amministra e chi sorveglia — dove «amministratore» avrebbe fatto burocrazia
e «controllore» il bigliettaio.
"""
