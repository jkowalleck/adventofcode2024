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

init, gates = open('muuh.txt').read().split('\n\n')
for i in init.split('\n'):
  r, s = i.split(': ')
  o_regs[r] = s == '1'
for g in gates.split('\n'):
  a, op, b, _, t = g.split(' ')
  o_grid.append((a, b, OPS[op], t))

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
    a, b = min(a, b), max(a, b)
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


dings1 = set(atree['z21']).difference(atree['z17'])
dings2 = set(atree['z17']).difference(atree['z21'])
pass
for d2 in dings2:
  d2_in_grid = next(g for g in o_grid if g[3] == d2)
  for d1 in dings1:
    d1_in_grid = next(g for g in o_grid if g[3] == d1)
    grid = o_grid.copy()
    grid.remove(d1_in_grid)
    grid.remove(d2_in_grid)
    grid.append((d1_in_grid[0], d1_in_grid[1], d1_in_grid[2], d2_in_grid[3]))
    grid.append((d2_in_grid[0], d2_in_grid[1], d2_in_grid[2], d1_in_grid[3]))
    regs = o_regs.copy()
    run_grid(grid, regs)
    if expected_z_regs['z17'] == regs['z17'] and expected_z_regs['z18'] == regs['z18']:
      print('found')
      print(d1, d2)
