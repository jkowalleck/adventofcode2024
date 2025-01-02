import random


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


def calc_xyz(regs):
  res = {}
  for w in ('x', 'y', 'z'):
    res_w = 0
    w_max = max(int(r[1:]) for r in regs if r.startswith(w))
    for wn in range(w_max, 0, -1):
      try:
        if regs[f'{w}{wn:02d}']:
          res_w |= 1 << wn
      except KeyError:
        continue
    res[w] = res_w
  return res


def check_xyz(res):
  return res['z'] == res['x'] + res['y']


o_regs = {}
o_grid = []

init, gates = open('kow.txt').read().split('\n\n')
for i in init.split('\n'):
  r, s = i.split(': ')
  o_regs[r] = s == '1'
for g in gates.split('\n'):
  a, op, b, _, t = g.split(' ')
  o_grid.append((a, b, OPS[op], t))

while True:
  print('.', end='')

  regs = o_regs.copy()
  grid = o_grid.copy()

  random.shuffle(grid)
  s1 = grid.pop()
  s2 = grid.pop()
  s3 = grid.pop()
  s4 = grid.pop()
  s5 = grid.pop()
  s6 = grid.pop()
  s7 = grid.pop()
  s8 = grid.pop()

  grid.append((s1[0], s1[1], s1[2], s2[3]))
  grid.append((s2[0], s2[1], s2[2], s1[3]))
  grid.append((s3[0], s3[1], s3[2], s4[3]))
  grid.append((s4[0], s4[1], s4[2], s3[3]))
  grid.append((s5[0], s5[1], s5[2], s6[3]))
  grid.append((s6[0], s6[1], s6[2], s5[3]))
  grid.append((s7[0], s7[1], s7[2], s8[3]))
  grid.append((s8[0], s8[1], s8[2], s7[3]))

  while gl := len(grid):
    gdone = []
    for gi in range(gl):
      a, b, op, t = grid[gi]
      if t in regs:
        continue
      if a in regs and b in regs:
        regs[t] = op(regs[a], regs[b])
        gdone.append(gi)
    if len(gdone) == 0:
      break  # did not do anything
    for gi in sorted(gdone, reverse=True):
      grid.pop(gi)

  xyz = calc_xyz(regs)
  if check_xyz(xyz):
    print(xyz)
    print(','.join(sorted((s1[3], s2[3], s3[3], s4[3], s5[3], s6[3], s7[3], s8[3]))))
    break
