from input import lines

res = 0

ls = len(lines)
cs = len(lines[0])
for l in range(1, ls -1 ):
  for c in range(1, cs -1):
    if lines[l][c] != 'A':
      continue
    a1, a2, b1, b2 = lines[l - 1][c - 1], lines[l + 1][c + 1], lines[l - 1][c + 1], lines[l + 1][c - 1]
    if (
      (a1 == 'M' and a2 == 'S')  # \ MAS
      or
      (a1 == 'S' and a2 == 'M')  # \ SAM
    ) and (
      (b1 == 'M' and b2 == 'S')  # / MAS
      or
      (b1 == 'S' and b2 == 'M')  # / SAM
    ):
      res += 1
print('res', res)
