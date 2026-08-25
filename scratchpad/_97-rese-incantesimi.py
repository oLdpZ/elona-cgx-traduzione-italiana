# -*- coding: utf-8 -*-
"""97a - `command.hsp`: i due menu degli incantesimi (`:8481`-`:9032`).

24 firme, e sono **due finestre**, non una: la creazione dei grimori
(`:8481`-`:8567`) e il lancio (`:8787`-`:9032`).

⚠️⚠️ **VANNO INSIEME PERCHE' DUE FIRME SONO LE STESSE.** `Name` e
`Cost(Stock) Lv/Chance` compaiono in tutt'e due (`:8483`/`:8789`,
`:8484`/`:8790`) con lo stesso giapponese: **e' una firma sola**, e
`estrai --da-tradurre` la registra sulla prima occorrenza, cioe' su quella dei
grimori. Tagliare il lotto sul menu del lancio le lasciava fuori — lo script si
e' fermato dicendo «in piu': (8789, 'Name'), (8790, 'Cost(Stock) Lv/Chance')».
💡 Il tetto di una firma condivisa e' **il piu' stretto dei due riquadri**; qui i
due sono identici (720 px, colonne a 28/190/460), quindi la domanda non si pone,
ma andava guardata prima di rispondere.

⭐⭐ LA COSA CHE DECIDE IL LOTTO: **QUI I TETTI SONO TRE, E STANNO SCRITTI NEL
SORGENTE, NON A OCCHIO.**

  - la finestra e' `display_window …, 720, 438` (`:8788`), e le tre intestazioni
    partono da `wx + 28`, `wx + 190`, `wx + 460` (`:8789`-`:8791`): le colonne
    sono larghe **162**, **270** e ~**232** px. Le misura
    `strumenti.intestazioni_larghezze`, che e' una delle quindici verifiche
    d'apertura e deve restare a **perimetro 0**;
  - il limitatore e' un `*prompt_key` con `val = promptx, prompty, 200, 1`
    (`:8905`): 200 px, cioe' **20 caratteri** col metro di `larghezze.py`
    (`(200 - 46) / 7,7`). «Limite liv. 1500» sono 16, e l'inglese
    «Limiter LV.1000» 15;
  - la colonna «Effetto» ospita `:9004` e `:9032` **insieme al numero**, quindi
    la sigla e' un pezzo di riga e non una voce.

⚠️⚠️ LA SECONDA, ED E' UNA TRAPPOLA CHE UNA RETE VEDE: `:8894` E `:8895` HANNO
LO **STESSO GIAPPONESE** E DUE INGLESI DIVERSI. Il sorgente scrive
`lang("やっぱりやめる", "No Spell-lvl Limit")` per `z` e
`lang("やっぱりやめる", "No Casting-lvl Limit")` per `x`: il giapponese dice due
volte «lascia perdere», l'inglese specifica **quale** dei due limitatori.
**Si rende uguale** — «Nessun limite» — perche' il menu si apre da `z` o da `x`,
mai da tutt'e due, quindi quale limitatore sia lo sa gia' chi guarda.

⚠️⚠️ **CORREZIONE, e ho ripetuto l'errore che la 96a aveva gia' scritto.** Qui
c'era «`battute --divergenti` salirebbe da 13 a 14». **E' falso**, e si verifica
in una riga: `strumenti/battute.py:79` dice `FILE = "db_creature.hsp"`. Quello
strumento guarda **un file solo** — le battute delle creature — e su una riga di
`command.hsp` non ha niente da dire, ne' prima ne' dopo. La 96a aveva scoperto
la stessa cosa sui due `(Empty)` e l'aveva scritto nella sua ripresa; io l'ho
riscritta sbagliata lo stesso.

⭐ La rete che **vede** davvero questa famiglia su tutto il dizionario e'
`scratchpad/misura-rete4.py`: raggruppa per (giapponese, funzioni) e separa i
gruppi con lo **stesso** inglese — quelli senza scusa — da quelli con inglese
diverso, che e' il caso di qui. Se i due limitatori fossero resi in due modi, il
suo conto salirebbe di uno nella colonna «inglese diverso».

⚠️ E il senso e' **quello dell'inglese, non del giapponese**: `rtval` vale `0`
(`:8894`, terzo argomento) e `:8908` lo scrive in `customspelllimiter`. Non e'
un «annulla», e' il limite tolto. Il giapponese qui e' il testimone peggiore.

⭐ LA TERZA: `魔法の詠唱` E' «RECITAZIONE DELLA MAGIA», MA IL TITOLO E' UNA
TARGA. L'inglese lo accorcia a «Spell» e fa bene: la finestra e' l'elenco da cui
si sceglie. «Incantesimi» — il termine di `glossario.md`, riga 77 — e non
«Magia», che nel progetto e' l'**elemento** (`skill.hsp:70`).

LESSICO EREDITATO (non deciso qui):
  - incantesimo          `glossario.md`, «I nomi degli incantesimi»
  - abilità              `glossario.md`, `Skill`
  - Pot.                 `command.hsp:10734`, `SpellPow` -> «Pot. magia»
  - Turni / t            `command.hsp:10526`, `:10754`, `blend.hsp:379`
  - grimorio             `glossario.md`; `chat.hsp:5337` «sconti sui grimori»
  - Scorta               `blend.hsp:466`, `Stock:` -> «Scorta:»
  - lo stile dei suggerimenti: «Invio [Allena abilità]  », `command.hsp:10358`

PERIMETRO: 24 firme su 24, nessuna in un ramo `if ( jp )` (`_97-vive.py`).

⚠️ Accenti veri; niente virgolette tipografiche, niente caratteri a due byte.
"""
import io
import json
import sys

# chiave: (riga, inizio dell'inglese) — `:8787` porta DUE lang() sulla stessa riga
RESE = {
    # --- la finestra dei grimori
    (8481, 'Spellbook Production'): 'Creazione dei grimori',
    (8483, 'Name'): 'Nome',
    (8484, 'Cost(Stock) Lv/Chance'): 'Costo(scorta) Liv/Riuscita',
    (8485, 'Number'): 'Quanti',

    # --- il verdetto in coda alla riga: `strmid(s, 0, 40)` a `wx + 420` (`:8569`)
    (8561, 'books can be produced '): ' grimori ricavabili ',
    (8564, 'Not enough magic stock '): 'Scorta insufficiente ',
    (8567, "Can't produce "): 'Non convertibile ',

    # --- la finestra del lancio: titolo e suggerimento
    (8787, 'Spell'): 'Incantesimi',
    (8787, '  z/x [Spell-Lv/Casting-limit]  '): '  z/x [limiti magia/lancio]  ',
    (8791, 'Effect'): 'Effetto',

    # --- il limitatore (JAMES CUSTOM): tetto 20 caratteri
    (8894, 'No Spell-lvl Limit'): 'Nessun limite',
    (8895, 'No Casting-lvl Limit'): 'Nessun limite',
    (8896, 'Limiter LV.1'): 'Limite liv. 1',
    (8897, 'Limiter LV.10'): 'Limite liv. 10',
    (8898, 'Limiter LV.25'): 'Limite liv. 25',
    (8899, 'Limiter LV.50'): 'Limite liv. 50',
    (8900, 'Limiter LV.100'): 'Limite liv. 100',
    (8901, 'Limiter LV.250'): 'Limite liv. 250',
    (8902, 'Limiter LV.500'): 'Limite liv. 500',
    (8903, 'Limiter LV.1000'): 'Limite liv. 1000',
    (8904, 'Limiter LV.1500'): 'Limite liv. 1500',

    # --- il registro
    (8950, '[Showing all spells]'): '[Mostro tutti gli incantesimi]',

    # --- i due pezzi della colonna «Effetto», che vivono accanto a un numero
    (9004, 't '): 't ',
    (9032, 'Power:'): 'Pot.:',
}

LOTTO = 'lavoro/97-command-incantesimi.jsonl'

voci = [json.loads(l) for l in io.open(LOTTO, encoding='utf-8') if l.strip()]


def chiave(v):
    trovate = [k for k in RESE if k[0] == v['riga'] and v['en'].startswith(k[1])]
    if len(trovate) != 1:
        return None
    return trovate[0]


mancanti = [(v['riga'], v['en']) for v in voci if chiave(v) is None]
usate = {chiave(v) for v in voci if chiave(v)}
in_piu = [k for k in RESE if k not in usate]
if mancanti or in_piu:
    print('mancanti: %s' % mancanti)
    print("in piu' : %s" % in_piu)
    sys.exit(1)

with io.open(LOTTO, 'w', encoding='utf-8', newline='\n') as fh:
    for v in voci:
        v['it'] = RESE[chiave(v)]
        fh.write(json.dumps(v, ensure_ascii=False) + '\n')
print('%d rese scritte in %s' % (len(voci), LOTTO))
