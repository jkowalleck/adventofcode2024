from input import inp

map_o, moves = inp('sample')

map = []
for line_o in map_o:
  line = []
  map.append(line)
  for c in line_o:
    if c == '#':
      line.append(c)
      line.append(c)
    elif c == 'O':
      line.append('[')
      line.append(']')
    elif c == '.':
      line.append(c)
      line.append(c)
    elif c == '@':
      line.append(c)
      line.append('.')

def render():
  for line in map:
    print(*line, sep='')
  print()


def find_robot():
  for y, line in enumerate(map):
    for x, c in enumerate(line):
      if c == '@':
        return x, y


pos = list(find_robot())

dirs = {
  '^': (0, -1),
  '>': (1, 0),
  'v': (0, 1),
  '<': (-1, 0),
}


def move_it(m):
  xd, yd = dirs[m]
  xp, yp = pos
  # TODO


render()
for m in moves:
  move_it(m)
  # render()
  # input()
  pass

res = 0
for y, line in enumerate(map):
  for x, c in enumerate(line):
    if c == 'O':
      res += 100 * y + x

print('res', res)
