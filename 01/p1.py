from input import left, right

dist = sum(abs(l - r) for l, r in zip(sorted(left), sorted(right)))
print('dist', dist)
