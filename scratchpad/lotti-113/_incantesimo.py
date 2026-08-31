# -*- coding: utf-8 -*-
"""118a - Per ogni riga del lotto, il NOME ITALIANO DELL'INCANTESIMO che il
grimorio insegna, preso dal codice e non dal nome del libro.

`description(0)` di un grimorio dice «un libro per imparare l'incantesimo X».
X e' il nome che il giocatore legge nella lista degli incantesimi, e **non** e'
il nome del libro: `db_item.hsp:91976` scrive 「扉生成」 mentre lo skillname e'
ドア生成 / "Door Creation" (`skill.hsp:709`). Prenderlo dal nome del libro
darebbe al giocatore un nome che nella lista non esiste.

Il percorso e' quello del codice: dal blocco `if ( dbid == ... )` che contiene
la riga si legge `efid = SKILL_SPELL_...` sotto `DBMODE_ON_READ`, si risolve la
costante nei `defines/`, e da `skill.hsp` si prende `skillname(...)`, che il
dizionario ha gia' reso.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/lotti-113/_incantesimo.py 047
"""
import importlib.util
import io
import json
import os
import re
import sys

QUI = os.path.dirname(os.path.abspath(__file__))
SORGENTE = 'C:/Games/Elona/_traduzione/sorgente/2.05-custom-gx'

_DBID = re.compile(r'^\tif \( dbid == (\w+) \) \{')
_EFID = re.compile(r'^\s*efid = (SKILL_SPELL_\w+)')
_DEFINE = re.compile(r'^#define global\s+(\w+)\s+(\d+)')
_SKILLNAME = re.compile(r'^skillname\((\w+)\) = lang\("([^"]*)", "([^"]*)"\)')


def leggi(nome):
    return io.open(os.path.join(SORGENTE, nome), encoding='cp932').read().split('\n')


def righe_del_lotto(numero):
    percorso = os.path.join(QUI, 'righe%s.py' % numero)
    spec = importlib.util.spec_from_file_location('righe', percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return sorted(modulo.RIGHE)


def costanti():
    fuori = {}
    for nome in sorted(os.listdir(os.path.join(SORGENTE, 'defines'))):
        if not nome.endswith('.hsp'):
            continue
        for linea in leggi('defines/' + nome):
            m = _DEFINE.match(linea.replace('\t', ' ').replace('  ', ' ').strip())
            if m is None:
                m = _DEFINE.match(re.sub(r'\s+', ' ', linea).strip())
            if m:
                fuori[m.group(1)] = int(m.group(2))
    return fuori


def skillnames():
    """SKILL_SPELL_xxx -> (jp, en, riga di skill.hsp)."""
    fuori = {}
    for n, linea in enumerate(leggi('skill.hsp'), 1):
        m = _SKILLNAME.match(linea.strip())
        if m:
            fuori[m.group(1)] = (m.group(2), m.group(3), n)
    return fuori


def rese_skill():
    """(jp, en) -> it, dalle voci di skill.hsp gia' rese."""
    fuori = {}
    with io.open('dizionario/skill.hsp.jsonl', encoding='utf-8') as f:
        for linea in f:
            if linea.strip():
                voce = json.loads(linea)
                if voce.get('it'):
                    fuori[(voce.get('jp'), voce.get('en'))] = voce['it']
    return fuori


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    numero = sys.argv[1]

    db = leggi('db_item.hsp')
    nomi = skillnames()
    rese = rese_skill()

    # per ogni riga: il dbid del blocco che la contiene, e il suo efid di lettura
    blocchi = []          # (riga_inizio, dbid)
    for n, linea in enumerate(db, 1):
        m = _DBID.match(linea)
        if m:
            blocchi.append((n, m.group(1)))

    def blocco_di(riga):
        scelto = None
        for inizio, dbid in blocchi:
            if inizio <= riga:
                scelto = (inizio, dbid)
            else:
                break
        return scelto

    def efid_di(inizio, fine):
        for linea in db[inizio - 1:fine]:
            m = _EFID.match(linea)
            if m:
                return m.group(1)
        return None

    inizi = [b[0] for b in blocchi]
    senza = 0
    for riga in righe_del_lotto(numero):
        b = blocco_di(riga)
        if b is None:
            print(':%d   ⚠️ nessun blocco dbid' % riga)
            continue
        inizio, dbid = b
        i = inizi.index(inizio)
        fine = inizi[i + 1] - 1 if i + 1 < len(inizi) else len(db)
        efid = efid_di(inizio, fine)
        if efid is None or efid not in nomi:
            senza += 1
            print(':%-7d %-40s   — nessun incantesimo' % (riga, dbid))
            continue
        jp, en, n_skill = nomi[efid]
        it = rese.get((jp, en), '⚠️ NON RESO')
        print(':%-7d %-40s %s  (skill.hsp:%d)\n            jp %s   en %s'
              % (riga, dbid, it, n_skill, jp, en))
    print('\nrighe senza incantesimo: %d   (sono i libri che non sono grimori)' % senza)


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    main()
