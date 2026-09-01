# -*- coding: utf-8 -*-
"""120a - Lotto 055 di `db_item.hsp`: I MINERALI, e la categoria CHIUDE.

`FILTER_ORE`, righe da `:48805` a `:128795`: **33 righe**, tutte dell'indice 0,
su 33 oggetti — la categoria intera in un lotto solo. Con questo lotto
`FILTER_ORE` va a **0 da fare su 33 vive**, ed e' la **decima** categoria del
corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 055`: **+33** per 33 rese,
nessuna gemella. ⓘ `_gia-reso.py 055`: 0 su 33. `_code.py 055`: 0 righe senza
resa in tabella.

### ⭐⭐⭐ TRE SERIE IN UN LOTTO SOLO, E LA PIU' LUNGA E' DI DODICI

E' la stessa forma della serie delle tre della sessione (le armi che nessun
uomo solleva), ma qui il lotto ne porta **tre**, ed e' la prova che la domanda
«questa riga ha delle sorelle?» va fatta a ogni lotto e non solo quando salta
all'occhio:

  - **le dodici pietre dei mesi** (`:48805`-`:49575`). Il giapponese le scrive
    identiche parola per parola e cambia **due** cose: il nome della pietra e
    il mese. Le dodici rese fanno lo stesso, con la stessa formula ripetuta;
  - **le tre pietre grezze** (`:128305` diamante, `:128375` smeraldo,
    `:128515` rubynus). Identiche, cambia la gemma;
  - **i tre cristalli degli elementi** (`:128655` sole/giallo, `:128725`
    mana/rosso, `:128795` terra/arancione). Identici nell'apertura — «un
    cristallo ◯ che si dice racchiuda la forza di ◯» — e due su tre
    condividono anche il seguito, 光に透かすと «guardandolo in controluce».
    ⓘ Il terzo (il mana) diverge nel giapponese, e la resa lo lascia divergere:
    non si uniforma cio' che l'originale distingue.

⚠️ La tentazione, in una serie, e' variare per non sembrare svista: e'
l'opposto. La ripetizione **e' il testo** — dodici gemme che il giocatore
incontra a mesi di distanza si riconoscono per la formula, non malgrado.

### ⭐⭐ E LA SERIE FA VEDERE UNA DISTINZIONE CHE L'INGLESE NON HA

Nelle dodici pietre il giapponese usa **due nomi diversi** per la stessa
pietra: il nome dell'oggetto e' in **katakana** (ガーネット, サードニクス,
アレキサンドライト), la descrizione usa il nome **nostrano o mineralogico**
(ザクロ石, メノウ, 金緑石). L'inglese scrive due volte la stessa parola.

In italiano le due coincidono quasi sempre — granato, ametista, rubino — e li'
non c'e' niente da conservare. Ma in **due** casi la coppia esiste davvero, e
la resa la tiene:

    :49295  l'oggetto e' la sardonice   -> la descrizione dice «un'agata»
    :49155  l'oggetto e' l'alessandrite -> la descrizione dice «un crisoberillo»

Sono le due famiglie di cui quelle pietre sono varieta', ed e' esattamente cio'
che il giapponese fa. ⓘ Il giocatore vede «M08-Sardonice» e legge «un'agata
lavorata ad arte»: e' quello che legge anche il giocatore giapponese.

### ⚠️⚠️⚠️ LA QUINTA VOLTA CHE L'INGLESE RICOPIA LA RIGA GEMELLA

`:69118`, la **tavoletta di smeraldo**. Il giapponese dice
錬金術の基本思想を記したエメラルドの碑文 — «l'iscrizione su smeraldo che riporta
il pensiero fondamentale dell'alchimia», cioe' la Tavola Smeraldina. L'inglese
ci scrive **parola per parola la frase del rubynus e del diamante**: «Large
emerald are cut from collected gemstones that have been fused together through
alchemy...».

⚠️ Qui il guasto e' piu' grosso dei quattro della 119a, perche' la riga copiata
**non ha senso** sull'oggetto: una tavoletta incisa non e' una gemma tagliata,
e chi rendesse dall'inglese scriverebbe che l'iscrizione e' un brillante.
⭐ E a confermarlo non serve solo il giapponese: l'**indice 3**, gia' reso e
chiuso da sessioni, dice «Una tavoletta fatta di smeraldo», e i due indici il
pannello li disegna uno sotto l'altro.

ⓘ Sono cinque casi in due sessioni, e la forma e' sempre quella descritta in
`wiki/concepts/l-intermedio-ricopia-la-riga-gemella.md`: due righe gemelle per
costruzione, e monte ricopia l'una nell'altra. Qui le sorelle sono **tre**
(rubynus, diamante, tavoletta) e la copiata e' l'unica delle tre che non e' una
gemma.

### ⓘ Una coda che l'inglese sbaglia, e che lo strumento raddrizza da solo

`:52313`, la pietra del drago rosso: il giapponese chiude con
～ザイール鉱物図鑑～, l'atlante di **Zaile**, e l'inglese scrive «~Vernis Ore
Catalogue~». `_code.py` assegna la coda passando dal **giapponese** e scrive
«Atlante dei Minerali di Zaile»: il settimo posto dove guardare (la tabella dei
titoli) ha fatto il suo lavoro senza che nessuno dovesse accorgersene.

### ⚠️ UNA COSA CHE QUESTO LOTTO NON PUO' RIPARARE, E VA ANNOTATA

I **nomi** delle dodici pietre portano in giapponese un **epiteto** che
l'italiano non ha, perche' l'italiano ha seguito l'inglese:

    M01-真実のガーネット      «Granato della verita'»   -> M01-Granato gioiello
    M02-高貴のアメジスト      «Ametista della nobilta'» -> M02-Ametista gioiello
    M03-聡明のアクアマリン    «Acquamarina della sagacia»
    M04-無垢のダイヤモンド    «Diamante della purezza»
    M05-誠実のエメラルド      «Smeraldo della sincerita'»
    M06-情熱のアレキサンドライト «Alessandrite della passione»
    M07-威厳のルビー          «Rubino della dignita'»
    M08-円満のサードニクス    «Sardonice dell'armonia»
    M09-慈愛のサファイア      «Zaffiro dell'affetto»
    M10-希望のオパール        «Opale della speranza»
    M11-友情のトパーズ        «Topazio dell'amicizia»
    M12-成功のラピスラズリ    «Lapislazzuli del successo»

L'inglese scrive «jewel» dove il giapponese mette la virtu', su **dodici righe
su dodici**. Non e' materia di questo lotto — i nomi non sono il corpo — ma e'
la stessa forma delle due questioni aperte dalla 118a sui grimori: una
distinzione che il giapponese fa sistematicamente e che il giocatore italiano
oggi non legge. Va **decisa**, non ereditata.
"""
import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :48805
    (48805, 'Artfully processed garnet, this gemstone represents the month of January and would make a particularly nice gift for someone whose anniversary is in January. \\n#~Vernis Ore Catalogue~'):
        "Un granato lavorato ad arte. È la pietra che rappresenta gennaio, e regalarla a chi ha una ricorrenza in gennaio farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :48875
    (48875, 'Artfully processed amethyst, this gemstone represents the month of Febuary and would make a particularly nice gift for someone whose anniversary is in Febuary. \\n#~Vernis Ore Catalogue~'):
        "Un'ametista lavorata ad arte. È la pietra che rappresenta febbraio, e regalarla a chi ha una ricorrenza in febbraio farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :48945
    (48945, 'Artfully processed aquamarine, this gemstone represents the month of March and would make a particularly nice gift for someone whose anniversary is in March. \\n#~Vernis Ore Catalogue~'):
        "Un'acquamarina lavorata ad arte. È la pietra che rappresenta marzo, e regalarla a chi ha una ricorrenza in marzo farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49015
    (49015, 'Artfully processed diamond, this gemstone represents the month of April and would make a particularly nice gift for someone whose anniversary is in April. \\n#~Vernis Ore Catalogue~'):
        "Un diamante lavorato ad arte. È la pietra che rappresenta aprile, e regalarlo a chi ha una ricorrenza in aprile farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49085
    (49085, 'Artfully processed emerald, this gemstone represents the month of May and would make a particularly nice gift for someone whose anniversary is in May. \\n#~Vernis Ore Catalogue~'):
        "Uno smeraldo lavorato ad arte. È la pietra che rappresenta maggio, e regalarlo a chi ha una ricorrenza in maggio farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49155
    (49155, 'Artfully processed Alexandrite, this gemstone represents the month of June and would make a particularly nice gift for someone whose anniversary is in June. \\n#~Vernis Ore Catalogue~'):
        "Un crisoberillo lavorato ad arte. È la pietra che rappresenta giugno, e regalarlo a chi ha una ricorrenza in giugno farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49225
    (49225, 'Artfully processed ruby, this gemstone represents the month of July and would make a particularly nice gift for someone whose anniversary is in July. \\n#~Vernis Ore Catalogue~'):
        "Un rubino lavorato ad arte. È la pietra che rappresenta luglio, e regalarlo a chi ha una ricorrenza in luglio farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49295
    (49295, 'Artfully processed sardonyx, this gemstone represents the month of August and would make a particularly nice gift for someone whose anniversary is in August. \\n#~Vernis Ore Catalogue~'):
        "Un'agata lavorata ad arte. È la pietra che rappresenta agosto, e regalarla a chi ha una ricorrenza in agosto farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49365
    (49365, 'Artfully processed sapphire, this gemstone represents the month of September and would make a particularly nice gift for someone whose anniversary is in September. \\n#~Vernis Ore Catalogue~'):
        "Uno zaffiro lavorato ad arte. È la pietra che rappresenta settembre, e regalarlo a chi ha una ricorrenza in settembre farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49435
    (49435, 'Artfully processed opal, this gemstone represents the month of October and would make a particularly nice gift for someone whose anniversary is in October. \\n#~Vernis Ore Catalogue~'):
        "Un opale lavorato ad arte. È la pietra che rappresenta ottobre, e regalarlo a chi ha una ricorrenza in ottobre farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49505
    (49505, 'Artfully processed topaz, this gemstone represents the month of November and would make a particularly nice gift for someone whose anniversary is in November. \\n#~Vernis Ore Catalogue~'):
        "Un topazio lavorato ad arte. È la pietra che rappresenta novembre, e regalarlo a chi ha una ricorrenza in novembre farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49575
    (49575, 'Artfully processed lapis lazuli, this gemstone represents the month of December and would make a particularly nice gift for someone whose anniversary is in December. \\n#~Vernis Ore Catalogue~'):
        "Un lapislazzuli lavorato ad arte. È la pietra che rappresenta dicembre, e regalarlo a chi ha una ricorrenza in dicembre farà un piacere particolare. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :49708
    (49708, 'Golden statue. It is a very realistic sculpture, as if the real thing were turned directly into gold. \\n# ~Lumiest Art Catalogue~'):
        "Una statua che luccica d'oro. È modellata in modo straordinariamente vivo, come se una persona vera fosse stata mutata in oro così com'era. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :52170
    (52170, 'Beautiful skeleton formed by coralline worms. It is calcareous and hard, but can be eaten up or swallowed whole by stronger fish. \\n# ~Lumiest Art Catalogue~'):
        "Il bello scheletro che formano i polipi del corallo. È calcareo e duro, eppure i pesci robusti se lo sgranocchiano o se lo inghiottono intero. \\n# ~Catalogo d'Arte di Lumiest~",

    # ---------------------------------------------------------- :52313
    (52313, 'Reddish in color, this ore is softer than iron as it is, but once heated and processed, it turns silver in color and becomes remarkably hard. \\n#~Vernis Ore Catalogue~'):
        "Questo minerale, che tende al rosso, così com'è è più tenero del ferro; ma una volta scaldato e lavorato il colore vira all'argento e diventa duro da stupire. \\n#~Atlante dei Minerali di Zaile~",

    # ---------------------------------------------------------- :66137
    (66137, 'Teardrop-shaped jewel crystallized from a drop of divine power. It has the same kind of power as an artifact, albeit in a smaller quantity. It appears unexpectedly when the power of the gods is temporarily increased, and it is said to be difficult to produce it when you want it to appear. \\n# ~Irva Fantasy Encyclopedia~'):
        "Una gemma a forma di goccia, nata dal cristallizzarsi di una stilla di forza divina. Per quanto poca, dentro nasconde la stessa forza di un artefatto. Viene fuori così, senza preavviso, quando la forza di un dio cresce per un momento; e al contrario, volerla far uscire pare sia difficile. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :66199
    (66199, 'Fragments of divine power, the core of Nefia that forms the labyrinth and empowers its guardians. Almost all of its hidden power has already been used, and it is virtually a husk. However, since there is usually nothing left over after the birth of Nefia, it has a high scarcity value. It is traded at a high price, partly because the residue of divine power remains in the form of enchantments. \\n# ~Irva Fantasy Encyclopedia~'):
        "Un frammento di forza divina, e insieme il nucleo che forma il labirinto e dà potere ai suoi guardiani. La forza che vi era nascosta è stata ormai spesa quasi tutta, e di fatto è un residuo. Ma siccome di norma dopo la nascita di una Nefia non ne resta nessuno, è raro e per questo prezioso. Si scambia a caro prezzo anche perché quel che avanza della forza divina resta lì sotto forma di incantamento. \\n# ~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :69048
    (69048, 'Large rubynus are cut from collected gemstones that have been fused together through alchemy. Even though each rough stone is not worth polishing, if they are gathered together and polished, they will shine as splendid gems. \\n#~Vernis Ore Catalogue~'):
        "Un rubynus di gran misura, tagliato dopo aver fuso con l'alchimia i grezzi messi insieme. Anche se preso uno per uno nessuno di quei grezzi varrebbe la fatica di lucidarlo, a raccoglierli e lavorarli l'uno con l'altro ne esce una gemma di tutto rispetto, che brilla. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :69118
    (69118, 'Large emerald are cut from collected gemstones that have been fused together through alchemy. Even though each rough stone is not worth polishing, if they are gathered together and polished, they will shine as splendid gems. \\n#~Vernis Ore Catalogue~'):
        "Un'iscrizione su smeraldo, dove è riportato il pensiero fondamentale dell'alchimia. È roba per chi va matto per l'alchimia, ma vale molto anche come opera d'arte. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :69188
    (69188, 'Large diamond are cut from collected gemstones that have been fused together through alchemy. Even though each rough stone is not worth polishing, if they are gathered together and polished, they will shine as splendid gems. \\n#~Vernis Ore Catalogue~'):
        "Un diamante di gran misura, tagliato dopo aver fuso con l'alchimia i grezzi messi insieme. Per grandezza e per bellezza è perfetto, e gli si dà un prezzo che supera perfino quello di un artefatto. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :82213
    (82213, "A priceless piece of paper. It has the word 'friendship' crudely written on it. \\n#~Thousands of pieces of Junk I love~"):
        "Un pezzo di carta che si dice valga più di quanto il denaro possa comprare. Sopra c'è scritto \\\"amicizia\\\", con una grafia che pare il tracciato di un lombrico. \\n#~Le Mille Cianfrusaglie che Amo~",

    # ---------------------------------------------------------- :82610
    (82610, "Mystery ticket with several instruments drawn on it. It contains the performer's dream and the audience's appreciation. \\n# ~Music of the Melodious Irva~"):
        "Un biglietto misterioso, con disegnati sopra alcuni strumenti. Dentro ci stanno il sogno di chi suona e la riconoscenza di chi ascolta. \\n# ~Le Melodie della Limpida Irva~",

    # ---------------------------------------------------------- :89419
    (89419, 'A small coin believed to have been used in ancient times. They are not in circulation because they have only academic value, but many collectors are said to have especially collected them because of their rarity. \\n# ~Coins of this World - Tyris Edition~'):
        "Una monetina che si dice fosse in uso nell'antichità. Non circola più, perché ha ormai solo un valore di studio, ma pare che proprio per quanto è rara siano in molti i collezionisti che se ne occupano. \\n# ~Le Monete del Mondo: Tyris~",

    # ---------------------------------------------------------- :117318
    (117318, "It is a sinful mineral that, when appraised, leaves one in dismay. It shines so brightly that it seems almost deliberate, and is given mainly to children or to those who don't understand its value, as a token of appreciation. \\n#~Cheap Gifts for Your Kids~"):
        "Un minerale che fa peccato: a farlo esaminare non si può che restarci male. Brilla in un modo così plateale da parere apposta, e lo si regala soprattutto ai bambini, o a chi non ne capisce il valore, per dire grazie. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :128173
    (128173, 'Stones that have no scarcity value. There are plenty of them lying around, but it seems that many children collect them. \\n#~Cheap Gifts for Your Kids~'):
        "Un pezzo di pietra che di raro non ha proprio niente. Ce n'è quante se ne vuole in giro, eppure pare che di bambini che le raccolgono ce ne siano parecchi. \\n#~Cento Modi per Fregare i Bambini: i Souvenir~",

    # ---------------------------------------------------------- :128305
    (128305, 'A rare mineral that contains many elements of diamond. Through the process of processing, its size becomes extremely small, so it is not considered to be so valuable in relation to the size of the gemstone. \\n#~Vernis Ore Catalogue~'):
        "Un minerale raro, che contiene molto degli elementi del diamante. Nella lavorazione la sua misura si riduce all'estremo, e per questo si dice che non valga poi molto rispetto a quanto è grosso da grezzo. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128375
    (128375, 'A rare mineral that contains many elements of emerald. Through the process of processing, its size becomes extremely small, so it is not considered to be so valuable in relation to the size of the gemstone. \\n#~Vernis Ore Catalogue~'):
        "Un minerale raro, che contiene molto degli elementi dello smeraldo. Nella lavorazione la sua misura si riduce all'estremo, e per questo si dice che non valga poi molto rispetto a quanto è grosso da grezzo. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128445
    (128445, 'Small white minerals that emit a pale light. It is so beautiful that it is described as a pearl of stone, as it slowly builds up an almost elliptical sphere over time. \\n#~Vernis Ore Catalogue~'):
        "Un minerale piccolo e bianco, che manda una luce tenue. Attraverso ere e ere costruisce con calma una sfera quasi ovale, e a vederlo così è tanto bello che lo chiamano la perla di pietra. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128515
    (128515, 'A rare mineral that contains many elements of rubynus. Through the process of processing, its size becomes extremely small, so it is not considered to be so valuable in relation to the size of the gemstone. \\n#~Vernis Ore Catalogue~'):
        "Un minerale raro, che contiene molto degli elementi del rubynus. Nella lavorazione la sua misura si riduce all'estremo, e per questo si dice che non valga poi molto rispetto a quanto è grosso da grezzo. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128585
    (128585, 'A brilliant mineral that never rusts. It is very easy to process, and its unique bright color has been favored by powerful people as a symbol of wealth and power since ancient times. Because of its mysterious nature, it is often the subject of research. \\n#~Vernis Ore Catalogue~'):
        "Un minerale splendente, che non arrugginisce mai. È facilissimo da lavorare, e quel suo colore chiaro e inconfondibile è caro fin dall'antichità a chi ha il potere, come segno di ricchezza e di forza. Pare che per quel suo che di misterioso finisca spesso sotto studio. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128655
    (128655, 'This yellow crystal is said to contain the power of the sun. When you look through the light, you can see a faint atmospheric undulation-like movement in the mineral. \\n#~Vernis Ore Catalogue~'):
        "Un cristallo giallo, che si dice racchiuda la forza del sole. Guardandolo in controluce, dentro il minerale si scorge appena un movimento come di aria che ondeggia. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128725
    (128725, 'A red crystal that is said to contain magical power. The mineral itself is as transparent as pure magic power. It is said that in an emergency, a mage would crush it and put it in his body. \\n#~Vernis Ore Catalogue~'):
        "Un cristallo rosso, che si dice racchiuda la forza magica. Il minerale in sé è trasparente quanto il mana puro. Si racconta che nei momenti critici i maghi lo frantumino per accoglierlo nel proprio corpo. \\n#~Atlante dei Minerali di Vernis~",

    # ---------------------------------------------------------- :128795
    (128795, 'This orange crystal is said to contain the power of the earth. When you look through the light, the reflection from the many cracks inside the crystal is very beautiful. \\n#~Vernis Ore Catalogue~'):
        "Un cristallo arancione, che si dice racchiuda la forza della terra. Guardandolo in controluce, la luce si riflette sulle molte crepe che lo percorrono dentro, ed è bellissimo. \\n#~Atlante dei Minerali di Vernis~",

# 33 voci, 0 ambigue
}
# rete 5: l'accento deve essere PRECOMPOSTO. Vedi il lotto 005.
RESE = {chiave: unicodedata.normalize('NFC', resa) for chiave, resa in RESE.items()}

RINVIATE = set()

USCITA = 'lavoro/fase5-db_item-055.jsonl'
RIGHE = {
    48805, 48875, 48945, 49015, 49085, 49155, 49225, 49295, 49365, 49435,
    49505, 49575, 49708, 52170, 52313, 66137, 66199, 69048, 69118, 69188,
    82213, 82610, 89419, 117318, 128173, 128305, 128375, 128445, 128515, 128585,
    128655, 128725, 128795,
}
SORGENTE = r'C:\\Games\\Elona\\_traduzione\\sorgente\\2.05-custom-gx\\db_item.hsp'

tutte = [json.loads(l) for l in io.open('lavoro/_107-daitem.jsonl', encoding='utf-8') if l.strip()]
zona = [v for v in tutte if v['riga'] in RIGHE]
# rete 0: la chiave di un lotto e' `(riga, en)`, e **non e' univoca**.
#
# Due `lang()` diverse sulla stessa riga possono avere lo stesso inglese: se il
# giapponese distingue e l'inglese no, la chiave corta identifica due voci. Fino
# alla 41a la rete si limitava a fermare la zona, che era giusto — meglio fermarsi
# che scrivere la resa sulla voce sbagliata — ma lasciava il lotto senza strada:
# `ai.hsp:4576` fu scritto a mano, indicizzato per `firma`, perche' 「変身！」 e
# 「トランスフォーム！」 sono tutt'e due `cnvtalk("Transform!")`.
#
# Poi `init.hsp` ne ha portate tre in un file solo — `:358` («Great museum» per
# 大人気の博物館 e per 来客の絶えない博物館), `:2225` (lo spazio per 年 e per 日),
# `:2235` (i due punti per 時間 e per 分) — e la strada a mano non regge piu'.
#
# ✅ Adesso la voce ambigua si dichiara con la **chiave lunga** `(riga, en, jp)`,
# che e' univoca perche' e' il giapponese a distinguere. La `firma` lo sarebbe
# altrettanto, ma e' un sha1: illeggibile in un file che si rilegge a mano.
# Le voci non ambigue tengono la chiave corta, quindi i lotti gia' scritti
# valgono tal quale.
AMBIGUE = {k for k, n in collections.Counter((v['riga'], v['en']) for v in zona).items() if n > 1}


def chiave(v) -> tuple:
    corta = (v['riga'], v['en'])
    return (v['riga'], v['en'], v['jp']) if corta in AMBIGUE else corta


voci = [v for v in zona if chiave(v) not in RINVIATE]

errori = []
for k in sorted(AMBIGUE):
    print(f'💡 rete 0: la chiave {k} identifica piu\' di una voce: '
          f'vanno date con la chiave lunga (riga, en, jp)')
indice = {chiave(v): v for v in voci}
for v in voci:
    if chiave(v) not in RESE:
        errori.append(f"rete 1: voce senza resa -> chiave {chiave(v)!r}")
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')
for k in RINVIATE:
    if k not in {chiave(v) for v in zona}:
        errori.append(f'rete 2-bis: rinviata che non aggancia nessuna voce -> {k}')

# ⚠️ E il controllo di rete 1 va PRIMA delle altre reti, non dopo: la rete 8
# dereferenzia `RESE` e, se una resa manca, quel che esce e' un `KeyError` nudo
# invece del messaggio della rete 1. Difetto noto dalla 38a (`proc.hsp:23654`),
# corretto qui.
if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

sorgente = io.open(SORGENTE, encoding='cp932').read().split('\n')

# rete 6: righe spente, col `;` (lotto 006), col `//` (100a) o dentro un
# blocco (lotto 014).
# ⚠️⚠️ **Si guarda la FIRMA, non la riga** (45a): `estrai --da-tradurre` ancora
# la voce alla PRIMA occorrenza, che puo' essere spenta mentre le altre sono
# vive. `command.hsp:17285` sta nel blocco ORIGINAL che il mod ha spento e
# rivive a `:17316`, dentro il blocco messo al suo posto: rinviarla avrebbe
# lasciato inglese un menu che il giocatore apre a ogni uscita dal gioco.
# Misurato prima di toccare la rete: 36 firme toccano un blocco spento, **28
# sono spente del tutto** — e li' la rete aveva ragione — **8 sono miste**, e
# sette di quelle hanno l'ancora nella riga morta.
# ⚠️ Lo strumento, non lo scratch: `strumenti/commenti.py` e' la stessa funzione
# di `scratchpad/commenti-blocco.py` ma con dei test, e dalla 100a sa anche del
# commento di riga `//`.
from strumenti import commenti as _cb
SPENTE = _cb.righe_in_commento(SORGENTE)

from pathlib import Path as _Path
from strumenti import estrai as _estrai

_righe_per_firma = collections.defaultdict(list)
for _v in _estrai.estrai_da_file(_Path(SORGENTE)):
    _righe_per_firma[_v['firma']].append(_v['riga'])


def _e_spenta(riga: int) -> bool:
    testo = sorgente[riga - 1]
    return (testo.lstrip().startswith(';')
            or _cb.lang_spenta_da_barre(testo)
            or riga in SPENTE)


for v in voci:
    _righe = _righe_per_firma.get(v['firma']) or [v['riga']]
    if all(_e_spenta(r) for r in _righe):
        _testa = sorgente[_righe[0] - 1]
        if _testa.lstrip().startswith(';'):
            _come = "e' commentata nel sorgente"
        elif _cb.lang_spenta_da_barre(_testa):
            _come = "e' spenta da un commento `//`"
        else:
            _come = 'sta dentro un commento di BLOCCO'
        errori.append(f"rete 6: riga {v['riga']} {_come}, va rinviata")
    elif _e_spenta(v['riga']):
        _vive = [r for r in _righe if not _e_spenta(r)]
        print(f"\U0001f4a1 rete 6: la riga {v['riga']} e' spenta, ma la stessa firma vive "
              f"a {_vive}: si traduce")

# rete 7: una voce dentro un CONFRONTO non e' testo (lotto 007).
for v in voci:
    testa = sorgente[v['riga'] - 1].split('lang(')[0]
    if '==' in testa or '!=' in testa:
        errori.append(f"rete 7: riga {v['riga']} e' un confronto, non un testo: va rinviata")

# rete 8: niente preposizione che si fonde davanti a un nome (lotto 009).
# `valn` solo se NON viene da uno `skillname` (lotto 014).
FONDONO = re.compile(r'\b(a|di|da|in|su)\s*"\s*\+\s*(name|itemname|valn|cdatan)\b')
ASSEGNA_VALN = re.compile(r'^\s*valn\s*=\s*([A-Za-z_][A-Za-z0-9_]*)\s*\(')


def valn_viene_da(riga: int) -> str:
    for i in range(riga - 1, max(0, riga - 60), -1):
        trovato = ASSEGNA_VALN.match(sorgente[i - 1])
        if trovato:
            return trovato.group(1)
    return '?'


for v in voci:
    resa = RESE[chiave(v)]
    for _, nome in FONDONO.findall(resa):
        if nome == 'valn' and valn_viene_da(v['riga']) == 'skillname':
            continue
        errori.append(f"rete 8: riga {v['riga']} ha una preposizione che si fonde "
                      f"davanti a {nome} -> {resa}")

# rete 9: una TESTA di frase (l'inglese finisce in « and») deve chiudersi col
# connettivo (lotto 010).
#
# ⚠️ E la testa finisce in « and» SENZA spazio in coda: lo `.rstrip()` che stava
# qui cancellava proprio la differenza fra una testa e una congiunzione infissa,
# ed e' la stessa specie di errore della rete 8 nella 37a — la rete boccia una
# resa giusta perche' guarda male, non perche' la resa sbagli.
# `command.hsp:13` compone la lista degli oggetti sulla casella con
# `lang("と", " and ")`, spazio davanti e dietro, e la rete pretendeva che « e »
# finisse col connettivo, che e' l'unica cosa che quella resa contiene.
# ✅ Misurato sul dizionario intero: le teste vere sono **29** e finiscono tutte
# in « and» esatto (`action.hsp:4866`, «name(cc) + " calcia via " + name(tc) + " e"»);
# l'unica voce che finisce in « and » con lo spazio e' `text.hsp:11685`, che e'
# una congiunzione infissa come questa. La distinzione la impone il sorgente.
TESTA = re.compile(r'\se"$')
for v in voci:
    if v['en'].endswith(' and'):
        resa = RESE[chiave(v)].rstrip()
        if not TESTA.search(resa):
            errori.append(f"rete 9: riga {v['riga']} e' una testa di frase ma non "
                          f"finisce con ' e' -> {resa}")

# rete 10: `his(x, 1)` regge un nome maschile singolare (lotto 011).
POSSESSIVO = re.compile(r'\b(his|he|him)\s*\([^)]*,[^)]*\)\s*\+\s*"\s*([A-Za-zÀ-ÿ\']+)')
accanto = []
for v in voci:
    for _, nome in POSSESSIVO.findall(RESE[chiave(v)]):
        accanto.append((v['riga'], nome))

# rete 12: la resa di una DINAMICA e' un'espressione HSP, non testo nudo
# (lotto 014: l'ha trovata il compilatore).
for v in voci:
    if v['tipo'] == 'dinamica' and '"' not in RESE[chiave(v)]:
        errori.append(f"rete 12: riga {v['riga']} e' una dinamica ma la resa e' testo "
                      f"nudo: va scritta come espressione, fra virgolette")

# rete 11: le funzioni di CONTENUTO devono coincidere (verifica.py:367).
try:
    from strumenti.funzioni import funzioni_di_contenuto
except ImportError:
    funzioni_di_contenuto = None
if funzioni_di_contenuto is not None:
    for v in voci:
        if v['tipo'] != 'dinamica':
            continue
        attese = funzioni_di_contenuto(v['en_grezzo'])
        trovate = funzioni_di_contenuto(RESE[chiave(v)])
        if attese != trovate:
            di_troppo = [f for f in trovate if f not in attese]
            mancanti = [f for f in attese if f not in trovate]
            dettaglio = []
            if di_troppo:
                dettaglio.append(f'di troppo {di_troppo}')
            if mancanti:
                dettaglio.append(f'mancanti {mancanti}')
            if not dettaglio:
                dettaglio.append(f'ordine diverso: attese {attese}, trovate {trovate}')
            errori.append(f"rete 11: riga {v['riga']} — {'; '.join(dettaglio)}")

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti')

# Il confronto fra due rese e' sui LETTERALI, non sull'espressione (lotto 011
# per la rete 4, lotto 014 per la rete 3).
LETTERALI = re.compile(r'"((?:[^"\\]|\\.)*)"')


def parole(resa: str) -> tuple:
    if '"' not in resa:
        return (resa,)
    return tuple(LETTERALI.findall(resa))


gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))
for v in voci:
    resa = RESE[chiave(v)]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it == resa:
            continue
        if parole(it) == parole(resa):
            print(f"💡 rete 3: riga {v['riga']} dice le stesse parole di {nome}:{riga} "
                  f'su variabili diverse: e\' la stessa resa')
            continue
        print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
              f"      qui      {resa!r}\n"
              f"      {nome}:{riga}  {it!r}")


# rete 4: lo stesso giapponese non puo' avere due rese diverse DENTRO il lotto.
# Raggruppata per (giapponese, funzioni di contenuto): vedi il lotto 015.
#
# ⚠️⚠️ **Corretta nella 57a, ed e' la QUINTA rete che si corregge** dopo la 8, la
# 4 (una prima volta), la 9 e la 6. Le mancava l'INGLESE nella chiave.
# `main.hsp:4151` e `:4232` hanno lo stesso giapponese — 「あなたは「」とコメント
# した。」, cioe' «hai commentato "X"» — e lo stesso `cnvtalk`, ma l'inglese di
# monte ci mette il nome del boss: «Upon killing Meshera Alpha, you said,» e
# «Upon killing Enthumesis, you said,». Sono i due finali di Tyris del Sud, e le
# rese DEVONO differire.
#
# La rete raggruppava per `(giapponese, funzioni)` perche' la 37a le aveva
# insegnato che la rete 11 pretende le funzioni dell'inglese: due giapponesi
# uguali con un numero diverso di `name()` non possono coincidere. Ma le
# **parole** dell'inglese non erano nella chiave, e upstream distingue anche con
# quelle. Il risultato era che la rete fermava una resa giusta senza lasciare
# strada — la stessa forma del difetto che la 45a aveva trovato nella rete 6.
#
# ✅ Adesso la chiave e' `(giapponese, funzioni, inglese)`. La rete perde zero
# potere sul caso per cui e' nata — i due Yerleswood del lotto 039 hanno lo
# stesso giapponese **e** lo stesso inglese, e restano bocciati — e smette di
# bocciare le distinzioni che non sono nostre. ⚠️ La rete 3 continua a segnalarle
# come referto, perche' li' il confronto e' su tutto il dizionario ed e' giusto
# che un umano le guardi.
def firma_di(v) -> tuple:
    if funzioni_di_contenuto is None or v['tipo'] != 'dinamica':
        return ()
    return tuple(funzioni_di_contenuto(v['en_grezzo']))


per_jp = collections.defaultdict(set)
firme_per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[(v['jp'], firma_di(v), v['en'])].add(parole(RESE[chiave(v)]))
    firme_per_jp[v['jp']].add(firma_di(v))
for (jp, firma, _en), rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} con firma {firma} reso in {len(rese)} modi: {rese}')
for jp, firme in firme_per_jp.items():
    if len(firme) > 1:
        print(f'💡 rete 4: {jp!r} ha {len(firme)} firme diverse di monte {sorted(firme)}: '
              f'le rese non possono coincidere, e non e\' una scelta')

# rete 13: due voci con lo STESSO INGLESE e un giapponese diverso sono un errore
# di monte finche' non si guarda: l'inglese ha appiattito una distinzione che il
# giapponese fa. ⚠️ Nata nella 37a da `:14521`/`:14573`. Referto da leggere.
per_en = collections.defaultdict(set)
for v in voci:
    per_en[v['en']].add(v['jp'])
for en, giapponesi in sorted(per_en.items()):
    if len(giapponesi) > 1:
        print(f'💡 rete 13: l\'inglese {en!r} sta per {len(giapponesi)} giapponesi diversi '
              f'{sorted(giapponesi)}: guarda se la distinzione va tenuta')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')
print(f'{len(voci)} voci scritte in {USCITA} ({len(RINVIATE)} rinviate)')
for riga, nome in accanto:
    print(f'rete 10: riga {riga} — his(x, 1) regge «{nome}»: dev\'essere maschile singolare')
