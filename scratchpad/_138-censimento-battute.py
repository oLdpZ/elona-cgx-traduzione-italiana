"""Censimento del lotto D: le battute del gioco di carte, prese da CHI PARLA.

Non dalla forma della stringa (l'euristica che la 137a ha visto perdere 58
etichette), ma dai siti che mandano un testo alla nuvoletta:

    efllistaddchat  <espressione>, ...      tcg.hsp:1362, la disegna `bmes`
    efllistaddchatplayer <espressione>, ... tcg.hsp:1357, chiama la prima

Se l'espressione e' un letterale, e' una battuta. Se e' un array
(`randomchat@tcg(rnd(3))`), il nome dell'array si segna e poi si cercano le
sue ASSEGNAZIONI, che portano piu' letterali sulla stessa riga.
"""
import re
from collections import defaultdict

from strumenti import percorsi
from strumenti.commenti import righe_in_commento

FILE = ("tcg.hsp", "tcg_skill.hsp", "tcg_custom.hsp", "tcg_mod.hsp")

_CHIAMATA = re.compile(r"\befllistaddchat(?:player)?\s+(.+)$")
_LETTERALE = re.compile(r'"((?:[^"\\]|\\.)*)"')
_ARRAY = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*@tcg)\s*\(")
_NUDO = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*@tcg)\s*,")

letterali = []          # (file, riga, testo, come)
arrays = defaultdict(list)

testi = {}
for nome in FILE:
    percorso = percorsi.SORGENTE_HSP / nome
    testi[nome] = percorso.read_bytes().decode("cp932").split("\r\n")
    morte = righe_in_commento(percorso)
    for numero, riga in enumerate(testi[nome], 1):
        spoglia = riga.lstrip()
        if numero in morte or spoglia.startswith(";") or spoglia.startswith("//"):
            continue
        trovato = _CHIAMATA.search(riga)
        if trovato is None:
            continue
        coda = trovato.group(1).strip()
        if coda.startswith('"') or coda.startswith("cnvtalk("):
            for testo in _LETTERALE.findall(coda):
                letterali.append((nome, numero, testo, "diretta"))
        else:
            nome_array = _ARRAY.match(coda) or _NUDO.match(coda)
            if nome_array:
                arrays[nome_array.group(1)].append("%s:%d" % (nome, numero))

print("=== battute dirette: %d ===" % len(letterali))
for nome, numero, testo, _ in letterali:
    print("  %-16s %5d  %r" % (nome, numero, testo))

print("\n=== array di battute: %d ===" % len(arrays))
for nome_array, posti in sorted(arrays.items()):
    print("  %-24s letto da %s" % (nome_array, ", ".join(posti[:4])))

print("\n=== assegnazioni degli array ===")
totale_array = 0
for nome_array in sorted(arrays):
    assegna = re.compile(r"^\s*%s\s*(\([^)]*\))?\s*\+?=\s*(.*)$"
                         % re.escape(nome_array))
    for nome in FILE:
        morte = righe_in_commento(percorsi.SORGENTE_HSP / nome)
        for numero, riga in enumerate(testi[nome], 1):
            spoglia = riga.lstrip()
            if numero in morte or spoglia.startswith(";") or spoglia.startswith("//"):
                continue
            trovato = assegna.match(riga)
            if trovato is None:
                continue
            pezzi = _LETTERALE.findall(trovato.group(2))
            if not pezzi:
                continue
            totale_array += len(pezzi)
            print("  %-16s %5d  %-24s %d: %s"
                  % (nome, numero, nome_array, len(pezzi),
                     " | ".join(repr(p) for p in pezzi)))

print("\ndirette %d + da array %d = %d"
      % (len(letterali), totale_array, len(letterali) + totale_array))
