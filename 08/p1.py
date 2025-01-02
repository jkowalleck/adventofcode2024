from itertools import combinations
from input import inp

"""
field of `emitters`
for each pair of emitters:
  calc the vector betwean them
  antinodes = add that vector ontop of the dif-vector in both sides
"""

# find al types of all emitters
# fuer jeden emitter-typ: finde ale positions-kombinationen
#   fuer jede der positions-kombinationen: berechne die anti-nodes wie oben benannt
# rule 1: antonodes muessen im feld sein (kein wrap-around, kein oput-of-bounds)
# rule 2: antinodes koenen "auf einander" liegen
# rule 3: antinodes koenen auf der pos von emitter sliegen
# result: anzahl der "unique" positionen von antinodes

field = inp('muuh')
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

antinodes = set()
for et, es in emitters.items():
  for e1, e2 in combinations(es, 2):
    x1, y1 = e1
    x2, y2 = e2
    xd = x1 - x2
    yd = y1 - y2
    a1 = (x1 + xd, y1 + yd)
    a2 = (x1 - xd, y1 - yd)
    a3 = (x2 + xd, y2 + yd)
    a4 = (x2 - xd, y2 - yd)
    for a in (a1, a2, a3, a4):
      if (
        a not in (e1, e2)  # not emitter
        and (0 <= a[0] < width and 0 <= a[1] < height)  # not out of bounds
      ):
        antinodes.add(a)

print('res', len(antinodes))
