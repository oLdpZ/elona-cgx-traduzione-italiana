# -*- coding: utf-8 -*-
"""115a - Lotto 038 di `db_item.hsp`: GLI SCARTI, prima parte.

`FILTER_JUNK`, righe 0-62.000: **44 righe** su 36 oggetti — 36 dell'indice 0,
4 dell'indice 1 e 4 dell'indice 2. E' il primo lotto della categoria, che ne ha
124 e non ha moltiplicatore: «da fare» e «vive» coincidono.

⚠️ La taglia si e' scelta con due tentativi in piu' del solito: fra `0 60000`
(39 righe) e `0 64000` (70) c'e' un **addensamento** — i sei materium e i sei
esplosivi stanno quasi attaccati. `0 62000` ne da' 44.

### ⭐⭐⭐ LA TILDE DI MONTE NON E' SEMPRE UNA TILDE, E SONO SETTE RIGHE

`_code.py` ha aperto il lotto dicendo «righe senza resa in tabella: **1**»,
dove il valore atteso e' 0. La riga e' `:46213`, la dernefia, e la sua coda
giapponese e' `#?ティリス園芸図鑑?`: **due punti interrogativi ASCII**
(U+003F) al posto della tilde larga (U+FF5E) che le altre **quaranta**
occorrenze dello stesso libro portano.

Non e' un artefatto della nostra estrazione: `db_item.hsp:46207` sta scritta
cosi' nel sorgente pinnato, e si legge byte per byte.

⭐ **Misurata, la famiglia e' piccola e compatta**:
`scratchpad/_115-fonti-storpiate.py` conta **7 code su 2.542**, tutte fra
`:46213` e `:46340` — tre oggetti soli, cioe' una sola sessione di lavoro di
monte. ⓘ Due delle sette la 112a le aveva gia' incontrate e messe in tabella
**con i punti interrogativi dentro la chiave**; questa e' la terza, e si e'
aggiunta allo stesso modo. La tabella adesso porta tre chiavi storpiate.

⚠️ Aggiungere la chiave **non cambia** il 234 di `_112-verifica-fonti`, che
conta le coppie del sorgente e non le voci della tabella. Verificato prima e
dopo.

### ⭐⭐ E UNA RIGA HA LA CODA IN GIAPPONESE E NON IN INGLESE: E' LA TERZA IN TUTTO IL CORPO

Sempre `:46213`: l'inglese la coda-fonte **non ce l'ha proprio**. Le altre due
in questa condizione sono `:47287` e `:47288`, trovate dal lotto 033, e la 114a
aveva gia' deciso che non gliela rimettiamo — il cancello conta il `#` contro
l'inglese, e aggiungerlo lo accende.

La resa quindi **non ha coda**, ed e' l'unica delle 44.

⚠️⚠️ `_112-verifica-fonti` questa cosa non la vede: la sua copertura salta le
righe senza coda inglese (`if not t_en: continue`). Il conto giusto lo da'
`_115-fonti-storpiate.py`, che dice **3 righe** — e per dirlo deve escludere i
**1.128 rapporti di identificazione**, il cui inglese una coda non ce l'ha mai.
ⓘ Senza quel taglio il numero e' 1.131 e non vuol dire niente: e' la lezione
della 114a sulla soglia mancante, ripetuta su un altro referto.

### ⚠️⚠️ IL CANCELLO DEI TITOLI PASSA DA 5 A 6, E ANCHE QUESTO E' DI MONTE

`:55921` (l'argilla) ha per fonte giapponese ～ルミエスト美術目録～, il catalogo
d'arte di Lumiest; l'inglese ci mette `~Vernis Ore Catalogue~`, che e' la fonte
di `:55983` (lo zolfo) e che in giapponese e' ～ヴェルニース鉱物図鑑～.

Il cancello chiava sull'inglese, quindi dopo questo lotto passa da **5 a 6**:
il sesto e' `~Vernis Ore Catalogue~` -> Catalogo d'Arte di Lumiest / Atlante
dei Minerali di Vernis. **Annunciato prima di misurarlo.** Un 7 e' nuovo.

ⓘ Che l'argilla stia nel catalogo d'arte e non in quello dei minerali ha senso:
serve a fare ceramiche. L'inglese ha guardato la sostanza e non il libro.

### ⭐⭐ I NOMI DELLE ABILITA' NON SI SCRIVONO A MEMORIA

Gli scarti da lancio dicono quasi tutti da quali **due** abilita' dipende la
loro potenza, e sono nove nomi in un lotto solo. Stanno gia' resi in
`skill.hsp`, e si prendono da li' con `lotti-113/_abilita038.py`:

    宝石細工 Oreficeria      生化学 Ingegneria genetica   戦術 Tattica
    魔力制御 Controllo magia  魔力の限界 Capacità magica    瞑想 Meditazione
    罠の知識 Disarmo trappole 工作 Falegnameria           投擲 Lancio
    魔道具 Dispositivi magici 料理 Cucina

⚠️⚠️ **E uno di questi nove non e' quello che sembra**: 射撃 in `skill.hsp` e'
**Mira** (`Marksman`), non «Tiro». «Tiro» e' la resa di `command.hsp` e
`help.hsp`, dove 射撃 e' l'azione. Nel corpo, dove il testo dice 〜の技術, la
parola giusta e' il nome dell'abilita' che il giocatore trova nella sua lista:
**Mira**.
⚠️ Difetto nostro gia' in gioco: l'indice 3 di `:76317` (la gemma di Mani) dice
«secondo il **Tiro**» per 射撃スキル依存. E' scritto qui perche' non si perda:
va uniformato in una passata sull'indice 3, non in un lotto del corpo.

### ⭐ L'INGLESE SBAGLIA CALDO PER FREDDO

`:52579`, il magaice: il giapponese dice 冷気 tre volte — il **gelo**. L'inglese
scrive «absorb hot air» e «when exposed to hot air», poi pero' chiude con
«freezing damage» e «the cold air», contraddicendosi da solo dentro la stessa
riga. Il nome dell'oggetto (冷吸の勾玉, «perla ricurva che assorbe il freddo») e
l'indice 3, gia' reso, dicono gelo. Si segue il giapponese.

### ⓘ Due giochi di parole, e uno si puo' tenere

`:46010`, il fukagurumi: il giapponese scrive なかなかジョーズに作られており,
dove ジョーズ e' insieme «Jaws» e 上手, «ben fatto». L'inglese dice «jawsome».
L'italiano ha **«fatto a pinna d'arte»**, che tiene tutt'e due i sensi.

`:42976`, l'expoopsion: la battuta e' nel nome, non nel testo, e il testo
giapponese e' serio (una fatta di forma «troppo artistica» che, essendo arte,
esplode). L'inglese ci aggiunge «the magnum poopus», che il giapponese non ha:
non si riporta.
"""
