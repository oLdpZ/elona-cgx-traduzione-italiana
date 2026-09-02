# -*- coding: utf-8 -*-
"""Le quattro condizioni che il referto della 129a ha trovato maturate.

Sono le prime quattro che qualcuno guarda da quando i rinvii esistono, e nessuna
delle quattro si sarebbe vista rileggendo la prosa: due sono **gemelle vive**
(una firma rinviata perche' morta in un sito, e viva in un altro), due sono
**toppe arrivate** dopo il rinvio che le aspettava.

    1. command.hsp ` level`   RESA. La firma vive a :2956 (ramo `if ( jp )`,
       morta) e a **:10710, viva**, nel pannello del personaggio: accanto
       all'etichetta gia' italiana «Potenza» il gioco scrive «N level».
       Diventa « liv.», come `" Lv"` -> `" liv."` di :17435 e come dice il
       glossario (`Level` -> `Livello`, abbreviato `Lv.`).

    2. command.hsp ` Plat`    RESTA RINVIATA, ma con la condizione giusta. La
       gemella viva e' :3067, dentro il ramo `else` del diario — quello che
       stampa tutto in **inglese nudo** e che nessuno ha ancora toppato.
       Renderla adesso metterebbe una parola italiana in mezzo a una riga
       inglese: aspetta quella toppa, e il referto lo dira' il giorno in cui
       arriva. ⚠️ Il vecchio motivo diceva che la `lang()` «non viene valutata
       mai», e per :3067 era **falso**.

    3. item_func.hsp ` grown ` La toppa che aspettava C'E'. Il rinvio diceva
       «dipende da `_weight()`, si fa nello stesso lotto»: quel lotto e' stato
       fatto (`Fase 1: la taglia e la qualita' del manoscritto`) e la riga :974
       nella build dice gia' « di taglia ».

    4. item_func.hsp `:1386`   Idem: il giunto del materiale e' passato a
       `mtcomplemento` con la toppa `Il giunto del materiale non e' uno solo:
       sette elidono`. ⚠️ **La ripresa della 128a dava questo rinvio per
       «ancora vero»**, cercandolo a mano: e' il quarto della famiglia che
       quella sessione diceva di aver trovato, ed era gia' chiuso.

Si lancia una volta sola.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strumenti import estrai, percorsi  # noqa: E402

RESA = ' liv.'


def _voce_del_sito(nome_file: str, firma: str, riga_attesa: int) -> dict:
    """La voce di dizionario del sito, presa da `estrai`: non si scrive a mano.

    I campi sono undici e tre sono derivati (`en_grezzo`, `tipo`, `contesto`):
    ricopiarli a mano da una voce vicina e' il modo di scrivere una firma che
    non corrisponde a niente.
    """
    for voce in estrai.estrai_da_file(percorsi.SORGENTE_HSP / nome_file):
        if voce['firma'] == firma and voce['riga'] == riga_attesa:
            return voce
    raise SystemExit('sito non trovato: %s:%d' % (nome_file, riga_attesa))


def togli_rinvio(indice_atteso: int, en_atteso: str) -> dict:
    percorso = percorsi.PROGETTO / 'rinviate.jsonl'
    righe = [r for r in percorso.read_text(encoding='utf-8').splitlines() if r.strip()]
    voce = json.loads(righe[indice_atteso - 1])
    if voce['en'] != en_atteso:
        raise SystemExit('la voce %d non e\' %r ma %r' % (indice_atteso, en_atteso, voce['en']))
    del righe[indice_atteso - 1]
    percorso.write_text('\n'.join(righe) + '\n', encoding='utf-8')
    return voce


def cambia_rinvio(indice_atteso: int, en_atteso: str, condizione: dict, motivo: str) -> None:
    percorso = percorsi.PROGETTO / 'rinviate.jsonl'
    righe = [r for r in percorso.read_text(encoding='utf-8').splitlines() if r.strip()]
    voce = json.loads(righe[indice_atteso - 1])
    if voce['en'] != en_atteso:
        raise SystemExit('la voce %d non e\' %r ma %r' % (indice_atteso, en_atteso, voce['en']))
    voce['rinviata_a'] = condizione.pop('rinviata_a')
    voce['motivo'] = voce['motivo'] + motivo
    voce['condizione'] = condizione
    righe[indice_atteso - 1] = json.dumps(voce, ensure_ascii=False)
    percorso.write_text('\n'.join(righe) + '\n', encoding='utf-8')


def aggiungi_resa(nome_file: str, firma: str, riga: int, resa: str) -> None:
    percorso = percorsi.DIZIONARIO / (nome_file + '.jsonl')
    voci = [json.loads(r) for r in percorso.read_text(encoding='utf-8').splitlines() if r.strip()]
    if any(v['firma'] == firma for v in voci):
        raise SystemExit('la firma e\' gia\' nel dizionario')
    nuova = _voce_del_sito(nome_file, firma, riga)
    nuova['it'] = resa
    # il file sta in ordine di riga, e ci resta: chi lo legge a occhio cammina
    # con il sorgente aperto di fianco
    posto = next((i for i, v in enumerate(voci) if v['riga'] > riga), len(voci))
    voci.insert(posto, nuova)
    percorso.write_text(
        '\n'.join(json.dumps(v, ensure_ascii=False) for v in voci) + '\n', encoding='utf-8')
    print('  resa aggiunta a %s, riga %d: %r -> %r' % (percorso.name, riga, nuova['en'], resa))


def main() -> int:
    # --- 2, 3, 4: le tre che restano rinviate, con la condizione giusta ------
    cambia_rinvio(
        28, ' Plat',
        {'rinviata_a': 'con la toppa che rendera\' il ramo `else` del diario',
         'tipo': 'attende_toppa', 'siti': ['command.hsp:3067']},
        motivo=(
            ' ⚠️⚠️⚠️ CORRETTO NELLA 129a: PER QUESTA FIRMA IL MOTIVO QUI SOPRA '
            'ERA FALSO. La firma non vive solo a :2982 dentro il ramo `if ( jp )`: '
            'vive **anche a :3067**, nel ramo `else`, dove la `lang()` viene '
            'valutata eccome e il giocatore italiano legge « Plat». Il rinvio '
            'resta — renderla adesso metterebbe una parola italiana in mezzo a '
            '«@BL   Total Platinum: 12 Plat», che e\' inglese per il resto — ma '
            'la condizione non e\' piu\' «e\' morta»: e\' «aspetta la toppa che '
            'rende il ramo else», e il referto '
            '`scratchpad/_129-condizioni-dei-rinvii.py` la misura.'))

    cambia_rinvio(
        85, ' grown ',
        {'rinviata_a': 'nessuna fase: risolta da toppa (item_func.hsp:974)',
         'tipo': 'risolta_da_toppa'},
        motivo=(
            ' ✅ CHIUSO, E LA CONDIZIONE ERA MATURA DA UN PEZZO: il lotto dei '
            'modificatori di qualita\' e\' stato fatto (commit «Fase 1: la taglia '
            'e la qualita\' del manoscritto») e la toppa su :974 rende gia\' '
            '« di taglia », accordata con le dieci rese di `_weight`. Nessuno '
            'era tornato a leggere il rinvio: l\'ha trovato il referto della 129a.'))

    cambia_rinvio(
        100, ' ',
        {'rinviata_a': 'nessuna fase: risolta da toppa (item_func.hsp:1386)',
         'tipo': 'risolta_da_toppa'},
        motivo=(
            ' ✅ CHIUSO: la toppa che sposta la concatenazione esiste (commit '
            '«Il giunto del materiale non e\' uno solo: sette elidono»), e :1386 '
            'nella build passa per `mtcomplemento`. ⚠️ La ripresa della 128a '
            'dava questo rinvio per «ancora vero», cercandolo a mano fra i 114: '
            'era gia\' chiuso, e a dirlo e\' bastato guardare la build invece '
            'della prosa.'))

    # --- 1: l'unica che diventa lavoro --------------------------------------
    voce = togli_rinvio(103, ' level')
    aggiungi_resa('command.hsp', voce['firma'], 10710, RESA)
    print('  rinvio tolto: %r (era %r)' % (voce['en'], voce['rinviata_a']))
    return 0


if __name__ == '__main__':
    sys.exit(main())
