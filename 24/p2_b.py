import random
from itertools import pairwise, combinations, chain


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

def run_grid(grid, regs):
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
      raise ValueError # did not do anything - unsolvable
    for gi in sorted(gdone, reverse=True):
      grid.pop(gi)


def reg2int(regs, w):
  res = 0
  w_max = max(int(r[1:]) for r in regs if r.startswith(w))
  for wn in range(w_max, 0 - 1, -1):
    if regs[f'{w}{wn:02d}']:
      res |= 1 << wn
  return res

o_regs = {}
o_grid = []
o_grid_t = {}

init, gates = open('muuh.txt').read().split('\n\n')
for i in init.split('\n'):
  r, s = i.split(': ')
  o_regs[r] = s == '1'
for g in gates.split('\n'):
  a, op, b, _, t = g.split(' ')
  g = [a, b, OPS[op], t]
  o_grid.append(g)
  o_grid_t[t] = g

"""
wie funktioniert binary addition?
0    vom least significant bit: a ^ b = new bit
1-45 next bit: a ^ b ^ carry = new bit
46   most significant bit: carry = new bit

ALLE x und alle y sind gegeben!
"""

init_x = reg2int(o_regs, 'x')
init_y = reg2int(o_regs, 'y')
expected_z = init_x + init_y
# print(f'{init_x:046b}', f'{init_y:046b}', f'{expected_z:046b}', sep='\n')
expected_z_regs = {f'z{w:02d}': v == '1' for w, v in enumerate(f'{expected_z:046b}'[::-1])}


def find_dep_targets(k, grid):
  deps = []
  tree = {g[3]: g for g in grid}
  lfg = [k]
  givens = ('x', 'y')
  while len(lfg):
    l = lfg.pop(0)
    a, b, _, t = tree[l]
    deps.append(t)
    if a[0] not in givens:
      lfg.append(a)
    if b[0] not in givens:
      lfg.append(b)
  return deps

regs = o_regs.copy()
run_grid(o_grid.copy(), regs)

atree = {}
wtree = {}
for zw, zv in expected_z_regs.items():
  atree[zw] = find_dep_targets(zw, o_grid)
  if regs[zw] != zv:
    wtree[zw] = atree[zw]

# used = set(chain.from_iterable(atree.values()))
# unused = set(t for _,_,_,t in o_grid if t not in used)


stree = {}
for wa, wb in pairwise(atree):
  stree[f'{wa}_{wb}'] = set(atree[wb]).difference(atree[wa])


bla = 17
korrekt = set(chain.from_iterable(atree[f'z{w:02d}'] for w in range(bla)))
unused = tuple(set(o_grid_t.keys()).difference(korrekt))
switchers = []

while True:
  print('.', end='')

  switcher = random.choice(wtree[f'z{bla:02d}'])
  switchers.append(switcher)
  for switcher in random.sample(unused, k=7):
    switchers.append(switcher)
  o_grid_t[switchers[0]][3], o_grid_t[switchers[1]][3] = o_grid_t[switchers[1]][3], o_grid_t[switchers[0]][3]
  o_grid_t[switchers[2]][3], o_grid_t[switchers[3]][3] = o_grid_t[switchers[3]][3], o_grid_t[switchers[2]][3]
  o_grid_t[switchers[4]][3], o_grid_t[switchers[5]][3] = o_grid_t[switchers[5]][3], o_grid_t[switchers[4]][3]
  o_grid_t[switchers[6]][3], o_grid_t[switchers[7]][3] = o_grid_t[switchers[7]][3], o_grid_t[switchers[6]][3]

  regs = o_regs.copy()
  try:
    run_grid(o_grid.copy(), regs)
  except ValueError:
    continue

  if reg2int(regs, 'z') == expected_z:
    print('found', switchers)
    break
  else:
    o_grid_t[switchers[0]][3], o_grid_t[switchers[1]][3] = o_grid_t[switchers[1]][3], o_grid_t[switchers[0]][3]
    o_grid_t[switchers[2]][3], o_grid_t[switchers[3]][3] = o_grid_t[switchers[3]][3], o_grid_t[switchers[2]][3]
    o_grid_t[switchers[4]][3], o_grid_t[switchers[5]][3] = o_grid_t[switchers[5]][3], o_grid_t[switchers[4]][3]
    o_grid_t[switchers[6]][3], o_grid_t[switchers[7]][3] = o_grid_t[switchers[7]][3], o_grid_t[switchers[6]][3]
