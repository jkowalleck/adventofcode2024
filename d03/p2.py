from re import compile

from input import lines


_INSTR_PATTERN = compile(r"(mul)\((\d{1,3}),(\d{1,3})\)|(do)\(\)|(don't)\(\)")

muls = []
enable = True
for line in lines:
  for mul, a, b, do, dont in _INSTR_PATTERN.findall(line):
    if do:
      enable = True
    elif dont:
      enable = False
    elif mul:
      if enable:
        muls.append((int(a), int(b)))

res = sum(a * b for a, b in muls)
print('res', res)
