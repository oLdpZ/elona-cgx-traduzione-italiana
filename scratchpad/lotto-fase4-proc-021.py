# -*- coding: utf-8 -*-
"""Lotto fase4-proc-021: la melma che scioglie, il magnetismo, il ranch, la
stretta e il bacio (proc.hsp 22000-22999).

59 rese, nessuna rinviata. `proc.hsp` passa a 952 su 1.098 (87%). E' il lotto
piu' grosso del progetto.

⚠️⚠️ **Le otto parole del terreno portano il loro ARTICOLO, ed e' la scoperta
del lotto.** A `:22088`-`:22112` il sorgente costruisce `s` scegliendo fra otto
parole — 糸/web, 闇/darkness, 酸/acid, エーテル/ether, 炎/fire, 液体/potion,
光/light, 煙/smoke — e a `:22117` la usa come **soggetto**:
«the `s` caught `name(tc)`!». In italiano quelle otto parole hanno **generi
diversi** (la ragnatela, l'acido, il fuoco, la luce...), quindi la frase che le
ospita non puo' mettere un articolo fisso. ✅ **L'articolo va dentro ciascuna
delle otto**, esattamente come `db_item.hsp` fa con `ioriginalnamearticolodet`
(la toppa del pozzo, 36ª). La frase diventa «Quasi avesse vita propria, la
ragnatela avvolge X!», e **«vita propria» non concorda con niente**: se avessi
scritto «Come se fosse vivo» avrebbe concordato con `s`.
💡 `:22103` e' **液体 = liquido**, non «potion»: l'inglese ha messo il nome
dell'oggetto al posto della pozzanghera. Reso sul giapponese.
⚠️ **La rete 3 gridera' su `:22097`, ed e' la prova che la scoperta e' vera**:
lo stesso giapponese エーテル e' «etere» a `item_data.hsp:1304`, qui e'
**«l'etere»**. Non e' una divergenza: e' la stessa parola in due ruoli
sintattici diversi — li' e' un nome di materiale dentro una lista, qui e' il
soggetto di una frase. L'articolo lo impone il sito.

⚠️⚠️ **Cinque righe dove l'inglese e' sbagliato, e la serie sale a ventisette.**
Tre sono il personaggio, due sono la riga intera:

| riga | l'inglese dice | il giapponese e il codice dicono |
|---|---|---|
| `:22228` | `name(cc)` | `name(tc)`, e la riga sotto fa `cbitmod ..., tc, TRUE` |
| `:22896` | `name(cc)` | `name(tc)`, e la riga sopra fa `cdata(CDATA_CONDITION_ANGRY, tc) = 30` |
| `:22690` | «\\"What?\\"», ricopiata da `:22766` | 「痛い！」, cioe' «Ahi!»: qui ci si abbraccia da soli e **fa male** |
| `:22620` | « squeezed », ricopiata da `:22682` | 「信じられないほどの力で抵抗し、あなたを振りほどいた」: tc **resiste e si libera**, il contrario |
| `:22639` | « squeezed », idem | 「形だけの抵抗しか見せなかった」: tc **si lascia fare** |

⚠️ **E `:22620` e `:22639` mostrano il limite della rete 11 nel verso
opposto a `:18280`.** Li' l'inglese aveva **meno** `name()` del giapponese e la
resa doveva rinunciare a un nome; qui ne ha **due** dove il giapponese ne ha
**uno**, quindi la resa e' costretta a nominare anche l'altro personaggio — che
per fortuna la frase giapponese sottintende («ti ha scrollato via»). Non e' una
liberta': e' la guardia che impone il numero.

⚠️ **Otto rese girate per la rete 8**, e le due piu' interessanti usano il
**`-ne` enclitico**, la strada aperta dalla 37ª per il genitivo: «comincia a
sciogliere**ne** il corpo» (`:22048`) e «**ne** e' uscito latte densissimo»
(`:22576`). Le altre mettono il nome come complemento oggetto.

💡 **Cinque rese sono copie**: 「ヘンタイ！」 e' gia' «Che indecenza!»
(`action.hsp:10776`), 「ひどい…」 «Che crudelta'...» (`db_creature:100229`),
「ひっ！」 «Iii!» (`db_creature:117237`), エーテル «etere»
(`item_data.hsp:1304`), e `:22896` copia `proc.hsp:17835` («si infuria»), stesso
giapponese, dal lotto 018.

⚠️ **`:22792` porta un `♪1`**, che non e' testo: `init.hsp:1376` legge la cifra
dopo la nota come **numero dell'icona** e la toglie dalla stringa. Va copiata
identica, e `verifica` lo controlla.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- la melma che si attacca e scioglie. Il `-ne` enclitico evita il
    #     genitivo davanti a name(), e «sciogliere» non concorda con nessuno.
    (22048, ' assembled with  and started to melt.'):
        'name(cc) + " si stringe addosso " + name(tc) + " e comincia a scioglierne il corpo."',
    # copiata da db_creature.hsp:117237, stesso giapponese
    (22049, 'Ouch!'):
        'Iii!',
    (22049, "I'm m-melting!"):
        'M-mi sto sciogliendo!',
    (22049, 'Aaaaah!'):
        'Aaaaah!?',
    (22049, 'Gyaaaaaahh...!'):
        'Gyaaaaah...!',
    (22055, ' devoted magical power to the surroundings!'):
        'name(cc) + " libera il proprio potere magico tutt\'intorno!"',

    # --- le otto parole del terreno. ⚠️ Portano l'ARTICOLO dentro, perche' a
    #     :22117 fanno da soggetto e in italiano hanno generi diversi.
    (22088, 'web'):
        'la ragnatela',
    (22091, 'darkness'):
        'l\'oscurità',
    (22094, 'acid'):
        'l\'acido',
    # copiata da item_data.hsp:1304, piu' l'articolo
    (22097, 'ether'):
        'l\'etere',
    (22100, 'fire'):
        'il fuoco',
    # ⚠️ reso sul giapponese: 液体 e' il liquido, non la pozione
    (22103, 'potion'):
        'il liquido',
    (22106, 'light'):
        'la luce',
    (22109, 'smoke'):
        'il fumo',
    # «di » davanti a skillname non si fonde: i nomi di abilita' non portano
    # articolo (lotto 014)
    (22112, 'remnants of  element'):
        '"i residui di " + skillname(mef(MEF_TYPE, i) - MEF_TYPE_REMNANT_FIRE + SKILL_RES_FIRE)',
    # ⚠️ «vivo» concorderebbe con s, che ha otto generi diversi: «vita propria»
    #    non concorda con niente
    (22117, 'As if it were alive, the  caught !'):
        '"Quasi avesse vita propria, " + s + " avvolge " + name(tc) + "!"',

    # --- il magnetismo.
    # ⚠️ reso su name(tc): la riga sotto fa cbitmod ..., tc, TRUE
    (22228, ' became the S pole on the front!'):
        'name(tc) + " ha il fronte polarizzato a S!"',
    # statica: il name(tc) del giapponese non si puo' tenere
    (22436, 'The magnetism disappeared...'):
        'Il magnetismo è svanito...',

    # --- Inferno del solletico.
    # «lo solletica» sceglierebbe un genere
    (22462, ' held down  and started to tickle  at full power!'):
        'name(cc) + " immobilizza " + name(tc) + " e parte col solletico a più non posso!"',

    # --- la mungitura al ranch. Il giapponese non nomina nessuno, l'inglese
    #     si': la rete 11 impone un name().
    (22516, ' has not accumulated milk yet.'):
        'name(tc) + " non ha ancora latte."',
    (22520, '  not old enough to produce milk.'):
        'name(tc) + " non è ancora grande abbastanza per dare latte."',
    (22525, 'If you squeeze more milk,  will die. Stop it?'):
        '"Se spremi ancora, " + name(tc) + " ci lascia le penne. Smettere?"',
    (22530, 'You squeezed  to exhaustion.'):
        '"Hai munto " + name(tc) + " fino all\'ultima goccia."',
    # ⚠️ «da name(tc)» si fonderebbe: il `-ne` enclitico
    (22576, 'You squeezed milk from .'):
        '"Hai munto " + name(tc) + " e ne è uscito latte densissimo."',
    (22578, ' got weakened.'):
        'name(tc) + " ha perso ogni energia."',
    (22590, ' says: \\"Please make do with the hug pillow!\\"'):
        'cdatan(CDATAN_NAME, cnt) + " dice: \\"Accontentati del cuscino da abbracciare!\\""',

    # --- la stretta e l'abbraccio.
    (22615, ' hugged  to bed.'):
        'name(cc) + " tira " + name(tc) + " a letto in un abbraccio."',
    # ⚠️ reso sul giapponese: l'inglese ricopia :22682 e dice il contrario.
    #    La rete 11 pretende DUE name(), e il giapponese sottintende il secondo.
    (22620, ' squeezed .'):
        'name(tc) + " oppone una forza incredibile (" + teikou + ") e scrolla via " + name(cc) + "."',
    (22625, ' tried desperately to resist, but you were stronger.'):
        'name(tc) + " ha resistito con tutte le forze, ma tu eri più forte."',
    # ⚠️ idem: l'inglese ricopia :22682, il giapponese dice che si lascia fare
    (22639, ' squeezed .'):
        'name(cc) + " incontra appena un cenno di resistenza: " + name(tc) + " si lascia fare."',
    (22652, ' hugs you and pushes you onto the bed.'):
        'name(tc) + " si libera dall\'abbraccio e ti inchioda al letto."',
    (22682, ' squeezed .'):
        'name(cc) + " stritola " + name(tc) + " in una morsa."',
    (22686, ' hugged  tightly.'):
        'name(cc) + " stringe " + name(tc) + " in un abbraccio."',
    # ⚠️ reso sul giapponese: l'inglese ricopia :22766. Qui ci si abbraccia da
    #    soli, e il giapponese dice che fa male.
    (22690, '\\"What?\\"'):
        'Ahi!',
    # 極め技 e' la presa di sottomissione del jujitsu
    (22700, 'Further,  attacked  by kiwame-waza.'):
        '"E poi " + name(cc) + " blocca " + name(tc) + " con una presa di sottomissione."',
    (22737, ' silently hugs back.'):
        'name(tc) + " ricambia l\'abbraccio in silenzio."',
    (22737, 'Warm..'):
        'Che calore...',
    (22737, 'I feel happy.'):
        'Che bella sensazione.',
    (22760, ' says: \\"I will protect Lady Jure\'s lips at all costs!\\"'):
        'cdatan(CDATAN_NAME, cnt) + " dice: \\"Le labbra di Jure le difendo a costo della vita!\\""',

    # --- il bacio.
    (22766, 'What?'):
        'Eh?',
    # «a name(tc)» si fonderebbe: verbo transitivo
    (22776, ' kissed .'):
        'name(cc) + " bacia " + name(tc) + "."',
    # ⚠️ il ♪1 va copiato identico: la cifra e' il numero dell'icona
    (22792, 'Love it♪1'):
        'Ti voglio bene♪1',
    (22792, 'Mwah..♪'):
        'Mmh...♪',
    (22792, 'Give me.. more.'):
        'Ancora... ti prego.',
    (22792, "I don't want just a kiss..."):
        'Non mi basta un bacio...',
    # copiata da action.hsp:10776, stesso giapponese
    (22802, 'HENTAI!'):
        'Che indecenza!',
    (22802, 'I will kill you!'):
        'Ti ammazzo.',
    (22802, 'Ugh! Pffft.'):
        'Bleah... ptu, ptu.',
    # copiata da db_creature.hsp:100229, stesso giapponese
    (22802, 'Disgusting..'):
        'Che crudeltà...',
    (22818, 'Wait.. what!?'):
        'M-ma che ti salta in mente?!',
    (22818, 'Hey, not funny.'):
        'Non fare scherzi.',
    (22818, 'Do you want that kind of relationship?'):
        'Vuoi che fra noi ci sia quel genere di cosa?',
    (22818, 'Take responsibility!'):
        'Adesso te ne prendi la responsabilità!',

    # --- lo stato del terreno.
    (22879, 'The current field state cannot be reset...'):
        'Questo stato del terreno non si può annullare...',
    (22884, 'The field state was reset.'):
        'Lo stato del terreno è tornato normale.',

    # --- la furia e la confusione.
    # copiata da proc.hsp:17835 (lotto 018), stesso giapponese.
    # ⚠️ reso su name(tc): la riga sopra fa cdata(CDATA_CONDITION_ANGRY, tc) = 30
    (22896, ' went berserk.'):
        'name(tc) + " si infuria."',
    (22902, '  confused.'):
        'name(tc) + " va in confusione."',
    (22942, ' accumulates power.'):
        'name(cc) + " raccoglie le forze!"',
    # «in preda al terrore» non concorda: stessa forma di action.hsp:296
    (22987, '  overwhelmed.'):
        'name(tc) + " è in preda al terrore."',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-021.jsonl'
DA, A = 22000, 22999
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
