# -*- coding: utf-8 -*-
"""96a - `item_func.hsp`: le parentesi di stato della riga d'inventario.

53 firme fra `:1975` e `:2248`. Non sono prosa: sono i **pezzi che il gioco
attacca in coda al nome dell'oggetto** mentre lo compone (`itemname()`), e il
giocatore le legge su ogni bacchetta carica, ogni contenitore, ogni cibo, ogni
carico da commercio. Sono la parte di questo file **meno intrecciata con la
grammatica del nome**: stanno dentro le loro parentesi e non concordano con
niente. Per questo aprono il file.

⭐⭐⭐ LA COSA CHE CAMBIA IL LOTTO: LA BARA DELLA NEGROMANZIA NON ELENCA
PAROLE, ELENCA OTTO CREATURE CHE IL PROGETTO HA GIA' BATTEZZATO.
L'inglese scrive `(cat)`, `(dragon)`, `(dead-eyes)`, `(doll)`, `(skeleton)`, e
sembrano etichette generiche. Non lo sono: `chara_func.hsp:8862` elenca gli otto
`CREATURE_ID` della negromanzia **nello stesso ordine** dei `PARAM1` 2..9 —
CAT_ZOMBIE, ZOMBIE, MUMMY, SKELETON_WARRIOR, LICH, NECRO_DOLL, DRAGON_ZOMBIE,
DEAD_EYES_BLOOD_DRAGON. Sono nomi propri di creatura, e stanno **gia' tutti in
`db_creature.hsp`**:

    猫ゾンビ      :90374   il gatto zombi          ドラゴンゾンビ :92807  il drago zombi
    ゾンビ        :107615  lo zombi                リッチ        :108009 il lich
    マミー        :111272  la mummia               ネクロドール   :79817  la necrobambola
    骸骨戦士      :114551  lo scheletro guerriero  デッドアイズ…  :79753  il drago di sangue
                                                                         dagli occhi morti

⚠️ Due sarebbero uscite sbagliate seguendo l'inglese: `(skeleton)` e' **lo
scheletro guerriero** (骸骨戦士, non 骸骨), e `(dragon)` e `(dead-eyes)` sono
**due draghi diversi** che l'inglese distingue per meta' nome ciascuno.
💡 E' di nuovo la lezione della 95a: qui il raggruppamento non e' «le parentesi
di `item_func.hsp`», e' «i nomi che stanno in un altro file».

⚠️ DEROGA 1 — L'ARTICOLO SI TOGLIE. In `db_creature.hsp` il nome porta il
proprio articolo («lo zombi»), perche' li' e' il soggetto di una frase. Qui e'
un'**apposizione fra parentesi** attaccata al nome di un oggetto: «una bara
della negromanzia (lo zombi)» non si legge. Si scrive «(zombi)». Stessa ragione
per cui le sei qualita' sono invariabili (`guida-stile.md`, «l'etichetta si
legge dove esce»).

⚠️ DEROGA 2 — `:2110` NON PORTA IL NOME INTERO. «il drago di sangue dagli occhi
morti» dentro una parentesi, in coda a un nome gia' composto, sono 33 caratteri
per una riga d'inventario. La parentesi serve a **distinguerlo da `:2107`**, e
«(occhi morti)» lo distingue: e' la stessa scelta che ha fatto l'inglese, che
tiene «dragon» per l'uno e «dead-eyes» per l'altro.

⭐⭐ LA SECONDA: I DUE `(Empty)` NON SONO LA STESSA PAROLA, E IL GENERE LO DICE
IL SITO. `:2156` esce **solo** sulla sfera dei mostri (`ITEM_ID_MONSTER_BALL`,
femminile, `db_item.hsp:143296`): li' «(vuota)» e' giusto e si puo' accordare.
`:2192` esce su **ogni** contenitore (`FILTER_CONTAINER`) — cassa, forziere,
borsa, valigia — e un aggettivo li' sceglierebbe il genere sbagliato una volta
su due: «(niente dentro)», che non ha genere.

⚠️ **E nessuna rete vede questa coppia.** Qui c'era scritto che
`battute --divergenti` le avrebbe elencate: e' falso, e il conto lo dimostra —
resta **13** dopo il lotto. Quello strumento cerca **un giapponese reso in piu'
modi**, e questi due giapponesi sono diversi: 空 sulla sfera, 空っぽ sul
contenitore. E' l'**inglese** a essere lo stesso, avendo fuso due parole che il
giapponese distingue. Una rete che cerchi gli inglesi divergenti non c'e', e
sarebbe l'altra meta' di `--divergenti`: qui avrebbe trovato una coppia
legittima, ma e' esattamente la forma in cui si nasconde una resa sbagliata per
imitazione (la lezione della 90a, il riquadro che taglia).

⚠️ DEROGA 3 — LE QUATTRO SFERE OSCURE SONO CODICE MORTO, E L'HO VERIFICATO
PRIMA DI TRADURLE. I ventun modi fra `:2006` e `:2072` appartengono a
`ITEM_ID_JADE/AZURE/CRIMSON/WHITE_DARK_ORB`, e l'effetto di quegli oggetti e'
`action.hsp:15057`: 「開発中。」 / «Under development.» Nessuno dei ventun nomi
compare altrove nel sorgente — cercati tutti e ventuno in tutti i `.hsp`. Il
**nome** pero' si compone lo stesso e si legge nell'inventario, quindi vanno
resi; ma non c'e' un effetto da guardare per decidere il senso, e questa e' la
sola famiglia del lotto dove l'unica prova disponibile e' la parola.

⚠️ E l'inglese li' e' il testimone peggiore del lotto:
  - `トラバサミ` -> «torabasami»: l'inglese **si arrende e translittera**. E'
    虎挟み, la **tagliola** (`罠` -> «trappola» in dodici rese, da `action.hsp`);
  - `エレキホース` -> «electric horse»: `ホース` qui e' **hose**, non horse. Sta
    in una famiglia di trappole d'ambiente (pavimento a gas, catapulta,
    tagliola), non di cavalli: «tubo elettrico»;
  - `デンジカタパルト` -> «(electromagnetic)»: l'inglese **butta la catapulta**,
    che e' l'unica parola concreta della voce;
  - `レインロック` -> «rock rain»: l'inglese inverte i due pezzi. E' レイン+ロック,
    «pioggia di rocce», e l'ordine giusto in italiano coincide col giapponese.

⭐ LA TERZA: `モード` NON E' «Model». `:2077` e i suoi due gemelli dicono
モード = **modo**; l'inglese scrive «Model-1», che e' un'altra parola (forma,
non modalita'). Si segue il giapponese (57a).

⭐⭐ LA QUARTA: I DUE PRESAGI SI AGGANCIANO A UNA FAMIGLIA GIA' SCRITTA, MA NON
CI ENTRANO DENTRO. `text.hsp:182`, `:183` e `:192` rendono i tre stati certi
con un complemento invariabile — «con maledizione», «con benedizione», «con
dannazione». `:2178` (恐ろしい) e `:2181` (禍々しい) sono gli stessi due stati
ma **prima che il giocatore li sappia**: sono la sensazione, non il verdetto, e
copiarci sopra «con maledizione» direbbe al giocatore una cosa che il gioco gli
sta nascondendo apposta. Restano sostantivi invariabili — «(spavento)»,
«(malaugurio)» — come vuole `guida-stile.md`.

LESSICO EREDITATO (non deciso qui):
  - cariche        `action.hsp:6742`  «Non ha piu' cariche.»
  - esca           `action.hsp:12067` e sei altri siti
  - trappola       `action.hsp:6238`  «Scopri una trappola.»
  - Lv             gia' in `invariati.md`: l'italiano scrive uguale
  - veleno         `text.hsp:69`
  - globo oscuro   `db_item.hsp:135698`, `:135711`, `:135724`
  - sfera dei mostri, bara della negromanzia, canna da pesca, borsa del mercante

PERIMETRO: 53 firme su 53, tutte dentro `itemname()`. Nessuna esce da un ramo
`if ( jp )` (`python scratchpad/_96-rami-jp.py`: le nove spente del file sono le
parti del corpo di `:1036`-`:1060`, che non stanno in questo lotto).

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""
import io, json, sys

# chiave: (riga, inizio dell'inglese) — `:2156` porta DUE lang() sulla stessa riga
RESE = {
    # --- quante volte lo puoi ancora usare
    (1975, ' (Charges: '): '" (cariche: " + inv(INV_ITEM_CHARGE, itemname_itemid) + ")"',
    (1999, ' (Bullets: '): '" (colpi: " + inv(INV_ITEM_PARAM2, itemname_itemid) + ")"',
    (2002, ' (Remain: '):  '" (ancora " + inv(INV_ITEM_PARAM2, itemname_itemid) + "/5)"',
    (2151, ' ('):          '" (" + biten(inv(INV_ITEM_FISHING_BAIT, itemname_itemid)) + ", ancora " + inv(INV_ITEM_CHARGE, itemname_itemid) + ")"',

    # --- il globo oscuro verde: trappole d'ambiente
    (2006, ' (oil pot)'):          " (vaso d'olio)",
    (2009, ' (guillotine fall)'):  ' (ghigliottina)',
    (2012, ' (hammer pendulum)'):  ' (pendolo a martello)',
    (2015, ' (rock rain)'):        ' (pioggia di rocce)',
    (2018, ' (Mazin beam)'):       ' (raggio del demone)',
    # --- il globo oscuro blu
    (2023, ' (torabasami)'):       ' (tagliola)',
    (2026, ' (electric horse)'):   ' (tubo elettrico)',
    (2029, ' (electromagnetic)'):  ' (catapulta magnetica)',
    (2032, ' (gas floor)'):        ' (pavimento a gas)',
    (2035, ' (Mazin punch)'):      ' (pugno del demone)',
    # --- il globo oscuro cremisi
    (2040, ' (splash)'):           ' (spruzzo)',
    (2043, ' (flame Arrow)'):      ' (freccia di fiamma)',
    (2046, ' (impact wall)'):      " (muro d'urto)",
    (2049, ' (mega buzzsaw)'):     ' (megasega)',
    (2052, ' (Mazin fire)'):       ' (fuoco del demone)',
    # --- il globo oscuro bianco: sei lance
    (2057, ' (vibrating spear)'):  ' (lancia vibrante)',
    (2060, ' (poison spear)'):     ' (lancia velenosa)',
    (2063, ' (sleepy spear)'):     ' (lancia ipnotica)',
    (2066, ' (ink spear)'):        " (lancia d'inchiostro)",
    (2069, ' (smelly spear)'):     ' (lancia puzzolente)',
    (2072, ' (paralyze spear)'):   ' (lancia paralizzante)',

    # --- gli oggetti che cambiano forma
    (2077, ' (Model-'): '" (modo " + locvar_itemname_form + ")"',

    # --- la bara della negromanzia: otto creature, non otto etichette
    (2089, ' (cat)'):        ' (gatto zombi)',
    (2092, ' (zombie)'):     ' (zombi)',
    (2095, ' (mummy)'):      ' (mummia)',
    (2098, ' (skeleton)'):   ' (scheletro guerriero)',
    (2101, ' (lich)'):       ' (lich)',
    (2104, ' (doll)'):       ' (necrobambola)',
    (2107, ' (dragon)'):     ' (drago zombi)',
    (2110, ' (dead-eyes)'):  ' (occhi morti)',
    (2114, '-Deceive'):      '-inganno',

    # --- la sfera dei mostri e la serratura
    (2156, ' Lv. '):      ' Lv. ',
    (2156, ' (Empty)'):   ' (vuota)',
    (2166, ' Lock-Lv. '): ' serratura liv. ',

    # --- quel che si sa dell'oggetto senza saperne la benedizione
    (2175, '['): '"[" + cnven(mtname(0, inv(INV_ITEM_MATERIAL, itemname_itemid))) + "]"',
    (2178, ' (Scary)'):    ' (spavento)',
    (2181, ' (Dreadful)'): ' (malaugurio)',

    # --- contenitori e carichi
    (2187, ' (Temporal)'): ' (svanisce in viaggio)',
    (2192, ' (Empty)'):    ' (niente dentro)',
    (2199, '(Buying price: '): '"(prezzo: " + inv(INV_ITEM_PARAM2, itemname_itemid) + "g)"',

    # --- che cosa hanno messo dentro al cibo
    (2203, ' (Aphrodisiac)'): ' (afrodisiaco)',
    (2206, ' (Poisoned)'):    ' (veleno)',
    (2209, ' (Danger!)'):     ' (pericolo!)',
    (2213, ' (Herb)'):        ' (con erbe)',
    (2217, ' (Antiseptic)'):  ' (antisettico)',

    # --- il tempo che manca
    (2233, '(Next: '): '"(fra " + (inv(INV_ITEM_NEXT_PERIOD, itemname_itemid) - (gdata(GDATA_HOUR) + gdata(GDATA_DAY) * 24 + gdata(GDATA_MONTH) * 24 * 30 + gdata(GDATA_YEAR) * 24 * 30 * 12)) + " ore)"',
    (2237, ' (Need Sleep)'): ' (serve dormire)',

    # --- i numeri di serie
    (2243, ' Serial No.'):   ' n. serie ',
    (2248, ' Property No.'): ' immobile n. ',
}

LOTTO = 'lavoro/96-item_func-parentesi.jsonl'

voci = [json.loads(l) for l in io.open(LOTTO, encoding='utf-8') if l.strip()]


def chiave(v):
    trovate = [k for k in RESE if k[0] == v['riga'] and v['en'].startswith(k[1])]
    if len(trovate) != 1:
        return None
    return trovate[0]


mancanti = [(v['riga'], v['en']) for v in voci if chiave(v) is None]
usate = {chiave(v) for v in voci if chiave(v)}
in_piu = [k for k in RESE if k not in usate]
if mancanti or in_piu:
    print('mancanti: %s' % mancanti)
    print("in piu' : %s" % in_piu)
    sys.exit(1)

with io.open(LOTTO, 'w', encoding='utf-8', newline='\n') as fh:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        fh.write(json.dumps(v, ensure_ascii=False) + '\n')
print('%d rese scritte in %s' % (len(voci), LOTTO))
