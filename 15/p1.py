from input import inp

map, moves = inp('kow')


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
  push = ['@']
  while True:
    xp += xd
    yp += yd
    c = map[yp][xp]
    if c == '#':
      break
    push.append(c)
    if c == '.':
      break
  if push[-1] != '.':
    # print('skip:', m)
    return
  # print('move:', m)
  xp, yp = pos
  map[yp][xp] = '.';
  pos[0] += xd;
  pos[1] += yd
  for p in range(len(push) - 1):
    xp += xd
    yp += yd
    map[yp][xp] = push[p]


for m in moves:
  move_it(m)
  # render()
  # input()

res = 0
for y, line in enumerate(map):
  for x, c in enumerate(line):
    if c == 'O':
      res += 100 * y + x

print('res', res)
