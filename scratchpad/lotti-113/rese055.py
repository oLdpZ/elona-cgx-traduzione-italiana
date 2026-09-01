import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :48805
    (48805, 'Artfully processed garnet, this gemstone represents the month of January and would make a particularly nice gift for someone whose anniversary is in January. \\n#~Vernis Ore Catalogue~'):
        "Un granato lavorato ad arte. È la pietra che rappresenta gennaio, e regalarla a chi ha una ricorrenza in gennaio farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :48875
    (48875, 'Artfully processed amethyst, this gemstone represents the month of Febuary and would make a particularly nice gift for someone whose anniversary is in Febuary. \\n#~Vernis Ore Catalogue~'):
        "Un'ametista lavorata ad arte. È la pietra che rappresenta febbraio, e regalarla a chi ha una ricorrenza in febbraio farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :48945
    (48945, 'Artfully processed aquamarine, this gemstone represents the month of March and would make a particularly nice gift for someone whose anniversary is in March. \\n#~Vernis Ore Catalogue~'):
        "Un'acquamarina lavorata ad arte. È la pietra che rappresenta marzo, e regalarla a chi ha una ricorrenza in marzo farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49015
    (49015, 'Artfully processed diamond, this gemstone represents the month of April and would make a particularly nice gift for someone whose anniversary is in April. \\n#~Vernis Ore Catalogue~'):
        "Un diamante lavorato ad arte. È la pietra che rappresenta aprile, e regalarlo a chi ha una ricorrenza in aprile farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49085
    (49085, 'Artfully processed emerald, this gemstone represents the month of May and would make a particularly nice gift for someone whose anniversary is in May. \\n#~Vernis Ore Catalogue~'):
        "Uno smeraldo lavorato ad arte. È la pietra che rappresenta maggio, e regalarlo a chi ha una ricorrenza in maggio farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49155
    (49155, 'Artfully processed Alexandrite, this gemstone represents the month of June and would make a particularly nice gift for someone whose anniversary is in June. \\n#~Vernis Ore Catalogue~'):
        "Un crisoberillo lavorato ad arte. È la pietra che rappresenta giugno, e regalarlo a chi ha una ricorrenza in giugno farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49225
    (49225, 'Artfully processed ruby, this gemstone represents the month of July and would make a particularly nice gift for someone whose anniversary is in July. \\n#~Vernis Ore Catalogue~'):
        "Un rubino lavorato ad arte. È la pietra che rappresenta luglio, e regalarlo a chi ha una ricorrenza in luglio farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49295
    (49295, 'Artfully processed sardonyx, this gemstone represents the month of August and would make a particularly nice gift for someone whose anniversary is in August. \\n#~Vernis Ore Catalogue~'):
        "Un'agata lavorata ad arte. È la pietra che rappresenta agosto, e regalarla a chi ha una ricorrenza in agosto farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49365
    (49365, 'Artfully processed sapphire, this gemstone represents the month of September and would make a particularly nice gift for someone whose anniversary is in September. \\n#~Vernis Ore Catalogue~'):
        "Uno zaffiro lavorato ad arte. È la pietra che rappresenta settembre, e regalarlo a chi ha una ricorrenza in settembre farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49435
    (49435, 'Artfully processed opal, this gemstone represents the month of October and would make a particularly nice gift for someone whose anniversary is in October. \\n#~Vernis Ore Catalogue~'):
        "Un opale lavorato ad arte. È la pietra che rappresenta ottobre, e regalarlo a chi ha una ricorrenza in ottobre farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49505
    (49505, 'Artfully processed topaz, this gemstone represents the month of November and would make a particularly nice gift for someone whose anniversary is in November. \\n#~Vernis Ore Catalogue~'):
        "Un topazio lavorato ad arte. È la pietra che rappresenta novembre, e regalarlo a chi ha una ricorrenza in novembre farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49575
    (49575, 'Artfully processed lapis lazuli, this gemstone represents the month of December and would make a particularly nice gift for someone whose anniversary is in December. \\n#~Vernis Ore Catalogue~'):
        "Un lapislazzuli lavorato ad arte. È la pietra che rappresenta dicembre, e regalarlo a chi ha una ricorrenza in dicembre farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49708
    (49708, 'Golden statue. It is a very realistic sculpture, as if the real thing were turned directly into gold. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che luccica d'oro. È modellata in modo straordinariamente vivo, come se una persona vera fosse stata mutata in oro così com'era. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :52170
    (52170, 'Beautiful skeleton formed by coralline worms. It is calcareous and hard, but can be eaten up or swallowed whole by stronger fish. \\n# ~Lumiest Art Catalogue~'):
        "Il bello scheletro che formano i polipi del corallo. È calcareo e duro, eppure i pesci robusti se lo sgranocchiano o se lo inghiottono intero. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :52313
    (52313, 'Reddish in color, this ore is softer than iron as it is, but once heated and processed, it turns silver in color and becomes remarkably hard. \\n#~Vernis Ore Catalogue~'):
        "Questo minerale, che tende al rosso, così com'è è più tenero del ferro; ma una volta scaldato e lavorato il colore vira all'argento e diventa duro da stupire. \\n#~Atlante dei Minerali di Zaile~",

    # ---------------------------------------------------------- :66137
    (66137, 'Teardrop-shaped jewel crystallized from a drop of divine power. It has the same kind of power as an artifact, albeit in a smaller quantity. It appears unexpectedly when the power of the gods is temporarily increased, and it is said to be difficult to produce it when you want it to appear. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una gemma a forma di goccia, nata dal cristallizzarsi di una stilla di forza divina. Per quanto poca, dentro nasconde la stessa forza di un artefatto. Viene fuori così, senza preavviso, quando la forza di un dio cresce per un momento; e al contrario, volerla far uscire pare sia difficile. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :66199
    (66199, 'Fragments of divine power, the core of Nefia that forms the labyrinth and empowers its guardians. Almost all of its hidden power has already been used, and it is virtually a husk. However, since there is usually nothing left over after the birth of Nefia, it has a high scarcity value. It is traded at a high price, partly because the residue of divine power remains in the form of enchantments. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un frammento di forza divina, e insieme il nucleo che forma il labirinto e dà potere ai suoi guardiani. La forza che vi era nascosta è stata ormai spesa quasi tutta, e di fatto è un residuo. Ma siccome di norma dopo la nascita di una Nefia non ne resta nessuno, è raro e per questo prezioso. Si scambia a caro prezzo anche perché quel che avanza della forza divina resta lì sotto forma di incantamento. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :69048
    (69048, 'Large rubynus are cut from collected gemstones that have been fused together through alchemy. Even though each rough stone is not worth polishing, if they are gathered together and polished, they will shine as splendid gems. \\n#~Vernis Ore Catalogue~'):
        "Un rubynus di gran misura, tagliato dopo aver fuso con l'alchimia i grezzi messi insieme. Anche se preso uno per uno nessuno di quei grezzi varrebbe la fatica di lucidarlo, a raccoglierli e lavorarli l'uno con l'altro ne esce una gemma di tutto rispetto, che brilla. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :69118
    (69118, 'Large emerald are cut from collected gemstones that have been fused together through alchemy. Even though each rough stone is not worth polishing, if they are gathered together and polished, they will shine as splendid gems. \\n#~Vernis Ore Catalogue~'):
        "Un'iscrizione su smeraldo, dove è riportato il pensiero fondamentale dell'alchimia. È roba per chi va matto per l'alchimia, ma vale molto anche come opera d'arte. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :69188
    (69188, 'Large diamond are cut from collected gemstones that have been fused together through alchemy. Even though each rough stone is not worth polishing, if they are gathered together and polished, they will shine as splendid gems. \\n#~Vernis Ore Catalogue~'):
        "Un diamante di gran misura, tagliato dopo aver fuso con l'alchimia i grezzi messi insieme. Per grandezza e per bellezza è perfetto, e gli si dà un prezzo che supera perfino quello di un artefatto. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :82213
    (82213, "A priceless piece of paper. It has the word 'friendship' crudely written on it. \\n#~Thousands of pieces of Junk I love~"):
        "Un pezzo di carta che si dice valga più di quanto il denaro possa comprare. Sopra c'è scritto \\\"amicizia\\\", con una grafia che pare il tracciato di un lombrico. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :82610
    (82610, "Mystery ticket with several instruments drawn on it. It contains the performer's dream and the audience's appreciation. \\n# ~Music of the Melodious Irva~"):
        "Un biglietto misterioso, con disegnati sopra alcuni strumenti. Dentro ci stanno il sogno di chi suona e la riconoscenza di chi ascolta. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :89419
    (89419, 'A small coin believed to have been used in ancient times. They are not in circulation because they have only academic value, but many collectors are said to have especially collected them because of their rarity. \\n# ~Coins of this World - Tyris Edition~'):
        "Una monetina che si dice fosse in uso nell'antichità. Non circola più, perché ha ormai solo un valore di studio, ma pare che proprio per quanto è rara siano in molti i collezionisti che se ne occupano. \\n# ~Le Monete del Mondo: Tyris~",

    # ---------------------------------------------------------- :117318
    (117318, "It is a sinful mineral that, when appraised, leaves one in dismay. It shines so brightly that it seems almost deliberate, and is given mainly to children or to those who don't understand its value, as a token of appreciation. \\n#~Cheap Gifts for Your Kids~"):
        "Un minerale che fa peccato: a farlo esaminare non si può che restarci male. Brilla in un modo così plateale da parere apposta, e lo si regala soprattutto ai bambini, o a chi non ne capisce il valore, per dire grazie. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :128173
    (128173, 'Stones that have no scarcity value. There are plenty of them lying around, but it seems that many children collect them. \\n#~Cheap Gifts for Your Kids~'):
        "Un pezzo di pietra che di raro non ha proprio niente. Ce n'è quante se ne vuole in giro, eppure pare che di bambini che le raccolgono ce ne siano parecchi. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :128305
    (128305, 'A rare mineral that contains many elements of diamond. Through the process of processing, its size becomes extremely small, so it is not considered to be so valuable in relation to the size of the gemstone. \\n#~Vernis Ore Catalogue~'):
        "Un minerale raro, che contiene molto degli elementi del diamante. Nella lavorazione la sua misura si riduce all'estremo, e per questo si dice che non valga poi molto rispetto a quanto è grosso da grezzo. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128375
    (128375, 'A rare mineral that contains many elements of emerald. Through the process of processing, its size becomes extremely small, so it is not considered to be so valuable in relation to the size of the gemstone. \\n#~Vernis Ore Catalogue~'):
        "Un minerale raro, che contiene molto degli elementi dello smeraldo. Nella lavorazione la sua misura si riduce all'estremo, e per questo si dice che non valga poi molto rispetto a quanto è grosso da grezzo. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128445
    (128445, 'Small white minerals that emit a pale light. It is so beautiful that it is described as a pearl of stone, as it slowly builds up an almost elliptical sphere over time. \\n#~Vernis Ore Catalogue~'):
        "Un minerale piccolo e bianco, che manda una luce tenue. Attraverso ere e ere costruisce con calma una sfera quasi ovale, e a vederlo così è tanto bello che lo chiamano la perla di pietra. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128515
    (128515, 'A rare mineral that contains many elements of rubynus. Through the process of processing, its size becomes extremely small, so it is not considered to be so valuable in relation to the size of the gemstone. \\n#~Vernis Ore Catalogue~'):
        "Un minerale raro, che contiene molto degli elementi del rubynus. Nella lavorazione la sua misura si riduce all'estremo, e per questo si dice che non valga poi molto rispetto a quanto è grosso da grezzo. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128585
    (128585, 'A brilliant mineral that never rusts. It is very easy to process, and its unique bright color has been favored by powerful people as a symbol of wealth and power since ancient times. Because of its mysterious nature, it is often the subject of research. \\n#~Vernis Ore Catalogue~'):
        "Un minerale splendente, che non arrugginisce mai. È facilissimo da lavorare, e quel suo colore chiaro e inconfondibile è caro fin dall'antichità a chi ha il potere, come segno di ricchezza e di forza. Pare che per quel suo che di misterioso finisca spesso sotto studio. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128655
    (128655, 'This yellow crystal is said to contain the power of the sun. When you look through the light, you can see a faint atmospheric undulation-like movement in the mineral. \\n#~Vernis Ore Catalogue~'):
        "Un cristallo giallo, che si dice racchiuda la forza del sole. Guardandolo in controluce, dentro il minerale si scorge appena un movimento come di aria che ondeggia. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128725
    (128725, 'A red crystal that is said to contain magical power. The mineral itself is as transparent as pure magic power. It is said that in an emergency, a mage would crush it and put it in his body. \\n#~Vernis Ore Catalogue~'):
        "Un cristallo rosso, che si dice racchiuda la forza magica. Il minerale in sé è trasparente quanto il mana puro. Si racconta che nei momenti critici i maghi lo frantumino per accoglierlo nel proprio corpo. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128795
    (128795, 'This orange crystal is said to contain the power of the earth. When you look through the light, the reflection from the many cracks inside the crystal is very beautiful. \\n#~Vernis Ore Catalogue~'):
        "Un cristallo arancione, che si dice racchiuda la forza della terra. Guardandolo in controluce, la luce si riflette sulle molte crepe che lo percorrono dentro, ed è bellissimo. \\n#~Atlante dei Minerali di Vernis~",

# 33 voci, 0 ambigue
}
