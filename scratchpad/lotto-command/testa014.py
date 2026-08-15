# -*- coding: utf-8 -*-
"""Lotto `command-014`: i 27 materiali che un compagno ti consegna, piu' la riga
che apre la consegna.

E' il comando «Raccogli i materiali» del lotto prima: ogni alleato porta quel
che ha raccolto in giro, e il gioco stampa una riga per tipo. Ventotto
dinamiche, tutte sulla stessa forma.

⚠️⚠️ **I nomi NON sono di questo file, e questa e' la trappola.** I 59 nomi
canonici stanno in `material_data.hsp:249`… — `matname(MATERIAL_PEBBLE) =
lang("石ころ", "Pebble")` — e quel file **non ha ancora un dizionario**. Qui
compaiono annegati dentro una frase: il giapponese di `:6289` e'
「マテリアル:**石ころ**を" + m1 + "個受け取った。」, che **contiene** 石ころ ma
non gli e' uguale.
⚠️ Quindi ne' `dossier.py` ne' la rete 3 li pescano: e' esattamente il caso
della 42a — un termine deciso in un file che torna a chiedere il conto in un
altro — e la risposta che quella sessione aveva gia' scritto e' **`glossario.md`**.
✅ I 27 nomi sono stati aggiunti li', in una tabella loro, col numero di riga di
`material_data.hsp` accanto. Chi apre quel file li trova gia' decisi.

⭐ **La forma non fa concordare niente col numero.** L'inglese scrive «You get 3
Pebble.», che e' sgrammaticato anche in inglese; l'italiano non puo' scrivere
«Ricevi 3 pietruzza» ne' indovinare il plurale di una variabile. ✅ Il
giapponese ha gia' la soluzione — 「石ころ**を3個**受け取った」, col contatore 個
che lascia il nome invariato — e in italiano il contatore e' la **parentesi**:
«Materiale ricevuto: pietruzza (3).» Il participio cade su «materiale», che un
genere ce l'ha suo.

⚠️ **Un nome diverge fra giapponese e inglese, e vince l'inglese.** 「風切石」 e'
«pietra che taglia il vento», ma la costante si chiama
`MATERIAL_ELEMENT_FRAGMENT` e l'inglese scrive «Element fragment» — e nel gioco
ci sono altre quattro «schegge» (etere, mithril, ferro, memoria, magia). Qui
**la coerenza batte il giapponese**, che e' la formula della 42a: «scheggia
elementale», per non lasciare un solo membro della famiglia fuori.
💡 E' l'unico dei ventisette in cui le due lingue non dicono la stessa cosa.

⭐ **Uno era gia' deciso**: 「魔法のインク」 e' «inchiostro magico» da
`action.hsp:12351`-`:12355`, le due righe che ti dicono quanto ne serve per una
pergamena.

⚠️ `:6248` porta `name(tc)` **come contenuto** e `he(tc)` come morfologia: il
primo resta, il secondo sparisce. «raccolti» concorda con «materiali», non col
compagno.
"""
