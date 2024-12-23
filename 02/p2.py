from itertools import pairwise

from input import report

safe = 0
for r in report:
  for ra in (r, *(r[:o] + r[o + 1:] for o in range(len(r)))):
    s = True
    dir = ra[0] - ra[1]
    for l1, l2 in pairwise(ra):
      d = l1 - l2
      s &= (dir < 0) == (d < 0) and (1 <= abs(d) <= 3)
    if s:
      safe += 1
      break

print('safe', safe)
