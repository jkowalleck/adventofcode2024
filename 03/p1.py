from re import compile

from input import lines


_MUL_PATTERN = compile(r'mul\((\d{1,3}),(\d{1,3})\)')

muls = []
for line in lines:
  for a, b in _MUL_PATTERN.findall(line):
    muls.append((int(a), int(b)))

res = sum(a * b for a, b in muls)
print('res', res)
