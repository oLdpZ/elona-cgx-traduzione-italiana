# -*- coding: utf-8 -*-
"""Lotto fase4-map-001: i messaggi di viaggio, le porte sbarrate e il nome di
casa tua (map.hsp, righe 500-1500).

43 rese **+1 rinviata**, ed e' il **primo lotto di `map.hsp`**: il file diventa
il diciottesimo dei 54 con `lang()` ad avere un dizionario. Il lotto nasce dal
collaudo della 42a, non da un conteggio.

⭐⭐ **Chiude il difetto dei due nomi, e la causa era piu' piccola di quel che
sembrava.** Il collaudo ha mostrato due righe consecutive che chiamano casa tua
in due modi: «Vuoi lasciare **Your Home**?» e «You left **Casa tua**.» La prima
legge `mdatan(MDATAN_NAME)`, la seconda `mapname()`.
✅ E `map.hsp:1400`-`:1402` dice che il caso e' **uno solo**:

    else {
        mdatan(MDATAN_NAME) = mapname(gdata(GDATA_AREA))
    }

Per **ogni area tranne AREA_HOME** il nome della mappa viene riletto da
`mapname()` — la tabella di `text.hsp`, gia' tradotta — a ogni `*map_init_main`.
«Grassland», «Forest», «Plain Field» non erano un difetto separato: si sistemano
da sole. Casa tua e' l'unica mappa che il giocatore puo' **rinominare**, e per
questo ha una guardia che evita di sovrascrivere il nome scelto.

⚠️⚠️ **`:1396` e' un confronto contro un valore scritto nel salvataggio, e va
rinviata.** `module.hsp:4598` fa `noteadd mdatan(cnt)` e `:4601` fa
`noteget mdatan(cnt)`: `mdatan` e' serializzato. La riga confronta il nome
memorizzato con `lang("ノースティリス", "North Tyris")`; tradurre l'operando
farebbe fallire il confronto su ogni salvataggio che porta il nome inglese. E'
la regola che la **rete 7** ha imposto ai nove `CDATAN_NEWSEX` nella 41a, e qui
casca su una riga che nessuno aveva ancora guardato.
💡 **L'asimmetria con `:1397` e' la stessa di `init.hsp`/`text.hsp`**: `:1397` e'
un **assegnamento**, cioe' testo che si stampa, e si rende; `:1396` e' un
operando di `==`, e si rinvia. La rete 7 guarda il sito, non la stringa.

⭐ **E `:1397` e' una copia obbligata**: `text.hsp:2764` ha la **stessa firma** —
stesso giapponese, stesso inglese — ed e' resa «Casa tua». `applica.py:618`
applica ogni dizionario al **suo** file soltanto, quindi la voce va riscritta
qui. E' il caso di 「性別不明」 della 41a, ma stavolta la firma mancante
**produceva un difetto visibile** invece di essere innocua.

⚠️ **Resta fuori la migrazione dei salvataggi vecchi, e la fa una toppa.** Dopo
questo lotto una partita nuova dice «Casa tua», ma un salvataggio che porta gia'
«Your Home» memorizzato non passa la guardia — il nome non e' ne' `""` ne'
«North Tyris» — e resterebbe inglese per sempre. La toppa allarga la condizione
con `| mdatan(MDATAN_NAME) == "Your Home"`, ed e' la **prima toppa di
migrazione** del progetto: le 303 esistenti correggono errori di monte, nessuna
converte un dato vecchio.

⭐ **La rete 13 grida una volta, e stavolta l'inglese aveva appiattito due
luoghi.** `:1121` e `:1137` hanno tutt'e due «You entered the Mountain Pass.»,
ma il giapponese distingue マウンテンパス da 風の山道 e il codice conferma due
aree diverse (`AREA_MOUNTAIN_PASS` contro `AREA_MOUNTAIN_PASS_WINDY`).
✅ E la distinzione **era gia' scritta**: `text.hsp:2854` rende 山道 «il Passo di
Montagna» e `:3024` rende 風の山道 «il Passo Ventoso». L'italiano le separa dove
l'inglese le aveva fuse.

⚠️⚠️ **Il genitivo davanti a `mapname()` e' chiuso, e sono SEI righe.** I nomi di
area portano l'articolo dentro — «la Torre Rovente», «la grotta dei morti», «il
Castello Antico», «il Vuoto» — quindi «la superficie **di** X» e «entri **in** X»
sono tutt'e due bocciate dalla rete 8. E le preposizioni che non si fondono
(«con», «contro», «per», «tra», «sotto», «sopra») qui non servono a niente,
perche' il rapporto e' proprio locativo.
✅ **La strada e' mettere il nome fuori dalla frase**, con i due punti o come
oggetto diretto:

  - `:1048` «Entri qui: X.» e `:1058` «Torni qui: X» — il nome sta **dopo** i due
    punti, dove nessuna preposizione lo tocca;
  - `:891` «X: torni in superficie.» e `:894` «X: ne lasci la superficie.» — il
    nome sta **in testa**, che e' anche l'ordine del giapponese, e il `-ne`
    enclitico riprende il possesso senza genitivo;
  - `:1061` «Lasci X.» — ⭐ il caso piu' economico: «lasciare» regge l'**oggetto
    diretto**, quindi la preposizione non c'e' proprio.

💡 **E' la strada del participio e del genitivo della 37a portata su un
complemento di luogo**, ed e' la prima volta che il progetto la percorre: fino a
qui il problema era sempre `name()` e `cdatan()`, mai `mapname()`.

💡 **Le righe di diario parlano in prima persona, e non l'ho deciso io.**
`:815`, `:822` e `:848` sono promemoria di trama, e `text.hsp` ne ha gia' una
dozzina rese con «Devo…»: «Devo sentire Gavela, a Melugas.», «Devo annientare
l'esercito di difesa Yerles.» ✅ Copiato il registro, e `:822` e' quasi la
stessa frase di quella di `text.hsp`.

💡 **Quattro nomi propri erano gia' fissati** e sono stati copiati senza
decidere niente: `Yerles`, `Eulderna`, `Elea`, `Gavela`/`Melugas`, `Noyel`.

⚠️ **Una grida della rete 3 che non e' una divergenza.** 「当然だ」 e' «Certo che
me la svigno.» ad `action.hsp:2153`, dove chi parla scappa, e «Certo che entro.»
a `:772`, dove chi parla entra a Vernis. Stesso giapponese, due mestieri: e' il
caso di 日 del lotto `init-003`. La sorella `:773` invece **coincide** e si copia
tale e quale da `action.hsp:2154`.

⚠️ **Tre participi girati per non far concordare il giocatore.** «Non sei
riuscito a difendere il concerto» concorderebbe (`:599`), e cosi' «Sei entrato»
(`:1048`) e «Vieni riportato» (`:1035`). ✅ «Il concerto e' andato in rovina…»,
«Entri qui: X.», «Ti riportano al punto di rientro.» — presente e terza plurale
impersonale, che genere non hanno.

💡 **`:606`-`:682` parlano al PLURALE, e in italiano si sente.** Il giapponese
dice あなた達, «voi», perche' sono il giocatore e i compagni: «Vi disinfettate su
una scialuppa e fate ritorno.», «Riuscite a stento a tornare a Noyel.»
L'inglese usa «You», che il plurale non lo distingue.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :595-:599 il concerto di Karavika, difeso o perduto.
    # ⭐ :595 copiata da proc.hsp:989, stesso inglese
    # ⚠️ :599 «non sei riuscito» concorderebbe col giocatore: girata sul concerto
    (595, 'A Legendary stage!'):
        "Un'esibizione da leggenda!",
    (599, 'The party turned out to be a big flop...'):
        'Il concerto è andato in rovina...',

    # --- :606-:682 i quattro rientri, tutti al PLURALE (あなた達 = voi).
    (606, 'You return via a small boat after disinfecting it.'):
        'Vi disinfettate su una scialuppa e fate ritorno.',
    (621, 'You return from the Eulderna capital.'):
        'Fate ritorno dalla capitale di Eulderna.',
    (652, 'You somehow make it back to Noyel.'):
        'Riuscite a stento a tornare a Noyel.',
    (682, 'You return to the border station.'):
        'Riuscite a stento a tornare al posto di frontiera.',

    # --- :710-:724 le scale.
    (710, 'You walk down the stairs.'):
        'Scendi le scale.',
    (724, 'You walk up the stairs.'):
        'Sali le scale.',

    # --- :755 il naufrago che si e' salvato. gdata e' contenuto: resta.
    (755, 'Drifter thanked you and left. (Karma + )'):
        '"Il naufrago ti ringrazia e se ne va. (Karma + " + gdata(GDATA_FLAG_SAVED_DRIFTERS) * 2 + ")"',

    # --- :768-:773 la sfida che rade al suolo la grotta dei mendicanti.
    # ⚠️ :772 「当然だ」 diverge da action.hsp:2153 apposta: li' si scappa, qui si entra
    # ⭐ :773 invece coincide e si copia da action.hsp:2154
    (768, 'Entering Vernis.'):
        'Entrare a Vernis.',
    (770, "You haven't said goodbye to the Eleas in your home yet. Are you sure to enter Vernis?"):
        'Non hai ancora salutato gli Elea che stanno a casa tua. Vuoi davvero entrare a Vernis?',
    (772, 'I will enter Vernis.'):
        'Certo che entro.',
    (773, 'Maybe later.'):
        'Andrò a dirglielo.',

    # --- :784-:870 le nove porte che il gioco tiene chiuse.
    # 💡 :815, :822 e :848 sono promemoria di trama: registro «Devo…», copiato
    #    dalla dozzina che text.hsp ha gia' reso cosi'
    (784, 'You are not permitted to explore this dungeon.'):
        'Non hai il permesso di esplorare questa caverna.',
    (791, "You don't have an invitation."):
        "Non hai l'invito per la piramide.",
    (797, 'The guards turn you away from the jail.'):
        'Le guardie ti respingono.',
    (808, "A high concentration of ether fills the area. You'd better stay away."):
        "Una fitta concentrazione di etere satura l'aria. Meglio starne alla larga.",
    (815, 'The Yerles army has closed the entrance via an electronic lock. I should look for a way through.'):
        "L'esercito Yerles ha sbarrato l'ingresso con una serratura elettronica. Devo trovare il modo di aprirla.",
    (822, 'I should hear what Gavela in Melugas has to say.'):
        'Devo prima sentire Gavela, a Melugas.',
    (829, "No one answered the door. There's a For Sale sign in front of the mansion."):
        "Pare che la villa sia in vendita: ho sbirciato dentro, ma non c'era nessuno.",
    (836, 'The front entrance is shut tight. You have no idea how to get inside.'):
        "L'ingresso principale è sbarrato. Chissà da dove si entra.",
    (848, 'I should go to the ruin of forest ahead.'):
        'Devo prima andare alle rovine nella foresta di cui ha parlato Norn.',
    (855, 'You sense an extraordinary presence. It would be better to learn more information '
          'about this Nefia before exploring it.'):
        'Avverti una presenza fuori dal comune. Meglio raccogliere altre notizie su questa '
        'Nefia prima di esplorarla.',
    (862, 'The gate is firmly closed...'):
        'Il cancello è serrato...',
    (870, 'When you try to enter it, the tower dissipates as a mirage...'):
        'Quando provi a entrare, la torre si dissolve come un miraggio...',

    # --- :891-:1061 i sei messaggi di passaggio da una mappa all'altra.
    # ⚠️⚠️ mapname() porta l'articolo dentro («la Torre Rovente», «il Vuoto»),
    #      quindi «di X» e «in X» sono chiuse dalla rete 8. Il nome si mette
    #      FUORI dalla frase: dopo i due punti, in testa, o come oggetto diretto.
    (891, 'You returned to the surface of .'):
        '"" + mapname(gdata(GDATA_AREA)) + ": torni in superficie."',
    (894, 'You left the surface of .'):
        '"" + mapname(gdata(GDATA_AREA)) + ": ne lasci la superficie."',
    (1035, 'You were delivered to your home.'):
        'Ti riportano al punto di rientro.',
    (1041, 'You leave your ship.'):
        'Scendi dalla nave.',
    (1045, 'You got off the world-vehicle and entered .'):
        '"Scendi dal veicolo ed entri qui: " + mapname(gdata(GDATA_AREA)) + "."',
    (1048, 'You entered .'):
        '"Entri qui: " + mapname(gdata(GDATA_AREA)) + "."',
    (1054, 'You boarded your ship'):
        'Sali a bordo della nave',
    (1058, 'You returned to '):
        '"Torni qui: " + mapname(gdata(GDATA_AREA))',
    # ⭐ il caso piu' economico: «lasciare» regge l'oggetto diretto
    (1061, 'You left .'):
        '"Lasci " + mapname(gdata(GDATA_AREA_PREV)) + "."',

    # --- :1069 il carro troppo carico.
    (1069, 'The weight of your cargo burdens your traveling speed.'):
        'Il carro sovraccarico ti rallenta parecchio.',

    # --- :1121-:1145 i quattro arrivi del valico.
    # ⭐ rete 13: :1121 e :1137 hanno lo STESSO inglese e due giapponesi diversi,
    #    e sono due aree distinte. text.hsp:2854 e :3024 avevano gia' i due nomi.
    (1121, 'You entered the Mountain Pass.'):
        'Scendi nel Passo di Montagna.',
    (1129, 'You reached the town of Larna.'):
        'Arrivi al villaggio di Larna.',
    (1137, 'You entered the Mountain Pass.'):
        'Scendi nel Passo Ventoso.',
    (1145, 'You reached the ancient garden.'):
        'Arrivi al Giardino Antico.',

    # --- :1197 il diario. ⭐ copiata: quattro file la rendono gia' cosi'
    (1197, 'Your journal has been updated.'):
        'Il tuo diario è stato aggiornato.',

    # --- :1297 la finestra di sistema che rigenera una mappa rotta.
    (1297, 'Reinitialize this map? (Warning, only do this if an error occurs when loading this '
           'map. Make sure you have a backup of the current save folder before doing this.)'):
        'Vuoi reinizializzare questa mappa? (Attenzione: può avere conseguenze sulla partita. '
        'Fallo solo se compare un errore mentre la mappa viene caricata, e solo dopo aver messo '
        'da parte una copia della cartella dei salvataggi.)',

    # --- :1396-:1397 il nome di casa tua, che e' il difetto del collaudo.
    # ⚠️⚠️ :1396 e' RINVIATA: e' un confronto contro un valore serializzato da
    #      module.hsp:4598. Vedi `rinviate001.py` e il docstring.
    # ⭐ :1397 e' copiata da text.hsp:2764, stessa firma
    (1397, 'Your Home'):
        'Casa tua',

    # --- :1486 il presagio del piano.
    (1486, '  ...You sense fortune on this map...!'):
        '  ...Su questo piano si sente il destino...!',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = {(1396, 'North Tyris')}

USCITA = 'lavoro/fase4-map-001.jsonl'
DA, A = 500, 1500
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\map.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_map.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if DA <= v['riga'] <= A]

# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

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
    resa = RESE[chiave(v)]
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
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
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
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
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
    resa = RESE[chiave(v)]
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
    per_jp[(v['jp'], firma_di(v))].add(parole(RESE[chiave(v)]))
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
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
