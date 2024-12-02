from input import report
from itertools import pairwise

safe = 0
for r in report:
    s = True
    dir = r[0] - r[1]
    for l1, l2 in pairwise(r):
        d = l1 - l2
        s &= (dir < 0) == (d < 0) and (1 <= abs(d) <= 3)
    if s:
        safe += 1

print('safe', safe)