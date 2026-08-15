import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :6248 la riga che apre la consegna. ⚠️ `name(tc)` e' contenuto e resta,
    #     `he(tc)` e' morfologia e sparisce; «raccolti» concorda con «materiali».
    (6248, ' handed over the materials  has gathered during your adventures.'):
        'name(tc) + " ti consegna i materiali raccolti durante il viaggio."',

    # --- :6289-:6305 le pietre.
    (6289, 'You get  Pebble.'):
        '"Materiale ricevuto: pietruzza (" + m1 + ")."',
    (6293, 'You get  Fine stone.'):
        '"Materiale ricevuto: pietra pregiata (" + m2 + ")."',
    (6297, 'You get  Ether fragment.'):
        '"Materiale ricevuto: scheggia di etere (" + m3 + ")."',
    # ⚠️ 「風切石」 e' «pietra del vento», ma la costante e' ELEMENT_FRAGMENT e le
    #    schegge sono una famiglia: qui la coerenza batte il giapponese
    (6301, 'You get  Element fragment.'):
        '"Materiale ricevuto: scheggia elementale (" + m4 + ")."',
    (6305, 'You get  Chaos stone.'):
        '"Materiale ricevuto: pietra del caos (" + m5 + ")."',

    # --- :6349-:6365 l'acqua.
    (6349, 'You get  Waterdrop.'):
        '"Materiale ricevuto: goccia d\'acqua (" + m1 + ")."',
    (6353, 'You get  Hot water.'):
        '"Materiale ricevuto: acqua calda (" + m2 + ")."',
    (6357, 'You get  Snow.'):
        '"Materiale ricevuto: neve (" + m3 + ")."',
    (6361, "You get  Witch's tear."):
        '"Materiale ricevuto: lacrima di strega (" + m4 + ")."',
    (6365, "You get  Angel's tear."):
        '"Materiale ricevuto: lacrima d\'angelo (" + m5 + ")."',

    # --- :6407-:6423 il bosco.
    (6407, 'You get  Stick.'):
        '"Materiale ricevuto: bastone (" + m1 + ")."',
    (6411, 'You get  Branch.'):
        '"Materiale ricevuto: ramo (" + m2 + ")."',
    (6415, 'You get  Holy weed.'):
        '"Materiale ricevuto: erba sacra (" + m3 + ")."',
    (6419, 'You get  Shining weed.'):
        '"Materiale ricevuto: erba lucente (" + m4 + ")."',
    # ⚠️ nome proprio del canone Elona, con la sua storpiatura: non «Yggdrasil»
    (6423, 'You get  Sap of Yaggdrasil.'):
        '"Materiale ricevuto: linfa di Yaggdrasil (" + m5 + ")."',

    # --- :6465-:6481 la carne e la magia.
    (6465, 'You get  Human gene.'):
        '"Materiale ricevuto: gene umano (" + m1 + ")."',
    (6469, 'You get  Troll gene.'):
        '"Materiale ricevuto: gene di troll (" + m2 + ")."',
    (6473, "You get  Rabbit's tail."):
        '"Materiale ricevuto: coda di coniglio (" + m3 + ")."',
    (6477, "You get  Witch's eye."):
        '"Materiale ricevuto: occhio di strega (" + m4 + ")."',
    (6481, 'You get  Fairy dust.'):
        '"Materiale ricevuto: polvere di fata (" + m5 + ")."',

    # --- :6533-:6557 la bottega. ⚠️ 「わめく狂人」 e' un MATERIALE che si chiama
    #     cosi', non una persona.
    (6533, 'You get  Cloth.'):
        '"Materiale ricevuto: pezza di stoffa (" + m1 + ")."',
    (6537, 'You get  Paper.'):
        '"Materiale ricevuto: carta (" + m2 + ")."',
    (6541, 'You get  Yelling madman.'):
        '"Materiale ricevuto: pazzo urlante (" + m3 + ")."',
    # ⭐ copiata: action.hsp:12351 rende gia' 「魔法のインク」 «inchiostro magico»
    (6545, 'You get  Magic ink.'):
        '"Materiale ricevuto: inchiostro magico (" + m4 + ")."',
    (6549, 'You get  Magic mass.'):
        '"Materiale ricevuto: massa magica (" + m5 + ")."',
    (6553, 'You get  Generator.'):
        '"Materiale ricevuto: macchina generatrice (" + m6 + ")."',
    (6557, 'You get  Electricity.'):
        '"Materiale ricevuto: elettricità (" + m7 + ")."',
}
