from itertools import combinations

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
del a, b, con

groups = set()
for f, ts in cons.items():
  for n in range(len(ts) + 1, 3, -1):
    found = False
    for kn in combinations(ts, n - 1):
      k = {f, *kn}
      if all(n == len({i, *cons[i]} & k) for i in kn):
        groups.add(tuple(sorted(k)))
        found = True
        break
    if found:
      break

longest = max(groups, key=len)
print('res', ','.join(longest))
