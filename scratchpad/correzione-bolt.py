# -*- coding: utf-8 -*-
"""Corregge in `db_item.hsp` i 15 nomi di «bolt», da «dardo» a «saetta».

⚠️ Il dizionario aveva DUE rese per la stessa magia: `skill.hsp` (i nomi di
incantesimo, quelli che il giocatore sceglie dalla lista di lancio) diceva
«Saetta di gelo», `db_item.hsp` (i nomi di libro e di bacchetta) diceva «dardo di
ghiaccio». Il giocatore compra il libro del «dardo» e impara la «saetta»: sono la
stessa magia con due nomi.

⚠️ E il disaccordo non era solo nella testa: **cinque nomi su dodici avevano
anche il qualificatore diverso** — 冷気 «gelo»/«ghiaccio», 暗黒
«d'oscurita'»/«oscuro», 毒 «velenosa»/«di veleno», 神経 «dei nervi»/«neurale»,
魔法 «magica»/«arcano». Non bastava sostituire una parola.

Vince `skill.hsp`, per due motivi: e' la lista che il giocatore apre a ogni
lancio (il libro lo legge una volta), e i suoi 12 nomi sono gia' fra loro
coerenti. Le rese qui sono le sue, con l'iniziale minuscola perche' i nomi di
oggetto di `db_item.hsp` non sono maiuscoli.

⚠️ ⚠️ **LA PRIMA PASSATA ERA INCOMPLETA**, ed e' il motivo per cui questo script
cerca per INGLESE e non per giapponese. Cercando 「ボルト」 nel giapponese si
trovano i 12 **libri**, ma non le 3 **bacchette**: quelle hanno un nome
giapponese poetico che il katakana non contiene affatto — 稲妻の軌跡 «la scia
della folgore», 炎の衝撃 «l'urto della fiamma», 氷の視線 «lo sguardo del gelo» — e
solo l'inglese le chiama `lightning bolt`, `fire bolt`, `ice bolt`. Sono la
stessa magia in mano al giocatore, e dicevano ancora «dardo». Qui la misura
giusta e' sull'inglese, perche' e' la lingua che nomina l'effetto; il giapponese
nomina l'oggetto. 💡 Nota per il futuro: i nomi giapponesi delle bacchette sono
belli e sono andati persi gia' prima di questa correzione (泡沫の波動 e' reso
«sfera di bolle», che viene da `bubble ball`). Non lo cambia questo script.

⚠️ E due voci con «dardo» NON vanno toccate, perche' non sono questa famiglia:
`db_item.hsp:146183` («bolt» = i dardi da balestra, tutt'altro oggetto) e
`db_item.hsp:151150` («magic missile», che e' 魔法の矢 / `Magic Dart`, gia'
«Dardo magico» in `skill.hsp:479` — un'altra magia).

⚠️ «saetta» e' FEMMINILE dove «dardo» era maschile, quindi cambiano tre campi e
non uno: `it`, `plurale` e `genere`. Il `genere` qui non muove l'articolo
dell'oggetto — `applica.ARTICOLO_DI` lo mette **solo sulla testa**, che per questi
e' `ioriginalnameref2` («grimorio», «bacchetta») — ma il dato dev'essere vero
comunque, perche' e' il dizionario a dichiararlo e non si deduce. Il `plurale`
invece viaggia su tutti i siti e va rifatto al femminile.

⚠️ Questa divergenza `--divergenti` non l'avrebbe mai vista: misurato nella 29ª,
`rese_gia_decise()` apre `db_creature.hsp` e basta.

Lo script e' ripetibile: una voce gia' corretta si salta.
"""
import io, json

# (riga, en) -> (it, plurale). Le rese sono quelle di skill.hsp, in minuscolo.
CORREZIONI = {
    # --- i 12 libri (giapponese ...ボルトの魔法書)
    (152349, 'ice bolt'):       ('saetta di gelo',        'saette di gelo'),
    (152334, 'fire bolt'):      ('saetta di fuoco',       'saette di fuoco'),
    (152319, 'lightning bolt'): ('saetta di fulmine',     'saette di fulmine'),
    (149160, 'darkness bolt'):  ("saetta d'oscurità",     "saette d'oscurità"),
    (149145, 'mind bolt'):      ('saetta mentale',        'saette mentali'),
    (135057, 'nether bolt'):    ("saetta d'oltretomba",   "saette d'oltretomba"),
    (135072, 'poison bolt'):    ('saetta velenosa',       'saette velenose'),
    (135087, 'sound bolt'):     ('saetta sonora',         'saette sonore'),
    (135102, 'chaos bolt'):     ('saetta caotica',        'saette caotiche'),
    (135117, 'nerve bolt'):     ('saetta dei nervi',      'saette dei nervi'),
    (143126, 'magic bolt'):     ('saetta magica',         'saette magiche'),
    (138035, 'hydro bolt'):     ("saetta d'acqua",        "saette d'acqua"),
    # --- le 3 bacchette, che il giapponese chiama in un altro modo
    (150425, 'lightning bolt'): ('saetta di fulmine',     'saette di fulmine'),
    (151105, 'fire bolt'):      ('saetta di fuoco',       'saette di fuoco'),
    (151120, 'ice bolt'):       ('saetta di gelo',        'saette di gelo'),
}

P = 'dizionario/db_item.hsp.jsonl'
righe = [json.loads(l) for l in io.open(P, encoding='utf-8') if l.strip()]

# rete 1: le rese di skill.hsp devono esistere davvero e coincidere con queste,
# se no si sta allineando a un bersaglio immaginario.
skill = {}
for l in io.open('dizionario/skill.hsp.jsonl', encoding='utf-8'):
    if not l.strip():
        continue
    d = json.loads(l)
    if (d.get('it') or '').startswith('Saetta'):
        skill[d['it'].lower()] = d['riga']
mancanti = sorted({it for it, _ in CORREZIONI.values()} - set(skill))
if mancanti:
    raise SystemExit(f'rete 1: queste rese non esistono in skill.hsp -> {mancanti}')

# rete 2: nessuna voce di db_item il cui inglese contiene «bolt» deve restare
# fuori dall'elenco, tranne le due dichiarate estranee. E' la rete che sarebbe
# servita alla prima passata, che cercava per giapponese e ne perdeva tre.
ESTRANEE = {
    (146183, 'bolt'),          # i dardi da balestra: altro oggetto
    (151150, 'magic missile'), # 魔法の矢 / Magic Dart, altra magia
}
tutte_bolt = {(d['riga'], d.get('en')) for d in righe
              if 'bolt' in (d.get('en') or '').lower()}
scoperte = tutte_bolt - set(CORREZIONI) - ESTRANEE
if scoperte:
    raise SystemExit(f'rete 2: voci con «bolt» non elencate -> {sorted(scoperte)}')

fatte, saltate, viste = 0, 0, set()
for d in righe:
    k = (d['riga'], d.get('en'))
    if k not in CORREZIONI:
        continue
    viste.add(k)
    it, plurale = CORREZIONI[k]
    if d.get('it') == it:
        saltate += 1
        continue
    # rete 3: si corregge solo quello che dice ancora «dardo»
    if not (d.get('it') or '').startswith('dardo'):
        raise SystemExit(f"rete 3: {k} non dice «dardo» ne' e' gia' corretta, "
                         f"ma {d.get('it')!r}: e' la voce sbagliata")
    print(f"{d['riga']:<8d} {d['it']:<22s} -> {it:<22s}  "
          f"({d.get('plurale')} -> {plurale}, {d.get('genere')} -> f)")
    d['it'], d['plurale'], d['genere'] = it, plurale, 'f'
    fatte += 1

if len(viste) != len(CORREZIONI):
    raise SystemExit(f'rete 4: {len(CORREZIONI) - len(viste)} correzioni non hanno '
                     f'agganciato nessuna voce -> {sorted(set(CORREZIONI) - viste)}')

with io.open(P, 'w', encoding='utf-8', newline='\n') as f:
    for d in righe:
        f.write(json.dumps(d, ensure_ascii=False) + '\n')
print(f'--- {fatte} nomi corretti, {saltate} gia\' a posto, su {len(CORREZIONI)} in {P}')
