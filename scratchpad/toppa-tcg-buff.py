# -*- coding: utf-8 -*-
"""Il corpo della finestra del gioco di carte: gli esiti e i rifiuti degli dei.

Quarantuno righe di `tcg.hsp` che scrivono `buff` con un letterale inglese nudo,
cioe' l'**undicesimo punto cieco** (`scratchpad/buff_en.py`, 59a). Non passano
da nessuna `lang()`, non hanno firma, non hanno voce di dizionario: si toccano
solo con una toppa.

## Le diciotto che si leggono alla fine di OGNI partita

`:2804`-`:2821` sono gli esiti del duello, e il corpo della finestra che
`*re_select` disegna quando la partita finisce. Qualunque cosa succeda, una di
queste diciotto compare in mezzo allo schermo.

⭐ **E `:2803` era gia' reso** — «Esito imprevisto, da segnalare a chi ha scritto
il gioco.» — mentre i diciotto fratelli intorno no. E' la forma di
`item_func.hsp` nella 34a: un caso toppato per volta, senza sapere che era una
famiglia. Questa toppa chiude la famiglia.

## Le ventitre' che spiegano perche' il mazzo non si puo' usare

`:2575`-`:2600`, nel Gioco delle Ombre (`yaminogemu@tcg == 1`): sedici righe che
dicono che un dio non assiste chi duella, e otto che dicono che una carta la
puo' usare solo chi crede nel suo dio.

⚠️ **`:2577` e' commentata nel sorgente** e resta fuori: e' la riga di Mani, che
pero' vive a `:2586` col creatura evoluto. E' la regola della rete 6 applicata a
mano, perche' le toppe non hanno reti.

## Il vocabolario, tutto gia' fissato altrove

    Eternal League      «il Patto Eterno»       db_creature.hsp:46255, main.hsp:4017
    exile               «l'esiliato»            db_card.hsp:14520
    golden knight       «il cavaliere dorato»   db_card.hsp:14533
    android             «l'androide»            db_card.hsp:14494
    cute fairy          «la fatina»             db_card.hsp:14481
    black cat           «il gatto nero»         db_card.hsp:14468
    defender            «il difensore»          db_card.hsp:14546
    black angel         «l'angelo nero»         db_card.hsp:14507
    goose               «l'oca»                 db_card.hsp:14455
    Life                «Vita»                  toppa del tavolo, 53a
    Zeome               invariato               db_card.hsp:10397
    Meshera             «il Meshera»            action.hsp:17270
    Unitdead            «unimorto»              db_card.hsp:3455
    Chaos Child         «il Figlio del Caos»    db_card.hsp:1648

⚠️ **«Termination Card Game (TCG)» non aveva una resa, e non ne prende una.**
Il progetto chiama le due porte «Duello!» e «Gioco delle Ombre!»
(`command.hsp:6163`, `:6166`, dal giapponese 決闘 e 闇のゲーム), e le carte
parlano di 「子供向けのカードゲーム」. Un nome proprio inventato qui
contraddirebbe quelle tre. Le rese dicono **«il gioco di carte»**, che e' quel
che il giapponese dice e quel che il giocatore capisce.

## ⚠️⚠️ Il genere di chi gioca, che qui morde due volte

`:2804` e `:2805` in inglese sono «You flipped the table and leave the game»: in
italiano «te ne sei andato» porta il genere di chi legge. Le rese usano
**«hai … e lasciato la partita»**, dove il participio con `avere` non concorda.
`:2817` «You are BANNED!» ha lo stesso problema con «squalificato»: la resa dice
**«SEI FUORI DAL GIOCO!»**, che e' invariante. Su `:2816` invece si puo': il
participio concorda con «avversario», che e' maschile per grammatica e non per
il personaggio.

## La geometria

Sono corpi, non voci di menu: `talk_conv` li manda a capo da solo
(`event.hsp:4154`) e `dy` cresce col numero di righe (`:4155`), quindi non c'e'
tetto da rispettare. ⚠️ Non e' cosi' per le voci di `chatList` nella stessa
finestra: quelle hanno il tetto della rete 15.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'tcg.hsp'

CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO scritto in `buff`: non passa da nessuna `lang()`, "
    "quindi non ha firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — "
    "si tocca solo con una toppa. E' l'UNDICESIMO punto cieco (`scratchpad/buff_en.py`, "
    "59a): il CORPO della finestra dell'evento, che cade fra `nudi_en.py` (guarda i "
    "letterali che disegnano, e questo sta in un'assegnazione) e `variabili_en.py` "
    "(guarda le variabili interpolate in una `lang()`, e `buff` non ci finisce mai). "
)
PARTITA = (
    "Sta nella finestra che `*re_select` disegna alla fine di una partita a carte "
    "(`tcg.hsp:2822`), cioe' il testo che il giocatore legge in mezzo allo schermo a "
    "ogni duello concluso. ⭐ `:2803` era gia' reso e i diciotto fratelli intorno no: "
    "la forma di `item_func.hsp` nella 34a, un caso toppato per volta senza sapere che "
    "era una famiglia. "
)
MAZZO = (
    "Sta nel controllo del mazzo prima del Gioco delle Ombre (`yaminogemu@tcg == 1`, "
    "`tcg.hsp:2570`-`:2609`): se il mazzo contiene una carta che il dio del giocatore "
    "non consente, la partita non comincia e questa riga spiega perche'. ⭐ «il Patto "
    "Eterno» e' la resa gia' fissata per «the Eternal League» (`db_creature.hsp:46255`, "
    "`main.hsp:4017`), e i nomi delle otto carte vengono da `db_card.hsp`. "
    "⚠️ «Termination Card Game (TCG)» non prende un nome proprio: il progetto chiama le "
    "due porte «Duello!» e «Gioco delle Ombre!» (`command.hsp:6163`, `:6166`), e "
    "inventarne un terzo contraddirebbe quelle. "
)

_VIETA = 'The Eternal League forbids %s from assisting participants of Termination Card Game (TCG)'
_VIETA_IT = 'Il Patto Eterno vieta a %s di assistere chi duella nel gioco di carte'
_SOLO = 'Only a believer of %s can use %s in Termination Card Game (TCG)'
_SOLO_IT = 'Solo un fedele di %s puo\' usare %s nel gioco di carte'

# (riga, [(cerca, metti)], occorrenze_attese, motivo)
VOCI = []

# ── i sedici divieti: otto dei, ciascuno col suo creatura base e l'evoluto ──
# ⚠️ :2577 (Mani, base) e' commentata nel sorgente e resta fuori. Mani vive a
#    :2586 con `DEUS_EX_MANINA`, ed e' quella che si tocca.
for riga, dio in [
    (2575, 'Itzpalt'), (2576, 'Opatos'), (2578, 'Kumiromi'), (2579, 'Ehekatl'),
    (2580, 'Jure'), (2581, 'Lulwy'), (2582, 'Yacatect'),
    (2584, 'Itzpalt'), (2585, 'Opatos'), (2586, 'Mani'), (2587, 'Kumiromi'),
    (2588, 'Ehekatl'), (2589, 'Jure'), (2590, 'Lulwy'), (2591, 'Yacatect'),
]:
    VOCI.append((riga, [(f'"{_VIETA % dio}"', f'"{_VIETA_IT % dio}"')], 1,
                 f"Il divieto di {dio}. " + MAZZO))

# ── gli otto vincoli di fede, uno per carta ────────────────────────────────
for riga, dio, carta, resa in [
    (2593, 'Itzpalt', 'the exile', "l'esiliato"),
    (2594, 'Opatos', 'the golden knight', 'il cavaliere dorato'),
    (2595, 'Mani', 'the android', "l'androide"),
    (2596, 'Kumiromi', 'the cute fairy', 'la fatina'),
    (2597, 'Ehekatl', 'the black cat', 'il gatto nero'),
    (2598, 'Jure', 'the defender', 'il difensore'),
    (2599, 'Lulwy', 'the black angel', "l'angelo nero"),
    (2600, 'Yacatect', 'a goose', "l'oca"),
]:
    VOCI.append((riga, [(f'"{_SOLO % (dio, carta)}"', f'"{_SOLO_IT % (dio, resa)}"')], 1,
                 f"La carta di {dio}. ⭐ «{resa}» e' la resa gia' fissata in "
                 f"`db_card.hsp`, e vale su tutte e tre le copie del nome "
                 f"(bestiario, evoluzione, carta). " + MAZZO))

# ── i diciotto esiti della partita ─────────────────────────────────────────
for riga, en, it, nota in [
    (2804, 'You flipped the table and leave the game.',
     'Hai ribaltato il tavolo e lasciato la partita.',
     "⚠️ Non «te ne sei andato»: quel participio porta il genere di chi legge. Col "
     "passato prossimo di `avere` il participio non concorda, e la riga vale per "
     "tutti. 💡 «Ribaltare il tavolo» tiene l'immagine dell'idiotismo giapponese "
     "(ちゃぶ台返し), che e' quel che l'inglese ha tradotto alla lettera. "),
    (2805, 'You flipped the table in a hurry and leave the game.',
     'Hai ribaltato il tavolo in fretta e lasciato la partita.',
     "La stessa di sopra con la fuga precipitosa. Stesso accorgimento sul genere. "),
    (2806, "Opponent's health is reduced to 0.",
     "La vita dell'avversario e' scesa a zero.",
     "⭐ «vita» e non «salute»: e' il nome che il tavolo da gia' alla riserva di punti "
     "(`mes \"Vita \" + cpdata@tcg(TCG_PLAYER_LIFE, 0)`, toppato nella 53a). Chiamarla "
     "altrimenti qui darebbe due nomi alla stessa cosa nella stessa schermata. "),
    (2807, 'Your health is reduced to 0.',
     "La tua vita e' scesa a zero.",
     "La gemella, dal lato di chi gioca. "),
    (2808, 'Opponent lose due to fatigue damage.',
     "L'avversario perde per il danno da sfinimento.",
     "Il mazzo finito: chi non ha piu' carte da pescare comincia a perdere vita. "),
    (2809, 'You lose due to fatigue damage.',
     'Perdi per il danno da sfinimento.',
     "La gemella. ⚠️ «Perdi» e non «hai perso»: il participio porterebbe il genere. "),
    (2810, "You won using Zeome's effect.",
     "Hai vinto con l'effetto di <Zeome>.",
     "⭐ <Zeome> resta invariato: e' il nome proprio del falso profeta "
     "(`db_card.hsp:10397`, «<Zeome> il falso profeta»). "),
    (2811, "You lose due to Zeome's effect.",
     "Hai perso per l'effetto di <Zeome>.",
     "La gemella. 💡 «con» quando l'effetto e' tuo, «per» quando lo subisci: la "
     "distinzione e' nell'inglese («using» contro «due to») e si tiene. "),
    (2812, "You won using Meshera's effect.",
     "Hai vinto con l'effetto del Meshera.",
     "⭐ «il Meshera» e' la forma gia' usata (`action.hsp:17270`, «il Meshera "
     "Soldado»): e' una stirpe, e in italiano vuole l'articolo. "),
    (2813, "You lose due to Meshera's effect.",
     "Hai perso per l'effetto del Meshera.",
     "La gemella. "),
    (2814, "You won using Unitdeads' effect.",
     "Hai vinto con l'effetto degli unimorti.",
     "⭐ «unimorto» e' la parola coniata dal progetto per «unitdead» "
     "(`db_card.hsp:3455`, «il re unimorto»): il plurale la segue. "),
    (2815, "You lose due to Unitdeads' effect.",
     "Hai perso per l'effetto degli unimorti.",
     "La gemella. "),
    (2816, 'You opponent is BANNED.',
     "Il tuo avversario e' SQUALIFICATO.",
     "⚠️ Qui il participio si puo' usare: concorda con «avversario», che e' maschile "
     "per grammatica e non per il personaggio. Il maiuscolo dell'inglese resta, ed e' "
     "il tono da annuncio arbitrale. "),
    (2817, 'You are BANNED!',
     'SEI FUORI DAL GIOCO!',
     "⚠️⚠️ La gemella NON puo' dire «SEI SQUALIFICATO»: li' il participio concorda con "
     "chi legge. «Fuori dal gioco» e' invariante e dice la stessa cosa con lo stesso "
     "tono. E' una perdita dichiarata: la simmetria con :2816 si rompe apposta. "),
    (2818, "You've been playing for too long!",
     'Hai giocato troppo a lungo!',
     "Il limite di turni. ⚠️ La riga e' identica a :2819 nel testo ma non nella "
     "condizione (`gameresult` 13 contro 14): sono due toppe, non una `tutte`. "),
    (2819, "You've been playing for too long!",
     'Hai giocato troppo a lungo!',
     "La gemella di :2818, dall'altro lato del tavolo. "),
    (2820, "You won due to the Chaos Child's effect.",
     "Hai vinto per l'effetto del Figlio del Caos.",
     "⭐ «il Figlio del Caos» e' la resa gia' fissata (`db_card.hsp:1648`, "
     "«<Jaldabaoth> il Figlio del Caos»; `action.hsp:3008`). "),
    (2821, "You lose due to the Chaos Child's effect.",
     "Hai perso per l'effetto del Figlio del Caos.",
     "La gemella. "),
]:
    VOCI.append((riga, [(f'"{en}"', f'"{it}"')], 1, nota + PARTITA))


sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')

nuove = []
for riga, sostituzioni, attese, motivo in VOCI:
    originale = sorg[riga - 1]
    if build[riga - 1] != originale:
        raise SystemExit(f"{NOME}:{riga}: la build ha gia' una resa su questa riga")
    if 'lang("' in originale:
        raise SystemExit(f'{NOME}:{riga}: la riga porta una resa (regola della 46a)')
    # ⚠️ una riga commentata non si tocca: e' la regola della rete 6, che qui va
    #    applicata a mano perche' le toppe non hanno reti.
    if originale.lstrip().startswith(';'):
        raise SystemExit(f'{NOME}:{riga}: la riga e\' commentata nel sorgente')
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
    toppa['motivo'] = motivo + CLASSE
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
