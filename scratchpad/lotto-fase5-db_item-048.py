# -*- coding: utf-8 -*-
"""118a - Lotto 048 di `db_item.hsp`: I GRIMORI, il CORPO, e la categoria CHIUDE.

`FILTER_ITEM_SPELLBOOK`, righe da `:102037` a `:129870`: **48 righe** su 42
oggetti — 42 dell'indice 0, **4 dell'indice 1** e 2 dell'indice 2. Con questo
lotto `FILTER_ITEM_SPELLBOOK` va a **0 da fare su 92 vive**: e' la **sesta**
categoria del corpo che si chiude, dopo mobilio, attrezzi, cibi, scarti e armi.

⚠️⚠️ Previsione di `applica`: **+48** per 48 rese, nessuna gemella.

### ⭐⭐⭐ L'INDICE 1 DEI GRIMORI: IL GIAPPONESE E L'INGLESE DICONO DUE COSE

Quattro righe di questo lotto — `:113099`, `:113172`, `:113245`, `:113460` —
non sono la stessa frase in due lingue. Sono **due contenuti diversi nello
stesso posto**:

    JP  <ランク6魔法>
    EN  \\"Ouch! Hot!\\" \\n# a Eulderna Researcher handling this tome

Il giapponese ci mette il **tassello del rango**; l'inglese lo butta e ci mette
una battuta. Non e' un appiattimento e non e' una perdita: e' l'unico posto del
file dove le due lingue riempiono lo slot con roba diversa.

**La decisione**: la build e' il ramo `en`, e la stringa che il giocatore legge
e' quella inglese. Si rende **quella**. Il rango resta non scritto, che e'
esattamente la decisione della 110a, e la battuta che il giocatore vede oggi non
sparisce.

### ⚠️⚠️⚠️ E LA DOMANDA «QUANTE CE NE SONO» HA SMENTITO LA 110a

Chiesto al sorgente — 「ランク…魔法」 su ogni `description()` di `db_item.hsp` —
il tassello del rango non e' su quattro righe: e' su **80**, una per **ogni**
grimorio, sempre in `description(1)` del ramo `if ( jp )`. Le quattro di questo
lotto sono le uniche **vive**, perche' per le altre 76 l'inglese lascia
`description(1) = ""` e una riga con l'inglese vuoto non arriva
nell'estrazione.

⚠️ Questo **smentisce l'argomento** su cui la 110a ha deciso di non scrivere il
rango. Il glossario dice, degli 82 inglesi dell'indice 3: «il giapponese non lo
dice mai — non su una sola riga [...] Il rango si sa dire; qui l'autore ha
scelto di non dirlo». L'autore lo dice, su tutti e 80 gli oggetti, **un indice
piu' su**. Il rango non e' un'aggiunta dell'inglese: e' una cosa che le due
lingue mettono in due posti diversi.

    JP   description(1)   <ランク6魔法>            80 righe su 80
    EN   description(3)   Book of Rank 6 Magic.   82 righe su 82
    IT   da nessuna parte                          (la decisione della 110a)

Oggi il giocatore italiano e' **l'unico dei tre** che il rango non lo legge. La
decisione va riaperta, e non la riapre questo lotto: le 80 righe dell'indice 3
sono gia' rese e chiuse (1.319 su 1.319), il loro tetto e' **secco a 69** e il
glossario stesso nota che ci stanno dentro proprio perche' non portano parole in
piu'. Rimetterci il rango e' un lavoro suo, da misurare prima di cominciarlo.

ⓘ La lezione e' quella della 117a, la `?` dell'uovo: la domanda giusta non e'
«come rendo questa riga», e' «quante ce ne sono». Stavolta la risposta non ha
confermato un numero — ne ha rovesciato uno scritto nel glossario da otto
sessioni.

### ⭐⭐⭐ IL NOME DEL LIBRO NON E' IL NOME DELL'INCANTESIMO, E QUI SONO TREDICI

La 047 aveva trovato tre righe in cui il nome del libro e quello
dell'incantesimo divergono. Qui sono **tredici su 42**, e
`_incantesimo.py 048` le trova tutte passando dall'`efid` invece che dal
nome:

    :104519  «conoscenza»            -> **Saggezza divina**
    :105228  «pioggia sacra»         -> **Scaccia i malocchi**
    :105742  «debolezza»             -> **Nebbia di fragilità**
    :106398  «resistenza»            -> **Scudo elementale**
    :106686  «silenzio»              -> **Nebbia di silenzio**
    :112952  «vortice caotico»       -> **Vortice del caos**
    :113025  «onda di boato»         -> **Onda fragorosa**
    :113459  «ago neurale»           -> **Ago dei nervi**
    :113532  «occhio caotico»        -> **Occhio del caos**
    :113605  «sospiro infernale»     -> **Sospiro d'oltretomba**
    :114013  «freccia magica»        -> **Dardo magico**
    :114788  «cartografia magica»    -> **Mappa magica**
    :123492  «teletrasporto minore»  -> **Teletrasporto breve**

⚠️ Nessuna rete lo vede: il nome del libro e' li' nel dossier, due righe sopra
la prosa, e sarebbe bastato copiarlo. Il conto dei due lotti e' **16 su 80**:
una riga su cinque.

### ⭐⭐ IL DESIDERIO E' L'UNICO 珍しい魔法書, E L'INGLESE LO PERDE

`:111850` apre con 「〜という呪文について学ぶことができる**珍しい**魔法書。」 —
un grimorio **raro**. E' l'unico degli 80 che porti l'aggettivo, ed e' il libro
del Desiderio, che nel gioco e' il piu' raro che ci sia (rango 50). L'inglese
scrive il solito «A spellbook to help you learn...» e la parola cade.

### ⚠️ UN ROVESCIAMENTO E DUE PAROLE LETTE MALE

  - ⚠️⚠️ `:129870` (il teletrasporto) — 今すぐ旅に出たいあなたに e' «per te che
    vuoi partire subito». L'inglese scrive «For those who hates traveling»: il
    **rovescio** della dedica;
  - `:128941` — 寒がり e' «chi sente il freddo». L'inglese legge «For those who
    catches the cold», il raffreddore;
  - `:106181` — 足を引っ張る e' «trattenere, ostacolare», ed e' il senso che il
    rallentamento chiede. L'inglese scrive «pull people's legs», prendere in
    giro;
  - `:113532` — 流し眼 e' l'occhiata di sottecchi, quella che si lancia di lato.
    L'inglese ne fa «people with a lot of eye problems»;
  - `:105301` — 体調の優れぬ e' «non essere in forma». L'inglese scrive «For the
    hardcore exorcists», che nel giapponese non c'e' in nessuna forma.

### ⓘ E quattro volte l'inglese butta la dedica e ne scrive una sua

`:105886` («Strangely reading this book gives you a slight adrenalin rush»),
`:114013` («Designed for beginners»), `:128868` («This tome let's off a static
discharge») e `:113459` («It makes people's eye twitch»). In tutt'e quattro il
giapponese dice 「〜なあなたに」 e parla a chi legge; l'inglese parla del libro.

### ⓘ I CANCELLI NON DEVONO MUOVERSI

Le code del lotto sono **cinque**, tutte gia' in tabella con una sola resa
italiana: `~Il Libro dei Libri: i Grimori~` (42 righe), `#un ricercatore
Eulderna che maneggia questo tomo` (3), e una a testa per `#un ricercatore
Eulderna che tiene in mano questo tomo`, `#un ricercatore Eulderna ripudiato` e
`#un incendiario in arresto`. Il cancello «titoli resi in PIU' modi» resta a
**7**.

⚠️ La forma: **6** righe su 48 hanno lo spazio prima del `\\n` — le quattro
dell'indice 1 e le due dell'indice 2 — e **nessuna** delle 48 code ha lo spazio
dopo il `#`, nemmeno le cinque il cui inglese ce l'ha. La coda italiana la
decide la tabella dei titoli, non la forma dell'inglese.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :102037
    (102037, "A spellbook to help you learn about the spell 'Mutation'. For those who want to change themselves.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Mutazione. Per te che vuoi cambiare te stesso.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :103649
    (103649, "A spellbook to help you learn about the spell 'Detect Object'. For future detectives.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Percezione oggetti. Per te che vuoi fare il detective.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :104519
    (104519, "A spellbook to help you learn about the spell 'Divine Wisdom'. For those who are going to the exams.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saggezza divina. Per te che stai per affrontare un esame.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :104592
    (104592, "A spellbook to help you learn about the spell 'Nightmare'. For those who overslept a lot.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Incubo. Per te che finisci sempre per dormire troppo.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :105228
    (105228, "A spellbook to help you learn about the spell 'Vanquish Hex'. For those of you who are feeling down and out.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Scaccia i malocchi. Per te che ti senti giù di morale.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :105301
    (105301, "A spellbook to help you learn about the spell 'Holy Light'. For the hardcore exorcists.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Luce purificatrice. Per te che non ti senti in forma.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :105525
    (105525, "A spellbook to help you learn about the spell 'Holy Veil'. For those with a fragile physique.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Velo sacro. Per te che sei di salute delicata.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :105669
    (105669, "A spellbook to help you learn about the spell 'Element Scar'. For those who knew the danger of nature.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Cicatrice elementale. Per te che vuoi sapere quanto la natura faccia paura.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :105742
    (105742, "A spellbook to help you learn about the spell 'Mist of Frailness'. For those who have a friend who is too proud of his strength.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Nebbia di fragilità. Per te che hai un amico che si vanta troppo della sua forza.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :105886
    (105886, "A spellbook to help you learn about the spell 'Hero'. Strangely reading this book gives you a slight adrenalin rush.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Eroismo. Per te che vuoi crogiolarti nel sentirti un eroe.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :106181
    (106181, "A spellbook to help you learn about the spell 'Slow'. For those who love to pull people's legs.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Rallentamento. Per te che vuoi mettere i bastoni fra le ruote al rivale.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :106254
    (106254, "A spellbook to help you learn about the spell 'Speed'. For those who want to stand out from your competitors.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Accelerazione. Per te che vuoi staccare il rivale.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :106398
    (106398, "A spellbook to help you learn about the spell 'Attirbute Shield'. For those who want to protect themselves against various threats.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Scudo elementale. Per te che vuoi difenderti da ogni sorta di pericolo.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :106542
    (106542, "A spellbook to help you learn about the spell 'Regeneration'. For those who want to heal in a more natural way.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Rigenerazione. Per te che guarisci lentamente dalle ferite.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :106686
    (106686, "A spellbook to help you learn about the spell 'Mist of Silence'. For those who with really annoying friends.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Nebbia di silenzio. Per te che hai un amico chiacchierone.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :106839
    (106839, "A spellbook to help you learn about the spell 'Holy Shield'. For those with a loose guard.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Scudo sacro. Per te che tieni la guardia bassa.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :111850
    (111850, "A spellbook to help you learn about the spell 'Wish'. For those who believe in a miracle.\\n#~Big Book of Magical Books~"):
        "Un grimorio raro su cui studiare l'incantesimo Desiderio. Per te che credi nei miracoli.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :112952
    (112952, "A spellbook to help you learn about the spell 'Chaos Ball'. For those who want to make a big mess.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Vortice del caos. Per te che vuoi far casino a più non posso.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :113025
    (113025, "A spellbook to help you learn about the spell 'Raging Roar'. For those who really, really hate their neighbours.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Onda fragorosa. Per te che vuoi fare chiasso a tutto volume.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :113027
    (113027, '\\"I swear I just heard something.\\" \\n# a Eulderna Researcher holding this tome'):
        "\\\"Giuro che ho appena sentito qualcosa.\\\" \\n#un ricercatore Eulderna che tiene in mano questo tomo",

    # ---------------------------------------------------------- :113098
    (113098, "A spellbook to help you learn about the spell 'Burning Storm'. For those who aims for global warming.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Tempesta ardente. Per te che vuoi scaldare l'aria qui intorno.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :113099
    (113099, '\\"Ouch! Hot!\\" \\n# a Eulderna Researcher handling this tome'):
        "\\\"Ahi! Scotta!\\\" \\n#un ricercatore Eulderna che maneggia questo tomo",

    # ---------------------------------------------------------- :113100
    (113100, '\\"I-I just want to start a flame in her heart..\\" \\n# arrested arsonist'):
        "\\\"I-io volevo solo accendere una fiamma nel suo cuore...\\\" \\n#un incendiario in arresto",

# 2 voci, 0 ambigue

    # ---------------------------------------------------------- :113171
    (113171, "A spellbook to help you learn about the spell 'Freezing Wave'. For those who try to prevent global warming.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Onda di gelo. Per te che vuoi rinfrescare l'aria qui intorno.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :113172
    (113172, '\\"Yeeek! Cold!\\" \\n# a Eulderna Researcher handling this tome'):
        "\\\"Iiih! Gela!\\\" \\n#un ricercatore Eulderna che maneggia questo tomo",

    # ---------------------------------------------------------- :113244
    (113244, "A spellbook to help you learn about the spell 'Mind Bolt'. For those who wants to do a sexy wink (and kill their rivals in the process).\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saetta mentale. Per te che sai fare un occhiolino irresistibile.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :113245
    (113245, '\\"My eyes hurt, and my head hurts even more..\\" \\n# a Eulderna Researcher handling this tome'):
        "\\\"Mi fanno male gli occhi, e la testa ancora di più...\\\" \\n#un ricercatore Eulderna che maneggia questo tomo",

    # ---------------------------------------------------------- :113317
    (113317, "A spellbook to help you learn about the spell 'Darkness Bolt'. For absolute edgelords with a supreme demon-king-evil eye.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saetta d'oscurità. Per te che hai uno sguardo che mette in soggezione.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :113459
    (113459, "A spellbook to help you learn about the spell 'Nerve Needle'. It makes people's eye twitch.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Ago dei nervi. Per te che scambi facilmente un incontro qualunque per il destino.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :113460
    (113460, '\\"In my theory, it\'s a sound spell that creates blackboard scratching noises.\\" \\n# outcast Eulderna Researcher'):
        "\\\"Secondo la mia teoria è una magia sonora che fa il rumore delle unghie sulla lavagna.\\\" \\n#un ricercatore Eulderna ripudiato",

# 4 voci, 0 ambigue

    # ---------------------------------------------------------- :113532
    (113532, "A spellbook to help you learn about the spell 'Chaos Eye'. For people with a lot of eye problems.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Occhio del caos. Per te che ti eserciti nello sguardo di sottecchi.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :113605
    (113605, "A spellbook to help you learn about the spell 'Nether Sigh'. Designed for devil's advocates.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Sospiro d'oltretomba. Per te che vuoi darti arie da demonio.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :114013
    (114013, "A spellbook to help you learn about the spell 'Magic Dart'. Designed for beginners.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Dardo magico. Per te che vuoi toccare l'essenza della magia.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :114350
    (114350, "A spellbook to help you learn about the spell 'Cure of Jure'. For those who almost met their demise.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Cura di Jure. Per te che vuoi scamparla per un pelo.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :114423
    (114423, "A spellbook to help you learn about the spell 'Cure of Eris'. For those who survived miraculously.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Cura di Eris. Per te che vuoi tornare vivo per miracolo.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :114496
    (114496, "A spellbook to help you learn about the spell 'Heal Criticle Wound'. For those who often suffers from accidents.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Cura ferite gravi. Per te che, sfortunato come sei, negli incidenti ci finisci spesso.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :114569
    (114569, "A spellbook to help you learn about the spell 'Heal Light Wound'. For those who are covered in scratches.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Cura ferite lievi. Per te che hai sempre addosso qualche ferita fresca.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :114642
    (114642, "A spellbook to help you learn about the spell 'Return'. For those who suffer from homesick.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Ritorno. Per te che ti prende spesso la nostalgia di casa.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :114715
    (114715, "A spellbook to help you learn about the spell 'Oracle'. For those who loves fortune-telling.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Oracolo. Per te che ami farti predire il futuro.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :114788
    (114788, "A spellbook to help you learn about the spell 'Magic Map'. For those who often lost their way home.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Mappa magica. Per te che ti perdi facilmente.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :123357
    (123357, "A spellbook to help you learn about the spell 'Summon Monsters'. For aspiring zoologists.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Evoca mostri. Per te che ami gli animali.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :123492
    (123492, "A spellbook to help you learn about the spell 'Short Teleport'. For those who hates walking.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Teletrasporto breve. Per te che camminare ti pesa.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :128868
    (128868, "A spellbook to help you learn about the spell 'Lightning Bolt'. This tome let's off a static discharge.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saetta di fulmine. Per te che i fulmini li vorresti vedere sempre.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :128941
    (128941, "A spellbook to help you learn about the spell 'Fire Bolt'. For those who catches the cold.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saetta di fuoco. Per te che soffri il freddo.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :129014
    (129014, "A spellbook to help you learn about the spell 'Ice Bolt'. For those who are heatstorke.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Saetta di gelo. Per te che soffri il caldo.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :129724
    (129724, "A spellbook to help you learn about the spell 'Uncurse'. For those believe in the spirits.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Purificazione. Per te che credi che gli spiriti esistano.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :129797
    (129797, "A spellbook to help you learn about the spell 'Identification'. For those who are paranoid about unknown things.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Identifica. Per te che hai il vizio di dubitare di tutto.\\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :129870
    (129870, "A spellbook to help you learn about the spell 'Teleport'. For those who hates traveling.\\n#~Big Book of Magical Books~"):
        "Un grimorio su cui studiare l'incantesimo Teletrasporto. Per te che vuoi partire per un viaggio subito.\\n#~Il Libro dei Libri: i Grimori~",

# 42 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-048.jsonl'
RIGHE = {
    102037, 103649, 104519, 104592, 105228, 105301, 105525, 105669, 105742, 105886,
    106181, 106254, 106398, 106542, 106686, 106839, 111850, 112952, 113025, 113027,
    113098, 113099, 113100, 113171, 113172, 113244, 113245, 113317, 113459, 113460,
    113532, 113605, 114013, 114350, 114423, 114496, 114569, 114642, 114715, 114788,
    123357, 123492, 128868, 128941, 129014, 129724, 129797, 129870,
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
