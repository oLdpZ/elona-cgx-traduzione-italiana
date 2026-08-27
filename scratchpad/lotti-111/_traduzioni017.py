# -*- coding: utf-8 -*-
"""Le rese del lotto 017 (gli ELMI e i CAPPELLI, `FILTER_HELM`), per RIGA.

    PYTHONIOENCODING=utf-8 python scratchpad/lotti-109/_monta.py 017 scratchpad/lotti-111

**15 righe del sorgente, 15 firme**, 14 giapponesi distinti.

⭐ **Tre parole per la testa, e restano tre**: 兜 «elmo», 帽子 «cappello»,
ヘルメット «casco» (il katakana, cioe' il moderno — stessa mossa di アーマー
«armatura» contro 鎧 «corazza» nel lotto 015). ウィッグ e' «parrucca», che i
nomi non identificati dicono gia'.

### ⚠️ `:43047` E `:43115` HANNO LO STESSO GIAPPONESE E DUE INGLESI

使うと見た目が変わるウィッグだ — la stessa riga, e l'inglese distingue il
codino («side-tail wig») dalla parrucca liscia. **Stessa resa**: e' la regola
della 110a sulle armi da lancio (`:68185` e `:117188`).

⭐ E la riga e' la **gemella** di `:51643` del lotto 015
(使うと見た目が変わる服だ, il Clothworld): stessa costruzione, stessa coda
何度でも使用することができる — gia' «Si può usare sempre.» nel dizionario.

### ⭐ TRE RITROVAMENTI, E NESSUNO E' UNA SCELTA

- 見えない者 e' gia' **«chi non si vede»**: sta nella descrizione della pistola
  di `:*` resa nel lotto 013 (「見えない者さえ打ちぬく拳銃だ」 -> «Una pistola
  che passa da parte a parte anche chi non si vede»). Quindi `:89080` e' «Un
  elmo che fa vedere chi non si vede».
- 異星人 e' gia' **«extraterrestre»** (la creatura che si finge uomo).
- 魔法使い e' gia' **«mago»**, ventidue volte.

### ⭐⭐ LA FAMIGLIA DEI DONI DIVINI ARRIVA A QUATTRO, IN TRE LOTTI

「身に着けると変形して〜になる」 — quattro artefatti, quattro oggetti diversi,
una costruzione sola. Cambia **solo** il nome della cosa, come nel giapponese:

    :57965  手枷           -> in ceppi                  (lotto 014)
    :75986  拘束具         -> in una gabbia             (lotto 015)
    :76184  頭につける輪   -> in un cerchietto da testa  (questo lotto)
    :76250  首輪           -> in un collare             (lotto 018)

⚠️ Se una delle quattro cambiasse costruzione, la famiglia si vedrebbe solo
leggendo il giapponese — cioe' non si vedrebbe.

### ⚠️ 用 / 向け / のため: tre costruzioni, un «per»

騎士用の兜 (:100005), 妖精向けの帽子 (:130847), 魔法使いのための帽子
(:130912), piu' 軽装向けの盾 (:101050, lotto 014) e 騎士用の盾 (:127207). In
giapponese sono tre sfumature; in italiano sono tutte «per», e forzarne una
diversa direbbe qualcosa che il giapponese non dice. Restano cinque «per».

ⓘ `:100070` e' 重量がある兜だ, **non** 重い: e' un'altra espressione e prende
un'altra resa («di un certo peso»), come 非常に重い e とても重い restano due.
"""

CAMBIA_ASPETTO = "Una parrucca che cambia aspetto. Si può usare sempre."

IT = {
    # === le due parrucche: stesso giapponese, due inglesi, una resa
    43047: CAMBIA_ASPETTO,
    43115: CAMBIA_ASPETTO,

    # === il dono divino, terzo dei quattro
    76184: "Se lo indossi, si trasforma in un cerchietto da testa.",

    # === gli elmi
    66980: "Un elmo ricavato dalla testa di un extraterrestre.",
    80427: "Un elmo con doti offensive.",
    89080: "Un elmo che fa vedere chi non si vede.",
    99875: "Un elmo duro.",
    100005: "Un elmo per i cavalieri.",
    100070: "Un elmo di un certo peso.",
    99940: "Un'armatura per proteggere la testa.",
    65401: "Una macchina a forma di casco.",

    # === i cappelli
    72421: "Un cappello che amplifica la magia.",
    100135: "Un cappello con una piuma.",
    130847: "Un cappello per le fate.",
    130912: "Un cappello per i maghi.",
}
