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
