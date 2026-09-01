# -*- coding: utf-8 -*-
"""123a - Lotto 071 di `db_item.hsp`: LE ALGHE, e la categoria CHIUDE.

`FILTER_ENVIRONMENT_SEABED`, righe da `:44863` a `:44991`: **6 righe** —
3 dell'indice 0 e **3 dell'indice 2** — su 3 oggetti (mozuku, kombu, wakame).
Con questo lotto la categoria va a **0 da fare su 6 vive**, ed e' la
**ventiseiesima** categoria del corpo che si chiude.

⚠️⚠️ Previsione di `applica`, da `_previsione.py 071`: **+6** per 6 rese,
nessuna gemella. ⓘ `_code.py 071`: 0 righe senza resa in tabella.
`_forma.py 071`: 0 su 6 con lo spazio prima del `\\n`, 0 su 6 con lo spazio
dopo il `#` — tutte e sei senza. Preflight: **0 guasti, 0 parole lunghe**.
`_122-sorelle-per-frase 071`: **0 frasi con una sorella**, la prima volta.

### ⭐⭐⭐ TRE RIGHE COL GIAPPONESE VUOTO, E UNA RETE CHE PER QUESTO SBAGLIA

Le tre `description(2)` — `:44865`, `:44928`, `:44991` — **non hanno
giapponese**. L'inglese un testo ce l'ha, quindi si rendono: e' il caso di
`:89358` e non quello di `:129299`, e la domanda non e' «manca il giapponese?»
ma «esiste una fonte?».

⚠️⚠️⚠️ **Il seguito e' che `_120-serie-bacchette` da' un avviso FALSO.** La
rete dice:

    en :44928  Giant seaweed. You can eat it I guess.
    en :44991  Huge seaweed. You can eat it I guess.
    ⚠️ le rese di queste righe devono essere IDENTICHE: il giapponese e' lo
       stesso, e l'inglese differisce per una sciocchezza

Il giapponese e' lo stesso perche' e' **vuoto** in tutt'e due, e due stringhe
vuote sono uguali a ogni rete che le confronti. Seguito alla lettera, l'avviso
avrebbe cancellato una distinzione che il gioco fa davvero.

⭐ **L'arbitro sta nella `description(3)` degli stessi due oggetti**, che il
giapponese ce l'ha e che il dizionario ha gia' reso:

    :44929  巨大な海藻だ  ->  «Un'alga gigantesca»   (kombu,  en «Giant»)
    :44992  大きな海藻だ  ->  «Un'alga grande»       (wakame, en «Huge»)

Quindi le tre rese dell'indice 2 aprono con **la stessa parola dell'indice 3
dello stesso oggetto**, e il pannello si legge coerente dall'alto in basso.
E l'inglese, che qui e' l'unica fonte diretta, dice la stessa cosa: «Giant» e
«Huge» sono due parole, non una sciocchezza.

⚠️ **La regola generale.** Una rete che confronta due campi puo' dire «uguali»
perche' i campi **non ci sono**. Prima di seguire un avviso di uguaglianza si
guarda se il valore su cui l'ha dato e' vuoto — e se lo e', l'avviso non e' una
prova, e' un'assenza di prove.

### ⓘ Le parole del giapponese, e da dove vengono

- 海藻 -> **«alga»** (glossario). `mozuku`, `kombu` e `wakame` sono nomi
  **invariati** (`invariati.md`, tre voci): non compaiono nel corpo, che parla
  sempre di «un'alga», ed e' il nome in cima al pannello a dire quale sia.
- 具材 -> **«ingrediente»**, dal dizionario: le due righe del mochi.
- ダシ non e' nel dizionario, ma **«brodo»** ci sta gia' due volte, nelle
  stesse due righe del mochi. Si ricopia da li' invece di inventare.
- 喉越し non ha una voce, e l'italiano ce l'ha di suo: di un cibo o di una
  bevanda si dice che **«scende bene»**. L'inglese qui traduce a calco («an
  excellent texture and throat») e non aiuta.
- 酢漬け -> **«sott'aceto»**. 重宝されてきた -> «e' tenuta cara», col passato
  che dura, come fa l'inglese con «has long been valued».

### ▶ Il conto

Il corpo passa da **1.492 a 1.498 rese su 1.513**, e restano **15 righe** — di
cui una rinviata (`:129299`). Dopo il 071 mancano **sei** categorie:

    5  FILTER_AMMO             1  FILTER_PLATINUM
    4  FILTER_FURNITURE_WELL   1  FILTER_GOLD
    2  FILTER_FURNITURE_ALTAR  1  FILTER_CARGO_FOOD

⚠️ La tabella si rilegge con `_114-corpo-da-fare`, non si eredita da qui.
"""
