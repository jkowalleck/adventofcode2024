import astar

from input import inp

width = 71
height = 71
mcnt = 1024

# region build maze

field = [['.' for x in range(width)] for y in range(height)]
for m in inp('kow')[:mcnt]:
  mx, my = map(int, m.split(','))
  field[my][mx] = '#'

# endregion build maze

start = (0, 0)
goal = (width - 1, height - 1)

dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))

def neighbors_fnct(pos):
  x, y = pos
  for dx, dy in dirs:
    nx, ny = x + dx, y + dy
    if (
      0 <= nx < width and 0 <= ny < height
      and field[ny][nx] == '.'
    ):
      yield (nx, ny)


solved = list(astar.find_path(
  start=start,
  goal=goal,
  neighbors_fnct=neighbors_fnct,
))
print('steps:', len(solved)-1)
