from itertools import combinations, chain
from input import inp

"""
field of `emitters`
for each pair of emitters:
  calc the vector betwean them
  antinodes = add that vector ontop of the dif-vector in both sides multiple times
"""

# find al types of all emitters
# fuer jeden emitter-typ: finde ale positions-kombinationen
#   fuer jede der positions-kombinationen: berechne die anti-nodes wie oben benannt
# rule 1: antonodes muessen im feld sein (kein wrap-around, kein oput-of-bounds)
# rule 2: antinodes koenen "auf einander" liegen
# rule 3: antinodes koenen nicht auf der pos von emitter sliegen
# result: anzahl der "unique" positionen von antinodes + "unique" position von emittern

field = inp('sample')
height = len(field)
width = len(field[0])

emitters = {}
for y, l in enumerate(field):
  for x, c in enumerate(l):
    if c != '.':
      if c not in emitters:
        emitters[c] = {(x, y), }
      else:
        emitters[c].add((x, y))


def in_bounds(x, y):
  return (0 <= x < width) \
    and (0 <= y < height)


antinodes = set(chain.from_iterable(e for _, e in emitters.items()))
for et, es in emitters.items():
  for e1, e2 in combinations(es, 2):
    x1, y1 = e1
    x2, y2 = e2
    xd = x1 - x2
    yd = y1 - y2

    for s in (+1, -1):
      _xd = s * xd
      _yd = s * yd
      y = y1
      x = x1
      while in_bounds(x, y):
        antinodes.add((x, y))
        x += _xd
        y += _yd

print('res', len(antinodes))
