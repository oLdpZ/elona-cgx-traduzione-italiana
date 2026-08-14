# -*- coding: utf-8 -*-
"""La toppa di `chara_func.hsp:4520` e i due rinvii del lotto 004.

⚠️⚠️ **Il possessivo inglese arriva da trenta righe piu' su, e da una `lang()`
che `estrai.py` non vede.** `:4491` fa

    locvar_item_cold_s = name(item_cold_arg1) + lang("の", your(item_cold_arg1))

e `:4520` usa quella variabile come **prefisso** della frase. Il ramo inglese di
quella `lang()` e' **una sola chiamata di funzione, senza letterale**: non e' una
firma — le firme di `chara_func.hsp` sono 342 e `:4491` non e' fra loro — quindi
il dizionario non la raggiunge, ne' oggi ne' quando si tradurra' il file.
`your()` restituisce `"'s"` o `"r"` (`init.hsp:2045`), fuori da `lang()`, e a
schermo la riga italiana leggerebbe «il putit**'s** la spada e' andata in
frantumi».

⚠️ **E la resa non puo' rimediare nemmeno nominando il proprietario**: il
`name()` sta **dentro la variabile**, quindi `funzioni_di_contenuto` non lo
vede. L'inglese di `:4520` dichiara `['itemname']`, e una resa che aggiungesse
`name(item_cold_arg1)` verrebbe bocciata dalla rete 11. E' la strettoia di
`proc.hsp:11481`, `proc.hsp:24107` e `chara_func.hsp:3037` per una quarta
ragione.

✅ **La toppa gira il possessivo da PREFISSO a SUFFISSO**, che e' quello che
l'italiano vuole comunque: `:4491` costruisce «, che X porta addosso» e `:4520`
lo mette in fondo. Quando l'oggetto e' per terra la variabile e' vuota
(`:4488`) e la frase si chiude da sola.

    per terra   →  «Il gelo manda in frantumi la spada.»
    di qualcuno →  «Il gelo manda in frantumi la spada, che il putit porta addosso.»

⚠️ **Il ramo giapponese di tutt'e due le righe resta identico**, byte per byte:
la toppa tocca solo l'inglese.

⚠️ Le toppe **non passano da `degrada()`**: niente accenti nella sostituzione.
E si compone, si valida e si codifica tutto in memoria **prima** di aprire un
file in scrittura — la lezione della 39ª, quando uno script ha troncato
`toppe.jsonl` a zero byte.
"""
import io
import json
import os
import sys

sys.path.insert(0, os.getcwd())

from strumenti import percorsi  # noqa: E402

SORGENTE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\chara_func.hsp'

CERCA_A = ('\t\t\t\t\tlocvar_item_cold_s = name(item_cold_arg1) '
           '+ lang("の", your(item_cold_arg1))')
METTI_A = ('\t\t\t\t\tlocvar_item_cold_s = lang(name(item_cold_arg1) + "の", '
           '", che " + name(item_cold_arg1) + " porta addosso")')

CERCA_B = ('\t\t\t\ttxt lang(locvar_item_cold_s + itemname(locvar_item_acid_ci, '
           'locvar_item_acid_p) + "は粉々に砕けた。", locvar_item_cold_s + '
           'itemname(locvar_item_acid_ci, locvar_item_acid_p) + " break" '
           '+ _s2(locvar_item_acid_p) + " to pieces.")')
METTI_B = ('\t\t\t\ttxt lang(locvar_item_cold_s + itemname(locvar_item_acid_ci, '
           'locvar_item_acid_p) + "は粉々に砕けた。", "Il gelo manda in frantumi " '
           '+ itemname(locvar_item_acid_ci, locvar_item_acid_p) '
           '+ locvar_item_cold_s + ".")')

MOTIVO_TOPPA = (
    "chara_func.hsp:4520, piu' la riga che lo prepara, :4491. **Non e' una resa "
    "mancante: e' una riga che il dizionario non puo' aggiustare**, ed e' la quarta "
    "della famiglia dopo proc.hsp:11481 (36a), proc.hsp:24107 (39a) e "
    "chara_func.hsp:3037 (39a). La causa pero' e' nuova: il pezzo da girare sta in "
    "una **lang() che estrai.py non vede**. :4491 fa `locvar_item_cold_s = "
    "name(item_cold_arg1) + lang(\"の\", your(item_cold_arg1))`, e il ramo inglese di "
    "quella lang() e' **una sola chiamata di funzione, senza letterale**: non produce "
    "firma (le firme di chara_func.hsp sono 342 e :4491 non e' fra loro), quindi il "
    "dizionario non la raggiunge ne' oggi ne' domani. \u26a0\ufe0f `your()` restituisce "
    "\"'s\" o \"r\" (init.hsp:2045) fuori da lang(), e a schermo la riga leggerebbe "
    "«il putit's ...». \u26a0\ufe0f E la resa non puo' rimediare nominando il "
    "proprietario, perche' il name() sta DENTRO la variabile e "
    "funzioni_di_contenuto non lo vede: l'inglese dichiara ['itemname'] e la rete 11 "
    "boccerebbe una resa con name(). \u2705 La toppa gira il possessivo da prefisso a "
    "**suffisso**, che e' la forma che l'italiano vuole comunque: :4491 costruisce "
    "«, che X porta addosso» e :4520 lo mette in fondo. Quando l'oggetto e' per terra "
    "la variabile e' vuota (:4488) e la frase si chiude da sola. Il ramo giapponese "
    "di tutt'e due le righe resta identico. Fatta nella 40a insieme al rinvio."
)

MOTIVO_4369 = (
    "chara_func.hsp:4369. Riga **commentata** nel sorgente: sta dentro il blocco del "
    "tag-team che il mod ha spento riga per riga col `;`, e `estrai.py` non salta i "
    "commenti HSP (scoperta 1 della 27a). Il giocatore non la legge mai. \U0001f4a1 E non "
    "si perde niente comunque: lo stesso giapponese 「はをかばった！」 e lo stesso "
    "inglese sono gia' resi «X protegge Y.» in proc.hsp:6481 e text.hsp:13. Non c'e' "
    "toppa da fare: non e' un difetto a schermo, e' testo morto."
)


def riscrivi(percorso, righe_nuove) -> int:
    """Compone, codifica in memoria, e solo allora apre. Vedi il docstring."""
    righe = [r for r in io.open(percorso, encoding='utf-8').read().splitlines() if r.strip()]
    righe.extend(righe_nuove)
    dati = ('\n'.join(righe) + '\n').encode('utf-8')
    with io.open(percorso, 'wb') as f:
        f.write(dati)
    return len(righe)


sorgente = io.open(SORGENTE, encoding='cp932').read()
for etichetta, cerca in (('A (:4491)', CERCA_A), ('B (:4520)', CERCA_B)):
    quante = sorgente.count(cerca)
    if quante != 1:
        sys.exit(f'la riga {etichetta} compare {quante} volte nel sorgente, non una')
for metti in (METTI_A, METTI_B):
    metti.encode('cp932')

toppe = percorsi.PROGETTO / 'toppe.jsonl'
# ⚠️ `cerca` non e' sempre una stringa: alcune toppe ne portano una LISTA
# (sostituzioni su piu' righe). La chiave di confronto va normalizzata, o
# l'insieme esplode con «unhashable type: 'list'».
gia = {json.dumps(json.loads(r).get('cerca'), ensure_ascii=False)
       for r in io.open(toppe, encoding='utf-8').read().splitlines() if r.strip()}
nuove = [json.dumps({'file': 'chara_func.hsp', 'cerca': cerca, 'sostituisci': metti,
                     'motivo': MOTIVO_TOPPA}, ensure_ascii=False)
         for cerca, metti in ((CERCA_A, METTI_A), (CERCA_B, METTI_B))
         if json.dumps(cerca, ensure_ascii=False) not in gia]
if nuove:
    print('toppe.jsonl:', riscrivi(toppe, nuove), 'toppe')
else:
    print('toppe gia\' presenti')

estrazione = [json.loads(l) for l in io.open('lavoro/_chara_func.jsonl', encoding='utf-8')
              if l.strip()]
per_riga = {v['riga']: v for v in estrazione}

rinviate = percorsi.PROGETTO / 'rinviate.jsonl'
gia_rinviate = {json.loads(r).get('firma')
                for r in io.open(rinviate, encoding='utf-8').read().splitlines() if r.strip()}
righe_nuove = []
for riga, rinviata_a, motivo in (
    (4369, 'nessuna fase: riga commentata, codice morto', MOTIVO_4369),
    (4520, 'nessuna fase: risolta da toppa (chara_func.hsp:4491 e :4520, 40a)', MOTIVO_TOPPA),
):
    voce = per_riga.get(riga)
    if voce is None:
        sys.exit(f'voce {riga} non trovata nell\'estrazione')
    if voce['firma'] in gia_rinviate:
        continue
    righe_nuove.append(json.dumps(
        {'firma': voce['firma'], 'file': 'chara_func.hsp', 'en': voce['en_grezzo'],
         'rinviata_a': rinviata_a, 'motivo': motivo}, ensure_ascii=False))
if righe_nuove:
    print('rinviate.jsonl:', riscrivi(rinviate, righe_nuove), 'rinvii')
else:
    print('rinvii gia\' presenti')
