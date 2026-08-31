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

Sembra ovvio, e su tre righe e' **falso**:

    :91982  il libro dice 「扉生成」        l'incantesimo e' ドア生成
            en 'Door Creation'             -> **Crea porte**  (skill.hsp:709)
    :94175  il libro e' «mani guaritrici»  l'incantesimo e' 癒しの手
            en 'Healing Touch'             -> **Tocco curativo** (skill.hsp:434)
    :93222  il libro e' «suolo acido»      l'incantesimo e' 酸の海
            en 'Acid Ground'               -> **Terreno acido** (skill.hsp:699)

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
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :47359
    (47359, "A spellbook to help you learn about the spell 'Thunder Vortex'. For those who want to get angry and cast thunderbolts.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Vortice di tuoni. Per te che, quando ti arrabbi, vuoi far cadere i fulmini.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :47432
    (47432, "A spellbook to help you learn about the spell 'Eclipse Jail'. For those who find solace in the mystery of the dark.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Gabbia d'eclissi. Per te che nel buio senti il mistero.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :47505
    (47505, "A spellbook to help you learn about the spell 'Roar of Hades'. For those who wants to reign in hell.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Ruggito d'oltretomba. Per te che vuoi regnare sull'inferno.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :47578
    (47578, "A spellbook to help you learn about the spell 'Poison Storm'. For those who want to pollute the environment.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Tempesta velenosa. Per te che vuoi spargere veleno dappertutto.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :47651
    (47651, "A spellbook to help you learn about the spell 'Bubble Storm'. For those who loves soap bubbles.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Tempesta di bolle. Per te che ami le bolle di sapone.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :47724
    (47724, "A spellbook to help you learn about the spell 'Dreaming Roar'. For those who loves dreaming.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Ruggito illusorio. Per te che sogni a occhi aperti.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :47797
    (47797, "A spellbook to help you learn about the spell 'Anguish Jail'. For sadists.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Gabbia d'angoscia. Per te che sei un sadico.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :47870
    (47870, "A spellbook to help you learn about the spell 'Nether Bolt'. For enemies you want to throw into hell.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saetta d'oltretomba. Per te che hai qualcuno da mandare all'inferno.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :47943
    (47943, "A spellbook to help you learn about the spell 'Poison Bolt'. For genuinely toxic people.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saetta velenosa. Per te che ami le cose dai colori velenosi.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :48016
    (48016, "A spellbook to help you learn about the spell 'Sound Bolt'. For those who like to annoy their neighbours.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saetta sonora. Per te che ami il baccano.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :48089
    (48089, "A spellbook to help you learn about the spell 'Chaos Bolt'. For those who love to mess things up.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saetta caotica. Per te che stai più tranquillo quando è tutto in disordine.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :48162
    (48162, "A spellbook to help you learn about the spell 'Nerve Bolt'. For those who find love in suffering.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saetta dei nervi. Per te che credi che l'amore sia proprio il dolore.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :48235
    (48235, "A spellbook to help you learn about the spell 'Fire Claw'. For those who want to leave a hot scar.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Artiglio di fuoco. Per te che vuoi lasciare cicatrici bollenti.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :48237
    (48237, '\\"I have found a new reason to LIVE.\\" \\n# ~some Eulderna Pyromaniac~'):
        "\\\"Ho trovato una nuova ragione per VIVERE.\\\" \\n# ~un piromane Eulderna~",

    # ---------------------------------------------------------- :48308
    (48308, "A spellbook to help you learn about the spell 'Cold Blade'. For those who are naturally cool.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Lama di gelo. Per te che resti freddo e imperturbabile.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :48381
    (48381, "A spellbook to help you learn about the spell 'Lightning Spear'. For those wanted to wielded these rays of lightning, which remains fierce even as they fade.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Lancia di fulmine. Per te che vuoi lasciare tutti folgorati.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :48454
    (48454, "A spellbook to help you learn about the spell 'Mind Thorn'. For those wanted to trick enemies with illusion.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Spina mentale. Per te che vuoi prenderti gioco del nemico con le allucinazioni.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :48527
    (48527, "A spellbook to help you learn about the spell 'Poison Mucus'. For those loves poisonous creatures.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Muco velenoso. Per te che ti interessi alle creature velenose.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :48600
    (48600, "A spellbook to help you learn about the spell 'Sound Cannonball'. For those who wants to blast people with music.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Cannonata sonora. Per te che vuoi far volare via la gente a suon di musica.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :48673
    (48673, "A spellbook to help you learn about the spell 'Hydro Fang'. For those want people to know more about hydrophobia.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Zanna d'acqua. Per te che sai quanto l'acqua faccia paura.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :58993
    (58993, "A spellbook to help you learn about the spell 'Gem Power'. For those who are interested in Healing Crystals.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Pietra protettrice. Per te che ti interessi ai cristalli e al loro potere.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :61866
    (61866, "A spellbook to help you learn about the spell 'Hydro Bolt'. For those who love watercraft.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saetta d'acqua. Per te che vuoi diventare maestro nei giochi d'acqua.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :65600
    (65600, "A spellbook to help you learn about the spell 'Concentration'. For those who wants to concentrate more on things.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Concentrazione. Per te che vuoi concentrarti su quello che hai davanti.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :72957
    (72957, "A spellbook to help you learn about the spell 'Feather'. For those who wants to lose body weight.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Piuma. Per te che vuoi alleggerirti il corpo, almeno per un po'.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :78727
    (78727, 'A piece of paper containing the secret techniques of the cooks. You could learn as much as the best cooks with this. Whether you had the skill to keep up with it or not. \\n# ~Supporting Roles in Kitchen~'):
        "Un foglio dove stanno chiusi il gusto e le tecniche segrete dei cuochi. Con questo si può avere un sapere che non è da meno di quello di un cuoco di prima categoria. ...Poi, che la mano tenga il passo, è un altro discorso. \\n# ~I Comprimari della Cucina~",

    # ---------------------------------------------------------- :82077
    (82077, "A spellbook to help you learn about the spell 'Wizard's Harvest'. For those deeply in debt.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Raccolto del mago. Per te che hai avuto una spesa imprevista dopo l'altra.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :82079
    (82079, '\\"Wizards Harvest go brrr.\\" \\n# Bureau of Eulderna Punditry (BEP)'):
        "\\\"Il Raccolto del mago fa brrr.\\\" \\n#Ufficio Eulderna degli Studi Dotti (UESD)",

    # ---------------------------------------------------------- :82150
    (82150, "A spellbook to help you learn about the spell '4 Dimesional Pocket'. Designed for lazy hoarders.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Tasca quadridimensionale. Per te che di carattere non riesci a mettere in ordine.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :83555
    (83555, "A spellbook to help you learn about the spell 'Contigency'. For those who want to befriend their reaper.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Patto. Per te che vuoi fare amicizia con la Morte.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :84440
    (84440, "A spellbook to help you learn about the spell 'Magic Bolt'. For those who loves dynamites and laser beams.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saetta magica. Per te che vuoi sparare raggi dalle dita.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :84513
    (84513, "A spellbook to help you learn about the spell 'Magic Storm'. For those who wants to go outside during etherwind.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Tempesta magica. Per te che nei giorni di pioggia non stai in casa.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :85101
    (85101, 'A valuable document with diverse things written about it. It is believed that by reading and understanding it, one can come into contact with higher beings. \\n# ~Big Book of Magical Books: Pre-Censorship~'):
        "Un documento prezioso, dove sta scritto di tutto un po'. Si crede che, a decifrarlo, si possano sfiorare esseri superiori. \\n# ~Il Libro dei Libri: i Libri da Decifrare~",

    # ---------------------------------------------------------- :86940
    (86940, "A spellbook to help you learn about the spell 'Darkness Wedge'. For those who want to be cool and edgy.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Cuneo d'oscurità. Per te che vuoi darti un'aria da duro.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :86942
    (86942, '\\"This tome seems to carefully bend light.\\" \\n# a Eulderna Researcher'):
        "\\\"Pare che questo tomo pieghi la luce con cura.\\\" \\n#un ricercatore Eulderna",

    # ---------------------------------------------------------- :89010
    (89010, "A spellbook to help you learn about the spell 'Incognito'. For the trickers kinds.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Incognito. Per te che ami i dispetti.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :91982
    (91982, "A spellbook to help you learn about the spell 'Door Creation'. For those of you who want to open the door to someone else's heart.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Crea porte. Per te che vuoi aprire la porta del cuore di qualcuno.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :92870
    (92870, "A spellbook to help you learn about the spell 'Fire Wall'. For the all-year cold sufferer.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Muro di fuoco. Per te che patisci il freddo tutto l'anno.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :93222
    (93222, "A spellbook to help you learn about the spell 'Acid Ground'. For those who love to make a huge mess that is extremely unpleasant to clean up.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Terreno acido. Per te che sei debolmente alcalino.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :94175
    (94175, "A spellbook to help you learn about the spell 'Healing Touch'. For those who wants to shake hands with everyone.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Tocco curativo. Per te che tratti tutti allo stesso modo, senza distinzioni.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :94319
    (94319, "A spellbook to help you learn about the spell 'Healing Rain'. For those who want to show their companions love.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Pioggia curativa. Per te che ami i tuoi compagni.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :94454
    (94454, "A spellbook to help you learn about the spell 'Wall Creation'. For those with social anxiety.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Crea muri. Per te che vuoi restare solo.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :98649
    (98649, "A spellbook to help you learn about the spell 'Spider Web'. For those who celebrates Halloween everyday.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Ragnatela. Per te che vuoi divertirti con decorazioni un po' strane.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :98651
    (98651, '\\"I swear I saw spiders crawling out of this tome.\\" \\n# a Eulderna Researcher'):
        "\\\"Giuro di aver visto dei ragni uscire da questo tomo.\\\" \\n#un ricercatore Eulderna",

# 4 voci, 0 ambigue

    # ---------------------------------------------------------- :98874
    (98874, "A spellbook to help you learn about the spell 'Domination'. For thos who want to become friends with that girl you had a crush on.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Dominio. Per te che vuoi fare amicizia con quella ragazza che ti piace.\\n#~Il Libro dei Libri: i Grimori~",

# 40 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-047.jsonl'
RIGHE = {
    47359, 47432, 47505, 47578, 47651, 47724, 47797, 47870, 47943, 48016,
    48089, 48162, 48235, 48237, 48308, 48381, 48454, 48527, 48600, 48673,
    58993, 61866, 65600, 72957, 78727, 82077, 82079, 82150, 83555, 84440,
    84513, 85101, 86940, 86942, 89010, 91982, 92870, 93222, 94175, 94319,
    94454, 98649, 98651, 98874,
}
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_item.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_107-daitem.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if v['riga'] in RIGHE]
# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006), col `//` (100a) o dentro un
# blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
# ⚠️ Lo strumento, non lo scratch: `strumenti/commenti.py` e' la stessa funzione
# di `scratchpad/commenti-blocco.py` ma con dei test, e dalla 100a sa anche del
# commento di riga `//`.
from strumenti import commenti as _cb
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    testo = sorgente[riga - 1]
    return (testo.lstrip().startswith(';')
            or _cb.lang_spenta_da_barre(testo)
            or riga in SPENTE)


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _testa = sorgente[_righe[0] - 1]
        if _testa.lstrip().startswith(';'):
            _come = "e' commentata nel sorgente"
        elif _cb.lang_spenta_da_barre(_testa):
            _come = "e' spenta da un commento `//`"
        else:
            _come = 'sta dentro un commento di BLOCCO'
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[chiave(v)]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
