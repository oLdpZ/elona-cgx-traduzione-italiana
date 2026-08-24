# -*- coding: utf-8 -*-
"""95a - NERES e RYUTYE, i due smemorati (`chat.hsp:12872`-`:12906`, 8 rese).

Due blocchi attaccati e due creature attaccate: `map.hsp:5266` e `:5270` li
mettono a **16,15 e 17,15** in `AREA_WAR_GROUND` (`shrine_2`), una casella
l'uno dall'altra. Si leggono e si rendono insieme.

⭐⭐⭐ IL REGISTRO DI TUTT'E DUE ERA GIA' SCRITTO — IN `db_creature.hsp`, E
DECIDE PERSINO LA FORMA DI CORTESIA.
Nessuno dei due andava deciso qui:
  - **NERES** (`:71000`, `:71006`, `:71012`, gia' rese) e' feroce e beffarda:
    «Adesso ti faccio saltare la testa, eh.», «E adesso... come ti cucino?»,
    «Che pesciolino pieno di boria.» Da' del **tu**, e in `chat` ha クソッ, チッ
    e la coda 〜わ. La sua carta (`db_card.hsp:5945`) dice che ha l'aspetto di
    una bambina e che e' **abituata a combattere**.
  - **RYUTYE** (`:70912`, `:70918`, `:70924`, gia' rese) e' timido e cerimonioso
    — e le sue battute gia' rese danno al giocatore del **LEI**: «Non faccia
    cose terribili, la prego.», «Mi... dispiace...». La sua carta
    (`db_card.hsp:5932`) lo dice 少年 educato, cresciuto in una buona famiglia.

⚠️⚠️ DEROGA 1 — RYUTYE PRENDE IL **LEI**, NON IL VOI DELL'88a.
La regola dell'88a (Maile, poi Manson e Bonyac) dice che 敬語 + あなた al
giocatore si rende col **voi di cortesia**. Qui non si applica, e per la ragione
che quella regola stessa mette prima di tutto: **il registro si trova, non si
decide**. Ryutye ha gia' una voce nel gioco, `db_creature.hsp:70912`, ed e' una
battuta che il giocatore sente **nella stessa scena** — basta attaccarlo — dove
da' del lei. Con il voi lo stesso ragazzo userebbe due cortesie diverse a un
minuto di distanza.
⚠️ Il vincolo di genere e' comunque rispettato: il lei non chiede un genere sul
verbo, e nessuna delle rese mette un aggettivo o un participio addosso al
giocatore.
💡 Il lei di cortesia nel progetto esiste ed e' raro: `db_creature.hsp:70912`,
`:85750` («Mi faccia i complimenti, la prego.»), `:88098` («B-basta, la
prego...»). Sono tutte e tre battute di chi ha paura o supplica.

⭐⭐⭐ E LA PERDITA DI MEMORIA E' LA COSA CHE TIENE INSIEME LA GIORNATA.
`:12876` (Neres non ricorda che cosa ricordava), `:12897` (Ryutye non ricorda il
proprio nome), `:12898` («come ho vissuto fino a oggi?»), `:12902` (Neres ha
perso cose e non sa **quali**). Nello stesso giorno: NANCY non ricorda che cosa
le sia sparito (`:15355`), CRAY non ricorda chi si sia buttato nella fenditura
(`:15407`), MANSON ha perso il senso del tempo (`:15385`, 94a). Sono personaggi
di mappe diverse: la cosa che hanno in comune non e' il posto, e' il **buco**.
Nessuna delle rese lo alleggerisce.

LESSICO EREDITATO (non deciso qui):
  - 護衛      «scorta»            `chat.hsp:6735`, `:8146` e altri sette siti
  - 屋敷      «la villa»          `chat.hsp:7554`, `text.hsp:3033` e altri
  - 記憶喪失  «lo smemorato / la smemorata»  `db_creature.hsp:70938`, `:71026`

⚠️ DEROGA 2 — `:12876`, L'INGLESE SI INVENTA UN CORPO SBRANATO.
Il giapponese dice 「獣が散々食い散らかした跡みたいに」: i ricordi stanno come
**le tracce che lascia una bestia** dopo aver sparpagliato quel che mangiava.
L'inglese scrive «as if a beast has eaten its way **through my body** and left
behind only a few scraps», che aggiunge il corpo e sposta l'immagine dal
disordine allo sbranamento. Si segue il giapponese (57a).

⚠️ DEROGA 3 — 君 E ちゃん SI BUTTANO, E NON PER PIGRIZIA.
Neres dice リューツェ**君** e Ryutye dice ネレス**ちゃん**. L'inglese di `:12875`
prova a renderlo con «**Mr.** Ryutye», che in bocca a lei — che gli parla dal
di sopra — dice l'opposto. In italiano i due suffissi non hanno un equivalente
che non cambi il rapporto: restano **«Ryutye»** e **«Neres»** nudi, e il
rapporto lo porta il tono, che c'e' gia' in tutt'e due i blocchi.

⚠️ DEROGA 4 — `:12898`, LA さん DOPO IL NOME DEL GIOCATORE NON SI PUO' RENDERE.
「" + cdatan(CDATAN_NAME, CHARA_PLAYER) + "さんっていうんですね」. Il progetto
rende 〜さん con «il signor 〜» (`db_creature.hsp:83964`, `:87568`), ma qui il
nome e' quello del **giocatore**: un titolo davanti chiederebbe un genere. La
cortesia la porta il **lei** della frase, che c'e' gia'.
💡 La voce e' `dinamica` da tutt'e due i lati — l'inglese concatena anche lui —
quindi la variabile si puo' scrivere (rete della 94a).
⚠️ E l'inglese di monte, a differenza dell'italiano, **ha perso lo spazio e il
punto** dopo il nome: «uh... <nome>Are you adventuring». Non si copia.

PERIMETRO: 8 firme su 8 dentro i due blocchi, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 12872 12892`), zero gia' rese altrove.

MENU: nessuno. Tutte `chatMore`, e tutte con `strbye` tranne `:12896`.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
⚠️ Le virgolette dentro `:12898` si scrivono protette (`\\"`), come in HSP.
"""

RESE = {
    # --- NERES al Campo di Battaglia: il primo incontro
    12875: 'Mi ricordo che stavo combattendo contro qualcosa, per proteggere '
           'Ryutye. Poi mi ha avvolta una luce e mi sono ritrovata in questo '
           'posto senza senso...',
    12876: 'Maledizione. Della memoria mi restano solo brandelli, come le '
           'tracce che lascia una bestia dopo aver sparpagliato tutto. E per '
           'giunta sono alla rinfusa, e quasi non si attaccano l\'uno '
           'all\'altro...!',

    # --- NERES nella Culla del Caos, cioè quando la si porta dietro
    12885: 'Ti ho seguito perché avevi detto che mi avresti spiegato questo '
           'mondo, ma qui che roba è? Ho come l\'impressione di essere usata '
           'da scorta, quando ti fa comodo.',
    12881: 'Tsk... comincio a stare in pensiero per Ryutye, che ho lasciato '
           'indietro.',

    # --- RYUTYE: la prima volta in assoluto
    12896: 'P-piacere di conoscerla.',
    12897: 'Io sono Ryutye... o almeno pare che il mio nome sia questo. ...Mi '
           'scusi, non è che me lo ricordi tanto bene nemmeno io.',
    12898: '"Lei è... ehm... " + cdatan(CDATAN_NAME, CHARA_PLAYER) + ", '
           'giusto? Va per il mondo all\'avventura? La invidio: io dalla villa '
           'non sono mai... eh? Che stavo dicendo... Io, fino a oggi, '
           '\\"in che modo ho vissuto\\"...?"',

    # --- RYUTYE: tutte le volte dopo
    12902: 'Capisco anche perché Neres sia così su di giri. Ha perso tante '
           'cose a cui teneva... e non riesce ad accorgersi di che cosa '
           'fossero... e non sa nemmeno perché sia finita così... è una cosa '
           'che rode, davvero.',
}
