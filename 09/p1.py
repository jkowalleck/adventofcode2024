from itertools import pairwise

from input import inp

diskmap = inp('kow')
print('diskmap', diskmap)

disk = []

_fid = 0
for p, l in enumerate(diskmap):
  l = int(l)
  if p % 2:
    _f = '.'
  else:
    _f = _fid
    _fid += 1
  for _ in range(l):
    disk.append(_f)
# print('disk: ', *disk, sep='')

p = 0
while p < len(disk):
  while disk[p] == '.':
    disk[p] = disk.pop()
  p += 1

# print('disk: ', *disk, sep='')

checksum = sum(e * f for e, f in enumerate(disk))
print('checksum', checksum)
