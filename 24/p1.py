def g_and(a, b):
  if a is None or b is None:
    return None
  return a & b


def g_or(a, b):
  if a is None or b is None:
    return None
  return a | b


def g_xor(a, b):
  if a is None or b is None:
    return None
  return a ^ b


OPS = {
  'AND': g_and,
  'OR': g_or,
  'XOR': g_xor,
}

regs = {}
grid = []

init, gates = open('muuh.txt').read().split('\n\n')
for i in init.split('\n'):
  r, s = i.split(': ')
  regs[r] = s == '1'
for g in gates.split('\n'):
  a, op, b, _, t = g.split(' ')
  grid.append((a, b, OPS[op], t))

while len(grid):
  g = grid.pop(0)
  a, b, op, t = g
  if t in regs:
    continue
  if a in regs and b in regs:
    regs[t] = op(regs[a], regs[b])
  else:
    grid.append(g)

res = 0
z_max = max(int(r[1:]) for r in regs if r.startswith('z'))
for z in range(z_max, 0, -1):
  if regs[f'z{z:02d}']:
    res |= 1 << z

print(res)
