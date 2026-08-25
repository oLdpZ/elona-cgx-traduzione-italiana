# -*- coding: utf-8 -*-
"""96a - `item_func.hsp`: i pezzi con cui si compone il nome di un oggetto.

78 rese fra `:695` e `:1124`, tutte dentro `*itemNameSub` (`:693`-`:1118`).
Sei firme del blocco non sono qui: le rinvia `_96-rinvia-nome.py`.

⭐⭐⭐ LA COSA CHE RENDE POSSIBILE QUESTO LOTTO: IN INGLESE IL COMPOSITORE GIRA
**DOPO** IL NOME, IN GIAPPONESE PRIMA. `gosub *itemNameSub` compare due volte, e
le due chiamate stanno in due rami di lingua diversi — verificato con
`scratchpad/_96-rami-jp.py`:

    :1394   sotto `jp`   -> il blocco e' un PREFISSO   「エヘカトルの祭壇」
    :1936   sotto `en`   -> il blocco e' un SUFFISSO   «altare di Ehekatl»

E' la stessa posizione che vuole l'italiano. Percio' queste 78 si traducono
oggi, mentre le 24 di `:1300`-`:1458` — che stanno in `itemname()` **prima** del
nome (`:1731`, `:1747`, `:1770`) — no: li' l'ordine e' quello giapponese e non
si sistema con una resa. ⚠️ **Il file non si divide per argomento, si divide
per dove gira il compositore.** Nel vault:
[[il-lavoro-si-raggruppa-come-lo-legge-chi-lo-usa]], che qui vale al contrario —
non e' chi legge a raggruppare, e' chi concatena.

⭐⭐⭐ LA SECONDA: L'INGLESE INCORNICIA, IL GIAPPONESE DICE «DI» — E L'ITALIANO
STA COL GIAPPONESE. Sei voci di questo lotto compongono un complemento, e
l'inglese lo risolve con le angolari invece che con la preposizione:

    :920   altare    「godname + の」      « <Ehekatl>»        -> « di Ehekatl»
    :1092  vomito    「refchara + の」      « of X»             -> « di X»
    :1007  fuso      「(vuoto)」            « of »              -> « di »
    :880   libro     「《titolo》という題名の」 « titled <T>»       -> « dal titolo <T>»

Le angolari restano dove incorniciano un **titolo** (`:880`, `:898`, `:907`,
`:913`), che e' anche l'uso italiano; spariscono dove reggevano un
**complemento** (`:920`), dove l'italiano ha la preposizione e il giapponese pure.

⚠️ DEROGA 1 — `:898` E `:913`: «Art of» NON C'E' NEL GIAPPONESE. L'inglese
scrive « titled <Art of Fishing>» dove il giapponese ha 「《釣り》という題名の」,
cioe' solo il nome dell'abilita' fra parentesi. L'aggiunta inglese non si puo'
nemmeno tradurre bene: «l'arte di X» vuole la preposizione giusta per ogni
abilita' — «l'arte **della** pesca», «l'arte **del** commercio» — e la
preposizione la sceglierebbe una `lang()` che non sa che parola arrivera'.
Si segue il giapponese e l'aggiunta cade: «dal titolo <Pesca>».
💡 E' la stessa ragione per cui l'articolo lo porta il nome (`contratto-nomi.md`
§4): quel che dipende dalla parola non si decide dove la parola non si vede.

⚠️ DEROGA 2 — `:713` PERDE LA `s`. L'inglese compone il nome dell'oggetto
d'evoluzione come `"<" + evitemn(...)` e lo chiude con `"s>"` al plurale,
`">"` al singolare (mod BLOODYSHADE, `:712`-`:717`). In italiano il plurale non
si fa col suffisso — e' un **dato**, per nome, come dice `contratto-nomi.md`
§4-bis — quindi la resa e' `>` in tutt'e due i rami. E' la regola di
`guida-stile.md` sulle funzioni di morfologia inglese (`_s()`, `is()`): si
tolgono, non si traducono. ⚠️ Il ramo resta e non fa danno: scrive lo stesso
carattere due volte.

⭐⭐ LA TERZA: IL POTIOMAN SI TRADUCE A META', E IL CONFINE LO DICE
`item_data.hsp`. I sei **modi** hanno un senso dichiarato dalla forma distesa
gia' resa (`:702`-`:707`) e diventano italiani — スピニング e' `Rotante` perche'
«Imprime al tappo una rotazione tremenda»; i 28 **sottonomi** e le 11 **sigle**
sono nomi coniati e restano. Il ragionamento per esteso, con la tabella, sta in
`invariati.md`, sezione «Nomi coniati del potioman».
⚠️ E i quattro nomi base (`:725`-`:734`) **sono** il nome dell'oggetto:
`ioriginalnameref(ITEM_ID_CF_POTIOMAN)` e' vuoto (`db_item.hsp:135599`). Quindi
prendono l'ordine italiano — «potioman da battaglia», non «battaglia potioman» —
e «potioman» e' parola gia' tenuta, dalle rese del fabbro (`chat.hsp:3118`,
84a: «il tuo nuovo potioman»).

⭐ LA QUARTA: IL CAFFE' E IL TE' SI POSSONO FARE, IL SUCCO NO, E LA DIFFERENZA
E' UNA RIGA. `:924` mette il nome del frutto **davanti** ai tre pezzi del succo,
quindi «succo di mela» non e' raggiungibile e le quattro voci sono rinviate. Per
il caffe' (`:939`-`:945`) e il te' (`:947`-`:953`) davanti non c'e' niente e il
nome base e' vuoto: escono interi. 紅茶 e' **te' nero** e non «te'» generico —
il gioco ha anche `ITEM_ID_GREEN_TEA`, e i due vanno distinti.

LESSICO EREDITATO (non deciso qui):
  - potioman            `chat.hsp:3017`-`:3118` (84a)
  - Ehekatl, Opatos, Itzpalt, Jure, Mani   `db_item.hsp`, invariati
  - oro                 `text.hsp:193`
  - tesoro segreto      `db_item.hsp:143525`
  - ricetta             `db_item.hsp:141815`

PERIMETRO: 84 firme nel blocco, 78 rese + 6 rinviate. Nessuna esce da un ramo
`if ( jp )` e nessuna sta in un commento di blocco — controllate tutte con
`scratchpad/_96-rami-jp.py` e con `strumenti.commenti.righe_in_commento()`, che
ha trovato `:704`.

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""
import io, json, sys

RESE = {
    # --- cornici attorno a una funzione: quel che si legge lo scrive lei
    695: '"(" + moneyboxn(inv(INV_ITEM_PARAM2, itemowner_itemid)) + ")"',
    698: '" <" + biten(inv(INV_ITEM_PARAM1, itemowner_itemid)) + ">"',
    710: '"<" + evitemn(inv(INV_ITEM_PARAM1, itemowner_itemid))',
    713: '>',   # l'inglese qui mette «s>»: il plurale italiano non e' un suffisso
    716: '>',

    # --- i quattro potioman di serie: qui il nome dell'oggetto e' vuoto
    725: 'potioman CF',
    728: "potioman d'urto",
    731: 'potioman da battaglia',
    734: 'potioman super',

    # --- i sei modi, dalla forma distesa di `item_data.hsp:702`-`:707`
    738: 'Rotante',
    741: 'Potente',
    744: 'Doppio',
    747: 'Rapido',
    750: 'Preciso',
    753: 'Ingannevole',

    # --- i 28 sottonomi coniati: vedi `invariati.md`
    756: '-Flaenix', 759: '-Grifeak', 762: '-Pegather', 765: '-Dragoul',
    768: '-Ravrain', 771: '-Valkspear', 774: '-Orfin', 777: '-Wolfang',
    780: '-Leoheart', 783: '-Tigelaw', 786: '-Foxail', 789: '-Bearm',
    792: '-Ifheat', 795: '-Dinoguts', 798: '-Cerbeads', 801: '-Bihorn',
    804: '-Wyverng', 807: '-Leviascale', 810: '-Bushilade', 813: '-Ogreand',
    816: '-Stagito', 819: '-Goledy', 822: '-Knimail', 825: '-Soldigun',
    828: '-Deatranium', 831: '-Giganoot', 834: '-Kobolord', 837: '-Hercurest',

    # --- le 11 sigle della parte montata: un segno, non una parola
    840: ' F', 843: ' I', 846: ' L', 849: ' D', 852: ' M', 855: ' P',
    858: ' H', 861: ' S', 864: ' N', 867: ' C', 870: 'X',

    # --- i libri: le angolari incorniciano un titolo, e li' restano
    880: '" dal titolo <" + magebookn(inv(INV_ITEM_BOOK_ID, itemowner_itemid)) + ">"',
    885: ' ormai inservibile',
    892: '" di " + rpname(inv(INV_ITEM_SUB_NAME, itemowner_itemid))',
    898: '" dal titolo <" + skillname(inv(INV_ITEM_BOOK_ID, itemowner_itemid)) + ">"',
    902: ' di Rachel n.',
    907: '" dal titolo <" + booktitle(inv(INV_ITEM_BOOK_ID, itemowner_itemid)) + ">"',
    913: '" <" + skillname(inv(INV_ITEM_PARAM1, itemowner_itemid)) + ">"',
    916: '"<" + _seikaku(inv(INV_ITEM_PARAM1, itemowner_itemid)) + "> "',

    # --- l'altare: qui le angolari reggevano un complemento, e cadono
    920: '" di " + godname(inv(INV_ITEM_GOD, itemowner_itemid))',

    # --- caffe' e te' (il succo e' rinviato: il frutto gli sta davanti)
    941: 'caffelatte',
    944: 'caffè',
    949: 'tè al latte',
    952: 'tè nero',

    # --- il fuso dell'anima, la fattura, quel che qualcuno ha lasciato a terra
    1007: ' di ',
    1085: '" <" + inv(INV_ITEM_SUB_NAME, itemowner_itemid) + " oro>"',
    1092: '" di " + refchara(inv(INV_ITEM_SUB_NAME, itemowner_itemid), DBSPEC_CHARA_NAME_ORG, 1)',

    # --- il tesoro segreto: di chi e' la benedizione
    1097: ' del giusto',
    1100: ' del malvagio',
    1103: ' di Ehekatl',
    1106: ' di Opatos',
    1109: ' di Itzpalt',
    1112: ' di Jure',
    1115: ' di Mani',

    # --- e l'oggetto che questa versione non sa piu' leggere
    1124: 'oggetto sconosciuto (versione incompatibile)',
}

LOTTO = 'lavoro/96-item_func-nome.jsonl'

voci = [json.loads(l) for l in io.open(LOTTO, encoding='utf-8') if l.strip()]

# le rinviate escono dal lotto: `_96-rinvia-nome.py` gira PRIMA di questo
rinviate = {json.loads(l)['firma'] for l in io.open('rinviate.jsonl', encoding='utf-8')
            if l.strip()}
voci = [v for v in voci if v['firma'] not in rinviate]

mancanti = [v['riga'] for v in voci if v['riga'] not in RESE]
in_piu = [r for r in RESE if r not in {v['riga'] for v in voci}]
if mancanti or in_piu:
    print('mancanti: %s' % mancanti)
    print("in piu' : %s" % in_piu)
    sys.exit(1)

with io.open(LOTTO, 'w', encoding='utf-8', newline='\n') as fh:
    for v in voci:
        v['it'] = RESE[v['riga']]
        fh.write(json.dumps(v, ensure_ascii=False) + '\n')
print('%d rese scritte in %s' % (len(voci), LOTTO))
