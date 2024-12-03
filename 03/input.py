__all__ = ['lines']

from os import path

with open(path.join(path.dirname(__file__), 'input.txt'), 'r') as f:
  lines = f.readlines()
