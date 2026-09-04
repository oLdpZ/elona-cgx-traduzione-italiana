"""Quali toppe dei file riscritti non hanno una «novita'» da cercare.

Sono le toppe che TOLGONO e basta: il cancello della catena le prova al
contrario (la riga di monte non c'e' piu') invece che in avanti.
"""
import json

from strumenti import percorsi
from strumenti.tests.test_toppe import FILE_RISCRITTI, novita_di

for riga in (percorsi.PROGETTO / "toppe.jsonl").read_text(encoding="utf-8").splitlines():
    if not riga.strip():
        continue
    toppa = json.loads(riga)
    if toppa["file"] not in FILE_RISCRITTI:
        continue
    if not isinstance(toppa["sostituisci"], str):
        continue
    if not novita_di(toppa):
        print("%-16s %r" % (toppa["file"], toppa["cerca"].strip()[:90]))
        print("%-16s %r" % ("", toppa["sostituisci"].strip()[:90]))
