# -*- coding: utf-8 -*-
"""110a - Lotto 009 di `db_item.hsp`: il rapporto delle BACCHETTE.

`FILTER_ITEM_ROD`, `description(3)`: **32 righe del sorgente, 30 firme**. E' la
categoria piu' formulaica di tutto l'indice 3: **trenta righe su trenta** aprono
con 「振ることで」 e chiudono con 「魔法の杖だ。」. Quel che cambia sta in mezzo.

    振ることで〜魔法の杖だ。 -> Una bacchetta che, agitata, ...

### ⭐⭐ IL VERBO NON E' STATO SCELTO: ERA GIA' A SCHERMO

「を振った。」 sta nel dizionario da una sessione precedente come
«"Hai agitato " + itemname(ci, 1) + "."» — e' il messaggio che il giocatore
legge **ogni volta** che usa una bacchetta. Il rapporto d'identificazione e il
messaggio dell'azione adesso dicono la stessa parola, e la riga della scheda
spiega il tasto che si preme.

⚠️ Vale la stessa lezione del lotto 007 («模造品» era gia' «riproduzione») e
del lotto 008 (le due code dei libri): la parte cara del lavoro non e' scegliere,
e' **ricordarsi di guardare se qualcuno ha gia' scelto**.

### ⭐ E I NOMI DELLE MAGIE ERANO GIA' GIUSTI

`skill.hsp` dice «Saetta», e la 90a aveva corretto i quindici nomi di
`db_item.hsp` che dicevano «dardo». Il controllo qui e' **positivo**: i nomi
degli oggetti di questa stessa categoria dicono gia' «saetta di fulmine», «saetta
di fuoco», «saetta di gelo» — e i tre giapponesi che li accompagnano sono
電撃属性のボルト, 火炎属性のボルト, 冷気属性のボルト. La resa del rapporto usa
gli stessi tre nomi, cioe' la scheda chiama la magia come la chiama l'oggetto.
⭐ `:123207` fa eccezione ed e' giusto cosi': il giapponese dice 矢 (*freccia*),
non ボルト, e l'oggetto si chiama «dardo magico».

### ⚠️ DUE RIGHE CHE DIFFERISCONO PER LA LARGHEZZA DI DUE CARATTERI

`:94105` e `:122824` hanno l'**inglese identico** («heal wounds of nearby
target») e due giapponesi che si distinguono per **`HP` a mezza larghezza contro
`ＨＰ` a larghezza piena**. Non sono due frasi: e' la stessa frase scritta due
volte da due mani. Stessa resa.

ⓘ Se un giorno una rete cerca i giapponesi «quasi uguali», questo e' il caso di
prova: nessuna delle due reti d'apertura sull'inglese lo vede, perche' li'
l'inglese e' identico e non e' un difetto.

### ⓘ La struttura del lotto, in quattro famiglie

    attacchi ad area (4)     : PV/DV, veleno, fulmine, oscurita'
    saette e dardi (5)       : arcana, fulmine, fuoco, gelo, dardo magico
    cio' che si crea (6)     : porte, muri di fiamme, pozza d'acido, muri
                               magici, ragnatela, mostri ostili
    su di te o sui vicini (6): cura x2, MP, maledizioni levate, maledizioni
                               respinte, accelerazione

più quattro sul bersaglio e cinque solitari.

### ⓘ I termini, verificati nel dizionario

振る → «agitare» (`を振った。` -> «Hai agitato ...») · ボルト → «saetta»
(`skill.hsp`, `glossario.md`) · 沈黙 → «silenzio» · 加速 → «Accelerazione» ·
鈍足 → «Rallentamento» · 呪い → «maledizione» · 蜘蛛の巣 → «ragnatela» ·
鑑定 → «identificare» · テレポート → «teletrasporto» · `HP`, `MP`, `PV`, `DV`
invariati (il giapponese scrive le stesse sigle).
"""
