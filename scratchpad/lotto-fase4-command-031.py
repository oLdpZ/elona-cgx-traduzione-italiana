# -*- coding: utf-8 -*-
"""Lotto `command-031`: **i tre menu dell'aspetto** — il cambio di immagine
(`*com_shape_change`), l'editor del ritratto e del PCC (`*com_portrait_loop`) e
lo specchio che nasconde i pezzi d'armatura (`*com_mirror_loop`). Trentadue rese.

⚠️⚠️ **Il lotto non segue la zona: segue la FAMIGLIA, e la zona l'avrebbe
spezzata.** Le voci stanno in 11825-12297, cioè a cavallo del confine fra la
zona 11000-11999 e la 12000-12999. A tenerle insieme non è il gusto ma le
**firme condivise**: `lang("決定    ", "Done    ")` è ancorata a `:11825` e serve
tutt'e tre i menu (`:11825`, `:12034`, `:12276`); `lang("項目", "Category")` è
ancorata a `:11852` e la riusa `:12067`; la riga di aiuto
`"Right,left [Change]  Shift,Esc [Close]"` è ancorata a `:11849` e la riusano
`:12064` e `:12295`. Chi avesse aperto la sola zona 12000-12999 avrebbe reso
sette etichette di una colonna **lasciandone fuori la prima**, e la larghezza
della colonna si decide su tutte insieme.

⭐⭐⭐ **La scoperta del lotto: il carattere inglese è MONOSPAZIATO, quindi la
spaziatura di queste etichette non è decorativa — allinea davvero, e in un caso
è l'unico separatore.** `config.txt` dice `font2. "Courier New"`, cioè il
carattere che il ramo inglese usa a schermo. Per questo upstream scrive
`"Hair    "` e `"Body    "` imbottite a otto colonne: a `:12135`-`:12138` il
gioco fa `s = listn(0, p)` e poi `s += " " + rtval(2)`, e sono quelle spaziature
a incolonnare i numeri.
⚠️⚠️ **E nel menu dello specchio la spaziatura è LOAD-BEARING**: `:12333` e
`:12336` fanno `s += "On"` e `s += "Off"` **senza spazio davanti**. «Mantello» da
sola darebbe «MantelloOff». Per questo qui le etichette vanno a **nove** colonne
e non a otto: «Mantello» ne occupa già otto da sola.

⭐⭐ **Il tetto è 10, ed è misurato, non stimato.** Il testo esce a `wx + 64`
(`module.hsp:129`, `pos arg2 + 4 + arg5`) e la freccia destra è disegnata a
`wx + 175` (`:12153`, `:11900`, `:12340`, identiche in tutt'e tre i menu): sono
**111 px**. Courier a corpo 12 (`12 + sizefix - en * 2`) fa 7,2 px per carattere,
cioè **15,4 caratteri** per etichetta più valore.
⚠️ Il valore più lungo è quello del **ritratto**: `:12141`-`:12145` stampa
` N/A` se l'indice è −1 e ` u` + numero se è più negativo, quindi fino a **cinque**
caratteri. 10 + 5 = 15 → 108 px, dentro; 11 + 5 = 16 → 115 px, **fuori**. Le
righe di colore non arrivano mai a tanto (l'indice è una divisione, sempre ≥ 0),
ma la colonna è una sola e il tetto lo detta la riga peggiore.
✅ **E che 10 sia davvero permesso lo dimostra upstream**: `"Set Detail"` è di
dieci caratteri. Non è un caso che possa esserlo — `*portrait_item:11356` le dà
`rtval = -1`, e `:12136` appende il valore solo `if ( rtval >= 0 )`. Le righe
**senza valore** (`Done`, `Set Detail`, `Set Basic`, `Original`) non hanno tetto
stretto e non entrano nell'incolonnamento; le righe **con valore** vanno tutte
alla stessa larghezza. È la regola vera, e vale la pena scriverla: *l'imbottitura
serve alle righe che portano un numero, e solo a quelle.*

⭐⭐ **E `verifica` ha insegnato la regola giusta, che è più stretta della mia.**
`verifica.py:440` rifiuta una statica il cui inglese finisce con uno spazio e la
cui resa no, perché quello spazio è la **giuntura** col pezzo che segue. Aveva
ragione su due voci — «Conferma» e «Col.capel.», che riempivano tutte le colonne
senza lasciarne una vuota in fondo — e la ragione è più forte di come la guardia
la racconta: nel menu del ritratto lo spazio lo aggiunge il codice
(`s += " " + rtval(2)`), ma nello specchio **no** (`s += "Off"`). Una regola che
vale in un menu e non nell'altro è una regola che si dimentica.
✅ Quindi qui **ogni etichetta finisce con almeno uno spazio**, e la separazione
smette di dipendere da chi concatena. Il testo utile scende a nove colonne su
dieci, ed è per questo che 「髪の色」 è «Col.cap.» e non «Col.capel.».

⚠️⚠️ **La riga di aiuto è al tetto già in inglese, e nessuno strumento la
guarda.** `module.hsp:4344` la stampa a `wx + 58` con `mes`, senza taglio e senza
andare a capo; la riga «Page.» accanto (`:4349`) si tiene un margine di 40 px dal
bordo. Su una finestra da 380: 380 − 58 − 40 = **282 px = 39 caratteri**.
L'inglese ne usa **38**. Un carattere di margine.
✅ Per questo la resa **non** è «Destra,sinistra [Cambia]  Shift,Esc [Chiudi]»,
che ne farebbe 44 e uscirebbe dalla finestra, ma
«Dx,Sx [Cambia]  Shift,Esc [Chiudi]», che ne fa 34. ⚠️ `larghezze.py` non poteva
avvisare: guarda **solo `text.hsp`** e solo i menu che passano da `*prompt_key`,
e questa è la sottotitolatura di `display_window`.
💡 La forma della resa la detta `text.hsp:115`, che ha già `strhint3` =
«Shift,Esc [Chiudi]  »: il nome del tasto resta com'è, l'azione fra parentesi si
traduce.

⚠️ **Lo stesso giapponese sotto due inglesi diversi, e la rete 4 ha ragione a
pretenderne una resa sola.** 「項目」 è `"Category"` a `:11852` e `"Part"` a
`:12297`. La resa è **«Voce»** in tutt'e due, che è quel che 項目 vuol dire e che
regge sopra tutt'e due gli elenchi — le categorie dell'aspetto e i pezzi
d'armatura.

⭐ **E il rovescio: lo stesso inglese sotto TRE giapponesi diversi.**
`"Appearance"` sta per 「個別画像の変更」 (`:11849`, cambia lo sprite), per
「肖像の変更」 (`:12064`, cambia il ritratto) e per 「着替えさせる」 (`:6062`, già reso
«Cambia i vestiti» in una sessione passata). Tre schermate diverse, un inglese
solo: le rese sono «Cambia immagine», «Cambia aspetto» e quella già decisa. È la
famiglia della rete 13, e qui il referto avrà ragione a parlare.

⭐ Riscosso senza decidere: **«Ritratto»** era già la resa di `"Portrait"` in
`text.hsp:120` (`p [Ritratto]`), e i nomi delle parti del corpo di `text.hsp:136`
— Testa, Collo, Dorso, Torso, Mano, Anello, Arto, Vita, Gamba — fissano il
registro nominale asciutto che queste etichette seguono.

💡 **Due scelte di parola, per il tetto.** 「服」 è **«Veste»** e non «Vestito»
perché così «Col.veste» sta in nove colonne; 「アクセサリ1」 è **«Access. 1»** e non
«Etc1» perché l'inglese qui dice meno del giapponese e la voce è una statica,
senza contratto di funzioni da rispettare.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ================================================================
    # *com_shape_change — «Cambia immagine» (:11825-:11852)
    # ================================================================
    # ⭐ Firma condivisa dai TRE menu (:11825, :12034, :12276): una resa sola
    #    li serve tutti. Riga senza valore appeso (get_pic_selection:11407 le
    #    da' rtval = -2), quindi l'imbottitura non incolonna niente — ma lo
    #    spazio in coda ci va lo stesso, per la regola qui sotto.
    (11825, 'Done    '): 'Conferma ',
    # 「元々の姿にする」 = «riportalo all'aspetto di prima». Senza valore
    #    (get_pic_selection:11410, rtval = -3): larghezza libera.
    (11825, 'Original'): 'Originale',
    # ⚠️ L'unica riga di questo menu che porta un numero (rtval = 100), quindi
    #    l'unica col tetto: 8 + ' 123' = 12 caratteri = 86 px, dentro i 111.
    #    «applica:Pic_» ne farebbe 12 e con il numero sfonderebbe.
    (11825, 'apply:Pic_'): 'usa:Pic_',
    # ⭐ 「個別画像の変更」: il titolo della finestra. Il piatto di sfondo
    #    (module.hsp:4328) parte da 171 px e cresce solo oltre i 15 caratteri.
    (11849, 'Appearance'): 'Cambia immagine',
    # ⚠️⚠️ 39 caratteri di tetto, l'inglese ne usa 38. Questa ne fa 34.
    #    Vedi il docstring. La forma viene da text.hsp:115.
    (11849, 'Right,left [Change]  Shift,Esc [Close]'):
        'Dx,Sx [Cambia]  Shift,Esc [Chiudi]',
    # ⚠️ Stesso giapponese di :12297 («Part»): la rete 4 pretende una resa
    #    sola, e «Voce» regge sopra tutt'e due gli elenchi.
    (11852, 'Category'): 'Voce',

    # ================================================================
    # *com_portrait_loop — «Cambia aspetto», pagina 0 (:12034-:12039)
    # ================================================================
    # ⚠️ Righe CON valore: tutte a DIECI colonne, o i numeri non si
    #    incolonnano piu'. Vedi il docstring.
    (12034, 'Portrait'): 'Ritratto  ',
    (12034, 'Hair    '): 'Capelli   ',
    (12034, 'Sub Hair'): 'Capelli 2 ',
    # ⚠️ «Col.capel.» riempirebbe tutte e dieci le colonne senza lasciare lo
    #    spazio in coda: abbreviata di due caratteri perche' la regola dello
    #    spazio finale vale per tutta la colonna. Vedi il docstring.
    (12034, 'Hair CL '): 'Col.cap.  ',
    (12034, 'Body    '): 'Corpo     ',
    (12034, 'Cloth   '): 'Veste     ',
    (12034, 'Pants   '): 'Pantaloni ',
    # ⭐ Riga SENZA valore (portrait_item:11357, rtval = -1): e' la sola
    #    ragione per cui upstream ha potuto scriverci dieci caratteri.
    #    Cambia pagina, e fa coppia con «Di base» di :12044.
    (12034, 'Set Detail'): 'Dettagli',
    # ⚠️ Porta un valore (cbit CHARA_BIT_PCC, 0 o 1): dieci colonne anche lei.
    #    「ｶｽﾀﾑｷｬﾗ」 accende il PCC su un alleato al posto dello sprite fisso.
    (12036, 'Custom  '): 'Su misura ',
    (12039, 'Riding  '): 'A cavallo ',

    # ================================================================
    # *com_portrait_loop — pagina 1, i colori (:12044)
    # ================================================================
    # 💡 Famiglia «Col.», con il nome abbreviato solo dove il tetto lo impone.
    (12044, 'Body CL '): 'Col.corpo ',
    (12044, 'Cloth CL'): 'Col.veste ',
    (12044, 'Pants CL'): 'Col.pant. ',
    # ⭐ 「アクセサリ」 dice «accessorio»; l'inglese «Etc» dice meno. E' una
    #    statica, nessun contratto di funzioni: la resa segue il giapponese.
    (12044, 'Etc1    '): 'Access. 1 ',
    (12044, 'Etc2    '): 'Access. 2 ',
    (12044, 'Etc3    '): 'Access. 3 ',
    (12044, 'Eyes    '): 'Occhi     ',
    # ⭐ Riga senza valore (portrait_item:11397): larghezza libera.
    (12044, 'Set Basic'): 'Di base',
    # ⚠️ Stesso inglese di :11849 e di :6062, tre giapponesi diversi.
    (12064, 'Appearance'): 'Cambia aspetto',

    # ================================================================
    # *com_mirror_loop — «Parti da nascondere» (:12276-:12297)
    # ================================================================
    # ⚠️⚠️ Qui l'imbottitura e' l'UNICO separatore: :12333 e :12336 fanno
    #    s += "On" / s += "Off" senza spazio davanti. Nove colonne, non otto,
    #    perche' «Mantello» ne riempie gia' otto da sola.
    (12276, 'Chest   '): 'Corazza  ',
    (12276, 'Leg     '): 'Gambali  ',
    (12276, 'Belt    '): 'Cintura  ',
    (12276, 'Glove   '): 'Guanti   ',
    (12276, 'Mantle  '): 'Mantello ',
    (12295, 'Parts to hide'): 'Parti da nascondere',
    # ⚠️ Stesso giapponese di :11852. Vedi sopra.
    (12297, 'Part'): 'Voce',
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase4-command-031.jsonl'
DA, A = 11825, 12297
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\command.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_command.jsonl', encoding='utf-8') if l.strip()]
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
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
_spec = importlib.util.spec_from_file_location('cb', 'scratchpad/commenti-blocco.py')
_cb = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_cb)
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    return sorgente[riga - 1].lstrip().startswith(';') or riga in SPENTE


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _come = ("e' commentata nel sorgente"
                 if sorgente[_righe[0] - 1].lstrip().startswith(';')
                 else 'sta dentro un commento di BLOCCO')
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

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
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
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
