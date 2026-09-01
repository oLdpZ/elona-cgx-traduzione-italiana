import collections
import glob
import importlib.util
import io
import json
import re
import unicodedata

RESE = {

    # ---------------------------------------------------------- :47220
    (47220, 'It is said to appear before those who are on the same wavelength. It is not cold, but when you hold it in your hand, you feel an unusual chill down your spine, as if your soul is being grabbed. The pages are all black and translucent, but strange characters appear when reflected in the light. Some believe that they are made of a material that is not of this world, and that they are not books at all, but windows into the abyss.\\n#~Irva Fantasy Encyclopedia~'):
        "Si dice che compaia davanti a chi ha la sua stessa lunghezza d'onda. Freddo non è, eppure a tenerlo in mano la schiena si gela in modo innaturale, e ti prende la sensazione che qualcuno ti stringa l'anima nel pugno. Le pagine sono tutte nere e semitrasparenti, ma alla luce vi affiorano caratteri strani. È fatto di una materia che non è di questo mondo, e c'è chi sostiene che in verità non sia un libro, ma una finestra che riflette l'Abisso.\\n#~Dizionario Fantastico di Irva~",

    # ---------------------------------------------------------- :47222
    (47222, '\\"I was being used.\\" \\n# a Punched-in note'):
        "\\\"Io... ero solo uno strumento\\\" \\n#~Scarabocchio sul Foglietto Infilato Dentro~",

    # ---------------------------------------------------------- :50816
    (50816, 'Recording medium widely circulated in North Tyris. If anything, the volume tends to be more important than the content, you can sell them at shops to raise your fame. \\n# ~Big Book of Books~'):
        "Un supporto di registrazione che a Tyris del Nord circola parecchio. Semmai, più del contenuto tende a contare il volume. A darlo a un negozio, la fama dell'autore salirà. \\n# ~Il Libro dei Libri~",

    # ---------------------------------------------------------- :51150
    (51150, 'A book written by an angler to increase the number of his fishing buddies. He made good use of his waiting time for fishing to write the book. \\n# ~Big Book of Books~'):
        "Un libro che un pescatore ha scritto per farsi più compagni di pesca. Pare che a scriverlo abbia messo a frutto le attese fra un pesce e l'altro. \\n# ~Il Libro dei Libri~",

    # ---------------------------------------------------------- :51221
    (51221, 'A notebook prepared by a concerned father. He was worried about his child and slipped it into their luggage. The notebook was found beside the bulletin board, although it is unclear whether he dropped it, threw it away, or forgot about it. \\n# ~Big Book of Books~'):
        "Un taccuino che un padre aveva preparato. Pare che, in pensiero per il figlio, gliel'avesse infilato di nascosto nei bagagli. Se sia caduto, buttato o dimenticato non si sa: stava lì accanto alla bacheca. \\n# ~Il Libro dei Libri~",

    # ---------------------------------------------------------- :56055
    (56055, "A diary said to have been written by a butler. It is said that inside the diary are more detailed descriptions of the master's life than his own. \\n# ~Big Book of Children's Books~"):
        "Un diario che si dice vergato dal maggiordomo. Dentro, a quanto pare, la vita del padrone è raccontata per filo e per segno più della sua. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :56201
    (56201, 'Report written by the chief developer. They were going to start R&D with this as a starting point, but unfortunately, they did not get the budget. \\n# ~Big Book of Books~'):
        "Un rapporto scritto dall'ingegnere capo. Da qui voleva partire per aprire una ricerca, ma pare che il budget, purtroppo, non sia mai arrivato. \\n# ~Il Libro dei Libri~",

    # ---------------------------------------------------------- :57577
    (57577, "This is a photograph collection of sexy pictures of Lulwy. It is so excessive that the eye is involuntarily drawn to it regardless of one's tastes. The photographer published the book and continued to sell it until it was banned. They later proposed a second volume, but inadvertently offended Lulwy and became food for the sylphs.\\n#~Big Book of Adult Books~"):
        "Un album di foto in cui le immagini sexy di Lulwy sono stipate a non finire. Così spinte che l'occhio ci cade da solo, quali che siano i gusti. Lo pubblicò un fotografo che una volta era riuscito a metterla di buon umore, e si dice che abbia continuato a venderlo finché non fu proibito. Più tardi il fotografo propose un secondo volume, ma le guastò l'umore per sbadataggine e finì in pasto alle silfidi.\\n#~Il Libro dei Libri: le Riviste per Adulti~",

    # ---------------------------------------------------------- :62534
    (62534, 'Notebook of a researcher who was dissatisfied with his institute. It contains the activities of the people around him, along with his complaints. \\n# ~Big Book of Books~'):
        "Il taccuino di un ricercatore che non era contento dell'istituto per cui lavorava. Ci sono annotate le malefatte di chi gli stava intorno, e i lamenti che ne faceva. \\n# ~Il Libro dei Libri~",

    # ---------------------------------------------------------- :71100
    (71100, "A diary written by someone unknown. There is a rumor that an unusual author appears after reading a dozen or more.\\n# ~Big Book of Children's Books~"):
        "Un diario che si dice vergato da qualcuno. Di regola sulla copertina il nome non c'è, e finché non si guarda dentro non si sa di chi sia. Corre voce che, letta una dozzina abbondante di copie, salti fuori un autore raro.\\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :74101
    (74101, 'Diary written by a mad man named Cain. I think it describes the truth he learned at the end of his madness.... \\n# ~Big Book of Books~'):
        "Il diario che <Caim>, impazzito, ha scarabocchiato. Ci sta scritta la verità che in fondo alla sua follia ha conosciuto... o almeno così sembra. \\n# ~Il Libro dei Libri~",

    # ---------------------------------------------------------- :76791
    (76791, "A diary in which one's older sister's secrets are hidden. It is said that things which can never be said with words, are written in the diary, which has caused a stir among researchers. \\n# ~Big Book of Children's Books~"):
        "Un diario in cui la sorella maggiore ha nascosto i suoi segreti. Si dice contenga quelle cose lì che a voce non si dicono mai, e gli studiosi sono in agitazione. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :76935
    (76935, "A diary said to have been written by an older sister. It is said that her hardships and feelings are described in detail in it. \\n# ~Big Book of Children's Books~"):
        "Un diario che si dice vergato dalla sorella maggiore. Dentro, a quanto pare, le sue fatiche e i suoi sentimenti sono raccontati per filo e per segno. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :81064
    (81064, 'A religious book put up by a group of people who are said to be very eccentric. When you open its pages, you will know the truth of the world, and perhaps understand a granfalloon. \\n# ~Big Books of Historical Books~'):
        "Il libro sacro che innalza una congrega ritenuta stranissima. Aprendone le pagine saprai che quel che vi sta scritto è la verità, ed è una menzogna spudorata. \\n# ~Il Libro dei Libri: i Libri di Storia~",

    # ---------------------------------------------------------- :83697
    (83697, 'A precious book that is said to bring back lost beings. Ironically, there was a great war over this book in ancient times, and many lives were lost. \\n#~Big Book of Magical Books~'):
        "Un libro prezioso che si dice richiami indietro chi è andato perduto. Per ironia, nell'antichità intorno a questo libro ci fu una grande guerra, e si dice che molte vite andarono perdute. \\n#~Il Libro dei Libri: i Grimori~",

    # ---------------------------------------------------------- :84233
    (84233, 'This is a book that describes the state of affairs in the town. However, since North Tyris respects freedom, it is said that this book, which describes the system, has become useless. \\n# ~Big Books of Historical Books~'):
        "Un libro in cui è scritto come vanno le cose in città. Siccome però a Tyris del Nord si tiene alla libertà, pare che questo libro, che descrive dei regolamenti, sia diventato un ingombro inutile. \\n# ~Il Libro dei Libri: i Libri di Storia~",

    # ---------------------------------------------------------- :86403
    (86403, "A collection of children's stories by Rachel, a writer of children's stories. The unique warmth of the text and illustrations is said to give readers something that touches their hearts. There are four volumes in total, but they are very hard to find. I am sure there are people in the world who would love to read them. \\n# ~Big Book of Children's Books~"):
        "La raccolta di fiabe che ha fatto Rachel, la scrittrice di favole. Si dice che la scrittura e le illustrazioni, con quel loro calore tutto particolare, diano a chi legge qualcosa che tocca il cuore. I volumi sono quattro in tutto, ma metterli insieme è impresa difficilissima. Al mondo ci sarà di sicuro qualcuno che muore dalla voglia di leggerli. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :89284
    (89284, "A diary said to have been written by a young lady. It is said that inside the diary are detailed descriptions of her glittering life and some of her lovely hobbies. \\n# ~Big Book of Children's Books~"):
        "Un diario che si dice vergato dalla signorina. Dentro, a quanto pare, la sua vita sfavillante e qualcuno dei suoi passatempi graziosi sono raccontati per filo e per segno. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :89356
    (89356, "A diary in which the secrets of a younger sister are hidden. It is said that such and such things that can never be said in words are written in it, and it has caused a stir among researchers. \\n# ~Big Book of Children's Books~"):
        "Un diario in cui la sorella minore ha nascosto i suoi segreti. Si dice contenga quelle cose lì che a voce non si dicono mai, e gli studiosi sono in agitazione. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :89358
    (89358, '\\"Nyo reading!\\" \\n# ~words on the cover~'):
        "\\\"Vietato leggere, miao!\\\" \\n# ~parole sulla copertina~",

# 2 voci, 0 ambigue

    # ---------------------------------------------------------- :93292
    (93292, "Books that can be read to train the skills described in them. In remote villages where there are no schools, these books are said to be a substitute for teachers.\\n# ~Big Book of Books: Teacher's Edition~"):
        "Un libro che, a leggerlo, allena l'abilità di cui parla. Si dice che nei villaggi di confine, dove una scuola non c'è, libri come questo facciano le veci del maestro.\\n# ~Il Libro dei Libri: i Manuali d'Insegnamento~",

    # ---------------------------------------------------------- :97200
    (97200, "A diary written by a younger sister. In it, she writes about her daily feelings, recent favorites, delicious food, etc. in two days' skips. \\n# ~Big Book of Children's Books~"):
        "Il diario che ha scritto la sorella minore. Dentro ci sono le cose che sente giorno per giorno, quel che le piace di questi tempi, i cibi che ha trovato buoni: e scrive saltando due giorni per volta. \\n# ~Il Libro dei Libri: i Libri per Bambini~",

    # ---------------------------------------------------------- :129580
    (129580, 'Recording medium widely circulated in North Tyris. Some of them contain important information, but most of them are just scraps of information that are not worth reading. \\n# ~Big Book of Books~'):
        "Un supporto di registrazione che a Tyris del Nord circola parecchio. Ce n'è qualcuno in cui sta scritto qualcosa d'importante, ma quasi tutti valgono sì e no quanto un appunto a margine. \\n# ~Il Libro dei Libri~",

# 21 voci, 0 ambigue
}
