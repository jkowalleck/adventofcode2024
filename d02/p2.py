from input import report
from itertools import pairwise

safe = 0
for r in report:
    for ra in (r, *(r[:o] + r[o+1:] for o in range(len(r)))):
        dir = ra[0] - ra[1]
        s = True
        for l1, l2 in pairwise(ra):
            d = l1 - l2
            s &= (dir < 0) == (d < 0) and (1 <= abs(d) <= 3)
        if s:
            safe += 1
            break

print('safe', safe)