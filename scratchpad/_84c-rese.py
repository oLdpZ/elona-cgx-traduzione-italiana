# -*- coding: utf-8 -*-
"""Le rese di SILVIA la principessa (84a): chat.hsp :6308-:6445, zona chiusa.

La vicenda della principessa decaduta: tre gradini di carisma (100, 150, 200)
e un amante immaginario che si chiama Eurypides.

Il lessico stava nel DIARIO di questo stesso incarico, gia' reso per intero:

    text.hsp:10627   «la principessa <Silvia>», «Locanda del Fumo e della
                      Pipa», «un uomo affascinante», «carisma»
    text.hsp:10635   il secondo gradino
    text.hsp:10643   il terzo: «non distingue piu' una persona dall'altra»
    text.hsp:10833   il titolo: «Compagnia per la principessa»

⭐ Il TRE VOLTE 「えっ。」 di monte e' un caso da leggere prima di tradurre: la
stessa identica esclamazione giapponese sta a `:6341`, `:6382` e `:6423`, e
l'inglese la rende in tre modi diversi — «Hmph.», «Forget it...?», «Huh?».
Sono tre firme distinte, e vanno rese diverse: l'inglese sta interpretando il
contesto, non traducendo il suono.

💡 E `:6382` e' l'ECO della voce di menu `:6378` («Forget it.»): Silvia ripete
la scelta del giocatore. Le due rese si scrivono insieme — «Lascia perdere» /
«Lascia perdere...?» — come `:7463`/`:7484` nel lotto di Lune.

⚠️ Le trappole del genere, qui, sono TRE e su due bersagli diversi:
  - `:6347` «You're absolutely useless» parla del GIOCATORE: «buono a nulla»
    e' un aggettivo maschile, e diventa «non servi proprio a niente»;
  - `:6352` parla del COMPAGNO che il giocatore ha portato (`rc`), di cui il
    codice controlla solo `sdata(SKILL_ATTR_CHA, rc)`: puo' essere chiunque, e
    «Che bruttezza!» regge senza accordo dove «quanto e' brutto» no.
  - `:6393` invece l'accordo lo FA, ed e' giusto: «Eurypides non e' brutto
    cosi'» si accorda con Eurypides, che e' l'uomo immaginario di Silvia. Dove
    il codice nomina il personaggio, l'accordo si fa.

⚠️ `:6377` «I have him» dice «him» perche' l'incarico chiede un uomo, ma il
codice guarda solo `sdata(SKILL_ATTR_CHA, rc)`: si porta chi si vuole. La resa
non nomina il genere.
"""
import io, json, sys

# chiave: (riga, inglese) — perche' :6312 porta DUE lang() sulla stessa riga
RESE = {
    # --- il finale: la principessa che non riconosce piu' nessuno ---
    (6311, "Oh... Eurypides, what have you done to me?! My body aches without your touch. I can't stand it anymore!"):
        'Ah... Eurypides, che cosa mi hai fatto?! Il corpo mi brucia se non mi '
        'tocchi. Non resisto più!',
    (6312, 'I want to become one with you...'):
        'Voglio diventare una cosa sola con te...',
    (6312, 'Stop!'):
        'Smettila!',

    # --- il primo gradino: carisma 100 ---
    (6317, 'As you wish.'): 'Ai tuoi ordini',
    (6318, 'What about me?'): 'E io non vado bene?',
    (6319, 'Get a hold of yourself!'): 'Datti un contegno!',
    (6320, "The men around here can't satisfy me anymore! Bring me an absolutely stunning man!"):
        'Gli uomini di queste parti non mi bastano più! Portami un uomo '
        'davvero affascinante!',
    (6323, "I don't know why I expected anything out of you in the first place!"):
        'Ma figurati se potevo aspettarmi qualcosa da te!',
    (6327, "...Sorry, but you're not my type."):
        '...Mi dispiace, ma non sei il mio tipo.',
    (6331, 'Great. Get it done quickly. I hate to be kept waiting!'):
        'Ecco una buona risposta. Sbrigati, però: detesto aspettare!',

    # --- la consegna del primo ---
    (6336, 'Of course.'): 'Ma certo',
    (6337, 'Forget it.'): 'Lascia perdere',
    (6338, "You've brought someone, right?"): "L'avrai portato, spero?",
    (6341, 'Hmph.'): 'Uff.',
    (6347, "You're too slow. You're absolutely useless."):
        'Quanto ci metti. Non servi proprio a niente.',
    (6352, "I don't want an ugly oaf like this!"):
        'Che bruttezza! Non se ne parla proprio!',
    (6360, "You knew just what I wanted! I'll have to ask you again sometime."):
        'Vedo che hai capito i miei gusti! Potrei chiedertelo di nuovo, un giorno.',

    # --- il secondo gradino: carisma 150 ---
    (6377, 'I have him.'): 'Ecco chi ti ho portato',
    (6379, 'Eurypides is still not here? Hurry up and bring him!'):
        'Eurypides non è ancora qui? Sbrigati a portarmelo!',
    (6382, 'Forget it...?'): 'Lascia perdere...?',
    (6388, 'Hurry up and bring him to me you fool!'):
        'Muoviti a portarmelo, idiota!',
    (6393, 'I wanted to meet... Eurypides, not an ugly pig like this!'):
        'Ti ho aspettato... ma Eurypides non è brutto così!',
    (6401, 'Fufu... Eurypides... I love you...'):
        'Fufu... Eurypides... ti amo...',

    # --- il terzo gradino: carisma 200, ed e' il giocatore ---
    (6418, 'I am Eurypides.'): 'Eurypides sono io',
    (6419, "That's just creepy."): 'Che cosa inquietante',
    (6420, 'Oh... Eurypides... Eurypides, where have you gone? I am nothing without you...'):
        'Ah... Eurypides... Eurypides, dove sei finito? Senza di te non sono '
        'niente...',
    (6423, 'Huh?'): 'Eh?',
    (6427, 'I love you, Eurypides... Wait, who the hell are you?!'):
        'Ti amo, Eurypides... Ma un momento, tu chi diavolo sei?!',
    (6430, "Fufu... Eurypides... Let's have some fun..."):
        'Fufu... Eurypides... facciamo qualcosa di bello...',
}

LOTTO = 'lavoro/84-chat-silvia.jsonl'

voci = [json.loads(l) for l in io.open(LOTTO, encoding='utf-8') if l.strip()]
chiavi = {(v['riga'], v['en']) for v in voci}
mancanti = [k for k in chiavi if k not in RESE]
in_piu = [k for k in RESE if k not in chiavi]
if mancanti or in_piu:
    for k in mancanti:
        print('mancante: %s' % (k,))
    for k in in_piu:
        print('in piu\' : %s' % (k,))
    sys.exit(1)

with io.open(LOTTO, 'w', encoding='utf-8', newline='\n') as fh:
    for v in voci:
        v['it'] = RESE[(v['riga'], v['en'])]
        fh.write(json.dumps(v, ensure_ascii=False) + '\n')
print('%d rese scritte in %s' % (len(voci), LOTTO))
