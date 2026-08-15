import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {
    # --- :9873-:10005 i quarantatre difetti. Tutti minuscoli, tutti nominali:
    #     ognuno deve reggere dopo il «, ma» di uno qualsiasi dei 45 pregi.
    # ⚠️ errore di monte: il giapponese dice che chi si appassiona non vede piu'
    #    niente intorno, l'inglese che l'entusiasmo lo togli agli altri
    (9873, 'you drain the enthusiasm from those around you.'):
        'la passione fa perdere di vista tutto il resto.',
    (9876, "you are insensitive the other's goodwill."):
        "nessuna sensibilità per l'affetto altrui.",
    (9879, 'you often get caught up in your own delusions.'):
        'una gran brutta tendenza a fantasticare.',
    (9882, 'you look down on others.'):
        'uno sguardo dall\'alto in basso sugli altri.',
    (9885, 'you are in enormous debt.'):
        'un debito enorme sul groppone.',
    (9888, 'you have a strange sense of fashion.'):
        'un gusto strambo nel vestire.',
    (9891, 'your body odor is worrisome.'):
        'un cruccio fisso: il proprio odore.',
    (9894, 'your personality changes when you hold a knife.'):
        'il carattere cambia con una lama in mano.',
    (9897, 'you have experienced major trauma.'):
        'un trauma grosso da qualche parte.',
    (9900, 'you do not trust others.'):
        'nessuna fiducia negli altri.',
    (9903, 'you are surprisingly servile.'):
        'una remissività da far paura.',
    (9906, 'you suffer from a rare disease.'):
        'un male raro addosso.',
    (9909, 'you are cold to those who do not interest you.'):
        'gelo per chi non interessa.',
    (9912, 'you make poor financial decisions.'):
        'nessun senso del denaro.',
    (9915, 'you are not good at socializing.'):
        'poca dimestichezza con la gente.',
    (9918, 'you easily get carried away.'):
        'la testa si monta al primo successo.',
    (9921, 'your sense of taste is odd.'):
        'un palato tutto suo.',
    (9924, 'you are undisciplined in your private life.'):
        'una vita privata sciatta.',
    (9927, 'you make lots of mistakes.'):
        'una certa dose di sbadataggine.',
    # ⚠️ 「肝心なところで」: lo sbaglio arriva quando conta, non sulle cose facili
    (9930, 'you fail at basic things.'):
        'lo sbaglio arriva nel momento decisivo.',
    (9936, 'you act terribly when drunk.'):
        "pessime maniere quando c'è di mezzo il vino.",
    (9939, 'you hate yourself.'):
        'nessuna simpatia per se stessi.',
    (9942, 'you have no confidence in yourself.'):
        'nessuna fiducia in se stessi.',
    (9945, 'you are actually a gigantic pervert.'):
        'in verità, una perversione smisurata.',
    (9948, 'you have no sense of direction.'):
        "nessun senso dell'orientamento.",
    (9951, 'you are in love with money.'):
        'una debolezza per il denaro.',
    (9954, 'you are self-conscious.'):
        'troppa coscienza di sé.',
    (9957, 'your jokes are terrible.'):
        'battute che non fanno ridere nessuno.',
    (9960, 'you are greedy.'):
        'una certa ingordigia.',
    (9963, "you can't draw whatsoever."):
        'disegni da far pietà.',
    (9966, 'you tend to misunderstand people.'):
        'malintesi a ripetizione.',
    (9969, "you don't really have any friends."):
        'nemmeno un amico come si deve.',
    (9975, 'your emotions are easy to read.'):
        'i pensieri si leggono in faccia.',
    # ⚠️ errore di monte: 「周囲からよく誤解される」 e' passivo — sono gli altri a
    #    fraintendere. L'inglese lo gira in attivo e lo confonde con :9966.
    (9978, 'you often misunderstand situations.'):
        'gli altri fraintendono spesso.',
    (9981, "you can't handle insects."):
        'gli insetti fanno ribrezzo.',
    (9984, "you don't have much of a presence."):
        'una presenza che non si nota.',
    (9987, 'you are very prideful.'):
        'un orgoglio smisurato.',
    (9990, 'you love shady things.'):
        'una passione per le cose equivoche.',
    (9993, 'you have a hidden personality.'):
        "un'altra personalità tenuta nascosta.",
    # --- le quattro che in inglese cominciano con la maiuscola: qui no.
    (9996, "You can't read texts longer than five lines."):
        'niente testi più lunghi di cinque righe.',
    (9999, 'You are big foodie.'):
        'una gola notevole.',
    # ⚠️ il giapponese dice facce E nomi, l'inglese solo i nomi
    (10002, "You are bad at remembering other people's names."):
        'facce e nomi degli altri non restano in mente.',
    (10005, "You tend to put off things you don't like."):
        'le cose sgradite finiscono sempre rimandate.',
}
