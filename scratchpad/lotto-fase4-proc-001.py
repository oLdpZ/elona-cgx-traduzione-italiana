# -*- coding: utf-8 -*-
"""Lotto fase4-proc-001: le reazioni degli dei alla predica (proc.hsp 1716-1800).

Otto dei piu' la reazione generica della folla e il messaggio di conversione.
⚠️ Il registro di ognuno degli otto e' gia' deciso in db_creature.hsp e qui si
**segue**, non si ridecide: vedi le note voce per voce.
"""
import collections, glob, io, json

RESE = {
    # --- <Mani>, dio delle macchine. Registro: dichiarative asciutte e
    #     minuscole (db_creature 101522: «Un risultato prevedibile.»,
    #     «Avvio ricerca bersagli.»). ⚠️ Niente maiuscolo da robot: la 31ª ha
    #     deciso che il maiuscolo lo porta il katakana, e Mani parla giapponese
    #     normale.
    (1716, 'You could say this is a stunning logical development.'):
        "Un'argomentazione impeccabile, direi.",
    (1716, "Oh, I'm recording this one!"):
        'Sto registrando tutto, ovviamente.',

    # --- <Lulwy>, dea del vento. Registro: alterigia femminile, disprezzo per
    #     i mortali (db_creature 100761-100851).
    (1724, 'Oh, you do get it.'):
        'Ma guarda, hai capito benissimo.',
    # ⚠️ 「いい子ね」 e' «brava/bravo», che concorderebbe col giocatore. Sostituito
    #    con «Cosi' mi piaci», che vale per entrambi i generi. 愚民 = «plebaglia»,
    #    che tiene il disprezzo di Lulwy.
    (1724, 'What a good child. Teach the ignorant more.'):
        'Così mi piaci. Istruisci ancora la plebaglia.',

    # --- <Itzpalt>, dio degli elementi. Registro: aulico e arcaico
    #     (db_creature 87215-87221: «Dev'essere dura, per un mortale.»,
    #     «Torna agli elementi.»).
    (1732, 'You all, chant my name higher!'):
        'Tutti, invocate alto il mio nome.',
    (1732, 'Complements are seemingly unnecessary.'):
        'A quanto pare non c\'è nulla da aggiungere.',

    # --- <Ehekatl>, dea della fortuna. Registro: infantile, felino, RIPETE la
    #     coda della frase (db_creature 101187: 「なっちゃった！なっちゃった！」 ->
    #     «Di muoversi! Di muoversi!»). Qui 「くれてるの？くれてるの？」 e' la stessa
    #     figura e si rende allo stesso modo.
    (1740, 'E-hehe'):
        'Ehehee...',
    (1740, 'Are you praising me? Really, really?'):
        'Mi stai facendo un complimento? Un complimento?',

    # --- <Opatos>, dio della terra. Le sue risate sono gia' rese in
    #     db_creature 100929-100935: フハッハハアッ -> «Fuahhahaah!». Si segue
    #     quell'ortografia.
    (1748, "Muhan! That's the tune!"):
        'Fuaah! Così si fa!',
    (1748, 'Mwahahahan!!!'):
        'Fuahahahahaaan!!!',

    # --- <Jure>, dea della guarigione. Registro tsundere, con la balbuzie resa
    #     per raddoppio della prima lettera (db_creature 100593: 「さ、寂しく」 ->
    #     «N-non è che mi mancassi, eh!»).
    (1756, "Tsk... Don't tell me things like that!"):
        "Ehi... non c'è bisogno di dire anche questo!",
    # ⚠️ L'inglese ROVESCIA il giapponese: 「恥ずかしいじゃない」 con じゃない
    #    confermativo vuol dire «è imbarazzante, no?», non «I'm not embarrassed».
    #    Arbitra il giapponese, e il registro di Jure conferma.
    (1756, "W-What? I'm not embarrassed..."):
        'C-che c\'è... è imbarazzante...',

    # --- <Kumiromi>, dio del raccolto. Registro: timido, frasi sospese
    #     (db_creature 101438: «Ecco... il raccolto delle anime...»).
    (1764, 'I will... teach you more about me...'):
        'Su di me... ti dico ancora qualcosa...',
    (1764, "Fufu... I'm so happy..."):
        'Fufu... che gioia...',

    # --- <Yacatect>, dea della ricchezza. Registro: colloquiale e sbrigativo
    #     (db_creature 87388-87471: «Facile facile.», «Ma piantala, va'!»).
    #     Il kansai-ben si rende con l'italiano parlato, non con un dialetto.
    (1772, 'Hmm... Am I embarrassed...?'):
        'Mh... e dai, mi fai arrossire...',
    # お布施 e' gia' «obolo» in db_creature 87382 («l'o-bo-lo»).
    (1772, 'Yes, yes. Donations right this way!'):
        'Sì sì, gli oboli da questa parte!',

    # --- la reazione generica, quando chi ascolta non e' un dio
    # ⚠️ COPIATA da proc.hsp:850, dove lo stesso giapponese descrive il pubblico
    #    di un'esibizione. La rete 3 l'ha segnalata: qui la resa vecchia regge
    #    (stessa figura, pubblico che reagisce bene) e divergere avrebbe creato
    #    una divergenza che nessuna guardia vede — `--divergenti` legge solo
    #    db_creature.hsp.
    (1791, ' lets out a cheer.'):
        'name(tc) + " applaude."',
    (1791, 'I see.'):
        'Capisco.',
    (1791, "That's amazing!"):
        'Magnifico!',
    (1791, ' nods in agreement.'):
        'name(tc) + " annuisce di continuo."',

    # ⚠️ «si è convertito» concorderebbe con name(tc), che e' una creatura
    #    qualunque. Presente indicativo: nessun participio, nessun accordo.
    (1800, ' converted to  due to your inspiring words!'):
        'name(tc) + " si commuove e si converte a " + godname(cdata(CDATA_GOD, tc)) + "!"',
}

USCITA = 'lavoro/fase4-proc-001.jsonl'
DA, A = 1716, 1800

tutte = [json.loads(l) for l in io.open('lavoro/_proc.jsonl', encoding='utf-8') if l.strip()]
voci = [v for v in tutte if DA <= v['riga'] <= A]

errori = []

# rete 0: la chiave identifica una voce sola
for k, n in collections.Counter((v['riga'], v['en']) for v in voci).items():
    if n > 1:
        errori.append(f'rete 0: la chiave {k} identifica {n} voci, non una')

# rete 1: nessuna voce senza resa
indice = {(v['riga'], v['en']): v for v in voci}
for v in voci:
    if (v['riga'], v['en']) not in RESE:
        errori.append(f"rete 1: voce senza resa -> riga {v['riga']}  en={v['en']!r}")

# rete 2: nessuna resa che non aggancia niente
for k in RESE:
    if k not in indice:
        errori.append(f'rete 2: resa che non aggancia nessuna voce -> {k}')

if errori:
    for e in errori:
        print(e)
    raise SystemExit('lotto fermato dalle reti 0-2')

# rete 3: divergenza da una resa gia' decisa per lo stesso giapponese (stampa)
gia = {}
for p in glob.glob('dizionario/*.jsonl'):
    nome = p.split('\\')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it') and d.get('jp'):
            gia.setdefault(d['jp'], set()).add((nome, d['riga'], d['it']))

for v in voci:
    resa = RESE[(v['riga'], v['en'])]
    for nome, riga, it in gia.get(v['jp'], ()):
        if it != resa:
            print(f"⚠️ rete 3: riga {v['riga']} jp={v['jp']!r}\n"
                  f"      qui      {resa!r}\n"
                  f"      {nome}:{riga}  {it!r}")

# rete 4: nessun giapponese reso in due modi dentro il lotto
per_jp = collections.defaultdict(set)
for v in voci:
    per_jp[v['jp']].add(RESE[(v['riga'], v['en'])])
for jp, rese in per_jp.items():
    if len(rese) > 1:
        raise SystemExit(f'rete 4: {jp!r} reso in {len(rese)} modi: {rese}')

with io.open(USCITA, 'w', encoding='utf-8', newline='\n') as f:
    for v in voci:
        v['it'] = RESE[(v['riga'], v['en'])]
        f.write(json.dumps(v, ensure_ascii=False) + '\n')

print(f'{len(voci)} voci scritte in {USCITA}')
