from re import compile

from input import lines


_INSTR_PATTERN = compile(r"(mul)\((\d{1,3}),(\d{1,3})\)|(do|don't)\(\)")

muls = []
enable = True
for line in lines:
  for mul, a, b, do in _INSTR_PATTERN.findall(line):
    if do:
      enable = do == 'do'
    elif mul:
      if enable:
        muls.append((int(a), int(b)))

res = sum(a * b for a, b in muls)
print('res', res)
