from itertools import pairwise

from input import inp

map = inp('kow')
height = len(map)
width = len(map[0])

dirs = ((0, -1), (1, 0), (0, 1), (-1, 0))


def in_bounds(x, y):
  return (0 <= x < width) \
    and (0 <= y < height)


fieldmap = [[None for _ in range(width)] for _ in range(height)]
fields = []


def foo(cur, known):
  cx, cy = cur
  c = map[cy][cx]
  new = set()
  for xd, yd in dirs:
    x, y = cx + xd, cy + yd
    if not in_bounds(x, y):
      continue  # next dir
    if map[y][x] != c:
      continue  # next dir
    new.add((x, y))
  new_unknown = new.difference(known)
  known |= new
  for n in new_unknown:
    foo(n, known)


seen = set()
fields = []
for y, line in enumerate(map):
  for x, char in enumerate(line):
    cur = (x, y)
    if cur in seen:
      continue
    field = set([cur])
    foo(cur, field)
    fields.append(field)
    seen |= field
print('map', *map, sep='\n')
print('fields', *fields, sep='\n')


# print('fieldmap', *fieldmap, sep='\n')


def get_perim(field):
  perim = 4 * len(field)
  for x, y in field:
    for dx, dy in dirs:
      if (x + dx, y + dy) in field:
        perim -= 1
  return perim


res = 0
for field in fields:
  area = len(field)
  perim = get_perim(field)
  price = area * perim
  res += price
print('res', res)
