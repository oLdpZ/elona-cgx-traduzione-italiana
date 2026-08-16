# -*- coding: utf-8 -*-
"""Il platino della barra di stato: quattro caratteri, e non uno di piu'.

`screen.hsp:411` fa `bmes "" + cdata(CDATA_PLATINUM, CHARA_PLAYER) + " pp"`, il
gettone accanto all'oro toppato poco fa (`screen.hsp:405`). Stessa classe —
letterale nudo, quinto punto cieco — ma con un vincolo di larghezza che l'oro
non ha.

## Perche' non ` platino`, che pure esiste gia'

`text.hsp:194` ha gia' deciso la forma lunga: `strplat = lang(" plat", " platino")`.
Qui non ci sta, e il motivo e' che questo gettone e' **l'ultimo a destra**:

    :406  sx = windoww - 90     icona del platino a sx (24 px)
    :410  pos sx + 28           testo a windoww - 62

Alla destra del testo non c'e' un altro gettone, c'e' il **bordo dello schermo**:
62 px in tutto. Col carattere a corpo 11 (`13 - en * 2`) e i due metri del
progetto — 6,6 px per carattere sul carattere dei riquadri, 7,7 su quello dei
menu — il budget e' fra **8 e 9 caratteri**, cifre comprese.

    « 999 platino»   11 caratteri   73 / 85 px   sfora di brutto
    « 999 plat.»      9 caratteri   59 / 69 px   passa col metro stretto, sfora con l'altro
    « 999 pt.»        7 caratteri   46 / 54 px   passa con tutt'e due
    «9999 pt.»        8 caratteri   53 / 62 px   passa, al limite, anche a quattro cifre

⭐ ` pt.` e' l'unica forma che regge **il metro prudente e quattro cifre insieme**.
⚠️ E la scelta e' stata presa sapendo che ` platino` esiste altrove: non e'
un'incoerenza per distrazione, e' una sigla dove la sigla e' obbligata. La forma
lunga resta quella di `text.hsp:194` dovunque ci sia posto.

⚠️ **I due gettoni rimasti non si toccano, ognuno col suo motivo misurato:**
`:417` (`Sp`) ha 62 px fino all'icona dell'oro e ne usa gia' 59 con «Sp100/100»,
quindi non ha spazio per un carattere in piu'; `:423` (`Lv`) di spazio ne ha,
ma il dizionario e' in disaccordo con se' stesso (`command.hsp:17435` rende ` Lv`
con ` liv.`, `action.hsp:12383` lo lascia ` Lv`, `command.hsp:10845` scrive
`Lv(potenziale)`) e la barra di stato non e' il posto dove aprire di straforo una
questione che tocca decine di siti. `Lv` resta `Lv`.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'screen.hsp'
RIGA = 411
CERCA = '" pp"'
METTI = '" pt."'

MOTIVO = (
    "screen.hsp:411, il platino della BARRA DI STATO, il gettone accanto all'oro di "
    ":405 (toppato nella 50a). Stessa classe — letterale nudo, quinto punto cieco — "
    "ma con un vincolo di larghezza che l'oro non ha. "
    "⚠️ La misura: questo e' l'ULTIMO gettone a destra, e alla destra del testo non "
    "c'e' un altro gettone ma il bordo dello schermo. Icona a windoww-90, testo a "
    "windoww-62: 62 px in tutto. Col carattere a corpo 11 (`13 - en * 2`) e i due "
    "metri del progetto (6,6 px per carattere sul carattere dei riquadri, 7,7 su "
    "quello dei menu) il budget e' fra 8 e 9 caratteri, cifre comprese. "
    "« 999 platino» sono 11 caratteri (73/85 px) e sfora; « 999 plat.» sono 9 "
    "(59/69) e passa solo col metro stretto; « 999 pt.» sono 7 (46/54) e «9999 pt.» "
    "sono 8 (53/62): ` pt.` e' l'unica forma che regge il metro prudente e quattro "
    "cifre insieme. "
    "⚠️ La forma lunga ` platino` ESISTE gia' (text.hsp:194, `strplat = lang(\" plat\", "
    "\" platino\")`) e resta quella dovunque ci sia posto: qui la sigla non e' "
    "un'incoerenza per distrazione, e' obbligata dallo spazio. "
    "⚠️ I due gettoni rimasti non si toccano: :417 (`Sp`) ha 62 px fino all'icona "
    "dell'oro e ne usa gia' 59 con «Sp100/100»; :423 (`Lv`) e' largo ma il dizionario "
    "e' in disaccordo con se' stesso (command.hsp:17435 ` liv.`, action.hsp:12383 "
    "` Lv`, command.hsp:10845 `Lv(potenziale)`) e la barra non e' il posto dove aprire "
    "quella questione. "
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca "
    "solo con una toppa. La riga e' unica per giapponese e inglese, quindi la toppa "
    "vale per tutt'e due i rami."
)

sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')
originale = sorg[RIGA - 1]

if CERCA not in originale:
    raise SystemExit(f'{NOME}:{RIGA} non ha la forma attesa: {originale.strip()[:120]}')
if originale.count(CERCA) != 1:
    raise SystemExit(f'{NOME}:{RIGA}: `{CERCA}` compare piu\' di una volta nella riga')
for righe, eti in ((sorg, 'sorgente'), (build, 'build')):
    quante = sum(1 for r in righe if r == originale)
    if quante != 1:
        raise SystemExit(f'{NOME}:{RIGA} compare {quante} volte nel {eti}, non una: toppa ambigua')
if 'lang("' in originale:
    raise SystemExit(f'{NOME}:{RIGA}: la riga porta anche una resa')

nuova = originale.replace(CERCA, METTI)
toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova, 'motivo': MOTIVO}

esistenti = [l for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]


def _chiave(t: dict) -> tuple:
    cerca = t['cerca']
    return (t['file'], tuple(cerca) if isinstance(cerca, list) else cerca)


if _chiave(toppa) in {_chiave(json.loads(l)) for l in esistenti}:
    print('toppa gia presente, niente da fare')
else:
    # ⚠️ Si compone, si codifica in memoria e solo allora si apre: vedi la 39a.
    dati = (json.dumps(toppa, ensure_ascii=False) + '\n').encode('utf-8')
    with io.open('toppe.jsonl', 'ab') as f:
        f.write(dati)
    print(f'1 toppa aggiunta (totale {len(esistenti) + 1})')
    print(f'  {NOME}:{RIGA}')
    print(f'    - {originale.strip()}')
    print(f'    + {nuova.strip()}')
