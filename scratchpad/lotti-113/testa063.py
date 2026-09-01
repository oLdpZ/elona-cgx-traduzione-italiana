# -*- coding: utf-8 -*-
"""122a - Lotto 063 di `db_item.hsp`: GLI ELMI E I CAPPELLI, e la categoria CHIUDE.

`FILTER_HELM`, righe da `:43044` a `:130909`: **16 righe** — 15 dell'indice 0 e
**una dell'indice 2** (`:66979`, il verso dell'alieno) — su 15 oggetti. Con
questo lotto `FILTER_HELM` va a **0 da fare su 16 vive**, ed e' la
**diciottesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 063`: **+16** per 16 rese,
nessuna gemella. ⓘ `_gia-reso.py 063`: 0 su 16. `_code.py 063`: 0 righe senza
resa in tabella. `_forma.py 063`: 16 su 16 con lo spazio prima del `\\n`.

### ⭐⭐⭐ DUE FAMIGLIE ATTRAVERSANO ALTRI LOTTI, E STAVOLTA SI SONO CERCATE

Il lotto 060 aveva trovato la riga sorella nel lotto di un'ora prima **per
fortuna**, perche' le rese erano ancora sotto gli occhi. Qui la fortuna non
c'era — i lotti 058 e 060 sono di ieri sera — e le due famiglie sono uscite
solo perche' `_cerca.py` e' stato lanciato **prima** di scrivere, sulla prima
frase di ogni riga.

**La famiglia dei materiali, terza occorrenza:**

    :100849 (058)  特殊な素材をかけ合わせてより強固な防護を得た盾。
    :101769 (060)  特殊な素材をかけ合わせてより強固な防護を得た鎧。
    :99872  (063)  特殊な素材をかけ合わせてより強固な防護を得た兜。   <- questa

Le tre aperture italiane sono la stessa frase, cambia il nome del pezzo: «Uno
scudo / Una corazza / Un elmo che, incrociando materiali speciali, ha ottenuto
una protezione più solida.»

**La famiglia del segreto, tre righe in DUE categorie diverse:**

`:43044` e `:43112` (le due parrucche) aprono e chiudono con le stesse due
frasi, e le stesse due frasi stanno gia' in gioco su un **terzo** oggetto —
l'oggetto d'infiltrazione, un'altra categoria, reso in una sessione passata.
Sono state **copiate dal dizionario**, non riscritte:

    «Lo sviluppò un'organizzazione segreta che un tempo puntava alla conquista
     del mondo.»
    «Oggi ne restano sì e no i pochi esemplari dissotterrati e rimessi in sesto
     da qualche artigiano.»

⚠️ **Nessuno strumento del lotto poteva dirlo**: `_gia-reso` cerca la prosa
intera e dice 0 su 16, `_120-serie-bacchette` raggruppa dentro il lotto,
`_coerenza` fa lo stesso, e `_122-inglese-doppio-item` guarda l'inglese, non il
giapponese. ⭐ **Lo strumento che manca resta quello**: la ricerca della riga
sorella per **frase** — non per prosa intera — su tutto `db_item.hsp`. E' la
richiesta della 121a, e questo lotto e' la seconda prova che serve.

### ⭐ Le due righe che il giapponese costruisce sulla ripetizione

  - `:66977`, la testa dell'alieno di Sunbararia, accumula **tre** esitazioni
    di fila e chiude con はず — たぶん完全に死んでいるので、おそらく被っても
    きっと大丈夫なはず. La battuta sta nel mucchio, non in una parola: la resa
    tiene «Probabilmente… quasi di sicuro… non dovrebbe… si spera»;
  - `:130909`, il cappello magico, dice 何となく賢くなった気分 — un vago senso
    di essere piu' saggi. Togliere quel «vago» toglierebbe la riga.

### ⓘ Le decisioni minori, e da dove vengono

  - スンバラリア星人 «l'alieno di Sunbararia», 吟遊詩人 «menestrello»,
    定命 «mortale», 変異 «mutazione», 防弾チョッキ «giubbotto antiproiettile»
    (quest'ultimo dal lotto 060): tutti dal dizionario;
  - 幸運の神 (`:76181`) e' **Ehekatl**, e in gioco il suo epiteto e' «Ehekatl
    della Sorte»: la riga dice «la dea della sorte», non «della fortuna»,
    perche' e' la parola che il giocatore ha gia' letto. Il genere femminile
    viene dal gioco, dove Ehekatl parla al femminile («Mi hai chiamata?»);
  - `:66979` e' un **verso**, non una frase: monte lo lascia identico in tutt'e
    tre le lingue. Solo il titolo-fonte si traduce, e viene da `_code.py`;
  - le descrizioni lunghe usano le parole dell'**indice 3 gia' in gioco** degli
    stessi oggetti — «Un'armatura per proteggere la testa», «Un elmo per i
    cavalieri», «Un elmo di un certo peso».

### ⚠️⚠️ `reimporta` HA RESPINTO IL LOTTO INTERO PER UN VERSO DI DICIOTTO LETTERE

`:66979` e' 「ＡＳＤＪＵＲＨＦＫ＞ＲＯＷＲＷ＜ＭＷ！」, il verso dell'alieno, e
monte lo scrive uguale in tutt'e tre le lingue. **Copiarlo com'era e' costato
16 rese su 16**: quei caratteri sono a **doppia larghezza**, CP932 li scrive su
due byte e la build ne disegna **uno per byte** — a schermo sarebbero uscite
lettere latine a caso, come il 「・」 diventato «E» in una sessione passata.

⭐ E' `reimporta` che l'ha preso, non il preflight: la sua regola dei caratteri
guarda quel che CP932 spezza, mentre il punto 4 del preflight guarda gli accenti
dentro la parola. Sono due reti diverse, e la seconda non copre la prima.
💡 Il verso e' stato riscritto **a larghezza singola, lettera per lettera**:
`ASDJURHFK>ROWRW<MW!`. Non e' una traduzione — e' la stessa cosa scritta con
caratteri che la build sa disegnare.
⚠️ E vale in generale: **una stringa che si copia da monte perche' «non si
traduce» va comunque guardata carattere per carattere.** L'idea che copiare sia
l'operazione sicura e' esattamente sbagliata qui.

### ⓘ Il preflight ha segnalato quattro parole lunghe, e non erano un difetto

`un'organizzazione` (17), `sorprendentemente` (17) e il verso dell'alieno (22).
La finestra di rinculo del preflight e' 15, ma il tetto vero e' il budget da 77
del corpo impaginato: nel dizionario ci sono gia' **19 rese** con una parola da
17 caratteri o piu', e il cancello di `_107-descrizioni-item` legge 0 parole
spezzate. Verificato prima di proseguire, non dato per scontato.
"""
