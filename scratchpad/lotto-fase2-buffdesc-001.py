# -*- coding: utf-8 -*-
"""Lotto fase2-buffdesc-001: i 63 buffdesc di buff.hsp.

Chiave (riga, en) come dal lotto 041: l'inglese e' ASCII e non si sbaglia a
copiarlo. Le cinque reti del metodo sono in fondo.
"""
import glob, io, json, collections

RESE = {
    # --- crescita degli attributi (dinamiche)
    (301, 'Increases  growth rate by %'):
        '"Crescita di " + skillname(calcbuff_buffid - BUFF_GROW_STRENGTH + SKILL_ATTR_STR) + " +" + locvar_calcbuff_p + "%"',
    (316, 'Increases rate of skill growth by %'):
        '"Crescita di ogni abilità +" + locvar_calcbuff_p + "%"',

    # --- benedizioni
    (331, 'PV +10% and +/Shield +20%/RES+ fear'):
        '"PV +10% e +" + locvar_calcbuff_p + "/Scudo +20%/Res+ terrore"',
    (350, 'Decreased success rate of spellcasting'):
        'Meno riuscita degli incantesimi',
    (364, 'Enhances regeneration/RES+ chills'):
        'Più recupero HP e SP/Res+ tremore',
    (379, 'Enhances regeneration hard'):
        'Gran recupero HP',
    (393, 'RES+ fire,cold,lightning,mind,nerve,nether,poison,sound,chaos,darkness'):
        'Res+ fuoco,gelo,fulmine,oscurità,mente,veleno,oltretomba,suono,nervi,caos',
    (416, 'RES+ magic'):
        'Res+ magia',
    (430, 'Recovery every turn/RES+ fire'):
        'Cura HP e stati ogni turno/Res+ fuoco',
    (445, 'Increases Tact/MagCtl/Cast /Add magic to attack'):
        '"Tattica/Controllo magia/Incantesimi +" + locvar_calcbuff_p + "/Magia ai colpi fisici"',
    (461, 'Increases STR & PER/Magic Reflection'):
        'Più For e Per/Riflette magia',
    (477, 'Increases DEX & MAG/RES+ magic'):
        'Più Des e Mag/Res+ magia',
    (493, 'Increases Speed & DV/Immunity to Speed reduction'):
        'Più Vel e DV/Ignora i rallentamenti',
    (511, 'Increases CON & PV/Amplified Healing/Chance to nullify damage'):
        'Più Cos, PV e cure/Annulla più danni',
    (530, 'Attribute bonus & RES+ magic/Consumes HP & MP/Negates gauge depletion'):
        'Più attributi/Res+ magia/Consuma HP e MP/Barra ferma',
    (551, 'Run through and riding attack'):
        'Sfonda e danneggia (equitazione)',
    (568, 'Attack +10%/Defense +5%/Speed +'):
        '"Attacco +10%/Difesa +5%/Velocità +" + locvar_calcbuff_p',
    (591, 'Speed +'):
        '"Velocità +" + locvar_calcbuff_p',
    (611, 'Speed Decrease by %'):
        '"Velocità -" + locvar_calcbuff_p + "%"',
    (632, 'STR & DEX +10% and +/RES+ fear,confusion'):
        '"For e Des +10% e +" + locvar_calcbuff_p + "/Res+ terrore,confusione"',
    # ⚠️ l'inglese sbaglia due volte: il codice (buff.hsp:660-668) alza SETTE
    # attributi di +p (non del 10%), azzera il terrore e alza la resistenza
    # alla MAGIA, non alla confusione. Arbitra il giapponese, confermato dal codice.
    (656, 'Increases attribute by 10% and /RES+ fear,confusion'):
        '"7 attributi +" + locvar_calcbuff_p + "/Res+ terrore/Più Res magia"',
    (679, 'Enhance shooting by equipped skill/Immobility'):
        "Tiro e mira con l'arma/Immobilità",
    (693, 'Makes it easier to increase analysis rate/Expends stamina each turn'):
        '[-SP a turno] Analisi cresce prima',
    # copiata: stesso giapponese di skill.hsp:1241, gia' reso
    (707, 'Throwing reinforced with meditation/MP expend'):
        'Lancio x1,5 [-MP per lancio]',
    (721, 'Partially invalidates reduction effects/RES+ poison'):
        'Annulla in parte i cali/Res+ veleno',
    (735, 'Cancels stamina reduction'):
        'Gli SP non calano',
    (752, 'CON & CHR +10% and +/RES+ paralyze,blind'):
        '"Cos e Car +10% e +" + locvar_calcbuff_p + "/Res+ paralisi,cecità"',
    (776, 'Averaging'):
        'Attributi pareggiati',
    (801, 'PER & WIL +10% and +/RES+ sleep,confusion'):
        '"Per e Vol +10% e +" + locvar_calcbuff_p + "/Res+ sonno,confusione"',

    # --- maledizioni
    (825, 'PER and WIL -20%, Casting chance -3%'):
        'Per e Vol -20%/Riuscita incantesimi -3%',
    (845, 'Skip turn with 10% chance/Diminishes power gauge'):
        '10% di saltare il turno/Barra cala',
    (859, 'Increase rate of hunger and thirst'):
        'Più fame e più sete',
    (873, 'Weakened by Poison and Erosion'):
        'Veleno ed erosione indeboliscono',
    (886, 'Reduced ATK and DEF'):
        'Più danni subiti/Meno danni inflitti',
    (902, 'RES- fire,cold,lightning/Inhibits regeneration'):
        'Res- fuoco,gelo,fulmine/Blocca il recupero',
    (919, 'HexProtect(power: )/RES+ wince/RES+ erosion'):
        '"Protezione dai malus " + locvar_calcbuff_p + "/Res+ esitazione,erosione"',
    (933, 'RES- mind,nerve,nether,poison,sound,chaos,darkness'):
        'Res- oscurità,mente,veleno,oltretomba,suono,nervi,caos',
    (957, 'LER & MAG +10% and +/Literacy +10% and +'):
        '"App e Mag +10% e +" + locvar_calcbuff_p + "/Lettura +10% e +" + locvar_calcbuff_p(1)',
    (983, 'Speed, PV and DV -20%'):
        'DV, PV e Velocità -20%',
    (1006, 'Speed +20% and +'):
        '"Velocità +20% e +" + locvar_calcbuff_p',
    (1020, 'Disguise'):
        'Travestimento',
    (1034, 'Receives 9999 damage when the curse ends'):
        '9999 danni quando la maledizione si compie',
    (1049, 'Speed & Attributes +'):
        '"Velocità e attributi +" + locvar_calcbuff_p',
    (1067, 'Cooperation chance/interrupt resist for performance-type skills'):
        'Analisi aiuta la trattativa/Res+ interruzione',
    (1081, '% chance of nullifying lethal damage'):
        '"Una volta, " + locvar_calcbuff_p + "% di annullare il danno letale"',
    (1096, 'Increases Attributes'):
        'Più attributi',
    (1115, 'Increases MAG/Alchemy damage added to Hand-skills'):
        'Più Mag/Alchimia ai colpi di mano',
    (1130, 'Enhances Eye of Mind/HP, MP and Gauge absorption added to Eye-skills'):
        'Più Occhio della mente/Sguardi: assorbe Barra, HP, MP',
    (1145, 'Fluctuating Attributes/RES+ fear'):
        'Attributi instabili/Res+ terrore',
    (1165, 'Luck +'):
        '"Fortuna +" + locvar_calcbuff_p',
    (1180, 'Luck -666'):
        'Fortuna -666',
    # ⚠️ l'inglese perde il 軽装備20%上昇 del giapponese, che il codice conferma
    # (buff.hsp:1205, Farsetto * 12 / 10)
    (1195, 'DV +10% and +/Float/RES+ Gravity'):
        '"DV +10% e +" + locvar_calcbuff_p + "/Farsetto +20%/Res+ gravità/Levitazione"',
    (1216, 'Strengthens Physical/Magical/Breath damage for one attack'):
        'Una volta, più danno fisico/magico/soffio',
    (1230, 'Light equipment prevents criticals/Small physical damage reduction'):
        '[Armatura leggera] Nessun critico/Meno danno fisico',
    (1244, 'Medium equipment increases magical power/Magic damage reduction'):
        '[Armatura media] Più potenza magica/Meno danno magico',
    (1258, 'Heavy equipment reduces physical damage taken/No weight hit penalty/RES+ dim'):
        '[Armatura pesante] Meno danno fisico/Nessuna penalità da peso/Res+ stordimento',
    (1272, 'Parry and overturn the attacker when equipped with a shield'):
        '[Scudo] Para il colpo e atterra chi attacca',
    (1286, 'Increase Evasion with Tactics & Greater Evasion, counterattack when evading'):
        'Contrattacca schivando/Schivata su Tattica e Intuito',
    # copiata: stesso concetto di skill.hsp:1237, gia' reso
    (1301, 'Add most resistant element damage to martial arts'):
        'Elemento ai colpi a mani nude',
    # ⚠️ il giapponese dice «certe abilita'», l'inglese le nomina e il codice
    # (buff.hsp:1319-1322) conferma che sono quelle quattro; la barra la porta
    # solo il giapponese. La resa tiene tutt'e due le meta'.
    (1315, 'Increases Magic Device, Throw, Alchemy, Literacy'):
        'Più Dispositivi magici, Lancio, Alchimia, Lettura/Barra+ con certi oggetti',
    # copiata: stesso concetto di skill.hsp:1253, gia' reso
    (1333, 'Takes damage in place of an ally'):
        'Prende i danni degli alleati',
    (1347, 'Prevent teleport/Increases speed/Halve insane'):
        'Blocca il teletrasporto/Più Vel/Follia dimezzata',
    (1362, 'Increases skill level/RES+ brainwash'):
        'Più valore alle abilità/Res+ plagio',
}

USCITA = 'lavoro/fase2-buffdesc-001.jsonl'

voci = [json.loads(l) for l in io.open('lavoro/_buff.jsonl', encoding='utf-8') if l.strip()]

errori = []

# --- rete 0: la chiave identifica una voce sola
conta = collections.Counter((v['riga'], v['en']) for v in voci)
for k, n in conta.items():
    if n > 1:
        errori.append(f'rete 0: la chiave {k} identifica {n} voci, non una')

# --- rete 1: nessuna voce senza resa
indice = {(v['riga'], v['en']): v for v in voci}
for v in voci:
    if (v['riga'], v['en']) not in RESE:
        errori.append(f"rete 1: voce senza resa -> riga {v['riga']}  en={v['en']!r}")

# --- rete 2: nessuna resa che non aggancia niente
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti 0-2')

# --- rete 3: divergenza da una resa gia' decisa per lo stesso giapponese
#     ⚠️ stampa, non uccide: puo' essere sbagliata la resa vecchia.
gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.split('\\')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))

for v in voci:
    resa = RESE[(v['riga'], v['en'])]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it != resa:
            print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
                  f"      qui      {resa!r}\n"
                  f"      {nome}:{riga}  {it!r}")

# --- rete 4: nessun giapponese reso in due modi DENTRO il lotto
per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[v['jp']].add(RESE[(v['riga'], v['en'])])
for jp, rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} reso in {len(rese)} modi dentro il lotto: {rese}')

# --- scrittura
with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')

print(f'{len(voci)} voci scritte in {USCITA}')
