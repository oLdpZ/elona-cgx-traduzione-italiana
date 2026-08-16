# -*- coding: utf-8 -*-
"""Il menu dei ritocchi all'IA (`*AITweakMenu_loop`, custom_tweaks.hsp:1485-1615).

Sette voci e sette descrizioni: **14 righe**, il piu' piccolo dei sei menu di
dettaglio rimasti dopo la 50a. Titolo, riga di testa, «Indietro.» e «Torna al
menu precedente.» sono gia' chiusi dalle toppe `tutte` del menu principale —
verificato leggendo la build, che su :1487, :1489, :1500 e :1545 ha gia'
l'italiano.

## Il vocabolario, tutto preso da fuori e niente inventato

Nessuna di queste sette voci nomina una cosa nuova: sono tutte cose che il gioco
chiama gia' in un modo, e la voce di menu deve chiamarle come il giocatore le
legge altrove.

    AI              -> IA                    fissato nella 50a (menu principale)
    NPC             -> PNG                   custom_tweaks.hsp:133
    pet / ally      -> alleato                custom_tweaks.hsp:471 («primo alleato vivo»)
    Zeome           -> Zeome                 text.hsp:669, db_creature.hsp:98740
    necromancy      -> negromanzia           db_item.hsp:139896 («bara della negromanzia»)
    Shadow Step     -> Passo d'ombra         skill.hsp:932
    Healing Rain    -> Pioggia curativa      skill.hsp:429, db_item.hsp:145279
    'undead call'   -> 'Raduna i non-morti'  text.hsp:2101
    Party Time!     -> Si balla!             text.hsp:131

⭐ **Le due che si sarebbero sbagliate a occhio sono «necromancy» e «Party
Time!».** La prima in italiano e' **negromanzia**, non «necromanzia», e non l'ho
decisa io: `db_item.hsp:139896` l'ha gia' resa cosi'. La seconda non e' una festa
generica ma il **nome di un evento**, che il progetto chiama «Si balla!»
(`text.hsp:131`): tradurla come «festa» avrebbe scollegato la descrizione dalla
cosa che il giocatore vede annunciata a schermo.

⚠️ **«custom AI» resta un debito.** La descrizione di :1532 la nomina, e
`custom_ai.hsp` (~60 righe) non e' ancora tradotto: qui e' resa «IA
personalizzata», che e' la scelta ovvia, ma **e' la prima volta che compare** e
il lotto di `custom_ai.hsp` dovra' seguirla, non rifarla.

## La forma: voci all'imperativo o dichiarative, descrizioni in terza persona

E' la regola che il pannello ha gia' preso nella 50a e che qui si rispetta: la
voce segue la forma dell'inglese (imperativo dove l'inglese comanda,
dichiarativa dove l'inglese descrive), la descrizione sta sempre in terza
persona.

## La larghezza

Finestra 640. Le voci escono a `wx + 64` (576 px) e le descrizioni a `wx + 38`
(602 px); col metro prudente da 7,7 px per carattere fanno **74** e **78**
caratteri. ⚠️ Alle voci va tolto il suffisso di stato che `GetTStatus` appende:
in questo menu il piu' lungo e' « (Ora: acceso)», 14 caratteri — sei voci su
sette sono interruttori e la settima porta un numero. Il controllo e' scritto
qui sotto e conta anche quello.

⚠️ La descrizione di :1526 e' la piu' stretta del lotto e ha costretto a
scegliere: l'inglese avverte due volte («Warning: 100% is chaos.»), l'italiano
lo dice una volta sola per stare dentro la riga.

⚠️ **Niente virgolette a caporale** («»): CP932 non le sa scrivere. Dove
l'inglese cita una voce di menu (`'undead call'`) l'italiano usa l'apostrofo
semplice, come lui. E le toppe non passano da `accenti.py`, quindi l'apostrofo
degli accenti si scrive a mano: `piu'`, `probabilita'`, `cosi'`.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'custom_tweaks.hsp'

# metri prudenti: 7,7 px per carattere sui px disponibili
TETTO_VOCE = 74 - len(' (Ora: acceso)')   # il suffisso di stato piu' lungo del menu
TETTO_DESCRIZIONE = 78

CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca solo "
    "con una toppa. Quinto punto cieco (`nudi_en.py`, 49a; `triage_nudi.py`, 50a)."
)
MENU_AI = (
    "Sta nel menu dei ritocchi all'IA (`*AITweakMenu_loop`), uno dei sette menu di "
    "dettaglio del pannello dei ritocchi di Custom-GX. ⭐ «IA» e' la resa fissata nella "
    "50a col menu principale (custom_tweaks.hsp:106), «PNG» quella gia' in uso per gli "
    "NPC (:133) e «alleato» quella per pet e follower (:471). La finestra e' 640: le "
    "voci escono a `wx + 64` (576 px, 74 caratteri col metro prudente, meno i 14 del "
    "suffisso di stato) e le descrizioni a `wx + 38` (602 px, 78 caratteri per riga, "
    "che vanno a capo da sole sui `\\n` gia' presenti nel sorgente). "
)

# (riga, tipo, [(cerca, metti)], occorrenze_attese, motivo)
VOCI = [
    # ── le sette voci ───────────────────────────────────────────────────────
    (1492, 'voce', [('"Change Zeome\'s AI."', '"Cambia l\'IA di Zeome."')], 1,
     "Il ritocco che rende piu' duro lo scontro con Zeome. ⭐ «Zeome» e' il nome proprio "
     "gia' fissato (text.hsp:669, db_creature.hsp:98740 «<Zeome> il falso profeta»): non "
     "si traduce. "),
    (1493, 'voce', [('"Increased drinking/brawling chance during parties."',
                     '"Probabilita\' di bevute e risse durante le feste."')], 1,
     "⚠️ Questa non e' un interruttore ma un `IncrementTweak` da 0 a 100 a passi di 10 "
     "(:1573-:1578): il suffisso di stato ci mette un numero, non «acceso». Percio' la "
     "voce e' un nome di grandezza («Probabilita' di…») e non un comando: dire «Alza le "
     "risse» accanto a «(Ora: 30)» sarebbe stato un controsenso. "),
    (1494, 'voce', [('"Prevent home stayers from moving."',
                     '"Impedisci di muoversi a chi resta in casa."')], 1,
     "⚠️ «Home stayer» non aveva un traducente in dizionario, ma la cosa si', ed e' quella "
     "che il giocatore sceglie con «Chi vuoi che resti qui?» (command.hsp:1263): la voce "
     "usa lo stesso verbo di quella domanda invece di inventare un sostantivo. "),
    (1495, 'voce', [('"Pets Heal Other Pets."', '"Gli alleati si curano a vicenda."')], 1,
     "⚠️ L'inglese e' dichiarativo e l'italiano lo resta — nel pannello le voci seguono la "
     "forma dell'inglese, imperativo o dichiarativo. «a vicenda» dice in due parole "
     "quel che l'inglese dice ripetendo «Pets… Other Pets». "),
    (1496, 'voce', [('"Necromancy Autotargeting."', '"Bersagli automatici per la negromanzia."')], 1,
     "⭐ **negromanzia**, non «necromanzia»: e' la resa che il dizionario ha gia' scelto "
     "(db_item.hsp:139896, «bara della negromanzia»). E' la parola che un occhio "
     "distratto avrebbe ricalcato dall'inglese. "),
    (1497, 'voce', [('"Disable Necro/Summons auto shadow step."',
                     '"Disattiva il passo d\'ombra di evocazioni e non-morti."')], 1,
     "⭐ «Shadow Step» e' «Passo d'ombra» (skill.hsp:932): qui minuscolo perche' e' la "
     "mossa nominata dentro una frase, non la voce del libro delle abilita'. ⚠️ «Necro» "
     "e' l'abbreviazione di «Necromancy» e indica i servitori non-morti che evoca: "
     "l'italiano scioglie l'abbreviazione perche' ha lo spazio per farlo. "),
    (1498, 'voce', [('"Allies acting independently."', '"Alleati che agiscono per conto loro."')], 1,
     "«Independently» qui vuol dire che non si agganciano al bersaglio del giocatore — lo "
     "dice la descrizione di :1541. «per conto loro» e' quello, senza fingere una "
     "precisione tecnica che la voce di menu non ha. "),

    # ── le sette descrizioni ────────────────────────────────────────────────
    (1523, 'descrizione',
     [('"Changes Zeome\'s move list and AI to make the fight significantly more difficult."',
       '"Cambia le mosse e l\'IA di Zeome per rendere lo scontro molto piu\' duro."')], 1,
     "«move list» e' il repertorio di mosse: «le mosse» basta e sta in riga. "),
    (1526, 'descrizione',
     [('"NPC\'s drink and brawl more during Party Time! Warning: 100% is chaos. "',
       '"I PNG bevono e litigano di piu\' durante \'Si balla!\'. Al 100% e\' il caos."')], 1,
     "⭐ «Party Time!» non e' una festa generica ma il **nome dell'evento**, che il "
     "progetto rende «Si balla!» (text.hsp:131): tradurlo come parola comune avrebbe "
     "scollegato la descrizione da quel che il giocatore vede annunciato a schermo. "
     "⚠️ E' la riga piu' stretta del lotto: l'inglese avverte due volte («Warning: 100% "
     "is chaos.»), l'italiano lo dice una volta sola per restare sotto i 78 caratteri. "),
    (1529, 'descrizione',
     [('"Prevent your home stayers from moving inside your home."',
       '"Impedisce agli alleati che restano in casa di girare per le stanze."')], 1,
     "⚠️ L'inglese ripete «home» due volte in sette parole; l'italiano lo dice una volta "
     "e chiude con «per le stanze», che e' il movimento di cui si parla. "),
    (1532, 'descrizione',
     [('"Pets with Healing Rain will consider the health of other pets when deciding\\n'
       'whether or not to use it. If using custom AI, no effect except\\nusage out of '
       'combat (requires pet to know it naturally)."',
       '"Gli alleati con Pioggia curativa guardano la salute degli altri prima\\ndi '
       'lanciarla. Con l\'IA personalizzata vale solo fuori dal combattimento\\n(e serve '
       'che l\'alleato la conosca di suo)."')], 1,
     "⭐ «Healing Rain» e' «Pioggia curativa» (skill.hsp:429, db_item.hsp:145279). "
     "⚠️ **«custom AI» compare qui per la prima volta in tutto il progetto** ed e' resa "
     "«IA personalizzata»: `custom_ai.hsp` (~60 righe, «Tactical Instructions») non e' "
     "ancora tradotto e dovra' seguire questa scelta, non rifarne un'altra. "
     "«requires pet to know it naturally» vuol dire che deve conoscerla di suo, non "
     "averla imparata da un libro: «di suo». "),
    (1535, 'descrizione',
     [('"Make necromancy minions actively seek out enemies like pets do."',
       '"I servitori della negromanzia cercano i nemici come fanno gli alleati."')], 1,
     "«minion» non aveva una resa utile in dizionario (l'unica occorrenza e' «al soldo "
     "di», command.hsp:9558, che e' un'altra cosa): «servitore» e' quel che sono, i "
     "non-morti che la negromanzia alza e che seguono chi li ha alzati. "),
    (1538, 'descrizione',
     [('"Necromancy/Summons shadow steps player when out of sight.\\nWhich resets their '
       'target very often.\\n\\nYou can use \'undead call\' to pull them back manually."',
       '"Non-morti ed evocazioni fanno il passo d\'ombra verso di te quando ti\\nperdono '
       'di vista, e cosi\' cambiano bersaglio in continuazione.\\n\\nCon \'Raduna i '
       'non-morti\' li richiami a mano."')], 1,
     "⭐ «undead call» e' il comando che il gioco chiama «Raduna i non-morti» "
     "(text.hsp:2101): l'inglese lo cita fra apici e l'italiano fa uguale — ⚠️ niente "
     "virgolette a caporale, che CP932 non sa scrivere. L'inglese spezza in due frasi "
     "(«…out of sight. Which resets…»), l'italiano le lega con «e cosi'», che e' il "
     "nesso vero: e' il passo d'ombra a far cambiare bersaglio. "),
    (1541, 'descrizione',
     [('"Prevent allies from auto targeting player target.\\nPrevent allies from '
       'prioritize NPCs attacking players.\\nAlso allow NPCs to target NPCs outside of '
       'player\'s sight."',
       '"Gli alleati non prendono in automatico il tuo stesso bersaglio\\ne non danno la '
       'precedenza ai PNG che attaccano te.\\nE i PNG possono attaccarsi anche fuori '
       'dalla tua vista."')], 1,
     "⚠️ L'inglese ripete «Prevent allies from» due volte; l'italiano lo dice una volta "
     "sola e lega le due con «e non», che e' quel che significano. La terza riga cambia "
     "soggetto (dai tuoi alleati ai PNG in generale) e l'italiano lo segna con «E i PNG». "),
]

sorg = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
build = io.open(f'{BUILD}\\{NOME}', encoding='cp932').read().split('\n')


def _letterale(pezzo: str) -> str:
    """Il testo dentro le virgolette, con le sequenze `\\n` rese a capo vere."""
    return pezzo.strip('"').replace('\\n', '\n')


nuove = []
for riga, tipo, sostituzioni, attese, motivo in VOCI:
    originale = sorg[riga - 1]
    # ⚠️ regola della 50a: il `cerca` deve agganciare il sorgente pinnato E la build.
    if build[riga - 1] != originale:
        raise SystemExit(f"{NOME}:{riga}: la build ha gia' una resa su questa riga")
    if 'lang("' in originale:
        raise SystemExit(f'{NOME}:{riga}: la riga porta una resa (regola della 46a)')
    # ⚠️ `tutte` non e' una scusa per non guardare, e nemmeno la sua assenza:
    #    qui si pretende che ogni riga sia UNICA, cioe' che la toppa non sia ambigua.
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
        # la larghezza si misura sul testo, non sulla riga di codice
        tetto = TETTO_VOCE if tipo == 'voce' else TETTO_DESCRIZIONE
        for pezzo in _letterale(metti).split('\n'):
            if len(pezzo) > tetto:
                raise SystemExit(
                    f'{NOME}:{riga}: {len(pezzo)} caratteri, tetto {tetto} — {pezzo!r}')
    if nuova == originale:
        raise SystemExit(f'{NOME}:{riga}: la toppa non cambierebbe niente')
    # ⚠️ le toppe non passano da `accenti.py`: la degradazione e' scritta a mano
    #    e questo controllo e' l'unica rete che la verifica.
    try:
        nuova.encode('cp932')
    except UnicodeEncodeError as errore:
        raise SystemExit(f'{NOME}:{riga}: testo che CP932 non sa scrivere ({errore})')

    toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova}
    if attese > 1:
        toppa['tutte'] = True
    toppa['motivo'] = motivo + MENU_AI + CLASSE
    toppa['_riga'] = riga
    toppa['_quante'] = attese
    toppa['_lungo'] = max(
        len(p) for _, metti in sostituzioni for p in _letterale(metti).split('\n'))
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
        print(f"  :{t['_riga']}  (riga piu' lunga {t['_lungo']})")
        print(f"    - {t['cerca'].strip()[:110]}")
        print(f"    + {t['sostituisci'].strip()[:110]}")
