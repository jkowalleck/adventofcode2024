from itertools import pairwise

from input import inp

mace = inp('kow')

start = (-1, -1)
for y, line in enumerate(mace):
  for x, char in enumerate(line):
    if char == 'S':
      start = (x, y)

dirs = (
  # start facing east
  (1, 0),
  (0, 1),
  (-1, 0),
  (0, -1),
)

dir_arrow = '>V<^'

def get_waylen(way):
  l = len(way) + ( 1000 if way[0][0] != 0 else 0)
  for s1, s2 in pairwise(way):
    if s1[0] != s2[0]:
      l += 1000
  return l

def render(way, waylen):
  f = [list(l) for l in mace]
  for d, p in way:
    px, py = p
    f[py][px] = dir_arrow[d]
  for l in f:
    print(*l, sep='')
  print('waylen', waylen)

ways2E = set()
def solve_mace():
  way = [[-1, start]]
  while len(way):
    s = way[-1]
    s[0] += 1
    d, p = s
    if d > 3:
      way.pop()
      continue
    dx, dy = dirs[d]
    px, py = p
    nx, ny = n = px + dx, py + dy
    nc = mace[ny][nx]
    if nc == '#':
      continue  # wall
    if nc == 'S':
      continue  # circle
    if any(p == n for _, p in way):
      continue  # circle
    if nc == 'E':
      ways2E.add(tuple(map(tuple, way)))
      way.pop()
      continue
    way.append([-1, n])

solve_mace()

waylens = []
for way in ways2E:
  waylen = get_waylen(way)
  render(way, waylen)
  waylens.append(waylen)

res = min(*waylens)
print('res', res)
