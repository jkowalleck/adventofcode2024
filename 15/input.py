__all__ = ['inp']

from os import path


def inp(f):
  with open(path.join(path.dirname(__file__), f'{f}.txt'), 'r') as f:
    map, moves = f.read().split('\n\n')
    return [list(l) for l in map.split('\n')] \
      , moves.replace('\n', '')
