# -*- coding: utf-8 -*-
"""Il secondo lotto di `trait.hsp`: le mutazioni e le resistenze.

Segue le regole del primo lotto ([[lotto-trait-001.py]]): nomi **sostantivi**,
tetti misurati da [[misura-trait.py]].

## Le sigle non si inventano: stanno gia' in `text.hsp:61`

    _stats = FOR, COS, DES, PER, APP, VOL, MAG, CAR

Quindi `[STR+3]` diventa `[FOR+3]`, `[DEX+3]` `[DES+3]`, `[CHR+5]` `[CAR+5]`.
Per le altre si usa il nome che il gioco da' all'abilita': `Memorization` e'
«Memoria» (`skill.hsp:267`), `Regeneration` «Rigenerazione» (`skill.hsp:644`),
`Speed` «Velocita'» (`skill.hsp:59`), e gli elementi sono Fuoco, Gelo, Suono,
Magia (`text.hsp:1951`-`:1981`).

⚠️⚠️ **`HP` e `PV` non sono la stessa cosa, e confonderli cambia il senso.**
`glossario.md:138` mette `HP` fra gli **invariati**, e in Elona `PV` e' il
valore di protezione — lo usa questo stesso file per la pelle di ferro,
`[PV+3]`. Il primo lotto aveva reso `[HP+5%]` con `[PV+5%]`: diceva al
giocatore che gli saliva l'armatura invece dei punti vita. Corretto nella
stessa sessione.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LOTTO = 'lavoro/_trait.jsonl'

RESE = {
    # --- il mana nel corpo ---------------------------------------------
    (407, 'Magical Gene'): 'Gene magico',
    (407, 'Magical Cell'): 'Cellula magica',
    (407, 'Magical Blood'): 'Sangue magico',
    (407, 'Magic Body'): 'Corpo magico',
    (407, 'Magic Being'): 'Essere magico',
    (409, 'You gain MP by using gene manipulation.'):
        'Manipolare i geni ti fa guadagnare MP.',
    (409, 'Your genes contain magic. [MP+5%]'):
        'I tuoi geni contengono magia. [MP+5%]',
    (409, 'Your cells contain magic [MP+10%]'):
        'Le tue cellule contengono magia. [MP+10%]',
    (409, 'Your blood contains magic [MP+15%]'):
        'Il tuo sangue contiene magia. [MP+15%]',
    (409, 'Your body is made of magic. [MP+20%]'):
        'Il tuo corpo è fatto di magia. [MP+20%]',
    (409, 'Magic dominates your entire body. [MP+25%]'):
        'La magia domina tutto il tuo corpo. [MP+25%]',
    # --- i talenti che restano ------------------------------------------
    (419, 'Strings Assassin'): 'Fili assassini',
    (421, 'You concealed sharp durable strings.'):
        'Tieni nascosti dei fili sottili e resistenti.',
    (421, 'You manipulate strings freely.'): 'Manovri i fili a piacimento.',
    (433, 'Super Accel'): 'Superaccelerazione',
    (435, 'You pursue speed more than anyone.'):
        'Insegui la velocità più di chiunque altro.',
    (435, 'Your acceleration is amazing. [Speedspell+]'):
        'La tua accelerazione è formidabile. [Accelerazione+]',
    (445, 'Ground Manipulater'): 'Controllo del suolo',
    (447, 'You discover the energy of the land.'):
        "Scopri l'energia che scorre nella terra.",
    (447, 'You manipulate the ground.'): 'Manovri il suolo.',
    (459, 'Discernment'): 'Discernimento',
    (461, "In business life, you learned to judge people's age/sex/faith."):
        'Negli affari hai imparato a leggere età, sesso e fede.',
    (461, "You can see the other's gender, age, and religion."):
        'Vedi sesso, età e religione di chi hai davanti.',
    (470, 'Shiki-Origami'): 'Origami shiki',
    (472, 'You have mastered the ancient arts of manipulating paper.'):
        "Padroneggi l'antica arte di manovrare la carta.",
    (472, 'You know magical papercrafts.'): 'Conosci gli origami magici.',
    # --- le mutazioni: nome, poi i gradi --------------------------------
    (485, 'Cannibalism'): 'Cannibalismo',
    (485, 'You have no trouble eating human flesh.'):
        'Mangi carne umana senza farti problemi.',
    (487, 'You are charmed by the flavor of human flesh.'):
        'Il sapore della carne umana ti ha conquistato.',
    (487, 'You can no longer accept human flesh.'):
        'La carne umana non ti va più giù.',
    (496, 'Iron Skin'): 'Pelle di ferro',
    (496, 'Your skin is hard. [PV+3]'): 'La tua pelle è dura. [PV+3]',
    (496, 'Your skin is very hard. [PV+6]'): 'La tua pelle è durissima. [PV+6]',
    (496, 'Your skin is as hard as iron. [PV+9]'):
        'La tua pelle è dura come il ferro. [PV+9]',
    (499, 'Albino'): 'Albinismo',
    (499, 'Your skin is white. [PV-3]'): 'La tua pelle è bianca. [PV-3]',
    (499, 'Your skin is fragile. [PV-6]'): 'La tua pelle è fragile. [PV-6]',
    (499, 'Your skin is collapsing. [PV-9]'): 'La tua pelle si sfalda. [PV-9]',
    (501, 'Your skin becomes harder.'): 'La tua pelle si indurisce.',
    (501, 'Your skin becomes pale.'): 'La tua pelle sbianca.',
    (511, 'Flexible Joint'): 'Snodi flessibili',
    (511, 'Your joints are flexible. [DEX+3]'):
        'I tuoi snodi sono flessibili. [DES+3]',
    (511, 'Your joints are very flexible. [DEX+6]'):
        'I tuoi snodi sono molto flessibili. [DES+6]',
    (511, 'Your joints are incredibly flexible. [DEX+9]'):
        'I tuoi snodi sono flessibilissimi. [DES+9]',
    (514, 'Creaking Joint'): 'Snodi che scricchiolano',
    (514, 'Your joints creak. [DEX-3]'): 'I tuoi snodi scricchiolano. [DES-3]',
    (514, 'You are worrying about your joint creakings. [DEX-6]'):
        'Gli scricchiolii degli snodi ti preoccupano. [DES-6]',
    (514, 'You have terrible joint creakings. [DEX-9]'):
        'I tuoi snodi scricchiolano da far paura. [DES-9]',
    (516, 'Your joints become flexible.'): 'I tuoi snodi diventano flessibili.',
    (516, 'Your joints creak.'): 'I tuoi snodi scricchiolano.',
    (526, 'Troll Blood'): 'Sangue di troll',
    (526, 'Your wounds regenerate rapidly. [Regeneration+]'):
        'Le tue ferite si chiudono in fretta. [Rigenerazione+]',
    (526, 'Your wounds regenerate instantly. [Regeneration++]'):
        "Le tue ferite si chiudono all'istante. [Rigenerazione++]",
    (529, 'Anemia'): 'Anemia',
    (529, 'You suffer from anemia. [Regeneration-]'):
        'Soffri di anemia. [Rigenerazione-]',
    (529, 'You constantly have attacks of anemia. [Regeneration--]'):
        'Hai attacchi di anemia di continuo. [Rigenerazione--]',
    (531, 'Suddenly your blood become greenish!'):
        'Di colpo il tuo sangue vira al verde!',
    (531, 'Your metabolism slows down.'): 'Il tuo metabolismo rallenta.',
    (541, 'Lithe Leg'): 'Gambe agili',
    (541, 'You have lithe legs. [SPD+5]'): 'Hai gambe agili. [VEL+5]',
    (541, 'You have very lithe legs. [SPD+10]'):
        'Hai gambe molto agili. [VEL+10]',
    (541, 'You have ideal legs. [SPD+15]'): 'Hai gambe perfette. [VEL+15]',
    (544, 'Twisted Leg'): 'Gambe storte',
    (544, 'Your legs are twisted. [SPD-5]'): 'Hai le gambe storte. [VEL-5]',
    (544, 'Your legs are very twisted. [SPD-10]'):
        'Hai le gambe molto storte. [VEL-10]',
    (544, 'Your legs are broken. [SPD-15]'): 'Hai le gambe a pezzi. [VEL-15]',
    (546, 'Your legs become lithe.'): 'Le tue gambe diventano agili.',
    (546, 'Your legs are twisted!'): 'Le tue gambe si storcono!',
    (556, 'Strong Arm'): 'Braccia forti',
    (556, 'You have well-knit arms. [STR+3]'):
        'Hai braccia ben piantate. [FOR+3]',
    (556, 'You have well-muscled arms. [STR+6]'):
        'Hai braccia muscolose. [FOR+6]',
    (556, 'You have ideal arms. [STR+9]'): 'Hai braccia perfette. [FOR+9]',
    (559, 'Weak Arm'): 'Braccia deboli',
    (559, 'Your arms are thin. [STR-3]'): 'Hai braccia magre. [FOR-3]',
    (559, 'Your arms are very thin. [STR-6]'):
        'Hai braccia magrissime. [FOR-6]',
    (559, 'Your arms are just decorative. [STR-9]'):
        'Le tue braccia sono solo un ornamento. [FOR-9]',
    (561, 'Your arms grow stronger.'): 'Le tue braccia si irrobustiscono.',
    (561, 'Your arms become thin.'): 'Le tue braccia si assottigliano.',
    (571, 'Sweet Voice'): 'Voce dolce',
    (571, 'Your voice is sweet. [CHR+5]'): 'Hai una voce dolce. [CAR+5]',
    (571, 'Your voice charms everyone. [CHR+10]'):
        'La tua voce incanta chiunque. [CAR+10]',
    (574, 'Husky Voice'): 'Voce roca',
    (574, 'Your voice is husky. [CHR-5]'): 'Hai una voce roca. [CAR-5]',
    (574, 'Everyone is frightened when you talk. [CHR-10]'):
        'Quando parli metti paura a tutti. [CAR-10]',
    (576, 'Your voice becomes lovely.'): 'La tua voce si fa deliziosa.',
    (576, 'Your voice becomes scary.'): 'La tua voce si fa spaventosa.',
    (586, 'Brain Computer'): 'Cervello meccanico',
    (586, 'Your brain is mechanized. [Memorization+4]'):
        'Il tuo cervello è meccanizzato. [Memoria+4]',
    (586, 'Your brain is fully mechanized. [Memorization+8]'):
        'Il tuo cervello è tutto meccanizzato. [Memoria+8]',
    (589, 'Stupid'): 'Ottusità',
    (589, 'You are stupid. [Memorization-4]'): 'Sei una zucca vuota. [Memoria-4]',
    (589, 'You are really stupid. [Memorization-8]'):
        'Sei una zucca proprio vuota. [Memoria-8]',
    (591, 'Your brain is mechanized!'): 'Il tuo cervello viene meccanizzato!',
    (591, 'Your brain degenerates.'): 'Il tuo cervello si guasta.',
    # --- le resistenze ---------------------------------------------------
    (601, 'Magic Res+'): 'Res. magia+',
    (601, 'You have resistance to magic. [RES Magic+]'):
        'Resisti alla magia. [RES Magia+]',
    (604, 'Magic Res-'): 'Res. magia-',
    (604, 'You have weakness to magic. [RES Magic-]'):
        'Sei debole alla magia. [RES Magia-]',
    (606, 'You gain resistance to magic.'): 'Acquisti resistenza alla magia.',
    (606, 'You lose resistance to magic.'): 'Perdi resistenza alla magia.',
    (616, 'Sound Res+'): 'Res. suono+',
    (616, 'Your eardrums are thick. [RES Sound+]'):
        'Hai timpani spessi. [RES Suono+]',
    (619, 'Sound Res-'): 'Res. suono-',
    (619, 'Your eardrums are thin. [RES Sound-]'):
        'Hai timpani sottili. [RES Suono-]',
    (621, 'Your eardrums become thick.'): 'I tuoi timpani si ispessiscono.',
    (621, 'Your eardrums become thin.'): 'I tuoi timpani si assottigliano.',
    (631, 'Fire Res+'): 'Res. fuoco+',
    (631, 'Your blood is boiling. [RES Fire+]'):
        'Il tuo sangue ribolle. [RES Fuoco+]',
    (634, 'Fire Res-'): 'Res. fuoco-',
    (634, 'Your skin gets gooseflesh. [RES Fire-]'):
        "Ti viene la pelle d'oca. [RES Fuoco-]",
    (636, 'Your blood starts to boil.'): 'Il tuo sangue comincia a ribollire.',
    (636, 'Your skin gets gooseflesh.'): "Ti viene la pelle d'oca.",
    (646, 'Cold Res+'): 'Res. gelo+',
    (646, 'Your skin is covered by frost. [RES Cold+]'):
        'La brina ti copre la pelle. [RES Gelo+]',
}


def main():
    voci = [json.loads(r) for r in io.open(LOTTO, encoding='utf-8') if r.strip()]
    fatte = 0
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
