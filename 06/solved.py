import os
from enum import Enum
import math

i = open('../input.txt').read()


class Direction(Enum):
  U = '^'
  R = '>'
  D = 'v'
  L = '<'


width = len(i.splitlines()[0])
height = len(i.splitlines())
checkfield = i.replace('\n', '')

field = []
for line in i.splitlines():
  field.append(list(line))

step_forward = {
  Direction.U: lambda x, y: (x, y - 1),
  Direction.R: lambda x, y: (x + 1, y),
  Direction.D: lambda x, y: (x, y + 1),
  Direction.L: lambda x, y: (x - 1, y)
}


def render(field):
  os.system('clear')
  for line in field:
    print(*line, sep='', end='\n')


rot = {
  Direction.U: Direction.R,
  Direction.R: Direction.D,
  Direction.D: Direction.L,
  Direction.L: Direction.U
}

blockades = ('#', 'O')

def find_loop(field, x, y, d):
  visited = set()
  while True:
    visited.add((x, y, d))

    # input()
    # render(field)
    sx, sy = step_forward[d](x, y)

    if sx < 0 or sy < 0 or sx >= width or sy >= height:
      field[y][x] = 'X'
      # render(field)
      return False, visited

    field[y][x] = 'X'

    while field[sy][sx] in blockades:
      d = rot[d]
      sx, sy = step_forward[d](x, y)

    x, y = sx, sy

    field[y][x] = d.value
    if (x, y, d) in visited:
      return True, visited


y = math.floor(checkfield.index('^') / width)
x = checkfield.index('^') % width
d = Direction(field[y][x])

total = 0
newfield = [l[::] for l in field]
_, pathmap = find_loop(newfield, x, y, d)
pathmap = {(x[0], x[1]) for x in pathmap}
print('soviele: ', len(pathmap))
for j, i in pathmap:
  if field[i][j] != '#':
    newfield = [l[::] for l in field]
    newfield[i][j] = 'O'
    if find_loop(newfield, x, y, d)[0]:
      total += 1

print(total)
