# -*- coding: utf-8 -*-
"""94a - KARATA la mascotte del seminario (`chat.hsp:14660`-`:14927`, 8 su 8).

マスコットの『カラ太』 / `<Karata> the seminar mascot`, reso **«<Karata> la
mascotte»** (`db_card.hsp:3143`, `db_creature.hsp:54550`). Sta nel blocco del
**Seminario d'Avventura**, gia' lavorato nell'87a (i quattro conferenzieri) e
nella 92a: il lessico era pronto prima di cominciare.

⭐ IL REGISTRO E' GIA' FISSATO da due posti diversi:
  - le sue **battute** (`db_creature.hsp:54530`, `:54536`, rese in un lotto
    precedente): parla di se' in **terza persona** — «Karata... non chiede
    altro...», «Adesso ti metto via!»;
  - la sua **carta** (`db_card.hsp:3137`, non ancora resa): e' un baule
    svuotato a cui e' nata una coscienza, ha divorato gente e distrutto due
    villaggi, e il fondatore del seminario l'ha battuto e **costretto** a fare
    la mascotte. ⚠️ E' questo che da' il fondo alle due righe tristi di oggi
    (`:14915` i colleghi che se ne sono andati, `:14921` «Karata si sente
    solo»): non e' una mascotte allegra, e' una mascotte **rimasta li'**.
⚠️ Da' del **キミ** al giocatore: tu, affettuoso. E' **maschio** — 太 e' un
suffisso di nome maschile, e l'inglese della carta scrive «his».

LESSICO EREDITATO (non deciso qui):
  - 冒険ゼミ    «Seminario d'Avventura»      `text.hsp:2866`, `chat.hsp:14542`-`:14547`
  - 努力賞      «premio per l'impegno»       `chat.hsp:14530` (lo stesso seminario)
  - 宝箱        «baule»                      `db_item.hsp:149550`
  - ミミック    «mimic»                      `db_card.hsp:7498`, `:9110`
  - タヌキ      «tanuki»                     `db_card.hsp:7160` (il tanuki mutaforma)
  - ギルド      «gilda»                      `chat.hsp:5289`
  - 冒険者      «chi va all'avventura»       formula del progetto

⚠️⚠️ DEROGA 1 — `:14914`, ツクモガミ SI TIENE, MA CON UNA GLOSSA.
ツクモガミ compare **una volta sola in tutto il sorgente** (verificato con
`_94-cerca.py`), e l'inglese la tiene com'e'. Il progetto tiene le parole
giapponesi quando il gioco le tiene — «tanuki», «ninja», «kunoichi», «mimic» —
e qui si fa lo stesso. ⚠️ Ma questa riga **e' una definizione**, e il suo lavoro
e' distinguersi dal mimic: al lettore giapponese la parola dice gia' «oggetto
vecchio che ha preso un'anima», all'italiano non dice niente, e senza quello il
confronto col mimic non si sente piu'. Quindi la parola resta e accanto le si
mette la glossa minima. E' l'unica riga del lotto che aggiunge parole.

⚠️ DEROGA 2 — `:14911`, IL BISTICCIO SU カラ E' GIA' PERDUTO A MONTE.
「あげたくなっちゃう**カラ**…」 scrive in katakana il から di «perche'», e quel
カラ e' il suo nome. Non e' una scelta di oggi: la stessa cosa succede in
`db_creature.hsp:54536` — 「カラ太は**からから**と笑った」 — che un lotto
precedente ha reso «Karata ha riso di gusto», senza bisticcio. Si resta
coerenti con quella, invece di inventare un gioco di parole in una riga sola.

⭐ DEROGA 3 — `:14921`, 友達のガイド.
Non e' un nome proprio: **ガイド e' un mestiere** e nel gioco lo fanno in tre —
«<Norne> la guida», «<Yonorne> la guida novellina», «<Arma> la guida turistica»
(`db_card.hsp:7017`, `:1271`, `:9045`) — e sono **tutti e tre ancora in
partita**, quindi la battuta non ne indica nessuno. Resta «la guida», generico
come l'originale. 💡 E «la guida ... sua amica» concorda col **nome**, che in
italiano e' femminile: non attribuisce un sesso a nessuno.

⭐ DEROGA 4 — `:14924`, 冒険者の地位.
「冒険者の地位を上げる」 non e' «improve the standing» in astratto: la frase
prima dice che la ditta tratta con lo Stato **perche' a chi va all'avventura
venga pagato uno stipendio**. E' un sindacato. La resa tiene il nesso.

PERIMETRO: 8 firme su 8 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 14660`), zero gia' rese altrove.

MENU: nessuno. Tutte `chatMore`. `:14808` esce solo quando c'e' un premio da
dare (`karata > 0`, sedici casi); le altre sette sono la chiacchiera fissa.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- il premio, quando c'e'
    14808: 'Tu studi con tantissimo impegno! Ecco un premio per l\'impegno: è '
           'poca cosa, ma Karata te lo dà di cuore!',

    # --- la chiacchiera fissa
    14911: 'Mmh... Con chi studia di buona lena, a Karata viene sempre voglia '
           'di dare un premio per l\'impegno...',
    14912: 'Detto questo.',
    14914: 'Karata è il tsukumogami di un baule, cioè un oggetto vecchio a cui '
           'è nata un\'anima! Col mimic, che il baule lo imita e basta, si '
           'somiglia ma non c\'entra niente!',
    14915: 'Una volta c\'erano anche altre mascotte più anziane, un tanuki, un '
           'leone... ma se ne sono andate tutte...',
    14918: 'Il Seminario d\'Avventura fa parte di una ditta che si chiama '
           'Vanessa Corporation! E a scoprire Karata è stata proprio Vanessa, '
           'la fondatrice.',
    14921: 'Vanessa, quella che ha fondato il Seminario, voleva avventure '
           'ancora più grandi ed è partita per lo spazio insieme alla guida, '
           'che è sua amica! Chissà quando torna. Karata si sente solo...',
    14924: 'La Vanessa Corporation tratta con lo Stato perché a chi va '
           'all\'avventura venga pagato uno stipendio, e fa anche da sponsor '
           'alle gilde! Si dà un gran daffare per tirare su chi va '
           'all\'avventura.',
}
