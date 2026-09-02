# -*- coding: utf-8 -*-
"""Il settimo lotto della 127a: la coda delle righe nude in sei file.

    chara.hsp        14   «Gene from» in tredici schermate, e il lucchetto
    system.hsp        7   gli errori dei file dei PNG e degli oggetti
    main.hsp          6   il tempo, la lapide, il boss e i saluti al rientro
    help.hsp          4   la guida, la chat, le scene
    economy.hsp       4   l'allineamento della citta' e il prezzo di un edificio
    chara_func.hsp    2   la barriera di mana e il risucchio

⭐ Diverse sono ripetute identiche in piu' punti — «Gene from » sta in TREDICI
schermate della creazione — e per quelle la toppa e' dichiarata `"tutte": true`:
si guarda una volta, si scrive una volta, e il conto delle occorrenze e'
controllato qui sotto prima di scrivere.
"""
import io
import json

from strumenti.accenti import degrada

BASE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
SORGENTI = {}

NUDO = (
    "LETTERALE INGLESE NUDO: non passa da nessuna lang(), quindi non ha firma "
    "ne' voce di dizionario e nessun lotto puo' raggiungerlo (quinto punto "
    "cieco, nudi_en.py, 49a). "
)

# (file, riga di riferimento) -> (riga nuova, occorrenze attese, motivo)
LAVORO = []


def toppa(file, riga, nuova, attese, motivo):
    LAVORO.append((file, riga, nuova, attese, motivo))


# --- chara.hsp --------------------------------------------------------------

toppa('chara.hsp', 3178, 'mes "Gene di " + geneuse', 13,
      NUDO + "chara.hsp, la scritta in basso a sinistra che dice da quale "
      "personaggio vengono i geni del nuovo eroe. ⚠️ LA STESSA RIGA STA IN "
      "TREDICI SCHERMATE della creazione — nome, passato, razza, sesso, classe, "
      "abilita', attributi, talenti, ritratto e le tre finestre di rinomina "
      "(:3178, :3283, :3433, :3587, :3615, :3741, :3770, :3901, :3929, :3970, "
      ":4105, :4131, :4163) — e vogliono tutte la stessa resa: toppa `tutte`, "
      "e le occorrenze sono contate. ⓘ `geneuse` e' il nome del personaggio "
      "donatore, e «Gene» e' la parola che il progetto usa gia' "
      "(proc.hsp:4324). ⓘ Nessun tetto: `pos 20, windowh - 36` scrive sul "
      "bordo basso della finestra intera.")

toppa('chara.hsp', 4034, 'mes "Blocco!"', 1,
      NUDO + "chara.hsp:*cm_stats_WHILE1, il bollino che marca un attributo "
      "bloccato nella schermata dei geni. ⭐ LA PAROLA E' RISCOSSA VENTI RIGHE "
      "SOPRA: :4014 e' una `lang()` gia' in dizionario che dice «Blocchi "
      "rimasti: » — quindi in questa schermata il meccanismo si chiama gia' "
      "«blocco», e il bollino ne e' il nome. ⚠️ «Bloccato» sarebbe stato un "
      "participio sopra una colonna di NOVE attributi di genere misto — Forza "
      "e Volonta' femminili, Apprendimento e Carisma maschili — e avrebbe "
      "sbagliato l'accordo in meta' delle righe. Il sostantivo lo evita, ed e' "
      "la regola che la guida di stile detta per le etichette di stato.")

# --- system.hsp -------------------------------------------------------------

toppa('system.hsp', 1870, 'txt "File non valido. Operazione annullata."', 2,
      NUDO + "system.hsp:*user_item (:1870) e *user_npc (:1973), il rifiuto di "
      "un file di oggetto o di PNG personalizzato che non comincia con "
      "l'intestazione giusta. Le due righe sono identiche e vogliono la stessa "
      "resa: toppa `tutte`, occorrenze contate. ⓘ «Aborting» qui non e' "
      "«interruzione» ma la fine dell'operazione richiesta, e in italiano si "
      "dice cosi'.")

toppa('system.hsp', 1884,
      'txt "Il file deve pesare meno di 30 KB. Operazione annullata."', 2,
      NUDO + "system.hsp:*user_item (:1884) e *user_npc (:1987), il "
      "rifiuto di un'immagine troppo grande da incorporare in un oggetto o in "
      "un PNG personalizzato. Due righe identiche, toppa `tutte`, occorrenze "
      "contate. ⓘ Lo spazio prima di «KB» e' quello dell'uso italiano. "
      "⚠️ LA TERZA, :2004, DICE LA STESSA COSA MA HA DUE TABULAZIONI IN PIU' "
      "— sta dentro un `if` annidato — quindi è una riga DIVERSA e non entra in "
      "questa toppa: le toppe si agganciano al testo intero della riga, "
      "indentazione compresa. Ha la sua, qui accanto.")

toppa('system.hsp', 2004,
      'txt "Il file deve pesare meno di 30 KB. Operazione annullata."', 1,
      NUDO + "system.hsp:*user_npc, la terza copia dell'avviso sui 30 KB. "
      "⚠️ Non sta con le altre due perché è indentata di due tabulazioni in "
      "più: il `cerca` di una toppa è la riga INTERA, e due righe che dicono "
      "la stessa cosa a due profondità diverse sono due righe diverse. "
      "ⓘ La resa è identica alle altre due, e deve restarlo.")

toppa('system.hsp', 3701, 'mes "Nessun salvataggio trovato"', 1,
      NUDO + "system.hsp:*game_title_selectID_WHILE1, quel che la schermata "
      "del titolo scrive quando non c'e' nessuna partita da caricare. E' fra "
      "le primissime cose che un giocatore nuovo vede. ⓘ Senza punto, come "
      "l'inglese.")

toppa('system.hsp', 3812, 'mes "Nessun file di geni trovato."', 1,
      NUDO + "system.hsp:*game_title_selectGen_WHILE1, la gemella qui sopra "
      "per la schermata dei geni. ⓘ Col punto, come l'inglese: la differenza "
      "e' di monte e non e' nostra da correggere.")

# --- main.hsp ---------------------------------------------------------------

_TIC = (
    "main.hsp:*turn_end, il rumore dell'orologio che segna il passare del "
    "tempo. ⭐ L'onomatopea segue la famiglia gia' scritta nelle toppe di "
    "`proc.hsp` della 126a — ` *clang* `, ` *tonf* `, ` *zac* ` — dove "
    "l'italiano usa la sua e non ricopia l'inglese. ⚠️ Le due righe (:2651 e "
    ":2698) dicono la stessa cosa ma hanno INDENTAZIONE DIVERSA, quindi sono "
    "due toppe e non una `tutte`: il `cerca` è la riga intera, tabulazioni "
    "comprese. "
)
toppa('main.hsp', 2651, 'txt " *tic* "', 1, NUDO + _TIC + "1 di 2.")
toppa('main.hsp', 2698, 'txt " *tic* "', 1, NUDO + _TIC + "2 di 2.")

toppa('main.hsp', 4440, 's = "Nuovo!"', 1,
      NUDO + "main.hsp:*dead_draw, la lapide: marca la partita appena finita "
      "in mezzo alla classifica delle precedenti. ⓘ Le altre righe portano "
      "`cnvrank(cnt + 1)`, cioe' il numero d'ordine, e quella e' gia' a posto "
      "(la desinenza ordinale inglese e' morfologia, e la 85a l'ha tolta).")

toppa('main.hsp', 4449, 's = "nessun dato"', 1,
      NUDO + "main.hsp:*dead_draw, il posto vuoto della classifica quando le "
      "partite finite sono meno di otto. ⓘ Minuscolo come l'inglese: e' un "
      "riempitivo dentro una riga, non un'etichetta.")

toppa('main.hsp', 6550,
      'txt "Il boss non puo\' comparire, ci sono troppi mostri! Un mostro a caso viene eliminato."',
      1,
      NUDO + "main.hsp:*event, l'avviso quando la mappa e' troppo affollata "
      "perche' il boss di un evento ci entri. ⓘ `theres` e' un refuso di "
      "monte. ⓘ Il punto e virgola inglese («because») diventa due frasi: in "
      "italiano la causale lunga dentro un'esclamazione non regge.")

toppa('main.hsp', 8422,
      'txt cnvtalk("Eccoti qui!"), cnvtalk("Ehi, tesoro..."), '
      'cnvtalk("Sei di ritorno!"), cnvtalk("Ti aspettavo da tanto."), '
      'cnvtalk("Che bello riaverti a casa."), cnvtalk("Mi viene da piangere..."), '
      'cnvtalk("Buon lavoro.")', 1,
      NUDO + "main.hsp:*event, quel che dicono i compagni quando si torna a "
      "casa. ⭐ LA SORELLA GIAPPONESE C'E' ED E' :8419 — un blocco "
      "`if ( jp ) … if ( en ) …`, che `_126-sorella-jp.py` non riconosce "
      "perche' cerca gli `else` — e porta 「おかえり」, 「おかえりなさい」, "
      "「お疲れさま」, 「よかった…」, 「ずっと待ってたよ」, 「泣きそう…」. "
      "⚠️⚠️ «BENTORNATO» E' VIETATO QUI: chi parla saluta il GIOCATORE, che in "
      "Elona puo' essere donna, e 「おかえり」 di genere non ne ha. Le sette "
      "rese sono tutte invariabili — «Eccoti qui!», «Sei di ritorno!», «Che "
      "bello riaverti a casa» — e anche «Ti aspettavo da tanto» e' "
      "all'imperfetto apposta, per non avere il participio che «ti ho "
      "aspettato» si tirerebbe dietro. ⓘ 「お疲れさま」 e' «Buon lavoro», che "
      "l'inglese rende con «Cheers for good work».")

# --- help.hsp ---------------------------------------------------------------

toppa('help.hsp', 348, 's = "Guida di Elona", strhint2 + strhint3b', 1,
      NUDO + "help.hsp:*com_help_loop, il titolo della finestra dell'aiuto in "
      "gioco. ⓘ «In-Game» non si rende: in italiano «Guida di Elona» dice gia' "
      "tutto, e il titolo di finestra ha venti caratteri (module.hsp:4339 su "
      "una finestra da 780, dove ne stanno molti di piu').")

toppa('help.hsp', 572, 's = "Nessun messaggio nuovo."', 1,
      NUDO + "help.hsp:*com_chatlog, quel che il registro della chat di rete "
      "scrive quando non e' arrivato niente.")

toppa('help.hsp', 862, 'mes "Elona - Rivedi le scene"', 1,
      NUDO + "help.hsp:*com_story_loop, il titolo della finestra che rigioca "
      "le scene sbloccate. ⓘ La riga accanto (:866) passa da lang() ed e' gia' "
      "italiana. ⓘ Tetto largo: da `wx + 90` (:861) a `wx + 390` (:865), 300 "
      "px, e il carattere qui e' a corpo 10 (`12 - en * 2`, :859).")

toppa('help.hsp', 883, 'mes "(altro)"', 1,
      NUDO + "help.hsp:*com_story_loop, il segno che ci sono altre pagine di "
      "scene. ⓘ Sta a `wx + 590` con il numero di pagina a `wx + 500`: sette "
      "caratteri contro i sei dell'inglese, su un corpo 10 sono 6 px in piu' "
      "in una finestra che di posto ne ha.")

# --- economy.hsp ------------------------------------------------------------

_CITTA = (
    "economy.hsp:*com_politics_economy_loop, l'allineamento della citta' che "
    "si governa: `MDATA_CITY_PROPERTY_VALUE` sceglie fra tre parole, e :319 le "
    "stampa in coda alla riga «Sicurezza (N) …», che passa da lang() ed e' "
    "gia' italiana. ⚠️ Sono ETICHETTE DI STATO, quindi SOSTANTIVI: e' la "
    "regola della guida di stile, e qui il giapponese non c'e' a dirimere. "
)
toppa('economy.hsp', 249, 's1 = "Neutralita\'"', 1,
      NUDO + _CITTA + "Il valore fra -50 e 50. ⚠️ «Neutrale» sarebbe stato un "
      "aggettivo senza nome a cui riferirsi, in fila con «Legge» e «Caos» che "
      "nomi lo sono: le tre parole devono essere della stessa specie.")
toppa('economy.hsp', 252, 's1 = "Legge"', 1,
      NUDO + _CITTA + "Il valore da 50 in su. ⚠️ NON «Leggi», che in "
      "economy.hsp:468 e module.hsp:5163 e' gia' preso e vuol dire un'altra "
      "cosa — le ordinanze che il sindaco promulga. Qui e' il principio "
      "opposto al caos, ed e' singolare.")
toppa('economy.hsp', 255, 's1 = "Caos"', 1,
      NUDO + _CITTA + "Il valore da -50 in giu'. ⭐ Riscossa: `Chaos` -> «Caos» "
      "e' gia' in dizionario a text.hsp:1978 e in undici righe di action.hsp.")

toppa('economy.hsp', 720, 'mes "" + bdref(1, p) + "k oro"', 1,
      NUDO + "economy.hsp:*com_select_building_loop_WHILE1, il prezzo di un "
      "edificio da costruire in citta'. ⭐ RESA RISCOSSA NELLO STESSO FILE: "
      "`\"k gp\"` -> «k oro» e' gia' scritto nella toppa del bilancio "
      "(«Budget:» + … + «k oro»), che il giocatore legge nella schermata "
      "accanto.")

# --- chara_func.hsp ---------------------------------------------------------

toppa('chara_func.hsp', 5980,
      'txt "La barriera di mana assorbe il danno (" + locvar_dmghp_manabar + ")."', 1,
      NUDO + "chara_func.hsp:*dmghp, il messaggio del mod «JAMES CUSTOM - "
      "DAMAGE METER» quando l'MP incassa il colpo al posto degli HP. E' testo "
      "di COMBATTIMENTO, cioe' fra il piu' letto del gioco. ⚠️ Girata perche' "
      "la barriera faccia da soggetto: l'italiano passivo («il danno e' "
      "assorbito») porterebbe un participio, e qui il participio si puo' "
      "evitare senza perdere niente.")

toppa('chara_func.hsp', 6043, 'txt "(" + locvar_dmghp_healn + " risucchiati)"', 1,
      NUDO + "chara_func.hsp:*dmghp, quanto l'attaccante si riprende "
      "risucchiando. ⭐ Il verbo e' riscosso: calculation.hsp:1511 rende gia' "
      "「マナを吸収」 con «si vede risucchiare il mana», e db_item usa «succhia "
      "il mana» per le armi che fanno la stessa cosa. ⓘ Participio al plurale "
      "maschile perche' concorda con i punti vita, non con nessuno.")

# ---------------------------------------------------------------------------


def righe_di(nome):
    if nome not in SORGENTI:
        SORGENTI[nome] = io.open(BASE + '\\' + nome, encoding='cp932').read().split('\n')
    return SORGENTI[nome]


PROIBITI = '…“”～«»'

toppe = []
for nome, n, nuova_grezza, attese, motivo in LAVORO:
    righe = righe_di(nome)
    originale = righe[n - 1]
    indent = originale[:len(originale) - len(originale.lstrip())]
    nuova = indent + degrada(nuova_grezza)
    nuova.encode('cp932')                      # solleva se CP932 non sa scrivere
    cattivi = [c for c in nuova if c in PROIBITI]
    if cattivi:
        raise SystemExit('{}:{}: caratteri proibiti {}'.format(nome, n, cattivi))
    if nuova == originale:
        raise SystemExit('{}:{}: la toppa non cambierebbe niente'.format(nome, n))
    quante = sum(1 for r in righe if r == originale)
    if quante != attese:
        raise SystemExit('{}:{}: attese {} occorrenze di «{}», trovate {}'
                         .format(nome, n, attese, originale.strip()[:50], quante))
    t = {'file': nome, 'cerca': originale, 'sostituisci': nuova, 'motivo': motivo}
    if attese > 1:
        t['tutte'] = True
    toppe.append(t)
    print('{:16s}{:6d}  x{:<3d} {}'.format(nome, n, quante, nuova.strip()[:58]))

dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in toppe).encode('utf-8')
with io.open('lavoro/toppe-127-coda.jsonl', 'wb') as f:
    f.write(dati)
righe_toccate = sum(a for _, _, _, a, _ in LAVORO)
print('{} toppe, {} righe -> lavoro/toppe-127-coda.jsonl'.format(len(toppe), righe_toccate))
