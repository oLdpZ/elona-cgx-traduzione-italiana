# -*- coding: utf-8 -*-
"""118a - Il nome del GRIMORIO contro il nome dell'INCANTESIMO che insegna.

In giapponese le due cose coincidono quasi sempre: il grimorio si chiama «il
libro di X» e lo skillname e' X. In italiano no, perche' i nomi degli oggetti
(`db_item.hsp`) e i nomi degli incantesimi (`skill.hsp`) sono stati resi in
sessioni diverse, da chi non aveva sott'occhio l'altra tabella. Il giocatore
invece le vede **nello stesso pannello**: il nome in testa e la descrizione
sotto, che dalla 118a nomina l'incantesimo.

⚠️ E' un REFERTO, non un cancello: dice quante sono e quali. Esce sempre con 0.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_118-nomi-vs-incantesimi.py
"""
import bisect
import io
import json
import os
import re
import subprocess
import sys

SORGENTE = 'C:/Games/Elona/_traduzione/sorgente/2.05-custom-gx'

_DBID = re.compile(r'^\tif \( dbid == (\w+) \) \{')
_EFID = re.compile(r'^\s*efid = (SKILL_SPELL_\w+)')
_SKILLNAME = re.compile(r'^skillname\((\w+)\) = lang\("([^"]*)", "([^"]*)"\)')
_FORMULA = re.compile(r'\u300c(.+?)\u300d\u3068\u3044\u3046\u546a\u6587')


def leggi(nome):
    return io.open(os.path.join(SORGENTE, nome), encoding='cp932').read().split('\n')


def rese_skill():
    """jp -> it, per le voci gia' rese di `skill.hsp`."""
    fuori = {}
    with io.open('dizionario/skill.hsp.jsonl', encoding='utf-8') as f:
        for linea in f:
            if linea.strip():
                voce = json.loads(linea)
                if voce.get('it'):
                    fuori.setdefault(voce.get('jp'), voce['it'])
    return fuori


def nomi_dal_dossier():
    """ITEM_ID -> nome italiano dell'oggetto.

    ⚠️ Il nome italiano NON si ricostruisce dal sorgente: e' un blocco a piu'
    righe (`contratto-nomi.md` §1-ter), e a rimetterlo insieme e'
    `_107-dossier-item.py`. Si chiede a lui, come `_forma.py` chiede a
    `_code.py` invece di riscriverne il modello.
    """
    uscita = subprocess.run(
        [sys.executable, 'scratchpad/_107-dossier-item.py',
         '--categoria', 'FILTER_ITEM_SPELLBOOK'],
        capture_output=True, text=True, encoding='utf-8', check=True).stdout
    fuori, corrente = {}, None
    for riga in uscita.split('\n'):
        m = re.match(r'=== (\w+)\s', riga)
        if m:
            corrente = m.group(1)
            continue
        m = re.match(r'\s+IT (.+)$', riga)
        if m and corrente and corrente not in fuori:
            fuori[corrente] = m.group(1).strip()
    return fuori


def main():
    db = leggi('db_item.hsp')
    incantesimi = {}
    for linea in leggi('skill.hsp'):
        m = _SKILLNAME.match(linea.strip())
        if m:
            incantesimi[m.group(1)] = (m.group(2), m.group(3))

    blocchi = [(n, m.group(1)) for n, m in
               ((n, _DBID.match(l)) for n, l in enumerate(db, 1)) if m]
    inizi = [b[0] for b in blocchi]

    it_skill = rese_skill()
    nomi = nomi_dal_dossier()

    divergenti, tot, jp_divergenti, senza = [], 0, [], 0
    for n, linea in enumerate(db, 1):
        if not re.match(r'^\s*description\(0\)', linea):
            continue
        m = _FORMULA.search(linea)
        if m is None:                      # non e' un grimorio della formula
            continue
        i = bisect.bisect_right(inizi, n) - 1
        fine = inizi[i + 1] - 1 if i + 1 < len(inizi) else len(db)
        efid = None
        for riga in db[inizi[i] - 1:fine]:
            mm = _EFID.match(riga)
            if mm:
                efid = mm.group(1)
                break
        if efid is None or efid not in incantesimi:
            continue
        tot += 1
        jp_spell, en_spell = incantesimi[efid]
        if m.group(1) != jp_spell:
            jp_divergenti.append((n, m.group(1), jp_spell, en_spell))

        it_libro = nomi.get(blocchi[i][1])
        it_spell = it_skill.get(jp_spell)
        if not it_libro or not it_spell:
            senza += 1
            continue
        corto = re.sub(r'\s*(grimorio|libro)\s*$', '', it_libro).strip()
        if corto.lower() != it_spell.lower():
            divergenti.append((n, corto, it_spell))

    print('grimori con la formula 「X」という呪文: %d' % tot)
    print()
    print('=== IL GIAPPONESE: nome del libro contro skillname')
    print('  divergenti: %d' % len(jp_divergenti))
    for n, a, b, en in jp_divergenti:
        print('    :%-7d 「%s」 contro 「%s」 / %s' % (n, a, b, en))
    print()
    print("=== L'ITALIANO: nome dell'oggetto contro nome dell'incantesimo")
    print('  ⚠️ divergenti: %d su %d   (referto, non cancello; senza dato: %d)'
          % (len(divergenti), tot, senza))
    for n, a, b in sorted(divergenti, key=lambda x: x[1]):
        print('    :%-7d %-34s ->  %s' % (n, a, b))
    print()
    print('ⓘ Il giocatore le vede insieme: il nome in testa al pannello e la')
    print("  descrizione sotto. Il rimedio e' allineare il NOME allo skillname,")
    print('  non il contrario: la descrizione serve a cercare la magia in lista.')
    return 0


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
