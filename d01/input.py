__all__ = ['left', 'right']

import re
from os import path

left = []
right = []

pattern = re.compile(r'^(\d+) +(\d+)$')
with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
    for line in f.readlines():
        l, r = pattern.match(line).groups()
        left.append(int(l))
        right.append(int(r))