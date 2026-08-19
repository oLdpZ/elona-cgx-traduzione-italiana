# -*- coding: utf-8 -*-
"""Far girare un pezzo di HSP **fuori dal gioco**, e leggerne il diario.

⭐⭐⭐ Nato nella 65a, ed e' il modo con cui si e' trovata la causa del blocco
sugli epiteti in mezz'ora invece che a tentativi di ricompilazione. Fino a ieri
l'unico modo di provare il codice HSP era: `applica`, `compila --eseguibile`,
aprire il gioco, cliccare. Cinque minuti a giro, e chi collauda deve esserci.

Il banco monta un `#runtime "hsp3cl"` — il runtime **console** che sta gia'
nell'SDK — con dentro le funzioni copiate dalla build, lo compila con
`strumenti.compila` e lo esegue. Un giro costa **secondi**, e non serve nessuno
davanti allo schermo.

## Le due regole che il banco ha imparato a sue spese

⚠️⚠️ **1. Il diario si scrive su FILE, non con `mes`.** Se il codice in prova si
pianta, il processo va ucciso, e l'uscita bufferizzata di `mes` **si perde
tutta**: il banco sembra non aver stampato niente e non dice dove si e' fermato.
La 65a ci ha perso due giri prima di capirlo. La forma che tiene e' un `#deffunc`
che accoda al diario e fa `notesave` a ogni tappa.

⚠️⚠️⚠️ **2. La testa si scrive con lo strumento di scrittura, mai con
`printf`/heredoc.** Il primo banco della 65a dava un errore di file **sia in
italiano sia in inglese**, e per un quarto d'ora e' sembrato un guasto di monte:
era `exedir = "C:\\Games\\..."` coi backslash mangiati dalla shell, che HSP
leggeva come sequenze di escape. E' la lezione della 60a alla quarta ripetizione
(vedi [[elona-due-macchine]]).

## Come si usa

    from banco_hsp import Banco
    b = Banco("epiteti")
    b.testa(jp=0, en=1)                       # le variabili di lingua e exedir
    b.pezzo("init.hsp", 141, 148)             # lang()
    b.pezzo("init.hsp", 191, 212)             # cnven()
    b.pezzo("etc.hsp", 319, 532)              # csvsort + random_titleInit + random_title
    b.coda('''
    *avvio
        gosub *random_titleInit
        tappa "righe: " + length2(rnlist)
        repeat 20
            tappa "" + cnt + ": " + random_title(0)
        loop
        end
    ''')
    print(b.esegui(secondi=40))

⭐ E la regola della 61a vale anche qui: **il banco si prova sull'inglese di
monte prima di crederci sull'italiano.** Basta passare `albero=SORGENTE`: se non
riproduce l'inglese, il banco e' rotto lui, non il codice in prova.
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from strumenti import compila, percorsi

RUNTIME = percorsi.HSP / "hsp3cl.exe"
GIOCO = Path(r"C:\Games\Elona\elonaplus2.31")

TESTA = '''#runtime "hsp3cl"
\tjp = {jp}
\ten = {en}
\tsdim titlebuff, 65536
\tsdim msgtemp, 1024
\tsdim diario, 262144
\texedir = "{exedir}"
\tgoto *_banco_avvio

#deffunc tappa str tappa_t
\tdiario += tappa_t + "\\n"
\tnotesel diario
\tnotesave "diario.txt"
\treturn

'''


class Banco:
    """Un pezzo di HSP montato su hsp3cl, con il diario su file."""

    def __init__(self, nome, albero=None):
        self.nome = nome
        self.albero = Path(albero) if albero else percorsi.BUILD_HSP
        self.cartella = Path(tempfile.mkdtemp(prefix=f"banco-{nome}-"))
        self.pezzi = []
        self._testa = None
        self._coda = None

    def testa(self, jp=0, en=1, exedir=None):
        percorso = str(exedir or GIOCO)
        if not percorso.endswith("\\"):
            percorso += "\\"
        # HSP legge \ come escape: nel sorgente ce ne vogliono due
        self._testa = TESTA.format(jp=jp, en=en, exedir=percorso.replace("\\", "\\\\"))
        return self

    def pezzo(self, file, prima, ultima):
        """Copia le righe [prima, ultima] di un file della build, 1-based e incluse."""
        righe = (self.albero / file).read_bytes().decode("cp932", "replace").splitlines()
        self.pezzi.append("\n".join(righe[prima - 1:ultima]))
        return self

    def coda(self, testo):
        self._coda = testo
        return self

    def _scrivi(self):
        if self._testa is None:
            self.testa()
        corpo = self._testa + "\n\n".join(self.pezzi) + "\n" + (self._coda or "")
        # il file va scritto in CP932: i pezzi copiati portano dentro il giapponese
        (self.cartella / "main.hsp").write_bytes(corpo.encode("cp932", "replace"))

    def esegui(self, secondi=60):
        """Compila e fa girare. Ritorna il diario, anche se il codice si e' piantato."""
        self._scrivi()
        esito = compila.compila(self.cartella, self.cartella / "start.ax")
        if not esito.ok:
            raise RuntimeError(f"il banco non compila:\n{esito.messaggi}")
        shutil.copy(RUNTIME, self.cartella)
        diario = self.cartella / "diario.txt"
        if diario.exists():
            diario.unlink()
        try:
            subprocess.run([str(self.cartella / "hsp3cl.exe"), "start.ax"],
                           cwd=self.cartella, timeout=secondi,
                           stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            self.piantato = False
        except subprocess.TimeoutExpired:
            self.piantato = True
        if not diario.exists():
            return ""
        return diario.read_bytes().decode("cp932", "replace")

    def pulisci(self):
        shutil.rmtree(self.cartella, ignore_errors=True)


def prova():
    """Il banco si prova su se stesso: il generatore di epiteti deve dare 20 righe."""
    b = Banco("prova")
    b.testa()
    b.pezzo("init.hsp", 141, 148)
    b.pezzo("init.hsp", 191, 212)
    b.pezzo("etc.hsp", 319, 532)
    b.coda('\n*_banco_avvio\n\tgosub *random_titleInit\n'
           '\ttappa "righe: " + length2(rnlist)\n'
           '\trepeat 20\n\t\ttappa "" + cnt + ": " + random_title(0)\n\tloop\n'
           '\ttappa "FINITO"\n\tend\n')
    d = b.esegui(secondi=60)
    righe = [r for r in d.splitlines() if r.strip()]
    print(f"banco piantato: {b.piantato}")
    print(f"righe di diario: {len(righe)}  (attese 22)")
    for r in righe[:4]:
        print("   ", r)
    b.pulisci()
    return 0 if (not b.piantato and len(righe) == 22) else 1


if __name__ == "__main__":
    sys.exit(prova())
