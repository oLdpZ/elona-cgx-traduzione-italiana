# -*- coding: utf-8 -*-
"""94a - BONYAC il merciaio (`chat.hsp:15465`-`:15490`, 6 su 10).

雑貨店の『ボニャック』 / `<Bonyac> the general vendor`, reso **«<Bonyac> il
merciaio»** (`db_card.hsp:1856`, `db_creature.hsp:47220`). Le altre quattro
firme del blocco — le tre voci del menu e il `buff` — erano gia' rese.

⚠️⚠️ LA RIPRESA DELLA 93a LO DAVA PER «UN NEGOZIO, CHE SI APRE MOLTE VOLTE PER
PARTITA»: NON E' COSI'. `map.hsp:5042` lo mette in `ras05`, cioe' il **quinto
piano della Valle di Raskilis**, a poche caselle da un `OBLIVION_RUDE_BEAST`.
E' la bottega **abbandonata in fondo alla valle condannata**, non un emporio di
citta': si apre una volta per partita, e tutte e sei le righe parlano di
quello. 💡 Il conteggio delle firme non dice dove sta un parlante: lo dice
`map.hsp`.

⭐ IL REGISTRO E' GIA' FISSATO dal `buff` gia' reso, `:15470`: 「ラスキリス
いらっしゃいませ。」 → **«Benvenuti a Raskilis.»** Parla in ですます con la
formula del bottegaio, e la resa in essere ha gia' scelto il **voi**: le sei
righe nuove ci si accodano. ⚠️ Le voci del menu, che sono del **giocatore**,
danno del tu («Che cosa vendi?»): non e' un'incoerenza, sono due bocche
diverse.

LESSICO EREDITATO (non deciso qui):
  - ラスキリス  «Raskilis», «la Valle di Raskilis»  `chat.hsp:9381`, `:15184`, `:15470`
  - 谷          «la valle»                          `chat.hsp:15438`-`:15442` (91a)

⭐⭐ DEROGA 1 — `:15478` E `:15483`, DUE RIGHE CHE **DEVONO** ROMPERE IL SUO
REGISTRO. 「何も。」 e 「あ、それ在庫切れ。」 sono le uniche due righe del blocco
senza ですます, e sono le uniche due **battute**: alla domanda «Che cosa vendi?»
risponde secco «Niente.», e alla richiesta di pane «Ah, quello e' finito.» —
poi riparte il bottegaio compito con l'orgoglio della bottega. Se si uniforma
il registro si perde il tempo comico, che e' meta' del personaggio. Restano
brevi e piatte come l'originale.

⚠️ DEROGA 2 — `:15479`, PARLA DI SE' IN TERZA PERSONA, E NON E' L'INGLESE A
DIRLO. Il giapponese e' 「ここはボニャックの店なんです」. L'inglese ci mette
sopra un «**Mr.** Bonyac» e un «and it always will be» che il giapponese non ha;
la terza persona invece c'e' davvero, ed e' quella che regge la frase: non dice
«il mio negozio», dice «la bottega di Bonyac», come un'insegna.

⚠️ DEROGA 3 — `:15479`, 世界から忘れ去られようと.
«even if the rest of the world **forgets about us**»: il giapponese non ha
«us», il soggetto e' la bottega e il verbo e' passivo. ⭐ La riga rima con la
scena — la valle e' **chiusa dentro lo spazio** (`:15440`, «lo spazio si e'
richiuso»), quindi «il mondo se ne dimentica» e' letterale prima che
malinconico.

PERIMETRO: 6 firme da fare su 10 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 15465`).

MENU: uno, da 3 voci (`:15467`-`:15469`), gia' reso. Tutt'e tre le risposte
chiudono con `strbye`.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- «Meglio ripararsi»
    15473: 'Ma scherzate. Abbandonare questa bottega e scappare? Neanche per '
           'idea.',
    15474: 'È una bottega spoglia, lo so bene... Ma qui dentro ci sono i '
           'ricordi di tutti i clienti che ho avuto, e sono tanti.',

    # --- «Che cosa vendi?»
    15478: 'Niente.',
    15479: 'E ciò nonostante questa resta la bottega di Bonyac. Anche se non '
           'c\'è più niente da vendere, anche se il mondo se ne dimentica.',

    # --- «Vorrei del pane appena sfornato.»
    15483: 'Ah, quello è finito.',
    15484: 'Mi dispiace davvero. Se non fossimo in questa situazione, vi avrei '
           'sfornato un pane da leccarsi i baffi.',
}
