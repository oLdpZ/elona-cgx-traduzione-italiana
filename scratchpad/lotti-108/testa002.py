# -*- coding: utf-8 -*-
"""108a - Lotto 002 di `db_item.hsp`: il rapporto di identificazione delle POZIONI.

`FILTER_ITEM_POTION`, `description(3)`: **77 righe del sorgente, 65 firme**. La
formula e' quella fissata dal lotto 001 (`glossario.md`, sezione della 108a), e
qui prende la forma «**Una pozione che** …» / «**Una bevanda che** …» — la
casella della categoria la riempie il giapponese stesso, che alterna
ポーション, 飲み物, 液体 e 油.

⚠️ **Il tetto e' sempre secco: 69 caratteri degradati**, e questa categoria e'
la prima che lo tocca davvero. Sette righe compongono due fatti
(«alza X e Y, e resiste a Z e W»), e li' «Una pozione che» non ci sta: quelle
**aprono col verbo**. Non e' un'eccezione alla formula, e' la formula che cede
la testa quando il contenuto la riempie — l'inglese fa lo stesso, e infatti
110 righe dell'indice 3 sforano gia' in inglese.

### ⚠️ Quattro giapponesi uguali che l'inglese distingue

Il rovescio del lotto 001, dove l'inglese appiattiva. Qui e' il giapponese a
essere lo stesso e l'inglese a variare, e la resa dev'essere **una**:

    :44445 / :72144   様々な状態異常を引き起こすポーションだ。
                      en «a variety of undesired effects» / «many negative
                      status effects» — la stessa cosa detta in due modi
    :126010 / :126081 HPと状態異常を回復するポーションだ。
                      en «cures ALL status effects» solo sulla pozione di Jure:
                      le altre sei dicono «cures status effects»

⭐ Le due coppie passano dalla **rete 13**, che le stampa come referto: e'
esattamente il caso per cui esiste.

### ⚠️ Due righe dove il giapponese dice un'altra cosa, e vince lui

- **`:90772`, la bottiglia vuota.** L'inglese: «a potion bottle that is
  completely empty». Il giapponese: 「水を汲むことができる瓶だ。」, *una
  bottiglia in cui si puo' prendere l'acqua*. Il secondo dice a che serve, il
  primo descrive il nome dell'oggetto — e la bottiglia vuota, in gioco, si
  riempie al pozzo.
- **`:129442`, l'acqua sporca.** L'inglese dice che fa ammalare; il giapponese
  dice 「病気になる可能性のある」, *che **puo'** far ammalare*. La differenza e'
  fra una certezza e una probabilita', ed e' quella che il giocatore vuole.

ⓘ **`:63387`, i dolcetti della strega**: l'inglese apre con «It is **food**» ma
il giapponese dice 飲み物, *bevanda*, come tutta la sua famiglia. Si segue lui.

ⓘ **I termini gia' fissati altrove, e qui si ubbidisce:** 「友好度」 → «la
simpatia» (`chat.hsp:25511`, `:14284`, `:14335`), 「エーテル病」 → «la malattia
dell'etere», 「状態異常」 → «gli stati alterati» (`buff.hsp:430` li chiama
«stati»), 「潜在能力」 → «il potenziale» (`chara.hsp:4311`), 「恐怖」 →
«terrore», e `DV`, `PV`, `HP` sono **invariati** perche' il giapponese scrive le
stesse sigle (`invariati.md:79`, `:83`, `:84`).
"""
