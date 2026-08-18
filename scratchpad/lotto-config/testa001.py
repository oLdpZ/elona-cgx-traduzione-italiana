# -*- coding: utf-8 -*-
"""`config.hsp` si apre: le 86 etichette del pannello delle opzioni.

`config.hsp:580`-`:681`, cioe' il nome del pannello, i nove nomi di sezione e
tutte le voci delle nove sottosezioni. I valori accanto a ogni voce (`Show`,
`Don't show`, `Yes`, `No`...) stanno nel lotto 002.

⚠️ **Il file non aveva dizionario**: 219 `lang()` che nessun conteggio guardava.
E' la regola della 54a — «un file senza file di dizionario non e' un file
finito: e' un file che nessun conteggio guarda» — e con questo lotto
`config.hsp` entra nel referto.

## I due tetti, misurati nel disegnatore e non stimati

`cs_list` (`module.hsp:70`-`:130`) disegna l'etichetta e dichiara da se' quanto
misura un carattere:

    locvar_cs_list_tx = limit(strlen(cs_list_arg1) * 7 + 32 + cs_list_arg5, 10, 480)

**7 px per carattere**, e non e' una stima: il carattere inglese e' `Courier
New` (`config.txt`, `font2.`), monospaziato, e `config.hsp:716` lo chiede a
`14 - en * 2` = **12**. A 12 px di corpo il passo del Courier e' 0,6 em = 7,2 px,
cioe' i 7 che il sorgente scrive. ⚠️ E' lo stesso 7 della 59a, di nuovo
confermato: il 7,7 di `larghezze.py` viene da un altro carattere.

I due confini stanno nel disegnatore del pannello (`config.hsp:738`-`:747`):

    cs_list s, wx + 56 + x, ...      l'etichetta comincia a wx + 60 (+4 di cs_list)
    pos wx + 220 : gcopy ...         la freccia sinistra
    pos wx + 250 : mes s(...)        il valore
    pos wx + 358 : gcopy ...         la freccia destra

    etichetta   (220 - 60) / 7 = 22 caratteri
    valore      (358 - 250) / 7 = 15 caratteri     <- lotto 002

⚠️ **`mes` non taglia e non manda a capo**: quel che sfora finisce *sopra* la
freccia e poi sopra il valore. E' la stessa forma di `command.hsp:8186` nella
59a, dove l'eccedenza si stampava sopra la mappa.

⚠️ **L'inglese non e' il tetto, e qui sfora due volte**: «Block defecate
generation» ha 25 caratteri in un riquadro da 22, e «Show All in Town» ne ha 16
in uno da 15 (lotto 002). La resa italiana sta dentro tutt'e due.

💡 **L'elenco delle sezioni ha un riquadro suo**: `dx = 370` invece di 440
(`:583`), e li' non ci sono ne' frecce ne' valore — la voce arriva fino al bordo.
Per questo «Impostazioni extra 2 (schermo)» puo' avere 30 caratteri: la
linguetta del titolo cresce da sola (`module.hsp:4328`,
`limit(strlen(s) * 8 - 120, 0, 200)`).

## ⚠️ Due voci di questo menu NON sono in questo lotto, e non e' un rinvio

`:618` ha sei voci, e due sono letterali inglesi **nudi**, senza `lang()`:
`"  Display log instead*"` e `"Capitalize item names"`. Il dizionario non le
raggiunge e vogliono una toppa. Le ha trovate `scratchpad/nudi_accanto_a_lang.py`,
scritto oggi: e' il **dodicesimo punto cieco**, e nasce dal fatto che
`nudi_en.py` salta la riga intera appena ci legge un `lang(`.

## Il vocabolario fissato qui, e da dove viene

    PNG                 gia' 5 volte in command.hsp, mai «NPC»
    Norne               la guida, da db_creature.hsp:77957 — il giapponese
                        nomina il personaggio, l'inglese scrive «Extra Help»
    sterco              shit, da db_item.hsp:144913 — 汚物 non era mai stato reso
    barra               ゲージ技, «mossa di barra» da proc.hsp:12899
    malocchio           hex, dal glossario (⚠ non «maledizione», che e' curse)
    Alleato             ally, dal glossario
    Bersaglio / Tiro    da text.hsp:135 e :136, le due etichette gia' rese
    Schivata            da command.hsp:10732 («Schiv.», abbreviata li' per posto)
    Zaino               inventory, da command.hsp:12929 «Il tuo zaino e' pieno»
    Scheda              la linguetta di module.hsp:5148, per «Chara-sheet»
    Registro            la linguetta di module.hsp:5158, per «Log»
    Voce                項目, come «Category» e «Part» in command.hsp

## ⚠️ Le tre volte che il giapponese dice piu' dell'inglese

1. `:588` **ノルンの冒険ガイド** nomina Norne; l'inglese scrive «Extra Help» e
   perde chi parla. La guida in gioco e' scritta in prima persona da lei
   (`data/exhelp.txt`): la resa tiene il nome.
2. `:588` **汚物生成の阻止** dice che cosa si blocca (lo sterco); «Block defecate
   generation» dice l'atto. In italiano si nomina la cosa, come il giapponese.
3. `:606` **オートターンの挙動** dice «comportamento», l'inglese «Auto Turn
   Speed». I valori sono 普通 / 速め / 省略, che sono tre velocita': qui
   l'inglese ha ragione sul contenuto e il giapponese sulla forma, e la resa
   sta col giapponese perche' l'etichetta e' un sostantivo.

## ⚠️ E la volta che lo stesso giapponese vale due voci diverse

**ダメージ表示** compare a `:606` (inglese «Damage show») e a `:636` (inglese
«Damage Popups»), e sono **due impostazioni diverse**: la prima e' `cfg_dhyouji`,
che scrive il danno fra parentesi **nel registro** (`chara_func.hsp:6006`,
`:8020`); la seconda e' `cfg_dmgpopups`, i numeri che volano sopra il bersaglio.
Le rese devono differire, e la rete 4 non le ferma perche' l'inglese e' diverso.
"""
