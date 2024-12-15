from input import inp

robots = inp('kow')

width = 101
height = 103

turns = 0


def field():
  f = [['.' for _ in range(width)] for _ in range(height)]
  for r in robots:
    x, y, *_ = r
    f[y][x] = '#'
  return f


def render(f, tt):
  tw = 20
  th = 30
  x, y = tt
  print('T: ', turns, 'x', x, 'y', y)
  try:
    for ry in range(y-5, y + th):
      for rx in range(x - tw, x + tw):
        print(f[ry][rx], end='')
      print()
  except IndexError:
    pass
  print()


def is_tree(f):
  """search:
  ..#..
  .###.
  #####
  """
  for y, l in enumerate(f):
    for x, c in enumerate(l):
      try:
        if '#' == c \
          == f[y + 1][x - 1] == f[y + 1][x] == f[y + 1][x + 1] \
          == f[y + 2][x - 2] == f[y + 2][x - 1] == f[y + 2][x] == f[y + 2][x + 1] == f[y + 2][x + 2] \
          == f[y + 3][x - 3] == f[y + 3][x - 2] == f[y + 3][x - 1] == f[y + 3][x] == f[y + 3][x + 1] == f[y + 3][
          x + 2] == f[y + 3][x + 3] \
          :
          return x, y
      except IndexError:
        pass
  return None

tt = None
while tt is None:
  turns += 1
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
  f = field()
  if tt := is_tree(f):
    render(f, tt)

print('turns', turns)
