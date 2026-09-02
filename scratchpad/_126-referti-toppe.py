# -*- coding: utf-8 -*-
"""I referti di `referti.py`, girati sulle TOPPE invece che sul dizionario.

⚠️⚠️⚠️ **Le 1.062 toppe del progetto non le legge nessun referto.** `referti.py`
apre `dizionario/*.jsonl` e basta; `verifica`, `guardie`, `maiuscole`,
`larghezze`, `menu_dialogo` e le tredici reti del lotto guardano le **firme**, e
una toppa una firma non ce l'ha — e' la definizione stessa di toppa. Quindi
l'italiano che entra nel gioco da questa strada e' l'unico che **nessuna rete
del progetto ha mai letto**, e sono 1.062 righe.

E' lo stesso difetto che la 120a ha trovato sui participi: non un danno
misurato, ma **un permesso**. Finche' le toppe erano dieci articoli nudi non
contava; adesso sono il fronte principale, e nella 126a ne sono entrate 14 in un
colpo.

Qui si comincia dai due referti piu' economici — il **participio al maschile**
riferito a chi non ha genere noto e l'**elisione davanti a consonante** — perche'
sono gli stessi due che `referti.py` gia' misura, e cosi' i due numeri si
leggono insieme.

ⓘ **Come si trova l'italiano dentro una toppa.** Una toppa e' una riga di
codice, non una resa: i letterali di `sostituisci` che **non compaiono anche in
`cerca`** sono quel che la toppa ha aggiunto, cioe' l'italiano. Non e' esatto al
100% — una toppa che sposta un letterale senza cambiarlo non ha niente di nuovo
e sparisce dal conto — ma sbaglia per **difetto**, che e' il verso giusto per un
referto.

⚠️⚠️ **E lo zero non vuol dire «nessun participio».** L'unico participio che
questa sessione ha scritto apposta — «Tu sei gia' morto» di `proc.hsp:14389`,
la citazione di Ken il guerriero dichiarata in `invariati.md` — questo referto
**non lo vede**, per due motivi indipendenti: fra «sei» e il participio c'e'
«gia'», e «morto» non finisce con nessuna delle desinenze che l'espressione
cerca (`-ato -uto -ito -tto -so -sa`). L'espressione e' quella di `referti.py`
e resta identica apposta, perche' due reti che cercano la stessa cosa con due
regole diverse sono due numeri che non si possono confrontare. ⓘ Chi un giorno
allarghera' quella regola la allarghi **in `referti.py`**, e qui arrivera' da
sola.

⭐ Alla prima passata, su 1.062 toppe, ne ha trovati **due** — «Come sei andato
finora:» nel diario e «in base a come sei andato» nei ritocchi — e nessuno dei
due era di oggi: stavano li' da sessioni vecchie dietro una catena tutta verde,
perche' nessuna rete leggeva le toppe. Corretti in
`_126-participi-nelle-toppe.py`.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_126-referti-toppe.py
"""
import io
import json
import os
import re
import sys

_PROGETTO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# le stesse due espressioni di `referti.py`: se una cambia, cambiano tutt'e due
PARTICIPIO = re.compile(
    r'\b(?:ti sei|te ne sei|sei|sarai|ti eri|eri|il prossimo|la prossima)'
    r'\s+(\w+(?:ato|ata|uto|uta|ito|ita|tto|tta|so|sa))\b')
ELISIONE = re.compile(r"\b([Ll]|[Uu]n[ao]?|[Dd]ell|[Aa]ll|[Nn]ell|[Ss]ull|[Qq]uell)'([A-Za-z])")
VOCALI = set('aeiouAEIOUhH')
LETTERALE = re.compile(r'"(?:[^"\\]|\\.)*"')


def righe(valore) -> list:
    return list(valore) if isinstance(valore, list) else [valore]


def aggiunte(toppa: dict) -> list:
    """I letterali che `sostituisci` porta e `cerca` non aveva: l'italiano."""
    vecchi = set()
    for r in righe(toppa['cerca']):
        vecchi.update(LETTERALE.findall(r))
    fuori = []
    for r in righe(toppa['sostituisci']):
        for x in LETTERALE.findall(r):
            if x not in vecchi:
                fuori.append(x[1:-1])
    return fuori


def main() -> None:
    percorso = os.path.join(_PROGETTO, 'toppe.jsonl')
    toppe = [json.loads(l) for l in io.open(percorso, encoding='utf-8') if l.strip()]

    n_part = n_elis = 0
    con_testo = 0
    for toppa in toppe:
        nuovi = aggiunte(toppa)
        if nuovi:
            con_testo += 1
        for testo in nuovi:
            for m in PARTICIPIO.finditer(testo):
                print('PARTICIPIO  %-22s %s' % (toppa['file'], m.group(0)))
                print('            %s' % testo[:100])
                n_part += 1
            for m in ELISIONE.finditer(testo):
                if m.group(2) not in VOCALI:
                    print('ELISIONE    %-22s %s' % (toppa['file'], m.group(0)))
                    print('            %s' % testo[:100])
                    n_elis += 1

    print()
    print('toppe                       : %d' % len(toppe))
    print('toppe che aggiungono testo  : %d' % con_testo)
    print('participi                   : %d   ⚠️ lo zero non e\' «nessun '
          'participio»: vedi la testa del file' % n_part)
    print('elisioni                    : %d' % n_elis)
    return 0


if __name__ == '__main__':
    sys.exit(main())
