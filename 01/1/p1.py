import re

left = []
right = []
dists = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        l, r = re.match(r'^(\d+) +(\d+)$', line).groups()
        left.append(int(l))
        right.append(int(r))

left.sort()
right.sort()


for l, r in zip(left, right):
    dists.append(abs(l - r))

dist = sum(dists)
print('dist', dist)
