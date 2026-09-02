# -*- coding: utf-8 -*-
"""La condizione di un rinvio smette di stare in prosa e diventa un numero.

⚠️⚠️⚠️ **IL GUASTO CHE QUESTO REFERTO ESISTE PER NON RIFARE.** Nella 128a si e'
scoperto che **quattro rami del gioco erano morti** — il ballo nella sala delle
feste durava 4 turni invece di 41, scavare dentro una nave dava minerali invece
di spazzatura — e a ucciderli era stata la traduzione. Tre di quei quattro
guasti erano **rinvii con una condizione**, e la condizione era **maturata da
sessioni**:

    rinviate.jsonl, dalla 27a e dalla 60a:
    «Va tradotta INSIEME a map_rand.hsp, come evold/evname con
     db_creature.hsp: non prima.»

Chi assegna il nome della mappa e' stato tradotto in una sessione qualunque, e
nessuno e' tornato a leggere il rinvio.

> Un rinvio con una condizione non e' una decisione presa: e' una decisione
> **rimandata a un evento che nessuno osserva**. La condizione sta in prosa,
> dentro un campo `motivo`, e nessuno strumento la valuta.

⚠️⚠️ **E il modo di cercarle a mano NON FUNZIONA.** La 128a proponeva un `grep`
sulla prosa — `INSIEME|non prima|ASSEGNA|CONFRONT` — e provato sulle 114 voci
pesca **piu' di sessanta righe su centoquattordici**, perche' «se » compare in
quasi ogni motivo. Un filtro che lascia passare meta' dell'insieme non e' un
filtro: e' l'elenco completo con un passaggio in piu'.

---

## IL CAMPO `condizione`

Ogni voce di `rinviate.jsonl` porta un oggetto `condizione` con un `tipo`, e il
tipo dice **che cosa questo referto deve andare a misurare**. La prosa del
`motivo` resta dov'e', per chi legge; il campo e' per la macchina.

    riga_morta        la riga e' spenta nel sorgente — una delle cinque
                      famiglie che il progetto conosce (`;`, `//`, `/* */`,
                      ramo `if ( jp )`, `if ( FALSE )`). MATURA se torna viva.
    morta_per_flusso  la riga e' VIVA, ed e' morto **chi la stampa**: le sigle
                      delle statistiche di `item_func.hsp` si compongono
                      davvero, e il `mes` che le scriverebbe e' commentato
                      venti righe piu' sotto. E' la sesta famiglia di riga
                      morta, e l'unica che non si legge nel posto dove la riga
                      sta: i `siti` dicono chi deve restare spento, e MATURA se
                      uno di quelli torna vivo.
    risolta_da_toppa  una toppa parla gia' di questa riga. ROTTA se la toppa
                      sparisce: il rinvio tornerebbe aperto in silenzio.
    attende_toppa     aspetta una toppa che ancora non esiste.
                      MATURA il giorno in cui qualcuno la scrive.
    attende_resa      aspetta che un ALTRO sito sia reso — la famiglia che ha
                      ucciso i quattro rami. MATURA appena la build di quel
                      sito smette di dire l'inglese del sorgente.
    attende_monte     aspetta che monte cambi il sorgente pinnato.
                      MATURA se quella riga non e' piu' spenta a monte.
    mai               non c'e' nessuna condizione: non c'e' testo in nessuna
                      delle due lingue. E' l'unico tipo che non si misura, e
                      per questo pretende una `nota` che dica perche'.

`siti` porta gli `file.hsp:riga` su cui `attende_resa` e `attende_monte` si
misurano. Per gli altri tipi il sito e' **la voce stessa**: la firma si cerca
nel sorgente e da' le sue righe.

## I TRE NUMERI ATTESI

    MATURATE            0   <- il cancello: una condizione maturata e' lavoro
    ROTTE               0   <- una toppa sparita sotto un rinvio chiuso
    SENZA CONDIZIONE    0   <- una voce che nessuno ha classificato

⚠️ Il terzo conta quanto i primi due. Una voce senza `condizione` non e' una
voce senza condizione: e' una voce **che nessuno guarda**, ed e' esattamente lo
stato in cui stavano tutt'e 114 il giorno prima di questo referto.

    PYTHONIOENCODING=utf-8 PYTHONPATH=. python scratchpad/_129-condizioni-dei-rinvii.py
    ... --elenco            tutte le voci, tipo per tipo
"""
import collections
import contextlib
import importlib.util
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strumenti import commenti, estrai, percorsi  # noqa: E402

_QUI = os.path.dirname(os.path.abspath(__file__))

# ⚠️ Il vocabolario sta in `strumenti/estrai.py`, non qui: e' li' che
# `carica_rinviate` lo pretende su ogni estrazione, e due elenchi che devono
# restare uguali per disciplina restano uguali finche' qualcuno se ne ricorda.
TIPI = estrai.TIPI_CONDIZIONE


def _carica(nome: str, percorso: str):
    spec = importlib.util.spec_from_file_location(nome, percorso)
    modulo = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(modulo)
    return modulo


# ⚠️ Tutt'e due stampano il loro referto all'import: qui servono solo le due
# funzioni, e il loro referto in mezzo a questo sarebbe rumore che nasconde i
# numeri veri.
_ramo_jp = _carica('lang_nel_ramo_jp', os.path.join(_QUI, 'lang-nel-ramo-jp.py'))
_spente = _carica('spente_da_una_costante',
                  os.path.join(_QUI, '_126-spente-da-una-costante.py'))


class Sorgente:
    """Il sorgente e la build, letti una volta sola per file."""

    def __init__(self):
        self._righe = {}
        self._build = {}
        self._morte = {}
        self._siti = {}

    def righe(self, nome: str) -> list:
        if nome not in self._righe:
            testo = (percorsi.SORGENTE_HSP / nome).read_text(encoding='cp932')
            self._righe[nome] = estrai.spezza_righe(testo)[0]
        return self._righe[nome]

    def righe_build(self, nome: str) -> list:
        if nome not in self._build:
            testo = (percorsi.BUILD_HSP / nome).read_text(encoding='cp932')
            self._build[nome] = estrai.spezza_righe(testo)[0]
        return self._build[nome]

    def siti_per_firma(self, nome: str) -> dict:
        """firma -> [(numero_riga, colonna_di_lang)] nel sorgente."""
        if nome not in self._siti:
            testo = (percorsi.SORGENTE_HSP / nome).read_text(encoding='cp932')
            indice = collections.defaultdict(list)
            for sito in estrai.siti(testo):
                indice[sito[1]].append((sito[0], sito[7]))
            self._siti[nome] = indice
        return self._siti[nome]

    def perche_morta(self, nome: str, numero: int, colonna: int):
        """La famiglia di riga morta che spegne questo sito, o None se e' vivo.

        Le cinque famiglie sono quelle che il progetto ha gia' nominato una per
        una: `;` (rete 6), `/* */` (37a), ramo `if ( jp )` (45a), `if ( 0 )`
        (46a) e `//` (100a). Qui stanno insieme perche' a un rinvio non importa
        **quale** lo spenga: importa che sia spento.
        """
        if nome not in self._morte:
            righe = self.righe(nome)
            self._morte[nome] = (
                commenti.righe_in_commento(percorsi.SORGENTE_HSP / nome),
                _ramo_jp.righe_nel_ramo_jp(righe),
                _spente.righe_spente(righe),
                righe_sotto_guardia_composta(righe),
            )
        blocco, ramo, costante, composta = self._morte[nome]
        if numero in blocco:
            return 'commento di blocco /* */'
        if numero in ramo:
            return 'ramo if ( jp )'
        if numero in composta:
            return 'guardia composta con `& jp`'
        if numero in costante:
            return 'if ( FALSE )'
        riga = self.righe(nome)[numero - 1]
        barre = commenti.colonna_commento_riga(riga)
        if barre is not None and barre < colonna:
            return 'commento di riga //'
        punto = _colonna_punto_e_virgola(riga)
        if punto is not None and punto < colonna:
            return 'commento di riga ;'
        return None

    def cambiata_nella_build(self, nome: str, numero: int) -> bool:
        """Vero se la riga del sorgente non si ritrova piu' nella build.

        ⚠️ **Non si confrontano i numeri di riga**: le toppe possono aggiungere
        righe, e `map.hsp` nella build ne ha **cinque piu'** del sorgente. Si
        confrontano le **occorrenze del testo esatto**, cosi' che una riga
        ripetuta e cambiata in un punto solo si veda lo stesso.
        """
        testo = self.righe(nome)[numero - 1]
        return self.righe_build(nome).count(testo) < self.righe(nome).count(testo)


_GUARDIA_COMPOSTA = re.compile(r'^\s*if\s*\(.*&\s*jp\s*\)\s*\{\s*$')


def _saldo_graffe(riga: str) -> int:
    """Graffe aperte meno chiuse, **fuori dalle stringhe**.

    Una graffa dentro un letterale chiuderebbe un blocco che nel codice e'
    ancora aperto, e da li' in poi il conto sarebbe sfalsato per tutto il file.
    """
    dentro = estrai._dentro_stringa(riga)
    saldo = 0
    for indice, carattere in enumerate(riga):
        if dentro[indice]:
            continue
        if carattere == '{':
            saldo += 1
        elif carattere == '}':
            saldo -= 1
    return saldo


def righe_sotto_guardia_composta(righe: list) -> set:
    """I numeri di riga dentro un `if ( ... & jp ) {`.

    ⚠️ E' la **settima** famiglia di riga morta, e nessuno strumento la vedeva:
    `lang-nel-ramo-jp.py` riconosce solo `^if ( jp ) {`, e la sua stessa
    intestazione lo dichiara — «restano fuori due guardie composte». Le nove
    parti del corpo di `item_func.hsp:1034` stanno esattamente li' sotto
    (`if ( inv(...) == ITEM_ID_NECRO_PARTS & jp ) {`), e per questo il referto
    le dava per vive.

    Il conto delle graffe basta perche' in HSP l'apertura sta a fine riga: si
    entra sulla riga della guardia e si esce quando il saldo torna a zero.
    """
    dentro = set()
    profondita = 0
    attivo = False
    for numero, riga in enumerate(righe, 1):
        if not attivo and _GUARDIA_COMPOSTA.match(riga):
            attivo = True
            profondita = 0
        if attivo:
            profondita += _saldo_graffe(riga)
            dentro.add(numero)
            if profondita <= 0:
                attivo = False
    return dentro


def _colonna_punto_e_virgola(riga: str):
    """La colonna del `;` che spegne il resto della riga, o None.

    Il `;` si cerca **fuori dalle stringhe**, se no un punto e virgola dentro
    un letterale spegnerebbe la riga che lo contiene.
    """
    dentro = estrai._dentro_stringa(riga)
    for indice, carattere in enumerate(riga):
        if carattere == ';' and not dentro[indice]:
            return indice
    return None


def toppe_per_file() -> dict:
    percorso = percorsi.PROGETTO / 'toppe.jsonl'
    per_file = collections.defaultdict(list)
    for riga in percorso.read_text(encoding='utf-8').splitlines():
        if not riga.strip():
            continue
        voce = json.loads(riga)
        per_file[voce['file']].append(voce)
    return per_file


def coperta_da_toppa(toppe: list, testo_riga: str) -> bool:
    """Vero se una toppa del file nomina questa riga nel suo `cerca`.

    ⚠️ E' una copertura per **testo**, non per numero di riga: le toppe cercano
    e sostituiscono stringhe, e una toppa a blocco porta dentro piu' righe. Il
    limite e' che una riga non unica puo' risultare coperta da una toppa che
    parla di una sua gemella; per un rinvio va bene lo stesso, perche' la
    domanda e' «esiste una toppa che parla di questa forma».
    """
    nudo = testo_riga.strip()
    if not nudo:
        return False
    return any(nudo in toppa['cerca'] for toppa in toppe)


def _siti_dichiarati(voce: dict) -> list:
    fuori = []
    for sito in voce.get('condizione', {}).get('siti', []):
        nome, _, numero = sito.rpartition(':')
        fuori.append((nome, int(numero)))
    return fuori


def valuta(voce: dict, sorgente: Sorgente, toppe: dict) -> tuple:
    """(esito, dettaglio). Esito in: ok, MATURATA, ROTTA, SENZA-CONDIZIONE."""
    condizione = voce.get('condizione')
    if not condizione or condizione.get('tipo') not in TIPI:
        return 'SENZA-CONDIZIONE', 'nessun campo `condizione` valido'

    tipo = condizione['tipo']
    nome = voce['file']
    righe_del_sito = sorgente.siti_per_firma(nome).get(voce['firma'], [])
    if not righe_del_sito:
        return 'ROTTA', 'la firma non si trova piu\' nel sorgente'

    if tipo == 'mai':
        if not condizione.get('nota'):
            return 'SENZA-CONDIZIONE', '`mai` senza `nota`: non si misura e non si spiega'
        return 'ok', condizione['nota']

    if tipo == 'riga_morta':
        vive = []
        perche = []
        for numero, colonna in righe_del_sito:
            motivo = sorgente.perche_morta(nome, numero, colonna)
            if motivo is None:
                vive.append(numero)
            else:
                perche.append(motivo)
        if vive:
            return ('MATURATA',
                    'la riga e\' viva a %s' % ', '.join('%s:%d' % (nome, n) for n in vive))
        comuni = collections.Counter(perche).most_common(1)[0][0]
        return 'ok', '%d righe spente [%s]' % (len(righe_del_sito), comuni)

    if tipo in ('risolta_da_toppa', 'attende_toppa'):
        # ⚠️⚠️ **Non si guarda l'elenco delle toppe, si guarda la BUILD.** Il
        # primo tentativo cercava la riga dentro il `cerca` di una toppa, e
        # sbagliava su **sei rinvii su ventiquattro**: una toppa puo' cercare un
        # frammento invece della riga intera, o riscrivere il blocco intorno.
        # La domanda vera non e' «esiste una toppa che parla di questa riga»,
        # e' «quel che il giocatore riceve e' ancora l'inglese del sorgente».
        # E' la stessa lezione della 128a, dall'altro lato: si misura l'esito,
        # non l'intenzione.
        siti = _siti_dichiarati(voce) or [(nome, n) for n, _ in righe_del_sito]
        cambiate = ['%s:%d' % (f, n) for f, n in siti if sorgente.cambiata_nella_build(f, n)]
        if tipo == 'risolta_da_toppa':
            if not cambiate:
                return 'ROTTA', ('la riga arriva nella build intatta: quel che '
                                 'chiudeva il rinvio non c\'e\' piu\'')
            return 'ok', 'la build la cambia a %s' % ', '.join(cambiate)
        if cambiate:
            return 'MATURATA', 'quel che aspettava e\' arrivato: la build cambia %s' % ', '.join(cambiate)
        return 'ok', 'la riga arriva nella build intatta: la toppa attesa non c\'e\' ancora'

    if tipo == 'attende_resa':
        siti = _siti_dichiarati(voce)
        if not siti:
            return 'SENZA-CONDIZIONE', '`attende_resa` senza `siti`: non si sa che cosa aspetta'
        rese = ['%s:%d' % (f, n) for f, n in siti if sorgente.cambiata_nella_build(f, n)]
        if rese:
            return 'MATURATA', 'il sito atteso e\' stato reso: %s' % ', '.join(rese)
        return 'ok', 'i %d siti attesi sono ancora inglesi nella build' % len(siti)

    if tipo in ('attende_monte', 'morta_per_flusso'):
        siti = _siti_dichiarati(voce)
        if not siti:
            return 'SENZA-CONDIZIONE', '`%s` senza `siti`: non si sa che cosa aspetta' % tipo
        vive = []
        for file_sito, numero in siti:
            riga = sorgente.righe(file_sito)[numero - 1]
            # ⚠️ Qui il sito dichiarato non e' una `lang()`: non c'e' una
            # colonna d'argomento da cui misurare. Si guarda **tutta** la riga,
            # cioe' si chiede se un `;` o un `//` la spenga dal primo carattere
            # utile in poi.
            colonna = len(riga)
            if sorgente.perche_morta(file_sito, numero, colonna) is None:
                vive.append('%s:%d' % (file_sito, numero))
        if vive:
            if tipo == 'attende_monte':
                return 'MATURATA', 'monte ha riacceso %s' % ', '.join(vive)
            return 'MATURATA', 'chi la stampa e\' tornato vivo: %s' % ', '.join(vive)
        quale = 'spenti a monte' if tipo == 'attende_monte' else 'spenti: nessuno la stampa'
        return 'ok', 'i %d siti dichiarati sono ancora %s' % (len(siti), quale)

    raise AssertionError('tipo non gestito: %s' % tipo)


def carica_rinvii() -> list:
    percorso = percorsi.PROGETTO / 'rinviate.jsonl'
    return [json.loads(r) for r in percorso.read_text(encoding='utf-8').splitlines() if r.strip()]


def referto(rinvii: list) -> list:
    sorgente = Sorgente()
    toppe = toppe_per_file()
    return [(voce,) + valuta(voce, sorgente, toppe) for voce in rinvii]


def main(argv: list) -> int:
    elenco = '--elenco' in argv
    rinvii = carica_rinvii()
    esiti = referto(rinvii)

    per_tipo = collections.Counter(
        (v.get('condizione') or {}).get('tipo') or '(nessuna)' for v, _, _ in esiti)
    print('=== I RINVII PER TIPO DI CONDIZIONE (%d voci)' % len(rinvii))
    for tipo in TIPI:
        if per_tipo.get(tipo):
            print('  %-18s %4d' % (tipo, per_tipo[tipo]))
    if per_tipo.get('(nessuna)'):
        print('  %-18s %4d' % ('(nessuna)', per_tipo['(nessuna)']))

    maturate = [e for e in esiti if e[1] == 'MATURATA']
    rotte = [e for e in esiti if e[1] == 'ROTTA']
    senza = [e for e in esiti if e[1] == 'SENZA-CONDIZIONE']

    if elenco:
        print()
        print('=== TUTTE LE VOCI')
        for voce, esito, dettaglio in esiti:
            tipo = (voce.get('condizione') or {}).get('tipo', '-')
            print('  %-14s %-18s %-22s %s' % (
                esito if esito != 'ok' else '', tipo, voce['file'],
                (voce['en'][:40] + ' | ' + dettaglio)))

    for titolo, gruppo in (('MATURATE — la condizione si e\' avverata: e\' LAVORO', maturate),
                           ('ROTTE — quel che chiudeva il rinvio non c\'e\' piu\'', rotte),
                           ('SENZA CONDIZIONE — nessuno le guarda', senza)):
        if gruppo:
            print()
            print('=== %s' % titolo)
            for voce, _, dettaglio in gruppo:
                print('  %-22s %-45s %s' % (voce['file'], voce['en'][:45], dettaglio))

    print()
    print('--- MATURATE         : %4d   (atteso: 0)' % len(maturate))
    print('--- ROTTE            : %4d   (atteso: 0)' % len(rotte))
    print('--- SENZA CONDIZIONE : %4d   (atteso: 0)' % len(senza))
    print()
    print('=== PERCHE\' LO ZERO E\' ZERO — che cosa tiene chiusa ogni voce')
    print('  (uno zero senza la ragione dello zero non e\' un risultato)')
    ragioni = collections.Counter(dettaglio.split('[')[-1].rstrip(']')
                                  if v.get('condizione', {}).get('tipo') == 'riga_morta'
                                  else v['condizione']['tipo']
                                  for v, e, dettaglio in esiti if e == 'ok')
    for ragione, quante in ragioni.most_common():
        print('  %-34s %4d' % (ragione, quante))

    print()
    print('ⓘ Lo zero delle MATURATE non vuol dire «nessun rinvio ha una condizione»:')
    print('  %d voci su %d ne portano una che si misura davvero (tutte tranne le'
          % (len(rinvii) - per_tipo.get('mai', 0) - per_tipo.get('(nessuna)', 0), len(rinvii)))
    print('  `mai`). Vuol dire che oggi nessuna di quelle condizioni e\' avverata.')

    return 1 if (maturate or rotte or senza) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
