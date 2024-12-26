
cons = {}

print(cons)

for con in open('sample.txt').read().split('\n'):
  a, b = con.split('-')
  if a in cons:
    cons[a].append(b)
  else:
    cons[a] = [b]
  if b in cons:
    cons[a].append(b)
  else:
    cons[b] = [a]


