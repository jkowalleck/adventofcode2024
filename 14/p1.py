import re
from functools import reduce
from math import ceil, floor

from input import inp

robots = inp('kow')

width = 101
height = 103

quadrands = (
  ((0, 0), (floor(width / 2) - 1, floor(height / 2) - 1)),
  ((ceil(width / 2), 0), (width - 1, floor(height / 2) - 1)),
  ((0, ceil(height / 2)), (floor(width / 2) - 1, height - 1)),
  ((ceil(width / 2), ceil(height / 2)), (width - 1, height - 1))
)

turns = 100

for _ in range(turns):
  for r in robots:
    px, py, vx, vy = r
    px += vx
    py += vy
    if px < 0:
      px += width
    elif px >= width:
      px -= width
    if py < 0:
      py += height
    elif py >= height:
      py -= height
    r[0], r[1] = px, py

diq = [0, 0, 0, 0]
for q, qd in enumerate(quadrands):
  qxmin, qymin = qd[0]
  qxmax, qymax = qd[1]
  for px, py, *_ in robots:
    if qxmin <= px <= qxmax and qymin <= py <= qymax:
      diq[q] += 1

res = reduce(lambda a, b: a * b, diq, 1)
print('res', res)
