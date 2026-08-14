# -*- coding: utf-8 -*-
"""Lotto fase4-proc-020: necromanzia, incitamento, taglialegna, spazzolatura e
coccole (proc.hsp 21000-21999).

55 rese, nessuna rinviata. `proc.hsp` passa a 893 su 1.098 (81%). E' il lotto
piu' grosso mai fatto su questo file.

⚠️⚠️ **`:21110` interpola `tc` NUDO, cioe' il numero della creatura dove va il
nome.** E' una classe nuova di errore di monte — non il personaggio sbagliato,
ma **nessun personaggio**:

```hsp
stxt cc, lang(name(cc) + "は" + name(tc) + "を道連れに自爆した。",
              name(cc) + " explode with " + tc + ".")
```

`tc` e' l'**indice** nell'array dei personaggi: a schermo la build inglese
stampa «... explode with 37.» Il giapponese scrive `name(tc)`, com'e' giusto.
⚠️ **Ma la rete 11 non lascia rimediare**: pretende che le funzioni di contenuto
coincidano con quelle dell'inglese, e l'inglese qui ha **un** `name()` dove il
giapponese ne ha due. La resa nomina chi si fa esplodere e lascia il bersaglio
implicito. 💡 **E' un candidato a toppa**, non a traduzione: la riga andrebbe
corretta `+ tc +` → `+ name(tc) +`, e allora la resa potrebbe nominarli tutt'e
due. Registrato qui perche' nessuno se ne accorga di nuovo da capo.

⚠️ **`:21572` e' un altro copia-e-incolla**: il giapponese dice
「決意を固めた！」 (si fa forza, e infatti il codice sotto **riempie la barra**),
l'inglese ricopia « is excited!» da `:21206`, che sta trecento righe sopra e
dice un'altra cosa. Reso sul giapponese. La serie degli errori di monte sale a
**ventuno**.

⚠️ **`:21991` e `:21994` sono la stessa cosa una terza volta**: due giapponesi
opposti — 「お小遣いあげちゃう！」 (ti do la paghetta, PNG amichevole) e
「ひ、卑怯だ！」 (c-che colpo basso!, PNG ostile) — sotto **un inglese solo**,
che tiene la prima e perde la seconda. Il ramo lo sceglie
`cdata(CDATA_RELATION, tc)`. Resi sul giapponese; la rete 13 li ha pescati.

⚠️ **Dieci rese sono CODE di frase: il nome sta fuori da `lang()`.**
`:21853`-`:21869`, `:21893` e `:21935` sono scritte
`txt name(tc) + lang("...", " ...")`, quindi la resa **comincia con uno spazio**
e deve incastrarsi dopo un nome che porta gia' il suo articolo. E `:21893`,
`:21907`, `:21919` e `:21935` sono `txt A, B, C` — **alternative scelte a caso**,
non una frase in tre pezzi: ognuna dev'essere completa da sola.

⚠️ **Sei rese sono state girate per la rete 8, e una l'ha fermata davvero**:
`:21096` era scritta «la forza vitale **di** " + name(tc)», che a schermo avrebbe
dato «di il putit». Girata mettendo il nome come **complemento oggetto** —
«prosciuga X della forza vitale». Le altre cinque erano state girate prima di
scriverle. La piu' stretta e' `:21935`, che ha la forma fissa
`name(tc) + A + name(cc) + B`: il secondo nome sta **in mezzo** e non lo si puo'
spostare. Qualunque preposizione
davanti («si stringe **a** X», «cerca il fianco **di** X») si fonde con
l'articolo che `name()` porta dentro. La via d'uscita e' un **verbo
transitivo**: «e trova X lì accanto».

⚠️ **E `verifica` ha fermato le stesse cinque code per un secondo motivo**:
portano una battuta fra **virgolette**, e in una statica una `"` nuda
chiuderebbe in anticipo la stringa HSP che scrive `applica.py`. Vanno protette
`\\"`, come fa l'inglese di monte. E' la prima volta che capita in questo file —
finora le battute passavano da `cnvtalk()`, che le virgolette le mette da se'.

💡 **`_impression3` e `_impression4` sono gia' italiane.** Stanno in
`text.hsp:44-45` come array di `lang()`, e quel file e' chiuso: restituiscono
frasi intere («Sembra dare carne di ottima qualita'»). Quindi le quattro rese
che le ospitano sono **prefissi con due punti**, non frasi da completare —
`"Effetto allevatore: " + _impression3(...) + "."` — ed e' il motivo per cui la
rete 11 pretende `_impression3` e `cdata` dentro la resa.

💡 **`:21540` e' una copia**: stesso giapponese di `proc.hsp:17744`, fatto nel
lotto 018, e stesse parole («non ha nessuno accanto...») su una funzione diversa
(`name` invece di `cdatan`).

⚠️ **`:21206` fara' gridare la rete 3, ed e' legittimo.** Lo stesso giapponese
「は興奮した！」 e' gia' reso a `proc.hsp:10084` come «Ti sale l'eccitazione!»,
ma quello e' l'inglese «You are excited!», cioe' la **seconda persona** rivolta
al giocatore; qui l'inglese e' « is excited!» col nome. Due persone
grammaticali della stessa frase, e la differenza **la impone il sorgente**. La
resa la tiene riconoscibile: «name(tc) + " sente salire l'eccitazione!"».
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- il necromante e i suoi non morti.
    (21026, "'s eyes come back to normal."):
        'name(tc) + " ha di nuovo lo sguardo di sempre."',
    (21030, "'s eyes began to shine omniously."):
        'name(tc) + " ha gli occhi che mandano un bagliore sinistro."',
    # le due intestazioni *...*: spazio davanti e dietro, come l'inglese
    (21090, ' *Necro Charge* '):
        ' *Furia dei morti* ',
    (21091, ' strengthens those under  control.'):
        'name(cc) + " rinforza le proprie pedine."',
    (21095, ' *HP Drain* '):
        ' *Sfruttamento* ',
    # ⚠️ fermata dalla rete 8: «la forza vitale di » + name() si fonde.
    #    Il nome diventa complemento oggetto e la forza vitale un secondo caso.
    (21096, " has absorbed 's vitality."):
        'name(cc) + " prosciuga " + name(tc) + " della forza vitale."',
    # ⚠️ l'inglese interpola `tc` NUDO, cioe' un numero. Vedi la nota in cima:
    #    la rete 11 concede un name() solo, e va a chi si fa esplodere.
    (21110, ' explode with .'):
        'name(cc) + " si fa esplodere per trascinarsi dietro il bersaglio."',

    # --- Incitamento (skill.hsp, SKILL_SPACT_CHEER).
    (21176, ' cheer.'):
        'name(cc) + " incita i compagni."',
    # ⚠️ stesso giapponese di proc.hsp:10084, ma li' e' la seconda persona
    (21206, '  excited!'):
        'name(tc) + " sente salire l\'eccitazione!"',
    # «di name(cc)» si fonderebbe: il nome diventa soggetto
    (21241, 'Dynamic cheers of  echoed all around.'):
        'name(cc) + " scatena un tifo che risuona tutt\'intorno."',
    (21328, 'It feels sneaky...'):
        'Sarebbe un colpo basso...',
    (21390, 'Force is not enough...'):
        'La forza non basta...',
    (21506, ' encouraged the cognate.'):
        'name(cc) + " chiama a raccolta i propri simili."',
    # copiata da proc.hsp:17744 (lotto 018), stesso giapponese
    (21540, '  all alone.'):
        'name(cc) + " non ha nessuno accanto..."',
    # ⚠️ reso sul giapponese: l'inglese ricopia la riga di :21206, e il codice
    #    sotto riempie la barra, non eccita nessuno
    (21572, '  excited!'):
        'name(tc) + " si fa forza!"',
    (21606, ' disturbed .'):
        'name(cc) + " manda in confusione " + name(tc) + "."',

    # --- il taglialegna.
    (21634, 'You can not find a tree.'):
        'Non c\'è nessun albero da abbattere.',
    (21658, 'You have no item that can cut trees.'):
        'Non hai un attrezzo per abbattere alberi.',
    (21710, "It doesn't seem to be especially necessary."):
        'Non sembra che ce ne sia bisogno.',

    # --- la spazzolatura del bestiame.
    (21804, " says: Just where do you think you're putting those perverted hands of yours?! Stop this at once!"):
        'cdatan(CDATAN_NAME, cnt) + " dice: " + cnvtalk("Ma che modi sono?! Giù quelle mani, che roba!")',
    # ⚠️ «su name(tc)» si fonderebbe. L'inglese dice «You rub», quindi un name()
    (21814, 'You rub  with a brush.'):
        '"Spazzoli " + name(tc) + "."',
    # _impression3/_impression4 sono gia' italiane (text.hsp:44-45) e sono
    # frasi intere: la resa e' un prefisso coi due punti, non una frase da
    # completare
    (21819, "Your thoughts on this breeder's offspring: ."):
        '"Effetto allevatore: " + _impression3(cdata(CDATA_LIVESTOCK_QUALITY, tc)) + "."',
    (21823, "Your thoughts on this breeder's offspring: ."):
        '"Effetto allevatore: " + _impression4(cdata(CDATA_LIVESTOCK_PRODUCE_QUALITY, tc)) + "."',
    (21829, 'Your thoughts on this creature: .'):
        '"Questo animale: " + _impression3(cdata(CDATA_LIVESTOCK_QUALITY, tc)) + "."',
    (21834, 'Further,'):
        'E poi:',
    # ⚠️ questa esce anche DA SOLA, quando la sola qualita' del prodotto e' > 0:
    #    dev'essere una frase completa senza il «E poi:» davanti
    (21837, 'Your thoughts on this creature: .'):
        '_impression4(cdata(CDATA_LIVESTOCK_PRODUCE_QUALITY, tc)) + "."',
    # «spazzolato» concorderebbe con tc
    (21841, '  already brushed recently.'):
        '"Hai spazzolato " + name(tc) + " da poco: non serve a niente."',

    # --- i cinque gradini di spazzolatura. ⚠️ Sono CODE: il nome sta fuori da
    #     lang() e la resa comincia con uno spazio. Niente participi ne'
    #     aggettivi, che concorderebbero con l'animale.
    # ⚠️ le virgolette vanno PROTETTE (\") come nell'inglese di monte: una `"`
    #    nuda chiuderebbe in anticipo la stringa HSP che scrive applica.py
    (21853, ' looks proud. \\"Did it make me beautiful?\\"'):
        ' si pavoneggia un po\'. \\"Che ne dici, sono in ordine?\\"',
    (21857, ' looks clean. \\"Aww, it\'s already over?\\"'):
        ' ha un bell\'aspetto. \\"Uffa, già finito?\\"',
    (21861, ' looks marvelous. \\"Thank you!\\"'):
        ' fa la sua figura. \\"Grazie!\\"',
    (21865, ' looks quite healthy! \\"Thank you for everything!\\"'):
        ' sprizza salute! \\"Grazie di tutto!\\"',
    (21869, ' is positively shining! \\"I love you!\\"'):
        ' brilla di luce propria! \\"Ti voglio bene!\\"',
    # «da solo» concorderebbe col giocatore
    (21876, 'You brush yourself.'):
        'Ti dai una spazzolata.',
    (21879, ' rubbed .'):
        'name(cc) + " accarezza " + name(tc) + "."',

    # --- le coccole andate male. Le quattro di :21893 sono ALTERNATIVE a caso.
    (21889, "I'm scared, I'm scared... Ah, ah ah ah---!"):
        'Che paura, che paura... Ah, ah ah ah---!',
    (21893, ' appears to be irritated.'):
        ' non l\'ha presa bene.',
    # ⚠️ questa e la seguente sono un pezzo solo: name(tc) + A + name(cc) + B
    (21893, ' looks disgusted and brushes '):
        ' storce il naso e scaccia ',
    (21893, ' away.'):
        ' con un gesto.',
    (21893, 'Sexual harassment!'):
        'Molestie!',
    (21893, "Don't touch me."):
        'Non toccarmi.',

    # --- le coccole a metà.
    (21903, 'Ahyahya! More! Do it more... Ahyahya!'):
        'Ahiahiah! Ancora! Ancora, ti pre... Ahiahiah!',
    (21907, ' looks puzzled.'):
        'name(tc) + " non sa bene che pensare..."',
    (21907, ' looks slightly upset!'):
        'name(tc) + " storce un po\' il naso!"',
    (21907, ' silently steps away from .'):
        'name(tc) + " si scosta in silenzio e pianta lì " + name(cc) + "."',

    # --- le coccole riuscite.
    (21915, 'More! More brush brush!'):
        'Ancora! Ancora coccole!',
    (21919, ' looks somewhat happy.'):
        'name(tc) + " ci prende gusto."',
    (21919, ' blushes shyly...'):
        'name(tc) + " si fa rosso in viso..."',
    (21931, 'Haa... *purr*... haa... *purr*'):
        'Faaa... *fusa*... faaa... *fusa*',
    (21935, ' looks very happy!'):
        ' sprizza gioia!',
    # ⚠️ il secondo nome sta IN MEZZO e non si sposta: niente preposizione
    #    davanti, quindi un verbo transitivo. Vedi la nota in cima.
    (21935, ' silently snuggles up next to '):
        ' in silenzio cerca compagnia, e trova ',
    (21935, '.'):
        ' lì accanto.',

    # --- le moine.
    # «a name(tc)» e «di name(tc)» si fonderebbero: verbo transitivo
    (21964, ' tried fawn on .'):
        'name(cc) + " prova a intenerire " + name(tc) + "."',
    (21972, ' does not seem to be interested.'):
        'name(tc) + " non ci fa caso."',
    # ⚠️ due giapponesi opposti sotto un inglese solo: il ramo lo sceglie
    #    cdata(CDATA_RELATION, tc). Resi sul giapponese.
    (21991, ' took out the wallet without thinking \\"I\'ll give you pocket money!\\"'):
        'name(tc) + " tira fuori il portafogli senza pensarci. \\"E questa è la paghetta!\\""',
    (21994, ' took out the wallet without thinking \\"I\'ll give you pocket money!\\"'):
        'name(tc) + " tira fuori il portafogli senza pensarci. \\"C-che colpo basso!\\""',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-020.jsonl'
DA, A = 21000, 21999
SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\proc.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_proc.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]
voci = [v for v in zona if (v['riga'], v['en']) not in RINVIATE]

errori = []
for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items():
    if n > 1:
        errori.append(f'rete 0: la chiave {k} identifica {n} voci, non una')
indice = {(v['riga'], v['en']): v for v in voci}
for v in voci:
    if (v['riga'], v['en']) not in RESE:
        errori.append(f"rete 1: voce senza resa -> riga {v['riga']}  en={v['en']!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {(v['riga'], v['en']) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006) o dentro un blocco (lotto 014).
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)
for v in voci:
    if sorgente[v['riga'] - 1].lstrip().startswith(';'):
        errori.append(f"rete 6: riga {v['riga']} e' commentata nel sorgente, va rinviata")
    elif v['riga'] in SPENTE:
        errori.append(f"rete 6: riga {v['riga']} sta dentro un commento di BLOCCO, va rinviata")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[(v['riga'], v['en'])]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].rstrip().endswith(' and'):
        resa = RESE[(v['riga'], v['en'])].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[(v['riga'], v['en'])]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[(v['riga'], v['en'])]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[(v['riga'], v['en'])])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[(v['riga'], v['en'])]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[(v['riga'], v['en'])]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
