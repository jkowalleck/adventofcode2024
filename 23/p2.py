from itertools import chain, pairwise, combinations

cons = {}

for con in open('sample.txt').read().split('\n'):
  a, b = con.split('-')
  if a in cons:
    cons[a].add(b)
  else:
    cons[a] = {b, }
  if b in cons:
    cons[b].add(a)
  else:
    cons[b] = {a, }
del a, b

groups = set()
for f, ts in cons.items():
  g = {f, *ts}
  for t in ts:
    g &= {t, *cons[t]}
  groups.add(tuple(sorted(g)))

print('res', groups)
