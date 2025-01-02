from itertools import pairwise

from input import inp

map = inp('muuh')
height = len(map)
width = len(map[0])

dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))


def in_bounds(x, y):
  return (0 <= x < width) \
    and (0 <= y < height)


tops = {
  (x, y): set()
  for y, line in enumerate(map)
  for x, char in enumerate(line)
  if char == 9
}


def foo(cur, start):
  cx, cy = cur
  c = map[cy][cx]
  for xd, yd in dirs:
    x, y = cx + xd, cy + yd
    if not in_bounds(x, y):
      continue  # next dir
    if map[y][x] != c + 1:
      continue  # next dir
    next = (x, y)
    if map[y][x] == 9:
      tops[next].add(start)
    else:
      foo(next, start)


for y, line in enumerate(map):
  for x, char in enumerate(line):
    if char == 0:
      start = (x, y)
      foo(start, start)

print('res', sum(len(s) for s in tops.values()))
