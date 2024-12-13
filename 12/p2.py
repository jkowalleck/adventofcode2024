
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


def get_sides(field):
  """
  find all north-facing tiles
  group by neighboring
  count group

  repeat with east south west
  """
  sides = 0
  faces = {}
  for d in dirs:
    fs = set()
    for f in field:
      x, y = f[0] + d[0], f[1] + d[1]
      if (x, y) not in field:
        fs.add(f)
    faces[d] = sorted(fs)
  for d, fs in faces.items():
    while len(fs) > 0:
      x, y = fs.pop()
      if d[0] == 0:
        if (x+1, y) not in fs and (x-1, y) not in fs:
          sides += 1
      else:
        if (x, y+1) not in fs and (x, y-1) not in fs:
          sides += 1
  return sides


res = 0
for field in fields:
  area = len(field)
  sides = get_sides(field)
  price = area * sides
  cx, cy = field.pop()
  print(map[cy][cx], area, sides)
  res += price
print('res', res)
