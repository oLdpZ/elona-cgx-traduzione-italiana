# -*- coding: utf-8 -*-
"""91a - GARZIEM (`chat.hsp:11912`-`:12063`, 22 firme).

「《鉄騎のガルジエム》」, «<Garziem>» (`db_creature.hsp:72705`,
`db_card.hsp:6198`) — ⚠️ **l'epiteto 鉄騎 non c'e' ne' in inglese ne' in
italiano**: il nome di creatura e' il nome nudo, e va lasciato nudo anche qui.

E' il **capitano** della 神艦, che l'italiano chiama «la Nave Divina»
(`text.hsp:11326`), e l'incarico e' 「鉄騎のガルジエム」, «Incarico da
<Garziem> Lv150» (`text.hsp:11305`): infiltrarsi nel settore di lavoro e
fermare le macchine da lavoro impazzite.

REGISTRO: militare, alto in grado, cortese e asciutto — 「貴君」, 「〜たまえ」,
「了解した」, 「健闘を祈っている」. Il progetto gli ha gia' dato il «tu»
(`screen.hsp:1492`, «Garziem loda: La tua battaglia merita una medaglia!»),
quindi la formalita' sta nel giro di frase e non nel pronome: «Ricevuto»,
«Conto su di te», «Ti auguro buona fortuna».

LESSICO EREDITATO (non deciso qui) — ⭐ **quasi tutto il lotto e' gia' scritto
nel diario della missione**, `text.hsp:11305`-`:11336`, che il giocatore ha
sotto gli occhi mentre parla:
  - «<Garziem>»                       db_creature.hsp:72705
  - «la Nave Divina» (神艦)           text.hsp:11326
  - «la macchina da lavoro» (作業機械)   db_creature.hsp:72514, e «la macchina
                                      da lavoro speciale», :72607
  - «il settore (di lavoro)» (区画)   text.hsp:11336
  - «l'impazzimento», «le macchine impazzite» (暴走)   text.hsp:11326, :11336
  - «infiltrarsi» (潜入)              text.hsp:11336
  - «il controllo approfondito» (精密検査)   chat.hsp:22776, che e' **la stessa
                                      storia** vista dalla parte delle macchine
  - «serratura elettronica» (電子ロック)   map.hsp:815, chat.hsp:8158 — da cui
                                      l'aggettivo per le due parole nuove

LESSICO DECISO QUI (va in glossario):
  - 電子ウイルス -> **virus elettronico**, sul modello di «serratura
    elettronica» (`map.hsp:815`).
  - 電子頭脳 -> **cervello elettronico**, stesso modello.
  - 熱暴走 -> **surriscaldarsi fuori controllo**. ⚠️ Non c'era, e la parola
    giapponese e' la stessa 暴走 dell'«impazzimento» delle macchine: qui pero'
    il soggetto e' il calore, non la macchina, e «impazzimento del calore» non
    si dice.

⭐⭐ DEROGA 1 — 「ＩＤ」 A LARGHEZZA PIENA.
`:12033` scrive ＩＤ con i caratteri **a doppio byte**. A schermo la build
inglese disegna un glifo per byte, quindi due caratteri larghi diventano
quattro mezzi glifi illeggibili (guida di stile, la regola dei due byte). Si
scrive «ID» in ASCII: e' la stessa cosa che fa l'inglese di monte.

⭐ DEROGA 2 — 「もうこりごりだよ～」 E LA TILDE.
`:11962` finisce con 「～」, che e' a doppio byte e **non si puo' scrivere**
(89a, il caso di 「猫 イズ フリ～ダ～ム♪」: il `♪` si puo', la tilde no). Il
tono strascicato si rende con i puntini: «Ne ho avuto abbastanza...».

ALTRE DEROGHE DICHIARATE
3. `:12020` - IL GENERE DEL GIOCATORE. 「暇だしやるよ」 non puo' diventare
   «sono libero»: si gira in «Tempo ne ho, ci penso io».
4. `:12054` - 「1機たりとも帰ってこなかった」: il contatore 機 dice che quelli
   mandati dentro erano **macchine**, non uomini. L'inglese scrive «The workers
   we sent», che in inglese si legge come persone. In italiano «non ne e'
   tornata indietro nemmeno una» tiene il femminile delle macchine e lo dice
   senza spiegarlo.
5. `:11964` - 「各区画は独立していて、外部からでは指導はできても強制ができない
   のだ」 e' la ragione per cui serve il giocatore: non e' colore, e' la regola
   del posto. Si conserva intera.

PERIMETRO: 22 firme su 22 nel blocco, zero occorrenze fuori dal blocco
(`python scratchpad/_85-blocco.py 11912`).

MENU: quattro, tutti da 2 voci — il tetto delle due colonne non morde.

⚠️ Accenti veri; niente virgolette tipografiche e niente caratteri a due byte.
"""

RESE = {
    # --- >= 10, resto 0: la missione ripetibile e' a riposo
    11916: 'Grazie a te siamo a posto. Se dovessi aver bisogno ancora del tuo '
           'aiuto ti farò sapere: conto su di te.',

    # --- resto 6: il rapporto e il compenso
    11921: 'Ti sono grato. Dal controllo è risultato che alcune macchine '
           'erano impazzite per un virus elettronico. Anche le altre avevano '
           'il cervello elettronico surriscaldato fuori controllo: potevano '
           'esplodere da un momento all\'altro. Questo è il mio '
           'ringraziamento. Accettalo.',

    # --- resto 1: gli altri settori
    11962: 'Ne ho avuto abbastanza...',
    11963: 'Nel prossimo settore farò meglio',
    11964: 'Dai registri risulta che anche negli altri settori ci sono '
           'macchine da lavoro impazzite... Te la sentiresti di infiltrarti e '
           'far fare il controllo approfondito anche a loro? Ogni settore è '
           'indipendente: da fuori possiamo dare indicazioni, ma non imporle.',
    11967: 'Capisco... scusami.',
    11976: 'Che sollievo. Lo affido a te!',

    # --- resto fra 2 e 5: l'infiltrazione in corso
    11993: 'Per un po\' non ci voglio andare...',
    11994: 'Ci provo ancora un po\'',
    11995: 'L\'infiltrazione, procede bene?',
    11998: '...Non sforzarti, riposati pure.',
    12006: 'Ricevuto. Prenditi tutto il tempo che serve, senza strafare. Ti '
           'auguro buona fortuna.',

    # --- 1: l'incarico accettato
    12019: 'Adesso ho da fare',
    12020: 'Tempo ne ho, ci penso io',
    12021: 'Potrebbe essere una faccenda lunga... te ne occupi tu?',
    12024: 'Capisco. Scusami.',
    12033: 'L\'accesso è vietato ai non addetti, ma con la mia autorità ti ho '
           'preparato un ID e una via di trasferimento apposta. Potrai '
           'infiltrarti senza destare sospetti. Ti auguro buona fortuna!',

    # --- 0: il primo incontro
    12049: 'Non mi interessa',
    12050: 'Voglio sapere di cosa si tratta',
    12051: 'Hai fatto bene a venire. Ti ho accolto sulla mia nave perché ho '
           'una collaborazione da chiederti. Il compenso naturalmente c\'è. '
           'Che ne dici?',
    12054: '...In un certo settore ci sono macchine da lavoro impazzite. Non '
           'accettano più nessun comando da qui. Quelle che abbiamo mandato '
           'dentro sono rimaste intrappolate, e non ne è tornata indietro '
           'nemmeno una. Io sono il capitano e non posso lasciare il mio '
           'posto... ed è qui che entri tu.',
    12055: 'Voglio che ti infiltri nel settore in questione e che fermi '
           'l\'impazzimento delle macchine da lavoro. Quando te la senti, '
           'torna a parlarmi.',
}
