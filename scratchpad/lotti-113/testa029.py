# -*- coding: utf-8 -*-
"""114a - Lotto 029 di `db_item.hsp`: IL MOBILIO, terza parte.

`FILTER_FURNITURE`, righe 91.500-108.000: **30 righe** su 27 oggetti — 27
dell'indice 0 e **tre dell'indice 2** (`:94927`, `:98007`, `:98358`), che sono
le prime citazioni che il corpo del mobilio porta dentro.

⚠️ **E il mobilio che resta sta tutto DOPO, non prima.** Le 137 righe
dell'indice 0 e le 6 dell'indice 2 che restano vanno da **:108393 a :127609**:
sotto la riga 91.500 non ne resta **nessuna**. La prima stesura di questo
docstring diceva l'opposto — «tutte sotto la riga 91.500» — perche' il numero
veniva dalla tabella della 113a, che era scritta a mano e contava all'indietro.
Da qui `scratchpad/_114-corpo-da-fare.py`, che quel conto lo fa da se'.

### ⭐ LE FAMIGLIE CHE VANNO LETTE INSIEME

- **I tre lumi** (`:91718` il lampione moderno, `:91780` la lampada
  stravagante, `:91842` la candela): tre oggetti che fanno luce e nessuno dei
  tre la fa per lo stesso motivo — l'ornamento, il vanto dei nobili,
  l'atmosfera. Le rese restano tre.
  ⓘ `:91842` dice 恋する二人 come `:91274` del lotto 028 (il lampione innevato):
  li' era «accende il fuoco fra due innamorati», qui «la distanza fra due
  innamorati». Stesso termine, stessa resa.
- **I tre quadri** (`:94987` i girasoli, `:95049` il paesaggio, `:95111` la
  dama): stessa apertura 高名な画家が描いたとされる, che resta identica in tutte
  e tre — «che si dice dipinto da un pittore famoso» — e cambia solo il genere.
- **Le due macchine dei tesori** (`:103360` blu, `:103425` rossa): la **prima
  frase e' la stessa parola per parola**, e la seconda no. La resa della prima
  frase e' identica nelle due righe, come vuole `_107-firme-gemelle.py`.
- **Il gatto e chi non lo sopporta** (`:94925` e `:94927`): la statua e la
  battuta di <Tam>. La battuta nomina 石柱, la **colonna**, che e' la parola con
  cui la descrizione dell'indice 0 chiama l'oggetto: le due rese si tengono.
- **L'attrezzo da palestra** (`:98356` la reclame, `:98358` la prosa): due
  indici dello stesso oggetto, uno sotto l'altro nello stesso pannello.

### ⭐⭐ L'INGLESE SBAGLIA UNA VOLTA, E BUTTA VIA UNA FRASE

**`:94863`, il cristallo nero.** Il giapponese ha tre pezzi:
邪気を祓う (scaccia gli influssi maligni), 日の光を乱反射し燦然と輝く (rifrange
la luce del sole e sfolgora) e 古来から魔術において重要な位置を占める (occupa da
sempre un posto importante nella magia). L'inglese tiene il primo e il terzo e
**butta via il secondo**, che e' l'unico che dice come l'oggetto si vede. E' la
stessa forma del `:87505` del lotto 028, la credenza a cui l'inglese toglieva
l'estro nascosto del maestro.

⚠️ E due appiattimenti piu' piccoli, tutti e due sul quadro dei girasoli
(`:94987`): l'inglese scrive «The canvas is said to be filled with many
sunflowers» come se il *si dice* riguardasse i girasoli, mentre in giapponese
riguarda quello che i girasoli **fanno** — prendono l'occhio e il cuore di chi
guarda e non li lasciano piu'. E scrive 静物画 come «Still-life painting»
appiattendo il tipo di quadro, che invece distingue i tre: natura morta,
paesaggio, ritratto.

### ⭐ I TERMINI CERCATI A MANO

    サイバードーム   -> la Cupola Cibernetica   (`glossario.md:192`)
    ヴェルニース     -> Vernis                  (`invariati.md:40`, nome opaco)
    ヨウィン         -> Yowyn                   (`invariati.md:44`)
    パルミア         -> Palmia                  (`invariati.md:41`)
    警備部隊         -> corpo di guardia        (`db_creature.hsp`, <Orville>)
    マテリアル       -> materiale               (`chat.hsp`, «materiali da lavorazione»)
    大富豪           -> il riccone              (gia' nel dizionario)
    観葉植物         -> pianta ornamentale      (quattro nomi di oggetto)
    ガシャポンの玉   -> sfera del tesoro        (gia' nel dizionario)

⚠️ **パルミア警備隊 non e' nel dizionario**, ma 警備部隊 si': `<Orville> il
comandante della sicurezza` e «la scarsa preparazione del **corpo di guardia**».
Qui la resa e' «le guardie di Palmia», che e' la stessa cosa detta corta —
la riga e' gia' lunga e il pannello si impagina.

⚠️ **異国の硬貨 non e' nel dizionario in nessuna forma**: e' «una moneta
straniera», reso a lettera. Le monete che il dizionario conosce sono di bronzo
e di platino, e non sono queste.

### ⭐ LE TRE CITAZIONI PORTANO LE VIRGOLETTE CON L'ESCAPE

`:94927`, `:98007` e `:98356` sono discorso diretto, e nel sorgente HSP la
citazione sta dentro `\\"..\\"`. Il modello e' `_traduzioni026.py:23` (il
mesugaki): nella tabella si scrive `\\\\\\"`, che e' un backslash e una
virgoletta veri.

### ⭐ LA SETTIMA FONTE, PER IL CORPO

`scratchpad/lotti-113/_gia-reso.py` fa per la **prosa** la domanda che
`_113-fonti-gia-rese.py` fa per i titoli: questo giapponese e' gia' reso da
qualche altra parte? Per il lotto 029 la risposta e' **0 su 30** — nessuna di
queste trenta prose torna altrove nel gioco — e la prova al contrario e' il
lotto **028**, gia' reso, dove la stessa rete si accende **46 su 46**.

⚠️ La prima versione della rete diceva «30 su 30» e non voleva dire niente:
cercava il contenimento con la soglia su **un lato solo**, e ogni voce del
dizionario col giapponese corto — una particella, un `。` — sta dentro
qualunque prosa. La soglia va sui due lati.
"""
