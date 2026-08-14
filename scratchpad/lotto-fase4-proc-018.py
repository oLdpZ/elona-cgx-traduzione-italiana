# -*- coding: utf-8 -*-
"""Lotto fase4-proc-018: scrigni, Duplibacchetta, jujitsu, X-Frame, il legame,
la richiesta d'aiuto (proc.hsp 17000-17999).

42 rese, nessuna rinviata. `proc.hsp` passa a 800 su 1.098 (73%).

⚠️⚠️ **Due errori nuovi dell'inglese di monte, e sono lo stesso guasto: una riga
ricopiata dove non andava.** Portano la serie a **quindici**.

1. **`:17114` e `:17120` hanno lo stesso inglese e dicono il contrario.**
   «steadied his breathing and changed his posture» sta per tutt'e due, ma il
   giapponese distingue 「構えを変えた」 (cambia guardia, cioe' **esce** dal
   jujitsu) da 「柔術の構えをとった」 (**prende** la guardia di jujitsu), e il
   codice non lascia dubbi: `:17113` fa `cbitmod ... FALSE`, `:17119` fa
   `... TRUE`. E' l'interruttore dell'azione speciale, e in inglese le due
   posizioni si leggono uguali. Resi sul giapponese. 💡 **L'ha pescato la rete
   13**, nata nella 37ª per `:14521`/`:14573`: e' la seconda volta che paga.
2. **`:17149` porta l'inglese di un'ALTRA azione speciale.** Il giapponese dice
   「name(cc)は液体を操り、拡散射出した。」 — Manipolazione dei liquidi, la
   pozione spruzzata tutt'intorno — e l'inglese dice «established a breathing and
   changed the posture», cioe' la riga del jujitsu di trentacinque righe sopra,
   ricopiata parola per parola. Non e' una traduzione imprecisa: e' **un'altra
   frase**. Reso sul giapponese.

💡 **Nove rese su quarantadue sono copie**, ed e' la percentuale piu' alta di
tutto `proc.hsp` finora. Otto vengono dallo stesso posto: i versi
dell'**X-Frame** (`:17415`-`:17444`) sono gia' in `action.hsp:12960`-`:12989`
parola per parola, perche' il mod stampa la stessa sequenza da due punti.
Piu' `:17261` («cade a terra», `proc.hsp:9600`). La regola «cercare prima di
scrivere» qui ha reso quasi una voce su quattro.

⚠️ **Due rese sono state girate PRIMA di scriverle per la regola della rete 8**,
non perche' la rete le abbia fermate. La forma naturale sarebbe stata «Una
pioggia **di** " + itemname(ci)» a `:17292` e «Hai messo mano **a** " +
itemname(ci)» a `:17384`, e `itemname()` porta gia' l'articolo («una pozione»):
sarebbe uscito «di una pozione» dove serviva «di pozioni» e «a una pozione» dove
serviva «alla pozione». Girate tutt'e due mettendo l'oggetto come **soggetto**.
La rete resta la guardia se qualcuno ci ricasca.

⚠️ **Sei rese girano la frase per non far concordare un participio o un
aggettivo**, con la strada dei lotti 016 e 017: `:17235` («lanciato» →
«parte a tutta velocita'»), `:17908` («daunted» → «La minaccia intimidisce X»),
`:17830` («infuriato» → «e' gia' in preda alla furia»), `:17060` («robusto» →
«non cede facilmente»), `:17542` («non gli esce la voce» → «dalla gola non esce
un suono», perche' il possessivo avrebbe scelto un genere), `:17744`
(«e' rimasto solo» → «non ha nessuno accanto»).

💡 **I nomi vengono tutti da `skill.hsp`, e nessuno e' stato inventato**:
Duplibacchetta (`:1556`), Jujitsu vindaliano (`:1616`), Minaccia (`:1196`),
Nebbia di silenzio (`:639`, e `buff.hsp:11`), Lanciatore lineare (`:1808`).
Per 狂暴化 il dizionario non aveva un verbo — `text.hsp:72` ha «Frenesia» per lo
stato e `skill.hsp:1145` «Fa infuriare gli alleati» per l'effetto — quindi la
coppia e' **«si infuria» / «e' gia' in preda alla furia»**, che regge tutt'e due
i siti senza concordare con nessuno.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- lo scrigno forzato a mani nude. 錠 -> «serratura» (action.hsp:3174).
    (17001, 'Which target?'):
        'Che cosa vuoi aprire?',
    (17055, "...You realize that it's impossible to force open."):
        '...Nemmeno con la forza bruta si apre.',
    # «robusto» concorderebbe con lo scrigno
    (17060, "...It's quite sturdy."):
        '...Non cede facilmente.',
    (17065, "You've successfully destroyed the lock!"):
        'Hai spaccato la serratura!',

    # --- Duplibacchetta (skill.hsp:1556). 杖 -> «bacchetta» (proc.hsp:7274).
    #     Il giapponese dice «あなた», l'inglese `name(cc)`: la voce e' dinamica
    #     e il nome resta.
    (17099, ' will attack by normal cane.'):
        'name(cc) + " decide di attaccare con la bacchetta normale."',
    (17105, ' will attack by duplicated cane.'):
        'name(cc) + " decide di attaccare con la bacchetta duplicata."',

    # --- Jujitsu vindaliano (skill.hsp:1616).
    # ⚠️ :17114 spegne l'azione (cbitmod FALSE a :17113) e :17120 l'accende
    #    (TRUE a :17119): l'inglese e' lo stesso per tutt'e due. Resi sul
    #    giapponese. Vedi la nota in cima.
    (17114, ' steadied  breathing and changed  posture.'):
        'name(cc) + " riprende fiato e cambia guardia."',
    (17120, ' steadied  breathing and changed  posture.'):
        'name(cc) + " riprende fiato e prende la guardia del jujitsu."',

    # --- Manipolazione dei liquidi.
    (17128, 'Which potion?'):
        'Quale pozione usare?',
    # ⚠️ reso sul giapponese: l'inglese e' la riga del jujitsu, ricopiata
    (17149, ' established a breathing and changed the posture.'):
        'name(cc) + " manipola il liquido e lo spruzza tutt\'intorno."',

    # --- Lanciatore lineare (skill.hsp:1808).
    (17215, 'Which item will you consume?'):
        'Quale oggetto consumare e lanciare?',
    # «lanciato» concorderebbe con l'oggetto
    (17235, ' was launched at high speed.'):
        'itemname(ci) + " parte a tutta velocità."',
    # copiata da proc.hsp:9600, stesso giapponese e stesso inglese
    (17261, '  knocked down.'):
        'name(tc) + " cade a terra."',
    # ⚠️ «Una pioggia di » + itemname: itemname porta gia' l'articolo. Girata.
    (17292, ' rain poured down in around.'):
        'itemname(ci) + " si rovescia tutt\'intorno come pioggia."',
    (17355, 'Rain pours down all around.'):
        'La pioggia si rovescia tutt\'intorno.',

    # --- il cibo manomesso (ibitmod ITEM_BIT_HAZARD due righe sotto).
    (17376, 'Which food?'):
        'Quale cibo?',
    # ⚠️ «Hai messo mano a » + itemname: stessa fusione. Girata.
    (17384, 'You arranged .'):
        '"Hai ritoccato " + itemname(ci) + "!"',

    # --- X-Frame. Tutte e otto copiate da action.hsp:12960-12989, dove il mod
    #     stampa la stessa sequenza.
    (17393, 'Which item?'):
        'Quale oggetto?',
    (17415, 'It has the same performance...'):
        'Ha già la stessa funzione...',
    (17421, 'X-Frame Change!'):
        'Cambio telaio X!',
    (17424, 'Spinning Foot!'):
        'Piede rotante!',
    (17428, 'Mighty Arm!'):
        'Braccio possente!',
    (17432, 'Dual Core!'):
        'Doppio nucleo!',
    (17436, 'Rapid Server!'):
        'Servo rapido!',
    (17440, 'Snipe Head!'):
        'Testa da cecchino!',
    (17444, 'Deceive Barrel!'):
        'Canna ingannevole!',

    # --- Getuei il maestro ninja. 忍法 -> «arte ninja» (db_creature:87632).
    (17481, '*Shadow Dance*'):
        'Arte ninja suprema: la danza delle ombre!',

    # --- Chiede aiuto (skill.hsp:1093).
    # «non gli esce la voce» sceglierebbe un genere: esce dalla gola
    (17542, ' called out for help in a trembling voice, but no sound came out.'):
        'name(cc) + " prova a gridare aiuto, ma dalla gola non esce un suono..."',
    (17546, ' called for help from those around.'):
        'name(cc) + " chiede aiuto a chi ha intorno."',

    # --- Nebbia di silenzio (buff.hsp:11, skill.hsp:639).
    (17664, 'The mist of silence interrupts a spell.'):
        'La nebbia di silenzio impedisce di lanciare.',
    # «rimasto solo» concorderebbe. cdatan(CDATAN_NAME, x) porta l'articolo
    # come name(x) (la toppa di init.hsp:1717): niente preposizione davanti.
    (17744, ' is lonely.'):
        'cdatan(CDATAN_NAME, cc) + " non ha nessuno accanto..."',

    # --- la furia. 狂暴化: «si infuria» e «in preda alla furia», che non
    #     concordano con nessuno.
    (17830, ' has already gone berserk.'):
        'name(tc) + " è già in preda alla furia."',
    (17835, ' went berserk.'):
        'name(tc) + " si infuria."',

    # --- Cuori sincronizzati.
    (17846, 'Did not meet the conditions of use.'):
        'Non si attiva se non sei alle strette.',
    (17850, 'With our hearts united, we spin off even more power!'):
        'I legami che ci uniscono filano una forza ancora più grande!',
    # i quattro versi stanno tutti sulla riga 17881, uno per `lang()`: il gioco
    # ne pesca uno a caso. Sono `cnvtalk()`, quindi testo nudo.
    (17881, 'I can still fight!'):
        'Posso ancora combattere!',
    (17881, 'The game is just starting!'):
        'Il bello viene adesso!',
    (17881, 'Together as one...!'):
        'Un cuore solo...!',
    (17881, 'Alliance Power!'):
        'Il potere del legame!',

    # --- Minaccia (skill.hsp:1196). «daunted» concorderebbe con tc: la
    #     minaccia diventa soggetto.
    (17908, '  daunted by the browbeat.'):
        '"La minaccia intimidisce " + name(tc) + "."',
    (17917, ' sends out a shockwave.'):
        'name(cc) + " libera un\'onda d\'urto."',
    (17986, ' compressed and released a stream of blood.'):
        'name(cc) + " comprime il proprio sangue e lo scaglia."',
}

# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-proc-018.jsonl'
DA, A = 17000, 17999
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
