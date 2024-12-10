from itertools import pairwise

from input import inp

map = inp('kow')
height = len(map)
width = len(map[0])

dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))


def in_bounds(x, y):
  return (0 <= x < width) \
    and (0 <= y < height)


tops = {
  (x, y): 0
  for y, line in enumerate(map)
  for x, char in enumerate(line)
  if char == 9
}


def foo(cx, cy):
  c = map[cy][cx]
  for xd, yd in dirs:
    x, y = cx + xd, cy + yd
    if not in_bounds(x, y):
      continue  # next dir
    if map[y][x] != c + 1:
      continue  # next dir
    if map[y][x] == 9:
      tops[(x, y)] += 1
    else:
      foo(x, y)


for y, line in enumerate(map):
  for x, char in enumerate(line):
    if char == 0:
      foo(x, y)

print('res', sum(tops.values()))
