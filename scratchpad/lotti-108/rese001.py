import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :42785 la mesugaki
    (42785, 'It is seafood that can be cooked and eaten.'):
        "Un cibo di mare che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :52111 la pianta acquatica
    (52111, 'It is vegetable that can be cooked and eaten.'):
        "Una verdura che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :52246 l'anguilla giardiniera
    # ⚠️ stesso inglese di :42785, giapponese diverso solo per due tabulazioni:
    #    e' la stessa cosa e si scrive uguale.
    (52246, 'It is seafood that can be cooked and eaten.'):
        "Un cibo di mare che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :55077 il cristallo curativo
    (55077, 'It is a precious food used to cure ether disease.'):
        "Un cibo prezioso che guarisce la malattia dell'etere.",

    # ---------------------------------------------------------- :55547 la gomma masticata
    (55547, 'It is food that barely restores satiety.'):
        "Un cibo che sazia appena appena.",

    # ---------------------------------------------------------- :55610 la gomma da masticare
    (55610, 'It is food that can slightly restore satiety.'):
        "Un cibo che sazia poco.",

    # ---------------------------------------------------------- :56403 la pastura
    (56403, '(Single-use) tool type food for feeding fishes placed on the ground.'):
        "Un cibo da dare ai pesci posati per terra (usa e getta).",

    # ---------------------------------------------------------- :56874 l'hamburger
    (56874, 'It is food that can restore satiety.'):
        "Un cibo che sazia.",

    # ---------------------------------------------------------- :56937 l'osiruko, l'ozouni
    (56937, 'It is food that can restore satiety. CHOKE WARNING.'):
        "Un cibo che sazia. Certe volte va di traverso.",

    # ---------------------------------------------------------- :57191 il pesce essiccato
    (57191, 'It is a dried out fish that can restore satiety.'):
        "Un pesce essiccato che sazia.",

    # ---------------------------------------------------------- :57254 la verdura essiccata
    (57254, 'It is a dried out vegetable that can restore satiety.'):
        "Una verdura essiccata che sazia.",

    # ---------------------------------------------------------- :57317 la frutta secca
    (57317, 'It is a dried out fruit that can restore satiety.'):
        "Un frutto essiccato che sazia.",

    # ---------------------------------------------------------- :58592 il tofu fritto e i suoi
    (58592, 'It is food that can restore satiety.'):
        "Un cibo che sazia.",

    # ---------------------------------------------------------- :60517 le tre bottiglie del condimento
    # ⚠️ il giapponese dice solo 「調味料だ。使用することができる（使い捨て）。」.
    #    L'inglese aggiunge il bestiame prima della macellazione: si tace, per la
    #    regola della 57a e della 91a (decisioni.md, «Quando l'inglese aggiunge un fatto»).
    (60517, '(Single-use) Seasoning. Some pour these on livestocks before slaughter.'):
        "Un condimento. Si può usare (usa e getta).",

    # ---------------------------------------------------------- :65530 la lanterna di zucca
    (65530, 'It is food that can restore satiety, illuminates surroundings brightly.'):
        "Un cibo che sazia e che di notte illumina un po' i dintorni.",

    # ---------------------------------------------------------- :67324 il pranzo dell'abisso
    (67324, 'It is a bento blessed by abyssal powers, it restores your stamina.'):
        "Un pranzo protetto dall'acqua. Ridà anche vigore.",

    # ---------------------------------------------------------- :67795 romias
    (67795, 'It is food that can restore satiety. Are you sure you want to eat it?'):
        "Un cibo che sazia. Vuoi davvero mangiarlo?",

    # ---------------------------------------------------------- :67860 il caco
    (67860, 'It is fruit that can be cooked and eaten.'):
        "Un frutto che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :67923 la ghianda dorata
    (67923, 'These are nuts that can be eaten, but it cannot cooked.'):
        "Frutti a guscio che si mangiano, ma non si possono cucinare.",

    # ---------------------------------------------------------- :67986 la ghianda, la castagna
    (67986, 'These are nuts that can be cooked and eaten.'):
        "Frutti a guscio che si possono cucinare e mangiare.",

    # ---------------------------------------------------------- :68653 la crimberry
    (68653, 'It is food that can restore satiety. Contains harmful substances.'):
        "Un cibo che sazia. Contiene sostanze nocive.",

    # ---------------------------------------------------------- :74167 la carne proibita
    (74167, "One thing for sure, it's edible."):
        "Tutto sommato è un cibo.",

    # ---------------------------------------------------------- :74301 il pranzo del ringiovanimento
    # ⚠️ «bambino» vorrebbe il genere del giocatore, che non si conosce
    #    (guida-stile.md): si rende il fatto, non la persona.
    (74301, 'It is food that turns you into a child.'):
        "Un cibo che ti riporta all'infanzia.",

    # ---------------------------------------------------------- :74364 il pranzo dell'invecchiamento
    (74364, 'It is food that makes you old.'):
        "Un cibo che ti fa invecchiare.",

    # ---------------------------------------------------------- :76722 la polpetta di riso
    (76722, 'It is food that can restore satiety instantly.'):
        "Un cibo che sazia in un attimo.",

    # ---------------------------------------------------------- :78118 il putitoro
    (78118, 'It is food that can restore satiety. Has beauty benefits.'):
        "Un cibo che sazia. Fa bene anche alla bellezza.",

    # ---------------------------------------------------------- :80490 il mochi
    # ⭐ L'INGLESE HA PERSO LA SECONDA FRASE. Il giapponese e' identico a quello
    #    di :56937 — 「のどに詰まることがある。」 — e la gemella :80553 (il kagami
    #    mochi) l'inglese ce l'ha, «CHOKE WARNING». Qui l'italiano la rimette,
    #    e la resa e' la stessa delle altre tre.
    (80490, 'It is food that can restore satiety.'):
        "Un cibo che sazia. Certe volte va di traverso.",

    # ---------------------------------------------------------- :81672 il biscotto della fortuna
    (81672, 'It is food that can restore satiety, and it will tell you your fortune.'):
        "Un cibo che sazia. Dopo averlo mangiato, predice la sorte.",

    # ---------------------------------------------------------- :84103 la coda di coniglio
    (84103, 'It is food that brings luck when eaten.'):
        "Un cibo che alza la fortuna.",

    # ---------------------------------------------------------- :86469 il pranzo della sorella
    # ⚠️ il giapponese dice solo 「狂気度が減少する食物だ。」: la sazieta' la
    #    aggiunge l'inglese. 狂気度 e' «Follia» da command.hsp:10517.
    (86469, 'It is food that can restore satiety and lower insanity.'):
        "Un cibo che abbassa la follia.",

    # ---------------------------------------------------------- :86803 il frutto magico
    (86803, 'It is a fruit increase mana when eaten.'):
        "Un cibo che alza il mana.",

    # ---------------------------------------------------------- :87256 il formaggio dell'eroe
    (87256, 'It is food that can increase your life energy.'):
        "Un cibo che alza la vita.",

    # ---------------------------------------------------------- :88278 la mela della felicità
    (88278, "It is a magical fruit that increase one's luck greatly."):
        "Un cibo che alza molto la fortuna.",

    # ---------------------------------------------------------- :92588 l'uovo
    (92588, 'It is an egg that can be cooked and eaten.'):
        "Un uovo che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :92720 la carne secca
    (92720, 'It is a dried out meat that can restore satiety.'):
        "Della carne secca che sazia.",

    # ---------------------------------------------------------- :93893 il seme magico
    (93893, '(Single-use) edible seed that can be planted to grow magical plants.'):
        "Un seme che diventa un albero magico. Si usa (usa e getta).",

    # ---------------------------------------------------------- :93960 il seme di gemma
    (93960, '(Single-use) edible seed that can be planted to grow gems.'):
        "Un seme che diventa un albero di gemme. Si usa (usa e getta).",

    # ---------------------------------------------------------- :102524 la stomafillia
    (102524, 'It is a type of herb that can greatly restore satiety.'):
        "Un'erba che sazia molto.",

    # ---------------------------------------------------------- :102587 l'alraunia
    (102587, 'It is a type of herb that is good for your learning and charisma..'):
        "Un'erba che alza apprendimento e carisma.",

    # ---------------------------------------------------------- :102650 la curaria
    (102650, 'It is a type of herb that is good for your overall abilities.'):
        "Un'erba che alza un po' tutti gli attributi base.",

    # ---------------------------------------------------------- :102713 la spenseweed
    (102713, 'It is a type of herb that is good for your dexterity and perception.'):
        "Un'erba che alza destrezza e percezione.",

    # ---------------------------------------------------------- :102776 il mareilon
    (102776, 'It is a type of herb that is good for your magic and willpower..'):
        "Un'erba che alza magia e volontà.",

    # ---------------------------------------------------------- :102839 la morgia
    (102839, 'It is a type of herb that is good for your strength and constitution.'):
        "Un'erba che alza forza e costituzione.",

    # ---------------------------------------------------------- :102906 il seme di artefatto
    (102906, '(Single-use) edible seed that can be planted to grow artifacts.'):
        "Un seme che diventa un albero di artefatti. Si usa (usa e getta).",

    # ---------------------------------------------------------- :102973 il seme ignoto
    (102973, '(Single-use) edible seed that can be planted to grow a mysterious plant.'):
        "Un seme che diventa un albero misterioso. Si usa (usa e getta).",

    # ---------------------------------------------------------- :103040 il seme di erba
    (103040, '(Single-use) edible seed that can be planted to grow magical herbs.'):
        "Un seme che diventa un albero di erbe. Si usa (usa e getta).",

    # ---------------------------------------------------------- :103107 il seme di frutto
    (103107, '(Single-use) edible seed that can be planted to grow fruits.'):
        "Un seme che diventa un albero da frutto. Si usa (usa e getta).",

    # ---------------------------------------------------------- :103174 il seme di ortaggio
    (103174, '(Single-use) edible seed that can be planted to grow vegetables.'):
        "Un seme che diventa un albero di ortaggi. Si usa (usa e getta).",

    # ---------------------------------------------------------- :107676 il pesce sciabola
    # ⚠️ il giapponese e' la formula generica; l'anguilla la nomina solo l'inglese.
    (107676, 'It is seafood that looks something like an Eel.'):
        "Un cibo di mare che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :107749 il tonno
    (107749, 'It is a carnivorous fish that can be cooked and eaten.'):
        "Un cibo di mare che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :107895 il salmone
    (107895, 'It is a fish with unique spawning habits.'):
        "Un cibo di mare che si può cucinare e mangiare.",

    # ---------------------------------------------------------- :113815 il sacco di farina
    (113815, 'It is flour used for baking.'):
        "Un cibo che sazia e che si può cucinare.",

    # ---------------------------------------------------------- :113880 la pasta fresca
    (113880, 'It is food that would taste better cooked.'):
        "Un cibo che sazia e che si può cucinare.",

    # ---------------------------------------------------------- :113943 il filoncino
    # ⭐ l'inglese ha perso 「調理することができる。」, che il giapponese ha.
    (113943, 'It is food that can restore satiety.'):
        "Un cibo che sazia e che si può cucinare.",

    # ---------------------------------------------------------- :115655 la razione
    # ⭐⭐ QUI L'INGLESE DICE IL CONTRARIO DEL GIAPPONESE: 「調理することができる。」
    #    e' «si puo' cucinare», e l'inglese scrive «it cannot be cooked».
    (115655, 'It is food that restores satiety, it cannot be cooked.'):
        "Un cibo che sazia e che si può cucinare.",

    # ---------------------------------------------------------- :117602 il cadavere
    (117602, 'It is food that restores satiety, it can be cooked into meat dishes.'):
        "Un cibo che sazia e che si può cucinare.",
}
