import re

from input import lines

_PATTERN = re.compile(r'(?=XMAS|SAMX)')


# Python3 program for the above approach

# Function to rotate matrix by 45 degree


def matrix_rotate_45(li):
  lines = len(li)
  cols = len(li[0])
  ctr = 0
  while ctr < lines + cols - 1:
    lst = []
    for l in range(lines):
      for c in range(cols):
        if c + l == ctr:
          lst.append(li[l][c])
    yield lst
    ctr += 1


def matrix_rotate_n45(li):
  lines = len(li)
  cols = len(li[0])
  ctr = 0
  while ctr < lines + cols - 1:
    lst = []
    for l in range(lines):
      for c in range(cols):
        if c + l == ctr:
          lst.append(li[lines - l - 1][c])
    yield lst
    ctr += 1


def matrix_trans(li):
  return zip(*li)


cnt = sum(
  len(_PATTERN.findall('|'.join(''.join(cs) for cs in ls)))
  for ls in (
    lines,  # --
    matrix_trans(lines),  # |
    matrix_rotate_45(lines),  # /
    matrix_rotate_n45(lines),  # \
  )
)
print('cnt', cnt)
