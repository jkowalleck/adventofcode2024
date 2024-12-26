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
  if f[0] != 't':
    continue
  for c1, c2 in combinations(ts, 2):
    if c1 in cons[c2]:
      groups.add(tuple(sorted([f, c1, c2])))

print('res', len(groups))
