# -*- coding: utf-8 -*-
"""108a - Lotto 003 di `db_item.hsp`: il rapporto delle PERGAMENE e degli ATTI.

`FILTER_ITEM_SCROLL`, `description(3)`: **66 righe del sorgente, 65 firme**.
Dentro la categoria ci sono **due famiglie** che il giapponese tiene separate
con due parole diverse, e la resa le segue:

    巻物   → **una pergamena** (紙片, «foglio», nella riga di categoria)
    権利書 → **un atto**       (証書, «certificato»)

⚠️ **L'inglese apre venticinque righe con «It is a scroll that when read, …»**,
e in italiano quella testa costa: «Una pergamena che, letta, …» sono venti
caratteri su 69 spesi per dire due volte quel che il nome dell'oggetto dice già.
Il giapponese non ha quella testa — dice 「…する巻物だ。」, con la parola in
fondo — quindi la resa mette il **fatto** davanti quando il fatto è lungo, e
tiene «Una pergamena che …» quando ci sta. È la stessa scelta del lotto 002.

### ⚠️⚠️ Dieci atti, un solo giapponese, e dieci inglesi diversi

`:45063`-`:45418` e `:51362`-`:51575` sono i mezzi di trasporto: zattera,
peschereccio, nave pirata, nave da crociera, nave da guerra, sottomarino,
corazzata, locomotiva, autocarro, carrozza. **Il giapponese scrive la stessa
frase per tutti e dieci** — 「海マップでの乗り物の権利書だ。」 e
「ワールドマップでの乗り物の権利書だ。」, *un atto per un mezzo della mappa del
mare* / *della mappa del mondo* — e l'inglese ci mette il nome del mezzo.

**Il nome del mezzo è già il nome dell'oggetto**, dieci righe più su nella
stessa scheda: ripeterlo nel referto lo spreca. E la distinzione che il
giapponese fa — mare contro terra — è quella che al giocatore serve, perché dice
**dove** il mezzo si può usare. Due rese per dieci firme.

### ⚠️ Tre righe dove l'inglese aggiunge, e si tace

- **`:52520`**, la stregoneria: l'inglese dice «5 spell bonus points», il
  giapponese solo スペルボーナス. Il numero non è nel giapponese, e `text.hsp`
  ha già una riga che lo dice quando succede.
- **`:81402`**, la licenza del Vuoto: l'inglese dice **dove** sta il Vuoto
  («at South-West North Tyris»), il giapponese no.
- **`:89493`**, la mappa del tesoro: «from sources unknown» è dell'inglese.

### ⚠️ Le stelle non si scrivono

Il giapponese di `:81743` dice 「☆のついた武器防具」 e quello di `:130246`
parla degli oggetti col ★. **`☆` e `★` sono a doppia larghezza in CP932** e li
boccia `guardie`; nel dizionario non ce n'è **nemmeno uno** su 23.469 rese. Si
scrive quel che la stella significa, e in tutt'e due i casi lo dice l'inglese:
le due qualità che ☆ marca sono `_quality` 4 e 5, «eccezionale» e «celestiale»
(`glossario.md`), e ★ marca gli **artefatti**.

ⓘ **I termini già fissati altrove, e qui si ubbidisce:** 巻物 → «pergamena» e
権利書 → «atto» (i nomi degli oggetti in `db_item.hsp`), 呪い → «la maledizione»,
信仰 → «la Fede» (`chat.hsp`), 潜在能力 → «il potenziale», マテリアル →
«materiale», スペルボーナス → «punti bonus per gli incantesimi»
(`proc.hsp`), 収容所 → «accampamento», e `MP` è **invariato**
(`invariati.md:79`, che tiene `HP/MP` insieme).
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # ---------------------------------------------------------- :44034 l'atto dell'accampamento
    (44034, '(Single-use) Readable deed used to build a labor camp.'):
        "Un atto: letto, fa nascere un accampamento.",

    # ---------------------------------------------------------- :44303 la pergamena del raccolto
    (44303, 'It is a scroll that when read, causes gold coins to fall from the sky.'):
        "Una pergamena che fa piovere monete d'oro dal cielo.",

    # ---------------------------------------------------------- :44374 la pergamena del richiamo
    (44374, 'It is a scroll that when read, pulls three enemies to you.'):
        "Una pergamena che tira a sé fino a tre nemici.",

    # ---------------------------------------------------------- :45063 i sei atti dei mezzi di mare
    # ⚠️ il giapponese non nomina il mezzo — dice «un mezzo per la mappa del
    #    mare» — perché il nome dell'oggetto lo dice già. Sei firme, un solo
    #    giapponese, e l'inglese ci mette il nome: qui vince il giapponese.
    (45063, 'Certificate of ownership of a land raft. Can be read more than once.'):
        "Un atto per un mezzo di mare. Si può rileggere sempre.",

    (45134, 'Certificate of ownership of a fishing ship. Can be read more than once.'):
        "Un atto per un mezzo di mare. Si può rileggere sempre.",

    (45205, 'Certificate of ownership of a pirate ship. Can be read more than once.'):
        "Un atto per un mezzo di mare. Si può rileggere sempre.",

    (45276, 'Certificate of ownership of a cruise ship. Can be read more than once.'):
        "Un atto per un mezzo di mare. Si può rileggere sempre.",

    (45347, 'Certificate of ownership of a warship. Can be read more than once.'):
        "Un atto per un mezzo di mare. Si può rileggere sempre.",

    (45418, 'Certificate of ownership of a submarine. Can be read more than once.'):
        "Un atto per un mezzo di mare. Si può rileggere sempre.",

    # ---------------------------------------------------------- :51362 i quattro atti dei mezzi di terra
    (51362, 'Certificate of ownership of a battleship. Can be read more than once.'):
        "Un atto per un mezzo da viaggio. Si può rileggere sempre.",

    (51433, 'Certificate of ownership of a locomotive. Can be read more than once.'):
        "Un atto per un mezzo da viaggio. Si può rileggere sempre.",

    (51504, 'Certificate of ownership of a truck. Can be read more than once.'):
        "Un atto per un mezzo da viaggio. Si può rileggere sempre.",

    (51575, 'Certificate of ownership of a carriage. Can be read more than once.'):
        "Un atto per un mezzo da viaggio. Si può rileggere sempre.",

    # ---------------------------------------------------------- :52520 la pergamena della stregoneria
    # ⚠️ il «5» lo dice solo l'inglese; il giapponese dice スペルボーナス e basta.
    (52520, 'It is a scroll that when read, grants 5 spell bonus points.'):
        "Una pergamena che dà punti bonus per gli incantesimi.",

    # ---------------------------------------------------------- :55214 l'atto del trasferimento
    (55214, '(Single-use) Readable deed used to move a building, except your home.'):
        "Un atto: letto, sposta un edificio che non sia la casa.",

    # ---------------------------------------------------------- :58399 i due certificati fiscali
    (58399, 'Certificate that allows tax to be paid in advance. Pay them at tax boxes.'):
        "Paga le tasse in anticipo. Si mette nella cassetta delle tasse.",

    # ---------------------------------------------------------- :70200 l'atto dell'allevamento abbandonato
    (70200, '(Single-use) Readable deed used to build a giant ranch.'):
        "Un atto: letto, fa nascere un allevamento di mostri.",

    # ---------------------------------------------------------- :71031 l'atto del trasloco
    (71031, '(Single-use) Readable deed used to move your home.'):
        "Un atto: letto, permette di traslocare.",

    # ---------------------------------------------------------- :81402 la licenza dell'esploratore del vuoto
    # ⚠️ il giapponese non dice DOVE sta il Vuoto: lo aggiunge l'inglese.
    (81402, 'Certificate that allow one to explore the Void at South-West North Tyris.'):
        "Un atto: letto, dà il permesso di entrare nel Vuoto.",

    # ---------------------------------------------------------- :81743 la pergamena del nome
    # ⚠️ il giapponese scrive 「☆のついた武器防具」, ma ☆ e ★ sono a DOPPIA
    #    LARGHEZZA in CP932 e `guardie` li boccia: nessuna resa del progetto ne
    #    contiene uno (0 su 23.469). Si scrive quel che la stella significa, e
    #    lo dice l'inglese: le due qualità che marca, `_quality` 4 e 5.
    (81743, 'It is a scroll that when read, renames a miracle or godly equipment.'):
        "Cambia il nome a un'arma o armatura eccezionale o celestiale.",

    # ---------------------------------------------------------- :83414 l'atto del sotterraneo
    (83414, '(Single-use) Readable deed used to build a dungeon.'):
        "Un atto: letto, fa nascere un sotterraneo.",

    # ---------------------------------------------------------- :83629 la pergamena della contingenza
    (83629, 'It is a scroll that when read, allow you to sometimes cheat Death.'):
        "A volte azzera il colpo che sarebbe mortale.",

    # ---------------------------------------------------------- :88349 la pergamena della fuga
    (88349, 'It is a scroll that when read, opens a rift to escape after a few turns.'):
        "Porta fuori dal sotterraneo dopo qualche turno. Rileggerla annulla.",

    # ---------------------------------------------------------- :88744 la pergamena volante
    (88744, 'It is a scroll that when read, reduce weight of 1 item in your backpack.'):
        "Alleggerisce un oggetto dello zaino.",

    # ---------------------------------------------------------- :89493 la mappa del tesoro
    (89493, "(Re-usable) readable map from sources unknown that lead's to treasure."):
        "Una mappa con su un tesoro nascosto da qualche parte.",

    # ---------------------------------------------------------- :89887 la fattura
    (89887, 'It is a piece of paper with the amount of tax to be collected.'):
        "Un foglio con su quante tasse si devono pagare.",

    # ---------------------------------------------------------- :92657 l'atto dell'allevamento
    (92657, '(Single-use) Readable deed used to build a ranch.'):
        "Un atto: letto, fa nascere un allevamento.",

    # ---------------------------------------------------------- :94249 la pergamena della pioggia curativa
    (94249, 'It is a scroll that when read, restore health of the surrounding allies.'):
        "Cura i compagni qui attorno.",

    # ---------------------------------------------------------- :94673 l'atto del magazzino
    (94673, '(Single-use) Readable deed used to build a warehouse.'):
        "Un atto: letto, fa nascere un magazzino.",

    # ---------------------------------------------------------- :94742 l'atto del campo
    (94742, '(Single-use) Readable deed used to build a farm.'):
        "Un atto: letto, fa nascere un campo.",

    # ---------------------------------------------------------- :95993 l'atto del negozio
    (95993, '(Single-use) Readable deed used to build a shop.'):
        "Un atto: letto, fa nascere un negozio.",

    # ---------------------------------------------------------- :96063 l'atto del museo
    (96063, '(Single-use) Readable deed used to build a museum.'):
        "Un atto: letto, fa nascere un museo.",

    # ---------------------------------------------------------- :96500 la pergamena della ricarica
    (96500, 'It is a scroll that when read, restore charges of certain items.'):
        "Ridà cariche a certi oggetti.",

    # ---------------------------------------------------------- :96785 l'atto dell'eredità
    (96785, "It is a deed of heirship. It grants you power to open the heir's trunk"):
        "Un atto: letto, apre la borsa dei ricordi.",

    # ---------------------------------------------------------- :96918 potenziamento armatura, superiore
    (96918, 'It is a scroll that when read, enhances your equipment, potent.'):
        "Potenzia un'armatura. È più forte del solito.",

    # ---------------------------------------------------------- :96989 potenziamento armatura
    (96989, 'It is a scroll that when read, enhances your equipment.'):
        "Una pergamena che potenzia un'armatura.",

    # ---------------------------------------------------------- :97060 potenziamento arma, superiore
    (97060, 'It is a scroll that when read, enhances your weapon, potent.'):
        "Potenzia un'arma. È più forte del solito.",

    # ---------------------------------------------------------- :97131 potenziamento arma
    (97131, 'It is a scroll that when read, enhances your weapon.'):
        "Una pergamena che potenzia un'arma.",

    # ---------------------------------------------------------- :97399 materiale superiore
    (97399, 'It is a scroll that when read, remodel a item with rare materials.'):
        "Cambia il materiale di un oggetto. È più forte del solito.",

    # ---------------------------------------------------------- :97470 cambio di materiale
    (97470, 'It is a scroll that when read, remodel a item with a different material.'):
        "Una pergamena che cambia il materiale di un oggetto.",

    # ---------------------------------------------------------- :97541 materiale inferiore
    (97541, 'It is a scroll that when read, remodel a item with commonplace materials.'):
        "Cambia il materiale di un oggetto. Di solito in peggio.",

    # ---------------------------------------------------------- :99028 la pergamena dell'alleato
    (99028, 'It is a scroll that when read, summons a friendly character to join you.'):
        "Chiama una creatura amichevole che si unisce a te.",

    # ---------------------------------------------------------- :102253 la pergamena della fede
    (102253, 'It is a scroll that when read, deepens your faith.'):
        "Una pergamena che fa crescere la Fede.",

    # ---------------------------------------------------------- :102324 la pergamena della crescita
    (102324, 'It is a scroll that when read, raises your skill potential.'):
        "Alza il potenziale di un'abilità.",

    # ---------------------------------------------------------- :103579 la pergamena della scoperta
    (103579, 'It is a scroll that when read, detects and marks nearby objects.'):
        "Una pergamena che scopre le cose qui attorno.",

    # ---------------------------------------------------------- :104449 la pergamena della conoscenza
    (104449, 'It is a scroll that when read, enhances reading capabilities temporarily.'):
        "Per un po', rende più facile leggere i libri.",

    # ---------------------------------------------------------- :104666 la pergamena dei materiali
    (104666, 'It is a scroll that when read, grants you miscellaneous materials.'):
        "Una pergamena che fa ottenere dei materiali.",

    # ---------------------------------------------------------- :105016 la pergamena del mana
    (105016, 'It is a scroll that when read, restores your MP.'):
        "Una pergamena che ridà MP.",

    # ---------------------------------------------------------- :105087 la pioggia santa
    (105087, 'It is a scroll that when read, removes all curses cast on you.'):
        "Toglie di dosso tutte le maledizioni.",

    # ---------------------------------------------------------- :105158 la luce santa
    (105158, 'It is a scroll that when read, removes 1 curses cast on you.'):
        "Toglie di dosso una maledizione.",

    # ---------------------------------------------------------- :105455 il velo santo
    (105455, 'It is a scroll that when read, dispels curses temporarily.'):
        "Per un po', dà resistenza alle maledizioni.",

    # ---------------------------------------------------------- :106984 dissolvi maledizione
    (106984, 'It is a scroll that when read, removes curses from equipments. Potent.'):
        "Toglie la maledizione a un oggetto. È più forte del solito.",

    # ---------------------------------------------------------- :107055 identificazione superiore
    (107055, 'It is a scroll that when read, identifies unknown items. Potent.'):
        "Identifica gli oggetti ignoti. È più forte del solito.",

    # ---------------------------------------------------------- :108330 l'atto della casa
    (108330, '(Single-use) Readable deed used to build your own house.'):
        "Un atto: letto, fa nascere una casa.",

    # ---------------------------------------------------------- :111924 la pergamena della maledizione
    (111924, 'It is a scroll that when read, curses an item in your possession.'):
        "Una pergamena che maledice un oggetto.",

    # ---------------------------------------------------------- :114862 teletrasporto breve
    (114862, 'It is a scroll that when read, teleports you for a short distance.'):
        "Una pergamena che teletrasporta poco lontano.",

    # ---------------------------------------------------------- :114933 la pergamena del prodigio
    (114933, 'It is a scroll that when read, grants you magical knowledge.'):
        "Una pergamena che dà conoscenza magica.",

    # ---------------------------------------------------------- :115004 la pergamena del talento
    (115004, 'It is a scroll that when read, grants you profession skills.'):
        "Dà un'abilità che non si ha ancora.",

    # ---------------------------------------------------------- :115075 la mappa magica
    (115075, 'It is a scroll that when read, reveal undiscovered regions nearby.'):
        "Svela le parti del sotterraneo non ancora esplorate.",

    # ---------------------------------------------------------- :115456 la pergamena del ritorno
    (115456, 'It is a scroll that when read, teleports you to specified location.'):
        "Fra qualche turno porta in un luogo scelto. Rileggerla annulla.",

    # ---------------------------------------------------------- :117259 togli maledizione
    (117259, 'It is a scroll that when read, removes curses from your equipment.'):
        "Una pergamena che toglie la maledizione a un oggetto.",

    # ---------------------------------------------------------- :130104 la pergamena dell'incognito
    (130104, 'It is a scroll that when read, reset memories of hostile situations.'):
        "Azzera le ostilità, tranne quelle dei mostri.",

    # ---------------------------------------------------------- :130175 il teletrasporto
    (130175, 'It is a scroll that when read, teleports you for a distance.'):
        "Una pergamena che teletrasporta a caso.",

    # ---------------------------------------------------------- :130246 la pergamena dell'oracolo
    (130246, 'It is a scroll that when read, reveal locations of powerful artifacts.'):
        "Dice dove sono finiti gli artefatti già apparsi.",

    # ---------------------------------------------------------- :130317 l'identificazione
    (130317, 'It is a scroll that when read, identifies unknown items.'):
        "Una pergamena che identifica gli oggetti che si portano.",
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-003.jsonl'
RIGHE = {
    44034, 44303, 44374, 45063, 45134, 45205, 45276, 45347, 45418, 51362,
    51433, 51504, 51575, 52520, 55214, 58399, 70200, 71031, 81402, 81743,
    83414, 83629, 88349, 88744, 89493, 89887, 92657, 94249, 94673, 94742,
    95993, 96063, 96500, 96785, 96918, 96989, 97060, 97131, 97399, 97470,
    97541, 99028, 102253, 102324, 103579, 104449, 104666, 105016, 105087, 105158,
    105455, 106984, 107055, 108330, 111924, 114862, 114933, 115004, 115075, 115456,
    117259, 130104, 130175, 130246, 130317,
}
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_item.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_107-daitem.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if v['riga'] in RIGHE]
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

# rete 6: righe spente, col `;` (lotto 006), col `//` (100a) o dentro un
# blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
# ⚠️ Lo strumento, non lo scratch: `strumenti/commenti.py` e' la stessa funzione
# di `scratchpad/commenti-blocco.py` ma con dei test, e dalla 100a sa anche del
# commento di riga `//`.
from strumenti import commenti as _cb
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    testo = sorgente[riga - 1]
    return (testo.lstrip().startswith(';')
            or _cb.lang_spenta_da_barre(testo)
            or riga in SPENTE)


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _testa = sorgente[_righe[0] - 1]
        if _testa.lstrip().startswith(';'):
            _come = "e' commentata nel sorgente"
        elif _cb.lang_spenta_da_barre(_testa):
            _come = "e' spenta da un commento `//`"
        else:
            _come = 'sta dentro un commento di BLOCCO'
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
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
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
