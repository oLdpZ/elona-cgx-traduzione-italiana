# -*- coding: utf-8 -*-
"""Le toppe di `item_func.hsp`: i pezzi di nome che nessuna `lang()` raggiunge.

`item_func.hsp` e' il **compositore dei nomi degli oggetti**: incolla una
sessantina di pezzi — benedizione, materiale, qualita', il nome vero, i titoli
fra parentesi — e la 96a l'ha chiuso a 203 rese. Ma venti pezzi non passano da
nessuna `lang()`, e per venticinque sessioni sono rimasti inglesi dentro nomi
italiani. Diciotto si topano qui; due restano, e sono dichiarati.

## ⭐⭐⭐ Le nove parti del corpo erano gia' decise, in un'altra finestra

`:1338` compone il nome delle **parti necromantiche** — l'oggetto che
`db_item.hsp` lascia senza nome (`ioriginalnameref = ""`) e che si costruisce a
tempo di esecuzione: parte del corpo, poi `" of "` (gia' reso `" di "`,
`item_func.hsp:1007`), poi il nome della creatura. **L'ordine inglese e' gia'
quello italiano**, quindi la parte resta un prefisso e non serve spostarla:
«testa di putit».

⭐ E le nove parole non si scelgono: il progetto le ha **gia' rese**, nel menu
in cui si comprano le parti (`頭（減少生命力)` -> «Testa (Vita -N)» e sorelle).
Qui si riusano in minuscolo, perche' un nome di oggetto e' minuscolo.

    head testa | neck collo | back schiena | chest TORSO | hand mano
    finger dito | arm braccio | waist FIANCHI | leg gamba

⚠️ **«chest» non e' «petto» e «waist» non e' «vita».** Il giapponese dice 胴体
(*torso*) e 腰 (*fianchi*), lo slot si chiama `EQUIP_SLOT_BODY`, e soprattutto
«vita di putit» in italiano si legge *la vita del putit*: la parola sbagliata
qui non e' imprecisa, e' ambigua. Il progetto aveva gia' scelto «Torso» e
«Fianchi» nell'altra finestra, e qui si tiene la stessa parola.

ⓘ **Il ramo giapponese di queste nove sta a `:1034`, ed e' vivo per il
giapponese e morto per noi** (`... == ITEM_ID_NECRO_PARTS & jp`). E' una guardia
**composta**, quindi `lang-nel-ramo-jp.py` non la vede: le sue nove `lang()`
sono estratte da `estrai` e non stanno nel dizionario, e non e' un buco — sono
proprio le righe che l'italiano non esegue.

## L'aggettivo si sposta, il numero no

⚠️ `"decoded "` e `"custom "` sono **prefissi**, e in italiano l'aggettivo segue
il nome. Non si piega il lessico all'ordine inglese: si sposta il pezzo, e il
posto dove metterlo esiste gia' ed e' `locvar_itemname_s6`, la fessura dei
complementi che la build stampa dopo il nome (materiale, manifattura, mobilio).
Regola di `contratto-nomi.md` §3.

    :1330  "decoded "  ->  s6 += " decifrato"      su «libro antico» (maschile)
    :1335  "custom "   ->  s6 += " personalizzata" su «ricetta» (femminile)

ⓘ Il genere si legge in `db_item.hsp` della build, non si indovina:
`ioriginalnamearticolo(ITEM_ID_ANCIENT_BOOK) = "un "`, `(ITEM_ID_RECIPE) = "una "`.

I pezzi fra parentesi restano dove sono — l'ordine di una coda numerica non
cambia fra le due lingue — e prendono la parola che **questo stesso file** ha
gia' scelto: `No.` -> `n.` (`:902`, `:2243`, `:2248`), `Rank` -> `Rango`
(`chat.hsp:25597`), e `Lv.` **resta** (`:2156`), che cambia solo lo spazio.

⚠️ `:1972` porta **due spazi** prima della parentesi ed e' un refuso di monte:
la resa ne lascia uno.

## ⚠️ Le due righe che restano inglesi, e non sono da fare

  1. **`:1809`, `"the "`.** E' il **ripiego dichiarato** dell'articolo: la toppa
     che porta `locvar_itemname_s9` scrive nel suo motivo «se l'articolo
     italiano manca resta quello inglese, come il plurale ripiega sul
     singolare». Toparlo a «il » sarebbe peggio, perche' il genere della testa
     del nome qui non si conosce.
  2. **`:2252`, `" <BGM"`.** `BGM` e' la sigla della traccia, della stessa
     famiglia dei nomi del jukebox che `triage_nudi` classifica `sigla`.

⚠️⚠️ **E resta aperta una cosa che si vede a schermo**: le parti necromantiche
non hanno articolo italiano — `ioriginalnamearticolo(ITEM_ID_NECRO_PARTS)` e'
vuoto perche' il nome e' vuoto — quindi il ripiego stampa «a testa di putit».
Non e' un arretramento (prima diceva «a head of putit»), ma si chiude solo
mettendo `locvar_itemname_s8`/`s9` **dopo** la loro inizializzazione, che nella
build sta a `:1903`, e non qui: e' una toppa a blocco e una decisione.

⚠️ Si compone tutto in memoria e si scrive alla fine: regola della 39a.
"""
import io
import json

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
NOME = 'item_func.hsp'
USCITA = 'scratchpad/_126-toppe-item-func.jsonl'

_CIECO = (
    "LETTERALE INGLESE NUDO dentro il compositore dei nomi: non passa da "
    "nessuna lang(), quindi non ha firma ne' voce di dizionario e nessun lotto "
    "puo' raggiungerlo (quinto punto cieco, nudi_en.py, 49a). "
)

_PARTI = (
    "item_func.hsp:1338, il nome delle PARTI NECROMANTICHE, che db_item.hsp "
    "lascia senza nome (ioriginalnameref = \"\") e che si compone a tempo di "
    "esecuzione: parte del corpo + \" di \" (item_func.hsp:1007) + nome della "
    "creatura. L'ordine inglese e' gia' quello italiano, quindi la parte resta "
    "un prefisso. ⭐ La parola non si sceglie qui: il progetto l'ha gia' resa "
    "nel menu in cui le parti si comprano (「%s（減少生命力)」 -> «%s (Vita -N)»), "
    "e qui si riusa in minuscolo perche' un nome di oggetto e' minuscolo. "
)

# (riga, [(letterale, resa)] oppure None, riga intera nuova, motivo, tutte)
CASI = [
    (1340, [('"head"', '"testa"')], None, _CIECO + _PARTI % ('頭', 'Testa'), False),
    (1343, [('"neck"', '"collo"')], None, _CIECO + _PARTI % ('首', 'Collo'), False),
    (1346, [('"back"', '"schiena"')], None, _CIECO + _PARTI % ('背中', 'Schiena'), False),
    (1349, [('"chest"', '"torso"')], None,
     _CIECO + _PARTI % ('胴体', 'Torso') +
     "⚠️ NON «petto»: il giapponese dice 胴体, cioe' *torso*, lo slot si chiama "
     "EQUIP_SLOT_BODY, e la resa gia' decisa nell'altra finestra e' «Torso». "
     "L'inglese «chest» e' la parola imprecisa delle due.", False),
    (1352, [('"hand"', '"mano"')], None, _CIECO + _PARTI % ('手', 'Mano'), False),
    (1355, [('"finger"', '"dito"')], None, _CIECO + _PARTI % ('指', 'Dito'), False),
    (1358, [('"arm"', '"braccio"')], None, _CIECO + _PARTI % ('腕', 'Braccio'), False),
    (1361, [('"waist"', '"fianchi"')], None,
     _CIECO + _PARTI % ('腰', 'Fianchi') +
     "⚠️⚠️ NON «vita»: qui la parola sbagliata non sarebbe imprecisa, sarebbe "
     "AMBIGUA — «vita di putit» in italiano si legge *la vita del putit*, e "
     "questo e' il nome di un pezzo di cadavere. Il giapponese dice 腰 e la "
     "resa gia' decisa e' «Fianchi».", False),
    (1364, [('"leg"', '"gamba"')], None, _CIECO + _PARTI % ('足', 'Gamba'), False),

    (1330, None, '\t\t\t\tlocvar_itemname_s6 += " decifrato"',
     _CIECO +
     "item_func.hsp:1328, il libro antico dopo che e' stato decifrato "
     "(INV_ITEM_PARAM2 != 0). ⚠️ In inglese e' un PREFISSO e in italiano "
     "l'aggettivo segue il nome: non si piega il lessico all'ordine inglese, si "
     "sposta il pezzo (contratto-nomi.md §3). Il posto dove metterlo esiste "
     "gia' ed e' `locvar_itemname_s6`, la fessura dei complementi che la build "
     "stampa dopo il nome — la stessa che porta materiale e manifattura. "
     "ⓘ Il genere si legge in db_item.hsp: "
     "ioriginalnamearticolo(ITEM_ID_ANCIENT_BOOK) = \"un \", quindi «libro "
     "antico decifrato».", False),

    (1335, None, '\t\t\t\tlocvar_itemname_s6 += " personalizzata"',
     _CIECO +
     "item_func.hsp:1333, la ricetta senza sottonome, cioe' quella che il "
     "giocatore si e' fatto da se'. Stessa strada di :1330: prefisso inglese "
     "-> complemento in coda, dentro `locvar_itemname_s6`. "
     "ⓘ ioriginalnamearticolo(ITEM_ID_RECIPE) = \"una \", quindi femminile: "
     "«ricetta personalizzata».", False),

    (1031, [('" (No."', '" (n. "')], None,
     _CIECO +
     "item_func.hsp:1030, il numero della carta da collezione. «No.» in questo "
     "stesso file e' gia' reso «n.» tre volte (:902 « di Rachel n.», :2243 « n. "
     "serie », :2248 « immobile n. »): qui si segue la parola del file, e lo "
     "spazio dopo il punto e' quello che l'italiano scrive.", False),

    (1964, [('" (Lv."', '" (Lv. "')], None,
     _CIECO +
     "item_func.hsp:1962, il livello dei frammenti e delle pietre (fossile "
     "misterioso, frammento di memoria, destone). ⓘ «Lv» RESTA: il progetto lo "
     "scrive cosi' 51 volte, e questo stesso file lo tiene a :2156 (« Lv. »). "
     "Cambia solo lo spazio dopo il punto, che l'italiano vuole e :2156 ha gia'. "
     "⚠️ :1968 porta lo STESSO testo e vuole la stessa resa, e non serve "
     "`tutte`: le due righe hanno un'indentazione diversa (cinque tabulazioni "
     "contro quattro), quindi ciascuna aggancia la sua e l'ambiguita' non "
     "nasce. Se un giorno upstream le riallineasse, questa toppa si fermerebbe "
     "da sola invece di toppare quella sbagliata.", False),

    (1968, [('" (Lv."', '" (Lv. "')], None,
     _CIECO +
     "item_func.hsp:1967, il livello del biglietto di addestramento. Stessa "
     "resa di :1964, riga identica a meno dell'indentazione.", False),

    (1972, [('"  (Lv."', '" (Lv. "')], None,
     _CIECO +
     "item_func.hsp:1970, il livello della pietra del risveglio. ⚠️ QUI "
     "L'INGLESE HA DUE SPAZI prima della parentesi, dove le due righe sorelle "
     "(:1964, :1968) ne hanno uno: e' un refuso di monte, e la resa ne lascia "
     "uno solo.", False),

    (1980, [('" (Rank: "', '" (Rango: "')], None,
     _CIECO +
     "item_func.hsp:1977, il rango di un cibo cucinato. «Rank» e' gia' reso "
     "«Rango» dove indica un grado numerico (chat.hsp:25597 « Rango:», "
     "db_item.hsp «Un letto (rango 7)»); «classe» e' la resa dell'altro senso, "
     "quello delle categorie dell'arena, e qui non c'entra.", False),

    (1985, [('" (No."', '" (n. "')], None,
     _CIECO +
     "item_func.hsp:1984, il numero del colore nella bottiglia di tintura. "
     "Stessa parola di :1031 e delle tre righe di questo file che rendono «No.» "
     "con «n.».", False),

    (2146, [('" (Lost property)"', '" (Oggetto smarrito)"')], None,
     _CIECO +
     "item_func.hsp:2144, il portafoglio e la valigetta trovati per terra. "
     "⚠️ Non «(Smarrito)»: e' un participio, e i due oggetti che lo portano "
     "hanno generi diversi — «il portafoglio smarrito» ma «la valigetta "
     "smarrita». Il sostantivo non si accorda con niente e dice la stessa cosa; "
     "e' la strada di guida-stile.md, la stessa di «Fuori combattimento» per "
     "«Incapacitated».", False),
]

ACCENTATE = 'àèéìòùÀÈÉÌÒÙ'

righe = io.open(f'{SORGENTE}\\{NOME}', encoding='cp932').read().split('\n')
nuove = []
for numero, coppie, intera, motivo, tutte in CASI:
    riga = righe[numero - 1]
    if righe.count(riga) != 1 and not tutte:
        raise SystemExit(f'{NOME}:{numero} compare {righe.count(riga)} volte: '
                         'il cerca va allargato o vuole `tutte`')
    if intera is not None:
        nuova = intera
        vecchia_testa = riga[:len(riga) - len(riga.lstrip('\t'))]
        nuova_testa = nuova[:len(nuova) - len(nuova.lstrip('\t'))]
        if vecchia_testa != nuova_testa:
            raise SystemExit(f'{NOME}:{numero}: la riga nuova ha '
                             f'{len(nuova_testa)} tabulazioni invece di '
                             f'{len(vecchia_testa)}')
    else:
        nuova = riga
        for prima, dopo in coppie:
            if riga.count(prima) != 1:
                raise SystemExit(f'{NOME}:{numero} contiene {prima!r} '
                                 f'{riga.count(prima)} volte')
            nuova = nuova.replace(prima, dopo)
    if nuova == riga:
        raise SystemExit(f'{NOME}:{numero} non cambia')
    fuori = [c for c in ACCENTATE if c in nuova]
    if fuori:
        raise SystemExit(f'{NOME}:{numero} porta {fuori}: le toppe si scrivono '
                         "gia' degradate (e', piu', cosi')")
    nuova.encode('cp932')
    toppa = {'file': NOME, 'cerca': riga, 'sostituisci': nuova, 'motivo': motivo}
    if tutte:
        toppa['tutte'] = True
    nuove.append(toppa)

testo = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in nuove)
io.open(USCITA, 'w', encoding='utf-8', newline='\n').write(testo)
print(f'{len(nuove)} toppe in {USCITA}')
