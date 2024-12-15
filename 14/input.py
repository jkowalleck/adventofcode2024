__all__ = ['inp']

import re
from os import path

matcher = re.compile(r'^p=(\d+),(\d+) v=([+-]?\d+),([+-]?\d+)$')


def inp(f):
  with open(path.join(path.dirname(__file__), f'{f}.txt'), 'r') as f:
    return tuple(map(
      lambda l: list(map(int, matcher.match(l).groups()))
      , f.read().split('\n')
    ))
