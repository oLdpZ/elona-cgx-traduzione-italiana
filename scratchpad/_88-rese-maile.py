# -*- coding: utf-8 -*-
"""Le rese di MAILE la sacerdotessa fantoccio (`chat.hsp:13266`-`:13516`).

Perimetro: 48 firme dentro, **48 da fare**, zona chiusa, nessuna occorrenza
fuori. ⚠️ **Nessuna resa gia' fatta nella zona**: il registro non si eredita da
qui, si va a prendere altrove.

REGISTRO. Maile e' **donna** (`CDATA_SEX = 1`, `db_creature.hsp:60888`),
allineamento -10000, e le sue tre battute di `db_creature.hsp` sono gia' rese
(`scratchpad/repertorio.py Maile`):

    「グレティラとナゴレウの仇は必ずとります」  Vendichero' Gretilla e Nagarew,
                                                costi quel che costi.
    「本来の肉体があればこのような失態は…」      Con il mio vero corpo, una
                                                figuraccia simile...
    「イキーャ様のために…」                      Tutto per il sommo Iquilla...

Cioe': solenne, controllata, devota. In giapponese parla in 敬語 (のです /
ましょう) e da' del 貴方 al giocatore. ⭐ In italiano si traduce col **voi di
cortesia**, e non e' solo questione di tono: il voi e' l'unica seconda persona
che **non chiede un genere**, e qui il bersaglio e' il giocatore.

⭐⭐⭐ LA ZONA E' UN SERVIZIO SOLO, e la sua forma e' il punto.
Maile cancella i ricordi del giocatore — la Nefia piu' profonda, la gilda, il
passato, i tratti di karma, il rapporto con un compagno, l'esperienza,
l'arma vivente, il Vuoto — e **non lo dice mai**: mette in scena, in rosso,
**trentaquattro finte righe di errore di sistema**, una per variabile
azzerata. Trentaquattro delle 48 firme sono quella riga con dentro un nome
diverso.

⚠️⚠️ **La resa di quella riga NON si inventa: esiste gia'.** `proc.hsp:26301`
— la versione troncata che compare quando il [記憶の灯] attutisce la
cancellazione — dice «**[Sistema]Errore di origine ignota in globalda...**».
Il modello qui sotto e' scritto perche' quella riga vecchia ne sia una
troncatura esatta: stessa apertura, stesso «in» davanti al nome.

⚠️ **I nomi delle variabili restano in inglese e non si toccano**, che e'
quello che li rende spaventosi. Non sono lessico: sono l'oggetto della finta
diagnostica. (Il giapponese di monte scrive i nomi grezzi — `globaldata189`,
`globalrcbit961` — e l'inglese quelli simbolici; si segue l'inglese.)

LESSICO, cercato e non deciso:

  <Maile> la sacerdotessa fantoccio   `db_creature.hsp:60839`
  il Vuoto                            `text.hsp:2773` (すくつ)
  talento                             `command.hsp:2143`, «[Feat]» -> «[Talento]»
  gilda, Nefia                        gia' in uso in tutto `chat.hsp`

⚠️⚠️ IL TETTO CHE MORDE DAVVERO: **il menu ha UNDICI voci**, e sopra le dieci
la pergamena passa a **due colonne** e taglia con `strmid` a **24 caratteri**
(`chat.hsp:25164`-`:25166`). Non e' il tetto prudenziale da 58: qui il taglio
succede. Tutte e undici stanno nei 24, contate sulla forma degradata.

⚠️ LE DEROGHE DICHIARATE

1. **Le voci del menu perdono «Memory of»** («Memory of the deepest Nefia»,
   «Memory of belonging Guild», «Memory of living weapon»). Ci stanno tre
   ragioni: il tetto di 24 caratteri, il fatto che il giapponese ce l'ha solo
   in due voci su undici (「〜の記憶」 contro 「〜のこと」), e la battuta che
   apre il menu, che dice gia' che si sta scegliendo un ricordo.

2. **`:13382`** — `is(rc)` e' morfologia inglese (il verbo essere accordato al
   numero) e in italiano sparisce. La resa e' costruita perche' il participio
   non accordi: «come se non ti avesse mai visto» sta col compagno, non col
   giocatore.

3. **Il giapponese di `:13289`, `:13392`, `:13394`, `:13417`, `:13419`,
   `:13503` e `:13505` dice qualcosa in piu' o di diverso** — 「再計算を行い
   ます…」 («ricalcolo in corso»), 「再計算されました」 («ricalcolato») invece
   di 「初期化されました」, e a `:13373` 「削除されました」 («cancellato»).
   L'inglese appiattisce tutto su «has been initialized», e si segue
   l'inglese: **una finta diagnostica funziona perche' e' identica a se
   stessa**, e trentaquattro righe con tre formule diverse smetterebbero di
   sembrare una macchina.
"""

RESE = {}

# ============ il menu: undici voci, tetto vero di 24 caratteri ============

RESE[13268] = 'Niente del genere'
RESE[13269] = 'La Nefia più profonda'
RESE[13270] = 'La gilda'
RESE[13271] = 'Prima del viaggio'
RESE[13272] = 'Coscienza e malizia'
RESE[13273] = 'Il legame col compagno'
RESE[13274] = 'La mia esperienza'
RESE[13275] = 'Esperienza del compagno'
RESE[13276] = 'Talenti da negoziante'
RESE[13277] = "L'arma vivente"
RESE[13279] = 'La discesa nel Vuoto'

# ============ le due battute ============

RESE[13281] = ("Su, concentratevi soltanto sul ricordo che volete cancellare. Lo toglierò "
               "per bene dalla vostra testa e da questo mondo, senza lasciarne traccia.")
RESE[13293] = 'E con questo, un altro passo...'

# ⚠️ deroga 2: `is(rc)` e' morfologia inglese, e il participio non deve accordare.
RESE[13382] = 'name(rc) + " ti guarda come se non ti avesse mai visto..."'


# ============ le trentaquattro finte righe di errore ============
#
# ⚠️ Il modello e' quello gia' in build a `proc.hsp:26301`, di cui la riga
# vecchia — «[Sistema]Errore di origine ignota in globalda...» — dev'essere una
# troncatura esatta. I nomi delle variabili non si traducono.

def _sistema(nome: str) -> str:
    return '[Sistema]Errore di origine ignota in %s: valore reinizializzato.' % nome


VARIABILI = {
    13289: 'GDATA_DEEPEST_LEVEL',
    13299: 'GDATA_RANK_GUILD',
    13301: 'GDATA_FLAG_GUILD_THIEF',
    13303: 'GDATA_FLAG_GUILD_FIGHTER',
    13305: 'GDATA_FLAG_GUILD_MAGE',
    13307: 'GDATA_FLAG_GUILD_MAGE_NORMA',
    13309: 'GDATA_FLAG_GUILD_THIEF_NORMA',
    13311: 'GDATA_FLAG_SUB_GUILD_MAGE',
    13313: 'GDATA_FLAG_SUB_GUILD_THIEF',
    13315: 'GDATA_FLAG_SUB_GUILD_FIGHTER',
    13317: 'GDATA_FLAG_SUB_FIGHTER_1',
    13319: 'GDATA_FLAG_SUB_MAGE_1',
    13321: 'GDATA_FLAG_SUB_THIEF_1',
    13341: 'CDATA_BACKGROUND_PART_A1',
    13343: 'CDATA_BACKGROUND_PART_A2',
    13353: 'TRAIT_OTHER_WICKED',
    13355: 'TRAIT_OTHER_SAINT',
    13369: 'CDATA_IMPRESSION',
    13371: 'CDATA_MASTER_SERVANT',
    13373: 'CHARA_BIT_MARRIED',
    13392: 'CDATA_INIT_ATTR',
    13394: 'CDATA_INIT_SPEED',
    13417: 'CDATA_INIT_ATTR',
    13419: 'CDATA_INIT_SPEED',
    13443: 'CHARA_BIT_SHOP_ELEGANCE',
    13445: 'CHARA_BIT_SHOP_AESTHETIC_SENSE',
    13447: 'CHARA_BIT_SHOP_SALES_ROUTE',
    13449: 'CHARA_BIT_SHOP_STRONG_ALLY',
    13451: 'CHARA_BIT_SHOP_BUSINESS_SMILE',
    13453: 'CDATA_SALES_FEATS',
    13483: 'INV_ITEM_EXP',
    13485: 'INV_ITEM_GROWTH',
    13503: 'AREA_VOID',
    13505: 'GDATA_VOID_BOSS',
}

for _riga, _nome in VARIABILI.items():
    RESE[_riga] = _sistema(_nome)
