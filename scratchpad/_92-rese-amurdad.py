# -*- coding: utf-8 -*-
"""92a - AMURDAD (`chat.hsp:10627`-`:10728`, 12 firme).

《永遠のネヘルタード》 / `<Amurdad>` (`db_creature.hsp:75293`, `db_card.hsp:6601`)
sta nella **Gabbia di Amur** (`text.hsp:2929`, 闇檻 nudo = «Gabbia Oscura»,
`text.hsp:11274`) e da li' non puo' uscire. E' lui che manda a salvare
**l'anima smarrita** resa nella 91a (`chat.hsp:10551`-`:10626`): questo blocco
e' l'altra meta' di quella missione, e le due si leggono insieme.

⭐ IL REGISTRO E' GIA' FISSATO DA ALTRI FILE, e non si decide qui. <Amurdad>
parla a frasi mozze, con i puntini, sottovoce:

    map.hsp:10511   «<Amurdad> sussurra: Non c'e' tempo... corri col tasto Shift...»
    map.hsp:10514   «...ang...o de..ro...»            (la voce che si spezza)
    chara_func.hsp:7139  «Non c'e' piu' niente da fare... che peccato...»

Quindi: niente periodi lunghi, puntini di sospensione dove il giapponese li
mette, e mai un tono da oracolo solenne — e' stanco, non maestoso.

LESSICO EREDITATO (non deciso qui):
  - 定命            «mortale»        chat.hsp:6211, :10142, :10269, :18540
  - アストラル光     «luce astrale»   chat.hsp:9473, :10178, :18540
  - アーカーシャ     «Arkasha»        chat.hsp:15457 (la luce di), :18540 (i corridoi di)
  - アカシックレコード «rete akashica»  chat.hsp:10178
  - 迷い子           «l'anima smarrita» db_creature.hsp:44807, db_card.hsp:1427
  - 闇檻/Amur-Cage   «Gabbia di Amur» text.hsp:2929; «Gabbia Oscura» nudo, :11274
  - 悪鬼             «demone»         db_card.hsp:1388

⭐⭐⭐ DEROGA 1 — 「定命の君」 E' «MORTALE», E L'INGLESE SBAGLIA.
`:10706` in inglese e' «destined one», che legge 定命 come *destino*. Ma 定命
in questo progetto e' gia' **mortale** in cinque punti (chat.hsp:6211 «osservare
come vivono i mortali», :10142 «dei e mortali», :10269, :18540, command.hsp:4798)
ed e' il contrario esatto di quel che dice l'inglese: non «predestinato», ma
*chi ha una vita che finisce*, detto da uno che non muore. Si segue il
giapponese e il glossario di casa.

⭐⭐⭐ DEROGA 2 — 「魂のキャンパス」 E' UNA **TELA**, NON UN CAMPUS.
`:10716` scrive キャンパス (*campus*) dove vuole キャンバス (*canvas*), e
l'inglese si porta dietro l'errore alla lettera («laid upon the campus of the
soul»). Che sia una tela lo dicono le altre due parole della stessa battuta e
di quella prima: 描かれた («dipinto», `:10712`) e 画廊 («galleria di quadri»).
⭐ E la parola italiana esiste gia' nel progetto: `event.hsp:1733`
「この世はキャンバス」 e' reso **«Il mondo e' una tela»**. Qui diventa «la tela
delle anime», e l'eco con quella riga si sente.

⭐⭐ DEROGA 3 — `:10685`, IL FATTO CHE L'INGLESE BUTTA VIA.
Il giapponese e' 「仲間の最大数に達しているため、行っても連れてこられない…。」:
non dice «il gruppo e' pieno» e basta, dice **che andarci non servirebbe**,
perche' l'anima non la potresti riportare indietro. L'inglese ricicla la
formula generica di tutto il gioco («Your party is already full. You can't
invite someone anymore.», identica in nove file). Si rende il giapponese, e
`行っても` torna dentro.
⚠️ E l'accordo si appoggia ad **«anima»**, non alla creatura: il bambino ha
`CDATA_SEX` tirato a sorte (`db_creature.hsp:44851`, deroga 1 della 91a), quindi
«riportarla» funziona sempre perche' concorda col sostantivo italiano.

⭐ DEROGA 4 — `:10712`, L'IMPERSONALE PER NON DARE UN GENERE AL GIOCATORE.
導かれ e' un passivo senza soggetto e vale per chiunque muoia. «Sei condotto»
darebbe un genere; si usa l'impersonale **«si viene condotti»**, che in italiano
non lo da' a nessuno.

⭐ DEROGA 5 — `:10630`, DUE FILI TIRATI VERSO ALTRI FILE.
他の子 e' «un'altra **anima smarrita**» (il nome della creatura, non «un altro
bambino»: a schermo il giocatore ha appena scortato quella), e 連絡する e' la
**chiamata** di `main.hsp:1738` («E' arrivata una chiamata di soccorso da
<Amurdad>»), non un generico «ti contatto».

⚠️ DEROGA 6 — IL MENU DI `:10714`-`:10715` NON PUO' RIPETERE QUELLO DI
`:10671`-`:10672`, che e' gia' reso («Va bene» / «Non capisco»). Sono due menu
dello stesso personaggio, a poche righe di distanza: 意味が分からない diventa
«Non capisco che vuoi dire» e だいたい分かった «Piu' o meno ho capito».

⚠️ 因縁 qui **non** e' il «conto aperto» di `chat.hsp:10116`: quello e' un
rancore fra persone, questo e' il legame karmico fra due anime. «Vincolo
d'anima».

PERIMETRO: 12 firme su 12 dentro il blocco, zero occorrenze fuori
(`python scratchpad/_85-blocco.py 10627`). Le altre due firme del blocco
(`:10671`, `:10672`) erano gia' rese.

MENU: due, da 2 voci l'uno — le due colonne non mordono.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte
(i puntini di sospensione si scrivono con tre punti).
"""

RESE = {
    # --- il primo incontro: la richiesta appena accennata
    10706: 'Ho una cosa da chiedere a te, mortale... Se ti va... torna a '
           'parlarmi...',

    # --- il racconto, e il menu delle due risposte
    10712: 'Il registro delle vite di questo mondo, dipinto con la luce '
           'astrale... Quando la morte arriva come sta scritto nel registro, '
           'si viene condotti alla galleria che porta ad Arkasha... e la vita '
           'si fa luce. Si fa luce e torna alle stelle... E un giorno, dal '
           'mare di luce, si nasce di nuovo...',
    10714: 'Non capisco che vuoi dire',
    10715: 'Più o meno ho capito',
    10716: 'Quelli usciti dal ciclo delle rinascite... li vedi...? Sì, '
           'per la legge del mondo non possono farsi luce di stella... e '
           'restano lì, semplicemente, a esistere... Nel buio, sulla tela '
           'delle anime, per sempre... Agli occhi dei vivi ne appare solo una '
           'parte... solo quelli che hanno un vincolo d\'anima, solo quelli...',
    10719: 'Non lo so... il tuo registro... non c\'è... Se tornerai luce, '
           'non lo so... L\'ombra di Arkasha dov\'è...?',
    10722: 'Che il buio eterno e la benedizione della luce delle stelle ti '
           'accompagnino...',

    # --- l'incarico: salvare l'anima smarrita
    10673: 'Ho trovato un\'anima innocente, prigioniera dei demoni... Da qui '
           'non posso uscire... vorrei che andassi tu a salvarla. La strada '
           'la apro io...',
    10676: 'Cerca di capire...',
    10685: 'Il gruppo è al completo: anche se ci vai, non potresti '
           'riportarla indietro...',
    10689: 'Una volta dentro, prima che se ne accorgano... fa\' presto...',

    # --- il ritorno con l'anima
    10630: 'Grazie della fatica... questa è la ricompensa... Se trovo '
           'un\'altra anima smarrita ti mando un\'altra chiamata... Ora lascia '
           'riposare la tua anima...',
}
