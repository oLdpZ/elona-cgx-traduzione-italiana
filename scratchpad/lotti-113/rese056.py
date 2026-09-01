import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :61946
    (61946, 'Rods encasing specific magic, an ephemeral, yet fragile looking gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma fragile, che pare stia per rompersi da un momento all'altro.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :62314
    (62314, 'Rods encasing specific magic, an translucent, shining gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma traslucida che brilla.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :62394
    (62394, 'Rods encasing specific magic, a poison-tainted gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma di un colore che sa di veleno.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :70751
    (70751, 'Rods encasing specific magic, a shiny, glittering gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma che manda scintille crepitando.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :71856
    (71856, 'Rods encasing specific magic, a black and murky gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma nera e torbida.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :92062
    (92062, 'Rods encasing specific magic, an opaque white spherical gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma bianca e opaca, a forma di sfera.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :92797
    (92797, 'Rods encasing specific magic, an transparent gem, with a hint of red taint, is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma trasparente, con dentro mescolato del rosso.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :93149
    (93149, 'Rods encasing specific magic, not jeweled, just a long, thin rod with a pointed end. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Di gemme non ne ha, e pare un'asta lunga e sottile con la punta aguzza. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :94102
    (94102, 'Rods encasing specific magic, carved with a pattern resembling intertwined ivy. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un motivo come di edera intrecciata. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :94534
    (94534, 'Rods encasing specific magic, mineralized shiny gemstones are attached to it. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma che luccica come un minerale. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :96275
    (96275, 'Rods encasing specific magic, a Uroboros is carved on it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un drago che si tiene in bocca la propria coda.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :96355
    (96355, 'Rods encasing specific magic, sacred geometric patterns are carved into it. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci stanno incisi sopra motivi di geometria sacra. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :98576
    (98576, 'Rods encasing specific magic, not jeweled, latticed pattern is engraved on it. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Sull'asta è intagliato un motivo a graticcio. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :98954
    (98954, "Rods encasing specific magic, a huge purple gem like a creature's eye is attached to it.\\n# ~Arcane Almanac~"):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma viola enorme, come l'occhio di un essere vivo.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :103505
    (103505, 'Rods encasing specific magic, carved with fine letter-like patterns.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un motivo come di caratteri minuti.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :104942
    (104942, 'Rods encasing specific magic, an octahedron shaped crimson gemstone is attached. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma rosso sangue, tagliata a otto facce. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :105381
    (105381, 'Rods encasing specific magic, a cold blue gemstone is mounted on it. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma azzurra che dà una sensazione di freddo. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :105966
    (105966, 'Rods encasing specific magic, an opaque, blue gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma azzurra e opaca.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :106766
    (106766, 'Rods encasing specific magic, a black, murky gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma nera e torbida.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :111777
    (111777, 'Rods encasing specific magic, a cat-eye-shaped gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta preziosa, in cui è chiusa una magia precisa. Ci sta montata sopra una gemma come un occhio di gatto.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :117679
    (117679, 'Rods encasing specific magic, three small red jewels are attached.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci stanno montate sopra tre piccole gemme rosse.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :117759
    (117759, 'Rods encasing specific magic, carved with spiral-like patterns.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un motivo a spirale.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :119541
    (119541, 'Rods encasing specific magic, an opaque, red gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma rossa e opaca.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :119621
    (119621, 'Rods encasing specific magic, an translucent, yellow gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma gialla e traslucida.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :122821
    (122821, 'Rods encasing specific magic, carved with intertwined serpent-like patterns. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta inciso sopra un motivo come di serpenti intrecciati. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :122964
    (122964, 'Rods encasing specific magic, an translucent, red gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma rossa e traslucida.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :123044
    (123044, 'Rods encasing specific magic, an translucent, blue gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma azzurra e traslucida.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :123124
    (123124, 'Rods encasing specific magic, a sphere made from some kind of bone is attached to it. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una sfera ricavata dall'osso di qualcosa. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :123204
    (123204, 'Rods encasing specific magic, an translucent, white gem is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma bianca e traslucida.\\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :123284
    (123284, 'Rods encasing specific magic, spherical small red gemstone is attached. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una piccola gemma rossa a forma di sfera. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :129950
    (129950, 'Rods encasing specific magic, a green gemstone with clear quadrangulars is attached. \\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma verde e trasparente, squadrata. \\n# ~Compendio Completo degli Oggetti Magici~",

    # ---------------------------------------------------------- :130030
    (130030, 'Rods encasing specific magic, a crystal clear gemstone is attached to it.\\n# ~Arcane Almanac~'):
        "Una bacchetta in cui è chiusa una magia precisa. Ci sta montata sopra una gemma trasparente, che pare veda attraverso ogni cosa.\\n# ~Compendio Completo degli Oggetti Magici~",

# 32 voci, 0 ambigue
}
