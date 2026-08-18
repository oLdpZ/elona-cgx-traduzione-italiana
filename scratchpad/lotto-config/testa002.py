# -*- coding: utf-8 -*-
"""`config.hsp` si chiude: i 74 valori del pannello delle opzioni.

`config.hsp:751`-`:1046`, cioe' la colonna di destra — quel che il pannello
scrive accanto a ogni voce — piu' le due note in fondo. Con questo lotto
`config.hsp` e' **chiuso** per il referto del dizionario: 219 `lang()`, 160
firme, 160 rese.

Il tetto della colonna dei valori e' **15 caratteri**: il valore comincia a
`wx + 250` e la freccia destra sta a `wx + 358` (`config.hsp:743`, `:747`), a
7 px per carattere. Vedi il lotto 001 per come si e' misurato.

⚠️ **L'inglese lo sfora**: «Show All in Town» ha 16 caratteri. La resa
«Tutti in citta'» ne ha 15 esatti.

## ⚠️ Una firma sola serve dieci righe

`estrai.py --da-tradurre` da' **una voce per firma**, e le coppie
「しない」/「する」 → «No»/«Yes» compaiono a `:823`, `:827`, `:831`, `:861`,
`:865`, `:869`, `:878`, `:890`, `:898` e `:902`. Una resa sola le copre tutte,
e per questo deve funzionare in tutte: e' il motivo per cui 「なし」/«Don't
show» e' «No» e non «Nessuna» — la stessa firma serve l'interruttore della
guida (`:751`), le tre statistiche (`:783`), i cinque numeri di danno
(`:981`-`:994`) e i nomi dei PNG (`:1006`).

## ⚠️ Le quattro volte che l'inglese di monte e' peggio del giapponese

1. `:799` **確認なし** e' «nessuna conferma»; l'inglese scrive «Don't Use», che
   dice un'altra cosa — non si smette di usare i punti di viaggio, si smette di
   essere interrotti. `main.hsp:8470` lo conferma: `cfg_travelexp_select == 0`
   apre la domanda, l'altro valore la salta. Reso «Non chiedere».
2. `:894` **省略** e' «si salta»; l'inglese scrive «Highest», che continua la
   scala di velocita' invece di dire che il turno automatico non si vede piu'.
   Reso «Immediato», che tiene la scala e dice il fatto.
3. `:851` il giapponese mette la ragione fra parentesi — 「なし（高速）」,
   「あり（低速）」 — e l'inglese la copia stretta, «No(Fast)». La resa tiene la
   parentesi con lo spazio: «No (veloce)», «Si' (lento)».
4. `:1046` il giapponese ha **tre** righe e l'inglese due: quella che manca dice
   che le voci con (L) e (R) servono a cambiare linguetta nei menu, che e'
   l'unica ragione per cui quelle due voci hanno un suffisso. La resa tiene le
   tre righe.

## ⚠️ Cinque valori con lo stesso giapponese e cinque inglesi diversi

`:944` e' 「表示」 cinque volte, e l'inglese ci mette `Capitalize`, `Uppercase`,
`Lowercase`, `Spongebob`, `Schizophrenic`: sono i cinque modi di scrivere i nomi
degli oggetti nel registro (`cfg_capitalizeItemName`). Qui **l'inglese sa di
piu'** e si segue lui — il giapponese dice soltanto «si mostra». La rete 4 non
le ferma perche' dalla 57a la sua chiave porta anche l'inglese.

⚠️ La voce di menu che governa questi cinque valori e' uno dei due **letterali
nudi** di `:618` (`"Capitalize item names"`), e non sta in nessun lotto: vuole
una toppa. Vedi `scratchpad/nudi_accanto_a_lang.py`.

## Il vocabolario, e da dove viene

    Agita               道具を振る / «Zap», da text.hsp:135
    Identifica          道具を調べる / «Identify», da text.hsp:135 e skill.hsp:464
    al gancio           吊るし, da command.hsp:6608 «Finche' sta al gancio» —
                        l'inglese scrive «Sandbag», che e' l'oggetto e non il
                        gancio: qui il gioco controlla CHARA_BIT_SANDBAG, cioe'
                        una creatura appesa, non il sacco da boxe di db_item
    Bestie / Alleati    ペット e 味方, da db_card.hsp:13779 («arena delle
                        bestie») e dal glossario
    Direct sound        invariato: e' il nome del driver audio, come MCI
    Direct music        invariato, per la stessa ragione
    Spongebob           invariato: e' il nome del modo, una citazione
"""
