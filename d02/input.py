__all__ = ['report']

from os import path

report = []
with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
  for line in f.readlines():
    report.append(tuple(map(int, line.split())))
