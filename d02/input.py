__all__ = ['report']

import re
from os import path

report = []
pattern = re.compile(r'^(\d+) +(\d+)$')
with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
    for line in f.readlines():
        report.append(tuple(map(int, line.split())))