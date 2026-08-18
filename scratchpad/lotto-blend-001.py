# -*- coding: utf-8 -*-
"""Il lotto di `blend.hsp`: il sistema delle ricette (調合).

`blend.hsp` era il file **mezzo tradotto**: una toppa e nessun dizionario,
quindi 183 `lang()` che nessun conteggio guardava — la forma dei «mezzi fatti»
della 55a. Aprirlo lo fa entrare in `verifica --dizionario`.

## La geometria, misurata prima di scrivere

**La lista delle ricette** (`blend.hsp:1304`, `cs_list`): il nome comincia a
`wx + 88` e le icone di difficolta' e di spunta stanno a `wx + 317`. Sono 229 px
a 7 px per carattere = **32 caratteri**, prefisso compreso. ⚠️ `cs_list` **non
taglia** (`module.hsp:70` usa `strlen * 7 + 32` solo per la barra di selezione,
limitata a 480): il nome lungo si sovrappone alle icone. Upstream ne sfora gia'
**2 su 72** («Recipe of Meat-filling resuscitation», 36).

La riga della lista e' `lang("", "Recipe of ") + cnven(rpname) + lang("のレシピ", "")`:
il prefisso e' reso **«Ricetta: »** (9), quindi ai nomi restano **23 caratteri**.
⚠️ Renderlo vuoto non si puo': `verifica.py:275` rifiuta la traduzione vuota, e
l'unica deroga passa da `invariati.md`, che vuol dire un'altra cosa.

**La riga dei materiali** (`blend.hsp:469`) e' tagliata da un `strmid(..., 0, 44)`
vero e proprio, ed e' composta come «Aggiungi X (Scorta:N)».

## Il vocabolario

Il comando del gioco e' gia' **«Mescola»** (`text.hsp:135`, 調合 / `Mix`), quindi
tutto il file gira intorno a quel verbo. `putitoro` sta in `invariati.md`.

I tre `武具` di Elona+ — 柔 / 剛 / 鋭 — diventano **armatura molle / armatura
rigida / arma affilata**, e i sei nomi di ricetta che li usano seguono la stessa
coppia di verbi: «rifare» per 改修, «creare» per 作成.

## Il metodo

Le voci il cui giapponese e' gia' reso altrove **si riprendono da li'**, non si
riscrivono: 35 su 175, e sono quasi tutte le battute del pozzo e della pittura.
E' la domanda della 29a fatta in automatico.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LOTTO = 'lavoro/_blend.jsonl'

# (riga, inglese) -> italiano. L'inglese e' nella chiave perche' su una riga
# possono stare due `lang()` (`:381` porta " and " e " hours").
RESE = {
    # --- l'indicatore di riuscita, blend.hsp:45-71 ---------------------
    (23, ' corpse'): ' (cadavere)',
    (45, 'Perfect!'): 'Perfetto!',
    (48, 'A piece of cake!'): 'Uno scherzo!',
    (51, 'Very likely'): 'Facilissimo',
    (54, 'No problem'): 'Nessun problema',
    (57, 'Probably OK'): 'Dovrebbe andare',
    (60, 'Maybe'): 'Forse',
    (63, 'Bad'): 'Male',
    (66, 'Very bad'): 'Malissimo',
    (69, 'Almost impossible'): 'Quasi impossibile',
    (71, 'Impossible!'): 'Impossibile!',
    (94, 'The success rate goes up.'): 'Le probabilità di riuscita salgono.',
    (99, 'The success rate goes down.'): 'Le probabilità di riuscita scendono.',
    # --- il riquadro della ricetta -------------------------------------
    (368, 'Success Rate : '): 'Riuscita : ',
    (379, ' turns'): ' turni',
    (381, ' and '): ' e ',
    (381, ' hours'): ' ore',
    (385, 'Time: '): 'Tempo: ',
    (404, '[Page]  '): '[Pagina]  ',
    (424, 'Blending Procedure'): 'Procedimento',
    (441, 'Choose a recipe'): 'Scegli una ricetta',
    (466, 'Stock:'): 'Scorta:',
    (469, 'Selected '): 'Scelto ',
    (490, 'Start blending!'): 'Comincia a mescolare!',
    (499, 'Required Skills:'): 'Abilità richieste:',
    (520, 'Required equipment:'): 'Attrezzi richiesti:',
    (538, 'Attention: Up to 9999 gold coins can be exchanged at a time.'):
        'Attenzione: si possono scambiare al massimo 9999 monete alla volta.',
    (543, "You haven't identified it yet."): 'Non lo hai ancora identificato.',
    # --- i nomi delle ricette, tetto 23 --------------------------------
    (572, 'create junk'): 'creare cianfrusaglie',
    (579, 'inequivalent exchange'): 'scambio impari',
    (586, 'distillation'): 'distillazione',
    (593, 'instant ale'): 'fermentazione lampo',
    (600, 'cure crystal'): 'cristallo curativo',
    (607, 'harmful potion'): 'pozione nociva',
    (614, 'disinfectant'): 'disinfettante',
    (621, 'encount canceller'): 'scacciamostri',
    (628, 'extract essential oil'): 'olio essenziale',
    (635, 'ancient medicine'): 'medicina antica',
    (642, 'novelty medicine'): 'medicina moderna',
    (649, 'agonising medicine'): 'medicina del dolore',
    (656, 'cursed medicine'): 'medicina maledetta',
    (663, 'ball making'): 'palla fatta a mano',
    (670, 'mysterious diary'): 'diario di qualcuno',
    (677, 'fossil restoration'): 'ricostruzione fossile',
    (684, 'rust removal'): 'togliere la ruggine',
    (691, 'sulfuric'): 'acido solforico',
    (698, 'homemade molotov'): 'molotov fatta in casa',
    (705, 'ground bait'): 'pastura',
    (712, 'putitoro'): 'putitoro',
    (720, 'puff puff bread'): 'fare il pane',
    (727, 'mandrake salad'): 'insalata di mandragora',
    (735, 'steamed meat bun'): 'panino di carne',
    (743, 'sex change'): 'rito del cambio sesso',
    (750, 'unknown seed'): 'seme misterioso',
    (757, 'herb infusion'): 'infuso di erbe',
    (764, 'another evolution'): 'ramo evolutivo',
    (771, 'friendship token'): "pegno d'amicizia",
    (778, 'necromancy'): 'negromanzia',
    (785, 'necro remodel'): 'ritocco negromantico',
    (792, 'dark fusion'): 'fusione oscura',
    (799, 'brilliant rubynus'): 'rubynus lavorato',
    (806, 'emerald tablet'): 'smeraldo lavorato',
    (813, 'brilliant diamond'): 'diamante lavorato',
    (820, 'wood craft'): 'lavorare il legno',
    (827, 'stone craft'): 'lavorare la pietra',
    (834, 'clay craft'): 'ceramica',
    (841, 'craft mine'): 'mina artigianale',
    (848, 'barrel bomb'): 'bomba a barile',
    (855, 'poop bomb'): 'bomba di sterco',
    (862, 'crystal bomb'): 'bomba di mana',
    (869, 'big crystal bomb'): 'bomba di mana grande',
    (876, 'evil sword'): 'spada malefica',
    (883, 'true evil sword'): 'vera spada malefica',
    (890, 'large empty basket'): 'cesta grande vuota',
    (897, 'large picnic basket'): 'cesta da picnic',
    (904, 'first aid kit'): 'kit di pronto soccorso',
    (911, 'special ammo box'): 'cassa di munizioni',
    (918, 'tactical nuke'): 'atomica tattica',
    (925, 'tobacco processing'): 'lavorare il tabacco',
    (932, 'onigiri'): 'polpetta di riso',
    (939, 'coffee'): 'caffè scelto',
    (946, 'tea'): 'preparare il tè',
    (953, 'barley and wheat'): 'lavorare i cereali',
    (960, 'dairy products'): 'latticini',
    (967, 'fermentation coagulation'): 'cagliata fermentata',
    (974, 'mix feed'): 'mangime composto',
    (981, 'junk food'): 'cibo spazzatura',
    (988, 'hamburger'): 'hamburger',
    (995, 'kagami biraki'): 'rompere il mochi',
    (1002, 'Meat-filling resuscitation'): 'resurrezione di carne',
    (1009, 'lovely bouquet'): 'bel mazzo di fiori',
    (1016, 'log house'): 'casa di tronchi',
    (1023, 'Soft equip update'): 'rifare armatura molle',
    (1030, 'Hard equip update'): 'rifare armatura rigida',
    (1037, 'Sharp equip update'): 'rifare arma affilata',
    (1044, 'Soft equip making'): 'creare armatura molle',
    (1051, 'Hard equip making'): 'creare armatura rigida',
    (1058, 'Sharp equip making'): 'creare arma affilata',
    (1065, 'Starfiber'): 'fibra stellare',
    (1072, 'Appearance imitation'): "copiare l'aspetto",
    # --- i materiali, riga tagliata a 44 -------------------------------
    (1119, 'suitable flavoring'): 'condimento qualsiasi',
    (1120, 'any ore'): 'minerale qualsiasi',
    (1121, 'something made of wood'): 'qualcosa di legno',
    (1122, 'any item'): 'oggetto qualsiasi',
    (1123, 'fish'): 'pesce',
    (1124, 'EVitem'): 'oggetto evolutivo',
    (1125, 'rare herb'): 'erba rara',
    (1126, 'any seed'): 'seme qualsiasi',
    (1127, 'any vege'): 'verdura qualsiasi',
    (1128, 'any diary'): 'un diario',
    (1129, 'toxic potion'): 'pozione tossica',
    (1130, 'debuff potion'): 'pozione debilitante',
    (1131, 'any fruit'): 'frutto qualsiasi',
    (1132, 'any bread'): 'pane',
    (1133, 'any alcohol'): 'alcolico qualsiasi',
    (1134, 'any crystal bomb'): 'bomba di mana',
    (1135, 'any evil sword'): 'spada malefica',
    (1136, 'stardust, etc.'): 'polvere di stelle',
    (1137, 'any flower'): 'fiore qualsiasi',
    (1138, 'any head bone'): 'un teschio',
    (1139, 'any hard equip'): 'armatura rigida',
    (1140, 'any soft equip'): 'armatura molle',
    (1141, 'any sharp equip'): 'arma affilata',
    (1142, 'any coffin'): 'una bara',
    (1143, 'any bait'): 'esca qualsiasi',
    (1144, 'any barrel'): 'un barile',
    (1145, 'any healthy leaf'): 'erba medicinale',
    (1146, 'any holy item'): 'oggetto sacro',
    (1147, 'any blanket'): 'una coperta',
    (1148, 'reference item'): 'oggetto di riferimento',
    # --- i menu e le battute -------------------------------------------
    (1167, 'How many items do you want to create?'): 'Quanti ne vuoi fare?',
    (1168, 'Start blending'): 'Comincia a mescolare',
    (1169, 'Go back'): 'Torna indietro',
    (1170, 'From the start'): 'Da capo',
    (1231, 'Which recipe do you want to use?'): 'Quale ricetta vuoi usare?',
    (1253, 'Choose a recipe'): 'Scelta della ricetta',
    (1256, 'Name'): 'Nome',
    (1299, 'Recipe of '): 'Ricetta: ',
    (1389, 'Name'): 'Nome',
    (1566, 'The blending attempt failed!'): 'La mescolata è fallita!',
    (2509, ' *pug* '): ' *impasta impasta* ',
    (2509, ' *clank* '): ' *tuc tuc* ',
    (2536, 'A required material cannot be found.'): 'Manca un materiale.',
    (2593, 'You blend herbs with the food.'): 'Strofini le erbe sul cibo.',
    (2608, 'A possibility of another evolution was born.'):
        'È nata una nuova possibilità di evoluzione.',
    (3531, 'You hear the sound of the empty bottle shatters.'):
        'Senti il rumore della bottiglia che si rompe.',
    (3546, 'But the snow just melts.'): 'Ma con questa quantità non basta...',
    # --- le dinamiche ---------------------------------------------------
    (445, 'Chose the recipe of '): '"Hai scelto la ricetta: " + rpname(rpid)',
    (466, 'Add '): '"Aggiungi " + rpmatname(cnt) + ""',
    (496, 'The recipe of '): '"Ricetta: " + rpname(rpid)',
    (535, 'Add  gold.'): '"Aggiungi " + calcitemvalue(window_recipe_itemid, 3) + " monete."',
    (1376, 'Add \\"\\".'): '"Aggiungi \\"" + rpmatname(step) + "\\"."',
    (1484, 'You add .'): '"Aggiungi " + itemname(ci) + "."',
    (1551, 'You lose .'): '"Perdi " + itemname(rpref(10 + cnt * 2), 1) + "."',
    (2214, 'You successfully create '): '"Prepari " + itemname(ci, 1) + "!"',
    (2499, ' start blending of .'): 'name(cc) + " comincia a mescolare: " + rpname(rpid) + "."',
    (3131, 'You changed the equip to !'): '"Hai cambiato l\'equipaggiamento in " + itemname(ci) + "!"',
    (3194, 'You have learned new ability, .'):
        '"Impari una capacità nuova: " + skillname(SKILL_SPACT_ACCEL_NECRO) + "."',
    (3434, 'You scour the rust off the '): '"Togli la ruggine da " + itemname(ci)',
    (3459, 'You changed the appearance of .'): '"Cambi l\'aspetto di " + itemname(ci) + "."',
    (3411, 'You put  on .'):
        '"Versi " + itemname(ti, 1) + " sopra " + itemname(ci) + "."',
    (3492, 'You bait  with .'):
        '"Inneschi " + itemname(ci) + " con " + itemname(ti, 1) + "."',
    (3506, 'You shower  on .'): '"Cospargi " + itemname(ti, 1) + " con " + itemname(ci) + "."',
    (3529, 'You throw  into .'): '"Getti " + itemname(ci) + " dentro " + itemname(ti, 1) + "."',
}


def main():
    voci = [json.loads(r) for r in io.open(LOTTO, encoding='utf-8') if r.strip()]

    # 1. le voci gia' rese altrove: si riprendono dal dizionario
    gia = {}
    for nomefile in sorted(os.listdir('dizionario')):
        for r in io.open(f'dizionario/{nomefile}', encoding='utf-8'):
            if not r.strip():
                continue
            d = json.loads(r)
            if d.get('jp') and d.get('it'):
                gia.setdefault((d['jp'], d['tipo']), d['it'])

    riprese = 0
    scritte = 0
    mancanti = []
    for v in voci:
        chiave = (v['riga'], v['en'])
        if chiave in RESE:
            v['it'] = RESE[chiave]
            scritte += 1
            continue
        gemella = gia.get((v['jp'], v['tipo']))
        if gemella:
            v['it'] = gemella
            riprese += 1
            continue
        mancanti.append(v)

    if mancanti:
        print(f'⚠️ {len(mancanti)} voci senza resa:')
        for v in mancanti:
            print(f"   {v['riga']:>6} {v['tipo'][:3]} | {v['jp'][:24]!r} | {v['en']!r}")
        raise SystemExit('non scrivo')

    testo = '\n'.join(json.dumps(v, ensure_ascii=False) for v in voci) + '\n'
    io.open(LOTTO, 'w', encoding='utf-8', newline='\n').write(testo)
    print(f'{scritte} rese scritte, {riprese} riprese dal dizionario, '
          f'{len(voci)} in tutto')


if __name__ == '__main__':
    main()
