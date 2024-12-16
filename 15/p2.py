from input import inp

map_o, moves = inp('kow')

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


def move_it_lr(m):
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
  map[yp][xp] = '.'
  pos[0] += xd
  pos[1] += yd
  for p in range(len(push) - 1):
    xp += xd
    yp += yd
    map[yp][xp] = push[p]


def move_it_tb(m):
  xd, yd = dirs[m]
  change = []
  next = [pos]
  while len(next) > 0:
    xp, yp = next.pop()
    o = map[yp][xp]
    xp += xd
    yp += yd
    c = map[yp][xp]
    if c == '#':
      # print('skip:', m)
      return
    change.append((o, xp, yp))
    if c == '.':
      continue
    next.append((xp, yp))
    if c == '[':
      next.append((xp + 1, yp))
    elif c == ']':
      next.append((xp - 1, yp))
  # print('move:', m)
  pos[0] += xd
  pos[1] += yd
  for _, xp, yp in change:
    map[yp - yd][xp - xd] = '.'
  for c, xp, yp in change:
    map[yp][xp] = c


def move_it(m):
  return (
    move_it_tb
    if dirs[m][0] == 0
    else move_it_lr
  )(m)


# render()
for m in moves:
  move_it(m)
  # render()
  # input()
  pass

res = 0
for y, line in enumerate(map):
  for x, c in enumerate(line):
    if c == '[':
      res += 100 * y + x

print('res', res)
