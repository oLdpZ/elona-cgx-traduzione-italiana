# -*- coding: utf-8 -*-
"""94a - ZISILION il re sfaccendato delle miniere (`chat.hsp:13897`-`:13923`, 6 su 6).

有閑鉱山王『ジシリオン』 / `<Zisilion> the mine king`, reso **«<Zisilion> il re
sfaccendato delle miniere»** (`db_card.hsp:3260`, `db_creature.hsp:55291`).
⚠️ L'epiteto italiano viene da 有閑 — sfaccendato, che vive di rendita — e non
c'e' nell'inglese: e' gia' deciso e non si tocca.

⭐⭐ IL REGISTRO E' GIA' FISSATO, RIGA PER RIGA, dalle sue **dieci battute** rese
in un lotto precedente (`db_creature.hsp:55259`-`:55277`). Non e' un tono
generico: e' un personaggio che parla **solo di lavoro**, e le battute lo dicono
meglio di qualunque descrizione —
  «Vanno amati, i lavoratori.» · «Che noia...» · «Lavorare gratis e' la cosa
  che detesto di piu'!» · «Quanto vale una vita, secondo te?» · «Rapinare e
  uccidere sara' anche lavoro...?» · «Com'e' andata la mia prestazione?» ·
  ⭐ «Ho fatto una bella **sudata**.»
Usa 僕 e 君: **tu**, cordiale, un po' annoiato.

⭐⭐⭐ IL GEMELLO CHE DECIDE UNA PAROLA: `:13916` dice 「素晴らしい汗だ」, e la
battuta `db_creature.hsp:55277` dice 「いい汗をかいたよ」, gia' resa **«Ho fatto
una bella sudata»**. E' la stessa immagine, dello stesso personaggio, a due file
di distanza: qui si scrive **«sudata»** e non un sinonimo, se no il tic del
personaggio si spezza in un punto dove nessuna rete lo vede.

LESSICO EREDITATO (non deciso qui):
  - プラチナ硬貨  «monete di platino»    `action.hsp:931`, `chat.hsp:7941`
  - 関所          «posto di frontiera»   `map.hsp:682`
  - 街の依頼      «incarichi di città»   `chat.hsp:13964`, `:13978`

⭐ DOVE STA: `map.hsp:1789` lo mette in `station-nt1` **solo dal lato
`AREA_ST_NORTH_BORDER`**, cioe' il posto di frontiera fra Tyris del Nord e
Tyris del Sud, sul versante meridionale. E' un passaggio obbligato, e lui regala
tre monete di platino **al giorno** a chi ha finito un incarico di citta': e' la
ragione per cui questo blocco vale piu' delle sue sei righe.

⚠️ DEROGA 1 — `:13900`, LE VIRGOLETTE DI 「適度な」 SI TENGONO.
Il giapponese ne vira **solo** 「適度な」, ed e' la capriola della battuta: il
lavoro e' splendido *in giusta misura*, e lui che non lavora piu' si assolve con
quella misura. L'inglese le butta e scrive «a modest amount of work» in tondo.
Le virgolette restano, nella forma che il sorgente HSP accetta (barra rovescia
piu' virgoletta), come gia' a `chat.hsp:7879`.

⚠️ DEROGA 2 — `:13916`, L'INGLESE INVENTA UNA BATTUTA CHE NON C'E'.
«Another day, another platinum coin, eh?» non traduce niente: il giapponese e'
「ううん…素晴らしい汗だ」, cioe' lui che **fiuta la fatica** e la trova bella.
E' la stessa mano che a `:13901` lo tiene fermo a guardare la gente passare.

⚠️ DEROGA 3 — `:13913`, 街の依頼 E' UN NOME DI COSA, NON «a request for the city».
Nel gioco gli **incarichi di città** sono una meccanica con un nome suo, gia'
reso due volte nel corso del seminario (`:13964`, `:13978`). La riga sta dicendo
al giocatore **che cosa deve fare per essere pagato**, non facendo un discorso.

PERIMETRO: 6 firme su 6 dentro il blocco, **zero occorrenze fuori**
(`python scratchpad/_85-blocco.py 13897`), zero gia' rese altrove.

MENU: nessuno. Tutte `chatMore`.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""

RESE = {
    # --- il primo incontro
    13900: 'Tu sì che lavori, eh. Io lo trovo splendido, il lavoro. Ti guadagni '
           'da vivere e dai anche il tuo alla società... Per un animale sociale '
           'il lavoro \\"nella giusta misura\\" è una bella cosa. Io però un '
           'patrimonio l\'ho già messo da parte, e adesso di lavorare non mi va '
           'più...',
    13901: 'Ma anche uno come me un piccolo piacere ce l\'ha. Sto qui a '
           'guardare la gente che va e viene dal posto di frontiera, e a chi ha '
           'l\'aria di darci dentro do qualche moneta di platino. Ne do un po\' '
           'anche a te.',

    # --- se si torna troppo presto
    13909: 'Eh no, non essere ingordo... Ripassa domani.',
    13913: 'Tu, oggi, un incarico di città non l\'hai ancora portato a termine, '
           'mi pare. Quando l\'avrai fatto, ripassa.',

    # --- il regalo di ogni giorno
    13916: 'Sembra che tu lavori di buona lena. Mmh... che bella sudata. A te '
           'che ci dai dentro un po\' di platino lo do volentieri.',
    13921: 'E ripassa domani.',
}
