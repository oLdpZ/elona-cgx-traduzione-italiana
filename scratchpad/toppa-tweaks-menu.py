# -*- coding: utf-8 -*-
"""Il pannello dei ritocchi: il menu principale e le intestazioni di tutti e otto.

`custom_tweaks.hsp` e' il blocco piu' grosso del quinto punto cieco — **259
righe** secondo `triage_nudi.py` — ed e' il pannello di opzioni del mod: otto
menu con titoli, voci e descrizioni, tutto in inglese e tutto fuori da ogni
`lang()`. Questo lotto ne prende **24 righe** ma ne chiude **48**, perche' otto
di quelle 24 sono `tutte`.

## Il vocabolario: «ritocchi», e perche' non «opzioni» ne' «impostazioni»

⭐ La parola va scelta una volta e vale per tutto il pannello. **«Impostazioni» e'
gia' presa**: `command.hsp:17285` e `:17538` rendono cosi' «Game Setting» e
«Setting», cioe' il menu di configurazione del gioco vero, che e' un'altra
schermata. Chiamare «Opzioni» anche questo darebbe al giocatore due voci diverse
con lo stesso nome.
✅ **«Ritocchi»** e' quel che «tweak» dice — un aggiustamento piccolo e
facoltativo — ed e' libero.

⭐ **E «IA» si fissa qui.** Nessuna voce di dizionario aveva mai reso «AI» in
tutto il progetto: e' la prima volta, e la scelta si portera' dietro le sessanta
righe di `custom_ai.hsp` («Tactical Instructions», «Currently using custom AI»).
«IA» e' l'abbreviazione italiana normale e tiene le voci corte.

## Otto righe su ventiquattro sono `tutte`, e chiudono da sole 32 righe

Il pannello ripete se' stesso: ogni menu rialza lo stesso titolo e la stessa
riga di ritorno. Sono esattamente il caso per cui `tutte` e' nata nella 50a.

    "Tweak Setup", strhint3b               x6
    "Tweak Setup", strhint2 + strhint3b    x2
    "Configure Tweaks"                     x8
    "Return."                              x5
    "Return to the previous menu."         x9
    "Go back."  (listn(0, listmax - 1))    x2

⚠️ `"Go back."` ha **tre forme diverse** — `listn(0, 15)`, `listn(0, 31)` e
`listn(0, listmax - 1)` — e solo l'ultima e' ripetuta. Le prime due sono toppe
normali: `tutte` si dichiara dove serve, non per comodita'.

## La larghezza

La finestra e' 640 (`display_window …, 640, 448`). Le voci escono a `wx + 64` col
carattere a corpo 12, le descrizioni a `wx + 38` a corpo 11: **602 px** per la
riga piu' lunga, che in italiano e' «Accende e spegne i ritocchi che riportano
indietro alcune meccaniche.» — 69 caratteri, cioe' 455 px col metro da 6,6 e 531
con quello da 7,7. Dentro con tutt'e due.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'custom_tweaks.hsp'

CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca solo "
    "con una toppa. Quinto punto cieco (`nudi_en.py`, 49a; `triage_nudi.py`, 50a), dove "
    "`custom_tweaks.hsp` e' il blocco piu' grosso con 259 righe."
)
PANNELLO = (
    "Sta nel pannello dei ritocchi di Custom-GX (`custom_tweaks.hsp`), otto menu di "
    "opzioni facoltative. ⭐ «Ritocchi» e' la parola scelta per «tweak» in tutto il "
    "pannello: «Impostazioni» era gia' presa dal menu di configurazione del gioco "
    "(command.hsp:17285 e :17538), e due voci con lo stesso nome sarebbero un inganno. "
    "La finestra e' 640 e le descrizioni escono a `wx + 38`: 602 px, cioe' la riga "
    "italiana piu' lunga (69 caratteri) sta dentro con tutt'e due i metri del progetto. "
)

# (riga, [(cerca, metti)], occorrenze_attese, motivo)
# occorrenze_attese > 1 => la toppa nasce con `"tutte": true`
VOCI = [
    # ── le intestazioni che tutti gli otto menu ripetono ────────────────────
    (99, [('"Tweak Setup"', '"Ritocchi"')], 6,
     "Il titolo della finestra, rialzato uguale da sei menu su otto. ⭐ E' una toppa "
     "`tutte`: le sei occorrenze sono la stessa riga byte per byte e vogliono la stessa "
     "resa, che e' il caso per cui la deroga e' nata nella 50a. "),
    (798, [('"Tweak Setup"', '"Ritocchi"')], 2,
     "Il titolo della finestra negli altri due menu, che si distinguono solo per il "
     "suggerimento (`strhint2 + strhint3b` invece di `strhint3b`): riga diversa, stessa "
     "resa, toppa `tutte` sua. "),
    (101, [('"Configure Tweaks"', '"Scegli che cosa ritoccare"')], 8,
     "La riga di testa che `screen_drawMsg2` disegna sotto il titolo, uguale in tutti e "
     "otto i menu. ⚠️ L'inglese e' un imperativo che nomina l'oggetto («Configure "
     "Tweaks»); l'italiano dice al giocatore che cosa sta per fare, che e' quel che "
     "serve in una riga di testa. Toppa `tutte`. "),
    (264, [('"Return."', '"Indietro."')], 5,
     "L'ultima voce dell'elenco in cinque menu (`listn(0, listmax - 1)`). Toppa `tutte`. "),
    (321, [('"Return to the previous menu."', '"Torna al menu precedente."')], 9,
     "La descrizione della voce di ritorno, ripetuta da nove menu. E' la riga piu' "
     "ripetuta di tutto il file. Toppa `tutte`. "),
    (855, [('"Go back."', '"Indietro."')], 2,
     "L'ultima voce dell'elenco in due altri menu. ⚠️ `\"Go back.\"` ha TRE forme nel "
     "file — `listn(0, 15)`, `listn(0, 31)` e `listn(0, listmax - 1)` — e solo questa e' "
     "ripetuta: `tutte` si dichiara dove serve, non per comodita'. Le altre due sono "
     "toppe normali. "),
    (819, [('"Go back."', '"Indietro."')], 1,
     "La voce di ritorno del menu dei ritocchi al gioco (`listn(0, 15)`), che ha un "
     "indice fisso e quindi una riga unica. "),
    (836, [('"Go back."', '"Indietro."')], 1,
     "La voce di ritorno del secondo blocco dei ritocchi al gioco (`listn(0, 31)`). "),

    # ── il menu principale: le otto categorie ───────────────────────────────
    (104, [('"UI Tweaks"', '"Ritocchi all\'interfaccia"')], 1,
     "La prima categoria del menu principale. "),
    (105, [('"Convenience Tweaks"', '"Ritocchi di comodita\'"')], 1,
     "La seconda categoria: i ritocchi che tolgono attriti (conferme, raccolte "
     "automatiche, scorciatoie). "),
    (106, [('"AI Tweaks"', '"Ritocchi all\'IA"')], 1,
     "La terza categoria. ⭐ «IA» si fissa QUI: nessuna voce di dizionario aveva mai "
     "reso «AI» in tutto il progetto, e questa scelta si portera' dietro le sessanta "
     "righe di custom_ai.hsp («Tactical Instructions», «Currently using custom AI»). "
     "E' l'abbreviazione italiana normale e tiene le voci corte. "),
    (107, [('"Gameplay Tweaks"', '"Ritocchi al gioco"')], 1,
     "La quarta categoria: i ritocchi che riportano indietro meccaniche cambiate da "
     "monte. "),
    (108, [('"Extra Gameplay Tweaks"', '"Ritocchi extra al gioco"')], 1,
     "La quinta categoria: quelli che aggiungono roba nuova invece di riportare "
     "indietro. "),
    (109, [('"Challenge Tweaks"', '"Ritocchi di difficolta\'"')], 1,
     "La sesta categoria. ⚠️ «Challenge» qui non e' una sfida singola ma il livello di "
     "durezza della partita — la descrizione lo dice, «makes your life harder» — quindi "
     "«difficolta'» e non «sfida». "),
    (110, [('"Miscellaneous Tweaks"', '"Ritocchi vari"')], 1,
     "La settima categoria. "),
    (111, [('"Exit"', '"Esci"')], 1,
     "L'ottava voce del menu principale, che chiude il pannello. ⚠️ Non e' «Indietro»: "
     "da qui non si torna a un menu di sopra, si esce. "),

    # ── il menu principale: le otto descrizioni ─────────────────────────────
    (127, [('"Toggle tweaks that target UI functions."',
            '"Accende e spegne i ritocchi all\'interfaccia."')], 1,
     "La descrizione della prima categoria. ⚠️ «Toggle» e' un verbo che l'italiano non "
     "ha in una parola: «accende e spegne» dice la stessa cosa e resta corto. "),
    (130, [('"Toggle tweaks that make things more convenient."',
            '"Accende e spegne i ritocchi che rendono il gioco piu\' comodo."')], 1,
     "La descrizione della seconda categoria. "),
    (133, [('"Toggle tweaks that modify the AI of NPCs."',
            '"Accende e spegne i ritocchi all\'intelligenza dei PNG."')], 1,
     "La descrizione della terza categoria. ⚠️ Qui per esteso («intelligenza dei PNG») "
     "e non con la sigla: la voce di menu abbrevia perche' ha poco posto, la "
     "descrizione ha una riga intera e puo' spiegare. «PNG» e' il termine che il "
     "progetto usa gia' per gli NPC. "),
    (136, [('"Toggle tweaks that reverts some of the gameplay mechanics."',
            '"Accende e spegne i ritocchi che riportano indietro alcune meccaniche."')], 1,
     "La descrizione della quarta categoria. E' la riga italiana piu' lunga del lotto, "
     "69 caratteri: 455 px col metro da 6,6 e 531 con quello da 7,7, su 602 disponibili. "),
    (139, [('"Toggle tweaks that introduces extra game options."',
            '"Accende e spegne i ritocchi che aggiungono opzioni di gioco."')], 1,
     "La descrizione della quinta categoria. "),
    (142, [('"Toggle tweaks that makes your life harder."',
            '"Accende e spegne i ritocchi che ti rendono la vita difficile."')], 1,
     "La descrizione della sesta categoria. ⭐ L'inglese e' colloquiale («makes your "
     "life harder») e l'italiano lo resta: e' la riga che dice al giocatore che quei "
     "ritocchi servono a peggiorargli la vita apposta. "),
    (145, [('"Toggle tweaks that don\'t fall into any other category."',
            '"Accende e spegne i ritocchi che non stanno in nessun\'altra categoria."')], 1,
     "La descrizione della settima categoria. "),
    (148, [('"Exit the menu."', '"Esce dal menu."')], 1,
     "La descrizione della voce di uscita. ⚠️ Terza persona come tutte le altre "
     "descrizioni del pannello, non imperativo: la colonna aveva gia' scelto. "),
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
    # ⚠️ `tutte` non e' una scusa per non guardare: le occorrenze si contano e
    #    devono essere quelle che si e' deciso di toccare, non una di piu'.
    for righe_, eti in ((sorg, 'sorgente'), (build, 'build')):
        quante = sum(1 for r in righe_ if r == originale)
        if quante != attese:
            raise SystemExit(
                f'{NOME}:{riga} compare {quante} volte nel {eti}, non {attese}: '
                'la riga e\' cambiata, il conto va rifatto a mano'
            )

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

    toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova}
    if attese > 1:
        toppa['tutte'] = True
    toppa['motivo'] = motivo + PANNELLO + CLASSE
    toppa['_riga'] = riga
    toppa['_quante'] = attese
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
    coperte = sum(t['_quante'] for t in da_scrivere)
    print(f'{len(da_scrivere)} toppe aggiunte (totale {len(esistenti) + len(da_scrivere)}), '
          f'{coperte} righe coperte')
    for t in da_scrivere:
        marca = f" x{t['_quante']}" if t['_quante'] > 1 else ''
        print(f"  :{t['_riga']}{marca}")
        print(f"    - {t['cerca'].strip()[:105]}")
        print(f"    + {t['sostituisci'].strip()[:105]}")
