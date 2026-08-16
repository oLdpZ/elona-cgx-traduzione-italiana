# -*- coding: utf-8 -*-
"""L'oro della barra di stato: la riga inglese che si legge SEMPRE.

`screen.hsp:405` fa `bmes "" + cdata(CDATA_GOLD, CHARA_PLAYER) + " gp"`, cioe'
il gruzzolo in fondo a destra dello schermo. Non e' una schermata che si apre:
e' la barra di stato, e sta li' in ogni istante di gioco. E' della stessa classe
delle sei toppate stamattina — letterale fuori da ogni `lang()`, quinto punto
cieco — ma di gran lunga la piu' vista di tutte.

## La resa non e' una scelta: e' la terza volta che si scrive

    command.hsp:3677   mes s + lang(" gold", " oro")      colonna «Paga» degli alleati
    text.hsp:193       strgold = lang(" gold", " oro")    il suffisso di tutto il gioco
    command.hsp:14366  mes ... + " oro"                   toppa della 50a, l'oro dell'inventario

Questa e' la quarta. ⚠️ Anche qui il sorgente dice `gp` e non `gold` **solo**
perche' e' un letterale nudo: dove c'e' una `lang()`, upstream scrive `gold`.

## La misura: 102 pixel, e ne servono al massimo 92

Il pezzo di barra e' fatto di due gettoni affiancati, ciascuno icona + numero:

    :400  sx = windoww - 220     icona dell'oro a sx, testo a sx + 28
    :406  sx = windoww - 90      icona del platino a sx

Il testo dell'oro comincia a `windoww - 192` e il primo pixel occupato alla sua
destra e' l'icona del platino a `windoww - 90`: **102 px**. Il carattere e' a
corpo 11 (`13 - en * 2`), e il progetto ha due misure di larghezza — 6,6 px per
carattere sul carattere dei riquadri e 7,7 su quello dei menu. ⭐ La toppa sta
dentro **con tutt'e due**: l'oro arriva a otto cifre, e otto cifre piu' « oro»
fanno dodici caratteri, cioe' 79 px col metro stretto e 92 col metro largo.
L'inglese ne occupa 73 e 85: il margine cala di sette pixel e resta positivo in
ogni caso.

⚠️ **I tre gettoni vicini NON si toccano qui**, e non per dimenticanza:

- `:411` (` pp`, il platino) ha solo **62 px** fino al bordo destro dello
  schermo, e il ` platino` che `text.hsp:194` ha gia' scelto per la forma lunga
  non ci sta: vuole una decisione sull'abbreviazione, non una toppa d'ufficio.
- `:417` (`Sp`) ne ha **62** fino all'icona dell'oro e ne occupa gia' 59 con
  «Sp100/100»: non c'e' spazio per un carattere in piu'.
- `:423` (`Lv`) e' l'unico largo, ma il dizionario stesso e' in disaccordo con
  se' stesso — `command.hsp:17435` rende ` Lv` con ` liv.`, `action.hsp:12383`
  lo lascia ` Lv` — e una barra di stato non e' il posto dove aprire la
  questione di straforo.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'screen.hsp'
RIGA = 405
CERCA = '" gp"'
METTI = '" oro"'

MOTIVO = (
    "screen.hsp:405, l'oro della BARRA DI STATO: `bmes \"\" + cdata(CDATA_GOLD, "
    "CHARA_PLAYER) + \" gp\"`, il gruzzolo in fondo a destra. Non e' una schermata "
    "che si apre, e' quel che si legge in ogni istante di gioco. "
    "⭐ La resa e' la quarta scrittura della stessa cosa, non una scelta nuova: "
    "command.hsp:3677 e text.hsp:193 (`strgold`) hanno gia' `lang(\" gold\", \" oro\")`, "
    "e command.hsp:14366 e' la toppa gemella della 50a per l'oro dell'inventario. "
    "Anche qui il sorgente dice `gp` e non `gold` solo perche' e' un letterale nudo. "
    "⚠️ La misura: il testo comincia a windoww-192 (icona a windoww-220, testo a "
    "+28) e il primo pixel occupato alla sua destra e' l'icona del platino a "
    "windoww-90, cioe' 102 px. Col carattere a corpo 11 (`13 - en * 2`) e l'oro a "
    "otto cifre servono dodici caratteri: 79 px col metro da 6,6 e 92 con quello da "
    "7,7. Sta dentro con tutt'e due; l'inglese ne occupava 73 e 85. "
    "⚠️ I gettoni vicini non si toccano: :411 (` pp`) ha 62 px fino al bordo dello "
    "schermo e il ` platino` di text.hsp:194 non ci sta; :417 (`Sp`) ne ha 62 e ne "
    "usa gia' 59 con «Sp100/100»; :423 (`Lv`) e' largo ma il dizionario e' in "
    "disaccordo con se' stesso (command.hsp:17435 dice ` liv.`, action.hsp:12383 "
    "lascia ` Lv`). "
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca "
    "solo con una toppa. E' il quinto punto cieco, misurato da `scratchpad/nudi_en.py` "
    "nella 49a e classificato da `scratchpad/triage_nudi.py` nella 50a. La riga e' "
    "unica per giapponese e inglese, quindi la toppa vale per tutt'e due i rami."
)

sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')
originale = sorg[RIGA - 1]

if CERCA not in originale:
    raise SystemExit(f'{NOME}:{RIGA} non ha la forma attesa: {originale.strip()[:120]}')
if originale.count(CERCA) != 1:
    raise SystemExit(f'{NOME}:{RIGA}: `{CERCA}` compare piu\' di una volta nella riga')
# ⚠️ Una toppa si aggancia al testo, non al numero di riga: dev'essere unica, e
#    nel sorgente e nella build insieme (li' e' dove verra' applicata).
for righe, eti in ((sorg, 'sorgente'), (build, 'build')):
    quante = sum(1 for r in righe if r == originale)
    if quante != 1:
        raise SystemExit(f'{NOME}:{RIGA} compare {quante} volte nel {eti}, non una: toppa ambigua')
# ⚠️ Regola della 46a: una toppa e una resa non stanno sulla stessa riga.
if 'lang("' in originale:
    raise SystemExit(f'{NOME}:{RIGA}: la riga porta anche una resa')

nuova = originale.replace(CERCA, METTI)
toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova, 'motivo': MOTIVO}

esistenti = [l for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]
gia = {(json.loads(l)['file'], json.loads(l)['cerca']
        if isinstance(json.loads(l)['cerca'], str) else tuple(json.loads(l)['cerca']))
       for l in esistenti}

if (NOME, originale) in gia:
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
