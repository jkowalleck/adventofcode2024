import re
from itertools import product

from input import lines

_PATTERN = re.compile(r'(?=XMAS|SAMX)')


def matrix_rotate_45(li, pos):
  lines = len(li)
  cols = len(li[0])
  posm = (lambda l: l) \
    if pos else \
    (lambda l: lines - l - 1)
  dic = {p: [] for p in range(lines + cols - 1)}
  for l, c in product(range(lines), range(cols)):
    dic[l + c].append((l, c))
  for _, poss in dic.items():
    yield tuple(li[posm(l)][c] for l, c in poss)


def matrix_trans(li):
  return zip(*li)


cnt = sum(
  len(_PATTERN.findall('|'.join(''.join(cs) for cs in ls)))
  for ls in (
    lines,  # --
    matrix_trans(lines),  # |
    matrix_rotate_45(lines, True),  # /
    matrix_rotate_45(lines, False),  # \
  )
)
print('cnt', cnt)
