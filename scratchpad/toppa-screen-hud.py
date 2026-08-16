# -*- coding: utf-8 -*-
"""La barra di stato: 18 righe delle 23, e cinque che restano fuori apposta.

`screen.hsp:*screen_drawStatus` e' quel che sta a schermo **sempre**. Stamattina
ne sono uscite due (l'oro e il platino, `:405` e `:411`); qui si chiude il resto:
gli otto effetti di campo, la battaglia navale, il sacco da allenamento, la resa
in arena, il conto alla rovescia della Chiamata alla ribalta.

## Gli otto effetti di campo hanno gia' un nome italiano, e non e' questo file

⭐⭐ **Sei nomi su otto sono gia' stati resi altrove**, e la barra deve dire
quello che dice il libro degli incantesimi, non una traduzione nuova:

    [電磁獄]      E-Mag Cage        skill.hsp:1812   Gabbia elettromagnetica
    [弦葬世界]     Wire World        skill.hsp:1820   Mondo di fili
    [暴虐の庭園]    Violent Garden    skill.hsp:1704   Giardino violento
    [ロックラッシュ]  Rocrush           skill.hsp:1824   Frantumaroccia (ロックラッシャー)
    [狂気満ちる劇場]  Crazy Theater     text.hsp:2372    Teatro impazzito
    *カーテンコール*  *Curtain Call*    proc.hsp:4650    *Chiamata alla ribalta*

⚠️ `[ロックラッシュ]` non e' esattamente il nome della capacita' (`ロックラッシャー`,
«Rocrusher»): il campo perde il suffisso. L'italiano riusa lo stesso nome perche'
il giocatore deve poter collegare l'effetto alla capacita' che l'ha creato, e
«Frantumaroccia» e' quel che legge nel libro.
⚠️ `[懲罰結界]` («Reprimand Room») non ha un gemello esatto: la capacita' vicina e'
`懲罰の光` = «Punizione» (skill.hsp:1948), e 結界 e' una barriera magica, non una
stanza. ✅ «[Barriera punitiva]», che dice il giapponese e non l'inglese.

## La larghezza c'e', e l'ho misurata sulla configurazione vera

Le etichette di campo escono a `inf_clockw + 6`. Con la `config.txt` di questa
macchina (`clockW. 120`, `windowW. 1920`) sono **x = 126**, e su quella riga
(`inf_clocky + 50`) l'unica altra cosa che si disegna e' a `inf_clockw + 80`,
cioe' x = 200: sono i **fuori-campo della battaglia finale**
(`GDATA_FLAG_CUT_IN_MESSAGE_1`, `:1351`-`:1370`), che scrivono righe di sessanta
caratteri e sfondano quel confine gia' in inglese — segno che le due cose non
convivono. Oltre a loro la riga e' libera fino al bordo.
⭐ **E il conto regge anche alla risoluzione minima**: a 800 px di larghezza
«[Gabbia elettromagnetica]» (25 caratteri, 165-193 px secondo i due metri del
progetto) finisce a 319, e « *Chiamata alla ribalta* » — che parte da
`inf_clockw + 380`, cioe' 500 — finisce a 693.
⚠️ Il caso opposto esiste e non e' colpa nostra: `:1811` in inglese e' lungo 52
caratteri e a 800 px sfonda gia' da solo. L'italiano e' **piu' corto**, quindi la
toppa migliora anche quello.

## Le cinque che restano fuori, ognuna col suo motivo

- `:417` (`Sp`) ha 62 px fino all'icona dell'oro e ne usa gia' 59 con
  «Sp100/100»: non c'e' spazio per un carattere in piu'. Gia' scritto nella
  toppa del platino.
- `:423` (`Lv`) di spazio ne ha, ma il dizionario e' in disaccordo con se' stesso
  (`command.hsp:17435` ` liv.`, `action.hsp:12383` ` Lv`) e la barra non e' il
  posto dove aprire quella questione.
- `:1031` (`"PF"`) e' l'etichetta della piastrella che conta le carte del poker
  (`pokert@cgx`), larga 65 px e con due caratteri dentro. Non c'e' niente nel
  sorgente che dica di che cosa sia la sigla, e tradurre una sigla che non si e'
  capita e' un modo di sbagliare in silenzio.
- `:1125` (`"*debug*"`) e `:1128` (`"loop…sub…"`) escono solo con
  `GDATA_WIZARD == 1`: sono spie da sviluppatore, non testo di gioco.
  ⚠️⚠️ **E qui il triage sbaglia a favore del lavoro**: `triage_nudi.py` le
  chiama `testo` perche' la sua regola guarda il prefisso `dbg_` del nome della
  routine, e queste stanno dentro `screen_drawStatus`, che di suo e' la barra
  vera. La regola resta giusta — un nome non e' una prova — ma il suo punto cieco
  e' questo: **il debug guardato da una variabile invece che da una routine**.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'screen.hsp'

CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca solo "
    "con una toppa. Quinto punto cieco (`nudi_en.py`, 49a; `triage_nudi.py`, 50a)."
)
BARRA = (
    "Sta in `screen.hsp:*screen_drawStatus`, cioe' la barra di stato, che e' a schermo "
    "SEMPRE. "
)
CAMPO = (
    "E' una delle otto etichette di effetto di campo (`CDATA_FIELD_EFFECT`), scritte "
    "in due rami gemelli `if ( jp )` / `if ( en )`. ⚠️ La misura: escono a "
    "`inf_clockw + 6` (x = 126 con `clockW. 120`), e su quella riga l'unica altra cosa "
    "e' a `inf_clockw + 80` — i fuori-campo della battaglia finale (:1351-:1370), che "
    "sfondano quel confine gia' in inglese, segno che le due cose non convivono. Oltre "
    "a loro la riga e' libera fino al bordo, e il nome italiano piu' lungo finisce a "
    "319 px anche alla risoluzione minima di 800. "
)

# (riga, [(cerca, metti), ...], motivo)
VOCI = [
    (1157, [('"<Order of Chaos>"', '"<Ordine del caos>"')],
     "L'effetto di campo -2 (giapponese 「混沌の秩序」, «l'ordine del caos»). " + CAMPO),
    (1167, [('"<Doomsday sky>"', '"<Cielo della fine>"')],
     "L'effetto di campo -1 (giapponese 「終末の空」). ⭐ 終末 e' gia' reso «fine» nel "
     "diario, dove 「終末の発生回数」 e' diventato «Ragnarok scatenati», e in "
     "proc.hsp:4641 («e' giunto il giorno della fine»). " + CAMPO),
    (1177, [('"[E-Mag Cage]"', '"[Gabbia elettromagnetica]"')],
     "L'effetto di campo 1 (giapponese 「電磁獄」). ⭐ Il nome e' gia' deciso: "
     "skill.hsp:1812 rende 「電磁獄」 con «Gabbia elettromagnetica». La barra deve dire "
     "quel che dice il libro degli incantesimi. " + CAMPO),
    (1187, [('"[Wire World]"', '"[Mondo di fili]"')],
     "L'effetto di campo 2 (giapponese 「弦葬世界」). ⭐ skill.hsp:1820 rende gia' «Mondo "
     "di fili». " + CAMPO),
    (1197, [('"[Violent Garden]"', '"[Giardino violento]"')],
     "L'effetto di campo 3 (giapponese 「暴虐の庭園」). ⭐ skill.hsp:1704 rende gia' "
     "«Giardino violento». " + CAMPO),
    (1207, [('"[Rocrush]"', '"[Frantumaroccia]"')],
     "L'effetto di campo 4 (giapponese 「ロックラッシュ」). ⚠️ Il campo NON porta lo stesso "
     "nome della capacita': quella e' 「ロックラッシャー」 («Rocrusher», skill.hsp:1824, "
     "«Frantumaroccia»), il campo perde il suffisso. L'italiano riusa comunque il nome "
     "della capacita', perche' il giocatore deve poter collegare l'effetto a quel che "
     "l'ha creato. " + CAMPO),
    (1217, [('"[Crazy Theater]"', '"[Teatro impazzito]"')],
     "L'effetto di campo 5 (giapponese 「狂気満ちる劇場」). ⭐ text.hsp:2372 rende gia' "
     "«[Teatro impazzito]». " + CAMPO),
    (1227, [('"[Reprimand Room]"', '"[Barriera punitiva]"')],
     "L'effetto di campo 6 (giapponese 「懲罰結界」). ⚠️ Qui non c'e' un gemello esatto: "
     "la capacita' vicina e' 「懲罰の光」 = «Punizione» (skill.hsp:1948), e 結界 e' una "
     "barriera magica, non una stanza. L'italiano segue il giapponese e non l'inglese, "
     "che aveva inventato la «Room». " + CAMPO),

    (1243, [('"You can surrender by pressing the ESC key."',
             '"Puoi ritirarti premendo il tasto ESC."')],
     "Il messaggio dell'arena delle bestie (giapponese :1238, 「ESCキーで棄権できる」). "
     "Esce a `inf_clockw + 380`, cioe' x = 500, e l'italiano e' piu' corto "
     "dell'inglese: 37 caratteri contro 42. " + BARRA),

    (1252, [('" dmg / "', '" danni / "'), ('" turn "', '" turni "')],
     "Il contatore del sacco da allenamento mentre lo si colpisce. ⚠️ Questa riga non "
     "ha nessun ramo di lingua: e' inglese anche per chi gioca in giapponese. " + BARRA),
    (1257, [('"Total "', '"In tutto "'), ('" dmg! / "', '" danni! / "'),
            ('" turn "', '" turni "')],
     "Il totale del sacco da allenamento a fine prova. Come :1252, senza rami di "
     "lingua. " + BARRA),

    (1273, [('"Ship-Condition < "', '"Stato nave < "')],
     "Lo stato dello scafo nella battaglia navale (giapponese :1270, 「船の状態：」). "
     "Esce a `inf_clockw + 230`, x = 350, e l'italiano e' piu' corto dell'inglese. "
     + BARRA),
    (1282, [('"Opponent\'s Ship-Condition < "', '"Nave nemica < "')],
     "Lo stato della nave avversaria (giapponese :1279, 「相手の船の状態：」). "
     "⭐ Da 28 caratteri a 15: l'italiano dimezza. " + BARRA),
    (1313, [('"Drifters-Limit < "', '"Naufraghi < "')],
     "I naufraghi raccolti in mare (giapponese :1310, 「回収人数：n/m人」, «quante persone "
     "recuperate»). ⚠️ L'inglese dice «Limit» ma il valore e' un conteggio con un "
     "massimo (`maxship`), non un limite: il giapponese conta le persone, e l'italiano "
     "fa lo stesso. " + BARRA),
    (1326, [('"Quest [turn "', '"Incarico [restano "'), ('" left]"', '" turni]"')],
     "Il conto alla rovescia dell'incarico nel campo minato (giapponese :1321, "
     "「クエスト[残りNターン]」). «Incarico» e' il termine che la bacheca usa gia'. " + BARRA),
    (1335, [('"Soul-Limit < "', '"Anime < "')],
     "Le anime che restano da salvare nella Gabbia di Amur (`AREA_AMUR_CAGE`). "
     "⚠️ Questa riga non ha ramo giapponese: e' inglese per tutti. Il contesto e' la "
     "battuta di Nehertard due righe sotto (:1339), «le anime da salvare non si "
     "possono piu' aiutare». " + BARRA),

    (1811, [('"You had better leave this place as soon as possible."',
             '"Meglio andarsene da qui, e alla svelta."')],
     "L'avviso della Chiamata alla ribalta, il meccanismo anti-AFK, quando il contatore "
     "supera i due terzi (giapponese :1806, 「早くこの場を離れたほうがいい気がする…」). "
     "⭐ L'italiano e' piu' corto: 38 caratteri contro 52. ⚠️ Non e' cosmetico — a "
     "`inf_clockw + 380` (x = 500) l'inglese sfonda gia' da solo alla risoluzione "
     "minima di 800 px, e la toppa lo rimette dentro. " + BARRA),
    (1823, [('" *Curtain Call* "', '" *Chiamata alla ribalta* "')],
     "La Chiamata alla ribalta scattata (giapponese :1818, 「*カーテンコール*」). "
     "⭐ Il nome e' gia' deciso: proc.hsp:4650 rende 「*カーテンコール*」 con «*Chiamata "
     "alla ribalta*». ⚠️ E' piu' lungo dell'inglese (25 caratteri contro 16) ma parte "
     "da x = 500 e finisce a 693 anche a 800 px di larghezza. " + BARRA),
]

sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')

nuove = []
for riga, sostituzioni, motivo in VOCI:
    originale = sorg[riga - 1]
    if build[riga - 1] != originale:
        raise SystemExit(f"{NOME}:{riga}: la build ha gia' una resa su questa riga")
    if 'lang("' in originale:
        raise SystemExit(f'{NOME}:{riga}: la riga porta una resa (regola della 46a)')
    for righe_, eti in ((sorg, 'sorgente'), (build, 'build')):
        quante = sum(1 for r in righe_ if r == originale)
        if quante != 1:
            raise SystemExit(f'{NOME}:{riga} compare {quante} volte nel {eti}: toppa ambigua')

    nuova = originale
    for cerca, metti in sostituzioni:
        if nuova.count(cerca) != 1:
            raise SystemExit(f'{NOME}:{riga}: `{cerca}` compare {nuova.count(cerca)} volte, non una')
        nuova = nuova.replace(cerca, metti)
    if nuova == originale:
        raise SystemExit(f'{NOME}:{riga}: la toppa non cambierebbe niente')
    try:
        nuova.encode('cp932')
    except UnicodeEncodeError as errore:
        raise SystemExit(f'{NOME}:{riga}: testo che CP932 non sa scrivere ({errore})')

    nuove.append({'file': NOME, 'cerca': originale, 'sostituisci': nuova,
                  'motivo': motivo + CLASSE, '_riga': riga})

esistenti = [l for l in io.open('toppe.jsonl', encoding='utf-8') if l.strip()]


def _chiave(t: dict) -> tuple:
    cerca = t['cerca']
    return (t['file'], tuple(cerca) if isinstance(cerca, list) else cerca)


gia = {_chiave(json.loads(l)) for l in esistenti}
da_scrivere = [t for t in nuove if _chiave(t) not in gia]

if not da_scrivere:
    print('toppe gia presenti, niente da fare')
else:
    # ⚠️ Si compone, si codifica in memoria e solo allora si apre: vedi la 39a.
    dati = ''.join(
        json.dumps({k: v for k, v in t.items() if not k.startswith('_')},
                   ensure_ascii=False) + '\n'
        for t in da_scrivere
    ).encode('utf-8')
    with io.open('toppe.jsonl', 'ab') as f:
        f.write(dati)
    print(f'{len(da_scrivere)} toppe aggiunte (totale {len(esistenti) + len(da_scrivere)})')
    for t in da_scrivere:
        print(f"  :{t['_riga']}")
        print(f"    - {t['cerca'].strip()[:110]}")
        print(f"    + {t['sostituisci'].strip()[:110]}")
