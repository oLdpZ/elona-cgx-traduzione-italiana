# -*- coding: utf-8 -*-
"""Il terzo lotto di `trait.hsp`: il male dell'etere e i tratti di razza.

Chiude il file. Regole dei due lotti precedenti ([[lotto-trait-001.py]],
[[lotto-trait-002.py]]): nomi sostantivi, sigle da `text.hsp:61`, tetti da
[[misura-trait.py]].

## Le sigle di questo lotto, e da dove vengono

    STR -> FOR    END -> COS    DEX -> DES    PER -> PER
    LER -> APP    WIL -> VOL    MAG -> MAG    CHR -> CAR      text.hsp:61
    SPD -> VEL                                                skill.hsp:59
    HP, MP, SP, PV, DV, Karma, Mana                           invariati.md

⚠️ `PV` e `DV` restano cosi': sono il valore di protezione e quello di
schivata, e `glossario.md:138` li dichiara invariati insieme (`PVDV`).

⚠️ `END` e' **Endurance**, cioe' la Costituzione: `glossario.md` lo dice gia'
per `Con-Attack/X` → «Attacco Cos/X», dove *Con* e' Costituzione.

## Le righe di questo lotto sono le piu' lunghe del file

Sono le descrizioni dell'etere, che vanno sulla **riga larga** (86 caratteri,
meno i 6 di `[Ether]`). Upstream ne sfora due su centosettanta — la piu' lunga
ne ha 95 — perche' `mes` non taglia e il testo esce dalla finestra. Le rese
italiane stanno sotto, tranne dove l'inglese era gia' fuori.
"""
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LOTTO = 'lavoro/_trait.jsonl'

RESE = {
    (649, 'Cold Res-'): 'Res. gelo-',
    (649, 'Your skin is sheer. [RES Cold-]'):
        'Hai la pelle sottile. [RES Gelo-]',
    (651, 'You feel hot-headed.'): 'Ti sale il calore alla testa.',
    (651, 'You shiver.'): 'Ti vengono i brividi.',
    (661, 'Lightning Res+'): 'Res. fulmine+',
    (661, 'You have resistance to lightning. [RES Lightning+]'):
        'Resisti al fulmine. [RES Fulmine+]',
    (664, 'Lightning Res-'): 'Res. fulmine-',
    (664, 'You have weakness to lightning. [RES Lightning-]'):
        'Sei debole al fulmine. [RES Fulmine-]',
    (666, 'You gain resistance to lightning.'):
        'Acquisti resistenza al fulmine.',
    (666, 'You lose resistance to lightning.'): 'Perdi resistenza al fulmine.',
    (676, 'Hawk Eye'): 'Occhio di falco',
    (676, 'You have the eyes of a cat. [PER+5]'):
        'Hai occhi da gatto. [PER+5]',
    (676, 'You have the eyes of a hawk. [PER+10]'):
        'Hai occhi da falco. [PER+10]',
    (679, 'Color Blind'): 'Daltonismo',
    (679, 'You are partially color-blind. [PER-5]'):
        'Confondi certi colori. [PER-5]',
    (679, 'You are blind in one eye. [PER-10]'):
        'Non ci vedi da un occhio. [PER-10]',
    (681, 'Your eyes glow.'): 'I tuoi occhi si accendono.',
    (681, 'Your sight is weakened.'): 'La tua vista si indebolisce.',
    (691, 'You have resistance to fire.'): 'Resisti al fuoco.',
    (691, 'You have strong resistance to fire.'): 'Resisti molto al fuoco.',
    (694, 'You have weakness to fire.'): 'Sei debole al fuoco.',
    (694, 'You have strong weakness to fire.'): 'Sei molto debole al fuoco.',
    (705, 'You have resistance to cold.'): 'Resisti al gelo.',
    (705, 'You have strong resistance to cold.'): 'Resisti molto al gelo.',
    (708, 'You have weakness to cold.'): 'Sei debole al gelo.',
    (708, 'You have strong weakness to cold.'): 'Sei molto debole al gelo.',
    (719, 'You have resistance to poison.'): 'Resisti al veleno.',
    (719, 'You have strong resistance to poison.'): 'Resisti molto al veleno.',
    (722, 'You have weakness to poison.'): 'Sei debole al veleno.',
    (722, 'You have strong weakness to poison.'): 'Sei molto debole al veleno.',
    (733, 'You have resistance to darkness.'): 'Resisti al buio.',
    (733, 'You have strong resistance to darkness.'): 'Resisti molto al buio.',
    (736, 'You have weakness to darkness.'): 'Sei debole al buio.',
    (736, 'You have strong weakness to darkness.'): 'Sei molto debole al buio.',
    (747, 'You take less damage from magic reaction.'):
        'Il contraccolpo magico ti fa meno danno.',
    (757, 'You have outstanding resistances.'): 'Hai resistenze fuori dal comune.',
    (775, "You can't wear equipment weight over 2s. [DV++]"):
        'Non puoi portare più di 2s di equipaggiamento. [DV++]',
    (788, "You don't feel guilty. [Karma limit -20]"):
        'Non ti senti in colpa. [Limite karma -20]',
    (798, 'You are a good man. [Karma limit +20]'):
        'Hai buon cuore. [Limite karma +20]',
    (808, 'Quality stuff is generated around you.'):
        'Intorno a te compare roba di qualità.',
    (818, 'You are given physical damage reduction.'):
        'Il danno fisico che subisci cala.',
    (828, 'Elemental spells you cast are empowered.'):
        'Le tue magie elementali sono più forti.',
    (838, 'You are surrounded by an aura that cures insanity.'):
        "Ti circonda un'aura che cura la follia.",
    (848, 'You moe.'): 'Fai tenerezza.',
    (858, "You won't be dimmed."): 'Non ti si annebbia la vista.',
    (868, 'You reduce the hunger drop when you are hungry.'):
        'Quando hai fame, la fame cresce più piano.',
    (878, 'You can gather more materials.'): 'Raccogli più materiali.',
    (888, 'You receive extra bonus points.'): 'Ricevi punti bonus in più.',
    (898, 'You have resistance to magic.'): 'Resisti alla magia.',
    (898, 'You have strong resistance to magic.'): 'Resisti molto alla magia.',
    (901, 'You have weakness to magic.'): 'Sei debole alla magia.',
    (901, 'You have strong weakness to magic.'): 'Sei molto debole alla magia.',
    (912, 'Your body is changing every moment.'):
        'Il tuo corpo cambia di continuo.',
    (922, 'Your body slows the progress of the Ether Disease.'):
        "Il tuo corpo rallenta l'avanzata del male dell'etere.",
    (932, 'You generate gravity. [Weight+10%]'):
        'Generi gravità. [Peso+10%]',
    (932, 'You generate heavy gravity. [Weight+20%]'):
        'Generi una gravità pesante. [Peso+20%]',
    (932, 'You generate massive gravity. [Weight+30%]'):
        'Generi una gravità enorme. [Peso+30%]',
    (934, 'The gravity around you has diminished.'):
        'La gravità intorno a te cala.',
    (934, 'You start to generate gravity.'): 'Cominci a generare gravità.',
    (943, 'You have sores on your face. [CHR]'):
        'Hai piaghe sul viso. [CAR]',
    (943, 'Your face is ulcerate. [CHR]'): 'Il tuo viso è ulcerato. [CAR]',
    (943, 'Your face is crumbling. [CHR]'): 'Il tuo viso si sfalda. [CAR]',
    (945, 'The swelling in your face decreases.'): 'Il gonfiore del viso cala.',
    (945, 'Your face is festered.'): 'Il tuo viso suppura.',
    (955, "Your feet transformed into hooves. [SPD+ Can't wear boots]"):
        'I tuoi piedi sono zoccoli. [VEL+ Niente stivali]',
    (957, 'Your feet become normal.'): 'I tuoi piedi tornano normali.',
    (957, 'Your feet change into hooves.'): 'I tuoi piedi diventano zoccoli.',
    (967, 'You have 4 eyes. [PER+ CHR]'): 'Hai quattro occhi. [PER+ CAR]',
    (969, 'Your eyes become normal.'): 'I tuoi occhi tornano normali.',
    (969, 'Your eyes are multiplying.'): 'I tuoi occhi si moltiplicano.',
    (980, "You have grown feathers. [SPD+ Weight-20% Can't wear cloaks]"):
        'Ti sono cresciute le piume. [VEL+ Peso-20% Niente mantelli]',
    (982, 'Your feathers wilt.'): 'Le tue piume avvizziscono.',
    (982, 'Feathers come out from your back.'):
        'Dalla schiena ti spuntano le piume.',
    (993, "Your neck is extremely thick. [CHR PV+ Can't wear amulets]"):
        'Hai il collo grossissimo. [CAR PV+ Niente amuleti]',
    (995, 'Your neck becomes thin.'): 'Il tuo collo si assottiglia.',
    (995, 'Your neck becomes extremely thick.'): 'Il tuo collo si ingrossa.',
    (1006, 'Desire for violence arises within you. [Dmg taken+, Dmg dealt+] '):
        'Ti sale la voglia di violenza. [Danno subito+, inflitto+] ',
    (1008, ' A deep sense of peace fills your heart.'):
        ' Una pace profonda ti riempie il cuore.',
    (1008, 'Hatred dominates your soul.'): "L'odio ti domina l'animo.",
    (1017, 'Your head has grown huge. [END DEX LER+ WIL+]'):
        'La tua testa è diventata enorme. [COS DES APP+ VOL+]',
    (1019, 'Your head is normal size now.'): 'La tua testa torna normale.',
    (1019, 'Suddenly your head become giant size.'):
        'Di colpo la tua testa diventa gigantesca.',
    (1032, 'Clouds of rain follow you. [Chance of rain+]'):
        'Nuvole di pioggia ti seguono. [Piu pioggia]',
    (1034, 'Clouds of rain stop following you.'):
        'Le nuvole smettono di seguirti.',
    (1034, 'Clouds of rain start to follow you.'):
        'Delle nuvole di pioggia cominciano a seguirti.',
    (1043, 'You are addicted to potions. [Consume potions]'):
        'Sei schiavo delle pozioni. [Consuma pozioni]',
    (1045, 'You are no longer addicted to potions.'):
        'Non sei più schiavo delle pozioni.',
    (1045, 'Potions! More potions!! Suddenly, you become addicted to potions.'):
        'Pozioni! Altre pozioni!! Di colpo, sei schiavo delle pozioni.',
    (1054, 'You feel more sleepy during the day than at night. [Change in sleepiness]'):
        'Hai più sonno di giorno che di notte. [Sonno spostato]',
    (1056, 'You started feeling sleepy at night again.'):
        'Ricominci a sentire sonno di notte.',
    (1056, 'You start to feel sleepy during the day.'):
        'Cominci a sentire sonno di giorno.',
    (1065, 'You suffer debilitation. [HP-15% STR]'):
        'Ti porti addosso una debolezza. [HP-15% FOR]',
    (1067, 'You become healthy again.'): 'Torni in salute.',
    (1067, 'You become weak, very weak.'): 'Ti fai debole, debolissimo.',
    (1078, 'You have dementia. [MP-15% MAG]'):
        '"Hai la mente annebbiata. [MP-15% MAG" + '
        'limit((4 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 2) * (-1), -255, 0) + "]"',
    (1080, 'You become confident again.'): 'Ti torna la lucidità.',
    (1080, 'You become feebleminded.'): 'La tua mente si annebbia.',
    (1091, 'You are covered by heavy carapace. [PV+ SPD]'):
        '"Ti copre un carapace pesante. [PV+" + '
        'limit(15 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 2, 0, 255) + " VEL" + '
        'limit((20 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 2) * (-1), -255, 0) + "]"',
    (1093, 'Your carapace starts to break.'): 'Il tuo carapace comincia a rompersi.',
    (1093, 'A heavy carapace starts to cover up your skin.'):
        'Un carapace pesante comincia a coprirti la pelle.',
    (1104, 'You destabilize the space around you. [Random teleporation]'):
        'Sconvolgi lo spazio intorno a te. [Teletrasporto casuale]',
    (1106, 'You feel steady.'): 'Ti senti stabile.',
    (1106, 'You feel unstable.'): 'Ti senti instabile.',
    (1115, 'You are a living mana battery. [Absorb mana from rods]'):
        'Sei una batteria vivente di mana. [Assorbe mana dalle bacchette]',
    (1117, 'You are no longer a living mana battery.'):
        'Non sei più una batteria vivente di mana.',
    (1117, 'You are a living mana battery.'):
        'Sei una batteria vivente di mana.',
    (1126, 'Poison drips from your hands. [Poison potions RES Poison+]'):
        'Ti gocciola veleno dalle mani. [Avvelena pozioni RES Veleno+]',
    (1128, 'Your hands are clean now.'): 'Le tue mani sono pulite.',
    (1128, 'Poison starts to drip from your hands.'):
        'Comincia a gocciolarti veleno dalle mani.',
    (1138, "Your head is growing ears of a beast. [PER+ Can't wear helms]"):
        '"Ti crescono orecchie da bestia. [PER+" + '
        'limit(10 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 4, 0, 255) + " Niente elmi]"',
    (1140, 'Your ears have been restored.'): 'Le tue orecchie tornano normali.',
    (1140, 'Ears of the beast grew on your head.'):
        'Sulla testa ti sono cresciute orecchie da bestia.',
    (1150, "Your bones are popping out. [Deals cut damage to the attacker, Can't wear armors]"):
        'Ti spuntano le ossa. [Taglia chi ti colpisce, Niente armature]',
    (1152, 'Your bones have retracted.'): 'Le tue ossa rientrano.',
    (1152, 'Sharp bones from your body pierced through your skin.'):
        'Ossa aguzze ti hanno bucato la pelle.',
    (1161, "You have a developed tail. [DEX+ Can't wear girdles]"):
        '"Hai una coda ben cresciuta. [DES+" + '
        'limit(10 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 4, 0, 255) + " Niente cinture]"',
    (1163, 'Your tail has shrunk.'): 'La tua coda si è ritirata.',
    (1163, 'Your tail has grown.'): 'La tua coda è cresciuta.',
    (1173, 'The beautiful flower is blooming on you. [Prevents-aliens Healing CHR]'):
        '"Su di te sboccia un bel fiore. [Anti-alieni Guarigione" + '
        'limit((4 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 2) * (-1), -255, 0) + " CAR" + '
        'limit(1 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 8, 0, 255) + "]"',
    (1175, 'The flower that was blooming on you scattered.'):
        'Il fiore che ti sbocciava addosso si è sfaldato.',
    (1175, 'Your skin has torn and flowers have bloomed.'):
        'La tua pelle si è lacerata e sono sbocciati dei fiori.',
    (1186, "You have a big webbeds. [Swimming+ Can't wear rings]"):
        '"Hai membrane larghe. [Nuoto+" + '
        'limit(2 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 6, 0, 255) + " Niente anelli]"',
    (1188, 'Your webbed has become smaller.'): 'Le tue membrane si rimpiccioliscono.',
    (1188, 'Large webbeds were generated between your fingers.'):
        'Fra le dita ti sono cresciute membrane larghe.',
    (1198, "Your arms are thicker than your torso. [STR+ Can't wear gloves]"):
        '"Hai braccia più grosse del busto. [FOR+" + '
        'limit(5 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 6, 0, 255) + " Niente guanti]"',
    (1200, 'Your arms became restored.'): 'Le tue braccia tornano normali.',
    (1200, 'Your arms become thicker than your torso.'):
        'Le tue braccia diventano più grosse del busto.',
    (1210, "Your hands are blades. [Can't wear weapons, Available Decapitation]"):
        'Le tue mani sono lame. [Niente armi, Decapitazione]',
    (1212, 'Your hands became restored.'): 'Le tue mani tornano normali.',
    (1212, 'Your hands has turned into sharp blades.'):
        'Le tue mani sono diventate lame affilate.',
    (1221, 'Your mouth is torn. [CHR Available Voracity Fang]'):
        '"Hai la bocca lacerata. [CAR" + '
        'limit((4 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 8) * (-1), -255, 0) + " Zanna vorace]"',
    (1223, 'Your mouth became restored.'): 'La tua bocca torna normale.',
    (1223, 'Your mouth began to torn greatly.'):
        'La tua bocca comincia a lacerarsi.',
    (1233, 'You have multiple mouths. [END Halve eating turn]'):
        '"Hai più bocche. [COS" + '
        'limit((4 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 6) * (-1), -255, 0) + " Mangi in metà tempo]"',
    (1235, 'Your mouth has returned to its original number.'):
        'Le tue bocche tornano di numero normale.',
    (1235, 'Your skin cracked and a new mouth was formed.'):
        'La tua pelle si è spaccata ed è nata una bocca nuova.',
    (1245, 'Your libido is abnormal. [SP+20% WIL LER]'):
        '"Hai una libido fuori norma. [SP+20% VOL" + '
        'limit((4 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 4) * (-1), -255, 0) + " APP" + '
        'limit((4 + cdata(CDATA_LEVEL, CHARA_PLAYER) / 4) * (-1), -255, 0) + "]"',
    (1247, 'Your libido has subsided.'): 'La tua libido si è calmata.',
    (1247, 'You have full of libido pathologically.'):
        'Hai una libido malata.',
    (1258, 'Thin tentacles are growing from you. [Tentacles runaway during battle and interference]'):
        'Ti crescono tentacoli sottili. [Impazziscono in lotta e in intimità]',
    (1258, 'Thick tentacles are growing from you. [Strong tentacles runaway during battle and interference]'):
        'Ti crescono tentacoli grossi. [Impazziscono forte in lotta e in intimità]',
    (1260, 'Your tentacles have shrunk.'): 'I tuoi tentacoli si sono ritirati.',
    (1260, 'Tentacles have grown from your body.'):
        'Dal tuo corpo sono cresciuti dei tentacoli.',
}


# I marcatori dell'etere portano dentro un NUMERO calcolato dal livello del
# personaggio — `[CHR-9]`, `[PV+27 SPD-32]` — e quel numero sta in un
# `limit(...)` fuori dalle virgolette. Una resa scritta a mano come testo piatto
# lo butta via, e `verifica` lo vede: «interpolazioni non conservate».
#
# ⚠️ Invece di riscrivere l'espressione a mano dieci volte, qui si prende
# `en_grezzo` e si sostituiscono **solo i pezzi fra virgolette**, in ordine: il
# tessuto di `limit()` e `+` resta identico per costruzione, e non si puo'
# sbagliare un segno. E' la stessa idea della toppa `prima` della 61a — non
# toccare cio' che non si sta traducendo.
SEGMENTI = {
    (943, 'You have sores on your face. [CHR]'):
        ['Hai piaghe sul viso. [CAR', ']'],
    (943, 'Your face is ulcerate. [CHR]'):
        ['Il tuo viso è ulcerato. [CAR', ']'],
    (943, 'Your face is crumbling. [CHR]'):
        ['Il tuo viso si sfalda. [CAR', ']'],
    (955, "Your feet transformed into hooves. [SPD+ Can't wear boots]"):
        ['I tuoi piedi sono zoccoli. [VEL+', ' Niente stivali]'],
    (967, 'You have 4 eyes. [PER+ CHR]'):
        ['Hai quattro occhi. [PER+', ' CAR', ']'],
    (980, "You have grown feathers. [SPD+ Weight-20% Can't wear cloaks]"):
        ['Ti sono cresciute le piume. [VEL+', ' Peso-20% Niente mantelli]'],
    (993, "Your neck is extremely thick. [CHR PV+ Can't wear amulets]"):
        ['Hai il collo grossissimo. [CAR', ' PV+', ' Niente amuleti]'],
    (1006, 'Desire for violence arises within you. [Dmg taken+, Dmg dealt+] '):
        ['Ti sale la voglia di violenza. [Danno subito+', ', inflitto+', '] '],
    (1017, 'Your head has grown huge. [END DEX LER+ WIL+]'):
        ['La tua testa è diventata enorme. [COS', ' DES', ' APP+', ' VOL+', ']'],
    (1065, 'You suffer debilitation. [HP-15% STR]'):
        ['Ti porti addosso una debolezza. [HP-15% FOR', ']'],
}

_LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')


def ricuci(en_grezzo, segmenti):
    """L'espressione inglese con i soli letterali sostituiti dall'italiano."""
    quanti = len(_LETTERALE.findall(en_grezzo))
    if quanti != len(segmenti):
        raise SystemExit(f'{en_grezzo!r}: {quanti} letterali, {len(segmenti)} pezzi')
    coda = iter(segmenti)
    return _LETTERALE.sub(lambda m: '"' + next(coda) + '"', en_grezzo)


def main():
    voci = [json.loads(r) for r in io.open(LOTTO, encoding='utf-8') if r.strip()]
    fatte = 0
    for v in voci:
        chiave = (v['riga'], v['en'])
        if chiave in SEGMENTI:
            v['it'] = ricuci(v['en_grezzo'], SEGMENTI[chiave])
            fatte += 1
    for v in voci:
        chiave = (v['riga'], v['en'])
        if chiave in RESE and not v.get('it'):
            v['it'] = RESE[chiave]
            fatte += 1
    non_usate = set(RESE) - {(v['riga'], v['en']) for v in voci}
    if non_usate:
        for k in sorted(non_usate):
            print(f'  ⚠️ {k} non sta nel lotto')
        raise SystemExit('tavolo non allineato: non scrivo')
    testo = '\n'.join(json.dumps(v, ensure_ascii=False) for v in voci) + '\n'
    io.open(LOTTO, 'w', encoding='utf-8', newline='\n').write(testo)
    resta = sum(1 for v in voci if not v.get('it'))
    print(f'{fatte} rese scritte; restano {resta} voci senza resa')


if __name__ == '__main__':
    main()
