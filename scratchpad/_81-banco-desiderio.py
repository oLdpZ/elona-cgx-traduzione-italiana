# -*- coding: utf-8 -*-
"""Il desiderio di una CREATURA in italiano e' rotto: `fix_wish` (module.hsp)
non conosce le parole italiane, quindi dopo lo spoglio il nome non combacia con
nessuna creatura e `*wish_monster` ripiega su `dbid = 0` -> statuetta di `@`.

Le quattro parole d'innesco stanno in `lang()` (command.hsp:4846-4856) e sono
state tradotte; le righe che le tolgono dalla stringa NON stanno in `lang()`
(module.hsp:4815-4826) e sono rimaste inglesi.

Si prova prima sull'INGLESE DI MONTE (regola della 61a): se il banco non
riproduce l'inglese, e' rotto lui.

⚠️ Un difetto di MONTE trovato per strada: `cnv_str ..., "card", ""` morde
dentro i nomi. «figure of Scard» diventa «s», non «scard», e poi combacia con
la prima creatura che contiene una «s». Non e' nostro e non si tocca qui: per
questo il banco prova su Telhureza, che non contiene «card».

    python scratchpad/_81-banco-desiderio.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from banco_hsp import Banco
from strumenti import percorsi

# I nomi originali come li rende DBSPEC_CHARA_NAME_ORG nei due alberi.
# Il gioco li abbassa con getpath(s, 16) prima di confrontarli.
NOMI_MONTE = ["<Telhureza> the house guard", "<Oxode> the queen bee", "putit"]
NOMI_BUILD = ["<Telhureza> il geco di guardia", "<Oxode> l'ape stregina", "putit"]

# Le righe che la toppa aggiunge a fix_wish.
TOPPA = '''
\tcnv_str s2, "carta di ", ""
\tcnv_str s2, "carta ", ""
\tcnv_str s2, "carta", ""
\tcnv_str s2, "statuetta di ", ""
\tcnv_str s2, "statuetta ", ""
\tcnv_str s2, "statuetta", ""
\tcnv_str s2, "bambola dorata di ", ""
\tcnv_str s2, "bambola dorata ", ""
\tcnv_str s2, "bambola dorata", ""
\tcnv_str s2, "bambola di carne di ", ""
\tcnv_str s2, "bambola di carne ", ""
\tcnv_str s2, "bambola di carne", ""
'''


def giro(albero, etichetta, desiderio, nomi, toppa=False):
    b = Banco("desiderio", albero=albero)
    b.testa(jp=0, en=1)
    b.pezzo("init.hsp", 141, 148)        # lang()
    b.pezzo("module.hsp", 4783, 4827)    # del_str, cnv_str, fix_wish
    elenco = "\n".join(
        '\ts = "%s"\n\ts = getpath(s, 16)\n'
        '\tif ( instr(s, 0, s2) != (-1) ) { trovato = 1 : tappa "   COMBACIA: " + s }'
        % n.replace('"', '')
        for n in nomi
    )
    b.coda('''
*_banco_avvio
\ts2 = "%s"
\ts2 = getpath(s2, 16)
\ttappa "desiderio digitato : [" + s2 + "]"
\tfix_wish s2
%s
\ttappa "dopo lo spoglio    : [" + s2 + "]"
\ttrovato = 0
%s
\tif ( trovato == 0 ) { tappa "   NESSUN NOME COMBACIA -> dbid 0 -> statuetta di @" }
\ttappa "FINITO"
\tend
''' % (desiderio, TOPPA if toppa else "", elenco))
    d = b.esegui(secondi=60)
    print("=== %s   desiderio: %r" % (etichetta, desiderio))
    for r in d.splitlines():
        if r.strip():
            print("    " + r)
    b.pulisci()
    print()


def main():
    giro(percorsi.SORGENTE_HSP, "MONTE, inglese", "figure of Telhureza", NOMI_MONTE)
    giro(percorsi.BUILD_HSP, "BUILD, italiano, COM'E' ORA", "statuetta di Telhureza", NOMI_BUILD)
    giro(percorsi.BUILD_HSP, "BUILD, italiano, CON LA TOPPA", "statuetta di Telhureza", NOMI_BUILD, toppa=True)
    giro(percorsi.BUILD_HSP, "BUILD, carta, CON LA TOPPA", "carta di Oxode", NOMI_BUILD, toppa=True)
    giro(percorsi.BUILD_HSP, "BUILD, inglese ancora buono", "figure of Telhureza", NOMI_BUILD, toppa=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
