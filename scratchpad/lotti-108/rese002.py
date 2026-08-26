import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :43903 l'energetico
    (43903, 'It is a beverage that restores satiety.'):
        "Una bevanda che sazia.",

    # ---------------------------------------------------------- :44445 la pozione dell'agonia
    (44445, 'It is a potion that causes a variety of undesired effects.'):
        "Una pozione che provoca stati alterati di ogni genere.",

    # ---------------------------------------------------------- :44516 la pozione della calamità
    (44516, 'It is a potion that causes a variety of debuffs.'):
        "Una pozione che provoca indebolimenti di ogni genere.",

    # ---------------------------------------------------------- :44587 la pozione del fisico
    (44587, 'It is a potion that improves physical performance.'):
        "Una pozione che migliora le doti fisiche.",

    # ---------------------------------------------------------- :49649 l'idromele dorato
    (49649, 'It is a beverage that gives spirit-out-of-body experience.'):
        "Una bevanda che fa uscire dal corpo.",

    # ---------------------------------------------------------- :53775 il disinfettante
    (53775, 'It is a gallon of disinfectant.'):
        "Un prodotto per disinfettare.",

    # ---------------------------------------------------------- :55347 la cola, l'orzata, il succo
    (55347, 'It is a beverage that restores satiety.'):
        "Una bevanda che sazia.",

    # ---------------------------------------------------------- :56133 l'annullatore d'incontri
    (56133, '(Single-use) usable potion.'):
        "Un oggetto che si può anche bere. Si usa (usa e getta).",

    # ---------------------------------------------------------- :56474 l'urina, il vomito
    (56474, 'It is something that is (questionably) drinkable.'):
        "Un oggetto che si può bere.",

    # ---------------------------------------------------------- :58852 la pozione della saggezza
    (58852, 'It is a potion that boosts all sorts of abilities.'):
        "Una pozione che migliora attributi di ogni genere.",

    # ---------------------------------------------------------- :58923 la pozione della gemma
    # ⚠️ «Una pozione che» non ci sta nei 69: le quattro composte aprono col verbo.
    (58923, 'It is a potion that boosts CON & CHA and resists paralysis & blindness.'):
        "Alza costituzione e carisma, e resiste a paralisi e cecità.",

    # ---------------------------------------------------------- :59388 il tè verde, il tè nero
    (59388, 'It is a tea beverage with health benefits.'):
        "Un tè che ha effetti curativi.",

    # ---------------------------------------------------------- :61655 la benzina
    (61655, 'It is volatile oil that gives off an odor.'):
        "Un olio volatile che manda cattivo odore.",

    # ---------------------------------------------------------- :61726 l'olio essenziale
    (61726, 'It is some plant-based volatile oil.'):
        "Un olio volatile di origine vegetale.",

    # ---------------------------------------------------------- :63387 i dolcetti della strega
    (63387, 'It is food that fully restore satiety. Some faint due to its strong kick.'):
        "Una bevanda che sazia. Rimette in sesto, ma fa svenire.",

    # ---------------------------------------------------------- :65674 la pozione della piuma
    (65674, 'It is a potion that temporarily raises DV and floats you.'):
        "Alza il DV per un po' e fa fluttuare.",

    # ---------------------------------------------------------- :65745 la pozione della concentrazione
    (65745, 'It is a potion that boosts PER & WIL and helps resist sleep & confusion.'):
        "Alza percezione e volontà, e resiste a sonno e confusione.",

    # ---------------------------------------------------------- :68524 il caffè
    (68524, 'It is a potion that can trick mild sleepiness.'):
        "Una pozione che inganna un po' di sonnolenza.",

    # ---------------------------------------------------------- :70068 l'antisettico
    (70068, 'It is a potion that keeps food from rotting.'):
        "Mescolata a un cibo, gli impedisce di marcire.",

    # ---------------------------------------------------------- :72000 la pozione soma
    (72000, 'It is a potion that restores stamina and and relieves drowsiness.'):
        "Una pozione che toglie fatica e sonnolenza.",

    # ---------------------------------------------------------- :72073 la pozione nektar
    (72073, 'It is a potion that greatly restores HP.'):
        "Una pozione che ridà molti HP.",

    # ---------------------------------------------------------- :72144 la pozione del disastro
    # ⚠️ stesso giapponese di :44445, e quindi la stessa resa: l'inglese le
    #    distingue («undesired effects» / «negative status effects») e il
    #    giapponese no.
    (72144, 'It is a potion that causes many negative status effects.'):
        "Una pozione che provoca stati alterati di ogni genere.",

    # ---------------------------------------------------------- :72215 l'aqua sanctio
    (72215, 'It is a powerful offensive potion.'):
        "Una pozione d'attacco, e potente.",

    # ---------------------------------------------------------- :74435 l'acceleratore
    (74435, 'It is a potion that restores speed potential.'):
        "Una pozione che ridà potenziale alla velocità.",

    # ---------------------------------------------------------- :77637 la Vernis originale
    (77637, 'It is a special candy that restores all sorts of things.'):
        "Una caramella speciale che ridà un po' di tutto.",

    # ---------------------------------------------------------- :79506 la capsula blu
    (79506, 'It is a drinkable capsule that restores your stamina.'):
        "Una capsula che toglie la fatica. Si può bere.",

    # ---------------------------------------------------------- :79577 la gassosa
    (79577, 'It is a drink that can restore stamina.'):
        "Una bevanda che toglie la fatica.",

    # ---------------------------------------------------------- :81814 il liquido ignifugo
    (81814, 'It is a potion that protect items from fire when blended.'):
        "Mescolata a una cosa, la protegge dal fuoco.",

    # ---------------------------------------------------------- :83485 la pozione dell'evoluzione
    (83485, 'It is a potion that causes advantageous mutations.'):
        "Una pozione che porta mutazioni utili.",

    # ---------------------------------------------------------- :83838 la pozione della discesa
    (83838, 'It is a potion that induces level-lowering effect.'):
        "Una pozione che abbassa il livello.",

    # ---------------------------------------------------------- :84370 la soluzione salina
    (84370, "It is a potion that's just salty."):
        "Una pozione che è soltanto salata.",

    # ---------------------------------------------------------- :89152 il sangue di Ermes
    (89152, 'It is a potion that permanently increases speed.'):
        "Una pozione che alza la velocità per sempre.",

    # ---------------------------------------------------------- :89564 il filtro d'amore
    # ⓘ 友好度 è «la simpatia», già fissata da chat.hsp:25511 e :14284.
    (89564, 'It is a potion that increases impression. You can blend it in food.'):
        "Alza la simpatia. Si può mescolare al cibo.",

    # ---------------------------------------------------------- :90772 la bottiglia vuota
    # ⚠️ il giapponese non dice «vuota»: dice che ci si può prendere l'acqua.
    (90772, 'It is a potion bottle that is completely empty.'):
        "Una bottiglia in cui si può prendere l'acqua.",

    # ---------------------------------------------------------- :91659 la manciata di neve
    (91659, 'These are things that, can be used to build a snowman.'):
        "Se se ne raccoglie tanta, ci si fa un pupazzo di neve.",

    # ---------------------------------------------------------- :92326 la molotov
    (92326, 'It is a liquid that creates walls of flame.'):
        "Un liquido che fa nascere muri di fiamme.",

    # ---------------------------------------------------------- :92525 il latte
    (92525, 'It is a drink that fills your stomach.'):
        "Una bevanda che riempie la pancia.",

    # ---------------------------------------------------------- :93072 il liquido antiacido
    (93072, 'It is a potion that protect items from acid when blended.'):
        "Mescolata a una cosa, la protegge dagli acidi.",

    # ---------------------------------------------------------- :93557 la cura della corruzione
    (93557, 'It is a valuable potion that can cure Ether Disease.'):
        "Una pozione preziosa che guarisce la malattia dell'etere.",

    # ---------------------------------------------------------- :96198 la tintura
    (96198, "It is a potion that colors things it's mixed with."):
        "Mescolata a una cosa, la colora.",

    # ---------------------------------------------------------- :96429 l'acqua
    (96429, 'It is a potion with no particular effect.'):
        "Una pozione senza nessun effetto particolare.",

    # ---------------------------------------------------------- :102111 la cura della mutazione
    (102111, "It is a potion that removes some of your body's mutations."):
        "Una pozione che toglie qualcuna delle mutazioni addosso.",

    # ---------------------------------------------------------- :102182 la pozione della mutazione
    (102182, 'It is a potion that causes your body to mutate.'):
        "Una pozione che fa mutare il corpo.",

    # ---------------------------------------------------------- :102395 la pozione che indebolisce le resistenze
    (102395, 'It is a potion that temporarily lowers resistances.'):
        "Una pozione che abbassa le resistenze per un po'.",

    # ---------------------------------------------------------- :104865 l'acido solforico
    (104865, 'It is a chemical for dissolving bodies.'):
        "Un liquido che scioglie la carne.",

    # ---------------------------------------------------------- :105599 la pozione della debolezza
    (105599, 'It is a potion that temporarily lowers PV.'):
        "Una pozione che abbassa il PV per un po'.",

    # ---------------------------------------------------------- :105816 la pozione dell'eroe
    (105816, 'It is a potion that boosts STR & DEX and helps resist fear and confusion.'):
        "Alza forza e destrezza, e resiste a terrore e confusione.",

    # ---------------------------------------------------------- :106040 la pozione della lentezza
    (106040, 'It is a potion that temporarily slows you.'):
        "Una pozione che rallenta per un po'.",

    # ---------------------------------------------------------- :106111 la pozione della velocità
    (106111, 'It is a potion that temporarily speeds you up.'):
        "Una pozione che accelera per un po'.",

    # ---------------------------------------------------------- :106328 la pozione della resistenza
    (106328, 'It is a potion that temporarily confers resistance to all elements.'):
        "Dà per un po' resistenza agli elementi.",

    # ---------------------------------------------------------- :106472 il sangue di troll
    (106472, 'It is a potion that temporarily enhances natural regeneration.'):
        "Una pozione che alza per un po' la guarigione.",

    # ---------------------------------------------------------- :106616 la pozione del silenzio
    (106616, 'It is a potion that induces silence.'):
        "Una pozione che porta il silenzio.",

    # ---------------------------------------------------------- :106913 la pozione del difensore
    (106913, 'It is a potion that temporarily boosts PV and helps resist fear.'):
        "Alza il PV per un po' e resiste al terrore.",

    # ---------------------------------------------------------- :111995 la pozione del potenziale
    (111995, 'It is a potion that raises the potential of one attribute.'):
        "Alza il potenziale di uno degli attributi base.",

    # ---------------------------------------------------------- :112066 il ristoro dello spirito
    (112066, 'It is a potion that restores mental attributes.'):
        "Una pozione che ripara gli attributi mentali calati.",

    # ---------------------------------------------------------- :112137 il ristoro del corpo
    (112137, 'It is a potion that restores physical attributes.'):
        "Una pozione che ripara gli attributi fisici calati.",

    # ---------------------------------------------------------- :113679 il veleno
    (113679, 'It is poison. You can mix it in food.'):
        "Provoca l'avvelenamento. Si può mescolare al cibo.",

    # ---------------------------------------------------------- :114280 la birra, il whisky, la Crim ale
    (114280, 'It is a beverage that gets you drunk.'):
        "Una bevanda che ubriaca.",

    # ---------------------------------------------------------- :126010 la pozione di Jure
    # ⚠️ stesso giapponese di :126081, e l'inglese aggiunge «all» solo qui.
    (126010, 'It is a potion that restores HP and cures all status effects.'):
        "Una pozione che ridà HP e cura gli stati alterati.",

    # ---------------------------------------------------------- :126081 le altre sei pozioni di cura
    (126081, 'It is a potion that restores HP and cures status effects.'):
        "Una pozione che ridà HP e cura gli stati alterati.",

    # ---------------------------------------------------------- :129159 il sonnifero
    (129159, 'It is a potion that induces sleep.'):
        "Una pozione che fa addormentare.",

    # ---------------------------------------------------------- :129230 la pozione della paralisi
    (129230, 'It is a potion that induces paralysis.'):
        "Una pozione che paralizza.",

    # ---------------------------------------------------------- :129301 la pozione della confusione
    (129301, 'It is a potion that induces confusion.'):
        "Una pozione che confonde.",

    # ---------------------------------------------------------- :129372 la pozione della cecità
    (129372, 'It is a potion that induces blindness.'):
        "Una pozione che acceca.",

    # ---------------------------------------------------------- :129442 l'acqua sporca
    # ⚠️ il giapponese dice «può far ammalare», l'inglese lo dà per certo.
    (129442, 'It is a potion that induces sickness.'):
        "Una pozione che può far ammalare.",
}
