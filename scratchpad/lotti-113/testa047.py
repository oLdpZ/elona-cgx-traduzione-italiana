# -*- coding: utf-8 -*-
"""118a - Lotto 047 di `db_item.hsp`: I GRIMORI, il CORPO, prima parte.

`FILTER_ITEM_SPELLBOOK`, righe da `:47359` a `:98874`: **44 righe** su 40
oggetti — 40 dell'indice 0 e **4** dell'indice 2. La categoria e' **intatta**
(«da fare» 92, «vive» 92) ed e' la piu' grossa rimasta del corpo: 92 righe non
stanno in un lotto solo, e il taglio a `:100000` le divide in 44 e 48.

⚠️⚠️ Previsione di `applica`: **+44** per 44 rese. `_previsione.py 047` non
trova gemelle — 44 righe, 44 firme distinte — e il conto e' stato scritto
**prima**, come vuole la 117a.

### ⭐⭐⭐ IL NOME DELL'INCANTESIMO NON STA NEL NOME DEL LIBRO

Trentotto righe su 44 dicono la stessa cosa: 「「X」という呪文について学ぶこと
ができる魔法書。」 — *un grimorio su cui studiare l'incantesimo X*. X e' il nome
che il giocatore legge nella **lista degli incantesimi**, e prenderlo dal nome
del libro sembra ovvio: il libro si chiama «grimorio del vortice di tuono» e
l'incantesimo si chiama «Vortice di tuoni».

Sembra ovvio, ed e' **falso su 37 grimori su 80** — misurato, non stimato, da
`scratchpad/_118-nomi-vs-incantesimi.py`. In questo lotto per esempio:

    :91982  il libro dice 「扉生成」        l'incantesimo e' ドア生成
            en 'Door Creation'             -> **Crea porte**  (skill.hsp:709)
    :94175  il libro e' «mani guaritrici»  l'incantesimo e' 癒しの手
            en 'Healing Touch'             -> **Tocco curativo** (skill.hsp:434)
    :93222  il libro e' «suolo acido»      l'incantesimo e' 酸の海
            en 'Acid Ground'               -> **Terreno acido** (skill.hsp:699)

⚠️ E le due specie di divergenza non sono la stessa cosa. In **giapponese** il
nome del libro e lo skillname coincidono su 78 righe su 80: le due eccezioni
sono `:91976` e `:102031`, e sono di monte. Le altre 35 sono **nostre** — la
tabella dei nomi degli oggetti e `skill.hsp` sono stati resi in sessioni
diverse, e nessuno strumento del progetto confronta le due. Vedi `testa048.py`.

Su `:91982` il giapponese del libro e la lista degli incantesimi non dicono
nemmeno la stessa parola: 扉 contro ドア. Un giocatore che cercasse «扉生成» —
o la sua resa — nella lista non lo troverebbe, perche' li' non c'e'.

⭐ **Il percorso e' nel codice, e adesso e' uno strumento.**
`scratchpad/lotti-113/_incantesimo.py NNN` va, per ogni riga del lotto, dal
blocco `if ( dbid == ... )` che la contiene all'`efid = SKILL_SPELL_...` del
ramo `DBMODE_ON_READ`, poi allo `skillname()` di `skill.hsp`, e da li' alla resa
che il dizionario ha gia'. Su 42 righe di grimorio risolve **42 nomi su 42**,
zero non resi, e le due righe che restano sono i due libri che non insegnano
niente (la ricetta e il libro antico).

ⓘ E' la lezione della 110a — «il codice e' la quinta fonte» — usata **prima** di
scrivere invece che per rimediare: nessuna rete del lotto guarda `skill.hsp`, e
il difetto che avrebbe prodotto (un nome che nella lista non esiste) sarebbe
stato invisibile a tutti i cancelli e visibile solo al giocatore.

### ⭐⭐ L'INGLESE SBAGLIA IL NOME DI UN INCANTESIMO DA SOLO

Su `:47724` l'inglese scrive `'Dreaming Roar'`, ma lo skillname e' 夢幻の咆哮 /
`Illusion Roar`. Non e' un appiattimento: e' l'inglese che, dentro la propria
lingua, chiama la stessa magia con due nomi diversi in due schermate diverse.
Reso **Ruggito illusorio**, che e' il nome della lista.
ⓘ Stessa forma su `:47505`, dove la descrizione dice `'Roar of Hades'` e la
lista dice `Nether Roar`.

### ⭐⭐ LA DEDICA IN SECONDA PERSONA, CHE L'INGLESE PERDE TUTTE E 38 LE VOLTE

La seconda frase e' sempre 「〜なあなたに。」: una dedica da quarta di copertina,
rivolta a **te** che stai leggendo. L'inglese la gira in terza persona **tutte
e 38 le volte** — «For those who...», «For sadists», «For genuinely toxic
people», «Designed for lazy hoarders» — e la battuta smette di essere rivolta a
qualcuno. ⓘ Il punto piu' vicino che l'inglese raggiunge e' «For those of you
who...» di `:91982`, che e' ancora una terza persona con dentro un «voi».

In italiano resta **«Per te che...»**, che e' la forma della pubblicita' e del
risvolto di copertina, e che il giapponese ha scelto per tutte e 38.

### ⭐ Tre battute che l'inglese legge male, e una che l'italiano tiene intera

  - `:61866` — 水芸 e' il **gioco di prestigio con l'acqua**, l'arte del
    palcoscenico. L'inglese scrive «those who love watercraft», la
    navigazione: e' un'altra parola;
  - `:47943` — 毒々しい non e' «tossico» (l'inglese: «For genuinely toxic
    people»). E' il colore acceso e sgradevole di cio' che **sembra** velenoso;
  - `:72957` — 体を一時的に軽くする e' alleggerire il corpo per un po', ed e'
    la levitazione. L'inglese scrive «lose body weight» e ne fa una dieta;
  - ⭐ `:48381` — 皆を痺れさせたい gioca su 痺れる, che e' tutt'e due le cose:
    intorpidire e far restare a bocca aperta. In italiano **«folgorare»** le
    tiene tutt'e due, e il gioco di parole non si perde. E' il precedente delle
    fusioni delle razze: si rende il gioco, non le sillabe.

### ⓘ Le due righe che non sono grimori, e la loro coda

`:78727` (la ricetta) e `:85101` (il libro antico) sono gli stessi due che nel
lotto dell'indice 3 stavano fuori dalla griglia. La ricetta e' 紙片, un
**foglio** che non si legge — si usa e si consuma — e 調理人 e' «il cuoco»,
come in `:117599` del lotto 046.

⚠️ La coda del libro antico e' `~Big Book of Magical Books: Pre-Censorship~`,
che **non** e' la stessa dei 38 grimori: la tabella dei titoli le tiene distinte
(«i Grimori» contro «i Libri da Decifrare»), e il cancello dei titoli non si
muove.

### ⓘ LE QUATTRO CITAZIONI DELL'INDICE 2, DOVE IL GIAPPONESE NON C'E'

`:48237`, `:82079`, `:86942` e `:98651` hanno il giapponese **vuoto**: sono
quattro battute che l'inglese ha aggiunto di suo, e l'inglese e' l'unica fonte
che ci sia. «Tomo» viene dal glossario (`a Eulderna Researcher handling this
tome` -> «un ricercatore Eulderna che maneggia questo tomo»), e su `:82079` il
«go brrr» del meme della stamperia si tiene: e' scritto per essere quello.

⚠️ Le loro code italiane si incollano **come le da' `_code.py`**, spazio dopo il
`#` compreso: due su quattro non ce l'hanno (`#un ricercatore Eulderna`,
`#Ufficio Eulderna degli Studi Dotti (UESD)`) mentre l'inglese ce l'ha. La coda
italiana la decide la tabella dei titoli, non la forma dell'inglese.

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le code del lotto sono **sei**, tutte gia' in tabella con una sola resa
italiana: `~Il Libro dei Libri: i Grimori~` (38 righe), `#un ricercatore
Eulderna` (2), e una a testa per `# ~un piromane Eulderna~`,
`#Ufficio Eulderna degli Studi Dotti (UESD)`, `# ~I Comprimari della Cucina~` e
`# ~Il Libro dei Libri: i Libri da Decifrare~`. Il cancello «titoli resi in
PIU' modi» resta a **7**.

⚠️ La forma e' quasi uniforme: **6** righe su 44 hanno lo spazio prima del
`\\n` — le quattro dell'indice 2 piu' la ricetta e il libro antico — e le 38 dei
grimori non ce l'hanno. Si legge lo stesso `scratchpad/lotti-113/_forma.py 047`.

⚠️ **Una parola lunga**, e voluta: «quadridimensionale» (18 caratteri, `:82150`)
sfora la finestra di rinculo del preflight. Provata sull'impaginatore vero
(`_107-descrizioni-item.righe_a_schermo`) **non si spezza** e non allarga la
riga: il nome dell'incantesimo e' quello della lista, e accorciarlo darebbe al
giocatore una voce che non esiste.
"""
