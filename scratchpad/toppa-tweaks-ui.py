# -*- coding: utf-8 -*-
"""Il suffisso di stato del pannello, e il primo dei sette menu di dettaglio.

Due cose insieme, e la prima vale per **tutto** `custom_tweaks.hsp`:

1. **`GetTStatus` e le sue sorelle** (`:417`-`:513`) compongono il pezzo di riga
   che sta accanto a ogni voce del pannello: « (Currently: Off)», « (Currently:
   Draw Player Tachi-E)». Tradotte le voci e lasciato quello, ogni riga del
   pannello resterebbe mezza inglese.
2. **Il menu dei ritocchi all'interfaccia** (`*UITweakMenu_loop`), undici voci
   con le loro descrizioni.

## ⚠️⚠️ Un punto cieco nuovo: `return "…"` non lo vede nessuno

`nudi_en.py` cerca le righe che **disegnano** (`mes`, `bmes`, `txt`, `noteadd`…)
e quelle che **compongono** una variabile che verra' disegnata (`s = `,
`listn(0, …) = `, `buff += `). Un `return "…"` dentro un `#defcfunc` non e' ne'
l'una ne' l'altra, e il testo che restituisce finisce a schermo lo stesso.

Misurato oggi: **120 righe** cosi' in tutto il sorgente — `init.hsp` 56,
`text.hsp` 35, `custom_tweaks.hsp` 29.
⚠️ Ma **non tutte sono testo**, ed e' per questo che il filtro non e' stato
cambiato di corsa: i 35 di `text.hsp` sono `return "vernis"`, `return "kapul"`,
`return "fighterguild"` — **chiavi di mappa**, non parole. Mentre in `init.hsp`
c'e' roba vera: `:155`-`:168` restituiscono i suffissi ordinali inglesi
(`"st"`, `"nd"`, `"rd"`, `"th"`) del `cnvrank`, che il giocatore legge.
💡 Serve una regola di forma che distingua le due cose, e improvvisarla a fine
sessione sarebbe il modo di ripetere l'errore di `_PERCORSO`. Qui si traducono le
29 di `custom_tweaks.hsp` perche' sono state **lette una per una**; la misura
resta un debito dichiarato.

## Il vocabolario che si aggiunge a quello del menu principale

    (Currently: X)  ->  (Ora: X)      piu' corto, e «ora» e' quel che dice
    Off / On        ->  spento / acceso    (la coppia di «accende e spegne»)
    Disabled        ->  disattivato        l'inglese distingue Off da Disabled
    stamina         ->  SP                 buff.hsp:735, item_data.hsp:613
    tracker         ->  «osservate»        parola nuova: non c'era in dizionario
    Objet of Heart  ->  oggetto d'arte di cuore   db_item, ITEM_ID_OBJET_HEART
    enchantment     ->  incantamento       action.hsp:7716
    potential       ->  potenziale         db_item.hsp:148884
    figurine        ->  statuetta          db_item.hsp:145913
    flesh/golden doll -> bambola di carne / bambola dorata   command.hsp:4852-4855

⚠️ **«tracker» non aveva un traducente e ne serviva uno.** Il registro delle
abilita' seguite e' roba di Custom-GX e nessuna voce di dizionario lo nomina.
✅ Reso col participio — «le abilita' **osservate**», «le magie **osservate**» —
che evita di inventare un sostantivo tecnico e si legge come italiano.

## La larghezza

Finestra 640. Le voci escono a `wx + 64` (576 px, 74-87 caratteri) e le
descrizioni a `wx + 38` (602 px, 78-91). Le descrizioni vanno a capo da sole sui
`\n` che il sorgente gia' porta, quindi ogni riga ha tutto il budget. La piu'
lunga di questo lotto e' la seconda riga di `:302` a 65 caratteri.
⚠️ Due righe inglesi sono state **accorciate apposta** perche' la resa diretta
sfondava il metro prudente: `:308` («Reports x/y positions of duplicated cards
and figurines when the museum updates.», 80 caratteri) e la coda di `:302`.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
BUILD = r'C:\Games\Elona\_traduzione\build\2.05-custom-gx'
NOME = 'custom_tweaks.hsp'

CLASSE = (
    "⚠️ E' un letterale INGLESE NUDO: non passa da nessuna `lang()`, quindi non ha "
    "firma, non ha voce di dizionario e nessun lotto puo' raggiungerlo — si tocca solo "
    "con una toppa. Quinto punto cieco (`nudi_en.py`, 49a; `triage_nudi.py`, 50a)."
)
STATO = (
    "E' uno dei valori che `GetTStatus` e le sue sorelle (custom_tweaks.hsp:417-513) "
    "mettono accanto a OGNI voce del pannello dei ritocchi: tradotte le voci e lasciato "
    "questo, ogni riga resterebbe mezza inglese. ⭐ «(Currently: X)» -> «(Ora: X)»: piu' "
    "corto e «ora» e' esattamente quel che dice. "
    "⚠️⚠️ E' anche un PUNTO CIECO NUOVO, misurato nella 50a: `nudi_en.py` cerca le righe "
    "che disegnano e quelle che compongono una variabile, e un `return \"…\"` dentro un "
    "`#defcfunc` non e' ne' l'una ne' l'altra. Sono 120 righe cosi' in tutto il sorgente "
    "(init.hsp 56, text.hsp 35, custom_tweaks.hsp 29), ma non tutte sono testo — i 35 di "
    "text.hsp sono chiavi di mappa («vernis», «kapul») — quindi il filtro NON e' stato "
    "cambiato di corsa: serve una regola di forma che distingua, e improvvisarla "
    "sarebbe ripetere l'errore di `_PERCORSO`. Queste 29 si traducono perche' sono state "
    "lette una per una. "
)
MENU_UI = (
    "Sta nel menu dei ritocchi all'interfaccia (`*UITweakMenu_loop`), il primo dei sette "
    "menu di dettaglio del pannello. La finestra e' 640: le voci escono a `wx + 64` "
    "(576 px, 74-87 caratteri) e le descrizioni a `wx + 38` (602 px, 78-91), che vanno a "
    "capo da sole sui `\\n` gia' presenti nel sorgente. "
)

# (riga, [(cerca, metti)], occorrenze_attese, motivo)
VOCI = [
    # ── il suffisso di stato, comune a tutto il pannello ────────────────────
    (419, [('" (Currently: Off)"', '" (Ora: spento)"')], 2,
     "Il ritocco e' spento. ⭐ «spento»/«acceso» e' la coppia di «accende e spegne», il "
     "verbo scelto per «toggle» nelle descrizioni del menu principale. Toppa `tutte`: "
     "la stessa riga sta in due funzioni diverse (:419 e :504). "),
    (495, [('" (Currently: On)"', '" (Ora: acceso)"')], 2,
     "Il ritocco e' acceso. Toppa `tutte` (:495 e :507). "),
    (457, [('" (Currently: Disabled)"', '" (Ora: disattivato)"')], 3,
     "⚠️ L'inglese distingue «Off» da «Disabled» e l'italiano lo segue: «spento» e' un "
     "interruttore a due posizioni, «disattivato» e' il valore zero di una scelta a "
     "piu' valori. Toppa `tutte` (:457, :474, :491). "),
    (423, [('" (Currently: Japanese)"', '" (Ora: giapponese)"')], 1, "La lingua scelta. "),
    (426, [('" (Currently: English)"', '" (Ora: inglese)"')], 1, "La lingua scelta. "),
    (429, [('" (Currently: Romanji)"', '" (Ora: romaji)"')], 1,
     "⚠️ L'inglese scrive «Romanji», che e' un refuso diffuso: la parola giapponese e' "
     "ローマ字, «romaji». L'italiano scrive quella giusta. "),
    (434, [('" (Currently: Awakened Random Nefias)"', '" (Ora: Nefie casuali risvegliate)"')], 1,
     "⭐ «Nefia» resta il nome proprio del dizionario (db_item.hsp:138961), al plurale "
     "italiano «Nefie». "),
    (437, [('" (Currently: All Random Nefias)"', '" (Ora: tutte le Nefie casuali)"')], 1, ""),
    (440, [('" (Currently: Everywhere)"', '" (Ora: ovunque)"')], 1, ""),
    (443, [('" (Currently: None)"', '" (Ora: nessuno)"')], 1, ""),
    (448, [('" (Currently: Player Only)"', '" (Ora: solo il giocatore)"')], 1, ""),
    (451, [('" (Currently: Player/Follower Only)"', '" (Ora: solo giocatore e alleati)"')], 1,
     "⚠️ «Follower» e' l'alleato al seguito: il progetto usa «alleato». "),
    (454, [('" (Currently: All)"', '" (Ora: tutti)"')], 1, ""),
    (462, [('" (Currently: Draw Player Tachi-E)"', '" (Ora: ritratto del giocatore)"')], 1,
     "⚠️ «Tachi-E» (立ち絵) e' il disegno a figura intera del personaggio. L'italiano dice "
     "«ritratto», che e' la parola con cui il gioco chiama gia' quell'immagine, e lascia "
     "cadere il «Draw» che in una riga di stato non aggiunge niente. "),
    (465, [('" (Currently: Draw Player-Tag Tachi-E)"', '" (Ora: ritratto del compagno di scambio)"')], 1,
     "Il «tag» e' il compagno con cui ci si da' il cambio in battaglia. "),
    (468, [('" (Currently: Draw Player-Mount Tachi-E)"', '" (Ora: ritratto della cavalcatura)"')], 1, ""),
    (471, [('" (Currently: Draw First Alive Pet Tachi-E)"', '" (Ora: ritratto del primo alleato vivo)"')], 1, ""),
    (479, [('" (Currently: Main-Hand Staff)"', '" (Ora: bastone in mano principale)"')], 1, ""),
    (482, [('" (Currently: All Equipped Staff)"', '" (Ora: tutti i bastoni indossati)"')], 1, ""),
    (485, [('" (Currently: Main-Hand Weapon)"', '" (Ora: arma in mano principale)"')], 1, ""),
    (488, [('" (Currently: All Equipped Weapon)"', '" (Ora: tutte le armi indossate)"')], 1, ""),
    (498, [('" (Currently: "', '" (Ora: "')], 1,
     "La forma generica, dove il valore e' un numero. "),
    (500, [('" FAILED"', '" ERRORE"')], 1,
     "Il ramo di guasto: esce quando il ritocco ha un valore che nessun ramo riconosce. "),
    (510, [('" (Currently: "', '" (Ora: "')], 1,
     "La forma generica della seconda funzione, col numero e la sua descrizione. "),
    (512, [('" (Currently: FAILED)"', '" (Ora: ERRORE)"')], 1, "Il ramo di guasto della seconda funzione. "),

    # ── il menu dei ritocchi all'interfaccia: le voci ───────────────────────
    (252, [('"Show Enchant Strength With Objet of Heart. (Currently: "',
            '"Forza degli incantamenti con l\'oggetto d\'arte di cuore. (Ora: "')], 1,
     "⭐ «Objet of Heart» e' l'oggetto `ITEM_ID_OBJET_HEART`, che in italiano il "
     "dizionario compone come «oggetto d'arte di cuore» (db_item: `ioriginalnameref` = "
     "«cuore», `ioriginalnameref2` = «oggetto d'arte»): la voce di menu deve chiamarlo "
     "come il giocatore lo legge nell'inventario. «enchantment» -> «incantamento» viene "
     "da action.hsp:7716. "),
    (253, [('"Allow Spell Tracking."', '"Permetti di osservare anche le magie."')], 1,
     "⭐ «tracker» non aveva un traducente in tutto il progetto e ne serviva uno: il "
     "registro delle abilita' seguite e' roba di Custom-GX. Reso col participio — «le "
     "abilita' osservate», «le magie osservate» — che evita di inventare un sostantivo "
     "tecnico e si legge come italiano. "),
    (254, [('"Add Potentials To Skill Tracker."', '"Mostra il potenziale fra le abilita\' osservate."')], 1,
     "«potential» -> «potenziale» e' la resa del dizionario (db_item.hsp:148884, "
     "command.hsp:10845). "),
    (255, [('"Filter Skill Tracker By Potential."', '"Filtra le abilita\' osservate per potenziale."')], 1, ""),
    (256, [('"Show Spell Stock In Tracker."', '"Mostra la scorta delle magie osservate."')], 1,
     "«spell stock» e' il numero di lanci accumulati: «scorta». "),
    (257, [('"Highlight/Filter Items. (Currently: "', '"Evidenzia e filtra gli oggetti. (Ora: "')], 1,
     "⚠️ La barra dell'inglese («Highlight/Filter») e' una congiunzione, non una scelta "
     "fra due: l'italiano scrive «e». "),
    (258, [('"Re-parse ItemList.txt."', '"Rileggi ItemList.txt."')], 1,
     "⚠️⚠️ Questa riga era invisibile a `nudi_en.py`: la regola `_ESTENSIONE` scartava "
     "ogni letterale che contenesse un nome di file, e qui il nome sta DENTRO una "
     "frase. Corretta nella 50a con la stessa regola di `_PERCORSO`: un nome di file e' "
     "un token, senza spazi. Il nome del file non si traduce, perche' e' un file vero "
     "che il giocatore deve trovare sul disco. "),
    (259, [('"Report museum duplicates."', '"Segnala i doppioni del museo."')], 1,
     "«museum» -> «museo» (db_item.hsp:145651). "),
    (260, [('"Draw stamina bar."', '"Disegna la barra degli SP."')], 1,
     "⭐ «stamina» e' gia' «SP» nelle rese brevi (buff.hsp:735 «Gli SP non calano», "
     "item_data.hsp:613 «Assorbe SP»), e «SP» e' anche quel che la barra di stato "
     "scrive. Nelle frasi lunghe il progetto usa «vigore» (proc.hsp:10642). "),
    (261, [('"Draw full-sized items in inventory."',
            '"Disegna gli oggetti a grandezza intera nell\'inventario."')], 1, ""),
    (262, [('"Draw items left-and-right in inventory to reduce overlap."',
            '"Alterna gli oggetti a destra e a sinistra per non sovrapporli."')], 1,
     "⚠️ L'inglese descrive il come («left-and-right») e poi lo scopo; l'italiano mette "
     "il verbo che dice tutt'e due, «alterna». "),

    # ── il menu dei ritocchi all'interfaccia: le descrizioni ────────────────
    (287, [('"When examining items while holding the Objet of Heart, the strength\\nof '
            'enchantments on the item will be shown.\\n0 = Don\'t Show, 1 = Show For '
            'Enchants w/Level, 2 = Show All"',
            '"Esaminando un oggetto mentre tieni l\'oggetto d\'arte di cuore, si vede\\nla '
            'forza dei suoi incantamenti.\\n0 = non mostrare, 1 = solo quelli con livello, '
            '2 = mostra tutto"')], 1, ""),
    (290, [('"Spells can be added to the skill tracker in the same manner as skills."',
            '"Le magie si possono osservare come le abilita\'."')], 1, ""),
    (293, [('"All items in the skill tracker will also display their current potential."',
            '"Ogni voce osservata mostra anche il potenziale che ha adesso."')], 1, ""),
    (296, [('"Tracked skills/abilities will not display unless their potential is\\nequal '
            'to or below a certain threshold."',
            '"Le abilita\' osservate si vedono solo se il loro potenziale e\'\\npari o '
            'inferiore a una soglia."')], 1, ""),
    (299, [('"Tracked spells will also display their spell stock."',
            '"Le magie osservate mostrano anche la loro scorta."')], 1, ""),
    (302, [('"Configure your highlighting/filtering choice.\\n0 = No Highlight, 1 = '
            'Highlight and Mark Items, 2 = Only Show Highlighted Items"',
            '"Scegli come evidenziare e filtrare.\\n0 = niente, 1 = evidenzia e segna, '
            '2 = mostra solo gli evidenziati"')], 1,
     "⚠️ La coda inglese e' di 80 caratteri e sfonda il metro prudente (602 px "
     "disponibili, 7,7 px per carattere): l'italiano dice la stessa cosa in 65. "),
    (305, [('"Reload the ItemList.txt file, used to enable highlighting and filtering for items."',
            '"Rilegge il file ItemList.txt, che serve a evidenziare e filtrare gli oggetti."')], 1,
     "⚠️⚠️ Anche questa era invisibile per la regola `_ESTENSIONE`, corretta nella 50a. "),
    (308, [('"Reports x/y positions of duplicated cards and figurines when the museum updates."',
            '"Segnala x/y di carte e statuette doppie all\'aggiornamento del museo."')], 1,
     "⚠️ La resa diretta sarebbe di 80 caratteri e sfonderebbe il metro prudente: "
     "accorciata a 67 senza perdere niente. «figurine» -> «statuetta» (db_item.hsp:145913). "),
    (311, [('"Draw stamina bar instead of just displaying like Sp 12/23.\\nIt\'s using the '
            'yellow (gauge) bar below health in interface.bmp.\\nIf it looks weird check '
            'if your beautify does anything to that."',
            '"Disegna una barra invece di scrivere Sp 12/23.\\nUsa la barra gialla sotto '
            'la salute in interface.bmp.\\nSe viene strana, controlla che il tuo '
            'abbellimento non ci metta mano."')], 1,
     "⚠️⚠️ Invisibile per la regola `_ESTENSIONE` («interface.bmp»), corretta nella 50a. "
     "⭐ «Sp 12/23» resta com'e': e' la citazione letterale di quel che la barra di "
     "stato scrive, e la barra scrive ancora `Sp` (screen.hsp:417, lasciato apposta "
     "nella 50a perche' non ha spazio per un carattere in piu'). "),
    (314, [('"Draw 48x96 items with full size in inventory.\\n This includes flesh dolls '
            'and golden dolls."',
            '"Disegna a grandezza intera gli oggetti 48x96 nell\'inventario.\\n Comprese '
            'le bambole di carne e le bambole dorate."')], 1,
     "«flesh doll» e «golden doll» sono gia' «bambola di carne» e «bambola dorata» "
     "(command.hsp:4855 e :4852). "),
    (317, [('"Draw items in an alternate pattern of left and right to prevent overlap."',
            '"Disegna gli oggetti alternandoli a destra e a sinistra per non sovrapporli."')], 1, ""),
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
            raise SystemExit(f'{NOME}:{riga}: `{cerca}` compare {nuova.count(cerca)} volte, non una')
        nuova = nuova.replace(cerca, metti)
    if nuova == originale:
        raise SystemExit(f'{NOME}:{riga}: la toppa non cambierebbe niente')
    try:
        nuova.encode('cp932')
    except UnicodeEncodeError as errore:
        raise SystemExit(f'{NOME}:{riga}: testo che CP932 non sa scrivere ({errore})')

    coda = STATO if riga >= 417 and riga <= 513 else MENU_UI
    toppa = {'file': NOME, 'cerca': originale, 'sostituisci': nuova}
    if attese > 1:
        toppa['tutte'] = True
    toppa['motivo'] = (motivo or '') + coda + CLASSE
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
        print(f"  :{t['_riga']}{marca}  {t['sostituisci'].strip()[:96]}")
