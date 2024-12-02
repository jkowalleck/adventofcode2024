from input import left, right

dist = sum(l * right.count(l) for l in left)
print('dist', dist)
