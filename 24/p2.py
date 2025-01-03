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

"""
sample run
y00 XOR x00 -> z00 (z02_value)
x00 AND y00 -> kkc (z00_carry_out)
y01 XOR x01 -> kjh (z01_self)
kjh XOR kkc -> z01 (z02_value)
kjh AND kkc -> jjv (z01_carry_out)
x01 AND y01 -> npn (z01_carry_in)
npn OR  jjv -> jpt (z01_carry)
y02 XOR x02 -> jvk (z02_self)
jpt XOR jvk -> z02 (z02_value)
jpt AND jvk -> foo (z02_carry_out)
x02 AND y02 -> bar (z02_carry_in)
foo OR  bar -> baz (z02_carry)
y03 XOR x03 -> lol (z03_self)
baz XOR lol -> z03 (z02_value)
"""

i_init, i_grid = open('kow.txt').read().split('\n\n')
input_regs = ('x', 'y')

rules = dict()
for g in i_grid.split('\n'):
  a, op, b, _, t = g.split(' ')
  rules[t] = (min(a, b), max(a, b), op)
  del a, op, b, _, t
del g


def find_rule_target(rule):
  for t, r in rules.items():
    if rule == r:
      return t
  return None


zgroups = {0: {'value': rules['z00']}}

pvra, pvrb, _ = zgroups[0]['value']
carry_out = (pvra, pvrb, 'AND')
self = ('x01', 'y01', 'XOR')
reg_carry_out = find_rule_target(carry_out)
reg_self = find_rule_target(self)
value = (min(reg_carry_out, reg_self), max(reg_carry_out, reg_self), 'XOR')
zgroups[1] = {
  'carry_out': carry_out,
  'self': self,
  'value': value
}
for gn, gi in zgroups[1].items():
  if gi not in rules.values():
    print('ERROR', gn, gi)
    raise ValueError()
del gn, gi

switches = set()

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
    raise Exception('not implemented')
  reg_carry_in = find_rule_target(carry_in)
  if None is reg_carry_in:
    print('ERROR', carry_in)
    raise Exception('not implemented')
  reg_self = find_rule_target(self)
  if None is reg_self:
    print('ERROR', self)
    raise Exception('not implemented')
  carry = (min(reg_carry_in, reg_carry_out), max(reg_carry_in, reg_carry_out), 'OR')
  reg_carry = find_rule_target(carry)
  if None is reg_carry:
    print('ERROR', carry)
    raise Exception('not implemented')
  value = (min(reg_self, reg_carry), max(reg_self, reg_carry), 'XOR')
  reg_value = find_rule_target(value)
  if None is reg_value:
    a, b, op = value = rules[zr]
    assert op == 'XOR'
    sa, sb = min(reg_self, reg_carry), max(reg_self, reg_carry)
    if sa != a:
      print('switch', a, sa)
      switches.update((a, sa))
      rules[a], rules[sa] = rules[sa], rules[a]
    if sb != b:
      print('switch', b, sb)
      switches.update((b, sb))
      rules[b], rules[sb] = rules[sb], rules[b]
  elif reg_value != zr:
    print('switch', reg_value, zr)
    switches.update((reg_value, zr))
    rules[reg_value], rules[zr] = rules[zr], rules[reg_value]
  zgroups[gi] = {
    'carry_out': carry_out,
    'carry_in': carry_in,
    'carry': carry,
    'self': self,
    'value': value
  }

print('res', ','.join(sorted(switches)))
