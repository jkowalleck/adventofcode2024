from input import inp

diskmap = inp('kow')
# print('diskmap', diskmap)

disk = []

_fid = 0
for p, l in enumerate(diskmap):
  l = int(l)
  if p % 2:
    _f = '.'
  else:
    _f = _fid
    _fid += 1
  disk.append([_f, l])
# print('disk: ', *(str(df) * dl for df, dl in disk), sep='')

p = len(disk)
while p > 0:
  p -= 1
  # print('disk: ', *(str(df) * dl for df, dl in disk), sep='')
  df, dl = d = disk[p]
  if df == '.':
    continue
  if dl == 0:
    continue
  free = next((fp for fp, fd in enumerate(disk) if fd[0] == '.' and fd[1] >= dl), -1)
  if 0 < free < p:
    disk[free][1] -= dl
    if disk[free][1] == 0:
      disk.pop(free)
    else:
      p += 1
    d[0] = '.'
    disk.insert(free, [df, dl])

checksum = 0
_p = 0
for df, dl in disk:
  if df == '.':
    _p += dl
    continue
  for _ in range(dl):
    checksum += _p * df
    _p += 1
print('checksum', checksum)
