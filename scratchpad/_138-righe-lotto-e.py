"""Stampa in `repr` le righe esatte che il lotto E deve toppare."""
from strumenti import percorsi

BERSAGLI = {
    "tcg_skill.hsp": (602, 930, 931, 1214, 4246, 6208, 6230, 6234, 6237, 6241,
                      6245),
    "tcg.hsp": (4558, 4632, 4633, 4634, 4635, 4636, 4637, 4638, 4641, 4642,
                4643, 4644, 4645, 4646, 4647, 4648, 4651, 4652, 4653, 4654,
                4655, 4656, 4657, 4658),
}

for nome, numeri in BERSAGLI.items():
    righe = (percorsi.SORGENTE_HSP / nome).read_bytes().decode("cp932").split("\r\n")
    print("=" * 70)
    print(nome)
    for numero in numeri:
        print("%5d %r" % (numero, righe[numero - 1]))
