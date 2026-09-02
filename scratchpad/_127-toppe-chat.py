# -*- coding: utf-8 -*-
"""L'ottavo lotto della 127a: quattro righe, e una era una frase mozzata.

    chat.hsp:9402 :9403   il racconto di Mikraanesis su Sophia ed Enthumesis
    chat.hsp:17065        la SESTA riga della descrizione del modo Perdita
    blend.hsp:1257        il piede della finestra delle ricette

⚠️⚠️ `chat.hsp:17065` non e' una riga inglese qualunque: e' la CODA di una
frase le cui prime cinque righe sono gia' italiane. A schermo oggi si legge
«…Uscire senza salva ed esci option from the ESC menu will result in a penalty
at load time.» — una frase che comincia in italiano e finisce in inglese, e
nessun conteggio la distingueva dalle altre righe nude.
"""
import io
import json

from strumenti.accenti import degrada

BASE = r'C:\Games\Elona\_traduzione\sorgente\2.05-custom-gx'
SORGENTI = {}

NUDO = (
    "LETTERALE INGLESE NUDO: non passa da nessuna lang(), quindi non ha firma "
    "ne' voce di dizionario e nessun lotto puo' raggiungerlo (quinto punto "
    "cieco, nudi_en.py, 49a). "
)

LAVORO = []


def toppa(file, riga, nuova, motivo):
    LAVORO.append((file, riga, nuova, motivo))


_MIZUKI = (
    "chat.hsp:*chat_unique_mizuki, `chatval == 2`: Mikraanesis racconta come "
    "Sophia cadde dal cielo e come ne nacque Enthumesis. E' il ramo `else` di "
    "un `if ( jp )`, quindi la SORELLA GIAPPONESE C'E' ed e' :9399 — ⚠️ ma e' "
    "UNA riga sola, dove l'inglese ne ha DUE: chi ha tradotto ha spezzato il "
    "paragrafo in due `chatMore`. Le due rese italiane si spartiscono lo "
    "stesso giapponese, e il taglio resta dov'e' l'inglese, perche' i due "
    "`chatMore` sono due schermate. "
    "⭐ I nomi sono tutti riscossi dal dizionario: «Sophia» (venti voci), "
    "«Enthumesis» (quindici, e il progetto la tratta al FEMMINILE — «Enthumesis, "
    "dopo essersi separata da me»), «Sigillo Eterno» per 神の間 (quarantasette "
    "voci; l'inglese qui dice «Eternal Seal» e il giapponese 神の間, ed e' lo "
    "stesso posto). ⓘ Chi parla dice «noi»: Mikraanesis e' due divinita' in "
    "una, e chat.hsp:268 lo ha gia' fissato («Noi siamo Mikraanesis»). "
)

toppa('chat.hsp', 9402,
      'chatMore "Da piccola aveva una sete di sapere fuori dal comune. '
      'Te l\'hanno raccontata, la volta che volle sapere troppo del padre '
      'sconosciuto e fini\' in un disastro? Fu il finimondo: tutti a cercare '
      'Sophia, che era precipitata giu\' dal cielo, e quando finalmente la '
      'trovammo non poteva piu\' risalire, perche\' si era persa dietro alla sua '
      'stessa passione storta."',
      NUDO + _MIZUKI +
      "Prima delle due schermate. ⓘ 「歪んだ情熱」 e' «passione storta»: il "
      "giapponese dice *deformata*, e l'inglese «warped/twisted passions» "
      "concorda — e' la stessa immagine, ed e' la cosa che verra' strappata "
      "via nella schermata dopo, quindi la parola deve essere la stessa nelle "
      "due righe.")

toppa('chat.hsp', 9403,
      'chatMore "Alla fine le strappammo di dosso quella passione storta e la '
      'riportammo noi stessi lassu\'; ma il pezzo strappato prese forma umana e '
      'comincio\' a muoversi per conto suo. Distruggere un doppio nato da nostra '
      'sorella non ce la sentivamo, cosi\' lo lasciammo vivere libero, ed e\' '
      'diventato Enthumesis. L\'hai combattuta, quindi lo sai: e\' la dea del '
      'caos che stava nel Sigillo Eterno. Davvero, quella bambina non smette '
      'mai di dare da fare."',
      NUDO + _MIZUKI +
      "Seconda delle due schermate. ⚠️ «L'hai combattuta» concorda con "
      "ENTHUMESIS, non con chi legge: il participio ha per oggetto lei, e il "
      "sesso del giocatore non entra. ⓘ L'inglese chiude con una frase che il "
      "giapponese non ha («Inquisitive bookworm or all-powerful goddess…»); "
      "「本当に、手がかかる子」 e' «quella bambina non smette mai di dare da "
      "fare», ed e' il giapponese ad arbitrare.")

toppa('chat.hsp', 17065,
      's = "dal menu ESC comporta un limite al caricamento."',
      NUDO +
      "chat.hsp:*com_change_gamemode_loop, la descrizione del modo di gioco "
      "«Perdita». ⚠️⚠️ NON E' UNA RIGA A SE': e' la SESTA e ultima di una frase "
      "spezzata su sei `mes`, e le prime cinque (:17043-:17061) passano tutte "
      "da `lang()` e sono italiane da sessioni. A schermo oggi si legge «…"
      "Uscire senza salva ed esci option from the ESC menu will result in a "
      "penalty at load time.»: una frase che comincia in italiano e finisce in "
      "inglese. ⚠️ Il conto delle righe nude non poteva distinguerla — per lui "
      "e' un letterale intatto come gli altri — e a vederla serve leggere il "
      "blocco. ⭐ «Penalty at load time» -> «un limite al caricamento» e' "
      "riscossa da :17049, che rende la stessa espressione dentro la "
      "descrizione del modo «Anormale», tredici righe piu' su. ⓘ Sta dentro un "
      "`if ( en )` senza gemello giapponese, perche' in giapponese la frase "
      "sta in cinque righe e in inglese ne vuole sei: la sesta esiste solo per "
      "la lunghezza, e in italiano serve lo stesso.")

toppa('blend.hsp', 1257, 's = "" + listmax + " ricette"',
      NUDO +
      "blend.hsp:*com_blend_recipe_loop, il piede della finestra che sceglie "
      "la ricetta: quante ne conosci. ⭐ E' la gemella di `\" items\"` -> "
      "«\" oggetti\"» — stessa forma, stessa finestra di sistema, stessa "
      "posizione (`pos wx + 130, wy + wh - 65 - wh \\ 8`), e nello stesso file "
      "l'altra e' gia' stata resa in questa sessione.")

# ---------------------------------------------------------------------------


def righe_di(nome):
    if nome not in SORGENTI:
        SORGENTI[nome] = io.open(BASE + '\\' + nome, encoding='cp932').read().split('\n')
    return SORGENTI[nome]


def un_byte_solo(c):
    try:
        return len(c.encode('cp932')) == 1
    except UnicodeEncodeError:
        return False


toppe = []
for nome, n, nuova_grezza, motivo in LAVORO:
    righe = righe_di(nome)
    originale = righe[n - 1]
    indent = originale[:len(originale) - len(originale.lstrip())]
    nuova = indent + degrada(nuova_grezza)
    cattivi = sorted({c for c in nuova if c != '♪' and not un_byte_solo(c)})
    if cattivi:
        raise SystemExit('{}:{}: caratteri a due byte {}'.format(nome, n, cattivi))
    if nuova == originale:
        raise SystemExit('{}:{}: la toppa non cambierebbe niente'.format(nome, n))
    quante = sum(1 for r in righe if r == originale)
    if quante != 1:
        raise SystemExit('{}:{}: la riga compare {} volte'.format(nome, n, quante))
    toppe.append({'file': nome, 'cerca': originale, 'sostituisci': nuova,
                  'motivo': motivo})
    print('{:12s}{:6d}  {}'.format(nome, n, nuova.strip()[:72]))

dati = ''.join(json.dumps(t, ensure_ascii=False) + '\n' for t in toppe).encode('utf-8')
with io.open('lavoro/toppe-127-chat.jsonl', 'wb') as f:
    f.write(dati)
print('{} toppe -> lavoro/toppe-127-chat.jsonl'.format(len(toppe)))
