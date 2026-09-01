import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :61581
    (61581, "Giant belt buckle with an ego. It emits a light that temporarily transforms one's signature attribute. It is studded with gemstones that resemble eyes, each of which represents a different attribute. Its main body is also in the shape of a giant eye, but it seems that this design was created by chance during the course of its creation. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una cintura con una fibbia enorme. Manda una luce che cambia per un po' l'attributo in cui si è forti. È cosparsa di gemme fatte a somiglianza di occhi, e ognuna governa un attributo diverso. Anche il corpo della fibbia ha la forma di un occhio gigante, ma pare sia venuto così per caso, mentre la costruivano senza pensarci troppo. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :64276
    (64276, "This broom was given the ability to fly by Nein. Although it was originally intended to be ridden astride, it is safer to ride it sitting sideways because one's crotch might split open when it soars. It is capable of flying at the speed of sound due to its high specifications, but if it is actually used, the passenger will surely be swept off. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una scopa a cui <Nein> ha dato la facoltà di volare. All'inizio la si pensava da cavalcare a gambe larghe, ma siccome in salita improvvisa c'è il rischio di spaccarsi l'inguine conviene sedercisi sopra di traverso. Ha caratteristiche inutilmente spinte e arriva alla velocità del suono, ma a provarci davvero chi ci sta sopra viene sbalzato giù di sicuro. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :64343
    (64343, 'It was made by sewing tiger fur using magical threads extracted from the souls of mages. They are famous for their toughness and do not tear or stink even after 100 years of wear. Because they are easy to move in, they are used as sportswear, and there are even brand-name products made of white tiger fur. They are pants, but more like hot pants, so there is no need to be embarrassed when people see them. Put them on, yes, right now! \\n# ~Irva Fantasy Encyclopedia~'):
        "Fatte cucendo pelliccia di tigre con un filo magico estratto dall'anima dei maghi. Sono famose per la tenacia, e infatti a portarle cent'anni non si strappano e non prendono odore. Siccome lasciano muoversi bene si usano come abbigliamento sportivo, e ne esiste anche una versione di marca fatta con la pelliccia di tigre bianca. Mutande sì, ma nel senso di pantaloncini, quindi non c'è da vergognarsi se qualcuno le vede. Mettiamocele tutti. E mettiamocele, invece di tirarle. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :68112
    (68112, 'Belt studded with an imitation of the Lesimas Magic Stone. The original magic stone had the power to seal Lesimas, and a plan was proposed to apply it to create a defensive facility to protect Palmia. With the cooperation of adventurers from Eulderna, an imitation was produced, but the plan was abandoned because some of the strength could not be reproduced. Only a prototype of armor that temporarily covered only the bearer with a magical wall was produced. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una cintura cosparsa di imitazioni di pietre magiche. Le pietre magiche originali nascondevano una forza legata al sigillo di Lesimas, e da lì era nato il piano di costruire un impianto difensivo per proteggere Palmia. Con l'aiuto di un avventuriero venuto da Eulderna le imitazioni si riuscirono a produrre, ma una parte della forza non fu riproducibile e il piano si arenò. Di tutto rimase soltanto un prototipo: un'armatura che copre per un momento il solo portatore con un muro magico. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :76049
    (76049, 'Something the God of the Harvest uses to keep his precious objects from escaping. If you are not careful, it will wrap around you like a belt on its own. \\n# ~Irva Fantasy Encyclopedia~'):
        "Quello che il dio del raccolto adopera perché le cose a cui tiene non gli scappino. A distrarsi un attimo, si avvolge addosso da sé come una cintura. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :82342
    (82342, "Waistband made of ancient metals joined together in a scaly pattern. It is coated with a special red chemical that is said to protect the wearer's body and possessions. \\n# ~Irva Fantasy Encyclopedia~"):
        "Una cintura fatta di metallo antico unito a scaglie. Ci è passata sopra una sostanza rossa particolare, e dicono che protegga il corpo di chi la indossa e le cose che porta con sé. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :100327
    (100327, 'A waist support with increased protection by layering. In addition to the increased weight, the overlapping parts collide with each other, which has the adverse effect of creating noise. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Una cintura che alza la protezione sovrapponendo strato su strato. Oltre a pesare di più, ha la controindicazione che i pezzi sovrapposti sbattono l'uno contro l'altro e fanno rumore. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :100392
    (100392, "A waist brace made of a combination of special materials to provide stronger protection. It is lighter than the usual one, perhaps as a result of the material's advantages. \\n# ~Collection of Armaments you can Use Tomorrow~"):
        "Una cintura che, incrociando materiali speciali, ha ottenuto una protezione più solida. Forse perché ne hanno spinto i pregi, è venuta più leggera del solito. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

    # ---------------------------------------------------------- :126712
    (126712, 'Protective gear designed to protect the lower half of the body while not impeding action. In cold weather, some elderly women wear these due to their lightweight material. \\n# ~Collection of Armaments you can Use Tomorrow~'):
        "Un'armatura pensata per proteggere la parte bassa del corpo senza intralciare i movimenti. Pare che nella stagione fredda certe signore ne portino una fatta di materiale leggero. \\n# ~Raccolta di Armi e Armature da Usare Domani~",

# 9 voci, 0 ambigue
}
