# -*- coding: utf-8 -*-
"""93a - ARASIEL della tempesta di sabbia (`chat.hsp:10729`-`:10876`, 9 su 9).

`CREATURE_ID_ARASIEL` sta in cima alla **torre del deserto** e la amministra per
conto di Lulwy, la dea del vento, a cui ha giurato fedelta'. Prende in consegna
le creature che il giocatore le porta e le usa come «giocattoli»: e' la missione
`ARASIEL_OF_THE_SANDSTORM`.

⭐ IL REGISTRO: signora crudele e compiaciuta, che parla al femminile e con le
desinenze morbide (わ, のよ, ね). Il metro e' Lulwy stessa, gia' resa:
`action.hsp:14228` «Oh, e un mortale osa chiedere tanto? Uhuhu... per stavolta
faccio un'eccezione.» — la stessa crudelta' cortese, un gradino piu' su.

LESSICO EREDITATO (non deciso qui):
  - ルルウィ      «Lulwy»              god.hsp:279, db_card.hsp:10709
  - ルルウィお姉さま «sorella Lulwy»    db_creature.hsp:75097 «Sorella Lulwy... perdonatemi...»
  - 黒天使        «l'angelo nero»      action.hsp:16859, god.hsp:704
  - タッグ        «la coppia»          command.hsp:6094, chat.hsp:14285
  - ご褒美        «ricompensa»         chat.hsp:19335 e il resto della famiglia

⭐⭐ DEROGA 1 — `:10802` E' LA GEMELLA DI `map_user.hsp:878`, E SI DICE UGUALE.
「タッグを解除する必要がある。」 qui, 「タッグを解散する必要がある。」 la',
gia' reso **«Prima devi sciogliere la coppia.»**: due verbi giapponesi diversi
per la stessa identica azione, nello stesso identico momento (il gioco rifiuta
di consegnare un compagno che sta in coppia). Sono due firme distinte, quindi
nessuna rete le lega: si scrive la **stessa frase**, se no il giocatore legge
due messaggi diversi per lo stesso rifiuto.

⚠️ DEROGA 2 — `:10769` E' UNA DINAMICA CHE PORTA UN NOME DI CREATURA.
`refchara(..., DBSPEC_CHARA_NAME_ORG, 1)` restituisce il nome **con l'articolo**
(il contratto dei nomi: «il putit»), quindi davanti non ci puo' stare nessuna
preposizione semplice — e' la rete 8. La frase si costruisce con «portarmi» +
il nome nudo.

⭐ DEROGA 3 — `:10782`, IL FINALE CHE L'INGLESE SFUMA.
「ああ、やっぱり私はお姉さまには敵わないんだなぁって。すごくゾクゾクするのよ」:
mentre la tempesta la sbatte contro i muri, Arasiel pensa **che alla sorella non
puo' tener testa**, e la cosa le da' un brivido di piacere. L'inglese lo rende
con «I really can't compete with her. Just makes me tremble...», che si puo'
leggere come paura. In italiano il brivido resta **di piacere**, perche' e' il
personaggio: e' la stessa ammirazione per la spietatezza di `:10776`.

⚠️ DEROGA 4 — `:10785`, ボス猫女神 E' UNA DIVINITA', NON UN'IMPERATRICE.
L'inglese scrive «That empress cat god»: 女神 e' **dea**, e ボス猫 e' la gatta
capobanda dei gatti neri che assediano la torre. In Elona la dea gatta e'
Ehekatl (`chat.hsp:8448`, gia' resa), e Arasiel promette di punirla: si dice
«dea gatta», che e' quello che il giapponese dice e che il giocatore riconosce.

⚠️ MISURA: 0 fuori misura; tre righe (`:10779`, `:10782`, `:10785`) fanno **una
riga piu' dell'inglese**, tutte e tre lunghe e descrittive, e tutte e tre
lontanissime dal tetto (8 righe su 13, il massimo). Qui la riga in piu' non e'
prolissita': sono i periodi in cui il giapponese elenca — il te', la spiaggia,
i prigionieri — e l'italiano non ha modo di stringerli senza togliere una voce
dell'elenco.

PERIMETRO: 9 firme su 9 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 10729`) e **zero firme gia' rese altrove**.

MENU: nessuno. Le quattro battute `kaiwa == 0..3` (`:10776`-`:10785`) sono le
chiacchiere che escono a rotazione.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte —
tranne il ♪ di `:10814`, che e' l'unico ammesso e che il giapponese ha.
"""

RESE = {
    # --- la richiesta: una creatura nuova da tormentare
    10749: 'Tormentare i soliti schiavetti comincia ad annoiarmi... Voglio '
           'reazioni più fresche.',
    10769: '"Senti, non è che mi porteresti " '
           '+ refchara(gdata(GDATA_FLAG_SUB_ARASIEL_OF_THE_SANDSTORM_CREATURE), DBSPEC_CHARA_NAME_ORG, 1) '
           '+ "? ...Una ricompensa? Ma certo, se mi va."',
    10802: 'Prima devi sciogliere la coppia.',
    10814: 'Oh...♪ Come ti avevo detto, mi hai portato un giocattolo nuovo. '
           'Quando questo si rompe te ne chiedo un altro, mi raccomando.',
    10821: 'E va bene, sono di buon umore: ti do una ricompensa. Tienila.',

    # --- le quattro chiacchiere della torre
    10776: 'Il sole picchia, la sabbia si appiccica ed è fastidiosa, un posto '
           'davvero orribile... Antenna o quel che è, sorella Lulwy ha '
           'affidato proprio a me, che le ho giurato fedeltà, la cura di '
           'questa torre nel deserto. Ma è proprio quella spietatezza che me '
           'la fa amare...',
    10779: 'Questa spiaggia me l\'hanno costruita l\'angelo nero e i suoi '
           'servi. Pare abbiano faticato parecchio, perché la sabbia sporca '
           'del deserto non l\'hanno usata: se la sono fatta arrivare da '
           'fuori. In cambio li ho ricompensati in abbondanza.',
    10782: 'Anche sorella Lulwy viene qui in vacanza. Prendiamo il tè quando '
           'capita, ci divertiamo sulla spiaggia, puniamo insieme i '
           'prigionieri. Ma il pezzo forte è la tempesta della fine: scatena '
           'dentro la torre una tempesta in piccolo, manda all\'aria ogni '
           'cosa e se ne va. E mentre il vento mi sbatte di qua e di là io '
           'penso... ah, con mia sorella non posso proprio competere. Ed è un '
           'brivido bellissimo...',
    10785: 'Non so perché, ma intorno alla torre si sono stabiliti certi '
           'gatti neri di malaugurio. L\'angelo nero l\'hanno assalito più '
           'volte e per poco non gli strappavano le ali: a quella dea gatta '
           'capobanda, prima o poi, toccherà una punizione.',
}
