# -*- coding: utf-8 -*-
"""Il primo lotto di `trait.hsp`: i talenti che si comprano coi punti feat.

La finestra e' misurata da [[misura-trait.py]]: nome **26** caratteri, effetto
**65**, riga sola **86** (meno i 6 di `[Feat]`). Courier New a corpo 12, 7 px.

## Le due regole di forma

⭐ **I nomi dei talenti sono SOSTANTIVI**, non aggettivi. Lo dice gia'
`glossario.md` per `Luck`/`Unlucky` → «Fortuna»/«Sfortuna»: *«Sfortunato»
vorrebbe il genere di chi lo subisce*, e il genere del giocatore non si conosce.
Quindi `Lucky` → «Fortuna», `Ambidextrous` → «Ambidestria», `Saint` →
«Santita'», `Independent` → «Indipendenza».

⭐ **I marcatori fra quadre usano i nomi che il gioco usa altrove**: `[Stamina+]`
diventa `[SP+]` perche' e' cosi' che li chiama `skill.hsp:620`, e la barra a
schermo dice SP. In prosa invece 「スタミナ」 e' «vigore» (`proc.hsp:10642`).

⚠️ Il nome porta a schermo anche `(MAX)` o `(requirement)`, che il dizionario
non vede: sono altri 5 o 13 caratteri sulla stessa riga.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

LOTTO = 'lavoro/_trait.jsonl'

RESE = {
    (11, 'Short Distance Runner'): 'Velocista',
    (11, 'Middle Distance Runner'): 'Mezzofondista',
    (11, 'Long Distance Runner'): 'Fondista',
    (13, 'Years of training strengthens your stamina.'):
        'Anni di allenamento rafforzano il tuo vigore.',
    (13, 'You have good stamina. [Stamina+]'): 'Hai un buon vigore. [SP+]',
    (13, 'You have very good stamina. [Stamina++]'): 'Hai molto vigore. [SP++]',
    (13, 'You have outstanding stamina. [Stamina+++]'):
        'Il tuo vigore è formidabile. [SP+++]',
    (22, 'Vampiric Ability'): 'Capacità vampirica',
    (24, 'Your vampire friend teaches you how to suck blood.'):
        'Un amico vampiro ti insegna a succhiare il sangue.',
    (24, 'You can suck blood now.'): 'Sai succhiare il sangue.',
    (36, 'Natural Leader'): 'Guida naturale',
    (38, 'You find how to strengthen your allies for a short time.'):
        'Scopri come rinforzare gli alleati per un poco.',
    (38, 'You can temporally strengthen your allies.'):
        'Puoi rinforzare gli alleati per un poco.',
    (50, 'Knockout'): 'Stordimento',
    (52, 'You find how to stun enemy without killing.'):
        'Scopri come stordire un nemico senza ucciderlo.',
    (52, 'You can attack it easy on the enemy.'): 'Puoi colpire senza uccidere.',
    (64, 'Magic Eye'): 'Occhio magico',
    (66, 'You are subjected to the magic in the eyes by the ritual.'):
        'Un rito ti ha messo la magia negli occhi.',
    (66, 'Your eye is harboring the magic of mystery.'):
        'Il tuo occhio cova una magia misteriosa.',
    (78, 'Magical plant knowledge'): 'Piante magiche',
    (80, 'You learned how to summon magical plants from this note.'):
        'Da un appunto impari a evocare piante magiche.',
    (80, 'You can summon and manipulate magical plants.'):
        'Puoi evocare e guidare piante magiche.',
    (92, 'Dimensional Move'): 'Salto dimensionale',
    (94, 'You hit upon an idea of insta-teleport from a dream.'):
        'Da un sogno ti viene il lampo del salto istantaneo.',
    (94, 'You can insta-teleport to nearby tiles.'):
        'Puoi saltare di colpo a un riquadro vicino.',
    (106, 'Fire Breath'): 'Soffio di fuoco',
    (108, 'Too much drinking makes you want to breath fire.'):
        'Hai bevuto tanto da voler sputare fuoco.',
    (108, 'You can breath fire.'): 'Puoi sputare fuoco.',
    (120, 'Hypnotism'): 'Ipnosi',
    (122, 'Suddenly, you know how to make everyone sleep.'):
        'Di colpo sai come far addormentare chiunque.',
    (122, 'You can hypnotize single target.'): 'Puoi ipnotizzare un bersaglio.',
    (134, 'Poison Nail'): 'Unghia velenosa',
    (136, 'Researching poisons leads you to a method to poison others.'):
        'Studiando i veleni trovi il modo di avvelenare.',
    (136, 'You can poison a creature.'): 'Puoi avvelenare una creatura.',
    (148, 'Sexy Dance'): 'Danza seducente',
    (150, 'You learn a sexy dance.'): 'Impari una danza seducente.',
    (150, 'Your dance is very attractive.'): 'La tua danza attira parecchio.',
    (162, 'Uncontrollable power'): 'Potere incontrollato',
    (164, 'Swayed by the mystery power that lurks within.'):
        'Ti scuote un potere misterioso che ti sta dentro.',
    (164, 'You have hidden something that can not be controlled.'):
        'Dentro di te si nasconde qualcosa che non si governa.',
    (176, 'Apprentice Accountant'): 'Contabile apprendista',
    (176, 'Expert Accountant'): 'Contabile esperto',
    (178, 'Working as an accountant reduces your tax payment.'):
        'Fare il contabile ti abbassa le tasse.',
    (178, 'You are good at calculating taxes. [TAX-7%]'):
        'Sai fare i conti delle tasse. [TASSE-7%]',
    (178, 'You are very good at calculating taxes. [TAX-15%]'):
        'Sei una volpe coi conti delle tasse. [TASSE-15%]',
    (187, 'Apprentice Quartermaster'): 'Furiere apprendista',
    (187, 'Expert Quartermaster'): 'Furiere esperto',
    (189, 'Working as a quartermaster gives you better payoff.'):
        'Fare il furiere ti procura forniture migliori.',
    (189, 'You sometimes receive quality supplies.'):
        'Ogni tanto ricevi forniture di qualità.',
    (189, 'You frequently receive quality supplies.'):
        'Ricevi spesso forniture di qualità.',
    (198, 'Exorcist'): 'Esorcismo',
    (200, 'Your prayer weakens the power of cursed whisperings.'):
        'La tua preghiera fiacca i sussurri maledetti.',
    (200, 'Your prayer nullifies cursed whisperings.'):
        'La tua preghiera annulla i sussurri maledetti.',
    (209, 'Independent'): 'Indipendenza',
    (211, 'To the very end, you only believe in your own power.'):
        'Fino in fondo, credi solo nelle tue forze.',
    (211, 'You prefer to work alone. [SPD+20% when alone]'):
        'Preferisci fare da solo. [VEL+20% da solo]',
    (220, 'Mount Bond'): 'Intesa con la cavalcatura',
    (222, "By mounting horses, you learned to follow your mount's rhythm."):
        'A furia di cavalcare hai preso il ritmo della cavalcatura.',
    (222, 'You know how to handle weapons while riding. [Lowers to-hit penalty while riding]'):
        'Sai usare le armi in sella. [Meno malus a colpire in sella]',
    (231, 'Bomber'): 'Bombarolo',
    (233, 'You analyzed mana-bombs, learnt to convert your mana into explosions.'):
        'Studiando le bombe di mana impari a farlo esplodere.',
    (233, 'You can transform your mana into explosions.'):
        'Puoi trasformare il mana in esplosioni.',
    (245, 'Gravity Control'): 'Controllo della gravità',
    (247, 'Your genes allow you to manipulate gravity.'):
        'I tuoi geni ti fanno piegare la gravità.',
    (247, 'You manipulate gravity.'): 'Pieghi la gravità.',
    (259, 'Jiu-jitsu'): 'Jujitsu',
    (261, 'You have been taught martial arts by a mysterious old man.'):
        'Un vecchio misterioso ti ha insegnato le arti marziali.',
    (261, 'You have mastered Jiu-jitsu.'): 'Padroneggi il jujitsu.',
    (273, 'Magnetic Manipulate'): 'Controllo magnetico',
    (275, 'As a result of body modification, you can manipulate magnetic force.'):
        'Un innesto ti fa piegare la forza magnetica.',
    (275, 'You manipulate magnetic force.'): 'Pieghi la forza magnetica.',
    (287, 'Shield Bash'): 'Colpo di scudo',
    (289, 'Mastering shields increased the power of your shield bashing.'):
        'Padroneggiare lo scudo rende il tuo colpo più duro.',
    (289, 'You can shield bash more effectively.'):
        'Il tuo colpo di scudo rende di più.',
    (302, 'Gentle Face'): 'Volto gentile',
    (304, "Your smile makes it easier to raise one's friendliness and obedience."):
        'Il tuo sorriso rende più facile farsi voler bene.',
    (304, 'Your smile reassures others.'): 'Il tuo sorriso rassicura gli altri.',
    (313, 'Ambidextrous'): 'Ambidestria',
    (313, 'Improved Ambidextrous'): 'Ambidestria evoluta',
    (315, 'Years of training increases your two weapon fighting skill.'):
        'Anni di allenamento migliorano la doppia arma.',
    (315, 'You can handle multiple weapons. [Dual Wield+4]'):
        'Sai maneggiare più armi. [Doppia arma+4]',
    (315, 'You mastered multiple weapon style. [Two Wield+8]'):
        'Padroneggi il duello a due armi. [Doppia arma+8]',
    (328, 'Conquer Darkness'): 'Dominio del buio',
    (328, 'Conquer Deep Darkness'): 'Dominio del buio fitto',
    (330, 'Living in darkness makes you resistant to darkness.'):
        'Vivere al buio ti rende resistente al buio.',
    (330, "You don't fear darkness. [RES Darkness+]"):
        'Non temi il buio. [RES Buio+]',
    (330, 'You can dance in darkness. [RES Darkness++]'):
        'Nel buio ci balli. [RES Buio++]',
    (340, 'Poison Tolerance'): 'Tolleranza al veleno',
    (340, 'More Poison Tolerance'): 'Gran tolleranza al veleno',
    (342, 'Being a taster for a noble grants you resistance to poison.'):
        "Fare l'assaggiatore di un nobile insegna a reggere il veleno.",
    (342, 'You have a tolerance to poison. [RES Poison+]'):
        'Reggi il veleno. [RES Veleno+]',
    (342, 'You have a strong tolerance to poison. [RES Poison++]'):
        'Reggi bene il veleno. [RES Veleno++]',
    (352, 'Empathy'): 'Empatia',
    (354, 'You learn the skill to understand and respond to enemy thoughts.'):
        'Impari a capire e a rispondere ai pensieri altrui.',
    (354, 'Your words resonate within their hearts.'):
        'Le tue parole risuonano nei loro cuori.',
    (369, 'Saint'): 'Santità',
    (371, 'Training under a priest has taught you sacred skills.'):
        'Un sacerdote ti ha insegnato le arti sacre.',
    (371, 'You wield divine power.'): 'Maneggi un potere divino.',
    (383, 'Lucky'): 'Fortuna',
    (383, 'Incredibly Lucky'): 'Gran fortuna',
    (383, 'Goddess of Luck'): 'Dea della fortuna',
    (385, 'Sighting a falling star brings you luck.'):
        'Vedere una stella cadente ti porta fortuna.',
    (385, 'You are lucky'): 'La fortuna ti accompagna',
    (385, 'You can rely on a good dose of luck.'):
        'Puoi contare su una bella dose di fortuna.',
    (385, 'The goddess of luck smiles upon you.'):
        'La dea della fortuna ti sorride.',
    (395, 'Apprentice Ascetic'): 'Asceta apprendista',
    (395, 'Journeyman Ascetic'): 'Asceta provetto',
    (395, 'Expert Ascetic'): 'Asceta esperto',
    (395, 'Master Ascetic'): 'Asceta maestro',
    (395, 'Legendary Ascetic'): 'Asceta leggendario',
    (397, 'Being an ascetic increases your HP.'):
        'La vita da asceta ti alza i PV.',
    (397, 'You are an apprentice ascetic. [HP+5%]'):
        'Sei asceta apprendista. [HP+5%]',
    (397, 'You are a journeyman ascetic. [HP+10%]'):
        'Sei asceta provetto. [HP+10%]',
    (397, 'You are an expert ascetic. [HP+15%]'):
        'Sei asceta esperto. [HP+15%]',
    (397, 'You are a master ascetic. [HP+20%]'):
        'Sei asceta maestro. [HP+20%]',
    (397, 'You are a legendary ascetic. [HP+25%]'):
        'Sei asceta leggendario. [HP+25%]',
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
