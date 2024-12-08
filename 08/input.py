__all__ = ['inp']

from os import path

def inp(f):
  lines = []
  with open(path.join(path.dirname(__file__), f'{f}.txt'), 'r') as f:
    for line in f.readlines():
      lines.append(tuple(line.strip()))
  return lines

