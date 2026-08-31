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
