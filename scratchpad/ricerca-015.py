# -*- coding: utf-8 -*-
"""Le ricerche nel dizionario che servono al lotto 015."""
import glob
import io
import json

voci = []
for p in sorted(glob.glob('dizionario/*.jsonl')):
    nome = p.replace('\\', '/').split('/')[-1]
    for l in io.open(p, encoding='utf-8'):
        if not l.strip():
            continue
        d = json.loads(l)
        if d.get('it'):
            voci.append((nome, d.get('riga'), d.get('jp') or '', d.get('en') or '', d['it']))

DOMANDE = [
    ('ゲージ / power gauge', lambda jp, en, it: 'ゲージ' in jp or 'gauge' in en.lower()),
    ('麻痺 / paralyz', lambda jp, en, it: '麻痺' in jp or 'paraly' in en.lower()),
    ('電磁 / E-Mag', lambda jp, en, it: '電磁' in jp or 'e-mag' in en.lower()),
    ('極 / pole', lambda jp, en, it: 'Ｎ極' in jp or 'Ｓ極' in jp or ' pole' in en.lower()),
    ('願いの女神 / Wish Goddess', lambda jp, en, it: '願い' in jp or 'wish' in en.lower()),
    ('肉体 / body', lambda jp, en, it: '肉体' in jp),
    ('精神 / spirit', lambda jp, en, it: '精神' in jp),
    ('薙ぎ払/斬撃/一撃 (colpi)', lambda jp, en, it: any(x in jp for x in ('薙ぎ払', '斬撃', '一撃', '連続攻撃'))),
    ('砲弾 / cannon', lambda jp, en, it: '砲' in jp or 'cannon' in en.lower()),
    ('粒子 / particle', lambda jp, en, it: '粒子' in jp or 'particle' in en.lower()),
    ('影 / shadow step', lambda jp, en, it: 'shadow' in en.lower() or '影' in jp),
    ('怯んだ / frightened', lambda jp, en, it: 'frighten' in en.lower() or '怯' in jp),
]

for titolo, prova in DOMANDE:
    print('=' * 70)
    print('###', titolo)
    trovate = [v for v in voci if prova(v[2], v[3], v[4])]
    for nome, riga, jp, en, it in trovate[:14]:
        print(f'  {nome}:{riga}  jp={jp[:30]}  en={en[:44]}\n      -> {it[:86]}')
    if len(trovate) > 14:
        print(f'  ... e altre {len(trovate) - 14}')
    if not trovate:
        print('  (niente)')
