import re

from input import lines

_PATTERN = re.compile(r'(?=XMAS|SAMX)')


def matrix_rotate_45(li, pos):
  lines = len(li)
  cols = len(li[0])
  posm = (lambda l: l) \
    if pos else \
    (lambda l: lines - l - 1)
  ctr = 0
  while ctr < lines + cols - 1:
    yield tuple(
      li[posm(l)][c]
      for l in range(lines)
      for c in range(cols)
      if c + l == ctr
    )
    ctr += 1


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
