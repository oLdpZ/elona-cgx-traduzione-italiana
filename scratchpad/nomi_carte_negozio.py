# -*- coding: utf-8 -*-
"""Referto: i nomi di carta elencati nei blocchi `[Contains]` del negozio delle
carte, e la resa che il dizionario ha gia' per ciascuno.

⭐ **Nato nella 54ª.** Le 29 descrizioni di `tcg_custom.hsp` non sono prosa
soltanto: 26 portano in coda un elenco `[Contains]` di nomi di carta, e ogni
nome e' una **creatura del gioco** che il dizionario ha gia' reso altrove
(`db_creature.hsp`, `action.hsp`). Tradurre l'elenco senza guardare la resa
esistente vuol dire dare due nomi italiani alla stessa creatura: il giocatore
compra «la zanzara gigante» e sulla carta legge un'altra cosa.

⚠️ **La resa del dizionario porta l'articolo** («la zanzara gigante»), perche'
il contratto dei nomi dice che l'articolo lo porta il nome. Nell'elenco davanti
c'e' un numerale — « 1 Big Mosquito.» — e li' l'articolo non ci va: la colonna
`senza_articolo` e' quella da copiare nel lotto.

Uso:
    python scratchpad/nomi_carte_negozio.py           # tabella intera
    python scratchpad/nomi_carte_negozio.py --mancanti
"""
import argparse
import glob
import io
import json
import re
import sys
from pathlib import Path

SORGENTE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\tcg_custom.hsp')

LANG = re.compile(r'lang\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)')
DESC = re.compile(r'^\s*cardsetdesc@tcg\([^)]*\)\s*=\s*(.*)$')

# una voce dell'elenco: « 1 Spade Warrior.» / « 2 Yeek Warriors. » / «Little Girl»
VOCE = re.compile(r'^\s*(?:(\d+)\s+)?(.+?)\s*$')

ARTICOLI = ('il ', 'lo ', 'la ', 'i ', 'gli ', 'le ', "l'", "un ", "uno ", "una ", "un'")


def senza_articolo(resa: str) -> str:
    for a in ARTICOLI:
        if resa.lower().startswith(a):
            return resa[len(a):]
    return resa


def elenchi() -> list:
    """(riga, titolo del blocco, [ (quanti, nome inglese) ])."""
    fuori = []
    righe = io.open(SORGENTE, encoding='cp932').read().split('\n')
    for n, riga in enumerate(righe, 1):
        m = DESC.match(riga)
        if not m:
            continue
        l = LANG.search(m.group(1))
        if not l:
            continue
        testo = l.group(2).replace('\\n', '\n')
        for marca in ('[Contains]', '[Targets the following cards:]'):
            if marca not in testo:
                continue
            coda = testo.split(marca, 1)[1]
            voci = []
            for pezzo in coda.split('\n'):
                pezzo = pezzo.strip()
                if not pezzo:
                    continue
                # una riga puo' portare piu' voci: « 2 Ice Ents. 1 Grand Ent.»
                for parte in re.split(r'(?<=[.)])\s{1,}(?=\d)', pezzo):
                    parte = parte.strip()
                    if not parte:
                        continue
                    v = VOCE.match(parte)
                    quanti = int(v.group(1)) if v.group(1) else 1
                    nome = v.group(2).rstrip('.').strip()
                    voci.append((quanti, nome))
            fuori.append((n, marca, voci))
    return fuori


DB_CREATURE = Path(r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx\db_creature.hsp')
DBID = re.compile(r'^\s*if \(\s*dbid == (CREATURE_ID_[A-Z0-9_]+)\s*\)')
NAME_ORG = re.compile(r'DBSPEC_CHARA_NAME_ORG')
CONTENT = re.compile(r'^\s*cardsetcontent@tcg\([^)]*\)\s*=\s*(.*)$')


def nomi_per_id() -> dict:
    """CREATURE_ID_X -> nome inglese, letto da `DBSPEC_CHARA_NAME_ORG`.

    ⚠️ **Serve perche' l'elenco `[Contains]` non e' il contenuto vero.** Il
    contenuto sta in `cardsetcontent@tcg`, che porta gli id; l'elenco e' prosa
    scritta a mano, e in almeno un caso dice una cosa diversa — `:2166` elenca
    «Yerles Infantry» mentre la carta e' `Yerles machine infantry`. Chi traduce
    deve sapere quale delle due sta guardando."""
    mappa = {}
    righe = io.open(DB_CREATURE, encoding='cp932').read().split('\n')
    corrente = None
    atteso = False
    for riga in righe:
        m = DBID.match(riga)
        if m:
            corrente = m.group(1)
            atteso = False
            continue
        if corrente and NAME_ORG.search(riga):
            atteso = True
            continue
        if atteso:
            l = LANG.search(riga)
            if l:
                mappa.setdefault(corrente, l.group(2))
            atteso = False
    return mappa


def contenuti() -> dict:
    """riga della descrizione -> [CREATURE_ID_X, ...] davvero concessi."""
    fuori = {}
    righe = io.open(SORGENTE, encoding='cp932').read().split('\n')
    ultimo = None
    for n, riga in enumerate(righe, 1):
        m = CONTENT.match(riga)
        if m:
            ultimo = [x.strip() for x in m.group(1).split(',') if x.strip().startswith('CREATURE_ID_')]
            continue
        if DESC.match(riga) and ultimo is not None:
            fuori[n] = ultimo
            ultimo = None
    return fuori


def dizionario() -> dict:
    """inglese minuscolo -> [(file, riga, it)]"""
    indice = {}
    for p in sorted(glob.glob('dizionario/*.jsonl')):
        nome = Path(p).name
        for l in io.open(p, encoding='utf-8'):
            if not l.strip():
                continue
            d = json.loads(l)
            if not d.get('it'):
                continue
            indice.setdefault(d['en'].strip().lower(), []).append((nome, d['riga'], d['it']))
    return indice


def cerca(indice: dict, nome: str) -> list:
    """⚠️ Le voci dell'elenco non sono nomi puliti: portano una **battuta fra
    parentesi** («Skogsra (it's cute)») e sono al **plurale** quando il numerale
    e' maggiore di uno («2 Grizzlies»). Il dizionario ha il nome singolare e
    nudo, quindi le varianti vanno provate: e' la stessa disciplina della rete 3
    — si guarda se la resa esiste gia' prima di scriverne una nuova."""
    chiave = nome.strip().lower()
    nudo = re.sub(r'\s*\([^)]*\)\s*$', '', chiave).strip()
    varianti = [chiave, nudo, nudo.strip('<>'), f'<{nudo}>', nudo.removeprefix('the ')]
    if nudo.endswith('ies'):
        varianti.append(nudo[:-3] + 'y')
    if nudo.endswith('es'):
        varianti.append(nudo[:-2])
    if nudo.endswith('s'):
        varianti.append(nudo[:-1])
        varianti.append(f'<{nudo[:-1]}>')
    for variante in varianti:
        if variante in indice:
            return indice[variante]
    return []


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--mancanti', action='store_true')
    args = ap.parse_args()

    indice = dizionario()
    blocchi = elenchi()
    per_id = nomi_per_id()
    contenuto = contenuti()
    tutti = trovati = 0
    visti = {}
    divergenze = []
    for n, marca, voci in blocchi:
        # ⚠️ il conto vero delle carte: `cardsetcontent`, non l'elenco in prosa
        veri = [per_id.get(i, i) for i in contenuto.get(n, [])]
        # ⚠️ due falsi positivi da togliere prima di credere al conto:
        # `[Targets…]` non e' il contenuto del pacchetto ma la lista dei
        # bersagli, e «(Bonus)» e' un'etichetta che il lettore di voci conta
        # come se fosse una carta.
        quanti_elenco = sum(q for q, nome in voci if nome.lower() != '(bonus)')
        if veri and marca == '[Contains]' and quanti_elenco != len(veri):
            divergenze.append((n, quanti_elenco, len(veri), veri))
        righe_out = []
        for quanti, nome in voci:
            tutti += 1
            rese = cerca(indice, nome)
            if rese:
                trovati += 1
                it = rese[0][2]
                dove = f'{rese[0][0]}:{rese[0][1]}'
                diverse = {r[2] for r in rese}
                nota = f'  ⚠️ {len(diverse)} rese diverse' if len(diverse) > 1 else ''
                righe_out.append(f'    {quanti} {nome:38s} → {senza_articolo(it):38s} '
                                 f'[{dove}]{nota}')
            else:
                righe_out.append(f'    {quanti} {nome:38s} → ??? MANCA')
            visti.setdefault(nome, bool(rese))
        if args.mancanti and all('MANCA' not in r for r in righe_out):
            continue
        print(f'\n:{n} {marca}')
        if veri and not args.mancanti:
            print(f'    carte vere: {", ".join(veri)}')
        for r in righe_out:
            if args.mancanti and 'MANCA' not in r:
                continue
            print(r)
    mancanti = sorted(k for k, v in visti.items() if not v)
    print(f'\n=== {tutti} voci in {len(blocchi)} elenchi, {len(visti)} nomi distinti')
    print(f'=== trovati {trovati}/{tutti}; nomi distinti senza resa: {len(mancanti)}')
    for m in mancanti:
        print(f'    MANCA  {m}')
    print(f'\n=== l\'elenco in prosa contro `cardsetcontent`: '
          f'{len(divergenze)} descrizioni non tornano')
    for n, dichiarate, vere, veri in divergenze:
        print(f'    :{n}  l\'elenco dice {dichiarate} carte, il codice ne da\' {vere}')
        print(f'          {veri}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
