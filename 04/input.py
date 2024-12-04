__all__ = ['lines']

from os import path

lines = []
with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
  for line in f.readlines():
    lines.append(tuple(line.strip()))

