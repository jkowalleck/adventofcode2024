from itertools import chain, pairwise, combinations

cons = {}

for con in open('kow.txt').read().split('\n'):
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
  for n in range(len(ts), 2, -1):
    found = False
    for kn in combinations(ts, n):
      k = {f, *kn}
      if all(n + 1 == len({i, *cons[i]} & k) for i in kn):
        groups.add(tuple(sorted(k)))
        found = True
        break
    if found:
      break

print('res', ','.join(sorted(max(groups, key=len))))
