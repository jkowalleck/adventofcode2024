""""
+---+---+---+
| 7 | 8 | 9 |
+---+---+---+
| 4 | 5 | 6 |
+---+---+---+
| 1 | 2 | 3 |
+---+---+---+
    | 0 | A |
    +---+---+

    +---+---+
    | ^ | A |
+---+---+---+
| < | v | > |
+---+---+---+
"""

A = 'A'
U = '^'
D = 'v'
L = '<'
R = '>'

kp_dirs = {
  (A, A): ('',),
  (U, U): ('',),
  (L, L): ('',),
  (D, D): ('',),
  (R, R): ('',),
  (A, U): (L,),
  (A, R): (D,),
  (A, D): (L + D, D + L),
  (A, L): (D + L + L, L + D + L),
  (U, A): (R,),
  (U, R): (D + R, R + D),
  (U, D): (D,),
  (U, L): (D + L,),
  (L, A): (R + R + U, R + U + R),
  (L, U): (R + U,),
  (L, D): (R,),
  (L, R): (R + R,),
  (D, A): (U + R, R + U),
  (D, U): (U,),
  (D, L): (L,),
  (D, R): (R,),
  (R, A): (U,),
  (R, U): (L + U, U + L),
  (R, L): (L + L,),
  (R, D): (L,),
}

kp_nums_pos = {
  A: (2, 3),
  '0': (1, 3),
  '1': (0, 2),
  '2': (1, 2),
  '3': (2, 2),
  '4': (0, 1),
  '5': (1, 1),
  '6': (2, 1),
  '7': (0, 0),
  '8': (1, 0),
  '9': (2, 0),
}


def kp_ft(f, t):
  tp = kp_nums_pos[t]
  fp = kp_nums_pos[f]
  mx, my = (tp[0] - fp[0]), (tp[1] - fp[1])
  dx = R if mx > 0 else L
  dy = D if my > 0 else U
  if f in ('7', '4', '1') and t in ('0', A):
    return dx * abs(mx) + dy * abs(my)
  if f in ('0', A) and t in ('7', '4', '1'):
    return dy * abs(my) + dx * abs(mx)
  return (dy * abs(my) + dx * abs(mx)) \
    if my > 0 \
    else (dx * abs(mx) + dy * abs(my))


input = """
826A
341A
582A
983A
670A
""".strip().split('\n')

inst_sum = 0
for line in input:
  last_c1 = A
  last_c2 = A
  last_c3 = A
  inst_me = []
  for c1 in line:
    inst_r1 = kp_ft(last_c1, c1) + A
    last_c1 = c1
    for c2 in inst_r1:
      inst_r2 = kp_dirs[(last_c2, c2)][0] + A
      last_c2 = c2
      for c3 in inst_r2:
        inst_r3 = kp_dirs[(last_c3, c3)][0] + A
        last_c3 = c3
        inst_me.append(inst_r3)

  inst_me = ''.join(inst_me)
  inst_sum += int(line[:-1]) * len(inst_me)

print(inst_sum)
