import re

left = []
right = []
dists = []

with open('input.txt', 'r') as f:
    for line in f.readlines():
        l, r = re.match(r'^(\d+) +(\d+)$', line).groups()
        left.append(int(l))
        right.append(int(r))

for l in left:
    dists.append(l * right.count(l))

dist = sum(dists)
print('dist', dist)
