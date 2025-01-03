"""
goal: model a 45bit adder
"""

"""
wie funktioniert binary addition?
0    vom least significant bit: a ^ b = new bit
1-45 next bit: a ^ b ^ carry = new bit
46   most significant bit: carry = new bit

ALLE x und alle y sind gegeben!
"""

'x00 XOR y00 -> z00'
'x00 AND y00 -> z00_carry'
'x01 XOR y01 -> z01_self'
'z01_self XOR z00_carry -> z01'
'x01 AND y01 -> z01_self_carry'
'z01_self_carry OR y01 -> z01_carry'
'z02_self XOR z01_carry -> z02'

"""
x00 XOR y00 -> z00
x00 AND y00 -> 


"""

"""
y00 XOR x00 -> z00
x00 AND y00 -> kkc (z00_carry_out)
y01 XOR x01 -> kjh (z01_self)
kjh XOR kkc -> z01
kjh AND kkc -> jjv (z01_carry_out)
x01 AND y01 -> npn (z01_carry_in)
npn OR  jjv -> jpt (z01_carry)
y02 XOR x02 -> jvk (z02_self)
jpt XOR jvk -> z02
jpt AND jvk -> foo (z02_carry_out)
x02 AND y02 -> bar (z02_carry_in)
foo OR  bar -> baz (z02_carry)
y03 XOR x03 -> lol (z03_self)
baz XOR lol -> z03
"""

i_init, i_grid = open('muuh.txt').read().split('\n\n')
input_regs = ('x', 'y')

rules = dict()
for g in i_grid.split('\n'):
  a, op, b, _, t = g.split(' ')
  rules[t] = (min(a, b), max(a, b), op)
  del a, op, b, _, t
del g

def find_rule_target(value):
  for key, val in rules.items():
    if val == value:
      return key
  return None  # Return None if no matching key is found


"""parse given 
zgroups = dict()
zgroups[0] = [rules['z00']] # a xor b
for z in range(1, 45):
  zn = f'z{z:02d}'
  zp = f'z{z-1:02d}'
  zgroups[zn] = zgroup = [rules[zn]]
  prev_rule = rules[zp]
  prev_rule_carry_out = (prev_rule[0], prev_rule[1], 'AND')
  todo = [rules[zn][0], rules[zn][1]]
  while len(todo):
    t = todo.pop(0)
    r = rules[t]
    zgroup.insert(0, r)
    if r == prev_rule_carry_out:
      continue
    a,b, _ = r
    if a[0] not in input_regs:
      todo.append(a)
    if b[0] not in input_regs:
      todo.append(b)
"""

zgroups = {0: {'value': rules['z00']}}

xp, yp, _ = zgroups[0]['value']
carry_out = (xp, yp, 'AND')
self = ('x01', 'y01', 'XOR')
reg_carry_out = find_rule_target(carry_out)
reg_self = find_rule_target(self)
value = (min(reg_carry_out, reg_self), max(reg_carry_out, reg_self), 'XOR')
zgroups[1] = {'carry_out': carry_out, 'self': self, 'value': value}
for gn, gi in zgroups[1].items():
  if gi not in rules.values():
    print('ERROR', gn, gi)

for gi in range(2, 45):
  gp = gi - 1
  xpr, ypr = f'x{gp:02d}', f'y{gp:02d}'
  xr, yr, zr = f'x{gi:02d}', f'y{gi:02d}', f'z{gi:02d}'
  pvra, pvrb, _ = zgroups[gp]['value']
  carry_out = (pvra, pvrb, 'AND')
  carry_in = (xpr, ypr, 'AND')
  self = (xr, yr, 'XOR')
  reg_carry_out = find_rule_target(carry_out)
  if None is reg_carry_out:
    print('ERROR', carry_out)
  reg_carry_in = find_rule_target(carry_in)
  if None is reg_carry_in:
    print('ERROR', carry_in)
  reg_self = find_rule_target(self)
  if None is reg_self:
    print('ERROR', self)
  carry = (min(reg_carry_in, reg_carry_out), max(reg_carry_in, reg_carry_out), 'OR')
  reg_carry = find_rule_target(carry)
  if None is reg_carry:
    print('ERROR', carry)
  value = (min(reg_self, reg_carry), max(reg_self, reg_carry), 'XOR')
  reg_value = find_rule_target(value)
  if reg_value != zr:
    print('ERROR', reg_value)
  zgroups[gi] = {'carry_out': carry_out, 'carry_in': carry_in, 'carry': carry, 'self': self, 'value': value}