__all__ = ['inp']

from os import path

def inp(f):
  with open(path.join(path.dirname(__file__), f'{f}.txt'), 'r') as f:
    for line in f.readlines():
      return line.strip()

