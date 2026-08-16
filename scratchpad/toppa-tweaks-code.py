# -*- coding: utf-8 -*-
"""Le ultime quattro righe inglesi di `custom_tweaks.hsp`, fuori dai menu.

Chiusi i sette menu del pannello, il file ne teneva ancora **quattro**, e
nessuna delle quattro stava nelle 190 righe che la 50a aveva contato: sono
fuori dai `*…TweakMenu_loop` e quindi fuori dal blocco che `triage_nudi
--routine` mostra come «una schermata sola».

    :527, :535  in `*ToggleTweakChallenge` — le due conferme delle sfide
    :2009       in `*ZeomeCustomAI` — la battuta di Zeome in combattimento
    :1679       «Nani?!», che si lascia in inglese apposta (vedi il lotto dei
                ritocchi vari)

💡 **Sono la coda che il conteggio per schermata non vede.** Il criterio della
50a — «il testo non e' sparso, sta in blocchi, e un blocco e' una schermata
sola» — trova le 190 righe dei menu e non queste tre, che pero' il giocatore
legge di sicuro: due sono domande a cui deve rispondere e la terza esce in
mezzo a uno scontro. Chiudere il file vuol dire guardare anche fuori dai
blocchi.

## Le due conferme

`:527` e `:535` non sono voci di menu ma `txt` seguiti da `promptYesNo`: vanno
nel registro dei messaggi, che va a capo da solo. Non hanno tetto di larghezza.
⚠️ «challenge» qui e' la **singola partita a regole dure** che si vince o si
perde — «This will end the challenge and reset progress» — quindi «sfida»,
come a :1880, e non «difficolta'» come nel nome della categoria.

## La battuta di Zeome

`:2009` compone il testo con `name(cc)`, che e' una funzione di **contenuto**:
resta dov'e' e l'italiano ci si appoggia dietro. «grin» il progetto lo rende
«ghigno» / «sogghignare» (action.hsp:250 «*ghigno*», :6472 «Sogghigni»), e
«wickedly» e' il modo: «sogghigna con malizia».
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'custom_tweaks.hsp'

CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca solo "
    "con una toppa. Quinto punto cieco (`nudi_en.py`, 49a; `triage_nudi.py`, 50a). "
    "💡 E sta FUORI dai menu del pannello, cioe' fuori dal blocco che `triage_nudi "
    "--routine` mostra come una schermata sola: e' la coda che il conteggio per "
    "schermata non vede."
)

VOCI = [
    (527, [('"This is a challenge tweak. Are you sure to enable this?"',
            '"Questo e\' un ritocco di sfida. Vuoi davvero accenderlo?"')], 1,
     "La conferma che compare accendendo un ritocco del menu di difficolta' "
     "(`*ToggleTweakChallenge`, :524-:542). Non e' una voce di menu ma un `txt` seguito "
     "da `promptYesNo`: va nel registro dei messaggi, che va a capo da solo, e non ha "
     "tetto di larghezza. ⚠️ «challenge» qui e' la singola partita a regole dure — "
     "«sfida» — come a :1880, e non «difficolta'» come nel nome della categoria "
     "(custom_tweaks.hsp:109). ⭐ La forma della domanda e' quella che il gioco usa gia' "
     "dappertutto: «Vuoi davvero…?» (action.hsp:3187, :13786, map.hsp:770). "),
    (535, [('"This will end the challenge and reset progress. Are you sure to disable this?"',
            '"Cosi\' la sfida finisce e i progressi si azzerano. Vuoi davvero spegnerlo?"')], 1,
     "La conferma che compare spegnendo un ritocco di sfida: azzera il contatore che "
     "`GetTStatusProgress` mostra accanto alla voce («12 giorni di sopravvivenza», «3 "
     "mesi pagati»). ⚠️ L'inglese mette il soggetto in testa («This will end…»); "
     "l'italiano lo scioglie con «Cosi'», perche' «Questo finira' la sfida» non e' "
     "italiano. "),
    (2009, [('"" + name(cc) + " grins wickedly."', '"" + name(cc) + " sogghigna con malizia."')], 1,
     "La battuta che Zeome fa quando si carica addosso tutte le protezioni "
     "(`*ZeomeCustomAI`, :2007-:2009): esce in rosso (`tcol@txtfunc = 255, 51, 100`) in "
     "mezzo allo scontro. ⚠️ `name(cc)` e' una funzione di CONTENUTO e resta dov'e': "
     "l'italiano ci si appoggia dietro senza toccarla. ⭐ «grin» il progetto lo rende "
     "«ghigno»/«sogghignare» (action.hsp:250 «*ghigno*», :6472 «Sogghigni», :19088), e "
     "«wickedly» e' il modo. 💡 E' l'unica riga di `custom_tweaks.hsp` che non sta in un "
     "menu ma in un combattimento. "),
]

sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')

nuove = []
for riga, sostituzioni, attese, motivo in VOCI:
    originale = sorg[riga - 1]
    if build[riga - 1] != originale:
        raise SystemExit(f"{NOME}:{riga}: la build ha gia' una resa su questa riga")
    if 'lang("' in originale:
        raise SystemExit(f'{NOME}:{riga}: la riga porta una resa (regola della 46a)')
    for righe_, eti in ((sorg, 'sorgente'), (build, 'build')):
        quante = sum(1 for r in righe_ if r == originale)
        if quante != attese:
            raise SystemExit(
                f'{NOME}:{riga} compare {quante} volte nel {eti}, non {attese}')

    nuova = originale
    for cerca, metti in sostituzioni:
        if nuova.count(cerca) != 1:
            raise SystemExit(
                f'{NOME}:{riga}: `{cerca[:60]}` compare {nuova.count(cerca)} volte, non una')
        nuova = nuova.replace(cerca, metti)
    if nuova == originale:
        raise SystemExit(f'{NOME}:{riga}: la toppa non cambierebbe niente')
    try:
        nuova.encode('cp932')
    except UnicodeEncodeError as errore:
        raise SystemExit(f'{NOME}:{riga}: testo che CP932 non sa scrivere ({errore})')

    toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova,
             'motivo': motivo + CLASSE, '_riga': riga, '_quante': attese}
    nuove.append(toppa)

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
        print(f"  :{t['_riga']}  {t['sostituisci'].strip()[:110]}")
