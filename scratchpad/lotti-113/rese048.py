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
